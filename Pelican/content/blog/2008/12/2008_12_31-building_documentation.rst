Building Documentation
======================

:date: 2008-12-31 23:17
:tags: FOSS,open-source
:slug: 2008_12_31-building_documentation
:category: FOSS
:status: published







For years, I've written documentation using `ReStructured Text <http://docutils.sourceforge.net/rst.html>`_  (RST).  It's just one of several "`lightweight markup languages <http://en.wikipedia.org/wiki/Lightweight_markup_language>`_ ".  For others, look at `Markdown <http://daringfireball.net/projects/markdown/syntax>`_ , `StructuredText <http://dev.zope.org/Members/jim/StructuredTextWiki/FrontPage/>`_ , `Setext <http://docutils.sourceforge.net/mirror/setext.html>`_ , among many others.



I generally use the `rst2html <http://docutils.sourceforge.net/docs/user/tools.html#rst2html-py>`_  utility that comes with `Docutils <http://docutils.sourceforge.net/>`_ .  It works fine for small things.



I just read about the `Sphinx <http://sphinx.pocoo.org/>`_  documentation generator and I am totally hooked.



I spent a productive day making a bunch of small revisions to a big library of documentation to move it from some home-brewed rst2html tooling into Sphinx.  I got to delete some boilerplate markup from a lot of files, delete some tools, and generally tidy up.



:strong:`API Documentation`



Sphinx says that they don't produce API docs.  They're not `epydoc <http://epydoc.sourceforge.net/>`_ .



Previously, all of my internal API documentation was done using `epytext <http://epydoc.sourceforge.net/manual-epytext.html>`_ , but not for a great reason.  Because Sphinx works in RST, I need to convert my internal documentation from epytext to RST.



At first, this looked painful.  However, 90% of the changes are from @param this: some text to :param this: some text.  The other 10% are some massaging of @todo: and @note:; partly to change ``@todo:`` to ``:todo:`` but also to change the indentation to RST rules.



:strong:`Organizational Issues`



My original home-brewed documentation had lots of complex cross-references.  However, I couldn't bear the idea of putting all of the documents into some rational directory structure because all the links would break.



Sphinx tacks references across files, allowing me to define a name in one file and reference it in another.  Problem solved.  I can arrange and rearrange the components into an outline that actually makes sense for maintenance and management.



And nothing beats semantically rich pure text markup of RST as implemented by Sphinx.  Documentation is fun when there are no barriers to entry.




