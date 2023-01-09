TDD, API Design and Refactoring
===============================

:date: 2014-06-12 08:00
:tags: unit testing,#python,tdd,stingray reader,API Design,mastering object-oriented python
:slug: 2014_06_12-tdd_api_design_and_refactoring
:category: Architecture & Design
:status: published

See this short discussion on a Stingray Reader feature:

https://sourceforge.net/p/stingrayreader/discussion/COBOL/thread/d2132851/?limit=25#2a3a

This turned into an exercise in pure TDD.

    <rant>

    I'm not a fan of applying TDD in a strict, death-march fashion.

    I see the comments on Stack Overflow that indicate that some folks
    feel strongly that strict TDD is somehow helpful. While "test before
    code" is laudable and often helpful, there's no royal road to good
    software.

    Design involves a great deal of back and forth between code and test.
    A great deal.

    It's logically impossible to write a test without having thought about
    the code. In order to write the test first, there **must** be a
    notional API against which the test is written. Anyone who requires
    that the test file must be written before the notional class or module
    is just playing at petty tyranny.

    The notional design -- the rough outline of the class or module -- can
    be written into a file before any tests. It's okay. It is still
    test-driven because the considerations of testability drove the design
    process.

    In particular, when starting "from scratch" -- with nothing -- writing
    tests first is senseless. Some module or package structure must exist
    for the test modules to import.

    </rant>

Having ranted, it still arises that the tests do come before any code
under some circumstances.

In this case, the requested functionality was quite difficult to
visualize. However, it was possible to cobble together a test case
that simplified the problem down to something like this this:

::

    01 Some-Record.
        05 Header PIC XXX.
        05 Body PIC X(17).

    01 ABC-Segment.
        05 Field-ABC PIC X(17).

    01 DEF-Segment.
        05 Field-DEF PIC X(17).

In COBOL, the program would use logic like IF Header EQUALS "ABC" THEN
MOVE Body TO ABC-Segment. We need a way to handle something like this
in Python so that we can parse the EBCDIC COBOL data.

This summarized example allowed construction of a test case that made
use of a API that might have existed. I was pretty sure I had a test
case that showed an approach.

**What Actually Happened**

Since the application already had 178 unit tests, there was plenty of
structure that worked.

The single new unit test relied on a notional API that wasn't really
in place. The new test bombed grotesquely.

There are two solutions:

-  Modify the test.
-  Fix the notional API so that it works properly.


I started out chasing the second option. I tweaked some things. More
tests failed. I tweaked some more things. The new test finally passed,
but another test was failing.

Some careful study of the failing test revealed that my approach was
wrong. Way wrong.

The notional API was a bad idea.

The tweaks to make it work were a worse idea.

**Back to the Lab Bench**

At this point, I had made enough changes that the only thing to do was
copy the new test and use the Git Revoke on the local changes to
unwind the awful mistakes.

Staring again, I had a slightly better grip on the relevant code. I
had a failing test. I tried a different approach that wasn't quite so
inventive. This meant modifying the test.

I actually went through a few iterations of the test, using the test
method as a kind of lab bench.

A more Pythonic approach to the lab bench is to work from the >>>
prompt. I think that **all** of the exemplary projects use the >>>
prompt examples in their documentation. This is a way to narrow and
clarify the API. As projects get big, they can sprawl. New features
can wind up with many imports to pick and choose elements from
existing modules.

When it becomes difficult to use the >>> prompt as the lab bench,
that's a sign that the API is too complex. Refactoring must happen.

Using the unit test framework as the lab bench was a hint that
something had drifted out of tolerance.

However. I did get a test which passed. Yay. Sort of.

The test code was hideous.

**TDD and API Design**

The point of TDD, however, is that we have a working suite of tests.
Refactoring won't break anything.

The point was that the hideous API could be rewritten into something
that both

-  Passed all the tests, and
-  Was usable at the >>> prompt.


It's difficult to express how valuable the Python >>> prompt is to
help clarify API design issues.

The rule is this:

**If the API doesn't make sense at the >>> prompt, it's incomprehensible**


Sadly, Java doesn't have this kind of boundary. Java programming can
spin into quite complex API's, limited only by the laziness of the
programmer who avoids refactoring.

Or the malice of the programmer's manager in not allowing time to
refactor.





