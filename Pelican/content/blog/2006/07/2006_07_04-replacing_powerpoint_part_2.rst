Replacing Powerpoint (part 2)
=============================

:date: 2006-07-04 13:55
:tags: books,docbook,xml
:slug: 2006_07_04-replacing_powerpoint_part_2
:category: Technologies
:status: published





`Kontrawize <http://kontrawize.blogs.com/kontrawize/>`_  author Anthony Coates `warns <http://www.haloscan.com/comments/slott/E20060626115128/#137940>`_  that this is an attractive time sink.
Thanks for the heads up.



My `first round <{filename}/blog/2006/06/2006_06_26-powerpoint_alternatives.rst>`_  of research found `HTML
Slidy <http://www.w3.org/Talks/Tools/Slidy/>`_ , but didn't find `DocUtils + S5 <http://docutils.sourceforge.net/docs/user/slide-shows.html>`_ .  S5 is simpler and does less than
Slidy.  RST markup is far easier to cope with than HTML.  This looks like a
powerful and simple solution.



Indeed, a
LEO outline which produces RST directly (via an ``@file``
directive) for use by
rst2s5.py is a
piece of cake.   Similarly, a small change to
rst2s5.py could
create an
rst2slidy.py,
also.



**Better Integration** 



The next step, however,
is more subtle.  We have a number of choices of integration between DocUtils, S5
and Leo.  These choices stem directly from two prominent features of this
technology stack:

1.  This is all open source.  We can integrate at
    a number of levels: the application level, using the defined file interfaces, or
    the module level, directly marrying DocUtils into Leo.

2.  This is all Python.  Integration doesn't
    involve too much more than an appropriate
    import.



There
are a mountain of alternatives:

-   Leo's RST3 plug-in can produce HTML.  It
    would be nice to make
    rst2s5.py
    unnecessary, since the DocUtils parsing is already embedded in Leo.  However,
    RST3 would have to produce ``<div class="slide">`` in addition to ``<h1>``
    tags.

-   A variant on the RST3 plug-in that
    produces HTML more directly focused on S5's .js and .css.  This could produce
    the required ``<div>`` tags.

-   A simple plug-in that produces a pure RST
    text file, transforming headlines into RST section headers.  This could be run
    through
    rst2s5.py,
    leading to a tidy way to produce slides from an outline.

-   Either of the two plug-ins could be
    designed to use HTML markup instead of RST.  This would be slightly simpler in
    one sense (eliminating RST), but less usable.

-   A simple
    ``@file`` directive
    which produces an RST file that is post-processed by
    rst2s5.py. 
    This is doubly wasteful.  First, the RST3 plug-in integrates DocUtils; why use
    an external application?  Secondly, this requires the bodies be forced to match
    the headlines, wasting the headline information.

-   A simple
    ``@file`` directive
    which produces an HTML file, directly focused on S5.  This requires that the
    content be entirely in the bodies, making the headlines unimportant.  This is
    wasteful.



And we haven't -- really --
scratched the surface.  There are indirect integration using XML and XSLT that
add complexity without demonstrable value.

-   Since the Leo outline is XML, we can
    always fabricate some XSLT to transform the Leo outline into an S5-compatible
    HTML document.

-   Worse, we can have Leo produce an XML/OML
    which is independent of S5/Slidy/PowerPoint or other approach, and write XSLT
    transformations from generic OML to S5
    HTML.



What's wrong with XML-XSLT?  It
ignores the deep, open integration we can achieve between Leo, DocUtils,
PythonPoint (and Bruce/pyGame if we went that route).  XSLT puts the focus on
the superficial integration available via XML representation of the underlying
objects.  A needless level of indirection in the open source
world.



**Making the Choice** 



What makes the most sense? 
The choice has to be consistent with the advice to build as little as possible. 
More important, the choice has to be consistent with the problem (replacing
powerpoint) and the actual use
cases.



1.  Edit the material.  Hence
    Leo: it's fun to use an outliner to build
    presentations.



2.  Present the
    material.  Adobe Reader, Opera-Firefox-whatever, or Bruce are all alternatives
    to make my laptop drive a projector.



3.  Distribute the material.  This is a poser.  Share the Leo file?  Or share the
    resulting PDF?  Or share the resulting HTML + .js + .css files?  S5 handles
    distro a little better than Slidy, because S5 expects local
    storage.



4.  Print hand-outs.  Adobe
    Reader does a great job of this.  Opera-Firefox can do this job, also.  Bruce
    falls down on this count.  I could (I suppose) use PIL to create printable
    versions of the pages or something. 
    :-(



The above analysis makes a strong
case for integrating PythonPoint into Leo, and creating a PDF from that.  A
distant second is DocUtils
rst2s5.py. 



















