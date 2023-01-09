Powerpoint Alternatives
=======================

:date: 2006-06-26 15:51
:tags: books,docbook,xml
:slug: 2006_06_26-powerpoint_alternatives
:category: Technologies
:status: published





PPT has one big advantage: it is written by the
same people who wrote Windows.  So it can seize the Windows display and
keyboard, and take control over the entire UI.  I happen to think that's A Bad
Thing™ but I may be in the minority on
that.



Of course, it isn't portable to
Mac OS or Linux.  It depends on the OS.  Who wants to figure out the nuances of
the Mac OS or  Linux display libraries to provide portable functionality
equivalent to Powerpoint?



It has a
proprietary file format making it difficult to work with.  That's -- perhaps --
a more important problem.



So, what are
the alternatives?



OpenOffice/StarOffice
`Impress <http://www.openoffice.org/product/impress.html>`_ .  "a truly outstanding tool for creating
effective multimedia presentations. Your presentations will stand out with 2D
and 3D clip art, special effects, animation, and high-impact drawing tools." 
Likely to be completely true.  However, I'm not ready to make the leap to Open
Office.  Yet.  Office 12 may be the tipping
point.



KOffice `KPresenter <http://www.koffice.org/kpresenter/>`_ .  "With KPresenter, you can prepare a
set of slides for use in an on-screen slideshow or for printing. Your slides can
include text and graphics in a variety of formats, and of course, you can embed
all sorts of objects."  However, the Windows/Cygwin thing leaves me a little
cold.



`MagicPoint <http://member.wide.ad.jp/wg/mgp/>`_ .  "X11 based presentation tool. It is
designed to make simple presentations easy while to make complicated
presentations possible.  Its presentation file (whose suffix is typically .mgp)
is just text so that you can create presentation files quickly with your
favorite editor (e.g. Emacs, vi)."  Cool.  What about Windows?  That's what my
company-supplied laptop runs, and I'd like to stick close to that
platform.



Latex-based tools (a classic
write-up is `Making Presentations with LaTeX and Prosper <http://freshmeat.net/articles/view/667/>`_ ).
Not interesting to me because I'm more comfortable with the SGML/HTML/XML syntax
family.    Typically, LaTeX leads to a PDF that can be shown in full-screen
mode.  This is rather cool, since everyone has Adobe Reader nowadays.




HTML-based tools (see `Using Linux for Presentations Mini-HOWTO <http://www.shallowsky.com/linux/LinuxPresentations.html>`_ ).  In
this case, we rely on a browser to show the slides.  I've looked at some of the
following, and been unhappy for a variety of very small
reasons.



Also, there's `Bruce <http://bruce.python-hosting.com/%22%20target=%22NewWindow>`_ ,
which is new, and I haven't tried it.  It uses `PyGame <http://www.pygame.org/news.html>`_ ,
which sits on `SDL <http://www.libsdl.org/index.php>`_ , and looks like it can seize the display and
keyboard in a portable, non-proprietary way, which would be A Good Thing™.
It uses Python as a markup language, an interesting alternative to XML or LaTeX.
More precisely, a Bruce presentation IS a Python application which builds
individual Page objects and displays them using some interactive events for
navigation.



A Leo document to could
produce the Python app which is a Bruce presentation.   Leo does this in a very
elegant way.  A simple @button could launch Bruce on the resulting Python
file.



Or, even nicer, a plug-in to Leo
could present an outline directly in Bruce by combining Bruce's PyGame
presentation with a Leo outline reader to build Page objects from Leo outlines. 
At the end of the presentation, you'd be back editing
Leo.



`Pylize <http://www.chrisarndt.de/en/software/pylize/%22%20target=%22NewWindow>`_ .
While simple, the HTML markup leaves a little bit to be desired.  The slides
aren't contained, but rather delimited by <h1> tags.  I prefer proper
XML/DocBook containers (like <slide> or <frame> or even
<div>).



`PythonPoint <http://www.reportlab.org/python_point.html>`_ .  I like the idea of going from a
version of a DocBook-like XML to slides.   This is rather elegant, and since I
know (and like) DocBook markup, this has a lot of potential.  However, it isn't
full DocBook XML; in particular, some HTML in-line markup seems to work, but is
otherwise undocumented.  Finally, I'm not adverse to processing markup to see
the results, but in this case, the consequences of a word or two alters the look
of the slide so profoundly that something closer to WYSIWYG really is
appropriate.



Currently, I'm playing
with `Slidy <http://www.w3.org/Talks/Tools/Slidy/>`_ .  It uses XHTML, and ``<div>`` tags.  It
has a clunky distribution issue, since it is style sheets and a Javascript file
to make the whole thing go.  It does, however, look really good in FireFox, and
isn't too difficult to configure and make work.  Feedback to see the
consequences of a change is almost
instant.



Sadly, really cool layouts
require that I actually learn how to control CSS.  Until then, I'm stuck with
more-or-less the default CSS's supplied with
Slidy.



For either PythonPoint or Slidy,
I can prepare my XHTML using `Leo <http://webpages.charter.net/edreamleo/front.html>`_ .  It isn't a XML editor, so it doesn't help
with the markup.  It is, however, a scriptable outliner.  As outliner, it rules.
Being scriptable in Python means that I could write a Python script to emit the
<div> container and <h1> tags automatically.








