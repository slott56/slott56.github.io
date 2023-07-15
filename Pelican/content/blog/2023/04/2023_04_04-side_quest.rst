Side Quest
###################

:date: 2023-04-04 08:00
:tags: architecture,software design,writing,workflow
:slug: 2023_04_04-side_quest
:category: Technologies
:status: published

Few things are as distracting as those god-awful side quests.

In this case, I had to search out all of the examples in my new book drafts.

Previously
==========

Once upon a time, it was a manual check of code in the book to be sure it made sense.

Ugh. Not living like that again.

Tons of mistakes found by readers.

The root cause? Editors who liked MS Word forcing me to copy-and-paste examples.

Never again.

Automation I
============

I would draft in RST and then use Pandoc to convert to MS Word.

Then tweak the MS Word to use the publisher's preferred MS Word Template.
Point and click at every single thing to make sure it has the right
paragraph or character style name.

Nope. Never doing that again.

Automation II
=============

Let's use LaTeX. My project is an update to a book to the 3rd edition.

(It's this: https://www.packtpub.com/product/functional-python-programming-third-edition/9781803232577).

The 2nd ed. files came to me in MS Word format. I converted them to LaTeX with Pandoc.
Easy. Peasy.

I can now edit the LaTeX Like a real person with a text editor.
Global search and replace now works reliably.
No need to endlessly point and click at pieces of text to set the style.

I do need to remove some pandoc-isms and replace them with the publisher's preferred LaTeX.
This works out very nicely.

But... The examples...

Here's the side quest. (Foreshadowing: it's not the only one.)

Side Quest II-A
----------------

Parse the LaTeX (ugh) and locate all the examples.

Pandoc made them ``{verbatim}`` (I think) or maybe ``{lstlisting}``. Not sure. Doesn't matter.

Change them all to ``{minted}``. (The publisher then changed them all to a customized ``{codeblock}`` that looked GREAT!)

The code to do this **also** added a unique label to each example so the ``example~\\ref{ex-some-tag}`` worked.

(Yes, LaTeX is ugly.)

This was really only preparation for the second side quest.

Side Quest II-B
------------------

That's really only the start.
Once every example has a unique label, I can then do the following:

1.  Extract all of the code snippets from the book, and load them up into a big-old dictionary. LaTeX parsing is a potential ugh, but it works for this book's LaTeX.

2.  Put each snippet into a test context using Jinja and a directory of templates.

    - Some snippets are doctest code, and require little-to-no context.

    - Some snippets are full functions, easy to plug into a file that includes test case(s).

    - Some snippets are code fragments that require a much more elaborate context. And test cases.

3.  Run Black on the filled-in templates to undo any formatting mischief from the book (or from the template.)

4.  Run pytest on the whole show and make sure **everything** works.

The book's examples are a lot of code.
It works out better with a combination of ``tox`` and ``make`` to go chapter-by-chapter
to be sure everything works.

This is only to be sure the examples withstand scrutiny. I still have to write the text.
And rewrite the text when the reviewers find problems.
Which means rewriting the examples.

Code
-----

Here's a LaTeX parser. I can't make any guarantees, because your LaTeX may involve
constructs that I've never seen before.

::

    class BlockKind(Enum):
        BLANK = 0         # An empty line.
        COMMENT = 1       # A "%..." line. Comments at the end of a line are treated as part of the text.
        ENV = 2           # \\begin{name}[opts] ... \\end{name}. Nesting is **not** examined.
        MATH = 3          # $$ ... $$
        TEXTWITHMATH = 4  # A block with "$" in it
        TEXT = 5          # A block, frequently containing \\command[opts]{stuff}

I don't think this is all of the block types. But it is representative of all the block types I actually used.

Here's the definition of a block.

::

    @dataclass
    class Block:
        kind: BlockKind
        lines: list[str]

        @property
        def text(self) -> str:
            return '\n'.join(self.lines)

The first goal being that we can iterate through the blocks, and perform special-case
processing based on the enumerated ``BlockKind``.

The second goal is to be lossless. This means that some block text contains trailing or
leading stuff. Specifically, LaTeX in-line comments.

Next up, the various regex patterns that recognize most instances of the above
blocks.

..  important:: This is not a general solution.

LaTeX has lots and lots of ways to extend the language. Lots.

One opinion I've seen is that the whole thing is better understood
as a Turing machine that's executed and produces an output stream.

And it has constructs that extend the Turing machine with new syntax.
Dynamically.  On-the-fly.

But I don't use any of those. Or if I do use them, the implementation details
are opaque to me and I don't need to care.

::

    COMMENT_PAT = re.compile(r"^\s*%")
    MATH_ENV_PAT = re.compile(r"^\s*\$\$\s*$")
    ENV_BEGIN_PAT = re.compile(r"^\s*\\begin\{(\w+)\}(\[.*\])?")
    ENV_END_PAT = re.compile(r"^\s*\\end\{(\w+)\}")

A few more patterns that are used later to distinguish different kinds of block content:

::

    CONSOLE_PAT = re.compile(r"^\\textbf\{(.*)\}")
    GREATER_PAT = re.compile(r"\\textgreater\{\}|\\textgreater")
    CURLY_PAT = re.compile(r"\{(.)\}")

Here's the parser that breaks LaTeX into ``Block`` instances:

- BlockKind.BLANK  Blank lines between paragraphs.

- BlockKind.COMMENT: Line starting with "%". Note that comments at the end of a line are treated as part of the text.
  This is semantically wrong but syntactically lossless; it preserves the comment in an odd context.

- BlockKind.ENV: \\begin{env}[options] -- \\end{env}
  This is not **all** environments. It's only a short list of code sample environments.
  These are {"quote", "lstlisting", "minted", "codeblock", "consoleblock"}.
  The potential complication is an admonition environment (``\\begin{tipbox}``) MAY contain
  embedded code sample environments, but would not be found because we don't parse the full LaTeX tree.

- BlockKind.MATH: $$ to $$ block

- BlockKind.TEXTWITHMATH: Block of text with "$" in it somewhere.

- BlockKind.TEXT: blocks of text, possibly including commands of the form ``\\command[options]{stuff}``

See https://pylatexenc.readthedocs.io/en/latest/latexwalker/ for a possibly better approach.

This flat expansion works here because we **ONLY** want to distinguish code environments from non-code environments.
We don't really need the full parse tree.

::

    def block_iter(text: str) -> Iterator[Block]:
        """
        Dirty hack lossless LaTeX parser. Treats LaTeX as if it were a flat tree of environments (and commands.)
        Ignores nested environments. Will not dig into lists, for example.
        Doesn't find all comments.
        Will be confused by verbatim in general, but not in most examples that aren't books about LaTeX
        """

        target_environs =  {"quote", "lstlisting", "minted", "codeblock", "consoleblock"}
        text_lines = []
        line_iter = iter(text.splitlines())
        for line in line_iter:
            if len(line) == 0:
                if text_lines:
                    # End previous block
                    yield Block(BlockKind.TEXT, text_lines)
                    text_lines = []
                yield Block(BlockKind.BLANK, [""])
            elif (comment := COMMENT_PAT.match(line)) and comment:
                if text_lines:
                    # End previous block
                    yield Block(BlockKind.TEXT, text_lines)
                    text_lines = []
                yield Block(BlockKind.COMMENT, [line])
            elif (start := ENV_BEGIN_PAT.match(line)) and start and start.group(1) in target_environs:
                if text_lines:
                    # End previous block
                    yield Block(BlockKind.TEXT, text_lines)
                    text_lines = []
                body_lines = [line]
                for body in line_iter:
                    body_lines.append(body)
                    if (end := ENV_END_PAT.match(body)) and end and end.group(1) == start.group(1):
                        break
                yield Block(BlockKind.ENV, body_lines)
            elif (math := MATH_ENV_PAT.match(line)) and math:
                if text_lines:
                    # End previous block
                    yield Block(BlockKind.TEXT, text_lines)
                    text_lines = []
                body_lines = [line]
                for body in line_iter:
                    body_lines.append(body)
                    if body.strip() == "$$":
                        break
                yield Block(BlockKind.MATH, body_lines)
            elif "$" in line:  # TODO: must be unescaped and outside \verb
                if text_lines:
                    # End previous block
                    yield Block(BlockKind.TEXT, text_lines)
                    text_lines = []
                yield Block(BlockKind.TEXTWITHMATH, [line])
            else:
                # Accumulate a block
                text_lines.append(line)
        if text_lines:
            # End any final block
            yield Block(BlockKind.TEXT, text_lines)

Once we have the sequence of blocks, we can tweak the various code sample blocks.

Because the parsing is lossless, we can reconstruct a modified LaTeX document,
as long we nothing too weird is going on inside ``\\verbatim|...|`` blocks.

This worked well-enough to -- reliably -- pull all the code samples out of the text.

Automation III
==============

New book in the works.

Two key alternatives:

-   Write all the examples and use minted to pull lines of code from the example files.

-   Recapitulate the previous book's unique approach to example labels, and injection into specific contexts.

This book has a distinct focus, however. There isn't as much code.
it doesn't seem to be essential for the code to be copy-and-paste complete.

Further, it doesn't seem helpful to provide doctest-like examples.
The book is for a more advanced audience.

What I'm could try to do is locate all of the code examples in a corpus of code files.
Then I can gingerly switch out actual code for a reference to lines in a code file.

That seems easier to live with.

If I need to change the code, I fix the corpus of code files, and rerun the test suite.
If the example's line numbers changed, fiddle with the LaTeX a little to get the right lines into the book.

The downside of doing this is the corpus of code files become a first-class part of the book's
source. It lives side-by-side with images and LaTeX files.

Some more thinking required before I finally make a commitment.
