ReStructured Text markup and Content Management
===============================================

:date: 2009-05-25 11:40
:tags: RST,xml,sgml,HTML
:slug: 2009_05_25-restructured_text_markup_and_content_management
:category: Technologies
:status: published

I can't say enough good things about ReStructuredText (RST).  I've
used all of the available markup languages (SGML, HTML and XML).
They have their place, but they all fall short of being truly
usable.

In `This sounds complicated, because it
is <{filename}/blog/2009/05/2009_05_20-this_sounds_complicated_because_it_is.rst>`__ I
reviewed some of my history of cheap content management.

In looking at content of all kinds, I'm finding that RST is much,
much easier to work with than SGML, HTML or XML.  In short, I think
that RST makes the file system into a really good content management
system (CMS).  Unstructured content is a big win.  Structured content
is a "don't care".  But there's a middle ground of semi-structured
content that requires sophisticated semantic markup.

SGML At The Dawn Of Time

When the web started it's ascent (back in the 90's), I was lucky.  I had
already been working with folks that did military contracting, and folks
there had introduced me to
`SGML <http://www.webreference.com/dlab/books/html/3-2.html>`__.   When
I moved from SGML to HTML, I saw it as a pleasant simplification because
it had a more-or-less fixed DTD.

My first personal web pages were lovingly hand-crafted HTML
masterpieces.  (Okay, they were lovingly hand-crafted.)   There was
a lot of work involved in markup, cross-references, and
presentation.

HTML via a Class Hierarchy

My first templating was via proper Python classes.  I created class
hierarchies that embodied the page template and filled in required
data.  The heart of each class was an emit method that wrote the
final HTML.

Variant page layouts and special cases were easily handled by Python
simple inheritance.

Of course, the big problem is that HTML is just representation.
There's often some bleed-through between the problem domain model
and the HTML representation of that underlying model.  You don't want
your problem domain objects to encode any HTML.  You can have a
generic Tag class, but the Page class is specific to your problem
domain.

The Python class structure is nice, but it's only suitable for
structured content management.  When you have semi-structured and
unstructured data -- the strong suit of HTML -- you find the class
hierarchy to be too rigid.

Some time in the early 00's, I discovered
`Cheetah <http://www.cheetahtemplate.org/>`__.

HTML via Templates
-------------------

Cheetah (and template engines like
`Mako <http://www.makotemplates.org/docs/>`__,
`Jinja <http://jinja.pocoo.org/>`__, and `numerous
others <http://wiki.python.org/moin/Templating>`__) did what I
wanted.  A base template was -- effectively -- a superclass.  Each
block in that template could be overridden by a subclass.

The content, then, becomes a relatively simple template file that
extends a page layout.  You can handle unstructured and
semi-structured content very nicely.  I changed my ways of working
with HTML to leverage this elegant, extensible view of the world.  I
redid my `personal web
site <http://homepage.mac.com/s_lott/steve/>`__: the content become a
collection of Cheetah templates that contained all the content.

Note that I've \*added\* a markup language.  In addition to HTML, I
also have some Cheetah markup on each page.  While this got me
consistency and flexibility (and a reduction in the volume of stuff
on each page) it did make things slightly more complex.

Look at http://cadesignquilts.com/ for another example of an
all-Cheetah static site.  I did several sites like this.  The
workflow involved (1) design the overall page, (2) getting the data
into a usable form, (3) generating the page-level template files, and
(4) running Cheetah to emit HTML from the templates.  All static
content.  Runs like lightning.

The JSP Distraction
-------------------

Eventually, I started doing development with
`Struts <http://struts.apache.org/>`__, which depends heavily on
`JSP <http://struts.apache.org/primer.html#jsp>`__.  You have HTML
commingled with Java code.  Plus, you've got custom actions via a
`tag
library <http://java.sun.com/j2ee/tutorial/1_3-fcs/doc/JSPTags.html>`__
to extend JSP processing.  You can create page-level templates with a
reasonably smart JSP tag library.

This template solution doesn't work well for unstructured or
semi-structured data.  It's a pure programming solution.

DocBook XML and Semantic Markup
-------------------------------

I wrote `Building Skills in
Python <http://homepage.mac.com/s_lott/books/python.html>`__ entirely
in `Appleworks <http://www.apple.com/support/appleworks/>`__.  That
was pretty well unmaintainable and unpublishable in that form.

I converted the text to `DocBook <http://www.docbook.org/>`__ XML.  I
used the `Leo <http://webpages.charter.net/edreamleo/front.html>`__
outliner to manage the document as a whole.  I wrote my own
publishing workflow to transform the XML to HTML and PDF.   It worked
reasonably well.

More important, using DocBook reinforced the importance of semantic
markup.  It took me back to my SGML days.  It also showed why and
other HTML presentation things have to be moved out of the document
and into the stylesheet.

This was a very nice way to handle the semi-structured and
unstructured content in a book.  Direct use of XML is a pain in the
neck.  XML has a lot of syntax.  It's much nicer to do your thinking
with something lighter weight.

ReStructured Text (RST) for Unstructured Content
------------------------------------------------

Somewhere in the late 00's, I found Python's
`docutils <http://docutils.sourceforge.net/>`__ and
`RST <http://docutils.sourceforge.net/rst.html>`__.  I can't figure
out when I started -- precisely -- but using RST as part of content
management didn't fully click at first.

After reworking my personal site, which includes a lot of really
unstructured ("random" might be a better word) content, I'm seeing
the value in RST + Filesystem as a CMS.  I think the
`Sphinx <http://sphinx.pocoo.org/>`__ folks are right.  If you have a
simple markup system and all the filesystem tools that have evolved
over the past few decades, you're covered.

Further, on larger projects, I've found that I can pop out a nice
template documentation tree with a simple .. toctree:: directive on
the index.rst page and generate a tidy, complete documentation
package without much pain.

Structured Content
-------------------

For structured data, you have ordinary classes and programs.  You
have SQL databases, ORM to map to classes; all of that technology.
It's easy to write applications that emit RST which you can then
publish.

Most structured content can be boiled down to tables and charts.
The .. csv-table:: directive makes it easy to have an application
emit data that you fold into a more elegant-looking report.

The Nuance -- Semi-Structured Data
-----------------------------------

My worst-case scenarios are my résumés: sailing, programming and
writing.  The data has deep semantic meaning:  it isn't just words.
On the other hand, the data has lots of special-cases and
exceptions: it isn't totally amenable to a database.

The absolute best part of docutils is that the parser's output is
available for processing.  You can -- easily -- add
`directives <http://docutils.sourceforge.net/docs/howto/rst-directives.html>`__
and `text
roles <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`__
to create semantic meaning.

I experimented with XML and YAML for my résumés.  The XML is
cumbersome.  The YAML requires a fairly sophisticated class model to
make use of the information.

RST with a few text roles, however, rocks.  The .. role:: directive
makes it easy to throw roles into a document for later use by
applications.







