OO Design Principles: CUPID
#######################################

:date: 2025-10-03 09:46
:tags: python,oo,oodesign,design principles,cupid
:slug: 2025-10-03-oo_design_principles_cupid
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

Very important: Composable, Predictable, Domain-based.

These are consistent with the idea that software is knowledge capture.

Maybe less important: Unix-Philosophy and Idiomatic.
While nice ideas, they feel a bit redundant.

CUPID
=======

See https://cupid.dev/properties/

Composable
-----------

Highly desirable to have small pieces that compose into something useful.
This fits with SOLID **Interface Segregation Principle**, and provides an answer to "but, why?"
We segregate the interfaces to create something composable.

Unix-Philosophy
---------------

This **also** implies composability.
It goes a step further to incorporate the idea of the SOLID Single Responsibility Principle.
The Unix design patterns provides concrete examples of how to decompose a large problem into smaller pieces;
each piece does one thing well.

Predictable
-----------

This decomposes into three distinct aspects:

-   A component behaves as expected. This is sometimes called the Principle of Least Astonishment.

-   A component's behavior is consistent and deterministic.

-   A component's behavior needs to be observable, also.

These are all critical features, especially observability.

Idiomatic
---------

Yes, follow language idioms. Please do not boldly go where no programmer has gone before.

This seems to go without saying. It does help fill up the acronym, though.
And, perhaps, it's necessary advice.

Domain-based
-------------

The solution code should mirror the problem domain. This is really important, and not present in other sets of design principles.

Indeed, I don't think it can be emphasized enough.

OO modeling and design isn't about optimization or code reuse.
It's about fidelity to the problem domain.

Code reuse is nice to have.
Providing common behavior among the problem domain objects that are being modelled is the point.

Conclusion
===========

These are nice. They're very useful in conjunction with SOLID design principles.

It helps to have guideposts to help clarify an underlying "why" we design software.
