Analyzing a Dice Mechanic
===============================================

:date: 2023-09-14 14:57
:tags: python,games,tutorial
:slug: 2023-09-14-analyzing_a_dice_mechanic
:category: Python
:status: published

A "Dice Mechanic"? Yes. The thing you do with the dice to determine an outcome.
We'll use Python to see how the dice shake out.

A little backstory
------------------

For a casino game of craps, the roll of the dice can be 7 or 11 for an immediate win,
2, 3, or 12 for an immediate loss, and the other numbers establish a point.
You continue to roll until you get your point or a 7. That's a mechanic.
Kind of complicated -- by design.

Many Table-Top Role-Playing Games (TTRPG) include game mechanics that involve dice.
The original D&D used the Platonic regular polyhedra. They were summarized as "d6"
for the 6-sided die folks often think of. The term "3d8" was interpreted as "3 eight-sided dice."

It, of course, gets more complicated "3d6+1" is add one to three six-sided dice.

And, there are things like "4d6-low" to discard the lowest of 4 dice.
Or maybe "ll4d6" for "lose lowest". Clever people have worked out a lot of mechanics,
and a lot of ways to describe them.

The mechanics in question
-------------------------

We want to compare two mechanics:

1. Worst of 2d6. This tends to have a lot of low numbers.

2. Middle of 3d6. This -- well -- does it tend to favor low numbers, also?

We could -- if we had a big brain -- work out the odds.  But we don't have a big brain.

Another really good alternative is to exhaustively enumerate the possible outcomes.
With 3d6 there are only :math:`6^3 = 216` ways the dice can fall. This doesn't seem
pleasant. We'll set it aside.

Instead, we'll simulate.

..  sidebar::

    This isn't as dumb as it might sound.

    Some of the foundational statistical tests are designed to discern of outcomes
    are random or not. The "Null Hypothesis" is that the data's random.
    The various tests for the null hypothesis are often difficult to understand,
    and involve tables of magical numbers. The :math:`\chi^2` test involves a
    complicated computation to compare actual and expected and then you have to look
    up a number in a table.

    In some cases, it's easier to create random data and compute the correlation between
    actual and random. High correlation? Accept the Null Hypothesis.

We'll start by building a simulation of each mechanic.

Worst of 2d6
------------

Here's the code to roll a handful of dice.

::

    from random import randint

    def nd6(n: int) -> list[int]:
        return [randint(1, 6) for _ in range(n)]

The ``nd6(2)`` expression gives us a pair of dice as a tiny little list.

::

    def worst(dice: list[int]) -> int:
        return min(dice)

The ``worst(some_dice)`` expression returns the worst of the two values.
If we were more clever, we might write something like.

::

    def worst(dice: list[int]) -> int:
        d_1, d_2 = dice
        return d_1 if d_1 <= d_2 else d_2

Which would be faster when it runs.
But this is a lot more coding.
Efficiency isn't the goal.
We're comparing two dice mechanics.

Finally, this will apply the ``worst()`` decision to ``nd6(2)`` to
capture the worst numbers.

::

    from collections.abc import Iterator

    def worst_2d6(samples=1000) -> Iterator[int]:
        yield from (
            worst(nd6(2)) for _ in range(samples)
        )

This function is a kind of generator. It doesn't simply compute a value the way
the ``nd6()`` or ``worst()`` functions did. This will yield a result
each time it's asked for something. It iterates over a sequence of ``worst(nd6(2))`` values.

(The ``range(samples)`` defines how long the sequence will be.)

The point of the generator is to avoid producing a giant list with a thousand values
when all we're going to do is summarize the list into a small result.

Here's the summary.

::

    from collections import Counter

    distro_worst_2d6 = Counter(worst_2d6())

We'll create a ``Counter`` object from the values generated when evaluating the ``worst(nd6(2))`` expression 1,000 times.

Here's the result:

..  csv-table::
    :header: n, count

    1, 304
    2, 242
    3, 202
    4, 132
    5, 84
    6, 36

That fits our expectation, more-or-less.

And it wasn't too hard to create.

Let's look at the other mechanic.

Middle of 3d6
--------------

We're going to reuse the ``nd6()`` function. It works delightfully well for 3 dice as well as 2 dice.

Here's an approach to picking the middle value.

::

    def mid(dice: list[int]) -> int:
        return sorted(dice)[1]

We've sorted the three dice, and taken the one in position 1.
Position 0 has the least, and position 2 has the most.
In the middle is the target value.

We can optimize this, of course.

::

    d_0, d_1, d_2 = dice
    return (
        d_0 if d_1 <= d_0 <= d_2 else
        d_1 if d_0 <= d_1 <= d_2 else
        d_2
    )

Who needs that kind of optimization? Not me.

Here's a generator to provide the needed 1,000 samples.

::

    def mid_3d6(samples=1000):
        yield from (
            mid(nd6(3)) for _ in range(samples)
        )

It's really similar to the ``worst_2d6()`` function. And, yes, the two could be refactored to eliminate a tiny blot of redundant code. And, no, I won't spend a lot of time on that optimization.
(I wrote a whole book on Functional Python Programming.)

Here's the distribution:

::

    distro_mid_3d6 = Counter(mid_3d6())

What's it look like? This.

..  csv-table::
    :header: n, count

    1, 72
    2, 192
    3, 245
    4, 226
    5, 185
    6, 80

Seriously? It's weighted toward 3's and 4's?

That shouldn't be too surprising. Maybe it is.

I had no idea.

So Far, So Good
---------------

The point is to compare dice mechanics.

The strategy is to simulate them.

We wrote some functions to apply the mechanic.

We sampled it 1,000 times to create a ``Counter`` with the distribution of the 1,000 samples.

And now, you can decide if that's acceptable for the game you're designing.

Or, you can press on and do a little more math.

But wait, there's more
-----------------------

The worst-of-2d6 isn't too difficult to compute on paper.

When will the lowest value be 6? This requires a (6, 6) tie, :math:`P(6) = \frac{1}{36}`.

It's a 5 when there's a (5, 5), (5, 6), or (6, 5)) pair. :math:`P(5) = \frac{3}{36}`.

It's a 4 when there's any of (4, 4), (4, 5), (4, 6), (5, 4), or (6, 4). :math:`P(4) = \frac{5}{36}`.

And so on for 3, 2, and 1.  :math:`P(n) = \frac{2(6-n)+1}{36}`.

We can create prediction from this essential probability theory.

::

    for n in range(6):
        print(n+1, int(1000 * (2*(5-n)+1) / 36))

The predicted distribution is this.

..  csv-table::
    :header: n, count

    1, 305
    2, 250
    3, 194
    4, 138
    5, 83
    6, 27

That looks pretty close to the random simulation. It was more work to do the theory
than to simulate. That's why I started with the simulation.

This part is to convince any doubters that simulation gives useful results.

We'll continue to flog that point.

Middle of 3d6 Theory
---------------------

This exceeds my skills.

When will the median value be 6? This requires a (6, 6, 6) tie. Actually, it's a lot more than that. Anything with a pair of 6's means 6 will be the mid value. There are :math:`\frac{15}{216}` ways to have a pair of sixes and another number. Think of (1, 6, 6) to (5, 6, 6), and (6, 1, 6) to (6, 5, 6), and (6, 6, 1) to (6, 6, 5). So, total, is :math:`P(6) = \frac{16}{6^3}`.

For 5's? Ugh. I can't enumerate them manually. So. I'll use ``itertools`` to emit all :math:`6^3 = 216` combinations.

This isn't quite the same as simulation. The simulation *probably* hit all the combinations.
The ``itertools`` approach will absolutely create all of the combinations.

Here's the central part of enumerating all combinations:

::

    import itertools

    d6 = [n+1 for n in range(6)]
    for c in itertools.product(d6, d6, d6):
        # do something with c

The ``itertools.product()`` will enumerate all 3-item combinations of the values in the ``d6`` sequence.

Here it is in context.

::

    import itertools
    from collections import defaultdict

    d6 = [n+1 for n in range(6)]
    mid_3d6 = defaultdict(list)
    for c in itertools.product(d6, d6, d6):
        mid_3d6[mid(c)].append(c)
    for k in sorted(mid_3d6):
        print(k, len(mid_3d6[k]), [''.join(map(str, v)) for v in mid_3d6[k]])

We created a ``defaultdict`` object, a dictionary that will -- if a key is not found -- jam in a an empty ``list``. When we evaluate  ``mid_3d6[mid(c)]`` it will either

-   find a list in the dictionary, because this value of ``mid(c)`` has been seen before, OR

-   jam a new empty list into the dictionary, because the value has not been seen before.

Either way, ``mid_3d6[mid(c)]`` is a list, and we can ``append(c)`` to put another combination into that list. Why save them?

So we can display the count and all the patterns.

::

    6 16 ['166', '266', '366', '466', '566', '616', '626', '636', '646', '656', '661', '662', '663', '664', '665', '666']

A 6 is the middle value :math:`\tfrac{16}{216}` times. And there are the 16 patterns, to make it perfectly clear what's going on.

The sequence of 16-40-52-52-40-16 looks a lot like it is part of the binomial function.
Looking at the text patterns, I can work out the following.

-   :math:`P(6) = P(1) = \frac{1 + 3 \times 5}{6^3}`

-   :math:`P(5) = P(2) = \frac{1 + 3 \times 5 + 6 \times 4}{6^3}`

-   :math:`P(4) = P(3) = \frac{1 + 3 \times 5 + 6 \times 4 + 4 \times 3}{6^3}`

Beyond this, I'm lost.

But.

Simulation showed me the way forward, and it wasn't much code.
