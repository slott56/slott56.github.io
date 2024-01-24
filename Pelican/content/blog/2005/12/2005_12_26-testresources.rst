testresources
=============

:date: 2005-12-26 13:57
:tags: #python,unit testing
:slug: 2005_12_26-testresources
:category: Python
:status: published





``testresources`` http://www.robertcollins.net/unittest/testresources/
purpose appears to be to manage the resources used by a test suite.



Adding this resource management
context extends the **Test Suite**  to optimize tests around the resources. 
This can reshuffle the TestCases to minimize SetUp's.  This can be useful in
contexts where the **Fixture** includes **Singletons** or expensive resources.



While interesting, this package bends one of the common definitions of Unit Testing.
If there is a complex resource dependency, the **Fixture**
being tested isn't really isolated.  This pushes beyond isolated unit testing
with **Mock** objects into integration testing with real objects and real
interfaces.



One can make the case that
"unit" is intentionally vague; the Beck definitions refer to a **Fixture**
as the design pattern.  This could be a class, module or package, depending on
your willingness to abstract.  I agree that "unit" does not necessarily mean
class.  However, I do think that "unit" means isolated from other
components.



``testresources`` seems
specifically designed for integration test, not unit test.  I think it is
miscategorized, and belongs to an unidentified species of products: integration
testing frameworks.








