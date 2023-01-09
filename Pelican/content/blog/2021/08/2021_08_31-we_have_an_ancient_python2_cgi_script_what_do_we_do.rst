We have an ancient Python2 CGI script -- what do we do?
=======================================================

:date: 2021-08-31 11:00
:tags: Apache,wsgi,CGI,#python
:slug: 2021_08_31-we_have_an_ancient_python2_cgi_script_what_do_we_do
:category: Technologies
:status: published

This was a shocking email: the people have a Python 2 CGI script. They
needed advice on Python 2 to 3 migration.

Here's my advice on a Python 2 CGI script: **Throw It Away**.

A great deal of the CGI processing is part of the wsgi module, as well
as tools like jinja and flask. This means that the ancient Python 2 CGI
script has to be disentangled into two parts.

-  All the stuff that deals with CGI and HTML. This isn't valuable and
   must be deleted.
-  Whatever additional, useful, interesting processing it does for the
   various user communities.

The second part -- the useful work -- needs to be preserved. The rest is
junk.

With web services there are often at least three communities: the
"interactive users", "analysts", and the administrators who keep it
running. The names vary a lot with the problem domain. The interactive
users may further decompose into anonymous visitors, people with
privileges to make changes, and administrators to manage the privileges.
There may be multiple flavors of analytical work based on the web
transactions that are logged. A lot can go on, and each of these
communities has a feature set they require.

The idea here is to look at the project as a rewrite where **some** of
the legacy code may be preserved. It's better to proceed as though this
is new development with the legacy code providing examples and test
cases. If we look at this as new, we'll start with some diagrams to
provide a definition of done.

Step One
--------

Understand the user communities. Create a `4C <https://c4model.com>`__
Context Diagram to show who the users are and what the expect. Ideally,
it's small with "users" and "administrators." It may turn out to be big
with complex privilege rules to segregate users.

It's hard to get this right. Everyone wants the code "converted". But no
one really knows all the things the code does. There's a lot of pressure
to ignore this step.

This step creates the definition of done. Without this, there's no way
to do anything with the CGI code and make sure that the original
features still work.

Step Two
--------

Create a `4C <https://c4model.com>`__ Container Diagram showing the
Apache HTTPD (or whatever server you're using) that fires the CGI.
Document all other ancillary things are going on. Ideally, there's
nothing. Ideally, this is a minor, stand-alone server that no one
noticed until today. Label this picture "As Is." It will change, but you
need a checklist of what's running right now.

(This should be very quick to produce. If it's not, go back to step one
and make sure you really understand the context.)

Step Three
----------

Create a `4C <https://c4model.com>`__ Component Diagram, and label it
"As Is". This has all the parts of your code base. Be sure you locate
all the things in the local site-packages directory that were added onto
Python. Ideally, there isn't much, but -- of course -- there could be
dozens of add-on libraries.

You will have several lists. One list has all the things in
site-packages. If the ``PYTHONPATH`` environment variable is used, all
the things in the directories named in this environment variable. Plus.
All the things named in ``import`` statements.

These lists should overlap. Of course someone can install a package
that's not used, so the site-packages list should be a superset of the
import list.

This is a checklist of things that must be read (and possibly converted)
to build the new features.

Step Four?

You'll need two suites of fully automated tests.

-  Unit tests for the Python code. This must have 100% code coverage and
   will not be easy.
-  Integration tests for the CGI. You will be using the WSGI module
   instead of Apache HTTPD (or whatever the server was) for this
   testing. You will NOT integrate with the original web server,
   because, that interface is no longer supported and is a security
   nightmare.

Let's break this into two steps.

Step Four
---------

You need automated unit tests. You need to reach at last 100% code
coverage for the unit tests. This is going to be difficult for two
reasons. First, the legacy code may not be easy to read or test. Second,
Python 2 testing tools are no longer well supported. Many of them still
work, but if you encounter problems, the tool will never be fixed.

If you can find a Python 2 version of **coverage**, and a Python 2
version of **pytest**, I suggest using this combination to write a test
suite, and make sure you have 100% code coverage.

This is a lot of work, and there's no way around it. Without automated
testing, there's no way to prove that you're done and the software can
be trusted in production.

You will find bugs. Don't fix them now. Log them by marking the test
case with the proper answer different from the answer you're getting.

Step Five
---------

Python has a built-in CGI server you can use.
See https://docs.python.org/3/library/http.server.html#http.server.CGIHTTPRequestHandler
for a handler that will provide core CGI features from a Python script
allowing you to test without the overhead of Apache httpd or some other
server.

You need an integration test suite for each user stories in the context
you created in Step One. No exceptions. Each User. Each Story. A test to
show that it works.

You'll likely want to use the CGIHTTPRequestHandler class in the
http.server module to create a test server. You'll then create a pytest
fixture that starts the web server before a test and then kills the
process after the test. It's very important to use subprocess.Popen() to
start and stop the target server to be sure the CGI interface works
correctly.

It is common to find bugs. Don't fix them now. Log them by marking the
test case with the proper answer different from the answer you're
getting.

Step Six
--------

Refactor. Now that you have automated tests to prove the legacy CGI
script really works, you need to disentangle the Python code into three
distinct components.

#. A Component to parse the request: the methods, cookies, headers, and
   URL.
#. A Component that does useful work. This corresponds to the "model"
   and "control" part of the MVC design pattern.
#. A Component that builds the response: the status, headers, and
   content.

In many CGI scripts, there is often a hopeless jumble of bad code.
Because you have tests in Step Four and Step Five, you can refactor and
confirm the tests still pass.

If the code is already nicely structured, this step is easy. Don't plan
on it being easy.

One goal is to eventually replace HTML page output creation with jinja.
Similarly, another goal is to eventually replace parsing the request
with flask. All of the remaining CGI-related features get pushed into a
wsgi-compatible plug-in to a web server.

The component that does the useful work will have some underlying data
model (resources, files, downloads, computations, something) and some
control (post, get, different paths, queries.) We'd like to clean this
up, too. For now, it can be one module.

After refactoring, you'll have a new working application. You'll have a
new top-level CGI script that uses the built-in wsgi module to do
request and response processing. This is temporary, but is required to
pass the integration test suite.

You may want to create an intermediate Component diagram to describe the
new structure of the code.

Step Seven
----------

Write an OpenAPI specification for the revised application.
See https://swagger.io/specification/ for more information. Add the path
processing so openapi.json (or openapi.yaml) will produce the
specification. This means updating unit and integration tests to add
this feature.

While this is new development, it is absolutely essential for building
any kind of web service. It will implement the Context diagram, and most
of the Container diagram. It will describe significant portions of the
Component diagram, also. It is not optional. It's very likely this was
not part of the legacy application.

Some of the document structures described in the OpenAPI specification
will be based on the data model and control components factored out of
the legacy code. It's essential to get these details write in the
OpenAPI specification and the unit tests.

This may expose problems in the CGI's legacy behavior. Don't fix it now.
Instead document the features that don't fit with modern API's. Don't be
afraid to use # TODO comments to show what should be fixed.

Step Eight
----------

Use the 2to3 tool to convert ONLY the model and control components. Do
not convert request parsing and response processing components; they
will be discarded. This may involve additional redesign and rewrites
depending on how bad the old code was.

Convert the unit tests for ONLY the model and control
components components.

Get the unit tests for the model and control to work in Python 3. This
is the foundation for the new web site. Update the C4 container,
component, and code diagrams. Since there's no request handling or HTML
processing, don't worry about code coverage for the project as a whole.
Only get the model and control to have 100% coverage.

Do not start writing view functions or HTML templates until underlying
model and control module works. This is the foundation of the
application. It is not tied to HTTP, but must exist and be tested
independently.

Step Nine
---------

Using Flask as a framework and the OpenAPI specification for the web
application, build the view functions to exercise all the features of
the application. Build Jinja templates for the HTML output. Use proper
cookie management from Flask, discarding any legacy cookie management
from the CGI. Use proper header parsing rules in Flask, discarding any
legacy header processing.

Rewrite the remaining unit tests manually. These unit tests will now use
the Flask test client. The goal is to get back to 100% code coverage.

Update the C4 container, component, and code diagrams.

Step Ten
--------

There are untold number of ways to deploy a Flask application. Pick
something simple and secure. Do some test deployments to be sure you
understand how this works. As one example, you can continue to use
Apache httpd. As another example, some people prefer GUnicorn, others
prefer to use NGINX. There's lots of advice in the Flask project on ways
to deploy Flask applications.

Do not reuse the Apache httpd and CGI interface. This was terrible.

Step Eleven
-----------

Create a pyproject.toml file that includes a tox section so that you
have a fully-automated integration capability. You can automate the
CI/CD pipeline. Once the new app is in production, you can archive the
old code and never use it again for anything. Ever.

Step Twelve
-----------

Fix the bugs you found in Steps Four, Five, and Seven. You will be
creating a new release with new, improved features.

tl;dr
-----

This is a lot of work. There's no real alternative. CGI scripts need a
lot of rework.





