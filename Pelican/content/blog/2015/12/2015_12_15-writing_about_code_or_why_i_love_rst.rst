Writing About Code -- Or -- Why I love RST
==========================================

:date: 2015-12-15 08:00
:tags: PyLit
:slug: 2015_12_15-writing_about_code_or_why_i_love_rst
:category: literate programming
:status: published


I blog. I write books. I write code. There are profound tool-chain
issues in all three of these. Mostly, I'm tired of shabby "What You
See Is All You Get" editing.

First. I use this blogger site as well as a
`Jive-based <https://www.jivesoftware.com/>`__ site at work. They're
handy. But. There are a lot of issues. A lot. Web-based editing leaves
a lot to be desired.

Second. Books. `Packt <https://www.packtpub.com/>`__ requires MS-Word
for drafts. The idea here is that authors, editors, and reviewers
should all use a single tool. I push the boundaries by using `Libre
Office <https://www.libreoffice.org/>`__ and `Open
Office <https://www.openoffice.org/>`__. This works out most of the
time, since these tools will absorb the MS-office style sheet that
Packt uses. It doesn't work out well for typesetting math, but the
technical editors are good about tracking down the formulae when they
get lost in the conversions. These over-wrought do-too-much word
processing nightmares leave a lot to be desired.

Third. Code. I use `ActiveState Komodo
Edit <http://komodoide.com/komodo-edit/>`__.  Both at work and outside
of work. This rocks.

Web-Based Editing Fail
----------------------


What's wrong with Jive or Blogger? The stark contrast between
JavaScript-based text edit tools and HTML. It's either too little
control or too much detail.

The JS-based editors are fine for simple, running text. They're
actually kind of nice for that. Simple styles. Maybe a heading here or
there.

Code? Ugh. Epic Fail.

It gets worse.

I've become a real fan of semantic markup.
`DocBook <https://en.wikipedia.org/wiki/DocBook>`__ has a rich set of
constructs available.
`RST <http://docutils.sourceforge.net/rst.html>`__, similarly, has a
short list of text roles that can be expanded to include the same kind
of rich markup as DocBook. `Sphinx <http://sphinx-doc.org/>`__
leverages these roles to allow very sophisticated references to code
from text. `LaTeX <https://www.latex-project.org/>`__ has a great deal
of `semantic
markup <http://www.informit.com/articles/article.aspx?p=675273>`__.

Web-based editors lack any of this. We have HTML. We have HTML
`microformats <http://microformats.org/>`__ available. But. For a
JavaScript web editor, we're really asking for a lot. More than seems
possible for a quick download.

Desktop Tool Fail
-----------------


What's wrong with desktop tools? We have very rich style sheets
available. We should be able to define a useful set of styles and
produce a useful document. Right?

Sadly, it's not easy.

First, the desktop tools are extremely tolerant of totally messed-up
markup. They're focus is explicitly on making it look acceptable. It
doesn't have to be well-structured. It just has to look good.

Second, and more important, the file formats are almost utterly
opaque. Yes. There are standards now. Yes. It's all just XML. No. It's
still nearly impossible to process. Try it.

Most word-processing documents feel like XML serializations of
in-memory data structures. It's possible to locate the relevant
document text in there somewhere. It's not like they're being
intentionally obscure. But they're obscure.

Third, and most important, is the reliance on either complex GUI
gestures (pointing and clicking and what-not) or complex keyboard
"shortcuts" and stand-ins for GUI gestures. It might be possible to
use that row of F-keys to define some kinds of short-cuts that might
be helpful. But there's a lot of semantic markup and only a dozen
keys, some of which have common interpretations for help, copy, paste,
turn off the keyboard lights, play music, etc.

The Literate Programming ideal is to have the words and the code
existing cheek by jowls. No big separation. No hyper-complex tooling.
To me, this means sensible pure-text in-line markup.

Text Markup
-----------


I find that I really like RST markup. The more I write, the more I
like it.


I really like the idea of writing code/documentation in a simple,
uniform code-centric tooling. The pure-text world using RST pure-text
markup is delightfully simple.


#.  Write stuff. Words. Code. Whatever. Use RST markup to segregate
    the formal language (e.g. Python) from the natural language (e.g.,
    English in my case.)

#.  Click on some icon the right side of the screen (or maybe use an
    F-key) to run the test suite.

#.  Click on some icon (or hit a key) to produce prettified HTML page
    from
    ``python3 -m pylit3 doc.py doc.rst; rst2html.py doc.rst doc.html``.
    Having a simple toolchain to emit doc from code (or emit code from
    doc) is a delight.


The genesis for this blog post was an at-work blog post (in Jive)
that had a code error in it. Because of Jive's code markup features
(using non-breaking spaces everywhere) there's no easy copy-and-paste
to check syntax. It's nearly impossible to get the code off the web
page in a form that's useful.

If people can't copy-and-paste the code, the blog posts are
approximately worthless. Sigh.

If I rewrite the whole thing into RST, I lose the Jive-friendly
markup. Now it looks out-of-place, but is technically correct.

Either. Or.

Exclusive Xor.

Ugh. Does this mean I have to think about gathering the Jive .CSS
files, and create a version of those that's compatible with the
classes and ID's that Docutils uses?  I have some doubts about making
this work, since the classes and ID's might have overlaps that cause
problems.

Or. Do I have to publish on some small web-server at work, and use
the ``<iframe>`` tag to include RST-built content on the main
intranet? This probably works the best. But it leads to a multi-step
dance of writing, publishing on a private server, and then using a
iframe on the main intranet site. It seems needlessly complex.





