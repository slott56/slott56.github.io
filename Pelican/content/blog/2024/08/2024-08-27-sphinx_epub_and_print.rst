Sphinx EPUB and Print
##########################

:date: 2024-08-27 16:31
:tags: sphinx,RST,LaTeX,epub,PDF
:slug: 2024-08-27-sphinx_epub_and_print
:category: Books
:status: published

Let's say you want to self-publish an ebook and a print-on-demand paperback book.

This isn't impossible, nor is it particularly easy. Here's what I've learned.

Basic Workflow
==============

You've got two obvious paths to make sure your EPUB book and your print-on-demand book match:

1. Convert EPUB to Print. This generally means starting with HTML for the EPUB and building LaTeX from this to create the PDF. There are a number of tools that do this. It's relatively easy because HTML is easy to parse, and doesn't have quite to many options and features as LaTeX.

2. Convert Print to EPUB. This generally means using a specialized LaTeX tool to extract HTML from LaTeX. There's a pair of tools, **Tex4ht** and **LaTeX2HTML**, that can be pressed into service.

Both of these suffer from potential problems with vague markup.
HTML has a limited domain of tags, and important semantic details put into ``<div>`` and ``<span>`` tags where the CSS class name provides crucial information.
LaTeX is more than just markup; it's a Turning-complete programming language, and your ``.tex`` input as a piece of code that emits a DVI file that drives the final printing process.
Extracting semantically meaningful details can be difficult.

There's a third path: use a language like RST (or Markdown) and convert it to HTML **and** LaTeX.
Now you have one source for the content, and the vagaries of HTML tags vs. CSS classes or LaTeX layers are less burdensome.

The **Sphinx** package handles this elegantly. https://www.sphinx-doc.org/en/master/index.html.

Content Creation
================

First, get all the examples right. Be sure all the code has unit tests.

Option 1 is to use REPL-based examples and run the text through **doctest**.

Option 2 is to use more conventional modules in files with a separate test tool.
This can be **doctest**, but it may also need to be something more sophisticated, like **pytest** (https://docs.pytest.org/en/stable/).

It's imperative to use **mypy** or **pyright** to check the type hints, and **ruff** or **black** to format the code consistently.
This has to be done carefully. Sometimes, the book margins require fiddling with **ruff** configuration to narrow
the code so it will fit.

A handy feature of **doctest** is the ``__test__`` object. This is a mapping from test name to test code.

Let's say you have an example line of code like this:

..  code-block:: python

    p = 355 / 113

And you need to be sure it works.

Consider putting this into your examples file:

..  code-block:: python

    test_ex_1 = """
    >>> from math import isclose, pi
    >>> isclose(p, pi, rel_tol=1e-7)
    True
    """

You can add the following at the very bottom of the module.

..  code-block:: python

    __test__ = {name, case for name, case in vars().items() if name.startswith("test_")}

The doctest target, ``__test__`` will be a dictionary, with test cases pulled from
all global variables that start with ``test_``.
This means every random, little scrap of code can be thrown into a file with enough tests to make
the examples unassailable.

Of course, there's more to test design, but that's a start.

General Setup
=============

Diagrams are often best done using **PlantUML** (https://plantuml.com).
For really, really complicated stiff, use TIKZ and LaTeX.

That means installing the ``sphinxcontrib.plantuml`` plug-in to Sphinx to make PlantUML work cleanly.

Sphinx EPUB
==============

The EPUB pipeline in Sphinx is so similar to the HTML pipeline. It's easy to create the HTML
pages and review them for readability, formatting, spelling mistakes, clarity, spelling mistakes,
grammar errors, and spelling mistakes.

I use **pycharm**, and the spell-checking is less than ideal. For free. For a few $$$, I think I might do better.

I have some CSS features that I really like.

1.  A lettrine at the start of a section. This is a "dropped capital letter". It ties up two lines.

2.  From https://www.lode.de/, I borrowed the idea of big quotation marks around a blockquote paragraph.

These require special CSS in Sphinx. There are two parts.

1.  Add this to your ``conf.py``

    ..  code-block:: python

        html_static_path = ['_static']
        html_style = 'building_skills.css'

2.  Add a ``building_skills.css`` to the ``_static`` directory. It looks like this:

    ..  code-block:: css

        @import url("alabaster.css");

        p:has(>span.lettrine)::first-letter {
            float: left;
            font-size: 3em;
            line-height: 100%;
            padding: 0 0;
            margin: -0.1rem .4rem 0 0;
        }
        span.lettrine {
            font-variant-caps: small-caps;
        }

        div.myquotation {
            /* Indent */
            margin-left: 2em;
            margin-right: 2em;
            }

        div.myquotation::before {
            content: "“";
            font-size: 3em;
            float: left;
            line-height: 50%;
        }

Now, all you need to do is make sure there's a ``<span class="lettrine">`` to make the dropped-capital lettrine work. That's done with a local extension for Sphinx.
Again, there are two parts.

1.  Add this to your ``conf.py``

    ..  code-block:: python

        from pathlib import Path
        import sys

        sys.path.append(str(Path("ext").absolute()))

    And this, too.

    ..  code-block:: python

        extensions = [
            'lettrine',
            # all the others, like "sphinxcontrib.plantuml", and "sphinx.ext.imgmath",
        ]

2.  Create an ``ext`` directory, and include a module, ``lettrine.py``.

    ..  code-block:: python

        from docutils import nodes

        from sphinx.application import Sphinx
        from sphinx.util.docutils import SphinxDirective, SphinxRole
        from sphinx.util.typing import ExtensionMetadata


        class LettrineRole(SphinxRole):
            """A role to mark a Lettrine (often at the start of a section.)

            The text becomes a new inline ``<span class="lettrine">``
            """
            first: str
            rest: str
            def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
                # Break things up for LaTeX output.
                self.first = self.text[0]
                self.rest = self.text[1:]
                new_node = nodes.inline(text=self.text)
                new_node['classes'] = ['lettrine']
                return [new_node], []


        def setup(app: Sphinx) -> ExtensionMetadata:
            app.add_role('lettrine', LettrineRole())

            return {
                'version': '0.1',
                'parallel_read_safe': True,
                'parallel_write_safe': True,
            }

The role defines a ``:lettrine:`` role that merely wedges in the  proper class.
The ``setup`` adds the role to the sphinx environment.

..  code-block:: rst

    :lettrine:`Now, your opening sentence has a lettrine.`
    Subsequent lines of the paragraph are formatted **normally**.

Sphinx LaTeX
==============

This involves a **lot** of little details. We'll start with a little background.
Then we'll look at the configuration.

Background
----------

The LaTeX language involves a mixture of environments and commands.
The environments have clear boundaries, usually a ``\begin{X}`` and ``\end{X}``.
Sometimes commands **also** bracket something; the ``\makeatletter`` and ``\makeatother`` commands,
bracket a macro definition that needs to have ``@`` interpretation turned off.
This mixture of stateful commands and environments can be exasperating.

Also, the input can include macro definitions and redefinitions.
Macros can be recursive. There are ``\if`` constructs.
It's a Turing complete programming language, which makes some aspects quite complicated.

Producing a book is goes beyond built-in ``manual`` or ``howto`` document classes Sphinx offers.
The various book classes decompose the content into three kinds:

-   Front Matter. Some combination of Half-Title, Publisher, Acknowledgments, Contents, Forward, Prefix, Table of Contents, etc. (Once upon a time, books started with a "title page" that had the title, publisher, and copyright information. Now, most software is setup to create a paper title page in front of that, called a half-title, separate from the cover.)

-   Main Matter. The parts and chapters.

-   Back Matter. Appendices, indices, glossary, about the author, etc.

In addition to this, a preamble is used to define the various commands and environments.
Ideally, the ``main.tex`` file is a sequence of ``\input`` commands to build the preamble,
define the document environment, provide the needed commands, and input
the various pieces content from separate files. Ideally.

Pragmatically, Sphinx doesn't have a perfectly clean separation of the LaTeX organization
from the content.
Some of this is a consequence of the way LaTeX works, and the need for ``\if--\fi`` blocks
to handle special cases.
Other aspects are patches for subtle incompatibilities among LaTeX packages.

Latex Content
--------------

First, the top-level ``index.rst`` should have **almost** nothing in it.

..  code-block:: rst

    .. toctree::
       :maxdepth: 2

       front/index
       chapters/index
       back/index

The book will have three folders: ``front``, ``chapters``, and ``back``, each of
which has it's own ``index.rst``.

There are a few (very few) places where LaTeX-specific content is needed.
Here's the ``back/index.rst``.

..  code-block:: rst

    ..  raw:: latex

        \frontmatter

    ..  toctree::

        preface

That's it. Include the raw LaTeX command, and include the ``preface.rst`` file.
This generates nice-looking HTML and EPUB. And it injects the helpful ``\frontmatter`` in front of the preface.
The ``back/index.rst`` is similar, as is the ``chapters/index.rst``.

(The front matter setup doesn't seem ideal. I think the ``\frontmatter`` should include the half-title, publisher's page, and contents, also, but it doesn't seem to work unless it's in front of the preface.)

The Sphinx Configuration
------------------------

There are four configuration variables that need to be set.

:latex_engine:
    ``'xelatex'`` works well because it permits UTF encoded files and (some) Unicode.

:latex_elements:
    This is a large dictionary of individual settings. The value is a dictionary, wrapped in ``{}``,
    with string key values. Most of the values will be LaTeX commands.
    Because LaTeX uses ``\``, it's helpful to use ``r""" """`` around the LaTeX.

:latex_theme:
    ``'manual'`` is close to the book format we want to use. We'll provide a subsequent definition to expand on this. The "theme" in Sphinx parlance is the document class in LaTeX world.

:latex_toplevel_sectioning:
    ``'chapter'`` for books without parts. Otherwise ``'part'``.

:latex_docclass:
    This is a mapping from document class to the actual LaTeX class to use.
    We provide the value ``{'manual': 'scrbook'}`` because that seems to work well.

Within the ``latex_elements`` mapping, we have a number of configuration parameters.
Most of these are small-ish. Two are immensee blocks of LaTeX code.

:babel:
    I use ``r'\usepackage[american]{babel}'`` because, well, I'm an American writer.

:fncychap:
    Set to ``''`` to disable any of the fancy chapter styles. They seem busy to me.

:passoptionstopackages:
    I use ``r'\PassOptionsToPackage{headings}{fancyhdr}'``, even though I'm not sure this is really required.

:extrapackages:
    This is a bunch of ``\usepackage`` commands. I use ``lettrine``, ``xstring``, and ``afterpage``.

:preamble:
    This is huge, we'll return to it.

:fvset:
    This can be used to set the font for "fancyverb" verbatime environments.
    I use ``r'\fvset{fontsize=\scriptsize}'`` to make the font smaller so the examples fit
    in a :math:`6^{\prime\prime} \times 9^{\prime\prime}` book.

:releasename:
    This is really fussy. The word "release" seems too long, so I set this to ``v.``.

:geometry:
    This defines the page layouts. It's quite long.
    ``r'\usepackage[paperwidth=6in, paperheight=9in, inner=3.75pc, outer=3pc, top=2pc, bottom=3pc, includehead, includefoot, headheight=32pt]{geometry}'``

    The ``pc`` unit is pica, :math:`\tfrac{1}{6}` of an inch. I'm not sure it's helpful to switch units like this.

:maketitle:
    This is also quite large.

The Preamble
------------

The preamble adds style details. It's a large block of LaTeX.

..  code-block:: latex

        % Lettrine
        \newcommand{\DUrolelettrine}[1]{\StrLeft{#1}{1}[\First]\StrGobbleLeft{#1}{1}[\Rest]\lettrine{\First}{\Rest}}
        % Page Layout Normal
        \makeatletter
        \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[RO]{{\rmfamily\thepage}}
        \fancyfoot[LO]{{\rmfamily\nouppercase{\rightmark}}}
        \fancyhead[RO]{{\rmfamily \@title\sphinxheadercomma\py@release}}
        \if@twoside
         \fancyfoot[LE]{{\rmfamily\thepage}}
         \fancyfoot[RE]{{\rmfamily\nouppercase{\rightmark}}}
         \fancyhead[LE]{{\rmfamily \@title\sphinxheadercomma\py@release}}
        \fi
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
        % define chaptermark with \@chappos when \@chappos is available for Japanese
        \ltx@ifundefined{@chappos}{}
          {\def\chaptermark##1{\markboth{\@chapapp\space\thechapter\space\@chappos\space ##1}{}}}
        }
        % Page Layout Plain (1st page of Section or Chapter.)
        \fancypagestyle{plain}{
            \fancyhf{}
            \fancyfoot[RO]{{\rmfamily\thepage}}
            \if@twoside\fancyfoot[LE]{{\rmfamily\thepage}}\fi
            \renewcommand{\headrulewidth}{0pt}
            \renewcommand{\footrulewidth}{0.4pt}
        }
        \makeatother
        % Blank Page
        \newcommand{\blankpage}{%
            \afterpage{\null\thispagestyle{empty}\newpage}{\pagestyle{empty}\cleardoublepage}
        }
        % Define "myquotation" to indent a whole paragraph with a big, fancy " character.
        \renewcommand{\indent}{%
            \begin{picture}(0,0)\put(10,-5){\makebox(0,0){\scalebox{6}{\textcolor{lightgray}{“}}}}\end{picture}\hspace*{1.0cm}\hangindent=1.15cm
        }
        \newenvironment{sphinxclassmyquotation}{\indent}{}

The ``DUrolelettrine`` command is the Docutils role that is used
to define the ``lettrine`` role that we added as an extension to Sphinx.
The ``DUrole`` is prepended to define a unique command.
The implementation of this command is a macro that splits out the first letter to make it big, and the
rest of the text is set in small-caps style.

Two page layouts are defined: ``normal`` and ``plain``.
These revise the built-in Sphinx layouts to use different fonts for the page header and footer.
The definitions have to be wedged between ``\makeatnormal`` and ``\makeatother``.

The ``blankpage`` command is added here. It seems helpful for getting the even-odd page business
correct on the half-title and publisher pages.

The ``sphinxclassmyquotation`` environment is what Sphinx does with otherwise unknown directives.
When the text has a ``..  myquotation::`` directive, this becomes a new environment with a distinctive
name. We can then define an environment that provides the distinctive style attributes
for the content.

The mapping from RST role or directive to ``DUrole`` or ``sphinxclass`` isn't the most obvious,
but, it works delightfully well.
For HTML and EPUB, CSS definitions are required.
For LaTeX, these preamble definitions are required.

The MakeTitle Command
-----------------------

While LaTeX has a ``\maketitle`` command, there's a redefinition of this by Sphinx.
This is the ``\sphinxmaketitle`` command that emits the title page.

Ordinarily -- for the default manual or howto themes -- this is followed by the table of contents,
and then the content.
For books, the title page isn't the cover, and is demoted to being called a half-title.
There's often a publisher's page -- with important copyright information -- between the half-title page and the table of contents.

To build this, we need to provide a ``maketitle`` setting that **also** defines
a ``sphinxbackoftitlepage`` command. This command does everything between the half-page and the table of contents.

..  code-block:: latex

        \makeatletter
        \newcommand\sphinxbackoftitlepage{
            % Blank page on the verso after 1/2 title
            \blankpage
            % Publisher page is recto (odd page)
            \thispagestyle{empty}
            \sffamily\textbf{\textsc{Building Skills}}

            \Huge{\sffamily\textbf{\@title}}

            \large{"When your only tool is a hammer, every problem looks like a nail."}

            \normalsize
            By \@author

            \vspace{1in}
            Python 3.12\
            Release \py@release\
            Created \today

            \vfill
            \rmfamily\normalsize{
                \copyright~\the\year\ \textit{Steven F. Lott}\
                \textsc{All Rights Reserved.}
            }

            \vfill
            \url{https://fosstodon.org/@slott56}\
            \url{https://itmaybeahack.com}\
            \url{https://github.com/slott56/unlearning-sql}

            % Blank page on verso of publisher.
            \blankpage
            % Contents will follow.
        }
        \makeatother

        \sphinxmaketitle

It seems odd to put this definition here instead of in the preamble.
It also seems necessary to get the page numbering correct.

Summary
=======

On one hand, there is a **lot** of LaTeX customization required.

On the other hand, a single change to the RST files leads to two **identical** results
that can be uploaded for EPUB and print-on-demand.

There are still some odd, little glitches in the LaTeX.
It's not **perfect**, but it's really good.
