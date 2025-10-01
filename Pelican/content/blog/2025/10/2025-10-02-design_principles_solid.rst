OO Design Principles: SOLID
#######################################

:date: 2025-10-02 09:46
:tags: python,oo,oodesign,design principles,solid
:slug: 2025-10-02-oo_design_principles_solid
:category: Python
:status: draft

..  background:

    I’ve been reading quite a lot in the book “Fluent Python”. It's a brilliant resource and is helping me understand details of Python that I hadn't even looked at before. In the last few chapters I read several times that ideally I should avoid inheritance with ABCs and if I do, then from a standard class. That is, I should avoid creating a typical base and subclass construct that is used in a strategy pattern, for example.

    If I look at a principle like SOLID, where we have the Liskov Substitution Principle, the interface separation principle, and the dependency inversion principle, they all rely on a base class, which of course is created by inheriting from ABC. I think as long as we do not have concrete methods in the base class, this could be a protocol instead.

    However, I've been thinking about the general meaning of SOLID for Python. I can see these principles in an object-oriented only language like Java. Since this is the first language I learned, my intuition tells me that the language is perfect for following the principles. Python, on the other hand, does not have the strong need to be object-oriented, but most of the principles assume that we are working with classes. Often it's just easier to use a functional approach. An example would be the strategy pattern, where instead of having a construct of different classes that handle a specific strategy, we just have different functions. The intent for a developer is very explicit when using those, and I don't see the need for an ABC and inheritance from it. The only advantage I would see is to put it in a class that uses Protocols to enable type hints.

    I've also read about the GRASP principles, but some parts of it don't feel very natural to me in Python either. For example, very obviously, polymorphism, which is also not needed in Python. Of course, low coupling and high cohesion are rather language-agnostic concepts, and they seem to fit very well with Python.

    I know that these principles are not a religion, and I don't have to follow any specific one. I know I can take ideas from multiple ones and stack them together. However, I like the basic idea of dependency inversion, interface segregation and Liskov Substitution and used it in one of my products. Working with Liskov Substitution can make it difficult to navigate through an IDE. This plus explanations I’ve read in Fluent Python make me think that I've made my life more difficult with it, but I wonder what would be pythonic here?

    Since I couldn't find a helpful discussion online, I was wondering what others experience is and how they approach this? Do you follow any principles like SOLID or GRASP or do you find a mix to be the best option? I've been looking for articles that discuss this but haven't found a great resource. I'd love to hear your thoughts and experiences and if you know of a great resource.

Some quotes to provide context.

    "I read several times that ideally I should avoid inheritance with ABCs and if I do, then from a standard class. That is, I should avoid creating a typical base and subclass construct that is used in a strategy pattern, for example."

    "If I look at a principle like SOLID, where we have the Liskov Substitution Principle, the interface separation principle, and the dependency inversion principle, they all rely on a base class, which of course is created by inheriting from ABC."

    "Python, on the other hand, does not have the strong need to be object-oriented, but most of the principles assume that we are working with classes."

    "Working with Liskov Substitution can make it difficult to navigate through an IDE."

BLUF
====

Apply the design principles with a kind of priority mind-set.

1. Interface Segregation. Always.

2. Liskov Substitution where you actually have base classes or protocols.

3. Open/Closed. Always.

4. Dependency "Inversion" (I prefer "Injection"). Think of this as an optimization.

5. Single Responsibility. Here is where various GRASP patterns apply at this point here to help implement a "single" responsibility.
    Remember, GRASP are implementation patterns not quite the same as design principles.


SOLID Principles
================

I find the SOLID acronym is confusing. Mostly because the principles are presented in a funny order.
While the "Single Responsibility" principle is first, and seems most important, it's really more of a summary.

ISP
---

The "Interface Segregration" principle is -- perhaps -- the most important.

..  important:: Interface Segregration Principle

    ISP == Cut the fluff seen by collabators.

In a C++ or Java context, the more that's exposed to a collaborator, the wider the ripples from a change.

In a Python context, a too-rich interface is just annoying to understand, maintain, extend, and test.

One metric for paring down an interface is the number of mock objects needed for an isolated unit test.

(Some Facade and Adapter designs will have a lot of mocks because they're wrapping complicated things in a simple interface.
Don't apply the "minimize mocks" metric blindly.)


LSP
---

Remember, Python has duck typing. LSP is something that applies if -- and only if -- inheritance is being used.
A bunch of classes can all implement a common protocol without being suclasses of each other.

An Abstract Base Class has the abstract methods marked so that an object cannot be created.
When all of the methods are defined by some subclass, it's now concrete and an object **can** be created.

A concrete base class can be extended as needed, and any class in the hierarchy is usable.
There won't be any "Can't instantiate abstract class" exception.

In order to make LSP work, it's very helpful for subclasses to **add** features to base classes.
Base classes should be a minimal foundation; think of them as a generalization.
The extensions should add features; they will be specializations.
(It's not mandatory, it's just kind of tedious to write "do nothing" methods for a subclass to take away a base class feature.)

OCP
---

This requires some consideration of the sources of change and the kinds of extensions that might be necessary.

It's rather difficult to do well when working on a problem domain that's not well understood.
After creating some code -- and living with it -- it's easier to see what's likely to change and what's likely essential.
Once the change vectors are more clear, it becomes easier to see what parts of a class are likely to be extended.

..  important:: Open/Closed Principle

    There are no "bug fix" changes where you modify a class.

    Instead, think about extending a broken class with a subclass that has less buggy implementations of methods.
    The app then needs to use the subclass that's not as broken.
    Change happens through extension, not modification.

    Doing this means "Dependency Injection Principle" needs to be used **also.**

DIP
---

Dependency "Inversion" really means don't have simple names of classes everywhere.

In Java and C++ collaborators with a class would have a reference to that class compiled into them.
Change some class, and the collaborators all need to be recompiled.
No one likes this.

In Python, the name resolution happens at run-time, and there's no additional overhead from making a change.
(The name lookups are an overhead that's inherent in Python.)

In Python, the dependency injection means assigning a target class to a variable instead of simply using it.

..  code-block:: Python

    class SomeThing:
        def __init__(self, this: str, that: int) -> None:
            self.this = this
            self.that = that

    class Collaborator:
        what_to_build: type[SomeThing] = SomeThing
        def __init__(self, arg: str) -> None:
            self.something: SomeThing = self.what_to_build("this", arg)

The name of the thing to build is a class variable in the ``Collaborator`` class.
Making a change to the class used internally by the ``Collaborator`` class is isolated to this variable.

We can make a subclass of ``Collaborator`` with a new value for ``what_to_build`` and change it's behavior.
We can go further, of course, and have some centralized configuration that names the classes to use.
That can be handy in very complicated applications where a lot of things are likely to change.

As a practical matter, very few things change.
A small configuration object with a few critical class references is all that's really required.

SRP
---

The most difficult of of the SOLID design principles is identifying a "single" responsibility.
The question of responsibility often requires some qualifiers.
It's important to consider responsibilities from which collaborator's perspective.

A class may do a bunch of things internally.
But -- viewed from outside -- it's a single, atomic behavior.

This is where the nine GRASP patterns can come in handy, to implement a class with a single responsibility.

Conclusion
==========

Apply the SOLID principles carefully.

Always apply ISP, OCD, and DIP.  Use LSP when there's inheritance involved.
The SRP requires some careful thought, and -- from different perspectives -- can be awkwardly complicated.

The GRASP patterns can be helpful for implementation. Sometimes they are overly focused on Java and C++.
