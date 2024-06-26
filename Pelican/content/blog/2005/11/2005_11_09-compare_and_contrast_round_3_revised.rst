Compare and Contrast (round 3, revised)
=======================================

:date: 2005-11-09 19:38
:tags: #python,unit testing
:slug: 2005_11_09-compare_and_contrast_round_3_revised
:category: Python
:status: published





The object-oriented unit testing framework began
as Smalltalk's Beck Test framework http://www.xprogramming.com/testfram.htm.  It evolved to the JUnit http://www.junit.org/index.htm>`_ `  <http://www.junit.org/index.htm%22%20target=%22NewWindow
framework for Java.  Beck defined four repeated patterns of unit testing
software, covered in a previous posting <{filename}/blog/2005/11/2005_11_05-compare_and_contrast_round_1.rst>.



``Nose``, ``TestOOB``, ``test.py``
(and ``TestGears``) are significant revisions to the
**Test Suite**  and **Test Runner**  parts of the unit test patterns.
Additionally, these tools make efforts to implement the **Diagnostics** pattern, also.



The **Fixture**
is implied by the context in which the tests are discovered.  Nose can locate
package, module and function tests; it uses TestCase class definitions, also. 
TestOOB and test.py sit more squarely on unittest, with the resulting focus on
module-level testing.



In ``TestOOB`` and ``test.py``, the **TestCase**
class plus a flexible regular expressions or glob expression defines the test
cases.  test.py looks for packages of tests, using the path name of the package,
as well as the module name.  In ``Nose``, the **TestCase**
class can be used for compatibility, but this is not required; Nose will match a
regular expression to locate tests.



The **Results Check**  in ``nose`` can be done via the existing
``assert`` statement.  ``Nose``, pleasantly handles the "test which throws an exception"
case: a test function that exits normally is a "pass".  An ``AssertionError``
exception is a test failure; any other exception is an error.  Since ``TestOOB`` and
``test.py`` sit on ``unittest``, they
depend on the complex set of assert methods, and the ``fail()`` method.



The **Test Suite**  is implied by the collection of ``TestCase``
instances with the expected name forms in ``TestOOB``.  In ``Nose`` and ``test.py``, it is
the collection of modules, functions and methods with names that have the
expected forms.  Both cases make powerful use of Python introspection to track
down the tests.



The **Test Runner**  in nose can be a stand-alone ``nosetests``
program, or you can ``import nose; nose.main()``.
In the case of ``TestOOB``, we have a ``testoob``
program, or we can `import testoob; testoob.main()``.
``Nose`` has an interesting
integration with Python ``distutils/setuptools``.  It adds a new "test" verb to
``setup.py``.  The ``test.py`` main program has a large number of options to fine-tune
which tests are run



``Nose`` supports the **Diagnostics**
with output capture and a simple flag for producing additional details.  
``TestOOB``, in certain environments, will produce color output; it produces an XML
test report as well as HTML test reports.  ``TestOOB`` can launch the Python
debugger as well as log failing assertions in detail.  ``test.py`` can run
``pychecker``, do tracing and refcount checking as part of the diagnostics.



``TestOOB`` has some additional features for repeating and controlling the timing of the tests.
While this is not sufficient to prove that an application lacks the kind of race
condition that makes it behave poorly; it can help to provide some confidence
for load testing.  Similarly, ``test.py`` includes features for looping tests to
look for memory leaks and race conditions.










