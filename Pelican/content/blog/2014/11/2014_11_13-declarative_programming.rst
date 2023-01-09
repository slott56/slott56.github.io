Declarative Programming
=======================

:date: 2014-11-13 08:00
:tags: imperative,declarative,functional programming,#python
:slug: 2014_11_13-declarative_programming
:category: Technologies
:status: published

| I know that some folks swear by declarative programming. They like the
  ideas behind `ant <http://ant.apache.org/>`__ (and
  `make <http://www.gnu.org/software/make/>`__) and
  `SCons <http://www.scons.org/>`__ and related examples.
| You can google for "ant v. maven v. gradle" where people gripe about
  which is more declarative. The point of the whining being that more
  declarative == good and any traces of procedural or imperative
  programming == bad.
| All, of course, without any really good justification of why
  declarative is better. It's assumed that declarative simply has
  innumerable advantages. And yes, I've started
  with http://en.wikipedia.org/wiki/Declarative_programming. The issue
  isn't simply moot; the justification is weak.
| Perhaps there's a awful bias toward imperative and functional
  programming. After all, the big thinkers in computer science tend to
  favor the imperative and functional schools of thought. Maybe
  declarative suffers from some bias.
| Or maybe declarative has limited utility.
| There. I said it. Limited utility.
| I think a functional approach might be better, faster and simpler.
| **Side-bar Ranting**
| The code is below. You can skip down to the "*The Functional Build
  System*" section and not miss much.
| Declarative programming seems applicable to the cases where the
  ordering of operations can be easily deduced. It seems like the
  significant value of declarative programming is to rely on an
  optimizing compiler rearrange the declarations into properly-ordered
  imperative steps. From this viewpoint, it seems like ant/maven/gradle
  are optimizers that look at the dependencies among transformation
  functions and then apply the functions in the proper order.
| It seems like we're writing expressions like these:
| x.class = java(x.java)
| xyz.jar = jar(x.class, y.class, z.class, ... )
| app.war = war(xyz.jar, abc.jar, ... )
| and then turning them over to a clever compiler (like Haskell) to work
  out a total order among the expressions that will build the right
  thing for us.
| There's a *potential* difference between manually structuring a script
  to get all of the steps in order and allowing the compiler to arrange
  things properly based on some formal semantics behind each expression.
| It's a *potential* difference because most folks that deal with
  ant/maven/gradle tend to put things in more-or-less the right order so
  that others can figure out what the hell is going on. In the trivial
  cases where we're building simple web sites, the default rules have
  evolved to the point where they work in almost all cases, so we don't
  even look at the configuration of the tools. We hit Ctrl+B knowing
  that it's all setup properly
| **Some Requirements**
| A number of applications have ant-like (or make-like) aspects but
  don't really cry out for ant with customized actions. We might be
  doing data warehouse loads which involve an ant-like sequence of
  processing steps to do transformations, loads, and produce final
  summaries and confirmations. We can, of course, write this all in
  first-class Java code. The hard way.
| It's not terribly complex. A class to define a dependency. A suite of
  plug-in strategies. Some static definitions of the actual rules. Been
  there. Done that.
| Pragmatically, the declarative style suffers from a limitation of
  being rather rigid in applying a fixed set of rules. A more
  script-like implementation can be more helpful to support reruns,
  debugging, problem-solving and the inevitable special cases and
  exceptions. After a storage failure -- and the reruns required to get
  the warehouse back up-to-date -- one sees more need for script-like
  flexibility and less need for overly simplistic rigidity.
| Another end of the spectrum is individual steps all manually
  coordinated with a tool like BMC's Control-M. This requires endless
  manual intervention to make sure all the various tasks are defined
  properly in Control-M.
| Somewhere near the middle is a configurable application with some
  processing rules to give it flexibility. But some defined structure to
  remove the need for carefully planned manual intervention and deep
  expertise.
| **The Functional Build System**
| We can image an ant-like build system defined functionally.
| The core is a function that implements build-if-needed rules:

::

   def build_if_needed( builder, target_file, *source ):
       if target_ok( target_file, *source ):
           return "ok({0},...)".format(target_file)
       builder( target_file, *source )
       return "{0}({1},...)".format(builder.__class__.__name__,target_file)

| 
| We can use this function to define the essential dependency: use a
  builder function to create some target if it's out-of-date with
  respect to the sources. The return value forms a kind of audit log.
| This relies on some helper functions: target_ok() checks the
  modification times of files. The various builders do the various kinds
  of operations required to make one from the sources.
| Here's the target_ok() function

::

   def target_ok( target_file, *source_list, logger=logging ):
       try:
           mtime_target= datetime.datetime.fromtimestamp(
               os.path.getmtime( target_file ) )
       except Exception:
           return False
       # If a source doesn't exist, we throw an exception.
       times = (datetime.datetime.fromtimestamp(
               os.path.getmtime( source ) ) for source in source_list)
       return all(mtime_target > mtime_source for mtime_source in times)

| 
| I think this function is what started me thinking about a functional
  approach. It could be a method of a class. But. It's seems like a very
  functional design. It could be reduced to a single (long) expression.
| The builders are composite functions. They need to combine the
  subprocess.check_call() with a function that builds the command. We
  can do functional composition several ways in Python: we can combine
  functions via decorators. We can also combine functions via Callables.
  We could write a higher-order function that combines the check_call()
  with a function to create the command.
| We'll opt for the higher-order function and create partially evaluated
  forms using functools.partial().
| Here's a typical case:

::

   def subprocess_builder( make_command, target_file, *source_list ):
       command= make_command( target_file, *source_list )
       subprocess.check_call( command )

| 
| This is a generic function: it requires a function (or lambda) to
  build the actual command. We might do something like this to create a
  specific builder.

::

   def command_rst2html( output, *input ):
           return ["rst2html.py", "--syntax-highlight=long", "--input-encoding=utf-8", input[0], output]

   rst2html= partial( subprocess_builder, command_rst2html )

| 
| This rst2html() function can be used to define a dependency rule. We
  might have something like this:

::

       files_txt = glob.glob( "*.txt" )
       for f in files_txt:
           build_if_needed( rst2html, ext_to(f,'.html'), f )

| 
| This rule specifies that \*.html files depend on \*.txt files; when
  needed, use the rst2html() function to build the required html file
  when the txt file is newer.
| The ext_to() function is a two-liner that changes the extension on a
  filename. This helps us write "template" build rules rather than
  exhaustively enumerating a large number of similar files.

::

   def ext_to( filename, new_ext ):
       name, ext = os.path.splitext( filename )
       return name + new_ext

| 
| What we've done here is define a few generic functions that form the
  basis for a functional build system that can compete against ant, make
  or scons. The system is not even close to declarative. However, we
  only need to assure that our final build_if_needed() functions have a
  sensible ordering, something that's rarely a towering intellectual
  burden.
| The individual customizations are the build commands like rst2html()
  where we created the command-line list of strings for
  subprocess.check_call(). We can just as easily build functions which
  run entirely in the process or functions which farm the work out to
  separate processes via queues or RESTful web services.
| **Bottom Lines**
| It appears that declarative programming isn't terribly helpful. There
  may be a niche, but it seems to be a small niche to me.
| I'm sure that an object-oriented approach to this problem isn't any
  better. I've written a shabby-make version of this, and it's bigger.
  There's just more code and it's not significantly more clear what's
  going on. Inheritance can be difficult to suss out.
| Python seems to be a good functional programming language. It did this
  very nicely.





