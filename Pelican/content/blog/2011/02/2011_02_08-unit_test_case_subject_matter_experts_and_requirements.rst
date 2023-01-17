Unit Test Case, Subject Matter Experts and Requirements
=======================================================

:date: 2011-02-08 08:00
:tags: unit testing,#python,tdd
:slug: 2011_02_08-unit_test_case_subject_matter_experts_and_requirements
:category: Architecture & Design
:status: published

Here's a typical "I don't like TDD" question: the topic is "`Does TDD
really work for complex
projects? <http://programmers.stackexchange.com/questions/41773/does-tdd-really-work-for-complex-projects>`__"

Part of the question focused on the difficulty of preparing test
cases that cover the requirements. In particular, there was some
hand-wringing over conflicting and contradictory requirements.

Here's what's worked for me.

**Preparation**. The users provide the test cases as a spreadsheet
showing the business rules. The columns are attributes of some
business document or case. The rows are specific test cases. Users
can (and often will) do this at the drop of a hat. Often complex,
narrative requirements written by business analysts are based on such
a spreadsheet.

This is remarkably easy for must users to produce. It's just a
spreadsheet (or multiple spreadsheets) with concrete examples. It's
often easier for users to make concrete examples than it is for them
to write more general business rules.

Automated Test Case Construction
--------------------------------

Here's what can easily happen next.

Write a Python script to parse the spreadsheet and extract the cases.
There will be some ad-hoc rules, inconsistent test cases, small
technical problems. The spreadsheets will be formatted poorly or
inconsistently.

Once the cases are parsed, it's easy to then create a
Unittest.TestCase template of some kind. Use
`Jinja2 <http://jinja.pocoo.org/>`__ or even Python's string.Template
class to rough out the template for the test case. The specifics get
filled into the unit test template.

The outline of test case construction is something like this. Details
vary with target language, test case design, and overall test case
packaging approach.

::

    t = SomeTemplate()
    for case_dict in testCaseParser( "some.xls" ):
        code= t.render( **case_dict )
        with open(testcaseName(**case_dict ),'w') as result:
            result.write( code )

You now have a fully-populated tree of unit test classes, modules and
packages built from the end-user source documents.

You have your tests. You can start doing TDD.

Scenarios
---------

One of the earliest problems you'll have is test case spreadsheets
that are broken. Wrong column titles, wrong formatting, something
wrong. Go meet with the user or expert that built the spreadsheet and
get the thing straightened out.

Perhaps there's some business subtlety to this. Or perhaps they're
just careless. What's important is that the spreadsheets have to be
parsed by simple scripts to create simple unit tests. If you can't
arrive at a workable solution, you have Big Issues and it's better to
resolve it now than try to press on to implementation with a user or
SME that's uncooperative.

Another problem you'll have is that tests will be inconsistent. This
will be confusing at first because you've got code that passed one
test, and fails another test and you can't tell what the differences
between the tests are. You have to go meet with the users or SME's
and resolve what the issue is. Why are the tests inconsistent? Often,
attributes are missing from the spreadsheet -- attributes they each
assumed -- and attributes you didn't have explicitly written down
anywhere. Other times there's confusion that needs to be resolved
before any programming should begin.

The Big Payoff
--------------

When the tests all pass, you're ready for performance and final
acceptance testing. Here's where TDD (and having the users own the
test cases) pays out well.

Let's say we're running the final acceptance test cases and the users
balk at some result. "Can't be right" they say.

What do we do?

Actually, almost nothing. Get the correct answer into a spreadsheet
somewhere. The test cases were incomplete. This always happens.
Outside TDD, it's called "requirements problem" or "scope creep" or
something else. Inside TDD, it's called "test coverage" and some more
test cases are required. Either way, test cases are always
incomplete.

It may be that they're actually changing an earlier test case. Users
get examples wrong, too. Either way (omission or error) we're just
fixing the spreadsheets, regenerating the test cases, and starting up
the TDD process with the revised suite of test cases.

Bug Fixing
----------

Interestingly, a bug fix after production roll-out is no different
from an acceptance test problem. Indeed it's no different from
anything that's happened so far.

A user spots a bug. They report it. We ask for the concrete example
that exemplifies the correct answer.

We regenerate the test cases from the spreadsheets and start doing
development. 80% of the time, the new example is actually a change to
an existing example. And since the users built the example
spreadsheets with the test data, they can maintain those spreadsheets
to clarify the bugs. 20% of the time it's a new requirement. Either
way, the test cases are as complete and consistent as the users are
capable of producing.



-----

This sounds a lot like PyFIT and Robot Framework, ...
-----------------------------------------------------

Kent Johnson<noreply@blogger.com>

2011-02-08 12:37:43.819000-05:00

This sounds a lot like PyFIT and Robot Framework, you might be
interested in them.
http://code.google.com/p/robotframework/
http://fitnesse.org/FitServers.PythonFit


This sounds very interesting. Is there an example ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-02-09 04:50:25.130000-05:00

This sounds very interesting. Is there an example spreadsheet I can look
at to fully grasp it?





