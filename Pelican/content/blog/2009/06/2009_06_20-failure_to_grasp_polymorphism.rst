Failure To Grasp Polymorphism
=============================

:date: 2009-06-20 08:10
:tags: polymorphism,#python,object-oriented design
:slug: 2009_06_20-failure_to_grasp_polymorphism
:category: Technologies
:status: published

I've cataloged a third specific case of fundamental failures to
understand polymorphism. The first two I've seen a fair number of times.
The third seems to be more rare.

1. "How do I determine which subclass an object has?" The
Identification problem.

2. "How do I morph an object to a different subclass?" The
Transmutation problem.

3. "I can do that with delegation, I don't need subclasses." The
Denial problem.

Identification
------------------

The Identification problem is the most common. There are two
variants: People ask about class comparisons, and people who use some
other value as a surrogate class comparison. Either way, they have if
statements scattered around the code.

Bad.

::

    if someObject.__class__ == ThisClass:
        someObject.this_foo_method()
    elif someObject.__class__ == ThatClass:
        someObject.that_foo_method()

Worse.

::

    if someOtherIndicator == "this":
        someObject.this_foo_method()
    elif someOtherIndicator == "that":
        someObject.that_foo_method()

Better. Use inheritance. Override one method, don't provide two.

::

    someObject.foo_method()

Transmutation
--------------

This is more subtle because there's no easy "wrong" implementation.
Instead of bad code, you have goofy questions.

For example:

-  http://stackoverflow.com/questions/394770/override-a-method-at-instance-level

-  http://stackoverflow.com/questions/597199/converting-an-object-into-a-subclass-in-python

Both of these are attempts to "dynamically" transmute an object
from one class into another.

There are two variants: people ask about having the superclass
morph into a subclass, or people want to make a class change so
that the object's behavior changes.

In the morph case, they've overlooked the essential truth of
inheritance. Every subclass object is an instance of the
superclass, too. If you think you want to transmute from
superclass down to subclass, that's silly because the subclass
object already is an instance of the superclass. By definition. If
you think you want to morph, you really want some kind of
**Factory** that spits out proper subclass instances.

In the state-change case, they've overlooked the power of
delegation and the **Strategy** pattern. If you think you want to
use a class change, you really want to plug in a different
strategy object.

Denial
-------

For example,
http://stackoverflow.com/questions/1020453/whats-the-point-of-inheritance-in-python.

The example is great. It proves that you don't need inheritance.
Sadly, the proof only works if you're overriding every method. If
you don't want to override every method, then inheritance suddenly
becomes useful.

The denial problem (all delegation, no inheritance) is a kind of
opposite to the transmutation problem (all inheritance, no
delegation).



-----

+1, its pretty rare to see accurate defenses of OO...
-----------------------------------------------------

mike bayer<noreply@blogger.com>

2009-06-21 12:30:30.763000-04:00

+1, its pretty rare to see accurate defenses of OOP and inheritance
these days.


I often see programmers try to make generalized ru...
-----------------------------------------------------

Bill Karwin<noreply@blogger.com>

2009-06-20 11:57:12.692000-04:00

I often see programmers try to make generalized rules to make their job
easier. Everyone is seeking a Golden Hammer. In truth, inheritance and
delegation both have advantages in different circumstances, and we
should use the right tool for the job. Deciding which is the right tool
in a given circumstance is the process of OO design.

But unless we can articulate the right way to employ inheritance vs.
delegation in a single succinct paragraph written at an 8th grade
reading level, there will always be a large portion of software
developers who want to simplify by saying "always" or "never" use one or
the other.


These problems are best solved by using functions ...
-----------------------------------------------------

Jon Harrop<noreply@blogger.com>

2009-06-21 16:30:21.815000-04:00

These problems are best solved by using functions instead of objects.


Whether the first problems is best solved with fun...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-06-22 03:00:47.734000-04:00

Whether the first problems is best solved with functions or polymorphism
depends on analysis of the likely changes. New functions/New Classes.
If new functions are constantantly being added to a fairly static set of
classes, functions (perhaps structured as visitor) are indeed better
than polymorphism.

If new classes are being added with a large set of independent
functions, classes are better.

At PyCon there was a talk where the use of patterns was identified to
frequently indicate a work around for a missing feature. Perhaps using
strategy is a work around for not being able to transmute an objects
class.

Since languages provide fairly weak support for delegation, I frequently
use inheritance. When I get more experience with a language with good
support for delegation I will be more aware of where inheritance is
really missed.





