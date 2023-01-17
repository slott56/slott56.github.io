The Wrapper vs. Library vs. Aspect Problem
==========================================

:date: 2010-12-09 08:00
:tags: #python,API Design,architecture
:slug: 2010_12_09-the_wrapper_vs_library_vs_aspect_problem
:category: Technologies
:status: published

Imagine that we've got a collection of applications used by customers to
provide data, a collection of applications we use to collect data from
vendors. We've got a third collection of analytical tools.

Currently, they share a common database, but the focus, use cases,
and interfaces are different.

Okay so far? Three closely-related groups or families of
applications.

We need to introduce a new cross-cutting capability. Let's imagine
that it's something central like using
`celery <http://celeryproject.org/>`__ to manage long-running batch
jobs. Clearly, we don't want to just hack celery features into all
three families of applications. Do we?

Choices
-------

It appears that we have three choices.

#.  A "wrapper" application that unifies all the application families
    and provides a new central application. Responsibilities shift to
    the new application.

#.  A site-specific library that layers some common features so that
    our various families of applications can be more consistent. This
    involves less of a responsibility shift.

#.  An "aspect" via Aspect-Oriented programming techniques. Perhaps
    some additional decorators added to the various applications to
    make them use the new functionality in a consistent way.

Lessons Learned
---------------

Adding a new application to be an overall wrapper turned out to be a
bad idea. After implementing it, it was difficult to extend. We had
two dimensions of extension.

#.  The workflows in the "wrapper" application needed constant
    tweaking as the other applications evolved. Every time we wanted
    to add a step, we had to update the real application and also
    update the wrapper. Python has a lot of introspection, but these
    aren't technical changes, these are user-visible workflow changes.

#.  Introducing a new data types and file formats was painful. The
    responsibility for this is effectively split between the wrapper
    and the underlying applications. The wrapper merely serves to
    dilute the responsibilities.

Libraries/Aspects
-----------------

It appears that new common features are almost always new aspects of
existing applications.

What makes this realization painful is the process of retrofitting a
supporting library into multiple, existing applications. It seems
like a lot of cut-and-paste to add the new ``import`` statements, add
the new decorators and lines of code. However, it's a *pervasive*
change. The point is to add the common decorator in all the right
places.

Trying to "finesse" a pervasive change by introducing a higher-level
wrapper isn't a very good idea.

A pervasive change is simply a lot of changes and regression tests.
Okay, I'm over it.





