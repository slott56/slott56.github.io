Found an ancient cgi script -- part II -- testing
=================================================

:date: 2021-09-07 11:00
:tags: Apache,wsgi,CGI,#python
:slug: 2021_09_07-found_an_ancient_cgi_script_part_ii_testing
:category: Technologies
:status: published

See "`We have an ancient Python2 CGI script -- what do we
do? <{filename}/blog/2021/08/2021_08_31-we_have_an_ancient_python2_cgi_script_what_do_we_do.rst>`__"
The previous post in this series provides an overview of the process of
getting rid of legacy code.

Here's some code. I know it's painfully long; the point is to provide a
super-specific, very concrete example of what to keep and what to
discard. (I've omitted the module docstring and the imports.)

::

   try:
       os.mkdir("data")
   except OSError:
       pass

   path_elements = os.environ["PATH_INFO"].split("/")
   if path_elements[0] == "" and path_elements[1] == "resources":
       if os.environ["REQUEST_METHOD"] == "POST":
           type_name = path_elements[2]
           base = os.path.join("data", type_name)
           try:
               os.mkdir(base)
           except OSError:
               pass
           name = str(uuid.uuid4())
           full_name = os.path.join(base, name)
           data = cgi.parse(sys.stdin)
           output_file = open(full_name, 'w')
           output_file.write(repr(data))
           output_file.write('\n')
           output_file.close()

           print "Status: 201 CREATED"
           print "Content-Type: text/html"
           print
           print "<!DOCTYPE html>"
           print "<html>"
           print "<head><title>Created New %s</title></head>" % type_name
           print "<body>"
           print "<h1>Created New %s</h1>" % type_name
           print "<p>Path: %s/%s</p>" % (type_name, name)
           print "<p>Content: </p><pre>"
           print data
           print "</pre>"
           print "</body>"
           # cgi.print_environ()
           print "</html>"
       elif os.environ["REQUEST_METHOD"] == "GET" and len(path_elements) == 3:
           type_name = path_elements[2]
           print "Status: 200 OK"
           print "Content-Type: text/html"
           print
           print "<!DOCTYPE html>"
           print "<html>"
           print "<head><title>Query %s</title></head>" % (type_name,)
           print "<body><h1>Create new instance of <tt>%s</tt></h1>" % type_name
           print '<form action="/cgi-bin/example.py/resources/%s" method="POST">' % (type_name,)
           print """
             <label for="fname">First name:</label>
             <input type="text" id="fname" name="fname"><br><br>
             <label for="lname">Last name:</label>
             <input type="text" id="lname" name="lname"><br><br>
             <input type="submit" value="Submit">
           """
           print "</form>"
           # cgi.print_environ()
           print "</body>"
           print "</html>"
       elif os.environ["REQUEST_METHOD"] == "GET" and len(path_elements) == 4:
           type_name = path_elements[2]
           resource_name = path_elements[3]
           full_name = os.path.join("data", type_name, resource_name)
           input_file = open(full_name, 'r')
           content = input_file.read()
           input_file.close()

           print "Status: 200 OK"
           print "Content-Type: text/html"
           print
           print "<!DOCTYPE html>"
           print "<html>"
           print "<head><title>Document %s -- %s</title></head>" % (type_name, resource_name)
           print "<body><h1>Instance of <tt>%s</tt></h1>" % type_name
           print "<p>Path: %s/%s</p>" % (type_name, resource_name)
           print "<p>Content: </p><pre>"
           print content
           print "</pre>"
           print "</body>"
           # cgi.print_environ()
           print "</html>"
       else:
           print "Status: 403 Forbidden"
           print "Content-Type: text/html"
           print
           print "<!DOCTYPE html>"
           print "<html>"
           print "<head><title>Forbidden: %s to %s</title></head>"  % (os.environ["REQUEST_METHOD"], path_elements)
           cgi.print_environ()
           print "</html>"
   else:
       print "Status: 404 Not Found"
       print "Content-Type: text/html"
       print                               # blank line, end of headers
       print "<!DOCTYPE html>"
       print "<html>"
       print "<head><title>Not Found: %s</title></head>" % (os.environ["PATH_INFO"], )
       print "<h1>Error</h1>"
       print "<b>Resource <tt>%s</tt> not found</b>" % (os.environ["PATH_INFO"], )
       cgi.print_environ()
       print "</html>"

At first glance you might notice (1) there are several resource types
located on the URL path, and (2) there are several HTTP methods, also.
These features aren't always obvious in a CGI script, and it's one of
the reasons why CGI is simply horrible.

It's not clear from this what -- exactly -- the underlying data model is
and what processing is done and what parts are merely CGI and HTML
overheads.

This is why refactoring this code is absolutely essential to replacing
it.

And.

We can't refactor without test cases.

And (bonus).

We can't have test cases without some vague idea of what this thing
purports to do.

Let's tackle this in order. Starting with test cases.

Unit Test Cases
---------------

We can't unit test this.

As written, it's a top-level script without so much as as single def or
class. This style of programming -- while legitimate Python -- is an
epic fail when it comes to testing.

Step 1, then, is to refactor a script file into a module with
function(s) or class(es) that can be tested.

::

   def main():
       ... the original script ... 

   if __name__ == "__main__":  # pragma: no cover
       main()

For proper testability, there can be at most these two lines of code
that are not easily tested. These two (and only these two) are marked
with a special comment (``# pragma: no cover``) so the coverage tool can
politely ignore the fact that we won't try to test these two lines.

We can now provide a os.environ values that look like a CGI requests,
and exercise this script with concrete unit test cases.

How many things does it do?

Reading the code is headache-inducing, so, a fall-back plan is to count
the number of logic paths. Look at if/elif blocks and count those
without thinking too deeply about why the code looks the way it looks.

There appear to be five distinct behaviors. Since there are
possibilities of unhandled exceptions, there may be as many as 10 things
this will do in production.

This leads to a unit test that looks like the following:

::

   import unittest
   import urllib
   import example_2
   import os
   import io
   import sys

   class MyTestCase(unittest.TestCase):
       def setUp(self):
           self.cwd = os.getcwd()
           try:
               os.mkdir("test_path")
           except OSError:
               pass
           os.chdir("test_path")
           self.output = io.BytesIO()
           sys.stdout = self.output
       def tearDown(self):
           sys.stdout = sys.__stdout__
           sys.stdin = sys.__stdin__
           os.chdir(self.cwd)
       def test_path_1(self):
           """No /resources in path"""
           os.environ["PATH_INFO"] = "/not/valid"
           os.environ["REQUEST_METHOD"] = "invalid"
           example_2.main()
           out = self.output.getvalue()
           first_line = out.splitlines()[0]
           self.assertEqual(first_line, "Status: 404 Not Found")
       def test_path_2(self):
           """Path /resources but bad method"""
           os.environ["PATH_INFO"] = "/resources/example"
           os.environ["REQUEST_METHOD"] = "invalid"
           example_2.main()
           out = self.output.getvalue()
           first_line = out.splitlines()[0]
           self.assertEqual(first_line, "Status: 403 Forbidden")
       def test_path_3(self):
           os.environ["PATH_INFO"] = "/resources/example"
           os.environ["REQUEST_METHOD"] = "GET"
           example_2.main()
           out = self.output.getvalue()
           first_line = out.splitlines()[0]
           self.assertEqual(first_line, "Status: 200 OK")
           self.assertIn("<form ", out)
       def test_path_5(self):
           os.environ["PATH_INFO"] = "/resources/example"
           os.environ["REQUEST_METHOD"] = "POST"
           os.environ["CONTENT_TYPE"] = "application/x-www-form-urlencoded"
           content = urllib.urlencode({"field1": "value1", "field2": "value2"})
           form_data = io.BytesIO(content)
           os.environ["CONTENT_LENGTH"] = str(len(content))
           sys.stdin = form_data
           example_2.main()
           out = self.output.getvalue()
           first_line = out.splitlines()[0]
           self.assertEqual(first_line, "Status: 201 CREATED")
           self.assertIn("'field2': ['value2']", out)
           self.assertIn("'field1': ['value1']", out)


   if __name__ == '__main__':
       unittest.main()

Does this have 100% code coverage? I'll leave it to the reader to
copy-and-paste, add the ``coverage run`` command and look at the output.
What else is required?

Integration Test Case
---------------------

We can (barely) do an integration test on this. It's tricky because we
don't want to run Apache httpd (or some other server.) We want to run a
small Python script to be sure this works.

This means we need to (1) start a server as a separate process, and (2)
use urllib to send requests to that separate process. This isn't too
difficult. Right now, it's not *obviously* required. The test cases
above run the entire script from end to end, providing what we think are
appropriate mock values. Emphasis on "what we think." To be sure, we'll
need to actually fire up a separate process.

As with the unit tests, we need to enumerate **all** of the expected
behaviors.

Unlike the unit tests, there are (generally) fewer edge cases.

It looks like this.

::

   import unittest
   import subprocess
   import time
   import urllib2

   class TestExample_2(unittest.TestCase):
       def setUp(self):
           self.proc = subprocess.Popen(
               ["python2.7", "mock_httpd.py"],
               cwd="previous"
           )
           time.sleep(0.25)
       def tearDown(self):
           self.proc.kill()
           time.sleep(0.1)
       def test(self):
           req = urllib2.Request("http://localhost:8000/cgi-bin/example.py/resources/example")
           result = urllib2.urlopen(req)
           self.assertEqual(result.getcode(), 200)
           self.assertEqual(set(result.info().keys()), set(['date', 'status', 'content-type', 'server']))
           content = result.read()
           self.assertEqual(content.splitlines()[0], "<!DOCTYPE html>")
           self.assertIn("<form ", content)

   if __name__ == '__main__':
       unittest.main()

This will start a separate process and then make a request from that
process. After the request, it kills the subprocess.

We've only covered one of the behaviors. A bunch more test cases are
required. They're all going to be reasonably similar to the ``test()``
method.

Note the ``mock_httpd.py`` script. It's a tiny thing that invokes CGI's.

::

   import CGIHTTPServer
   import BaseHTTPServer

   server_class = BaseHTTPServer.HTTPServer
   handler_class = CGIHTTPServer.CGIHTTPRequestHandler

   server_address = ('', 8000)
   httpd = server_class(server_address, handler_class)
   httpd.serve_forever()

This will run any script file in the cgi-bin directory, acting as a kind
of mock for Apache httpd or other CGI servers.

Tests Pass, Now What?
---------------------

We need to formalize our knowledge with a some diagrams. This is a
Context diagram in PlantUML. It draws a picture that we can use to
discuss what this app does and who actually uses it.

::

   @startuml
   actor user
   usecase post
   usecase query
   usecase retrieve
   user --> post
   user --> query
   user --> retrieve

   usecase 404_not_found
   usecase 403_not_permitted
   user --> 404_not_found
   user --> 403_not_permitted

   retrieve <|-- 404_not_found
   @enduml

We can also update the Container diagram. There's an "as-is" version and
a "to-be" version.

Here's the as-is diagram of any CGI.

::

   @startuml
   interface HTTP

   node "web server" {
       component httpd as  "Apache httpd"
       interface cgi
       component app
       component python
       python --> app
       folder data
       app --> data
   }

   HTTP --> httpd
   httpd -> cgi
   cgi -> python
   @enduml

Here's a to-be diagram of a typical (small) Flask application.

::

   @startuml
   interface HTTP

   node "web server" {
       component httpd as  "nginx"
       component uwsgi
       interface wsgi
       component python
       component app
       component model
       component flask
       component jinja
       folder data
       folder static
       httpd --> static
       python --> wsgi
       wsgi --> app
       app --> flask
       app --> jinja
       app -> model
       model --> data
   }

   HTTP --> httpd
   httpd -> uwsgi
   uwsgi -> python
   @enduml

These diagrams can help to clarify how the CGI will be restructured. A
complex CGI might have a database or external web services involved.
These should be correctly depicted.

The previous post on this subject said we can now refactor this code.
The unit tests are required before making any real changes. (Yes, we
made one change to promote testability by repackaging a script to be a
function.)

We're aimed to start disentangling the HTML and CGI overheads from the
application and narrowing our focus onto the useful things it does.

| 





