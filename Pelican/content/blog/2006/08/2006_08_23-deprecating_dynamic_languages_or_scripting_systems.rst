Deprecating Dynamic Languages (or Scripting Systems)
====================================================

:date: 2006-08-23 11:05
:tags: news
:slug: 2006_08_23-deprecating_dynamic_languages_or_scripting_systems
:category: News
:status: published





Holub discards the currently popular dynamic
languages with a scathing
comment:



"And not scripting
systems (I’m reluctant to call them languages) like PHP and Ruby, which
are too Wild West to be trustworthy. No language that moves compile-time bugs
into runtime is worth your time if you consider reliability to be important; I
don’t care how fast its adherents allege you can throw together a program.
You don’t measure productivity improvements solely by looking at a
reduction in the lines-of-code-written-per-day numbers, even if these statistics
are
trustworthy."



Scathing.



Besides
failing to mention Python, he misses two important points: 

1.  Language #3 on the `TPCI <http://www.tiobe.com/tpci.htm>`_   is
    Visual Basic.  He quotes the description of `Scala <http://scala.epfl.ch/docu/>`_  (so
    similar to Java that it runs in the JVM), which provides some hint as to Holub's
    standards for a good language (e.g., type-safe, object-oriented, algebraic data
    types).  VB has almost none of these features, yet, it continues to grow in
    popularity.  As a **Next Big Thing** , that's a horrifying situation.  What
    about VB?  I guess, since this is Java Watch, we just ignore it as long as Java
    is language #1.

2.  Languages #5, 6, 7, and 10 are dynamic
    languages (PHP, Perl, Python and Javascript).  In aggregate, dynamic languages
    add up to a pool of languages as popular as Java.  Perhaps Holub's missed
    something interesting about dynamic languages.  

3.  What's the
    real clincher here?  If dynamic languages are
    "too Wild West to be
    trustworthy" why are they so popular? 




**Misconceptions.** 



Dynamic
languages aren't about the "lines-of-code-written-per-day numbers".  They're
about the lines-of-code-written-to-do-something-useful numbers.  I find non-OO
programming tedious because
*everything* 
is long-winded.  I find type-safe OO programming to be far better, but some
things can get still get long-winded.  To be properly type-safe, portable,
generic and explicit in Java means -- sometimes -- a lot of code which doesn't
really do very much.  A lot of the Java framework elements lead to programs
which seem more complex than they
are.



The reliability issue isn't *necessarily* 
true about dynamic programming.  Yes, a shoddy dynamic program will die at
run-time with a brain-dead error that should have been found via an inspection
or a good unit test.  But, `/dev/null <http://jroller.com/page/cpurdy>`_ 's post, `And the Braindead Award goes to... <http://jroller.com/page/cpurdy?entry=and_the_braindead_award_goes>`_  shows that
even type-safe, compiled languages can harbor hard-to-locate bugs.  Indeed,
having spent the last decade helping people do Java programming, I've seen a lot
of bad design written into both the code and the unit tests.  Bad design that
wouldn't be found until run-time.




**A Value Proposition.** 



What makes dynamic
languages so popular?  Clearly, they fill a need.  I think that the need is
`mutability <{filename}/blog/2005/09/2005_09_18-essay_14_mutability_analysis.rst>`_ .
I don't think it's effective to
package everything into static, compiled, type-safe Java applications.  Some
things require more flexibility.  We can use shell scripts, or XML-configuration
files of Ant class definitions, but we need last-minute, fine-tuning,
flexibility.



Flexibility is something
we can try to build into our software.  But sadly, our users are far more clever
(or devious) than we are and will push right past the envelope.  Every executive
that cuts a sweetheart deal with a preferred customer or vendor may be breaking
our application software with her handshake on the 18th green at her
country-club.  Since the software will be broken by business policy changes, we
can either plan for change -- and use a scripting language -- or fight against
the change.  Claiming that it will take months to rewrite the application is --
in effect -- fighting against the
change.



When it comes to application
software changes, the users hold the trump cards: Excel and Access.  If you
can't build it in Java RIGHT NOW, they will build some non-sensical manual
procedure with desktop tools.  When you're ready to build it in Java, they've
implemented a Byzantine process and trained the rest of the department; now they
demand that your application implement their bizarre
behavior.



I prefer to embrace dynamic
languages, give them a place at the table, and control their use very closely. 
That way, I don't have to fight change, but can be the agent of
change.











