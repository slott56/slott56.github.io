Cleaning up Examples
===============================================

:date: 2023-11-17 08:01
:tags: writing,latex
:slug: 2023-11-17-example_cleanup
:category: Books
:status: published

Stand-alone document files for tech writing are awful.
They should *not* be used as widely as they are.

BLUF: Don't Use MS-Word
-----------------------

We used to call editors like MS-Word *WYSIWYG* -- What You See Is What You Get.
Once upon a time, an editor that immediately presented the final rendered doc was an amazing, life-changing thing.
Steve Jobs insisted Macintosh offer variable-width fonts. Wonderful!

The current implementations seems terrible, however.

When writing about code, a ``.docx`` file can be filled with examples that -- no matter how careful the writing and editing process --
aren't really subject to any useful level of automated testing.

The author writes, tests and then -- ugh -- copies and pastes into the document file.
The reviewers review and check. The tech editor checks.
Any mistakes corrected in the source code need to be re-copied and re-pasted -- manually -- into the document file.
Who's got the list of all the copy-and-paste locations? Anyone?

And how would you get such a thing from MS-Word?

Some kind of "INCLUDE FROM EXTERNAL FILE HERE" marker seems like it is absolutely essential.

And missing.

There's a way with some kind of "merge" capability to maybe jam external text into a document.
But. Yuk. It's not at all clear how this works.
It doesn't seem to be a first-class, easy-to-be-sure-you're-doing-it-right feature.

It gets worse
-------------

Unpacking the official, final source documents for my books from the publisher's ``.DOCX`` was eye-opening.

First -- the various boundaries between segments of the text can be wrong.
Which means they were wrong all along.
The errors are small.
Indeed, the errors are so small I don't think anyone can actually *see* them. But.
When I go to make changes, I find there's a kind of nightmare of invisible boundaries.

The key problem is that the WYSIWYG editors seem to have innumerable invisible borders.
These wind up on the wrong side of the markup.
They can be accidentally assigned the wrong style. With **no** useful feedback.

(Yes you can make whitespace visible in MS-Word. Try it. Whitspace doesn't have a visible style,
so you still don't know what part of the content it belongs to.)

The implicit ¶ boundary after a code example -- to be specific -- can wind up as part of
the code.

Want to add text after the example?

It's now part of the example. It looks like ``CODE``.

This leads time wasted on pointing and clicking to adjust the boundaries to get the text out of the example.
Or the example out of the text.

Worse.

The implicit ¶ boundary that's part of an itemized list item can wind up in -- or out -- of the adjacent code example.
Visually, you can't tell. Sometimes, you might notice the bullet looks a little "off".
It's not obvious (from a single bullet) that it's in the ``CODE`` font, not the TEXT font.

Worse.

The WYSIWYG editor is designed so mom (my mom, who's in her 90's) can create a shopping list and print it out.
(Which makes you wonder why it has so many features mom will never use.)

Here's the problem with these "amateur user" features:

1.  The tools make (and enforce) assumptions about itemized and enumerated lists that are appropriate for mom.

2.  These assumption are not appropriate for technical writing.

    I need multiple paragraphs per number. How do I do this? I have to change the style of the "additional" paragraphs.

    Then, I have to make sure that the subsequent numbered paragraphs start with the right number.

3.  This is a lot of error-prone pointing and clicking. A small change leads to strange numbers.
    Or numbers in the ``CODE`` font.

I could go on. I'm not a fan of WYSIWYG. I call it "What is you is *all* you get."

What's Better?
--------------

I'm not **sure** what's better. But. I have to say, that I'm really pleased with LaTeX and the ability
to use the ``listings`` and ``minted`` packages to include a few lines of code from external files.

(Some people hate LaTeX with unbridled passion. I can't recommend it because the haters stop reading at "LaTeX.")

Case In Point
-------------

The book has snippets like the following:

::

    def some_method(self) -> None:
        # Do some prep.
        super().some_method()  # Use the superclass implementation.
        # Any followup goes here.

Just a little conceptual overview of how a subclass method can extend a superclass method using the ``super()`` function.

No biggie, right?

Heh.

Now that I can put this in a separate file -- and unit test it -- and subject it to **mypy** and **pyright** and **ruff**,
the little stand-alone snippet has fatal problems.

What to do?
-----------

It's not squeaky clean. What do I do?

1. Don't pull it out of the text and test it. It's just "conceptual" code-like material.

2. Gussy it up with the needed context and make sure it's really, really correct.

I'm an option 2 kind of writer. I'm not brilliant. I'm not introducing something new to the world. I didn't write
some world-changing FOSS package for which I'm writing the definitive documentation. All I've got -- really --
is exhaustively detailed design alternatives and sparkingly correct code.

In LaTeX world, wrapping up ``\verb|some_method()|`` into a separate file is

a.  Easy.

b.  Guarantees that it's correct.

c.  The absolutely latest and greatest version becomes part of the book automatically.

Boom. Done.

If it's so easy?
----------------

Why doesn't everyone do this?

-   Some folks hate LaTeX.  I don't blame them.  It's complicated.

-   Some folks hate LaTeX.  It's also quite slow. It takes multiple seconds to render a chapter.
    What that finishes, you're reading a PDF in one window and fiddling with LaTeX in another.
    Compilers are like that. Folks who hate on LaTeX put up with compiled code all the time.
    I get it. They have different expectations for editing words and editing code.

-   Some folks hate LaTeX.  As brilliant as Pandoc is, the .DOCX issues mean that you're LaTeX extraction from a .DOCX is -- well -- filled with annoying problems.
    Hundreds of non-breaking spaces ``~`` will be peppered randomly around. Some things like ``'`` will be transformed to ``\textsinglequote`` or ``\textsinglequote{}``.
    And on and on and on. I've got some Python code to cleanup parts of the problematic LaTeX, but not all of it. It's a manual
    pass -- 8 to 12 hours of labor -- to get things into an "acceptable" form where a good, clean PDF can be generated from a chapter.
    The invisible boundary problems all have to be found and fixed by hand.

-   Some folks hate LaTeX.  A single missing ``}`` from a ``\textbf{command`` can be a challenge to find. Easy to fix.
    Same for ``\verb|code`` where the trailing ``|`` is missing.

-   Some folks hate LaTeX.  Yesterday I spent a good 30 minutes -- maybe more -- looking for an unpaired ``"`` in the text.
    I used the words ``30"`` to mean ``30 inches``. Things don't work, but there's no positive **line 3194: unpaird quote** error.
    There's not even an obvious point in the document where formatting went to hell.
    Indeed, my preferred editor only sees the chapters without the ``main.tex`` wrapper, and doesn't know what packages have
    been included.  It thinks my LaTeX is just garbage.

But.

My code is clean. And the document **always** reflects unit-tested, type-checked code.

(I don't run all code through the **ruff** formatter because book margins force me to manually undo ideal PEP-8 formats.)

The cross-references all work perfectly.  Word can do this, but it's clunky and awkward. LaTex ``\secref{}`` and ``\label{}`` do everything I want.
I can search the document for all ``\section{}\label{}`` constructs to build a my own crib of things-to-cross-reference against.

The damnable invisible boundaries are visible. Commands like ``\begin{codeblock}`` and ``\end{codeblock}`` are clearly separated from ``\item``.
Clearly. I can add whitespace and comments to clarify, if I need to. Things are **visible**.
