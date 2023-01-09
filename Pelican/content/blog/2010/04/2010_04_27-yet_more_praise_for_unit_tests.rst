Yet More Praise for Unit Tests
==============================

:date: 2010-04-27 07:10
:tags: unit testing,tdd
:slug: 2010_04_27-yet_more_praise_for_unit_tests
:category: Architecture & Design
:status: published

I can't say enough good things about TDD.

But I'll try.

Due to an epic failure to read the documentation
(`this <http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIPassAuthorization>`__,
specifically) I couldn't get our RESTful web services to work in
Apache.

The entire application system has pretty good test coverage. I use
the Python
`unittest <http://docs.python.org/library/unittest.html>`__ to do
integration testing. A test module spins up a Django test server;
each TestCase uses the RESTful API library access the web servers
through a variety of use cases.

However. This integration isn't done through Apache and mod_wsgi.
It's done using Django's stand-alone testserver capability.

As I noted recently, Apache doesn't like to give up the HTTP
Authorization header. So, the real deployment on our real servers
didn't really work.

**The Blame Game**

At this point there are lots of things we can blame. Let's start
blaming the process.

#.  TDD didn't help. By now it should be obvious that TDD is a
    complete waste of time because it didn't uncover this obvious
    integration issue. There's no justification for TDD.

#.  The Unit Testing framework didn't help. It's a completely blown
u   nit. Unit testing is oversold as a technology.

#.  Reliance on "testing" is stupid. There's no point in even
    attempting to "test" software, since it still broke when we tried
    to deploy it. Testing simply doesn't uncover enough problems.

Clearly, we need a Bold New Process to solve and prevent problems
like this.

**Seriously**

Search Stack Overflow for "Justification of TDD" or "ROI of Unit
Testing" and those kinds of loaded questions and you'll find folks
that are angry that software development is hard and TDD or Unit
Testing or a slick IDE or a Dynamic Language or REST or SOAP or
something didn't make software easy.

There is no Pixie Dust. You've been told. Stop searching for it.
Software is hard. Unit Testing helps, but doesn't make it less
hard.

**Unit Testing to the Rescue**

Our code coverage is -- at best -- middlin'. I don't have counts,
nor do I actually care what the lines of code number is. Code
coverage can devolve to
`numerosity <{filename}/blog/2010/02/2010_02_23-numerosity_more_metrics_without_meaning.rst>`__.
The method function coverage and use case coverage is more
interesting. A "logic path coverage" might be helpful. But I'm
sure our coverage is far from complete.

So there we were.

#.  Hundreds of unit tests pass.

#.  A suite of a half-dozen "integration" scripts (over a dozen
    TestCases) pass.

#.  Real Apache deployment fails because I couldn't figure out how
    to get mod_wsgi to pass the HTTP Authorization header. Even
    though it's clearly and simply documented. [I was busy focusing
    on Apache; mod_wsgi solves the problem handily.]

What I did was copy a page from AWS and put the digested
authentication information in a query string. In one sense,
this is a huge change to the API's -- it's visible. In another
sense this is a minor tweak to the application.

The RESTful web services all rely on an authenticator object.
The change amounted to a new subclass of this authenticator.
Plus some refactoring to locate the digest in the query string.
This is a tightly focused change in authentication and the
client library. About two days of work to subclass and refactor
the auth.rest module.

**Success Factors**

Because of TDD and a suite of unit tests, many things went
really, really well.

#.  I could extend the test script for the auth.rest module to
    include the new authentication-via-query-string mechanism.
    Having tests that failed made is really easy to refactor and
    subclass until the tests passed. Then I could refactor some
    more to simplify the resulting modules.

#.  I could rerun the unittest suite, including the various
    "integration" tests (tests that had everything by Apache) to
    be sure everything still worked. Believe it or not, there
    were actual problems uncovered by this. Specifically, some
    tests didn't properly use the web services API library. The
    library had changed, but was *mostly* backwards compatible,
    so the tests had continued to work. The latest round of
    changes broke backwards compatibility, and some tests now
    failed.

#.  Despair did not set in. There were issues: sales folks were
    in total panic because the whole "house of cards"
    architecture had collapsed. A working test suite makes a
    compelling case that the application -- generally -- is
    still sound. We're just stumbling on an Apache deployment
    issue. In one sense, it's a "show stopper", but in another
    sense it's just a Visible But Minor (VBM™) hurdle.



-----

Not meaning to rub it in, more just providing furt...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-04-27 07:34:30.612000-04:00

Not meaning to rub it in, more just providing further references for
people who have similar problem with Authorization header and stumble
across your posts, but the issue is also mentioned in
'http://code.google.com/p/modwsgi/wiki/FrequentlyAskedQuestions#Access_Control_Mechanisms'
and 'http://code.google.com/p/modwsgi/wiki/AccessControlMechanisms'. :-)





