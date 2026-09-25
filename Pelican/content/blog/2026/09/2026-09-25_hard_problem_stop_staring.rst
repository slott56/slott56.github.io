Hard Problem? Stop Staring At The Code
################################################

:date: 2026-09-25 09:32
:tags: codebyhand,ibm1620,retrocomputing
:slug: 2026-09-25_hard_problem_stop_staring
:category: Architecture & Design
:status: published

BLUF
====

Can't get the software to work?

Stop Staring At It.

Often, there are two problems:

-   The code doesn't work.

-   You're making faulty assumptions about why it doesn't work.

It's essential to stop staring (and hand-wringing) over the code and **gather evidence.**

This will allow you to challenge your faulty assumptions.

..  sidebar::

    I had the misfortune for working with someone who was blind to their own assumptions.

    They made evidence-free assertions.

    When I asked for evidence they blustered and make random (often contradictory) noises for a dismayingly long time.

    Eventually (a few times they only stopped when I accused them of lying) they would resort to claiming
    these were "auto-assumptions": something so obvious it couldn't be false, and
    didn't count as an assumption because it was -- like gravity -- universally true.

    Except in these cases where they couldn't provide evidence.

    They would never self-challenge their assumptions.  **Never.**
    It had to get heated with me (repeatedly) asking for evidence.
    The need to gather tangible evidence was -- to them -- a whim of mine, not a rational process for assessing the facts.

The Detailed Example
====================

I've been struggling to create an accurate emulation of
the #RetroComputing IBM 1620.

(See `Hard Problem? Shift Position <{filename}/blog/2026/09/2026-09-20_hard_problem_shift_position.rst>`_.)

The IBM1620 is not a particularly good machine. (The PDP-8 is much better.)

The IBM1620 is **simple**. Making it a potentially good vehicle for talking about machine-language programming.
Without getting tangled up up the creeping collection of confusing contraptions that characterize
a lot of modern CPU's.

Also. It's **decimal**.  We can set the binary-to-decimal-to-hexadecimal stuff aside.

Test Cases
===========

I got the examples from the reference manuals to work. Big yay!

This meant I needed to add yet more examples.

For 2-digit, signed numbers, there are 4,000 pairs.
(Superficially, it seems like -99 to 00 to +99 is only 199 two-digit values, 39,601 examples.
Actually, there's signed zeroes -- -00 and +00 -- so, it's a proper 200 values.)

Testing **all** of them is (in a way) dumb, since most of the cases are simply redundant.
There are 8 conditions in the sign analysis table in figure 13-6 of the documentation.
Detailed *Boundary Value Analysis* could create as many as 40 cases targeting "below minimum", "at minimum", "middle", "at maximum", "above maximum" sums.

My lazy approach is to use 3-digit values like 998, 3, -3, and -998.
This has a number of overflows, and tricky sign rules.

This revealed adding ``-003 + 998`` did not produce ``995``.

Details Matter
==============

I spent some time improving the output log.

And improving it again.

I needed to match the code against the processing rules spread over 9 pages.

Here's the strategy:

-   **Not** staring at the code.

-   Stare at the output from the ``print()`` functions throughout the code.

Here's the outline of how the processing cycle is implemented:

::

    while trigger:
        match trigger:
            case trg_11:
                # Q-digit stuff
                trigger_next = trg_12
            case trg_12:
                # P-digit stuff and sign analysis
                trigger_next = trg_13
            # etc.
        pprint(locals())
        trigger = trigger_next

Yes. I printed **all** the local variables.  ``pprint(locals())`` exposes everything.
It forces renaming variables so they are located near each other.
It forces creating intermediate variables to expose complex computations.

This let me stop staring at the code (which was my design, with my faulty assumptions)
and look at the **effect** of the code.

Victory-ish Outcome
===================

Eventually, I uncovered a subtle recomplement condition.

Unit tests still failed.

What I did **not** do (for hours) was actually look at the test case failure.

- **Initially**.  The incorrect result was -006. A nuanced recomplement problem.

    I found and fixed the recomplement problem.

    There was still a unit test error.

    **I did not know I fixed this bug.**

    I actually had a second problem.

- **Finally**.  The incorrect result was -995.  A simple failure to set the sign correctly.

    Scrolling around randomly, I noticed the failed assertion was different than it was initially.

    Big sigh. I **assumed** the test case failure reason had not changed.

Next Steps
==========

First. Rejoice at having gotten mixed sign add and recomplement to **work**.

Next. Investigate 3 subtract issues: all :math:`-P - -Q` computations.
Two of these have a final machine state issue: the High/Plus trigger logic is wrong.
One of these is a 10's complement vs. 9's complement nuance: the answer is off by 1; this may be related to the :math:`-3 + 998` problem.

