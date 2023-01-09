A LaTeX Thing I Did -- And A ToDo:
==================================

:date: 2022-06-14 08:00
:tags: literate programming,packtpub,#python
:slug: 2022_06_14-a_latex_thing_i_did_and_a_todo
:category: Technologies
:status: published

When writing about code in LaTeX, the essential strategy is to use an
environment to format the code so it stands out from surrounding text.
There are a few of these environments available as LaTeX add-on
packages. The three popular ones are:

-  **verbatim**. I think this is built-in to LaTeX. It's not very
   clever, but it is simple to use.
-  **listings**. See https://www.overleaf.com/learn/latex/Code_listing
-  **minted**.
   See https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted

These are nice for making code readable and distinct from the
surrounding text.

A common way to talk about the code is to use inline verbatim
``\verb|code|`` sections. I prefer inline ``\lstinline|code|``, but, my
editor prefers ``\verb``. (I have trouble getting all the moving parts
of minted installed properly, so I use **listings**.)

Also. And more important.

There's the
``\lstinputlisting[language=Python, firstline=2, lastline=12]{some_module.py}``
command. This lets an author incorporate examples from working, tested
modules. Minted doesn't seem to have this, but it might work with an
``\input`` command. Don't know. Haven't tried.

Let's talk about workflow.

Workflow
--------

The idea behind these tools is you have code and after that, you write
about the code. I call this **code first**.

Doing this means you can include code snippets from a file.

Which is okay, but, there's another point of view: you have a document
that contains the code. This is closer to the Literate Programming POV.
I call this **document first**. I've got all the code in the document
you're reading, I've just broken it up and spread it around in an order
to serve my purpose as a writer, not serve the limitations of a parser
or compiler.

There is a development environment --
`WEB <https://texfaq.org/FAQ-webpkgs>`__ -- to create code that can be
run through the Weave and Tangle tools to create working code and usable
documentation. This is appealing in many ways.

For now, I'm settling for the following workflow:

#. Write the document with code samples. Use ``\lstlisting`` environment
   with explicit unique labels for each snippet. The idea is to focus on
   the documentation with explanations.
#. Write a Jinja template that references the code samples. This is a
   lot of ``{{extract['lst:listing_1']}}`` kind of references. There's a
   bit more that can go in here, we'll return to the templates in a
   moment.
#. Run a tool to extract all the ``\lstlisting`` environments to a
   dictionary with the label as the key and the block of text as the
   value. This serializes nicely as a JSON (or TOML or YAML) file. It
   can even be pickled, but I prefer to be able to look at the file to
   see what's in it.
#. The tool to populate the template is a kind of trivial thing to build
   a Jinja environment, load up the template, fill in the code samples,
   and write the result.
#. I can then use **tox** (and **doctest** and **pytest** and **mypy**)
   to test the resulting module to be sure it works.

This tangles code from a source document. There's no weave step, since
the source is already designed for publication. This does require me to
make changes to the LaTeX document I'm writing and run a ``make test``
command to extract, tangle, and test. This is not a huge burden. Indeed,
it's easy to implement in PyCharm, because the latest release of PyCharm
understands Makefiles and tox. Since each chapter is a distinct
environment, I can use ``tox -e ch01`` to limit the testing to only the
chapter I'm working on.

I like this because it lets me focus on explanation, not implementation
details. It helps me make sure that all the code in the book is fully
tested.

The Templates
-------------

The template files for an example module have these three kinds of code
blocks:

#. Ordinary Listings. These fall into two subclasses.

#. 

   #. Complete function or class definitions.
   #. Lines of code taken out of context.

#. REPL Examples.

These have three different testing requirements. We'll start with the
"complete function or class definitions."  For these, the template might
look like the following

::

   {{extract['lst:listing_1']}}

   def test_listing_1() -> None:
       assert listing_1(42)
       assert not listing_1(None)

This has both the reference to the code in the text of the book and a
test case for the code.

For lines of code out of context, we have to be more careful. We might
have this.

::

   def some_example(arg: int) -> bool:
       {{extract['lst:listing_2']}}

   def test_listing_2() -> None:
       assert listing_2(42)
       assert not listing_2(None)

This is similar to a complete definition, but it has a fiddly
indentation that needs to be properly managed, also. Jinja's generally
good about not inserting spaces. The template, however, is full of what
*could* appear to be syntax errors, so the code editor **could** have a
conniption with all those ``{}`` blocks of code. They happen to be valid
Python set literals, so, they're tolerated. PyCharm's type checking
hates them.

The REPL examples, look like this.

::

   REPL_listing_3 = """
   {{extract['lst:listing_3']}}
   """

I collect these into a ``__test__`` variable to make them easy for
doctest to find. The extra fussiness of  a ``__test__`` variable isn't
needed, but it provides a handy audit for me to make sure everything has
a home.

The following line of code is in most (not all) templates.

::

   __test__ = {
       name: value
       for name, value in globals().items() 
       if name.startswith("REPL")
   }

This will locate all of the global variables with names starting with
REPL and put them in the ``__test__`` mapping. The REPL names then
become the test case names, making any test failures easier to spot.

My Goal
-------

I do have some Literate Programming tools that I might be able to
leverage to make myself a Weaver that produces useful LaTeX my publisher
can work with. I should do this because it would be slightly simpler.
The problem is my Web/Weave/Tangle tooling has a bunch of dumb
assumptions about the weave and tangle outputs; a problem I really need
to fix.

See `py-web-tool <https://github.com/slott56/py-web-tool>`__.

The idea here is to mimic other WEB-based tooling. These are the two
primary applications:

-  **Weave**. This makes documentation in a fairly transparent way from
   the source. There are a bunch of substitutions required to fill in
   HTML or LaTeX or Markdown or RST around the generic source. Right
   now, this is pretty inept and almost impossible to configure.
-  **Tangle**. This makes code from the source. The point here is the
   final source file is not necessarily built in any *obvious* order.
   It's a tangle of things from the documentation, put into the order
   required by parser or compiler or build system or whatever.

The weaving requires a better way to provide the various templates that
fill in missing bits. Markdown, for example, works well with fenced
blocks. RST uses a code directive that leads to an extra level of
indentation that needs to be carefully excised. Futher, most markup
languages have a mountain of cruft that goes around the content. This is
unpleasantly complex, and very much subject to odd little changes that
don't track against the content, but are part of the evolution of the
markup language.

My going-in assumption on tangling was the document contained **all**
the code. All of it. Without question or exception. For C/C++ this means
all the fiddly little pre-processor directives that add no semantic
clarity yet must be in the code file. This means the preprocessor
nonsense had to be relegated to an appendix of "yet more code that just
has to be there."

After writing a tangler to pull code from a book into a variety of
contexts, I'm thinking I need to have a tangler that works with a
template engine. I think there would be the following two use cases:

-  **No-Template Case**. The WEB source is complete. This works well for
   a lot of languages that don't have the kind of cruft that C/C++ has.
   It generally means a WEB source document will contain definition(s)
   for the final code file(s) as a bunch of references to the
   previously-explained bits. For C/C++, this final presentation can
   include the fiddly bits of preprocessor cruft.
-  **Template Case**. A template is used to with the source to create
   the tangled output. This is what I have now for pulling book content
   into a context where it is testable. For the most part, the template
   files are quite small because the book includes test cases in the
   form of REPL blocks. This presents a bit of a problem because it
   breaks the "all in one place" principle of a WEB project. I have a
   WEB source file with the visible content plus one or more templates
   with invisible content.

What I like about this is an attempt to reduce some of the cruftiness of
the various tools.

I think my py-web-tool might be expanded to handle my expanded
understanding of literate programming.

I have a book to finish, first, though. Then I can look at improving my
workflow. (And yes, this is backwards from a properly Agile approach.)





