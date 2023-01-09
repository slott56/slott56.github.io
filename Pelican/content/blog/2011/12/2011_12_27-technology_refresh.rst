Technology Refresh
==================

:date: 2011-12-27 08:00
:tags: software process improvement
:slug: 2011_12_27-technology_refresh
:category: Technologies
:status: published

I've been refurbishing an older project -- written in 2008.  Probably
with Django 1.0.1.  Certainly with Python 2.5.

The `Django 1.3
release <https://docs.djangoproject.com/en/1.3/releases/#release>`__
has been around since March.  The change underscored the importance of
technology refresh.

The best part was to delete code.  There were two significant reasons.

-   The `testserver command <https://docs.djangoproject.com/en/1.3/ref/django-admin/#testserver-fixture-fixture>`__ allowed
    me to eliminate a bunch of low-value test harness.   Without this
    command, we had to create our own test database, start a server, run
    integration tests, and then kill the server.  With this command, we
    simply start and kill the server.

-   The RESTful web services can be securely integrated into the main web
    application.  A simple piece of middleware can authenticate requests
    based on headers containing `ForgeRock
    OpenAM <http://forgerock.com/openam.html>`__ tokens.  It may be that
    this was *always* a feature of Django, but over the last few years,
    we've figured out how to exploit it with simple middleware.

Few things are better than removing old code and replacing it with
code written (and tested) by someone else.

In  addition to the deletes, we also rearranged some of the
dependencies.  We had (incorrectly) thought of the Django project as
somehow central or essential.  It turns out that a bunch of other
Python libraries were actually core to the application.  The Django
web presentation was just one of the sensible use cases.  A suite of
command-line apps could also be built around the underlying
libraries.

In addition to this cleanup, we also replaced the documentation with
a new Sphinx project.  The project originally used
`Epydoc <http://epydoc.sourceforge.net/>`__ markup.  This meant that
every single docstring had to be rewritten to use RST markup.  The
upside of this is that we corrected numerous errors.

**There Was Pain**

This wasn't without some pain.

Was the cost worth the effort?  That's the real question here.

I think that many IT managers adopt a silly "If it ain't broke, don't
fix it" policy that focuses on short-term cost and short-term value.
It ignores long-term accrual from even tiny short-term cost savings.

Here's are two important lessons.

-  Money saved today is saved forever.

-  Savings accrue.  Forever.

It's important to avoid short-term thinking about cost and benefit.

-----

Please consider updating the posting w/ how the co...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-12-28 08:18:36.389000-05:00

Please consider updating the posting w/ how the company actually saved
money. Also, consider adding a section about "value added" by things
like knowledge discovery.





