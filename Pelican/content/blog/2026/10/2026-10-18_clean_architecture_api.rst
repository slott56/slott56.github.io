Clean Architecture API Lesson Learned
#######################################

:date: 2026-10-18 07:41
:tags: object-oriented design,clean architecture,api,solid
:slug: 2026-10-18_clean_architecture_api
:category: Architecture & Design
:status: draft


BLUF
====

Clean Architecture means implementation choices can be revoked.

Ignore the "Dependency Inversion" part of the **SOLID** design principles at your peril.

Think through at least one alternative design and make sure the API covers more than one data structure.

(Full disclosure. I failed to do this recently. Don't follow my example.)

I've been struggling to create an accurate emulation of
the #RetroComputing IBM 1620.
(See `Hard Problem? Shift Position <{filename}/blog/2026/09/2026-09-20_hard_problem_shift_position.rst>`_,
and `Hard Problem? Stop Staring At The Code <{filename}/blog/2026/09/2026-09-25_hard_problem_stop_staring.rst>`_,
and `Hard Problem? Use Test Cases as Debug Aids <{filename}/blog/2026/10/2026-10-10_hard_problem_test_as_debug.rst>`_.)

The Sad Story: When Life Looks Like Easy Street...
===================================================

Here's a problem that was painful to fix.

::

    from enum import Enum

    class Trigger(Enum):
        OFF = 0
        ON = 1

    class TriggerState:
        def __init__(self, value: ScaleDomain) -> None:
            self.value = value

        def set_on(self) -> None:
            self.value = Trigger.ON

        def set_off(self) -> None:
            self.value = Trigger.OFF

        def invert(self) -> None:
            self.value = trigger.OFF if self.value.value else Trigger.ON

        def is_on(self) -> bool:
            return self.value.value

    triggers: dict[str, TriggerState] = {}

What's wrong with this?

It turns out -- after a painful experience -- changning the type of ``triggers`` is painful.

Why?

Glad you asked.

There is Danger At Your Door
============================

Consider the code to set a trigger on:

::

    triggers["I/O HOLD"].on()

Seems pretty plain: triggers are on or off or (sometimes) they're inverted.

This works out well for making changes observable.
For debugging purposes, the ``TriggerState.on()``, ``TriggerState.off()``, and ``TriggerState.invert()`` methods can log state changes.
This reduces the toil of working out what part of the source documentation is incomplete because a state change was omitted.
It also makes it possible to locate inconsistencies.

The Hidden Cost
---------------

Something as superficially simple as ``triggers["H/P"].invert()`` involved
dictionary operations, as well as ``TriggerState`` operations, as well as ``Trigger`` operations.
It's a lot of software overhead to model something quite simple.

(It was a digital circuit with a handful of transistors.)

Pragmatically, this is more appropriate:

::

    triggers: set[str] = set()

A trigger is on when it's in the set.
It's off when it's not in the set.

This, however, has a different API.


Barely Time to Wait
============================

Consider the code to set a trigger on:

::

    triggers.add("I/O HOLD")

Less overhead.
But.
Nothing at all like the dictionary implementation.

This requires hundreds of changes to the base application.
And -- bonus -- hundreds of changes to the unit test suite.
The number of broken tests was staggering.
A huge pile of work to correct the problems from the API change.

The SOLID design principle for Dependency Injection had been broken.
What should we have done?

You Know All the Rules By Now
=============================

Always imagine new underlying data structures.
In this case, we **should** have considered the possibility
of a ``dict`` vs. ``set`` change.

Considering this possibility means avoiding a ``dict``-specific design.
We can refactor the state changes out of ``TriggerState`` and put them
into the collection.

It would look like this:

::

    class TriggerDict(TriggerCollection):
        def __init__(self) -> None:
            self.values: dict[str, Trigger] = {}

        def on(self, name: str) -> None:
            self.values[name].on()

        def off(self, name: str) -> None:
            self.values[name].off()

        def invert(self, name: str) -> None:
            self.values[name].invert()

There's no ``TriggerState`` intermediate.

Here's the set-based alternative.

::

    class TriggerDict(TriggerCollection):
        def __init__(self) -> None:
            self.values: set[str] = set()

        def on(self, name: str) -> None:
            self.values.add(name)

        def off(self, name: str) -> None:
            self.values.discard(name)

        def invert(self, name: str) -> None:
            if name in self.values:
                self.off(name)
            else:
                self.on(name)

An underlying design **concept** is to have an abstract base class.
Pragmatically, we don't really need the ABC in Python.
We can work with the concrete subclass until we need to make a change.

For completeness, here's the ABC we don't really need:

::

    class TriggerCollection:
        def on(self, name: str) -> None:
            ...
        def off(self, name: str) -> None:
            ...
        def invert(self, name: str) -> None:
            ...

The alternative **without** the ABC means a slight simplification
to the two classes.

::

    class TriggerDict:  # Remove ``(TriggerCollection)``
        ...
    class TiggerSet:
        ...

    type TriggerCollection = TriggerDict | TriggerSet

At some point, we might even delete the high-overhead dict-based implementation.
It seems unlikely that this would ever actually be useful in practice.
