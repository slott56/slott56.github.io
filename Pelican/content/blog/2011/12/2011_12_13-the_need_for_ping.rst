The need for ping
=================

:date: 2011-12-13 08:00
:tags: unit testing,architecture
:slug: 2011_12_13-the_need_for_ping
:category: Architecture & Design
:status: published

Years ago, when designing an interface to a vendor's web services, I
did the following.  This isn't a genius move, but it's worth
emphasizing how important it is.  And what's most important isn't
technical.

#.  I built a simple `spike solution <http://c2.com/cgi/wiki?SpikeSolution>`__ to access their service.

#.  I morphed this into a "sanity check" to be sure that their service
    really was working.  Mostly, I cleaned up the code so that it was
    testable and deliverable without embarrassment.

#.  I morphed this into a "diagnostic tool" to bypass the higher-levels
    of the application and simply access the vendor (and optionally dump
    the results) to help determine what wasn't work.  This involved
    adding the dump option to the sanity check and renaming the
    command-line application.

#.  I morphed this into a "credentials check and diagnostic tool".  This
    was -- ahem -- merely taking the hard-wired credentials out of the
    application.  Yes.  The first versions had hard-wired credentials.

That brings us to the version in use today.  The "vendor ping"
application.

The default behavior is a credentials check.

One optional behavior is to dump the interface details.

Another optional behavior is to allow selection among a small number
of simple interactions just to be sure things are working.

**Unplanned Work**

What's important here isn't that I did all this.  What's important is
that the deliverables, user stories and project plans didn't include
this little nugget of high-value goodness.

It gets run fairly frequently in crunch situations.  The actor in the
story ("As system admin...") is rarely considered as a first-class
user of the application.  Yet, the admin is a first-class user, and
needs to have proper user stories for confirming that the application
is working properly.

