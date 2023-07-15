Python and Encapsulation -- How do I private?
##############################################

:date: 2023-06-20 08:00
:tags: architecture,software design,design patterns,python
:slug: 2023_06_20-python_and_encapsulation
:category: Technologies
:status: published

Central to OO design is "encapsulation." It's so central it is part of several separate principles.

In the S. O. L. I. D. design principles it's the **Interface Segregation Principle**.
And a significant part of the **Single Responsibility Principle**.

In some cases, Python n00bz -- folks who already know some OO programming in other languages -- complain
that the usual artifacts of encapsulation are missing from the Python language.

There's no **private** or **static** or **protected** keyword.

How can we implement super-important encapsulation without this super-important text marker in the source?

I'll address this from two points of view: what to do, and what not to do.

What to do
==========

Design with encapsulation in mind. Follow the S.O.L.I.D. design principles.

I suggest starting with Interface Separation.

For things that aren't part of the public API (perhaps "private" in some sense) use a leading ``_`` in their name.
One ``_`` only, please.

For things that are "protected", or "final", you probably don't need to do anything.
If you're really **really** worried about someone misapprehending your design intent,
include many comments.

If you're **sure** someone will utterly disregard your comments,
misuse a private item outside the class,
or misuse a protected item outside the package or subclass,
or extend a final item,
or some other nefarious thing, well, there it is.
You'll have to ask yourself why this feature is both private/protected and so appealingly attractive.
If you can't discourage people from abusing it, perhaps there are other design problems.

What not to do
==============

A ``__name`` is mangled to make it an implementation detail of a *specific* class.
These names tend to defeat ordinary inheritance.

Don't use double-underscore before-and-after ``__names__`` at all.
Never.
These are not conventionally "private" -- these are implementation details.
The name space is reserved to be part of Python's run-time.

Other double-underscore before ``__names`` are private, but are private to the class.
They cannot easily be overridden by a subclass. This is by design, and these are
specific solutions to the problem of implementing something where an override
is constrained to a single class in a hierarchy.

See https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers

Here's the quote:

    "Names in this category, when used within the context of a class definition, are re-written to use a mangled form to help avoid name clashes between “private” attributes of base and derived classes."

This is not conventional encapsulation.

Some additional thoughts
========================

Some questions I ask when people have **Serious Problems**
with Python's approach to privacy.

Question 1 -- Is private really important?
-------------------------------------------

Let me state as a going-on assumption that encapsulation is an important part of an OO design.
Failure to encapsulate can create incomprehensible state changes, which is isomorphic to
a lot of functions sharing global variables. That's precisely the thing OO design
lets us avoid.

So, yes, private -- as a design concept -- is very important.
Perhaps it's the single most important of OO design.

Inheritance follows behind encapsulation. It's riddled with disputes
because we can often use delegation instead of inheritance.

Question 2 -- Given encapsulation, what more does the language need?
--------------------------------------------------------------------

In other words, Python lacks a ``private`` keyword: is this a problem?

Python's notion of "hidden-ish" attributes and methods
seems to be perfectly adequate.
The leading ``_`` on the name seems to be **more** visible
than having to look back at a class definition to
see if a name is public, protected, or private.

It looks like this.

::

    class MyExampleClass:
        def visble_method(self, anArgValue: int) -> None:
            self._less_visible_method(anArgValue * 2)

        def _less_visible_method(self, anArgValue: int) -> None:
            self.anAttribute = anArgValue

The ``visible_method()`` method is considered "public".

The ``_less_visible_method()`` method is considered by most to be "private".
Yes, we can all see the method when we read the source.

Many tools will make some effort to hide this behind a thin screen.

Many developers understand this distinction. Sometimes n00bz don't -- at first -- recognize this convention.
They might complain that the ``_less_visible_method()`` method is missing from the API documentation.
Then they're told this is because it's an implementation detail they can't depend on.
Then they complain that it's still visible in the source -- they can see the implementation!
It's not **really** private!

The language makes no distinction between these methods.

The leading ``_`` is a convention. Widely-followed. Pretty universally adopted.
But not formally part of the language semantics.

Some linters will remind you that you've broken the rules by using a "private" method
from outside the confines of the class hierarchy.

Do we need more? Let's dig into what more we might ask for.

Q2A1. The language needs formal semantic support for private
-------------------------------------------------------------

Q: Why?

A: Because I need all the tools to absolutely guarantee that I don't abuse this.

Recall the use for privacy is to help us **design** API's cleanly.
Keywords like ``protected`` and ``final`` are part of a design effort.
They're (sometimes) helpful information for designers.

They're easily overlooked when using the class.

And, at run-time, they cease to be useful.

Do we really want the byte-code interpreter to be checking some kind of "ownership" before each
write to memory?

The usual answer is "No."

For a compiled language, privacy is honored as part of code generation.
But. That's essentially the same as having a convention and using a linter to
confirm the convention is followed properly.

(And yes, "language + linter" is not the same as "language".
Those folks who can't tolerate the "two-ness" of it
can write a shell script to bundle a linter with the Python run-time.
After all, that's how gcc used to work. It was a bundle of precompiler, C++ to C translator,
and the C compiler, which -- itself -- was a multi-step operation to build code.)

Q2A2. The languge tools must support private
---------------------------------------------

Q: Why? Do you have trouble seeing the ``_``? Do you have trouble remembering the semantics? Do you like referring back to the class definition all the time to see if a name is private or not?

A: Don't be an ass with questions like that. Of course **I** see it. Of course **I** know what it means. I worry about others, who aren't as gifted in the programming. Everyone knows there's always *someone* who can't follow the simple rules.

This is about projecting nefarious intent on others?

Some folks insist a Very Clever IDE (VCI™) would recognize context and provide
private or protected attributes in a drop-down list of alternatives based on
context. That seems nice, I suppose.

We've wandered far from the design intent behind encapsulation and into
areas of IDE UX. A UX can identify leading-\ ``_`` variables pretty well,
and mark them as not public.


Some Backstory
==============

The quote that drives this is "We're all consenting adults here."

This summarizes the idea that Python is distributed as source.
We can all see the implementation.
The notion of "private" is -- at best -- a suggestion.


(Tangentially related: `Python Big Picture -- What's the "roadmap"? <{filename}/blog/2015/12/2015_12_08-python_big_picture_whats_the_roadmap_revised.rst>`_.)
