Functional Python and Lambdas
=============================

:date: 2024-02-09 08:01
:tags: python,functional programming,functional python programming
:slug: 2024-02-09-functional_python_and_lambdas
:category: Python
:status: published

I saw a confusing post on https://fosstodon.org.

I won't link to it, but I will quote it because it repeats some common misconceptions.

::

    I have some iterator chain (in reality longer and more complex than this example).
    And now in one or more steps, I need to add an extra operator.
    Going from `foo.map(thing).filter(condition).reduce(collector)` to

    foo.map({
      thing
      if condition {
          other_thing
      }
    ).reduce({
      setup
      collector
      logger
    })

    The design of Python's iterators make this very hard.

    Because a lambda cannot easily contain multiple lines, conditions or statements.

There are two unrelated misconceptions here. One's an minor error, the other is a nuanced design choice.
We'll look at the minor error first, since it's a common misconception about Python lambdas.

And. I cover these in `Functional Python Programming <https://www.amazon.com/Functional-Python-Programming-functional-expressive/dp/1803232579>`_

Lambda and Lines of Code
------------------------

A Python lambda has a single **expression**. This precludes any statements.

An expression must be complete on a single **logical line** of code.
Because of the way ``(`` and ``)`` must balance, it can span multiple **physical lines** of code.

::

    a = list(
        map(
            lambda x: (
                (
                    3 * x + 1
                )
                if
                (
                    x % 2 == 1
                )
                else
                (
                    x // 2
                )
            ),
            range(10)
        )
    )

A lambda can be quite long. Use ``(`` and ``)`` to enclose it.

Design Choices
--------------

The Ruby ``foo.map(m).filter(f).reduce(r)`` has two renderings in Python.

-   Nested functions. This is bad, but we'll look at it.

-   Chains of generator expressions. I call them stacks. This is good.

Let's take a concrete example, one that we can unit test.
We'll look at it first as nested functions to see how bad it can be.

Nested Functions
----------------

Here's are two functions to generate some complicated data.

::

    hotpo = (
        lambda x:
            (x * 3 + 1) if (x % 2 == 1)
            else (x // 2)
    )
    hotpo_run = (
        lambda x, r:
            r + [x] if x == 1
            else hotpo_run(hotpo(x), r + [x])
    )

These are two functions that we've defined as lambdas for no particularly good reason.

Let's use a mapping to compute a range of values.
This is a bit like ``range(1, 11).map(lambda...)`` in Ruby.

::

    list(
        map(
            lambda n: hotpo_run(n, []),
            range(1, 11)
        )
    )

We don't want the lists. We want the lengths of the lists.

::

    list(
        map(len,
            map(
                lambda n: hotpo_run(n, []),
                range(1, 11)
            )
        )
    )

Not that it matters much, but let's add a filter.

::

    list(
        filter(
            lambda x: x > 0,
            map(len,
                map(
                    lambda n: hotpo_run(n, []),
                    range(1, 11)
                )
            )
        )
    )

..  note::

    BTW, the answer is ``[1, 2, 8, 3, 6, 9, 17, 4, 20, 7]``.

    Without a cache of some kind. It takes quite a while to compute more than a few results.

Let's reduce this to find the largest value.

Clearly ``max()`` will work, but, for the sake of matching the Ruby,
let's build ``max()`` as a ``reduce()``.

::

    from functools import reduce
    reduce(
        lambda a, b: a if a > b else b,
        filter(
            lambda x: x > 0,
            map(len,
                map(
                    lambda n: hotpo_run(n, []),
                    range(1, 11)
                )
            )
        )
    )

The answer is 20. What's important is the function-application version of the Ruby.

..  code-block:: ruby

    foo.map(m).filter(f).reduce(r)

..  code-block:: python

    reduce(r, filter(f, map(m, source)))


Folks don't like reading the Python right-to-left.
When you spread it into multiple lines it has to be read from bottom-to-top.
Or maybe from inside to outside.
This nested function version is not widely used.

We can do better with a stack of generator expressions.

Stacked Generators
------------------

We'll start with the original two lambdas, ``hotpo()`` and ``hotpo_run()``.

::

    runs = map(
            lambda n: hotpo_run(n, []),
            range(1, 11)
        )
    lengths = map(len, runs)
    positive = filter(lambda x: x > 0, lengths)
    maximum = reduce(
        lambda a, b: a if a > b else b,
        positive
    )

This reads from start to finish in an understandable fashion.

We can easily add steps in the middle of this.

The downside of adding steps is the intermediate results have names.

When we want to insert a step, we have to **also** modify the step after to
use the new intermediate results.

The upside is the intermediate results have names. These describe
what's going on. I really like this approach.

Hey, Wait
---------

Yes, this is related to the Collatz Conjecture.
See https://projecteuler.net/problem=14.

The definition of the ``hotpo_run()`` function isn't conducive to creating a cache.
We can rewrite it, easily, into a function that builds a list from a single argument value.
This works better with a cache.

::

    from functools import cache
    hotpo_run = cache(
        lambda x: [1] if x == 1 else [x] + hotpo_run(hotpo(x))
    )

This necessitates a change to the pipeline to deal with the slightly different parameter
signature for the ``hotpo_run()`` function.

::

    runs = map(
            hotpo_run,
            range(1, 11)
        )

The rest is the same. Second verse same as the first verse.

::

    lengths = map(len, runs)
    positive = filter(lambda x: x > 0, lengths)
    maximum = reduce(
        lambda a, b: a if a > b else b,
        positive
    )

This computes almost instantly.

What's important is the sequence of ``map()``-``filter()``-``reduce()`` functional operations
is better expressed as a sequence of generator expression statements.
I like to call it the "Stack of Generators" design pattern.
It has much of the expressive power of Ruby, with all of the flexibility we desire.

..  note::

    And yes, that's still not a solution to Euler 14.

    Euler 14 wants this: "Which starting number, under one million, produces the longest chain?".

    We need to change the result of the ``runs`` generator to be a (run, starting value) two-tuple.

    ::

        runs = ((hotpo_run(n), n) for n in range(1, 11))

    Or

    ::

        runs = map(lambda n: (hotpo_run(n), n), range(1, 11))

    The ``lengths`` generator needs to be modified to be ``lambda r_s: (len(r_s[0]), r_s[1])``.

    Drop the ``filter()``. It's only here to match the original conversation.

    Replace the ``reduce()`` with a simpler ``max()``.
