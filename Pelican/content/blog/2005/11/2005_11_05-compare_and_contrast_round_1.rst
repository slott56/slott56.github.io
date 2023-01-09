Compare and Contrast (round 1)
==============================

:date: 2005-11-05 20:21
:tags: #python,unit testing
:slug: 2005_11_05-compare_and_contrast_round_1
:category: Python
:status: published





**Some Basis for Comparison** 



The object-oriented unit
testing framework began as Smalltalk's Beck Test framework http://www.xprogramming.com/testfram.htm.  It evolved to the JUnit http://www.junit.org/index.htm
framework for Java.  Beck defined four repeated patterns of unit testing
software:



The
**Fixture** .
The thing we are testing; a class or possibly a set of instances of a given
class, or possibly something even larger.  If we are testing more than one class
at a time, we aren't really "unit" testing.  So the fixture often includes stubs
for missing classes.



The
**Test Case** .  A predictable reaction of the fixture. 
This should either work or fail.  It can, of course also raise one of those
egregious, unchecked-for errors that indicate fairly serious problems in a
preliminary piece of software.  Or, it may indicate something that was badly
damaged during maintenance and is now raising errors instead of simply failing
the regression test suite.



The
**Results Check** .  A specific assertion about the
fixture's results.



The
**Test Suite** . A collection of
TestCases.



JUnit and unittest add a
**Test Runner**  pattern, also.  This the top-level
component that uses a Test Suite to create test results by executing each Test
Case, assuring that each Results Check worked.  The Test Runner can also assure
that any Fixture Setup and Teardown is done
correctly.



**Legacy Frameworks** 



unittest delivers all
the Beck-defined features.  It should, it is the indirect descendant of the
original framework.  Having JUnit as an ancestor, however, leads to some clunky
non-Pythonic features.  In particular, Python features that Java lacks are
ignored, including modules and free-standing
functions.



doctest has an odd fit with
the Beck framework.  The fixture isn't well defined; since doctest has a
module-centric view, a shallow copy of the module globals are given to each
test, making the module globals the fixture.  Each Case and Results Check is
encoded in a docstring, usually by a cut and paste from an interactive testing
session.  The test suite is implied by the module
structure.



unittest isn't terribly
Pythonic.  Doctest is module-focused, not class focused, and doesn't treat the
notion of fixture very well.  



IMO,
module-based testing is a more useful level of unit testing.  Individual
classes, while important, rarely make sense in a vacuum.  All of the test
harness and stub classes required to test just one class seems like too much
unproductive work.  When the architecture changes, I may have to change a class
definition as well as the test harness classes that stand in for this class in
the unit testing framework.



Next Up,
py.test, nose and testgears.  Later, TestOOB and Sancho.








