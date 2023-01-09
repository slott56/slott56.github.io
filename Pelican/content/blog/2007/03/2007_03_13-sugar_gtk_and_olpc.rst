Sugar, GTK and OLPC
===================

:date: 2007-03-13 19:12
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2007_03_13-sugar_gtk_and_olpc
:category: Architecture & Design
:status: published





Some additional Sugar notes recently appeared in
"`Plumbing
Life's Depths <http://blog.vrplumber.com/1792>`_ ".



After
attending PyCon, I polished up my GTK environment, reloading the current
releases.  Here's what I did to get a workable PyGTK on my  various
desktops.



**The GTK Technology Stack** 



Here's an overview of the
components of this stack:

1.  GLIB - the essential graphics library.

2.  GTK - the GIMP Toolkit, used to build
    interesting and useful applications.

3.  PyGTK - The Python bindings for the GTK toolkit.



Linux users will use an X11
Graphics server or GNOME, which implements glib, and interacts with GTK
applications.  Windows users will install binaries which implement the glib
calls directly as window graphics
operations.



Associated components that
are essential to successful use of GTK:

- ATK (Accessibility Toolkit)

- Pango (text formatting)

- Cairo (printing)



This technology is
supported, largely, by `www.GNOME.org <http://www.gnome.org/>`_ , `www.GTK.org <http://www.gtk.org>`_ `
<http://www.gtk.org>`_  and `www.pyGTK.org <http://www.pygtk.org>`_ .  `Fink <http://www.finkproject.org/>`_  versions
for Mac OS X tends to lag behind these other
sites.



Gecko would also be a nice
addition to this stack to render
HTML.



**Mac OS** 



See `http://wiki.laptop.org/go/Sugar_on_MacOS_X <http://wiki.laptop.org/go/Sugar_on_MacOS_X>`_




We're assuming Python 2.4.4 is already
installed.



The pyGTK makes use of an X
window server.  It might be nice to have native GTK+ without the overhead of X
windows.   There is a GTK+ for Mac OS X project (`http://sourceforge.net/projects/gtk-osx/ <http://sourceforge.net/projects/gtk-osx/>`_ ) This
does not appear to be kept up-to-date. 




**Part 1 - Setup Fink** 



First, get dev-tools, known as
XCode 2.4.1 from `http://connect.apple.com <http://connect.apple.com>`_ .  This will download a
massive file named
xcode_2.4.1_8m1910_6936315.dmg.
This file almost a gigabyte in size.  You can order a DVD, which might be
quicker than downloading on an unreliable or low-speed connection.  Install
this.



Second, get Fink (`http://www.finkproject.org/download/index.php?phpLang=en <http://www.finkproject.org/download/index.php?phpLang=en>`_ ).
Install this.



You'll want to do a
self-upgrade of Fink, which rebuilds itself using dev-tools.  Run the Fink
Commander, and look for Source menu.  Select the "Self-Update-rsync" option to
resynch Fink and the package descriptions that Fink knows about. 




You'll then be advised to do an
Update-All.  This can take a very long time to complete.  However, it applies
updates to any add-on packages.  You'll do this periodically to get additional
updates.



You are looking for the
complete stack (glib, GTK, X11), which is based on "unstable packages".  
Therefore, in Fink Commander, locate the preferences.  The second tab (labeled
"Fink") has a button for using unstable packages, make sure this is checked. 
This will add this collection of "unstable"
packages.



**Part 2 - Get pyGTK and GTK+** 



There are two groups of
Fink packages that provide you the necessary Python bindings:

-   **pygobject2**, which includes pygobject2-py24 and
    pygobject2-py24-dev.

-   **pygtk2**, which includes pygtk2-gtk-py24,
    pygtk2-gtk-p24-dev and
    pygtk2-py24.



These Fink projects, in
turn, depend on GLIB, and GTK+, so Fink
*should* 
download and build these
automatically.



When prompted, there is
a choice between Apple's x11 vs xfree86.  Which is better?  My first choice was
XFree86 ("XDarwin"), and this seems to work reasonably well.  Later, there is a
warning that switching back to Apple's X11 requires rebuilding from scratch, so
perhaps X11 might have been a better choice.  Currently, everything works, so
I'm reluctant to change.



This drops
some demo software in
/usr/local/lib/pygtk.



Libraries
are installed in
/usr/local/lib/python2.4/site-packages/gtk-2.0,
plus
/usr/local/bin/pygtk*.



What's
important, however, is the final location of the completed
software.



**Part 3 - Using Fink's Packages** 



Fink places the software
it builds in a directory named
/sw.   To make
use of this new software, you need to put
/sw/lib/python2.4/site-packages
on your
PYTHONPATH. 
You can do this one of two ways:



Edit
your .profile
to include the line export
PYTHONPATH="/sw/lib/python2.4/site-packages" or
edit the
/etc/profile to
include the same export
statement.



**Part 4 - Upgrades** 



Note that there are
several components with different version numbers.  This can make configuration
management complex.



The GTK.org website
(`www.gtk.org <http://www.gtk.org>`_ )
has the following stable versions available.

-   glib - 2.12

-   GTK+ - 2.10

-   Pango - 1.14



Fink tends to lag behind these
versions.  Version 2.6.3. is available in Fink.  To upgrade to the GNOME
distribution, you would have to do a more-or-less manual build, outside of
Fink's management and control.



The
pyGTK.org website (`www.pygtk.org <http://www.pygtk.org>`_ ) has bindings for GTK+ version
2.10 and glib version 2.12.



`http://live.gnome.org/PyGTK <http://live.gnome.org/PyGTK>`_  has documentation
and downloads,
also.



**Windows** 



The
GLADE for Windows project (`http://gladewin32.sourceforge.net <http://gladewin32.sourceforge.net>`_   offers glib,
GTK+ for Windows.  GTK+ is version 2.10.7  GLIB is version
2.12.7.



The
gtk-2.10.7-win32-1.exe
includes all of the Glib and GTK you'll need.  Be sure to install it in
C:\GTK
directory.  It is a common mistake to attempt to install this in "Program
Files"; this won't work well because of the space between Program and
Files.



Then you'll need to get PyGTK,
PyGObject and PyCairo from Gnome.ORG.  These are pre-built
binaries.
















