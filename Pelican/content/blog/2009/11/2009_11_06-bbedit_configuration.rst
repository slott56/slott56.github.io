BBEdit Configuration
====================

:date: 2009-11-06 10:07
:tags: mac os x,#python,bbedit
:slug: 2009_11_06-bbedit_configuration
:category: Technologies
:status: published

After installing Python 2.6 in Mac OS X, I had problems with BBEdit not
finding the right version of Python. It kept running an old 2.5 version.

I finally tracked down the BBEdit documentation,
http://pine.barebones.com/manual/BBEdit_9_User_Manual.pdf.

Found this: "BBEdit expects to find Python in /usr/bin,
/usr/local/bin, or /sw/bin. If you have installed Python elsewhere,
you must create a symbolic link in /usr/local/bin pointing to your
copy of Python in order to use pydoc and the Python debugger."

Checked in /usr/bin and found an old Python there. I think Fink did
that. Removed it and BBEdit is much happier. As is Komodo Edit.



-----

The BBEdit manual is actually pretty trivial to tr...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-11-06 13:10:55.953000-05:00

The BBEdit manual is actually pretty trivial to track down: just go to
the Help menu, and choose 'User Manual'.





