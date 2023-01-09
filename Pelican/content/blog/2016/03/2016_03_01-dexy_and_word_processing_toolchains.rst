Dexy and word-processing toolchains
===================================

:date: 2016-03-01 08:00
:tags: RST,#python,LaTeX,xml
:slug: 2016_03_01-dexy_and_word_processing_toolchains
:category: Technologies
:status: published

See `http://www.dexy.it <http://www.dexy.it/>`__
Wow. That seems cool.
I write. A lot.
I've tried a lot of tool chains. A lot. And I mean non-trivial "try".
Whole books.  Hundreds of pages.
`LEO <https://pypi.python.org/pypi/leo/5.1>`__ + my own HTML Templates.
A lot of fun at first.  An outliner that generates RST is a very, very
handy thing for technical writing.
An XML editor (I forget which one. Maybe
http://www.xmlmind.com/xmleditor/?) with the
`DocBook <https://en.wikipedia.org/wiki/DocBook>`__ XML and XSLT
tool-chain. This produced HTML from the XML. I think it could also
produce LaTeX. Again, the outlining and structuring were kind of handy.
What was particularly cool was the diverse semantic markup tags
available in DocBook. Getting the tag containment right was a large pain
even with a handy GUI editor.
Plain Text using RST "the hard way;" i.e., without LEO. This isn't too
bad, it turns out. The outlining features of LEO -- while fun -- aren't
essential. A simple RST toolchain is easy to concoct. I used
`SCONS <http://scons.org/>`__ to rebuild HTML and LaTeX from the RST.
LaTeX. Once I had the base LaTeX from RST, I could then edit that to
produce an even richer document using lots of LaTeX add-on packages. I
use `MacTex <https://tug.org/mactex/>`__ and it is truly great. The
downside of LaTex -- for me -- was no *trivial* way to go back to HTML
from the LaTeX.  There are some complex back-and-forth toolchains, but
it's easier to just produce a PDF. PDF looks great, but wasn't really my
goal.
RST with Sphinx. Wow. This **is** elegant. I often produce chapter
drafts here, and then copy and paste the HTML into the word processors
preferred by the publishing industry.
[*They insist on applying their goofy markup templates to the text. It's
a subset of meaningful semantic markup used by Sphinx, but somehow their
toolchain must start with .DOCX files, and nothing else will do*.]
Dexy was cool right up until I read this: "Dexy is a Python package
(Python 2.6-2.7 only)".
Ouch. Web.py Utilities include DBUtils which won't install under Python
3.5. So that put the kibosh on Dexy. Sadface.





