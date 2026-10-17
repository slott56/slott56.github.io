Object-Oriented Design: Binary or Enum?
#######################################

:date: 2026-10-17 07:41
:tags: object-oriented design,enum,binary
:slug: 2026-10-17_oo_design_binary_enum
:category: Architecture & Design
:status: published


BLUF
====

Some aspects of a problem are superficially binary, perhaps modeled as a boolean value.

Don't be misled.
Some aspects of a problem are clearly **not** binary, and a boolean is wrong.
Other aspects may or may not be binary, and a boolean might not be ideal.

Clearly Not Binary
==================

Some part of a problem domain might be described as a simple binary condition or state.
Often, the claim is untethered from objective reality.
For example, recording a person's gender as a binary ("male = True") is nonsense.

(Full disclosure: back in the 70's, we did this kind of thing.
We ignored the reality of some of the people around us.
I can only issue a weak retroactive apology.)

Binary with a Story
====================

We often have situations where some condition has a story.
The story might be something like one of these examples:

-   Not Applicable.
-   Invalid or Rejected.
-   Pending some other processing.

When an attribute has a story, the story is metadata describing the current state.
In this example, it describes why a binary attribute isn't (currently) one of the two possible values.

We might not see these stories in a schema definition.
Think of SQL, where we might see a column ``APPROVED BIT(1) NULL``.
There's rarely any explanation of when the ``APPROVED`` field is allowed to be ``NULL``.
The nuances of how the attribute is used live in the code, not the schema.

Also, this is clearly not actually "binary": it has three values: ``b'0'``, ``b'1'``, and ``NULL``.
It also has metadata about the value (e.g., not applicable, invalid, or pending.)

Python Implementation
---------------------

How can we handle metadata in Python?

A.  Use a simple ``bool | None`` type and put the metadata processing details and rules in the code.

B.  Define an **Adapter** to carry both the value and the metadata.

Here's an example using an **Adapter**.
In this example, we'll us a "Not Applicable" rule as an example
of a meta condition for an attribute.

::

    from dataclasses import dataclass

    @dataclass
    class Approved:
        value: bool | None
        applicable: bool = True

    @dataclass
    class Something:
        approved: Approved

Here's how we might see this used:

::

    s = Something(
        approved=Approved(None, applicable=False)
    )

    assert s.approved.value is None
    assert not s.approved.applicable

This adds some complexity, but it can be a useful way to carry details in a form
that's more public than a simple ``bool | None`` type annotation.
It can also be clutter where the metadata storyline is simple and obvious.

May Not Be Binary
=================

In some cases, a domain of values is *discovered*, not defined by policy (or regulations.)

For example, we might be doing analysis of source data with some measurement value and a
condition. We'll use a temperature and a scale; the scale appears to be binary: "C" or "F".

As a small variant, sometimes the attribute is stateful.
This is a small consideration, and we'll set it aside for later.

We'll start with an attribute that has a domain that we don't really know.
There are two common reasons for this:

-   The source data is evolving, and we may discover subsequent data that doesn't match prior data.

-   We've only seen a subset of source data, and we may discover a value of the domain which wasn't present in the initial subset.

The distinction between these two is insignificant from a Python programming perspective.
(Organizationally, it may suggest different parts of the organization should perhaps be in closer contact.)

Here's a flawed design in Python.

::

    from dataclasses import dataclass

    @dataclass
    class Sample:
        temperature: float
        scale: bool  # True means "C"; False means "F".

This is risky.  Don't do this.

When a ``Sample`` value arrives with the scale value of ``"K"``, this data model collapses into a wreckage of faulty assumptions.

The scale value seemed like it might have been binary.
Without a complete survey of all data, we may discover an attribute domain wasn't actually binary.

Python Methods for Anticipating Change
--------------------------------------

When the domain of values is not well-known, or otherwise likely to change,
we can use an ``Enum``.

::

    from dataclasses import dataclass
    from enum import Enum

    class Scale(Enum):
        C = "C"
        F = "F"

    @dataclass
    class Sample:
        temperature: float
        scale: Scale

This works well; changes are isolate to the ``Scale`` enumeration of values.
If we discover new values in the source data, we can revise the ``Scale`` enumeration of values.

Above, we mentioned that a stateful attribute may have some additional considerations.
An attribute which changes during processing can be implemented with a simple ``Enum``.
However, sometimes an alternative implementation is required.

A Stateful Binary
=================

Stateful attributes -- and the associated state change -- may require additional care.
We can use an ``Enum``, and a state change is a simple assignment statement.

::

    sample_x.scale = Scale.F

This has the advantage of being simple.

It has the disadvantage of being difficult to observe.
Assignment statements can be used anywhere, and it can be difficult to be sure that **all** changes are known to developers and maintainers (and users.)

To promote observability, we want to encapsulate state changes with method that can make the change
visible. Perhaps it writes a log entry.

Here's the **Enumeration-by-Method** design we might do to make state changes visible.

::

    from logging import Logger
    from typing import ClassVar

    class Scale:
        value: str
        logger: ClassVar[Logger] = logging.getLogger("Scale")

        def __init__(self, source: str) -> None:
            self.set_value(source)

        def set_C(self) -> Self:
            self.value = "C"
            self.logger.info("Scale set to C")
            return self

        def set_F(self) -> Self:
            self.value = "F"
            self.logger.info("Scale set to F")
            return self

        def set_value(self, source: str) -> Self:
            if source == "C":
                return self.set_C()
            elif source == "F":
                return self.set_F()
            else:
                self.logger.error("Invalid scale setting %r", source)
                raise ValueError(f"invalid {source!r}")

This means a state change looks like this:

::

    sample_x.scale.set_f()

While we gained observability, we sacrificed the bare-bones simplicity of an ``Enum`` class.

Actually Binary
===============

Some attributes are clearly the result of a binary evaluation.
For example, we might have a "is below zero" flag.
This is, manifestly ``True`` or ``False``, and can be modeled with a simple ``bool`` field.

::

    from dataclasses import dataclass

    @dataclass
    class Sample:
        temperature: float
        scale: str
        is_below_zero: bool

        def __post_init__(self):
            assert self.is_below_zero == temperature < 0.0, "consistency error"

In some cases, a boolean attribute may be independent of other values.

In this example, however, the ``is_below_zero`` attribute is dependent on the ``temperature`` attribute.
Database designers call this a "3rd Normal Form" (3NF) problem, a field is dependent on other non-key fields.
The consequences of the 3NF problem don't have any real impact on the way we implement this in Python.
The field is boolean: it's not outside of objective reality, nor is it subject to some change through a discovery process.
It is, however, dependent on another field, and we can't be **sure** the source application set it properly.

A Warning
====================

Don't combine **Enumeration-by-Method** class design with an ``Enum``.
This is a bad idea.

::

    class ScaleDomain(Enum):
        F = "F"
        C = "C"

    class Scale:
        def __init__(self, value: ScaleDomain) -> None:
            self.value = value

        def set_F(self) -> Self:
            self.value = ScaleDomain.F

        def set_C(self) -> Self:
            self.value = ScaleDomain.C

You were warned.

The domain of values is stated twice:

-   The ``ScaleDomain`` lists a set of values.

-   The ``Scale`` class definitions has methods that imply a set of values.

These two must be kept in strict alignment.
This doesn't encapsulate the domain well.
It breaks the "Single Responsibility" S. O. L. I. D. design principle.

(Full disclosure. I did this recently. Don't follow my example.)

I've been struggling to create an accurate emulation of
the #RetroComputing IBM 1620.
(See `Hard Problem? Shift Position <{filename}/blog/2026/09/2026-09-20_hard_problem_shift_position.rst>`_,
and `Hard Problem? Stop Staring At The Code <{filename}/blog/2026/09/2026-09-25_hard_problem_stop_staring.rst>`_,
and `Hard Problem? Use Test Cases as Debug Aids <{filename}/blog/2026/10/2026-10-10_hard_problem_test_as_debug.rst>`_.)

I was deeply suspicious that the definition of a "lamp" wasn't actually binary.
Maybe it involved some state other than "on" or "off".
Maybe "flashing" or something.

It took a few weeks to realize the domain was actually binary.
It was a proper boolean.
There were no other methods.

Wrapping an ``Enum`` with another adapter class created a layer of indirection that made debugging painful.
