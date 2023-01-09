Multi-threaded apps and module globals
======================================

:date: 2009-05-17 15:40
:tags: #python,threads
:slug: 2009_05_17-multi_threaded_apps_and_module_globals
:category: Technologies
:status: published

Learned about module globals the hard way.

| 

The mod_wsgi daemon by default spawns 15 threads.  This is important,
but not obvious.

| 

During load testing, we had intermittent weird errors.  We were seeing
an odd inconsistency in replies.  My experience in creating military
software in the ’80’s leads me to put loop-back self-tests everywhere.
One of our loopbacks wasn’t looping back properly.

| 

The symptom looked like a single value being overwritten.  After a
design review, it appears that one information source -- a module global
-- wasn’t working well.

| 

Module globals -- like other Singletons -- are a seductive trap.   The
issue is that a multi-threaded application will have one copy of the
module.  The one copy may not be thread safe.

| 

The problem is that  thread-safety requires some fairly detailed
analysis. Simple unit testing isn’t quite enough.  But the process of
designing for testability is helpful.  Isolation and encapsulation are
important for testability as well as locating thread-safety issues.





