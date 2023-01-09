Configuration
=============

:date: 2005-01-02 22:47
:tags: books,docbook,xml
:slug: 2005_01_02-configuration
:category: Technologies
:status: published





I did discover that my Mac OS Doc Book
installation doesn't work correctly because the JDK is so old.  Because of the
tight integration of Mac OS components, I'm reluctant to attempt to upgrade the
JDK.  However, the Xalan processor leaves 11 hung threads and doesn't terminate.
So, I suppose I'll have to track down a bunch of total side-track JDK
command-line options, Xalan configuration options, and JDK upgrades.  Just to
edit the current draft using a nice display and
keyboard.



The windows version (JDK
1.4.2_04) works better.  I'm not 100% sure why at the present
time.



And, I still have to dry-run the
whole thing under RedHat 9, which will probably lead to more lost time
identifying the subtle issues
there.



However, I did finally learn to
use FireFox DOM browser to debug
CSS's.



UPDATE:  It
*is* 
the JVM that's out-of-date.








