TDD and Python
==============

:date: 2010-06-25 05:53
:tags: RDBMS,#python,tdd
:slug: 2010_06_25-tdd_and_python
:category: Technologies
:status: published

First, let me say that
`TDD <http://en.wikipedia.org/wiki/Test-driven_development>`__ rocks.

Few things are as much fun as (1) writing a test script for a
feature, and then (2) debugging the feature incrementally until it
passes the test. It's fun because a great deal of hand-wringing and
over-thinking is taken off the table.

To paraphrase `Obi-Wan
Kenobi <http://en.wikipedia.org/wiki/Obi-Wan_Kenobi>`__:

    **Use The Test, Luke.**

The essence of TDD is a pleasant two-step process: write tests, write
code.

However, leaving things at this simplistic level isn't appropriate.

Code Quality
------------

Most folks describe TDD as a 3-step process. I like to call this
"red-green-gold" (The Lithuanian Flag version of TDD.)

#. Tests don't pass (red).

#. Tests pass (green).

#. Refactor the code until things look good (gold).

The point here is that once you have tests that pass, you can
trivially engage in refactoring and other engineering tasks to
improve the overall quality of the code. You can optimize or make
it more readable or more reusable without breaking it.

Even this isn't quite right.

Test Quality
------------

The issue with a too-simplistic view TDD is that we walk a fine line.

-  Over-engineering the tests.

-  Under-engineering the tests.

We can -- trivially -- fall into the trap of wringing our hands
over every potential nuance of our new piece of code. We can be
stalled writing tests. Often we hear complaints from folks who
fall into this trap. They spend too much time writing tests and
indict all of TDD because they dove into details too early in the
process.

We can -- equally easily -- fall into the trap of failing to write
suitably robust tests for our software.

TDD is really a 3+1 step process.

#. Write tests, which don't pass (Red).

#. Write code until tests pass (Green).

#. (a) Clean up code to improve quality features. (b) Expand tests to add an appropriate level of robustness.

The operating word here is "appropriate".

Costs and Benefits
------------------

Some modules -- because of risk or complexity or visibility --
require extensive testing. Some modules don't require this.

Interestingly, portability -- even in Python -- requires some care in
testing. It turns out that MySQL and SQLite are not completely
identical in their behavior.

Omitting an order-by in a query can "work by accident" in one
database and fail in another. So we need appropriate testing to
ferret out these RDBMS-specific issues. Until we have the appropriate
level of testing we have an application that works in SQLite but
fails in MySQL.

The initial gut reaction can sometimes be "TDD failed us".

But this isn't true. TDD actually helped us by (1) identifying code
which passed on one platform and failed on another, and (2) leading
us to beef up all tests which depend on ordering. Pleasantly, there
aren't many.



-----

Good point about robustness of tests.

I came by <...
-----------------------------------------------------

Juho Vepsäläinen<noreply@blogger.com>

2010-06-25 11:29:52.728000-04:00

Good point about robustness of tests.
I came by `this
presentation <http://www.infoq.com/presentations/Sustainable-Test-Driven-Development>`__
a while ago. Freeman discusses these issues and then some in it (it
focuses on Java but the basic ideas still apply).


...  a test is a very inefficient way to find defe...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-06-27 10:47:26.977000-04:00

... a test is a very inefficient way to find defects ...
Check out the article
An Interview with Watts Humphrey, Part 18: The Move to SEI by By Watts
S. Humphrey and Grady Booch
http://www.informit.com/articles/article.aspx?p=1602411&ns=18775&WT.mc_id=2010-06-27_NL_InformITContent


Yeah, the Lithuanian flag is yellow-green-red.
----------------------------------------------

Anonymous<noreply@blogger.com>

2010-06-30 12:06:47.840000-04:00

Yeah, the Lithuanian flag is yellow-green-red.


Red green gold? Hmm, looks like burkins faso is th...
-----------------------------------------------------

Patrick Cornelissen<noreply@blogger.com>

2010-06-25 02:57:44.802000-04:00

Red green gold? Hmm, looks like burkins faso is the TDD country! Look at
their flag:
http://en.wikipedia.org/wiki/Pan-African_colours


