Editing DocBook XML
===================

:date: 2007-02-02 12:03
:tags: books,docbook,xml
:slug: 2007_02_02-editing_docbook_xml
:category: Technologies
:status: published





First, I wrote a book on `Programming with Python <http://www.itmaybeahack.com/homepage/books/python.html>`_.
It was back in the Python 2.0 days (2001 or thereabouts.)  I used `AppleWorks <http://www.apple.com/appleworks/>`_,
and it was fun.  Write all you want,
put in formulae, code samples, everything.  A few style sheets to give it a
reasonable look and I was happy with it.  There's no market for a book on
Python, but it was more a book about programming than about Python.  There's
even less of a market for that.



There may be no market for a book on programming, but I teach programming.  I've
taught programming in C, Ada, Java, PL/SQL, COBOL and Python.  So, I have a
pretty standard approach to programming, into which I plug the language.  It
works very well, and capturing the approach in a book was
helpful.



Then I re-discovered DocBook markup.  I say rediscovered because in the mid-90's, I learned SGML, and was
aware of DocBook.  I'd ignored it partly because there wasn't any affordable
tooling, but also because SGML is a pain in the ass to write.  SGML isn't as
painful as XML, but the differences are microscopic when compared with WYSIWYG
AppleWorks.



Enter LEO
---------



Meanwhile, as part of
developing a second book on `Object-Oriented Design <http://www.itmaybeahack.com/homepage/books/oodesign.html>`_ , I made serious use of
Literate Programming (LP).  I tried a number of tools, discarding many of them
as inappropriate for OO programming.  Many LP tools carry too much of the
original Web/Weave technology forward and provide too-complex macro
pre-processing features.  I found some minimalist tools (like `nuweb
and noweb <http://www.literateprogramming.com/tools.html>`_ ) and wrote my own pyWeb, which was even
simpler.



But a pyWeb/HTML document is
still a pain to produce because of the flatness of the source file.  I want an
editor that respects my outline, and I was creating documents that were
essentially flat text.  Yes, they would become HTML, which (because of
``<h``\ *x*\ ``>`` tags) reflects an outline.  But I wasn't able to use an outliner successfully to
create them.  Once it got respectably big, editing the pyWeb/HTML wasn't all
that easy and didn't provide any real intellectual
leverage.



Then I hit on using `LEO <http://webpages.charter.net/edreamleo/front.html>`_  to create pyWeb documents.  Which, after a
little experimentation, proved to be kind of silly.  LEO's RST module makes
emitting a pyWeb document redundant.  LEO can, with some care, emit a
nice-looking HTML document as well as the needed code files.  There's a bit of
jockeying around required to allow the author to mix and match non-code
documentation with code blocks, but it can be made to work.  LEO replaced the
pyWeb file rather than helping to build
it.



DocBook is Code
---------------



While using LEO to produce
pyWeb is silly, using LEO to produce a complex DocBook project is much more
sensible.  The exact features of LEO that let it produce complex code projects
helped me produce complex writing projects.  Indeed, the presence of the
outliner made writing something as complex as a programming book
possible.



Outliners introduce their own
problems, but it was a huge intellectual lever.  I could produce a DocBook 3.1
XML file, run the Xalan-based `DocBook XSL <http://docbook.sourceforge.net/>`_  transformations
(version 1.66, later 1.68) to create HTML and FO, and use `Apache
FOP <http://xmlgraphics.apache.org/fop/>`_  to produce PDF.  It was
marvelous.



The problem that an outliner
introduces is the Deep Digression problem.  You can open another level of the
outline, presuming that the nested context is useful and helpful.  It turns out
that it isn't.  You think of it as depth when you start: your reader sees it as
an incomprehensible digression.  Other than legal documents and software, most
things must be relatively flat and rely on a narrative arc and explicit
signposts along the way.  An outline more than a few levels deep is uselessly
baffling.



DocBook 5
---------



DocBook hasn't stood still since
the 3.1 days.   Indeed, 3.1 didn't properly achieve standard status; 4.1 and 4.5
were accepted by `OASIS <http://www.oasis-open.org>`_  as standards.  However, I stuck with my
3.1 technology stack because I'd customized my stylesheets to handle Python
correctly, and didn't want to migrate those changes into version 1.72 of the
XSL.



However, there are now some XML
editing solutions that look far nicer than my LEO-based technology stack.  The
`DocBook 5.0 Transition Guide <http://www.docbook.org/docs/howto/>`_  was enlightening.

-   `GNU Emacs <http://www.gnu.org/software/emacs/emacs.html>`_  and
    the `nXML mode <http://www.thaiopensource.com/nxml-mode/>`_  add-on.

-   `oXygen <http://www.oxygenxml.com/>`_  provides an XML editor that recognizes
    and exploits the DocBook schema.

-   `XMLMind XML Editor <http://www.xmlmind.com/xmleditor/>`_  (XXE) also works
    nicely.  The standard edition is free, and
    produces files which go through my Xalan technology stack. 




So far, the XXE solution is marvelous.











