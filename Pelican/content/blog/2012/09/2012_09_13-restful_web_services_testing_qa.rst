RESTful Web Services Testing, Q&A
=================================

:date: 2012-09-13 08:00
:tags: unit testing
:slug: 2012_09_13-restful_web_services_testing_qa
:category: Technologies
:status: published

Some background:

I was vaguely pointed at one call in an API, via a 2-page "tutorial"
that uses CURL examples. Told "Test this some more." by the guy who'd
been doing some amount (none?) of hand "success path" testing via
CURL. This has since morphed into "regression testing things, all 12
calls", "we have a build API as well", and "there's this hot new
feature for a vendor conference in a couple weeks ..."

There was more, but you get the idea.  There were so more specific
"requirements" for the RESTful unit testing environment.

1)  Get "smoke test" coverage vs. all the calls

    A sequence of CURL requests to exercise a server can be viewed as
    "testing".  It's piss-poor at best.  Indeed, it's often misleading
    because of the complexity of the technology stack.

    In addition to the app, you're also testing Apache (or whatever server
    they're using) plus the framework, plus the firewall, plus caching and
    any other components of the server's technology stack.

    However, it does get you started ASAP.

2)  expand / parameterize that

    CURL isn't the best choice.  You wind up writing shell scripts.  It
    gets ugly before long.

    Python is better for this.

    Selenium may also work.  Oh wait.  Selenium is written in Python.

3)  build out to response correctness & error codes

    Proper design for testability makes this easy.

    However.  When you've be tossed a "finished" RESTful web service that
    you're supposed to be testing, you have to struggle with expected vs.
    actual.

    It's not trivial because the responses may have legitimate variances:
    date-time stamps, changing security tokens or nonces, sequence numbers
    that vary.

    Essentially, you can't just use the OS DIFF program to compare actual
    CURL responses with expected CURL responses.

    You're going to have to parse the response, pick out appropriate
    fields to check and write proper unittest assertions around those
    fields.

4)  layer in at least that much testing for the new, new feature
    breathlessly happening RIGHT NOW.

    Without a proper design for testability, this can be painful.

    If you're using a good unit test framework, it shouldn't be
    impossible.  Your framework must be able to start the target RESTful
    web service for a TestCase, exercise the TestCase, and then shutdown
    the target RESTful web service when the test has completed.

    Now, you're just writing unittest TestCase instances for the new
    feature breathlessly happening RIGHT NOW.  That should be manageable.

...tool things I've found so far... [*list elided*]

    All crap, more or less.  They're REST client libraries, not testing tools.

    You need a proper unit testing framework with TestCase and TestSuite
    classes and a TestRunner.  The tools you identified aren't testing
    frameworks, they're lower level REST client and client library.  CURL,
    by itself, isn't really very good for robust testing unless you embed
    CURL in some test framework.

For defining interfaces (2), I have found these... [*list elided*]

    API's in a typical RESTful environment have little or no formal
    definition, other than Engrish.  WSDL is for Java/XML/SOAP.  It's not
    used much for (simpler) REST.  For the most part, REST API definitions
    (i.e., via JSON or whatever) are mostly experimental.  Not
    standardized.  Not to be trusted.

    The issue is one of parallel maintenance.  The idea is that a REST
    frameworks can operate without too much additional JSON or XML
    folderol; just the code should be sufficient.

    If there's no WSDL (because it's just REST) then there's no *formal*
    definition of anything.  Sorry.

I (perhaps foolishly) figured there's be some standard way to consume
the standard format definition of an API, to generate test cases and
stubbing at least. Maybe even a standard set of verifications, like
error codes. So I went a-googling for 1) a standard / conventional
way to spec these APIs, 2) a standard / conventional tool or maybe
tools @one per stack, and 3) a standard / conventional way to
generate tests or test scaffolding in these tools, consuming the
standard / conventional API spec. So far, not so much.

    "So far, not so much" is the state of the art.  You have correctly
    understood what's available.

    REST -- in spite of it's trivial simplicity and strict adherence to
    HTTP -- is a rather open world.  It's also pretty simple.  Fancy tools
    don't help much.

    Why not?

    Because decent programming languages already do REST; tools don't add
    *significant* value.  In the case of Python, there are relatively few
    tools (`Selenium <http://seleniumhq.org/>`__ is the big deal, and it's
    for browser testing) because there's no real marketplace niche for
    them.  In general, simple Python using httplib (or Python
    3 http.client) can test the living shit out of RESTful API better than
    CURL/DIFF with no ugly shell-script coding.  Only polite, civilized
    Python coding.




-----

good post.....I appreciate yor way of writing that...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-04-29 03:40:29.866000-04:00

good post.....I appreciate yor way of writing that make the blog
attractive and make reader to hold longer to your blog.
`web testing
services <http://www.qualitestgroup.com/Web-Testing-Services>`__





