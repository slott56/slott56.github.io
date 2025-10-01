OO Design Principles: GRASP patterns
#######################################

:date: 2025-10-04 09:46
:tags: python,oo,oodesign,design principles,grasp,patterns
:slug: 2025-10-04-oo_design_principles_grasp_patterns
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

The GRASP patterns can be helpful reminders.

Some GRASP patterns sound like design principles, and seem to overlap with the SOLID principles.

Other GRASP patterns seem like summaries, with a number of fine-grained implementation choices.

Controller and Pure Fabrication seem most helpful.

The "Gang of Four" Object-Oriented Design Patterns seem to be more useful and have more supporting details.

GRASP Patterns
==============

See https://www.geeksforgeeks.org/system-design/grasp-design-principles-in-ooad/

Controller
----------

See also the "Model-View-Control" pattern.

There's an internal model of reality. A description of the real-world stuff.
Maybe this is simply CRUD rules over a database (as if a database is reality -- it's only a model.)
Maybe this is an OO model that gets serialized into something persistent when the application exits (you know, like a word processor or spreadsheet.)
Maybe this is an OO model of a game where there's a state-of-play saved when you specifically ask to save.
Maybe this is a real-time controller of a device like a cruise control on a car where the model has the car's current speed and the target speed (and not much else, TBH.)
Maybe this is an anchoring position indicator with a position where the boat is expected to be and the most recent few minutes of GPS positions indicating if it's within a safe distance of the anchor or not and what direction the boat seems to be going (i.e., it is adrift?)

There's a view of reality, displaying the state of the model.
You fiddle with the view to update the model.
Maybe look at the number on the dashboard or push buttons on the cruise control.
Maybe type a bunch of stuff into fields on a form.

And there's the controller.

    "The controller is defined as the first object beyond the UI layer that receives and coordinates ("controls") a system operation. "

This applies widely.
In some applications -- programs like ``grep`` and ``sed`` -- the UI is really tiny and not interactive.

-   The input is command-line parsing (via ``argparse`` or ``click`` or whatever).

-   The output is stdout and stderr (via ``logging`` or ``print()`` or whatever).

-   There's a model (the file being processed, the text in that file, the patterns and commands).

-   There's a **tiny** controller that gets the input, then iterates through the model's visible state changes, writing the outputs.

This is one essence of **Clean Design**. Seperating the inputs and outputs from the model and control.

Creator
-------

There's potential overlap between Creator and `Information Expert`_.
Creators have the information required to create an instance of a collaborator.
Which sometimes means the creator is also an expert.

Indirection
-----------

Somestimes helpful. The Gang-of-Four design patterns subdivide this many ways.
You might have an Adapter or Facade to wrap one (or more) collaborators.
You might have a State or Strategy class hierarhcy that wraps up alternative implementation choices into a tidy structure.

Note there are two layers of indirection.
Objects can have indirect access to other objects, perhaps mediated by the current state.
Classes **should** have indirect access to other class definitions, per the SOLID **Dependency Inversion Principle**.

Information Expert
------------------

The SOLID **Single Responsibilty Principle**, restated. Nice to see everyone agrees on this.

Low Coupling
------------

This is a desirable feature of object design.
This is more of a principle that echoes the SOLID **Interface Segregation Principle**.

High Cohesion
-------------

This is also a very desirable feature of object design.
This isn't (explicitly) a SOLID design principle, but lurks in she shadows of the SOLID **Single Responsibilty Principle**.
In order to have a single responsibility, there must be a cohesive design to the class.

Polymorphism
------------

This is a mechanism as well as a **large** number of patterns.
The mechanism is a way to reuse code in a class hierarchy.
It saves repeating things when we have related classes.

The reason why we have a SOLID **Liskov Substitution Principle** is to manage polymorphism.

The entire Gang-of-Four design patterns book is an extended set of patterns for applying polymorphism.

Protected Variations
--------------------

This is a restatement of the SOLID **Open/Closed Principle**.
Open to extension (via variations.)
Closed to modification (the "protected" part of this.)

Pure Fabrication
----------------

I often call these frabricated classes part of the "Solution Domain" distinct from the "Problem Domain."

The model is part of the Problem Domain.
It represents the real-world things in software space.
This should map to the problem domain with a high degree of fidelity.

The view presents this to users.
It's part of the UI, which is part of the solution.
It can overlap with the problem domain, however, and may happen to match the model.
A CRUD application, for example, may display the data more-or-less directly and the view may match the model.

In some cases, the view twists and transforms the model into what people think they want to see.
Think of the aggregated data in a data warehouse.
Details are elided. It's a summary -- it's not the reality.
A great deal of twisting and turning happens during ETL and aggregation processing to provide a view the users can understand and act on.

A controller, however, has nothing to do with the problem domain.
It's *purely* part of the solution domain.
It reflects the purpose behind the software -- show status, update things, allow interaction, summarize, whatever.


Conclusion
===========

The GRASP patterns can be helpful reminders of different kinds of solutions.

They overlap with -- and can provide some amplication for -- the SOLID design patterns.

The Pure Fabrication and Controller GRASP patterns seem to be more significant than the others.
