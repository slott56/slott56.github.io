A "Don't Break the Build" Tip for Solo Python Developers
========================================================

:date: 2009-06-08 16:41
:tags: agile,#python,tdd
:slug: 2009_06_08-a_dont_break_the_build_tip_for_solo_python_developers
:category: Technologies
:status: published

One of the Agile practices is `Continuous
Integration <http://martinfowler.com/articles/continuousIntegration.html>`__.

Fowler suggests that everyone commits every day.  In `Elssamadisy's
book <http://www.elssamadisy.com/books.html>`__ includes specific advice
on why a daily check-in helps.

Some folks call this the "Don't Break the Build" practice.

But what does that mean for Python where there is no build?  And what
does it mean for a solo developer where there aren't any
consequences?

The No-Build Build
-------------------

The C++, Java, C# folks all have a really important, multi-step daily
build.  The code has to compile; it has to be packaged into JAR's (or
DLL's or whatever).  Perhaps higher-level packages like WAR's or
EAR's need to be built.  Then you can run unit tests.

We Python folks don't have anything between code and unit test --
there's no real packaging.  This makes the daily build practice seem
a little silly.

However, the daily "commit and run all the tests" is perhaps more
important in Python than it is in Java (or C++ or C#.)  Even without
any actual build activity, the daily build is still an essential
practice.

Things Go Wrong
---------------

In Python, you've got two fundamental things which a daily check-in
will spot.

#. Bugs.  All of the logic errors that a daily unit test will spot.

#. Bad Refactoring.  This is more subtle.  Not all refactoring errors
   lead directly to a bug that you can detect.  Indeed, there are a
   significant refactoring problem that I fight with weekly.

No Sense of Commitment
----------------------

Refactoring is central to Agile development.  It is inevitable
that you realize that you've misnamed, misplaced or overused some
module or package and need to either rename it or delete it.

In Python, you've got to use \`grep\` (or something similar) to
check your application for a clean change in names.  And you've
got to double-check by using SVN to delete or rename the module.

Adding a new module, however, is more subtle.  Adding a new module
is easy and quick.  You write it, you use it, you unit test and
you're good to go.

Except, of course, if you forget to check it into SVN.  If it's
not in SVN, it will still pass all your local unit tests.  It's
those "daily build" unit tests that will break on a missing
module.

VM To The Rescue
-----------------

Solo developers, of course, have trouble with the nightly build.
First, they can skip it.  Second, and more important for folks
saddled with Windows, you don't often have a clean QA user
separate from you, the developer.

A VM is a very, very nice thing to have.  You fire up
`VMWare <http://www.vmware.com/>`__ (or similar player) and run
your daily build in a separate machine.  For a solo developer, you
can do the following:

#. Make changes, unit test.

#. Commit the changes.

#. Fire up the VM.  Do an SVN UP.  Run the unit tests again.

When a Python app crashes and burns on the VM, 80% of the time,
it's a missing commit.  The rest of the time it's a failed
configuration change for any differences between development
and QA.

Now you can -- confidently -- turn code over to a sysadmin,
knowing that it actually will work.



-----

+1 for buildbot.
----------------

Dougal<noreply@blogger.com>

2009-06-09 06:21:20.484000-04:00

+1 for buildbot.


Be careful... Buildbot != Buildout.

Buildbot is p...
-----------------------------------------------------

Adam<noreply@blogger.com>

2009-06-09 12:16:33.952000-04:00

Be careful... Buildbot != Buildout.
Buildbot is probably overkill for single developers.


virtualenv in some cases can accomplish the same t...
-----------------------------------------------------

John<noreply@blogger.com>

2009-06-10 10:48:05.747000-04:00

virtualenv in some cases can accomplish the same thing as a virtual
machine, since it can give you a "clean" environment to
build/install/test from.


Post-commit hook that does a fresh checkout and ru...
-----------------------------------------------------

Michael Foord<noreply@blogger.com>

2009-06-09 13:53:34.346000-04:00

Post-commit hook that does a fresh checkout and runs all your tests.


Buildout is also a useful tool for running &#39;bu...
-----------------------------------------------------

boothead<noreply@blogger.com>

2009-06-09 04:36:21.252000-04:00

Buildout is also a useful tool for running 'builds'. When you buildout
your project it's all in it's own sandbox with all of its own
dependencies.





