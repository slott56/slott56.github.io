This sounds complicated, because it is
======================================

:date: 2009-05-20 07:25
:tags: RST,sphinx,#python,jinja,HTML,cheetah
:slug: 2009_05_20-this_sounds_complicated_because_it_is
:category: Technologies
:status: published

For a while, I generated documentation with
`Cheetah <http://www.cheetahtemplate.org/>`__. I wrote bodies as a
fragment of HTML and used Cheetah to wrap those bodies in standard
templates with navigation and branding.
To write my books, I learned `DocBook <http://www.docbook.org/>`__
markup and used `DocBook XSL <http://www.sagehill.net/docbookxsl/>`__
tools to create HTML and PDF versions of the book's text. Even though
XML is hard to work with, I managed to muddle through. It's painful --
at times -- but doable.

    [Eventually, I found XMLMind's `XML
    Editor <http://www.xmlmind.com/xmleditor/>`__.  It rocks.  But that's
    off-topic.]

Then, I fount `RST <http://docutils.sourceforge.net/rst.html>`__ and
`RST2HTML <http://docutils.sourceforge.net/docs/user/tools.html#rst2html-py>`__.
For a while, I wrote my documentation in RST and used a simple
script to create the HTML version of the documentation from RST
source.

Why ReStructuredText?
---------------------

From their site: "reStructuredText is an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax".

-   Easy-to-Read.  The markup is very, very simple.  Mostly spacing
    and simple quoting.  Yet, for edge cases, there is enough richness
    to approach DocBook XML.

-   WYSIWYG.  The markup doesn't get in the way; you write the text
    with a few conventions for spacing and quoting.

-   Plain Text.  A few spacing and quoting rules are used to
    distinguish structure from content.  Presentation is a limited
    part RST (like HTML where some presentation is present in the
    structural markup, but can be avoided.)

RST lead me, eventually to `Sphinx <http://sphinx.pocoo.org/>`__.

The Secret of Sphinx
--------------------

Sphinx is RST-based markup.  You write in plaintext (plus some
quoting and spacing) and you get an elegant HTML web site with
inter-document references all resolved correctly, contents,
indexes, auto-generated API documentation for your Python
software, syntax coloring, everything.  Wow.

I can't stop myself from doing everything in Sphinx.  You create a
development structure for your source files.  You use a series of
toctree directives to build the resulting documentation structure
that people will see and use.

I've decided to convert some ancient Cheetah-based stuff to
Sphinx.

Unmarking Up
------------

Revising HTML-based document bodies to RST is annoying.  It can be
done with `Beautiful
Soup <http://www.crummy.com/software/BeautifulSoup/>`__.  The HTML
is pretty regular (and pretty simple) so it wouldn't be too bad.
Except for a bunch of edge cases that have significant
complexity.

The original Cheetah-based site wasn't purely documentation.  It
doesn't fit the Sphinx use cases perfectly.  A fairly significant
percentage of the Cheetah-based pages are HTML pages with complex,
embedded applets to do calculations.

These pages are not -- strictly speaking -- documentation.
They're an application.  They contain markup (<embed> mostly)
that RST can't generate.  Further, they have to be unit tested
prior to running Sphinx to build the documentation, since the HTML
is actually part of the application.

Raw HTML?
---------

The applet pages are -- more or less -- raw HTML pages that need
to be folded in with the Sphinx-generated documentation.  Sphinx
has an HTML_STATIC_PATH configuration parameter that can copy
these applications from project folders into destination
directories.

But this leaves me with dozens of Cheetah-generated pages as part
of this application.  The presence of Cheetah in the midst this
Sphinx operation makes things complicated.

Or, perhaps it doesn't.

It turns out that Sphinx is built on
`Jinja <http://jinja.pocoo.org/2/>`__.  There's a template engine
under the hood!  That's handy.  That lets me build the application
HTML with a slightly different template engine; one that's
compatible with the rest of the Sphinx-generated site.

I think I've got a clean, RST-based replacement for my lovingly
hand-crafted HTML.  It's a lot of rework, but the simplification
is of immense value.





