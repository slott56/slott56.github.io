Compare and Contrast (round 2)
==============================

:date: 2005-11-07 17:50
:tags: #python,unit testing
:slug: 2005_11_07-compare_and_contrast_round_2
:category: Python
:status: published





The object-oriented unit testing framework began
as Smalltalk's Beck Test framework http://www.xprogramming.com/testfram.htm%22%20target=%22NewWindow.
It evolved to the JUnit http://www.junit.org/index.htm%22%20target=%22NewWindow
framework for Java.  Beck defined four repeated patterns of unit testing
software, covered in a previous posting <{filename}/blog/2005/11/2005_11_05-compare_and_contrast_round_1.rst>.



An
additional pattern that py.test introduces is the
**Diagnostics** 
pattern.  This is a useful traceback or cached output.  To make it useful, it is
presented only for failing tests, and elides repetition in the event of
recursions that lead to stack
overflows.



py.test seems to deliver
most of the Beck-defined features. 




The Fixture is created by offering a
number of setup/teardown functions, either at the module level (for a module or
class) or within a class.    



The Test
Case is a module, class or function with an appropriate name.  Either
``test_`` or
``Test_`` as a
prefix is sufficient to define a test
case.



The Results Check uses ordinary
asserts and a special
py.test.raises
function to cover all the bases.  Personally, I prefer the JUnit approach to
catching the expected exception and calling the
fail() method
for everything else.



The Suite is
developed by implication through Python's powerful introspection: everything
that looks like a test -- at the package, module and class level -- is a
candidate.  A regular expression can pick names, plus other global conditions
can be examined to further refine the test protocols. 




The Runner is a stand-alone
py.test program
that locates the tests, executes them and produces a log.  Further, it produces
Diagnostics focused on the failing tests.  








