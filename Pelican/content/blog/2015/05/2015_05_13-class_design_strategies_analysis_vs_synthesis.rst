Class Design Strategies -- analysis vs. synthesis
=================================================

:date: 2015-05-13 07:45
:tags: #python,analysis,OO design
:slug: 2015_05_13-class_design_strategies_analysis_vs_synthesis
:category: Technologies
:status: published

The conventional wisdom on class design is to model real-world things.
This is the Domain-Driven Design Approach. It's what we used to teach as
Rumbaugh's OMT (prior to the Three Amigos creating UML.)

The idea is simple: Look at the real world objects. Describe them.
Classes will have attributes and behaviors. They will have
relationships. Rumbaugh was very careful about keeping object and class
separate. A class had associations, and object had links. The
association was the abstraction, the link was a concrete implementation.
A class offered an operation, an object provided a method as an
implementation.

As powerful as this is, I'm not sure it's the final word.

The only problem it has is that people often get confused by "real world
objects." I've seen a number of places where folks completely fail to
distinguish Enterprise IT implementation choices from actual things that
reflect actual objects in the actual world.

Users and Credentials, for example. Users are real human beings. You
find them in the hallways, standing around. They take up space in
conference rooms. Credentials are a peculiar security-focused way to
summarize a person as something public (username) and something private
(password.) You don't find a stack of credentials tying up a room at the
end of the hallway. Indeed, you can't physically stack credentials.

While something a user knows is important, it isn't the entirety of a
User. The attributes and behaviors of credentials aren't a good model
for a User. But you still have this argument periodically when
developing a class model or a noSQL database document model.

I'd like to emphasize that this is -- as far as I can tell -- the only
problem with domain driven modeling. Some people don't see the domain
very clearly because they tend to stick to a technology-driven world
view.

However. That doesn't mean that drawing on the white board is the only
way to discover the domain.

Building Classes from Functions
-------------------------------

As a heretical alternative, allow me to suggest an alternative to the
whiteboard.

Once upon a time, the whiteboard was the only way to do object modeling.
The successor to the whiteboard (I use `Argo
UML <http://argouml.tigris.org/>`__ as well as Pocketworks
`yuml <http://yuml.me/diagram/scruffy/class/samples>`__) is a
diagramming tool that -- ideally -- helps you understand the domain
before committing to the cost and complexity of writing code.

Wait a second, though.

The "cost and complexity of writing code"? Java programmers know what I
mean. If you don't have your classes understood, you should **not**
start slapping code together.

Python programmers have no idea what "cost and complexity of writing
code" means. They slap classes together faster than I can draw the damn
pictures on Argo.

Indeed, the pictures can become a kind of burden. The picture shows
"x.X", therefore, the module must include "x.X". Even though there might
be a better way using classes in separate modules "a.Y" and "b.Z". But
changing the cluster of pictures that comprises a fairly complete UML
diagram isn't easy.

[*Clearly, this depends on how much you tried to show. If your diagrams
are really spare, refactoring is no problem. If you include parts of the
object model in the component diagram or activity diagram, you're in
trouble.*]

This leads to an alternative to the whiteboard. And the diagramming
tool.

Code. [*Cue Orchestral Hit: Ta-daaa!*]

Yes. Code. [*Cue Orchestral Hit: Ta-ta-ta-daaa!*]

When you can slap together a spike solution in Python you have a
sensible alternative to the whiteboard.

You can build some classes, write some demonstration code to show how
they work together. Don't like it? Start again from another base of
classes. You can do this as a `Mob
Programming <http://www.agilealliance.org/files/6214/0509/9357/ExperienceReport.2014.Zuill.pdf>`__
exercise. It fits somewhere between grooming a story and finishing an
MVP release. Indeed, it may be a good way to do specific, concrete
grooming.

In some cases, though, you can't build classes. You don't really know
(or can't agree) on what the real world things are.

Rather than debate, shift the focus. Just write functions.

In Python, this is easy, since functions are first-class inhabitants of
the programming model. In Java, this isn't easy at all. Functions aren't
proper things; they must be part of a class; and you can't agree on what
the classes are; the Java stalemate. [*Yes, Java 8 introduces
free-standing functions.*]

How This Works In Practice
--------------------------

In many cases, it makes sense to punt on the "big picture." You're not
really **sure** what you even have.  Yes, you know you have eight
individual CSV files that reflect events that happened somewhere in
cyberspace. (Let's just say they were the output from stored procedure
triggers; the only record of changes made to crucial data.)

You can wring your hands over the eight-table join required to
reconstruct the pre-change and post-change views of the objects. You can
wring your hands over the way it's really three (or is it four?)
different navigation paths from I to II to IV to (V to VI to VII) union
I to II to IV to (V to VI to VII) union I to III to IV to oh my god I'm
so confused.

Or.

You can get the sample data.  You can read it using the CSV module.
DictReader can awkward. It can be fixed, however. If your column titles
are legal Python variables, you can use this to create a namespace
reader from a DictReader. This allows you to say ``row.ATTRIBUTE`` instead
of ``row['ATTRIBUTE']``.

::

    def nsreader(dictreader):
        return (SimpleNamespace(**row) for row in dictreader)

We can then turn to working out the various join algorithms on real
data. Each step builds objects based on types.SimpleNamespace.
You start with simplest possible join algorithm: load everything into
dictionaries based on their keys.

::

    I_map = { row.KEY: row for row in nsreader(table_I_dict_reader) }
    II_map = { row.SOMETHING: row for row in nsreader(table_II_dict_reader)
    }

Once you have sample data in memory, you can figure out what the actual,
working relationships are. You can tinker with navigation paths through
the tangled mess of tables. You can explore that data. You can do data
profiling to find out how many misses there are.

If the tables are smallish (10,000 rows each) it all fits in memory
nicely. No need for fancy database connections and no need to reason out
join algorithms that don't tie up too much memory. You're not writing a
database server. You're writing an application.

Look For Common Features
------------------------

The design issue for classes is locating common features: common
attributes or common methods. We often start down the road of common
attributes. Because. Well... it seems logical.

Focus on attributes is a bias.

Classification of objects isn't based mostly on attributes. It's not
50-50 objects vs. attributes.

We tend to focus on attributes -- I think -- out of habit. Data
structures mean "common data", right? Databases include tables of
commonly-structured data.

But this isn't a requirement -- nor is it even important. It's just a
habit.

We can conceive of a class hierarchy based around common behavior, too.
This may require a very flexible collection of attributes. On the other
hand, there's no *a priori* reason not to define classes based on their
behavior.

That's why the idea of building functions first doesn't seem too
far-fetched.

First, we can build working functions.  We can have test cases and
everything.

Then we can look for commonality. We can refactor into classes. We can
start with a
`Flyweight <http://en.wikipedia.org/wiki/Flyweight_pattern>`__ design
pattern. As common attribute emerge, we can refactor to store more state
in the class, and less state somewhere else. The API changes while we do
this.

Then we examine it for the "is this a thing" criteria. Last, not first.
We may need to make a few more tweaks to reflect the thing we discovered
scattered around the functions. The thing may be a checklist or a recipe
or a procedure: something active instead of simply stateful.

This tends to make RESTful web services a bit of a head scratcher. If we
have an active thing, what is the state that we can represent and
transfer? The state may be very small; the active agency may be quite
sophisticated. This shouldn't be too baffling, but it can be confusing
when the GET request response is either 200 or 403/409: OK or
Forbidden/Conflict. Or there are multiple shades of 200: 200 OK with a
body that indicates success, vs. 200 OK with a body that indicates
something more needs to be done, vs. warnings, vs. exceptions, vs. other
nuanced results.

Summary -- tl;dr
----------------

I think there's a place for code-first design. Build something to
explore the space and learn about the problem domain. Refactor. Or
Delete and Start Again. In modern languages (i.e., Python) code is
cheap. Whiteboard design may not actually save effort.

I think there's a place for building functions and refactoring them into
classes. I think the Java pre-8 "All Classes or Burn In Hell" approach
is misleading. Functional programming and languages like Python show
that functions should be a first-class part of programming.

I think there's too much emphasis on stateful objects. The DDD warnings
about "anemic" classes seems to come from a habitual over-emphasis on
state and an under-emphsis on operations. I think that active classes
(as much as they push the REST envelope) might be a good thing.





