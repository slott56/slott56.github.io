Refactoring and Unit Testing
============================

:date: 2006-10-11 00:19
:tags: #python,unit testing
:slug: 2006_10_11-refactoring_and_unit_testing
:category: Python
:status: published





I do a fair amount of manual refactoring.  I've
used WebSphere Studio (Eclipse) to do some automated refactoring, so I have some
experience in using IDE's which exploit Java's static type-checking.



However, the question of
type checking in a dynamic language is interesting.  I don't use a sophisticated
IDE for Python development.  So, I have limited experience using an IDE to do
refactoring in a dynamic language.



However, JB notes

    "I'm having
    some heartburn about hierarchical type
    systems as a way of determining 1)
    conformability and 2) managing commitments of
    semantically equivalent behavior.

    ...

    Seems a constraining way to do it, to me, not
    that I have a better alternative at the
    moment."



Duck Typing
-----------



Since Python relies on
`Duck
Typing <http://en.wikipedia.org/wiki/Duck_typing>`_ , refactoring takes on an interesting new dimension.  We aren't
constrained to simply shuffle methods up and down the class hierarchy.  We are
now able to -- well -- put a method just about anywhere. 




Further, since Python doesn't have a
simple, single-inheritance model, the "hierarchical" type system doesn't
completely apply.



For these reasons,
refactoring in Python is one potentially complex problem.



From what I understand of
Ruby, you can override a class method without creating a subclass, essentially
redefining a base class in some obscure way.  This gives me the willies because
it makes refactoring a problem without any sensible boundaries.  Maybe I'm
misunderstanding Ruby, and have this wrong.



Essential Use Cases
-------------------



The principal refactoring
use case involves moving a common method up the inheritance hierarchy.  As a
practical matter, this does happen once in a while.



An additional text-book
refactoring use case arises when we're adding or removing whole methods in the
subclass hierarchy.



The fringe use case is a variation on the theme of ``SubClass1.methodA``
looking a lot like ``Subclass2.methodA``,
but they're not the same.  There are two interesting cases.

-   ``SC1.mA()`` is a superset of ``SC2.mA()``.
    All of ``SC2.mA()`` `gets refactored up, and ``SC1.mA()``
    overrides it to add features.

-   ``SC1.mA()`` overlaps with ``SC2.mA()``.
    Some common functionality has to get extracted, moved up the hierarchy;
    ``SC1.mA()`` and ``SC2.mA()`` are rebuilt around this common kernel.

-   ``SC1.mA()`` has no usable relationship with ``SC2.mA()``.
    What now?  In some cases, a complete change in design may be called for.  The mere
    presence of this situation is diagnostic of the designer having missed
    something.



Beyond the Fringe
------------------



Outside the fringe of
ordinary refactoring are the **New Design Pattern**\ ™ situations.  Mostly, these are
**Strategy** situations, where what looks -- initially -- like a variant method grows into a
different approach as we learn more about the
solution.



Consider a pair of ordinary
Entity classes that look like different entities because of different behavior. 
However, they have the same attributes, and almost identical methods.  The only
difference is one algorithm.  This can be done through inheritance, but
sometimes that variant algorithm is only the tip of the iceberg, and there is
more variability just below the
surface.



At this point, we realize we need a
**Strategy** hierarchy to contain the variant algorithms, not a hierarchy of ordinary
Entities.  How does refactoring work here, where we're moving the functionality
out of a class hierarchy into a different class hierarchy?  Is this even
refactoring, or is it the more general case of redesign?



It doesn't feel like
refactoring because  we aren't shuffling methods up and down the class
hierarchy.  In Python, the Duck Typing means we don't actually need a proper
hierarchy for the **Strategy** class definitions.  Consequently, we're free to make significant structural
changes that I don't think an IDE can ever help with.



Across the Spectrum
-------------------



One potential problem
with this is captured in the comment that "[the compiler] can’t help but
see your code as a pile of text".  By extension, then, the IDE can't do anything
more than treat source as text, losing precious semantic information. 




However, when doing a fundamental
restructuring (from class methods to Strategy hierarchy), the source code
information available to the compiler (or the IDE) isn't of much value until
you've finished.  Nothing helps you when you're in the middle of this.  Until
the semantic information exists, no IDE can help you manage and maintain the
semantic information.



There are parts of design (and redesign) that are hard.  I think anyone would agree that the
earliest phases of noodling around about a problem are done without benefit of
an IDE or formal semantics.  When the design is merely conceptual, tools can't
help.



I think refactoring includes a very broad spectrum.  At one end, things are essentially mechanical; at the
other end things, are completely conceptual.  This isn't really a problem that
needs a solution; it doesn't need tools.  It's part of the game of moving from a
good idea to software.  Some parts of the good idea don't have formal semantics.
Eventually, when formal semantics exist, tools can be
applied.



In the case of Python, I suspect that IDE support for refactoring could only be feeble at best.  The
mechanical end of the spectrum is so easy that tools aren't required.   At the
conceptual end of the spectrum, tools don't help in the first place.



The Middle Ground
-----------------



One might argue that simple, mechanical refactoring can be aided by the presence of static type
declarations.  However, my experience is that this covers only the most mundane
of the refactoring use cases.  In Python, we just move the method around. 




In Python, there's a double whammy:
checking types can't be done because the language traditionally lacked type
declarations.  Further -- and more important -- type checking doesn't need to be
done because the language is dynamic.  It can't be done, and even if it could,
it didn't matter anyway.



This is overly
simplistic, however.  There is some type checking which can be done in Python. 
The `epydoc <http://epydoc.sourceforge.net/>`_  package does considerable analysis of
source as part of writing documentation.  It spots unused arguments, and can
spot certain kinds of obvious mismatches in number of arguments vs. parameters. 




When we look at JB's point on
committing to specific semantics, we see something even more profound.  It goes
way beyond what even Java is capable of checking or
automating.



The Formal Specification
------------------------



JB is asking for a
level beyond syntax, beyond type matching and off into "intent".  JB appears to
be looking for formal assertions of preconditions and postconditions that he can
use to determine how to redesign methods to make them refactorable, and then how
to refactor the changed design.



JB's formality would be a nice thing to capture.  If every statement had a proper
precondition and postcondition, then we could prove almost anything about our
software except whether or not the loops actually terminated.  (That can't be
formally proven in a system with the same expressive power as software, it
requires more sophisticated logical tools.)



Since Java and Python have
added additional markers (annotations and decorators) JB's assertions could be
captured, to an extent.  You'd have to implement a simple "for all" and "there
exists" predicate, but Python has a nice reduce that can be paired with a lambda
that allows you to write a "for all"; from this you can built a "there exists". 




I'm not sure how helpful formal assertions would be.



Pragmatic Refactoring
---------------------



When working in the
center of the refactoring use cases, IDE aids are helpful.  When working at the
fringe, they're just visual noise.  Indeed, when redesigning something, I have
to be sure not to look at any of the "helpful" messages from Eclipse because
it's checking for errors using obsolete type information.  When I've broken the
whole thing down into a workbench full of parts, the semantic checks aren't even
meaningful.  Once I get it put back together again, automated checking can be
handy to assure a complete job.



In Python, breaking the whole thing down as part of a redesign is so much simpler.
We don't have the artifice of "interface" to keep to a single inheritance model
with static type checking across multiple aspects of a class.  We just move the
methods around.  We have multiple inheritance, and we don't need formal
interface declarations.



Indeed, it's
far, far easier to produce a working design in Python, and use that as a formal
specification for a Java program.  I can tweak and tinker, optimizing
performance and simplifying without the rigid formality of Java.  Adding proper
class hierarchies and turning multiple inheritance into single+interface
inheritance is typically a pretty easy transformation.  Since I knew I was
aiming at Java in the first place, I avoided Pythonisms that don't translate.



While it's true that we
don't need Java's formality in Python, much of that formality is helpful.  I
find it easier to work with a proper inheritance hierarchy, one that has
explicit Not Implemented exceptions to mark the place-holders.  I like to have a
tidy interface definition so that I can document the interface.  This additional
material makes refactoring slightly more complex, but could help an automated
tool do some useful method matching among classes.



The Final Test
---------------



Without appropriate unit
tests, refactoring is impossible.  Even in Java, with a swanky IDE that checks
everything, you still have potential problems which are uncheckable.  In
particular, a mis-named subclass method cannot be detected except by "near-miss"
fuzzy-matching rules that will almost always work and will have false-positives.
Only unit testing can locate this situation.



Unit testing absolutely is a
stand-in for things the compiler can't check.  You can portray the heavy use of
unit testing as a negative ("the compiler can't be trusted") or as a pragmatic
approach to verifying the things you can't formally state.  All of the
assertions in the world won't find a spelling mistake.



Worse, your formal
declarations (post-condition assertions or type definitions) could just as
easily be wrong.  A tidy formal proof with a wrong piece of logic will derive an
incorrect program.  A misspelled class name may compile, but still fail a suite
of tests.



Since the IDE can't register intent very well, it isn't a complete solution.
In the case of redesign, it isn't even very helpful.








