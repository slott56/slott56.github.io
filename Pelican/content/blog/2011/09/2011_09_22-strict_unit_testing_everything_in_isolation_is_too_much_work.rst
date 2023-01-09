"Strict" Unit Testing -- Everything In Isolation Is Too Much Work
=================================================================

:date: 2011-09-22 08:00
:tags: unit testing,#python
:slug: 2011_09_22-strict_unit_testing_everything_in_isolation_is_too_much_work
:category: Technologies
:status: published

Folks like to claim that unit testing absolutely requires each class be
tested in isolation using mocks for all dependencies.  This is a noble
aspiration, but doesn't work out perfectly well in Python.

First, "unit" is intentionally vague.  It could be a class, a
function, a module or a package.  It's "unit" of code.  Anything
could be considered a "unit".

Second--and more important--the extensive mocking isn't fully
appropriate for Python programming.  Mocks are very helpful in
statically-typed languages where you must be very fussy about
assuring that all of the interface definitions are carefully matched
up properly.

In Python, duck typing allows a mock to be defined quite trivially.
A mock library isn't terribly helpful, since it doesn't reduce the
code volume or complexity in any meaningful way.

**Dependencies without Injection**

The larger issue with trying to unit test in Python with mock objects
is the impact of change.

We have some class with an interface.

::

    class AppFeature( object ):

       def app_method( self, anotherObject ):
           etc.

    class AnotherClass( object ):

       def another_method( self ):
           etc.

We've properly used dependency injection to make AppFeature depend on
an instance of AnotherClass.  This means that we're *supposed* to
create a mock of AnotherClass to test the AppFeature.

::

    class MockAnotherClass( object ):

       def another_method( self ):
           etc.

In Python, this mock isn't a best practice.  It can be helpful.  But
adding a mock can also be confusing and misleading.

**Refactoring Scenario**

Consider the situation where we're refactoring and change the
interface to AnotherClass.  We modify another_method to take an
additional argument, for example.

How many mocks do we have?  How many need to be changed?  What
happens when we miss one of the mocks and have the mysterious
Isolated Test Failure?

While we can use a naming convention and grep to locate the mocks,
this can (and does) get murky when we've got a mock that replaces a
complex cluster of objects with a simple **Facade** for testing
purposes.  Now, we've got a mock that doesn't trivially replace the
mocked class.

**Alternative: Less Strict Mocking**

In Python--and other duck typing languages--a less mock-heavy
approach seems more productive.  The goal of testing **every** class
in isolation surrounded by mocks needs to be relaxed.  A more helpful
approach is to work up through the layers.

#.  Test the "low-level" classes--those with few or no
    dependencies--in isolation.  This is easy because they're already
    isolated by design.

#.  The classes which depend on these low-level classes can simply use
    the low-level classes without shame or embarrassment.  The
    low-level classes work.  Higher-level classes can depend on them.
    It's okay.

#.  In some cases, mocks are required for particularly complex or
    difficult classes.  Nothing is wrong with mocks.  But fussy
    overuse of mocks does create additional work.

The benefit of this is

-   The layered architecture is tested the way it's actually used.
    The low-level classes are tested in isolation as well as being
    tested in conjunction with the classes that depend on them.

-   It's easier to refactor.  The design changes aren't propagated
    into mocks.

-   Layer boundaries can be more strictly enforced.  Circularities are
    exposed in a more useful way through the dependencies and layered
    testing.

We need to still work out proper dependency injection.  If we try
to mock every dependency, we are forced to confront every
dependency in glorious detail.  If we don't mock every single
dependency, we can slide by without properly isolating our design.



-----

You need to mock out to a level which allows yo...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2011-09-26 13:21:05.696000-04:00

You need to mock out to a level which

- allows you to not have any side effects when executing tests

- allows you to immediately understand which is the affected "unit" when a test fails without necessarily have to fire up the debugger etc...


Lot of useful points are there. Its really keeps m...
-----------------------------------------------------

Movies Gallery 2011<noreply@blogger.com>

2011-11-29 07:10:48.813000-05:00

Lot of useful points are there. Its really keeps me updated.
`Vee Eee
Technologies <http://in.linkedin.com/pub/vee-eee-technologies/15/a00/b79>`__





