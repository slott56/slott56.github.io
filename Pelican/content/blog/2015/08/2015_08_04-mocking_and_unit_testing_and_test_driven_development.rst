Mocking and Unit Testing and Test-Driven Development
====================================================

:date: 2015-08-04 08:00
:tags: unit testing,#python
:slug: 2015_08_04-mocking_and_unit_testing_and_test_driven_development
:category: Technologies
:status: published


Mocking is essential to unit testing.

However.

It's also annoyingly difficult to get right.

If we aren't 100% perfectly clear on what we're mocking, we will
merely canonize any dumb assumptions into mock objects that don't
*really* work. They work in the sense that they don't crash, but they
don't properly test the application objects since they repeat some
(bad) assumptions.

When there are doubts, it seems like we have to proceed cautiously.
And act like we're breaking some of the test-first
test-driven-development rules.

Note. We're not really breaking the rules. Some folks, however, will
argue that test-driven development means literally every action you
take should be driven by tests. Does this include morning coffee or
rotating your monitor into portrait mode? Clearly not. What about
technical spikes?

Our position is this.

#.  Set a spike early and often.

#.  Once you have reason to believe that this crazy thing might work, you
    can formalize the spike with tests. And mock objects.

#.  Now you can write the rest of the app by creating tests and fitting
    code around those tests.


The import part here is not to create mocks until you really
understand what you're doing.

Book Examples
~~~~~~~~~~~~~


Now comes the tricky part: Writing a book.

Clearly every example must have a unit test of some kind. I use
doctest heavily for this. Each example is in a doctest test string.

The code for a chapter might look like this.

::

    test_hello_world = '''
    >>> print( 'hello world')
    'hello world'
    '''

    __test__ = { n:v for n,v in vars().items()
       if n.startswith('test_') }

    if __name__ == '__main__':
       import doctest
       doctest.testmod()




We've used the doctest feature that looks for a dictionary assigned to
a variable named ``__test__``. The values from this dictionary are tests
that get run as if they were docstrings found inside modules,
functions, or classes.

This is delightfully simple. Expostulate. Exemplify. Copy and Paste
the example into a script for test purposes and Exhibit in the text.

Until we get to external services. And RESTful API requests, and the
like. These are right awkward to mock. Mostly because a mocked
unittest is singularly uninformative.

Let's say we're writing about making a RESTful API request to
`http://www.data.gov <http://www.data.gov/>`__. The results of the
request are very interesting. The mechanics of making the request are
an important example of how REST API's work. And how
`CKAN <http://ckan.org/>`__-powered web sites work in general.

But if we replace urrlib.request with a mock urllib, the unit test
amounts to a check that we called urlopen() with the proper
parameters. Important for a lot of practical software development, but
also uniformative for folks who download the code associated with the
book.

It appears that I have four options:

#.  Grin and bear it. Not all examples have to be wonderfully detailed.

#.  Stick with the spike version. Don't mock things. The results may vary
    and some of the tests might fail on the editor's desktop.

#.  Skip the test.

#.  Write multiple versions of the test: a "with real internet" version
    and a "with corporate firewall proxy blockers in place" version that
    uses mocks and works everywhere.


So far, I've leveraged the first three heavily. The fourth is
awkward. We wind up with code like this:

::

  class Test_get_whois(unittest.TestCase):
      def test_should_get_subprocess(self):
          subprocess = MagicMock()
          subprocess.check_output.return_value=b'\nwords\n'
          with patch.dict('sys.modules', subprocess=subprocess):
              import subprocess
              from ch_2_ex_4 import get_whois
              result= get_whois('1.2.3.4')
          self.assertEquals( result, ['', 'words'] )
          subprocess.check_output.assert_called_with(['whois', '1.2.3.4'])

This is not a lot of code for enterprise software development
purposes. It's a bit weak, in fact, since it only tests the Happy
Path.


But for a book example, it seems to be heavy on the mock module and
light on the subject of interest.

Indeed, I defy anyone to figure out what the expository value of this
is, since it has only 2 lines of relevant code wrapped in 8 lines of
boilerplate required to mock a module successfully.

I'm not unhappy with the unitest.mock module in any way. It's great
for mocking modules; I think the boilerplate is acceptable considering
what kind of a wrenching change we're making to the runtime
environment for the unit under test.

This fails at explication.

I'm waffling over how to handle some of these more complex test cases.
In the past, I've skipped cases, and used the doctest Ellipsis feature
to work through variant outputs. I think I'll continue to do that,
since the mocking code seems to be less helpful for the readers, and
too focused on purely technical need of proving that all the code is
perfectly correct.





