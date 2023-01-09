The Browser as OS?  Perhaps Not
===============================

:date: 2006-09-23 15:02
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2006_09_23-the_browser_as_os_perhaps_not
:category: Architecture & Design
:status: published





While "Browser as OS" is what
*appears* 
to be happening.  The browser is the front-end for many applications.  Even in
the Ajax case, however, the browser is only one piece of the application, and
the browser isn't relevant on the server
side.



The important point that is
missed in the browser wars is that the browser is only the top-most layer in a
technology stack that is getting taller. 




Look at the latest fad:
virtualization.  Here's the layers in our "platform".

-   Application

-   Browser

-   "OS" 

-   Virtualization Engine

-   BIOS, ROM's and ASIC's

-   Hardware



If we have OS's sitting on the
virtualization engine, we make the OS more flexible and portable.  Similarly, if
we have platform-neutral browser, we make the browser portable.  Further, if we
have a browser-neutral application, our application is more
portable.



While Rapoza's point it good,
it conflates the entire technology stack into a single term, "OS", which isn't a
very helpful thing to do.  It misses the point that "the OS" isn't monolithic,
and changes to this technology stack are occurring in many places. 




If, however, we write an application
that depends on a browser, and that browser is portable enough to meet our
objectives, we're happy.  If that browser isn't portable enough, then we're
forced into multi-browser compatibility, and all the ugly hacks entailed by
that.  However, in either case, we're divorced from the rest of the technology
stack.  That's the most important part of this: browsers give us a portable
presentation layer.



Note that the thing
we call "Linux" is really GNU/Linux, and can be decomposed into the Linux
kernel, and the rest of the GNU drivers, file system, commands and utilities. 
Even the middle bit of our technology stack has
layers.



The browser is certainly not
the new OS.  It's the long-sought-after standard presentation tier of an OS. 
For years, we've wanted a standard presentation interface, and it's finally
arrived.  The previous "standard" presentation interfaces have included Curses,
CICS, various Forms API's.  Even the X-Window system promised a "standard"
presentation layer.



All of the previous
presentation tiers struck the compromise between hardware-feature-specific and
portable by bowing to the vendor's hardware features.  Each character-mode
terminal or X server had vendor-specific features and extensions.  Now, however,
the browser swings the compromise the other way, providing a minimal interface
that all hardware can support
successfully.



The browser isn't the new
OS.  The browser is the new, standard presentation layer.














