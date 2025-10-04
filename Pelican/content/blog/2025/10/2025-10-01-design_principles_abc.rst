OO Design Principles: ABC's
#######################################

:date: 2025-10-01 09:46
:tags: python,oo,oodesign,design principles,abc
:slug: 2025-10-01-oo_design_principles_abcs
:category: Python
:status: published

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

ABC's are only **required** as a way to do earlier validation that a class is complete.

Otherwise, they're not required.

They can be helpful when planning dependency injection.
The SOLID Dependency Inversion Principle advises us to depend on abstractions, not concrete, specialized subclasses.

In Python, we don't **need** an abstraction at the base of a class hierarchy.

Purely OO Design?
=================

First, I want to talk a little bit about OO design and "purely" OO languages.

Unlike Java or C++, Python is purely object-oriented. Not that it actually matters.

A functional style of Python depends on functions which are -- essentially -- callable objects.
They have one method, ``__call__()``.
They have attributes.
Because they descend from the ``object`` class, you can add attributes to a function.
They're instances of a type, ``function``.

Java and C++ have "primitive" types which aren't objects; they're not "purely" OO.
Python doesn't have this quirk.
Python is more purely object-oriented than Java.
Which suggests any OO purity test doesn't really matter.

OO Design Principles and Functional Design Principles can all be used with Python.
Indeed, some of the old COBOL design patterns can be used, too.
(Not all, of course. COBOL had GOTO's, an ALTER statement, and a very weird PERFORM THRU that make it right weird to map to Python.)

OO Purity? Doesn't matter.

Let's move on to look at Python's ABC's.
After that, we'll look at the SOLID principles in general.

To ABC or not to ABC?
=====================

C++ and Java (and many other languages) are built around separately-built binaries that are linked together.
Some linkage can be done at compile time, some can be done at run time by the OS loader.
Since they're separately-built binaries, everyone **must** agree on the binary interface.
Change cannot be tolerated.

I'll emphasize that.

..  admonition:: Emphasis

    C++ and Java emphasize a style of design where interface changes cannot be tolerated.

Pragmatically, we now have computers that are so fast that recompiling a very large Java or C++ app is no longer a nightmare of waiting for hours.
When these languages were designed, a development team might do one nightly build of everything.
During the day, you were limited to compiling the classes you were working on.
Nothing more.
Getting the interfaces to be stable was an important risk reduction technique.

Abstract Base Classes were a way to minimize recompilation.

..  important:: Abstract vs. Concrete

    There are abstract base classes and concrete base classes.
    The ``abc`` module introduces a whole bunch of stuff to support abstraction.
    Ordinary ``class Special(Die):`` inheritance from a concrete base class
    involves no abstraction, and no ``abc``.

Python eschews strict class hierarchies, and replaces this with "Duck Typing".
All an object requires is to have the method defined.

See `The eval() Conundrum and Python-as-DSL <{filename}/blog/2025/09/2025-09-28-the_eval_conundrum.rst>`_.
Way at the end is this snippet of code.

..  code-block:: python

    class Die:
        def __init__(self, faces: int) -> None:
            ...
        def __rmul__(self, n: int) -> "Die":
            ...
        def __add__(self, adj: int) -> "Die":
            ...
        def roll() -> int:
            ...
        @property
        def min(self) -> int:
            ...
        @property
        def max(self) -> int:
            ...

    D4 = Die(4)
    D6 = Die(6)
    D8 = Die(8)
    etc.

This means an object like ``D4`` can be used with the ``*`` and ``+`` operators.
In very limited ways.

The expression ``6 * D4`` is legal, where ``D4 * 6`` is not.
The way Duck Type works, there's a search for a method to implement ``*``.

Consider ``6 * D4``.

1.  Does ``6`` implement ``__mul__()``?  It does.
    However, when ``int.__mul__()`` is evaluated with a ``Die`` object, the result is ``NotImplemented``.

2.  Does ``Die`` implement ``__rmul__()``?  It does.
    When ``Die.__rmul__()`` is evaluated with an ``int`` object, the result is a new ``Die`` object.

(There's actually a first step, omitted for brevity. See the sidebar.)

Here's the bottom line.

    The Duck Typing two-step search for matching method names doesn't respect the class hierarchy.

..  sidebar:: The other step?

    There's an initial check which **does** in a limited way, reflect the class hierarchy.

    Is ``Die`` a subclass of ``int``?
    If ``Die`` was a subclass of ``int``, then ``Die`` must be considered first to permit a subclass to override a superclass.
    This reverses the **order** of the other two steps.

    A class hierarchy can shift the order of the Duck-Typing Two-Step.

A ``Protocol`` formalizes the Duck-Typing Two-Step in a way that tools can be sure the whole

**Summary**:

1.  When using only Python, most developers don't need to care about separately-compiled binaries.
    (When writing Rust or C extensions, of course, separately-compiled binaries are a big deal.)

2.  Duck typing eliminates a **requirement** for ABCs.

Conclusion
==========

Is an Abstract Base Class **still** helpful?
---------------------------------------------

Yes.

When?
-----

When you need it.

When is it necessary?
----------------------

The use case for an ABC in Python is to push the Duck-Typing Two-Step so it happens earlier.

1. ABC's permit type hint checking to be sure the code is likely to work.

2. At run time, ABC's prevent instantiating an incomplete object. Code may crash earlier.
    Most important: the exception is much more clear when a method is missing.

ABC's promote early detection of design problems.

When is it superfluous?
-----------------------

When your base class is concrete, don't waste time on an ABC.
Just use a concrete base class and extend it as needed.

That's enough on ABC's for now. Let's move on to the SOLID principles.
