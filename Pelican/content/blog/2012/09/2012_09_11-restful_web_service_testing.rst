RESTful Web Service Testing
===========================

:date: 2012-09-11 08:00
:tags: unit testing,JUnit,REST
:slug: 2012_09_11-restful_web_service_testing
:category: Technologies
:status: published

Unit testing RESTful web services is rather complex.  Ideally, the
services are tested in isolation before being packaged as a service.

However, sometimes people will want to test the "finished" or
"integrated" web services technology stack because (I suppose) they
don't trust their lower-level unit tests.

Or they don't have effective lower-level unit tests.

Before we look at testing a complete RESTful web service, we need to
expose some underlying principles.

Principle #1.  **Unit does not mean "class"**.  Unit means unit: a
discrete unit of code.  Class, package, module, framework, application.

All are legitimate meanings of unit.  We want to use stable,
easy-to-live with unit testing tools.  We don't want to invent something
based on shell scripts running CURL and DIFF.

Principle #2.  **The code under test cannot have any changes made to it
for testing**.  It has to be the real, unmodified production code.  This
seems self-evident.  But.  It gets violated by folks who have
badly-designed RESTful services.

This principle means that all the settings required for testability must
be part of an external configuration.  No exceptions.  It also means
that your service may need to be refactored so that the guts can be run
from the command line outside Apache.

When your RESTful Web Service depends on third-party web service(s),
there is an additional principle.

Principle #3.  **You must have formal proxy classes for all RESTful services your app consumes**.  These proxy classes are going to be
really simple, since they must **trivially** map resource requests to
proper HTTP processing.  In Python, it is delightfully simple to create
a class where each method simply uses httplib (or http.client in Python
3.2) to make a GET, POST, PUT or DELETE request.  In Java you can do
this, also, it's just not delightfully simple.

**TestCase Overview**

Testing a RESTful web service is a matter of starting an instance of the
service, running a standard unit testing TestCase, and then shutting
that instance down.  Generally this will involve setUpModule and
tearDownModule (in Python parlance) or a @BeforeClass and @AfterClass
(in Java parlance).

The class-level (or module-level) setup must start the application
server being tested.  The server will start in some known initial
condition.  This may involve building and populating known database,
too.  This can be fairly complex.

When working with SQL, In-memory databases are essential for this.

SQLite (Python) or `http://hsqldb.org <http://hsqldb.org/>`__ (Java)
can be life-savers because they're fast and flexible.

What's important is that the client access to the RESTful web service is
entirely under control of a unit testing framework.

**Mocking The Server**

A small, special-purpose server must be built that mocks the full
application server without the endless overheads of a full web server.
It can be simpler to mock a server rather than to try to reset the state
of a running Apache server.  TestCases often execute a sequence of
stateful requests assuming a known starting state.   Starting a fresh
mock server is sometimes an easy way to set this known starting state.
Here's a Python script that will start a server.   It writes the PID to
a file for the shutdown script.

::

    import http.server
    import os
    from the_application import some_application_feature
    class AppWrapper( http.server.BaseHTTPRequestHandler ):
        def do_GET( self ):
            # Parse the URL
            id= url.split("/")[-1]
            # Invoke the real application's method for GET on this URL.
            body= some_application_feature( id )
            # Respond appropriately
            self.send_response( 200, body )
        ... etc ...
    # Database setup before starting the service.
    # Filesystem setup before starting the service.
    # Other web service proxy processes must be started, too.
    with open("someservice.pid","w") as pid_file:
        print( os.getpid(), file=pid_file )
    httpd = http.server.HTTPServer("localhost:8000", AppWrapper)
    try:
        httpd.serve_forever()
    finally:
        # Cleanup other web services.

Here's a shutdown script.

::

    import os, signal
    with open("someservice.pid") as pid_file:
        pid= int( pid_file.read() )
    os.kill( pid, signal.CTRL_C_EVENT )

These two scripts will start and stop a mock server that wraps the
underlying application.

When you're working in Java, it isn't so *delightfully* simple as Python

But it should be respectably simple.  And you have `Jython Java
integration <http://www.jython.org/jythonbook/en/1.0/JythonAndJavaIntegration.html>`__
so that this Python code can invoke a Java application without too much
pain.

Plus,  you can always fall further back to a CGI-like unit testing
capability where "body= some_application_feature( id )" becomes a
subprocess.call(). Yes it's inefficient.  We're just testing.

This CGI-like access only works if the application is very well-behaved
and can be configured to process one request at a time from a local file
or from the command line.  This, in turn, may require building a test
harness that uses the core application logic in a CGI-like context where
STDIN is read and STDOUT is written.



-----


I am a newbie, I did not have a clear...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2012-09-11 08:58:36.627000-04:00

Thanks,
I am a newbie, I did not have a clear Idea about testing RESTful
services untill I saw this post.
Thanks again.





