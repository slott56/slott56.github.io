Python Roadmap Amplifications and Clarifications
================================================

:date: 2013-06-11 08:00
:tags: #python
:slug: 2013_06_11-python_roadmap_amplifications_and_clarifications
:category: Technologies
:status: published

Some additional points on using Python 2.7 in a way that bridges the gap
to Python 3.2. The steps are small and simple. You can start taking them
now.

Recently I suggested that one should always include ``from __future__ import division, print_function`` on every module. **Always**. Every
Module.

I also suggested using ``input=raw_input`` in those few scripts where input
might be expected. This  isn't the best idea, but it forces you to
depend on the semantics of the Python 3 ``input()`` function.

I failed to mention that you must stop using the **%** operator for
string formatting. This operator will be removed from Python 3.2. Start
using "".format() string formatting right now. **Always**. Every Module.

A follow-up question was "What the heck is ``from __future__``?"

The Python ``__future__`` package contains proposed language changes.
There are a number of modules. Of those, two are highly relevant to
easing the switch to 3.2.

**Division**.

The division module changes the semantics of division. The "/" operator
becomes "exact" division instead of "depends on the arguments" division.
In Python2.7, do

::

    >>> 22/7
    >>> 22/7.0

To see the "depends on the arguments" (or classical) mode.

Then try

::

    >>> from \__future_\_ import division
    >>> 22/7

This is the exact division operation that's used in Python 3.
For integer division, the "//" operator is used.

::

    >>> 22//7

Start now. Use them like this.

**Print Function**.

The print_function module actually changes the Python compiler to reject
the **print** statement as a syntax error. This allows you to use the
(less quirky) print() function.

In Python 3, the **print** statement has been removed.  It's easiest to
simply get out of the habit of using the **print** statement by
switching to the print() function as soon as possible.

This means that examples from older books will have to be translated.

::

    print "hello world"

becomes

::

    print("hello world")

Not too significant a change, really.

In some later chapters, they may introduce print >> somefile, data,
data.

The "chevron print". This syntax was a HUGE blunder, and is one of the
reasons for eliminating the **print** statement and replacing it with
the print() function. The print function equivalent is print( data,
data, file=somefile ). Much more regular; much less quirky.







