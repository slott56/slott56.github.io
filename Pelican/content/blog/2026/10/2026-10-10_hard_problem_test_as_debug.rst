Hard Problem? Use Test Cases as Debug Aids
################################################

:date: 2026-10-10 12:28
:tags: codebyhand,ibm1620,retrocomputing
:slug: 2026-10-10_hard_problem_test_as_debug
:category: Architecture & Design
:status: published


BLUF
====

Can't get the software to work?

The test cases are places to gather debugging details.
Some simple tricks:

- Observability: add debugging outputs to the code

- Enable debugging output in failing test cases

- **Make Failure an Option**


The Detailed Example
====================

I've been struggling to create an accurate emulation of
the #RetroComputing IBM 1620.

(See `Hard Problem? Shift Position <{filename}/blog/2026/09/2026-09-20_hard_problem_shift_position.rst>`_, and `Hard Problem? Stop Staring At The Code <{filename}/blog/2026/09/2026-09-25_hard_problem_stop_staring.rst>`_.)

The IBM 1620 has a number of peculiar features.
See `EWD37 <https://www.cs.utexas.edu/~EWD/transcriptions/EWD00xx/EWD37.html>`_ for a scathing analysis of the problems with this processor's design.
But, it's really simple, and works in decimal.

What's Broken
=============

I've got something that doesn't work.
Paired with a different implementation that does work.
I need to know what's different.

In one hand, I've got a proper Finite-State Automaton (FSA) that should reflect functional features of the CPU.
It doesn't work.

In the other hand, I've got a hackerish ``while-if`` big-ball-o-mud monster that **does** work.
It works really, really well, passing hundreds of unit tests.

Some Details
================

Skip this, if you're not interested in #retrocomputing and want to get to the #Python.

I'm working with the functional summaries of how the 1620 really worked.
And they're sometimes incomplete (and in one case, inaccurate.)

The IBM 1620 CPU has 64 (or so) "triggers" (or "latches", which might be more widely known as "flip-flops"), 15 registers of various sizes, and a 10-step clock cycle that controlled the details of the state changes.
A "functional" state included an illuminated a console lamp, and had as many internal changes as could be crammed into the clock cycle.

For example, the **Trigger 11** illuminated the ``E11`` lamp, updated the Digit/Branch register with a digit from memory,
and updated the OR-1 register with the next lower address in memory.
And set or cleared Field Mark 1, True/Complement, and the Carry Out latches.

The machine used magnetic core memory, and a read was destructive. It required a following write to make it idempotent, sucking up clock cycles in the kind of overhead that's really unhelpful to know anything about. Forget I mentioned the idea that reading from memory erased what was there.

One version works.
The other version is fatally broken.

Step 1 -- Observability
=======================

The first thing was to improve observability into both versions.

The FSA is designed so each state **is** highly observable.
The "functional" state class sets console lamps (in addition to doing internal state changes.)
The triggers and registers have logging to record state changes as well as display the final state an operator would see on the console.

The big-ball-o-mud monster? We need to expose **why** it works.
Merely knowing it's correct isn't quite as useful as it might seem.

Here's what to do:

1.  Add a locals dump.

    ::

        if _DETAILS == 2:
            pprint(
                {
                    name: value
                    for name, value in locals().items()
                    if not name.startswith("_")
                },
                width=156
            )

    This goes at the bottom of the ``while`` loop to dump the locals.
    It elides hidden variables, to reduce clutter somewhat.

    Also, this **forces** sensible naming conventions to make possible to understand the locals.
    The most important part of the name is first, clustering functionally-related variables together.
    Which tends to provide copious hints for class designs to encapsulate functionally-related items into a sensible state definition.

2.  Add an "Important State" dump.

    ::

        if _DETAILS:
            print(f"\n# 34-41: {multiplier_digit}×{multiplicand_digit}={''.join(map(str, memory.values()))}\n")

    A few of these were scattered around to display a summary of the processing so far.
    This provided context for the detail dumps above and below.

Step 2 -- In Test Cases
=======================

We don't want the output from **everything**.
We want output for selected test cases.
We're comparing the same test case for two implementations.

1.  Set the ``_DETAILS`` to ``2`` for selected test cases.
    This is done with ``monkeypatch.setattr(ibm1620.algorithms, '_DETAILS', 2)`` in the tests where debugging details are helpful.

2.  The tricky bit: saving the detailed logs for specific (failing) test cases.
    The goal is to have two parallel logs so we can compare what worked with what didn't work:

    -   ``bug_algo.log`` with the (working) big-ball-o-mud dumps of local variables.

    -   ``bug_final.log`` produced by the (not working) FSA's using the ordinary logging that's available from a tidy, well-designed bit of OO programming.

    The problem is that **pytest** won't capture much output from a test that passes.

We have two contexts for running the test suite:

A.  Does everything work?  A simple Yes/No will do nicely, thank you.

B.  Why does something work?

    Which is really a question of what test case ``test_s_page_71`` produces as output when it works.
    Normally, **pytest** doesn't save output from tests that pass.
    Capturing the debugging details requires a test to fail.

Make Failure an Option.

Step 3 -- Forced Failure
========================

The "normal" mode of testing is to run the tests to see what passes.
We can see the captured output from the failing tests, and use it to debug the problem.
This is an elegant feature of **pytest**.

The "side-by-side" mode of testing is to run tests with two implementations, capturing the output to compare them.
We're going to introduce a ``--debugfail`` flag into our **pytest** environment so failure can be an option.

Here's a recipe from my Makefile:

..  code-block:: make

    bug_logs:
        - pytest -v --show-capture all ibm1620/algorithms.py -k test_s_page_71 --debugfail >bug_algo.log
        pytest ibm1620/test_fcn_ibm1620_1_hw.py -k test_s_page_71 >bug_final.log

The ``algorithms.py`` works. It has the algorithm code, plus test cases for the algorithm code.
A big-ball-o-mud. We want to run ``test_s_page_71`` in ``--debugfail`` mode.

The ``test_fcn_ibm1620_1_hw.py`` is test cases for the FSA implementation.
We also want to run ``test_s_page_71``. Nothing extra is needed here, it's going to fail.
In fact, that's the point: It's failing.

We want to compare the outputs to see what's different between the implementations.

Adding an Option to pytest
--------------------------

We can add an option to **pytest** that's part of our test regime.
We do it with a single file, ``conftest.py`` located near the ``pyproject.toml`` for the project as a whole.

::

    def pytest_addoption(parser):
        parser.addoption(
            "--debugfail",
            action="store_true",
            help="Force a failure to capture debugging details"
        )

This is all that's neeed.

The command-line option information is available in the ``request`` fixture that can be used by a test case.

Adding Optional Behavior to a Test
--------------------------------------

Here's how a test case looks:

..  code-block:: python
    :linenos:

    def test_s_page_71(request, monkeypatch):
        """From A26-5706-3 page 71
        P 185 - Q 52 = 133.
        """
        monkeypatch.setattr(ibm1620.algorithms, '_DETAILS', 2 if request.config.getoption("--debugfail") else 0)
        p = Number(Sign.POS, [1, 8, 5])
        q = Number(Sign.POS, [5, 2])
        state, result = sub(p, q)
        assert state.High_Plus
        assert not state.Equal_Zero
        assert not state.Arith_Check
        assert result == Number(Sign.POS, [1, 3, 3])
        if request.config.getoption("--debugfail"):
            assert False, "Force capture of details"

Note the two modifications to the test.

-   **5**.
    A ``monkeypatch`` to set the ``_DETAILS`` level for this test case.

-   **13-14**.
    The "force failure" assertion that will be used when we want to capture the details to examine why this one worked.

It seems like the force-failure **might** be doable with more clever hook functions, but I have my doubts.
Someone smarter than me may have an approach that hides the detail.
I'm eager to see it.


What Have We Got Here?
----------------------

Now, the Makefile snippet will create two parallel logs.
We can side-by-side them to see what's different.

The log from the working big-ball-o-mud is a sequence of ``pprint()`` requests to dump a subset of ``locals()``.
It's ugly, but, detailed.

The log from the failing FSA is proper logging messages and console state dumps.
It's much easier on the eyes.

And The Bug?
------------

More #retrocomputing -- skip this, there's no #Python here.

I think there's a small error in the description of the Carry-Out trigger.
It says "2. Reset OFF by Triggers 11, 21, and 23.", but I don't think it should be
turned off by trigger 21.

I had taken it out of the big-ball-o-mud version, but left it in the FSA implementation of trigger 21.
Fixed. Tests pass.

And. I learned a cool thing about using my unit tests as debugging tools.
