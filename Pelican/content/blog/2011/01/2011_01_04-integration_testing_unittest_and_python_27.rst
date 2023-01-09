Integration Testing, unittest and Python 2.7
============================================

:date: 2011-01-04 08:00
:tags: unit testing,#python
:slug: 2011_01_04-integration_testing_unittest_and_python_27
:category: Technologies
:status: published

Many folks use Python's unittest module for integration testing. It
sometimes leads to whining and hand-wringing, but it is very effective.
Ordinary "unit" tests use mocks and focus on a class or a module
more-or-less in isolation. The purists say "complete isolation". But
that's sometimes unrealistic. A class that's part of a **State** design
pattern or a **Strategy** design pattern is often so trivial that "pure"
unit tests aren't really very enlightening. Using the stateful class
along with it's state class hierarchy is usually far more interesting
and helpful.

I argue that it's still "unit" testing because parts of the
application have been extracted from their processing context.

**OS and Module Mocks**

Some folks will hand-wring over the use of OS API's or other library
API's in a unit test. They feel that the OS API's should be
completely mocked in order to call it a "unit" test. In most cases,
simplistic mocks can be created, but for most use cases, the mock
grows to hellish complexity.

For example, we have a large number of tests which depend on Python's
csv module. While we could mock csv to produce row after row of
mocked data, it seems much simpler to trust that our infrastructure
works, use csv and simply provide files of test data in CSV format.
The file is part of the test fixture and is locked up in the source
code repository.

Is this "unit" testing when we're integrated with some of the
underlying modules?

We don't separately test csv. We simply trust that it library modules
have their own tests. If we're willing to trust the already-supplied
tests for csv, why not use it in our tests? Why Mock something we've
decided to trust?

[For that matter, we also trust Python, the OS and the unittest
module itself. Why draw lines between Python, unittest and csv?]

**ORM and RDBMS Mocks**

A similar kind of worry comes with an ORM layer. Somehow, the "trust"
factor starts to break down here. Folks want to mock the ORM layer.
Or -- worse -- they want to try and mock the RDBMS layer so that
they're testing the application and ORM layer. This is another
artificial distinction between stuff we'll trust (the RDBMS layer)
and stuff we feel we must write additional tests for (the ORM layer).

It's so much nicer to adopt the Django philosophy of building a test
database as part of the test fixture. The ORM and RDBMS are
integrated into the test itself. The thing that's "mocked" is the
data which gets pre-loaded into the database.

Outside of Django, this can be a bit complex to set up properly. You
need to create a temporary database, execute the SQL DDL, load the
fixture data. This is an annoying bit of code to write the first
time. However, it has handsome rewards because the "unit" testing
includes the ORM and RDBMS at a higher level where it's easier to
work with.

**Integration Testing**

We use the unittest module to do integration testing also. In Python
2.6, this involved a fair amount of work. We had to start our RESTful
server, run the unit test, and then kill the server. Because of the
way the subprocess module works, we can't be completely sure the
server is running, so we simply cheat and use a time.sleep(12) to
wait for the DB to be built and loaded.

Python 2.7 adds module-level test cases. It checks for setUpModule
and tearDownModule functions. I've been gleefully revising all our
unit tests to make ready for this. Our previous testing needed
pervasive (but minor) rewrites to refactor the database setup and
tear down and provide proper names.

Once that's in place, our big test shell script can be simplified
down to a little Python unittest module. This module will build a
unittest.Suite from all the other test modules (there are dozens) and
simply execute the suite as a single, integrated whole.



-----

Nice post! I&#39;ve done something similar while t...
-----------------------------------------------------

Andrei Savu<noreply@blogger.com>

2011-01-04 14:06:10.826000-05:00

Nice post! I've done something similar while testing an application
built using tornado and mongodb [1]
[1] https://github.com/andreisavu/automatic-testing-demo
I find this approach a lot more useful than trying to mock everything.
I would love to know what you think about this demo.


Regarding starting/stopping a server for tests, Ch...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-01-25 16:24:23.342000-05:00

Regarding starting/stopping a server for tests, CherryPy has a really
simple wait_for_port function that makes sure the socket is listening. I
usually also implement some sort of basic status URL as well that I can
query to make sure the service is really up and running.

Going further you can double up with something like logging.statistics
(http://www.aminus.org/blogs/index.php/2010/11/19/logging-statistics?blog=2)
when testing for whether a service is up.

Thanks for blogging about all this. The question of whether to
mock/stub/whatever else is always an interesting question that can be
tough to decide on.


I&#39;d say that people mock the ORM layer not bec...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-01-04 23:20:16.496000-05:00

I'd say that people mock the ORM layer not because of trust issues, but
because they want their unit tests to be \*fast*.





