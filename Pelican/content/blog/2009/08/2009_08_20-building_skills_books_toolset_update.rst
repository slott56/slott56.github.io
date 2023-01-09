Building Skills Books Toolset (Update)
======================================

:date: 2009-08-20 07:58
:tags: pdf,RST,xml,LaTeX,xhtml
:slug: 2009_08_20-building_skills_books_toolset_update
:category: Technologies
:status: published

I wrote the first `Building
Skills <http://homepage.mac.com/s_lott/books/index.html>`__ books using
`Appleworks <http://www.apple.com/support/appleworks/>`__. It wasn't too
bad to organize the styles around basic semantics of the subject area.
It's an easy, productive writing environment. Except, of course, for
internal cross-references, indexes, and tables of contents.

I converted to `DocBook XML <http://www.docbook.org/>`__ markup. The
conversion was arduous, but well worth it. I got better semantic
markup. I used the `DocBook
XSL <http://www.sagehill.net/docbookxsl/>`__ tools to convert to HTML
both as a single document, and a chunked presentation. It worked out
pretty well.

Two things don't work out well. First, the FOP processing is shaky.
The books are big, and rather complex, with a fair number of embedded
fonts. I have been unable to get the embedded fonts to work correctly
with FOP.

The second thing that doesn't work out well is the language-specific
markup. DocBook is biased toward C. There aren't enough tags for
Python markup (module and library tags are missing, for example) and
the syntax-oriented statement, class and function markup is all over
the map in DocBook.

**Objectives**

My goal is to have the books in four formats: XML, single HTML file,
chunked HTML and PDF. Of these, the single HTML is the least
appealing. The chunked HTML is a great carrier for Adsense ads. The
PDF is what I should be selling.

I don't mind writing in XML. Using XMLMind
`XMLEditor <http://www.xmlmind.com/xmleditor/>`__ is generally pretty
nice. Running the XSL-based tool chain to convert to HTML, and
chunked HTML is easy.

Currently, I'm using FireFox to create the PDF. It's quick, but
dirty. I'm not sure how many of the print-formatting CSS options
FireFox can handle, so I haven't really customized the CSS for
printing. However, the FireFox PDF has properly embedded fonts and
cross-reference links.

**Choices**

Apple's `Pages <http://www.apple.com/iwork/pages/>`__ does a lot.
It's a very nice product. But I'm not sure that the PDF and Chunked
HTML will work out all that well.

The DocBook tool chain has problems identified above. The PDF output
doesn't work because it overwhelms FOP.

-   Currently, I use FireFox to create PDF's. I could dress up the CSS
    to make it look a little better.

-   An alternative is to use `Pisa <http://www.xhtml2pdf.com/>`__ to
    transform the XHTML into PDF. I started using `Flying
    Saucer <https://xhtmlrenderer.dev.java.net/>`__ on `another
    project <{filename}/blog/2009/07/2009_07_11-flying_saucer.rst>`__
    and the XHTML to PDF idea has some appeal. This requires debugging
    the print-media CSS, which doesn't seem too bad.

On the other hand, `RST <http://docutils.sourceforge.net/rst.html>`__
can have almost all the `semantic
richness <{filename}/blog/2009/06/2009_06_24-semantic_markup_rst_vs_xml.rst>`__
of XML. I've decided to redo Building Skills in Programming entirely
in `Sphinx <http://sphinx.pocoo.org/>`__, using RST. This has the
advantage of being Python-specific, making heavy use of
`pygments <http://pygments.org/>`__ for syntax coloring.

Also, I could stick with XML and use a different tool-chain to go
from DocBook XML LaTeX. The
`dblatex <http://dblatex.sourceforge.net/>`__ package may do this
nicely.

**Tradeoffs**

If I switch to Sphinx, editing is much easier. The source is plain
text.

The chunked HTML created by Sphinx is outstanding. It's far better
than the DocBook HTML. It's much easier to customize than the DocBook
XSL, allowing use of Adsense ads with relatively little work.

On the other hand, to produce PDF, I have to go through LaTeX. This
means that I have to find a nice LaTeX to PDF tool.

Currently, Sphinx doesn't easily produce a single HTML file. There
may be ways around this; perhaps by using an alternate \`..
toctree::\` directive. But this is also a low-priority requirement,
so this may have to be dropped in favor of a better-looking PDF page.

**LaTeX to PDF**

A Google search for "mac os x latex to pdf" turns up some interesting
results.

- http://www.math.toronto.edu/joel/tex/

- http://www.math.wisc.edu/~andrejko/resources/LaTex-on-Mac-OSX.html

This list of references makes it look appealing to start with
`TeXShop <http://www.uoregon.edu/%7Ekoch/texshop/texshop.html>`__ and
seeing if the LaTeX output from Sphinx can be used to produce PDF.

The `TeXLive <http://ii2.sourceforge.net/tex-index.html>`__
distribution includes a basic pdfTeX utility that might emit a nice
PDF from the Sphinx LaTeX output.

Additionally, there is `iTeXMac <http://itexmac.sourceforge.net/>`__,
which may also convert my Sphinx LaTeX to PDF.

These, however, seem to be largely WYSIWYG editing. While editing
LaTeX isn't too bad, I want to work from a single RST source.

**Python Solutions**

The "python latex to pdf" Google search turns up the following
projects for doing LaTeX processing in Python. These look very nice.
In particular, they get away from manual editing of LaTeX.

- `plasTeX <http://plastex.sourceforge.net/>`__

- `pdfTeX <http://www.tug.org/applications/pdftex/>`__

**Better Still**

Finally, I located the following:
http://jimmyg.org/blog/2009/sphinx-pdf-generation-with-latex.html.
This makes it clear that Sphinx expects
`TeXLive <http://www.tug.org/texlive/>`__. This leads me to
`MacTeX <http://www.tug.org/mactex/>`__, which -- it appears -- is
what Sphinx expects.

Sphinx generates a makefile to create PDF from the LaTeX. Hopefully,
this is not highly Linux-specific and will use the TeXlive
distribution on Mac OS X.

**Bonus Feature**

Switching to LaTeX may also give me a better way to handle the
formulas in the exercise sections. Currently, I have to write them
and save the images. I don't know how many different equation editors
I've used.

**Alternative RST to PDF**

There's an `rst2pdf <http://code.google.com/p/rst2pdf/>`__ tool that
may make it possible to go from Sphinx RST directly to PDF.
Hopefully, this honors all the Sphinx extensions.



-----

Why the fear of Latex?  As far as markup languages...
-----------------------------------------------------

Benjamin<noreply@blogger.com>

2009-08-19 00:24:58.745000-04:00

Why the fear of Latex? As far as markup languages go, it's pretty damned
solid, especially if you want to use anything but the simplest
equations. In the world of mathematical publishing, it's the de facto
standard, and for good reason.

Considering that you're actually contemplating messing with CSS in order
to get Firefox to produce pdfs, using a markup language designed to
produce publishable quality documents and a tool designed to convert
those documents to pdf while maintaining that quality sounds like the
simpler and saner solution to me. In fact, I wonder if a better solution
for you, overall, would be to find some software that builds
satisfactory html from latex. Then again, my background is as a
sys-admin, so we may have differing opinions of 'satisfactory html.' (I
suspect dvi2html's method of producing images of the text wouldn't quite
cut it for your purposes.)


Maybe you can use Sphinx for pdf generation withou...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-08-19 07:06:41.459000-04:00

Maybe you can use Sphinx for pdf generation without latex.

Roberto Alsina's rst2pdf can be used as pdf producer in sphinx, as he
wrote in hes blog before. Maybe it's not mature enough at this moment,
but if you cooperate with him, he can get a good test material (your
books) to work with :)





