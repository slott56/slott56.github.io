Dice Mechanics: Equal Probability Outcomes from D6
==================================================

:status: hidden
:category: TTRPG
:tags: dice,mechanic


We want to make equal-probability choices using six-sided die. This
means we start with a random value(s) in the domain
:math:`D = \{1, 2, 3, 4, 5, 6\}`. We want to map the dice to values in
some outcome domain :math:`R`.

We’ll write :math:`\lvert R \rvert = 5` to mean there are 5 outcomes.
This implies :math:`R = \{1, 2, 3, 4, 5\}`.

Using D6 is easy for making choices between 2, 3, and 6 items. We’ll
beat these to death explicitly to introduce a little notation that can
help with more complicated mechanics.

We can also note the overlaps between D6 and using polyhedral die with
4, 6, 8, 10, 12 or 20 faces.

:math:`\lvert R \rvert = 2`, tossing a coin.
--------------------------------------------

To choose between two outcomes, we have two mechanics. One of these is
really easy to explain, the other appears contrived to most folks.

-  High-Low. :math:`R = \lfloor\frac{D-1}{3}\rfloor + 1`, which we can
   also write as
   :math:`R = 1 \textbf{ if } D \in \{1, 2, 3\}; 2 \textbf{ if } D \in \{4, 5, 6\}`.
   We’ll abbreviate this further to
   :math:`\bigwedge_D [\{1, 2, 3\}, \{4, 5, 6\}]`, relying on the order
   of subsets to provide the resulting value. The expression
   :math:`\bigwedge_D [S_0, S_1, ..., S_{n-1}]` defines :math:`n`
   subsets of the domain of :math:`D`. The resulting value is the subset
   number that contains :math:`D`\ ’s value.
-  Even-Odd. :math:`D-1 \pmod 2 + 1`, which we can also write as
   :math:`\bigwedge_D [\{2, 4, 6\}, \{1, 3, 5\}]`.

The :math:`\bigwedge_D [\{1, 2, 3\}, \{4, 5, 6\}]` seems easier to
communicate to players as a way to toss a coin with a D6. The idea of
lower 3 *vs.* upper 3 seems slightly more clear than the even-odd rule.

Especially if we write in something lass mathy. Maybe "D6 [1-3, 4-6]".

:math:`\lvert R \rvert = 3`
---------------------------

To choose between three outcomes, we also have two mechanics, one
simpler to explain than the other.

-  Low-Mid-High. :math:`R = \lfloor\frac{D-1}{2}\rfloor + 1`. Or
   :math:`\bigwedge_D [\{1, 2\}, \{3, 4\}, \{5, 6\}]`.
-  Mod 3. :math:`D-1 \pmod 3 + 1`. Or
   :math:`\bigwedge_D [\{3, 6\}, \{1, 5\}, \{2, 4\}]`.

The idea of lower 2 *vs.* middle 2 *vs.* upper 2 seems clear. The
modulo-3 rule is not as clear.

:math:`\lvert R \rvert = 4`
---------------------------

This is where things become a bit more complicated.

We have two mechanics to handle choosing among 4 outcomes.

-  One roll, of 2D.
-  Potential re-rolls using 1D.

The re-roll mechanic is pretty easy to explain.

==== =======
Die  Outcome
==== =======
1-4  D
5, 6 Reroll
==== =======

The other choice uses 2D and a computation.

1. Roll 2 die: :math:`D_2`, :math:`D_1`.
2. Map each die to a result using the :math:`\lvert R \rvert=2` rule:
   :math:`R_2=\bigwedge_{D_2} [\{1, 2, 3\}, \{4, 5, 6\}]`,
   :math:`R_1=\bigwedge_{D_1} [\{1, 2, 3\}, \{4, 5, 6\}]`.
3. The subscript is the weight. :math:`R_2` has a weight of :math:`2`.
   Compute :math:`R = R_2\times 2 + R_1\times 1`. Or
   :math:`\sum R_x\times x`.

We might explain this in the rules with:

   Use two different-colored die, perhaps white and green. Assign a
   weight of 1 to the white die, and a weight of 2 to the green one.
   Roll. Discard all dice that show 1-3. Keep the remaining dice. Sum
   the weights based on the colors. No dice is a sum of 0. The white is
   1. The green is 2. Both white and green is 3. Add one so the result
   is in the range 1-4.

This isn’t too onerous, and it provides equal probability results in a
single roll of two dice.

It provides a precise mapping from D6 to D4.

:math:`\lvert R \rvert=5`
-------------------------

As with :math:`\lvert R \rvert=4`, we have two mechanics: single roll of
of using 4D or re-roll using 1D. The re-roll version is clear: Use 1D
and reroll any 6’s to keep the range in 1 to 5.

The single roll alternative uses 4D.

===== =======
Total Outcome
===== =======
4-10  1
11-12 2
13-14 3
15-16 4
17-24 5
===== =======

The worst-case discrepancy between these outcomes and a 5-sided die is
about 4.1%.

:math:`\lvert R \rvert=6`
-------------------------

Doesn’t bear belaboring.

:math:`\lvert R \rvert=7`
-------------------------

As with 5, there are two mechanics:

-  Re-roll using the :math:`\lvert R \rvert=8` outcomes (shown next),
   re-rolling on a result of 8 to keep the results in the range 1-7.
-  For a single-roll, use 5D.

===== =======
Total Outcome
===== =======
5-12  1
13-14 2
15-16 3
17-17 4
18-19 5
20-21 6
22-30 7
===== =======

The worst-case discrepancy between these outcomes and a 7-sided die is
about 5.2%.

:math:`\lvert R \rvert=8`
-------------------------

For this we have two mechanics: a 3D computation, or a 4D table.

Similar to :math:`\lvert R \rvert=4`, we can do a computation. In this
case, it’s 3D with distinct colors and dice weights of 1, 2, and 4. We
can think of this as using a white, green, and red die. Roll all three,
discard all dice showing 1-3. Add the weights for the dice which remain:
1 for the white die, 2 for the green die, and 4 for the red die.

This approach provides a precise mapping from D6 to D8.

The alternative is to roll 4D table.

===== =======
Total Outcome
===== =======
4-9   1
10-11 2
12-12 3
13-13 4
14-14 5
15-15 6
16-17 7
18-24 8
===== =======

The actual distribution has a number of places where it differs by about
5.2% from the expected distribution. It’s difficult to do better without
rolling 9D.

:math:`\lvert R \rvert=9`
-------------------------

We can leverage the :math:`\lvert R \rvert=3` rules using 2D.

1. Roll 2 die: :math:`D_3`, :math:`D_1`.
2. Map each die to a result using the :math:`\lvert R \rvert=3` rule:
   :math:`R_3=\bigwedge_{D_3} [\{1, 2\}, \{3, 4\}, \{5, 6\}]`,
   :math:`R_1=\bigwedge_{D_1} [\{1, 2\}, \{3, 4\}, \{5, 6\}]`.
3. The subscript is the weight. :math:`R_3` has a weight of :math:`3`.
   Compute :math:`R = R_3\times 3 + R_1\times 1 + 1`. Or
   :math:`\sum R_x\times x + 1`.

In English:

    Use two distinctly colored die: say white and green.
    The green die as a weight of 3. The white die has a weight of one.

    We’ll transform each die’s value into the range 0, 1, 2, and then multiply by the weight.
    This means 3 times the green die’s value (0, 1 or 2) plus the white die’s value (0, 1, or 2) plus 1 more to make a number from 1 to 9.

This isn’t quite as simple as using :math:`\lvert R \rvert=2` rule,
where we can keep or discard dice. We’re stuck with adding and
multiplying to compute nine different values.

=== === =======
D_3 D_1 Outcome
=== === =======
1-2 1-2 1
\   3-4 2
\   5-6 3
3-4 1-2 4
\   3-4 5
\   5-6 6
5-6 1-2 7
\   3-4 8
\   5-6 9
=== === =======

This is precisely the result of a 9-sided die.

Or. We can roll 5D and use this table.

===== =======
Total Outcome
===== =======
5-12  1
13-14 2
15-15 3
16-16 4
17-17 5
18-18 6
19-19 7
20-21 8
22-30 9
===== =======

This has a maximum discrepancy of 4.2% from an ideal 9-sided die.

:math:`\lvert R \rvert = 10`
----------------------------

We have three mechanics to choose among 10 possible outcomes.

-  Use :math:`\lvert R \rvert = 12` outcomes and reroll on 11 or 12 to
   keep the result to the range 1 to 10.
-  Use :math:`\lvert R \rvert = 5` outcomes combined with
   :math:`\lvert R \rvert = 2` outcomes. This is 4D and one more
   distinctly-colored die. The 4D provides 5 values from 0 to 4. When
   the odd die is 1-3, discard it. Otherwise it has a weight of 5,
   pushing the 4D values from 5 to 9. Then add 1 to make the resulting
   value have a range of 1 to 10.
-  Use a 3D and the following table.

===== =======
Total Outcome
===== =======
3-6   1
7-7   2
8-8   3
9-9   4
10-10 5
11-11 6
12-12 7
13-13 8
14-14 9
15-18 10
===== =======

Interestingly the maximum error is only 3.1% with this.

:math:`\lvert R \rvert = 11`
----------------------------

There are two mechanics for choosing among 11 outcomes:

-  Use :math:`\lvert R \rvert = 12` outcomes and reroll on 12 to keep
   the value between 1 and 11.
-  Use 5D and the following table:

===== =======
Total Outcome
===== =======
5-11  1
12-13 2
14-14 3
15-15 4
16-16 5
17-17 6
18-18 7
19-19 8
20-20 9
21-22 10
23-30 11
===== =======

:math:`\lvert R \rvert = 12`
----------------------------

While 6D and a table of roll ranges and outcomes provides pretty good
results, it seems a lot simpler to use 2D.

One die is used to choose between the lower outcomes (1-6) or the upper
outcomes (7-12). The second die chooses an outcome from the selected
sub-group.

In effect, it decomposes the set of outcomes into two subsets.

This matches the results of a 12-side polyhedral die precisely.

:math:`\lvert R \rvert = 20`
----------------------------

We’ll include 20 choices just to think about a D20 polyhedral die.

-  We can combine :math:`\lvert R \rvert = 5` choices and
   :math:`\lvert R \rvert = 4` choices. This can be a *lot* of die
   rolling.
-  We can use 24 choices with rerolls. This is
   :math:`\lvert R \rvert = 4` choices multiplied 6, to which you’ll add
   an odd-colored die. Values above 20 get a re-roll.

This second choice isn’t too bad: it requires 3 distinctly-colored dice:
red, green, and white. 1. The red and green are used to compute select a
value from the set {0, 6, 12, 18}. The red die picks a subset: {0, 6} or
{12, 18}. The green die picks the final value. 2. The white die is added
to this, to make a number from 1 to 24. 3. Values from 21 to 24 get
re-rolled.

This 3D rule is precisely a D20 roll.

:math:`\lvert R \rvert = 100`
-----------------------------

For total completeness, we can also get 100-sided die outcomes. It’s
unpleasantly complicated.

With 3D – of distinct colors – the following can be done.

1. Roll 3 dice, white, green, red.
2. Use the red die to pick a value from {0, 36, 72}.
3. Multiply the green die by the white die to get a value from 1 to 36.
4. Add to get a value from 1 to 108.
5. Reroll anything over 100.

More pragmatically, most tables using D100 have less than 100 distinct
entries and wonderfully irregular probabilities. In some cases, the D100
probabilities mimic an ``nD6`` distribution. This is because it can be
easier to roll 2D10 than 5D6.

In other cases, the D100-based table can be decomposed into sub-tables,
and a chain of dice rolls can recreate the original probability
distribution.

TL;DR
-----

Here are mechanics for up to 12 choices.

We’ve drawn the line at 12 because any game designer with more than 12
choices can subdivide the choices into multiple, smaller groups. It
helps the players and GM’s to create a chain of smaller choice tables
instead of one too-big-to-understand table of choices.

..  csv-table:: Mechanic Alternatives
    :widths: 1, 10
    :header-rows: 1

    Outcomes,D6 Mechanic
    "2","1D [1-3, 4-6]"
    "3","1D [1-2, 3-4, 5-6]"
    "4","1D with reroll {5, 6}
    or 2D with weights of 2, 1"
    "5","1D with reroll {6}
    or 4D [4-10, 11-12, 13-14, 15-16, 17-24]"
    "6","1D *Do we even need to include this?*"
    "7","Use 8 outcomes with a reroll {7}
    or 5D [5-12, 13-14, 15-16, 17, 18-19, 20-21, 22-30]"
    "8","4D [4-9, 10-11, 12, 13, 14, 15, 16-17, 18-24]
    or 3D with weights of 4, 2, 1"
    "9","5D [5-12, 13-14, 15, 16, 17, 18, 19, 20-21, 22-30]
    or 2D with weights of 3, 1"
    "10","3D [3-6, 7, 8, 9, 10, 11, 12, 13, 14, 15-18]
    or 5 outcomes combined with 2 outcomes"
    "11","Use 12 outcomes with reroll {11}
    or 5D [5-11, 12-13, 14, 15, 16, 17, 18, 19, 20, 21-22, 23-30]"
    "12","Use 6 outcomes, combined with 2 outcomes"
    "above 12","Decompose into 2 or more tables; use a chain of rolls"

Implementation
--------------

This is a fun bit of programming to work out the proper distribution of
values for nD6.

Given a distribution of nD6, we can then divide it up into equal-sized
bins to work out the mapping from the dice distribution to a the desired
uniform distribution.

The distribution is tricky, though.

Multinomial Distribution for dice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have two ways to tackle a distribution of dice.

1. Exhaustive Enumeration of the dice combinations.
2. Direct computation of the results.

Exhaustive enumeration is easy to implement. We can use the
``itertools.product`` function to repeat the values from
:math:`\{1, 2, 3, 4, 5, 6\}` the right number of times.

For 2D, this is
:math:`\{1, 2, 3, 4, 5, 6\} \times \{1, 2, 3, 4, 5, 6\}`. It has
:math:`6^2 = 36` distinct pairs of values. It has 11 distinct sums
between 2 and 12.

For 10D, there are :math:`6^{10} = 60,466,176` distinct 10-tuples of
values, with sums from 10 to 60.

Why would anyone roll 10D to make a fair choice among alternatives?
While it doesn’t seem terribly practical, it seems prudent to at least
explore the possibility.

The problem is that enumerating over 60 million dice alternatives,
computing over 60 million sums, and then accumulating the values into a
``Counter`` object takes a lot of time. It only gets worse for more
dice.

My box of 6-sided die has a dozen dice. :math:`6^{12} = 2,176,782,336`.
Ouch, that’s a lot of combinations.

.. code:: python

    from collections import Counter
    from collections.abc import Iterator
    import itertools
    
    def all_rolls(n: int, k: int = 6) -> Iterator[int]:
        """
        Create *all* alternatives that will define a distribution with n samples of k categories.
        Sum the n-tuples to create totals that range in value between n and n*k.
        """
        yield from (
            sum(x) for x in itertools.product(range(1, k + 1), repeat=n)
        )
    
    def distribution_hard(n: int, k: int=6) -> Counter[int]:
        """Create a counter to summarize """
        return Counter(all_rolls(n, k))

.. code:: python

    sorted(distribution_hard(2).items())




.. parsed-literal::

    [(2, 1),
     (3, 2),
     (4, 3),
     (5, 4),
     (6, 5),
     (7, 6),
     (8, 5),
     (9, 4),
     (10, 3),
     (11, 2),
     (12, 1)]



For direct computation of the distribution of dice, we need a lesson in
multinomials.

See
https://towardsdatascience.com/modelling-the-probability-distributions-of-dice-b6ecf87b24ea/.
From this we learn the following (amongst other things). For :math:`n`
dice of :math:`s` sides (6 in our case), the probability of getting the
target value :math:`T` is this:

.. figure::
   https://towardsdatascience.com/wp-content/uploads/2021/01/1Q48-x74mNLrcyZoxIcOWtA.gif
   :alt: equation GIF

   equation GIF

(Above is the GIF from the original article.)

This is the formula, rewritten here in LaTeX:

:math:`P(n, s, T) = \Bigl(\sum\limits_{k=0}^{\lfloor \frac{T-n}{s} \rfloor}\bigl(-1\bigr)^k \frac{n!}{(n-k)!k!} \frac{(T-sk-1)!}{(T-sk-n)!(n-1)!}\Bigr)\Bigl(\frac{1}{s}\Bigr)^n`

Yes, they’re the same.

We’ll use the following, with two optimizations. First, Python has the
``math.comb()`` function to compute binomials directly. We can leverage
:math:`\frac{n!}{(n-k)!k!} = \binom{n}{k}`. Second, we’ll drop the
:math:`\bigl(\frac{1}{s}\bigr)^n` term because we don’t want a
probability, we want the actual number of combinations of dice with the
given total, :math:`T`.

:math:`P(n, s, T) = \sum\limits_{k=0}^{\lfloor \frac{T-n}{s} \rfloor}\bigl(-1\bigr)^k \binom{n}{k} \binom{T-sk-1}{n-1}`

We can compute the distribution using :math:`P(n, s, T)` instead of
enumerating the product of :math:`n` dice.

Also, as a Python implementation choice, we prefer to have the values of
``n`` and ``s`` last, since these don’t change as frequently as ``T``.
For our purposes, ``s`` has a default value of 6, which is not going to
change for this analysis.

.. code:: python

    from math import comb, factorial
    from functools import cache
    
    @cache
    def dice_prob(T, n, s=6):
        upper = (T - n) // s
        series = (
            (-1 if k % 2 == 1 else 1) * comb(n, k) * comb(T - s * k - 1, n - 1)
            for k in range(0, upper + 1)
        )
        return int(sum(series))
    
    def distribution_2(n, s=6):
        return dict((t, dice_prob(t, n)) for t in range(n, n*6+1))

.. code:: python

    sorted(distribution_2(2).items())




.. parsed-literal::

    [(2, 1),
     (3, 2),
     (4, 3),
     (5, 4),
     (6, 5),
     (7, 6),
     (8, 5),
     (9, 4),
     (10, 3),
     (11, 2),
     (12, 1)]



.. code:: python

    def test_distribution():
        """Takes over 3 minutes 40 seconds to demonstrate the two algorithms produce the same result."""
        for dice in range(2, 13):
            closed_form = distribution_2(dice, 6)
            hard_way = distribution_hard(dice, 6)
            assert closed_form == hard_way, f"mismatch for {dice=} {closed_form=} {hard_way=}"
        print("Identical!")
    
    # test_distribution()

Mechanic Details
~~~~~~~~~~~~~~~~

This data structure records the details of a dice-lookup table mechanic.

The ``Mechanic`` object will contain one or more ``DieRange`` instances.

A ``DieRange`` object lists the dice values from the source distribution
used to create (approximately) equal-sized outcome bins. It also has the
total number of dice combinations for the collection of values. When
summarizing, the ``low`` and ``high`` attribute are important to
summarize the range of values that define the outcome bin.

The ``Mechanic`` object is created with a list of ``DieRange``
instances. These define all the individual outcomes. The match with
ideal bin-sizes isn’t going to be absolutely correct. The ``score`` and
``max_error`` are two ways to evaluate how will the mechanic fits the
ideal.

.. code:: python

    from dataclasses import dataclass, field
    from statistics import mean, variance
    
    @dataclass
    class DieRange:
        map_to: int
        values: list[int] = field(default_factory=list)
        total: int = field(default=0)
    
        @property
        def low(self):
            return min(self.values)
    
        @property
        def high(self):
            return max(self.values)
    
    @dataclass
    class Mechanic:
        result_size: int
        n_dice: int
        total_size: int
        mapping: list[DieRange] = field(default_factory=list)
    
        _actuals: list[float] = field(default_factory=list, init=False)
    
        @property
        def actuals(self):
            if not self._actuals:
                self._actuals = [dr.total / self.total_size for dr in self.mapping]
            return self._actuals
    
        @property
        def total(self):
            return sum(self.mapping)
    
        @property
        def score(self):
            expected = 1 / self.result_size
            return sum(
                (actual - expected)**2
                for actual in self.actuals
            )
    
        @property
        def max_error(self):
            expected = 1 / self.result_size
            errors = (
                actual - expected
                for actual in self.actuals
            )
            return max(errors, key=lambda v: abs(v))

The goal is to produce ``Mechanic`` instances for a given number of
equal-probability outcomes, and a selected number of dice.

We can vary the number of dice for a given number of outcomes, looking
for one that has a minimal error.

.. code:: python

    from collections import defaultdict
    
    def make_mechanic(result_size: int, number_dice: int) -> Mechanic:
        """
        Computes the multinomial distribution for nD6.
        Formally, n samples of k=6 categories.
        Then, breaks the distribution into `result_size` distinct buckets.
        Return a summary of the Mechanic to make it easier to compare alternatives.
    
        :param result_size: number of outcomes
        :param number_dice: number of dice to try and map to outcomes
        :returns: a Mechanic with details of a table to provide (approximately) equal probability outcomes
        """
        distribution = distribution_2(number_dice)
    
        n_tile_width = sum(distribution.values()) / result_size
        # print(f"{n_tile_width:.1f} out of {sum(distribution.values())}")
        rolls = defaultdict(list)
        tile_num = 0
        accum_fq = 0
        for k in sorted(distribution):
            accum_fq = accum_fq + distribution[k]
            if accum_fq >= n_tile_width:
                tile_num += 0 if tile_num == result_size-1 else 1
                accum_fq = accum_fq - n_tile_width
            rolls[tile_num].append(k)
        m = Mechanic(
            result_size, number_dice, sum(distribution.values()),
            [
                DieRange(r, rolls[r], sum(distribution[n] for n in rolls[r]))
                for r in rolls
            ]
        )
        return m

The ``report()`` function explores the alternative space. It creates a
bunch of alternative mechanics, and then ranks them by the ``score``
computation.

In some cases, the best fit also involves a big handful of dice. A
slightly worse fit may involve substantially fewer dice. It’s not a
simple matter of picking the “best” fit; it also has to be reasonably
useful by actual players.

.. code:: python

    def report(outcomes: int = 5, max_dice: int | None = None):
        """
        Locate optimal Mechanics for a given number of outcomes.
        This prints a summary of each mechanic considered.
    
        :param outcomes: Number of distinct, equal-probability outcomes
        :param max_dice: Maximum number of dice to consider, the default is the number of outcomes.
        """
        mechanics = [
            make_mechanic(outcomes, n_dice)
            for n_dice in range(2, max_dice or outcomes+1)
        ]
        for m in sorted(mechanics, key=lambda m: m.score):
            print(f"{m.result_size} choices with {m.n_dice}D")
            print(f"| roll | result | frequency | error |")
            print(f"| ---- | ------ | --------- | ----- |")
            expected = 1 / outcomes
            for dr in m.mapping:
                actual = dr.total / m.total_size
                print(f"| {dr.low}-{dr.high} | {dr.map_to} | {actual:.1%} | {actual - expected:.1%} |")
            print(f"{m.score=:.3f} {m.max_error=:.1%}")
            print()

Let’s use this ``report()`` function to compute a number of different
kinds of equal-probability mechanics.

.. code:: python

    report(5)


.. parsed-literal::

    5 choices with 4D
    | roll | result | frequency | error |
    | ---- | ------ | --------- | ----- |
    | 4-10 | 0 | 15.9% | -4.1% |
    | 11-12 | 1 | 17.7% | -2.3% |
    | 13-14 | 2 | 22.1% | 2.1% |
    | 15-16 | 3 | 20.4% | 0.4% |
    | 17-24 | 4 | 23.9% | 3.9% |
    m.score=0.004 m.max_error=-4.1%
    
    5 choices with 3D
    | roll | result | frequency | error |
    | ---- | ------ | --------- | ----- |
    | 3-7 | 0 | 16.2% | -3.8% |
    | 8-9 | 1 | 21.3% | 1.3% |
    | 10-10 | 2 | 12.5% | -7.5% |
    | 11-12 | 3 | 24.1% | 4.1% |
    | 13-18 | 4 | 25.9% | 5.9% |
    m.score=0.012 m.max_error=-7.5%
    
    5 choices with 5D
    | roll | result | frequency | error |
    | ---- | ------ | --------- | ----- |
    | 5-13 | 0 | 15.2% | -4.8% |
    | 14-16 | 1 | 24.8% | 4.8% |
    | 17-17 | 2 | 10.0% | -10.0% |
    | 18-20 | 3 | 27.9% | 7.9% |
    | 21-30 | 4 | 22.1% | 2.1% |
    m.score=0.021 m.max_error=-10.0%
    
    5 choices with 2D
    | roll | result | frequency | error |
    | ---- | ------ | --------- | ----- |
    | 2-4 | 0 | 16.7% | -3.3% |
    | 5-5 | 1 | 11.1% | -8.9% |
    | 6-7 | 2 | 30.6% | 10.6% |
    | 8-8 | 3 | 13.9% | -6.1% |
    | 9-12 | 4 | 27.8% | 7.8% |
    m.score=0.030 m.max_error=10.6%
    
We'll omit all the other experiments we ran to fill in the `TL;DR`_ table up front.
