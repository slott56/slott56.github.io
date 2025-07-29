Gloom and Despair -- LaTeX Edition
###################################

:date: 2025-07-29 09:54
:tags: python,learning,latex
:slug: 2025-07-29-the_gloom_despair_latex
:category: Books
:status: published

I write all my books using LaTeX.
Parts of LaTeX are (at first) confusing.

Recently, I had a moment of despair when my LaTeX processing tools no longer worked.

BLUF
====

Don't panic. Gather the data.

If the logs aren't good enough to reveal what's going on, fix the logs.


The Story
=========

LaTeX has numerous advantages over strugging with .DOCX files in Libre Office (or MS-Word.)
In particular, having to get the styles **right** in a "What You See Is All You Get" visual editor is brutal.
The boundaries for the styles are utterly occluded and there's no real way to be sure the bullet items aren't also part of the code highlighting.

LaTeX is text. Any text editor produces perfect LaTeX.
No complicated pointing and clicking.

But. It's also more than text. Hence the gloom and despair.

The Quirk
=========

LaTeX has a quirk.
And it's a big one.

LaTeX is not really "markup" in the sames sense as XML or RST or Markdown.

LaTeX is code with embedded literal text.
What's important is the text doesn't always have quotes or clear boundaries.
There's a "if it's not in a macro, it's text" kind of rule.

LaTeX processing isn't really translating Text + Markup ==> PDF.
A LaTeX engine evaluates a program you wrote in the TeX language.
The side-effect of evaluating this program is to write a "DVI" file.
This file can then translated into a PDF.

This nuanced distinction matters because your LaTeX can (and frequently does) include new macro definitions that change the behavior of the rest of your program.
The parser is -- in effect -- stateful; some constructs change the parser's internal state.
The consequence of this is that it's difficult to trivially parse LaTeX.

We can't write an app to look for regular expression patterns like ``\w+\{\w+\}`` to parse the LaTeX.
It requires a more sophisticated algorithm.

What Do We Do?
===============

I've been using the ``pylatexenc`` library.  https://pypi.org/project/pylatexenc/.

This is focused on some edge cases of converting Unicode to LaTeX and LaTeX to Unicode.

However, it does have an elegant LaTeX parser, that -- with a proper context database -- can process a wide variety of LaTeX.

I've got two use cases.

-   Cleanup Pandoc LaTeX. Legacy .DOCX files can be converted to LaTeX by Pandoc. https://pandoc.org

    However. The LaTeX created from .DOCX is a large pain in the neck and requires a healthy dose of conversion and correction to make it useful. (The ``\textquotesingle`` is used all over the place.)

-   Analyze Overleaf LaTeX. I need to get summaries of the outlines decorated with page counts.

And this second use case baffled me.

What Broke
===============

A few days ago, I tried to get an outline from a finished project.
My outline parser crashed hard.
It's a simple app that examines all the ``.TEX`` files gathering structure information.
And it was unable to parse the book's outline.

Some tools worked.

Some didn't.

Ugh.

I had a number of questions and assumptions.

Question 1: What went wrong? What changed?
------------------------------------------

Clearly, the book's content changed. Somewhere in the writing process, I changed something.

Question 2: What content change could baffle the the ``pylatexenc`` library?
----------------------------------------------------------------------------

Just as clearly, it was the presence of a macro or an environment that had never been used before.
This has to be something I introduced during revisions or code review or something.
Some macro or environment is new.

But.  There's nothing in the output that helps identify the location of the problem.

All I had was a chorus of "Gloom, Despair, and Agony on Me."

Which wasn't appropriate.

My First Mistake
===================

As these tools evolved over the past few books, I'd been pretty fast and loose with my debugging.
I'd been using the following technique:

..  code-block:: python

    DEBUG = False

    def something() -> None:
        # some code
        if DEBUG:
            print("something")
        # more code

This was handy when I was poking at the code daily.
This isn't something I'm posting to PyPI.
It has a suite of unit tests, but there are odd special cases and edge cases all through it.

This seemed like a sensible approach.

Returning to the code after 7 months, this kind of debugging was opaque.
There's no good reason for this kind of thing.

I had no idea where I'd put these, or what they were going to reveal when I set ``DEBUG`` to ``True``.
Indeed, I hadn't provided any handy way to set ``DEBUG`` to ``True`` from the command line.

What I Fixed
=============

Every ``if DEBUG:`` had to be rewritten as ``logger.debug()``.
The ``print(f"whatever {arg1} {arg2}")`` had to become ``logger.debug("whatever %s %s", arg1, arg2)``.
This is not a substantial rewrite.
It's the work of a few mninutes to fix all 35 locations.

This revealed a lot. A lot.

The most important revelation was the ``pylatexenc`` library was already using the logger.
And I had not been making any use of that.

Foolishly.

Between adding proper debugging and enabling logging, I found out what was **actually** wrong.

And it had nothing to do with LaTeX parsing.

My assumptions were mostly wrong.
Well, about :math:`\frac{1}{2}` wrong.

The Real Mistake
================

It took a few exepriments to figure out what debugging was needed and what was too much of the wrong kind of detail.
My corrected logging revealed that LaTeX parsing was **not** broken.

The ``pylatexenc`` library produces a syntax tree from the LaTeX.
The parsing phase (the LatexWalker) creates this tree.
Then the application can visit the tree with a visitor subclass.

It became clear that the problem was related to the **Visitor** traversing the parsed LaTeX.
My application's visitor subclass used a **Builder** that accumulated the various structure macros into an outline.
The original design was predicated on a structure where each chapter stood more-or-less alone.

The publisher's style wraps each ``\chapter{}`` in a ``\begin{chapterenv}`` environment.
My **Builder** didn't work well with this extra environment wrapper around the chapter.

Ah.

The problemn **was** something I introduced.

But it **wasn not** a novel macro or environment.

It was an environment that baffled ``OutlineBuilder``.
A small change and I'm back in business.


