My Shifting Understanding and A Terrible Design Mistake
=======================================================

:date: 2022-06-21 08:00
:tags: #python,jinja,pyWeb,PyLit3
:slug: 2022_06_21-my_shifting_understanding_and_a_terrible_design_mistake
:category: literate programming
:status: published

I've been fascinated by Literate Programming forever.

I have two utterly divergent takes on this.

See https://github.com/slott56/PyLit-3 for one.

See https://github.com/slott56/py-web-tool for another.

And yet, I've still done a really bad design job. Before we get to the
design, a little bit of back story.

Back Story
----------

Why two separate literate programming projects? Because it's not
**clear** what's best. It's a field without too many boundaries and a
lot of questions about the value produced.

PyLit I found, forked, and upgraded to Python 3. I didn't design it.
It's far more clever than something I'd design.

Py-Web-Tool is something I wrote based on using a whole bunch of tools
that follow along behind the original WEB tools. Nothing to do with web
servers or web.py.

The Problem Domain
------------------

The design problem is, in retrospect, pretty obvious. I set it out here
as a cautionary tale.

I'm looking at the markup languages for doing literate programming. The
idea is to have named blocks of code in your document, presented in an
order that makes sense to your reader. A tool will "weave" a document
from your source. It will also "tangle" source code by rearranging the
code snippets from presentation order into compiler-friendly order.

This means you can present your core algorithm first, even though it's
buried in the middle of some module in the middle of your package.

The presentation order is \*not\* tied to the order needed by your
language's toolchain.

For languages like C this is huge freedom. For Python, it's not such a
gigantic win.

The source material is a "web" of code and information about the code. A
web file may look like this:

::

   Important insight.

   @d core feature you need to know about first @{
       def somecode() -> None:
           pass
   @}

   And see how this fits into a larger context?

   @d something more expansive @{
   def this() -> None:
       pass
       
   def that() -> None:
       pass
       
   @<core feature you need to know about first@>
   @}

   See how that works?

This is easy to write and (relatively) easy to read. The
``@<core feature you need to know about first@>`` becomes a hyperlink in
the published documentation. So you can flip between the sections. It's
physically expanded inline to tangle the code, but you don't often need
to look at the tangled code.

The Design Question
-------------------

The essential Literate Programming tool is a compiler with two outputs:

-  The "woven" document with markup and such
-  The "tangled" code files which are code, largely untouched, but
   reordered.

We've got four related problems.

#. Parsing the input
#. An AST we can process
#. Emitting tangled output from the AST
#. Emitting woven output form the AST

Or, we can look at it as three classic problems: deserialization, AST
representation, and serialization. Additionally, we have two distinct
serialization alternatives.

What did I do?

I tackled serialization first. Came up with a cool bunch of classes and
methods to serialize the two kinds of documents.

Then I wrote the deserialization (or parsing) of the source WEB file.
This is pretty easy, since the markup is designed to be as trivial as
possible.

The representation is little more than glue between the two.

What a mistake.

A Wrong Answer
--------------

Focusing on serialization was an epic mistake.

I want to try using
`Jinja2 <https://jinja.palletsprojects.com/en/3.1.x/>`__ for the markup
templates instead of
`string.Template <https://docs.python.org/3/library/string.html#template-strings>`__.

However.

My AST was such a bad hack job it was essentially impossible to use it.
It was a quagmire of inconsistent ad-hoc methods to solve a specific
serialization issue.

As I start down the Jinja road, I found a need to be able to build an
AST without the overhead of parsing.

Which caused me to realize that the AST was -- while structurally
sensible -- far from the simple ideal.

What's the ideal?

The Right Answer
----------------

This ideal AST is something that lets me build test fixtures like this:

::

   example = Web(
      chunks=[
          TextChunk("\n"),
          NamedCodeChunk(name="core feature you need to know about first", lines=["def someconme() -> None: ...", "pass"])),
          TextChunk("\nAnd see how this fits into a larger context?\n"),
          NamedCodeChunk(name="something more expansive", lines=[etc. etc.])
      ]
   )

Here's my test for usability: I can build the AST "manually" without a
parser.

The parser can build one, also, but I can build it as a sensible,
readable, first-class Python object.

This has pointed me to a better design for the overall constructs of the
WEB source document. Bonus. It's helping me define Jinja templates that
can render this as a sensible woven document.

Tangling does not need Jinja. It's simpler. And -- by convention -- the
tangled code does not have anything injected into it. The woven code is
in a markup language (Markdown, RST, HTML, LaTeX, ASCII DOC, whatever)
and some markup is required to create hyperlinks and code sections.
Jinja is super helpful here.

TL;DR
-----

The essence of the problem is rarely serialization or deserialization.
 It's the internal representation.

| 



-----

When learning how to use a word processor, it turn...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2022-07-16 13:24:35.832000-04:00

When learning how to use a word processor, it turns out the second word
processor you learn takes longer than the first. As you explore the
second one, the core ideas get contemplated and refined. The third one
on is just "where's the quick reference". We do the same with rewriting
code, as you are discovering. One point of literate programming is to
explain the insights we gain.





