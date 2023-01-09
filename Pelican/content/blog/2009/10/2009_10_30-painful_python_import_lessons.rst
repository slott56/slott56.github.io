Painful Python Import Lessons
=============================

:date: 2009-10-30 09:27
:tags: Django,#python,module,package
:slug: 2009_10_30-painful_python_import_lessons
:category: Technologies
:status: published

Python's packages and modules are -- generally -- quite elegant.

They're relatively easy to manage. The ``__init__.py`` file (to make a
module into a package) is very elegant. And stuff can be put into the
``__init__.py`` file to create a kind of top-level or header module in a
larger package of modules.

To a limit.

It took hours, but I found the edge of the envelope. The hard way.

We have a package with about 10 distinct Django apps. Each Django app
is -- itself -- a package. Nothing surprising or difficult here.

At first, just one of those apps used a couple of fancy
security-related functions to assure that only certain people could
see certain things in the view. It turns out that merely being logged
in (and a member of the right group) isn't enough. We have some
additional context choices that you must make.

The view functions wind up with a structure that looks like this.

::

    @login_required
    def someView( request, object_id, context_from_URL ):
        no_good = check_other_context( context_from_URL )
        if no_good is not None: return no_good
        still_no_good = check_session()
        if still_no_good is not None: return still_no_good
        # you get the idea

At first, just one app had this feature.

Then, it grew. Now several apps need to use check_session and
check_other_context.

**Where to Put The Common Code?**

So, now we have the standard architectural problem of refactoring
upwards. We need to move these functions somewhere accessible. It's
above the original app, and into the package of apps.

The dumb, obvious choice is the package-level ``__init__.py`` file.

Why this is dumb isn't obvious -- at first. This file is implicitly
imported. Doesn't seem like a bad thing. With one exception.

The settings.

If the settings file is in a package, and the package-level
``__init__.py`` file has any Django stuff in it -- any at all -- that
stuff will be imported *before* your settings have finished being
imported. Settings are loaded lazily -- as late as possible. However,
in the process of loading settings, there are defaults, and Django
may have to use those defaults in order to finish the import of your
settings.

This leads to the weird situation that Django is clearly ignoring
fundamental things like DATABASE_ENGINE and similar settings. You get
the dummy database engine, Yet, a basic from django.conf import
settings; print settings.DATABASE_ENGINE shows that you should have
your expected database.

**Moral Of the Story**

Nothing with any Django imports can go into the package-level
``\``__init__.py`` files that may get brought in while importing settings.





