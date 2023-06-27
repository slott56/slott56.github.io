any() and all() and Identity Elements
##############################################

:date: 2023-06-27 09:00
:tags: patterns,python,functional-programming
:slug: 2023-06-27-any_and_all_and_identity_elements
:category: Technologies
:status: published

This was a surprising thing (for me) to see.
Surprising because -- after writing a book about functional programming,
I'd forgotten that some of the ideas are actually really new to people.

(I've omitted the source of the quote because I want to reuse this
without worrying about link rot. Some web sites have rocky futures.)

    "
    Python tip:

    Be careful when using all()

    all() returns True for an empty sequence
    "

This seemed to be a surprise to the author. And a large number of people argued -- a few seemed vehement -- that Python is wrong here.

When I pointed out this is the mathematical definition they argued that

1) Programming isn't math. (This is demonstrably false. You may not have wide-ranging math skills, but programming very much is applied math.)

2) The math is wrong. (Also false.)

What is all()?
==============

First. What is ``all(x)``?

In effect it's ``reduce(and, x)``. Except, of course, there's no simple ``and`` operator. So, it's not **exactly** that, but it's close enough.
We'll get to ``reduce()`` in the next setion.

Let's reason by analogy for a while, using `sum()` and `math.prod()`.
These are also ``reduce()`` operations, but they work with numbers, not boolean values.

::

    >>> sum([1,2,3])
    6
    >>> prod([1,2,3])
    6

Okay. Using a perfect number like 6 is a bad example, isn't it?

Here's a better example.

::

    >>> sum([0, 1, 2])
    3
    >>> prod([0, 1, 2])
    0

No surprise, right?

Here is a more fundamental definition of the ``sum()`` function.

::

    >>> from functools import reduce
    >>> from operator import add, mul
    >>> reduce(add, [0, 1, 2])
    3

In effect, ``sum = functools.partial(reduce, add)``.

This works for ``prod = functools.partial(reduce, mul)``.

It would work for ``any()`` and ``all()`` **if** there was a simple operator in the
``operator`` module.

There's an ``and_`` and ``or_`` definition in operator, but these are names for ``&`` and ``|``,
which a bit-tweaking operations, only defined over integer values. They're **not**
the general-purpose, short-circuiting ``and`` and ``or`` operators.

You could create a lambda for this. ``all = functools.partial(reduce, lambda a, b: a and b)``.

All of this depends on the definition of ``reduce()``.

What is reduce()?
==================

The ``reduce()`` function is sometimes described as  a "fold".

When we do ``reduce(add, [1, 2, 3])`` it's essentially ``1 + 2 + 3``.

We've folded the ``+`` operator into the sequence of values.

When we do ``reduce(mul, [1, 2, 3])`` it's a lot like we did ``1 * 2 * 3``.

This folding idea also applies well to ``and`` and ``or``. We can fold logical operators into the sequence of values.

The ``all(x)`` is (conceptually) ``reduce(and, x)`` is ``x[0] and x[1] and x[2]...``.

The ``any(y)`` is (also, in concept) ``reduce(or, y)`` is ``y[0] or y[1] or y[2]...``.

(We have to throw around conceptually, because there's no trivial ``and`` or ``or`` operator.)

So far, so good. This ``reduce()`` hasn't introduced an complications, it's just a way of defining things
around the "fold" idea.

What about empty sequences or iterables?

The Initialization Problem
==========================

Here's the problem with our overly-simplistic use of Python's ``reduce()``.

::

    >>> reduce(add, [])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: reduce() of empty iterable with no initial value
    >>> reduce(mul, [])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: reduce() of empty iterable with no initial value

Failure.

Here are the right answers:

::

    >>> sum([])
    0
    >>> prod([])
    1

The sum of an empty list is zero.

The product of an empty list is 1.

Similarly.

::

    >>> any([])
    False
    >>> all([])
    True

The ``any()`` function is a little bit like a sum. The ``all()`` function is a little bit like
a product.

I think that's why the ``and`` operator has precedence over the ``or`` operator.

Wait, what?
===========

Yes, the value of ``all([])`` is True and the value of the expression ``prod([])`` is 1.

This **must** be true. It's not an implementation choice. It's a matter of definition.

Roll back to the definition of "reduce" as "folding in an operator".
(See `What is reduce()?`_, above.)

``prod([1, 2, 3])`` is ``reduce(mul, [1, 2, 3])`` is ``1 * 2 * 3``.

But ``prod([])`` works and ``reduce(mul, [])`` doesn't work. Something's wrong with ``reduce()``.

This is a problem with the ``reduce()`` function (as we used it above) not quite providing **all** the features required by the ``sum()`` and ``prod()`` functions.

Enter the initial value parameter for ``reduce()``.

::

    >>> reduce(mul, [], 1)
    1

Aha. This fixes the ``reduce()`` problem. It's a little more complicated, but it's now correct.

This means ``reduce(mul, [x, y, z], 1)`` is ``1 * x * y * z``.  The 1 is the multiplicative identity element and does nothing.

This means ``reduce(mul, [x, y, z])`` is ``x * y * z``. The 1 isn't needed because there's a value in the sequence.

And ``reduce(mul, [], 1)`` is ``1``.  The multiplicative identity element is **required** when the sequence is empty.

Consider the Fold
=================

Where are we?

Right.  ``prod([1, 2, 3])`` is ``1 * 1 * 2 * 3``. A multiplicateive identity element is provided.

Therefore, ``prod([])`` is ``1``.

Note the delightful algebraic elegance of the fold definition.

``prod([2, 3, 4])`` == ``prod([2, 3]) * 4`` == ``prod([2]) * 3 * 4`` == ``prod([]) * 2 * 3 * 4``.

This is the reason why ``all([])`` **must** return ``True``.


