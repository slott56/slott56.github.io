Hard Problem? Try Shifting Position
################################################

:date: 2026-09-30 13:32
:tags: codebyhand,ibm1620,retrocomputing
:slug: 2026-09-30_hard_problem_shift_position
:category: Architecture & Design
:status: published

BLUF
====

Can't get the software to work?

Rewrite it.

Seriously.

It's often faster to pick a new paradigm and start a rewrite than to bang your head against a wall.

Modern languages (like Python) don't require a **lot** of overhead or boilerplate to start again.

Can't get the object model right? Try rewriting as a functional program.
The insight gained will help retool the object design.

Can't work out a functional decomposition?
Try replacing pure functions with stateful callable objects.
This often reveals where a monad can help.
And in the Python case, maybe a really simply monad-like data class will help.

A Detailed Example
===================

I've been struggling to create an accurate emulation of
the #RetroComputing IBM 1620.

It's not a particularly good machine. (The PDP-8 is much better.)

It's **simple**. Making it a potentially good vehicle for talking about machine-language programming.
Without getting tangled up up the creeping collection of confusing contraptions that characterize
a lot of modern CPU's.

Also. It's **decimal**.  We can set the binary-to-decimal-to-hexadecimal stuff aside.

However.

The documentation is ancient and brain-scrambling.

The object model is not obvious, and had become difficult to debug.
It's not useless, but the encapsulation is also potentially unhelpful.
First, I'll give some back story on the problem.
Then, in `What Went Wrong?`_, below, I'll reveal the shift in perspective.

First. Background.

IBM 1620 Emulation
------------------

Specifically, addition.

It turns out add, subtract, and compare are nearly identical operations.
The 1620 would apply a 10's complement transformation, :math:`C(x)`, to make :math:`p - q` into :math:`p + C(q)`.
Depending on the sign and the carry-out, it might also recomplement the result.
Subtraction was addition with a complemented value.

Compare was subtract (which is add with a 10's complement) that sets the status latches, but doesn't update memory with a result.

Multiplication involved a product computation for each pair of digits; these were then summed.
Multiply depended on addition.

Division involved repetitive subtraction. (Yes, it was slow.)

The other operations are trivial.
Addition is the central feature of the CPU.

So?
===

What's so hard about getting addition to work?
It's a Finite State Automaton (FSA). Duh.

Here's some state transition diagrams.
Figure 13-3 to 13-7 in https://archive.org/details/bitsavers_ibm1620fe2stomerEngineeringManualofInstructionAug6_9837978.

The document is packed with brain-cramping details of moving data from memory to the Memory Data Register and to the Digit-Branch register where the True-Complement Switch might complement or complement + 1 or something something the digits. Depending on the triggers.

It **seems** like a Finite State Automaton (FSA) with a **lot** of states.
It -- however -- isn't really.
For example, figure 5-2 shows the complexities of the numerous state changes within the the clock cycle to support something as superficially simple as reading a digit from memory.
(Magnetic core memory read is destructive; the core must be rewritten after a read.
This level of detail is unhelpful, but carefully described. In bewildering detail.)

What this **means** is the diagrams commingle things which happen concurrently.
It's a simple box of circuit boards, after all.
And things which are happening sequentially because they're on different steps of the clock cycle.
There's a hidden little annotations like "R5-D6" to show how the clock's 10 different internal states were used to make somethings happen sequentially.

In spite of this,
the analysis of how addition works using Triggers 11, 12, 13, 14 **is** potentially helpful.

-   Trigger 11: Fetch a digit from P.
-   Trigger 12: Fetch a digit from Q.
-   Trigger 13: Compute a decimal sum and carry based on carry-in and complement processing.
-   Trigger 14: Write the sum to memory.

This kind of functional description reveals a useful level of detail about the **Instructions**, **Memory Access**, **Registers**, **Triggers**, and the overall concept of **Machine State**.
It shows how the CPU really worked without too many layers of abstraction.

(Triggers are also called Latches. More recently, we've taken to calling them flip-flops or status bits.)

The front-panel display (in Single-Cycle Execute mode) showed each of the tiggers as a little lamp.
The labels for triggers 11 to 14 are E11, E12, E13, E14.
The "E" prefix means they're part of the "execute" phase of the "fetch-execute" cycle.
(The fetch triggers used an "I" prefix because they did instruction decode.)

On the real hardware, you could see the lamp for the current trigger(s), and the register lamps for the Digit/Branch and Memory Data registers.
This let you see **exactly** what the state was and what the state change would be.
This would update the triggers, registers, and memory.

Exactly. Explicitly clear.

What Went Wrong?
================

The hardware of a CPU is an FSA.
More complicated than the minimal Turing Machine that serves to define "computability."
We can model an FSA using a class definition for each state.
Makes sense, right?

However.

However.

Stick closely to what follows.

Trigger 11 isn't a "state" of the processor.
It's a single bit out of maybe 64 or so triggers plus a bunch of registers.
With potentially 64 distinct triggers, there could be :math:`2^{64} = 10^{19}` states.
A bit much for a trivial mapping from IBM 1620 triggers to states of a FSA.

Some triggers **are** exclusive, like triggers 11, 12, 13, and 14.
Only one of these is on at a time.
The union of these triggers is 4 states, not 16.

Other triggers are not exclusive.
For example, the ``carry in``, ``true/complement``, ``field mk. 1``, ``field mk. 2``,
``recomp control``, and ``recomplement`` triggers have :math:`2^6 = 64` possible states.

While not **impossible**, it's difficult to work out **all** the combinations
of these triggers to derive tidy state definitions.
The narrative functional descriptions don't have a  particularly useful focus.
The hardware wiring diagrams in the appendix might have this focus.
(I'm not able to make sense of them, though.)

We arrived here: **the triggers described so elegantly in the documentation do not map to tidy blocks of code.**

The functional descriptions **almost** look like they could be code.
They almost look like FSA state definitions.

::

    class Function(abc.ABC)
        @abstractmethod
        def cycle(self) -> None: ...

    class E11(Function):
        def cycle(self) -> None: ...
            #  1. Read out of memory per OR-1 and store the digit in D/B register units.
            MAR.digits = OR_1.digits
            MEMORY.read()
            DIGIT_BRANCH[1] = MDR[0]

            # 2. Decrement OR-1.
            OR_1.digits = MAR.digits

            # 3. Field Mark 1 ON **if** **not** first cycle **and** flag
            if not TRIGGER['1st CYCLE'] and DIGIT_BRANCH[1].flag:
                TRIGGER["FIELD MK 1"].on()

            # etc.

The idea here is the globals, ``MAR``, ``MEMORY``, ``DIGIT_BRANCH``, ``OR_1``,
are all part of the console display.

(Yes, yes, yes, all those globals...
The underlying documentation treats all of the Triggers, Latches, Registers, Switches, etc. as global.
There's [almost] no logical partitioning in the documentation.
This makes the implementation hard to encapsulate properly until after it works with a bunch of unit tests.
Lacking any rational basis for making them local to something, they're global.)

What's the Other Position?
================================

In this case, the other position I adopted was to make two changes:

1.  Unwind the clever ``Register``, ``Memory``, and ``Trigger`` class definitions
    (with their clever observability design to update the console display when they changed.)

    Replace these with dumb-old lists and dictionaries.

2.  Unwind the class definitions.

::


    while True:
        if trigger_11:
            # E11, 1 & 2
            digit_branch, or_1 = q[or_1], or_1 - 1  # Decrement mode
            # E11, 3
            if or_1 == -1:  # Check the flag on the leading digit.
                field_mk_1 = True
            # etc...
        elif trigger_12:
            # do other stuff...
        elif trigger_13:
            ...
        elif trigger_14:
            ...

This tends to "flatten" all the processing into one ``while`` statement.
(140 or so lines of code. Not **bad**.)

What's the benefit?

This gave me a new perspective where the various bits of code are closer together.
The tiny overhead of ``class`` and ``def`` for methods is stripped away, putting a few more details into a single screen of code.

It's not a major rewrite.
It's a rethinking.
It's woefully incomplete with respect to the features an application needs to have.
It has no console implementation with the array of blinkenlights.

Rewriting from a new perspective exposed some sources of confusion.
One example is functional step 7 of trigger 12.
The contents of the Digit/Branch register are replaced by the contents of the Memory Data Register during a recomplement operation.

It was documented. It was easy to ignore.
Until things didn't work.

Sprawled out in "encapsulated" class definitions, the lack of an update to the D/B register wasn't obvious.

Mushed together, (with a lot of ``print()`` functions) it was more clear.

Next Steps
==========

First. Rejoice at having gotten mixed sign add and recomplement to work.

There are still a number of examples from the original reference manuals to canonize into unit tests.

There aren't too many edge cases.
Many of us learned them in 4th or 5th grade math when signed numbers were introduced.

Then.

And this is the important part.

Using the massive ``while`` statement to refactor the original code -- a collection of class definitions -- so it works.
Given a baseline of ugly code that works, I can then refactor it into less ugly code that still works.


