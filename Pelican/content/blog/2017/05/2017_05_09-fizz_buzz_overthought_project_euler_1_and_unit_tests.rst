Fizz Buzz Overthought, Project Euler #1, and Unit Tests
=======================================================

:date: 2017-05-09 08:00
:tags: functional python programming,#python
:slug: 2017_05_09-fizz_buzz_overthought_project_euler_1_and_unit_tests
:category: Technologies
:status: published


This. http://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/

And many other thoughts on overthinking fizz buzz. I'm going to
overthink it, also. Why not?

This is a problem where the obvious unit test may not cover the cases
properly. See https://projecteuler.net/problem=1 for a unit test case
with a subtle misdirection built in. I love this problem statement
deeply because the happy path is incomplete.

Part of my overthinking is overthinking this as a "classification"
exercise, where we have simple classifiers that we can apply as
functions of an input value. A higher-level function (i.e., map or a
generator expression) applies all of these functions to the input.
Some match. Some don't.

It shakes out like this.

The core classifier is a function that requires flexible parameter
binding.

::

   query = lambda n, t: lambda x: t if x%n == 0 else None


This is a two-step function definition. The outer function binds in
two parameters, n, and t. The result of this binding is the inner
function. If an argument value is a multiplier of n, return the text,
t. We can think of the result of the outer lambda as a partial
function, also, with some parameters defined, but not all.

We have two concrete results of this query() function:


::

    fizz = query(3, 'fizz')
    buzz = query(5, 'buzz')

We've bound in a number and some text. Here's how the resulting
functions work.

::

    >>> fizz(3)
    'fizz'
    >>> fizz(2)


The "trick" in the fizz buzz problem space is recognizing that
we're working with the power set of these two rules. There are
actually four separate conditions. This is remarkably easy to get
wrong even though the sample code may pass a unit test like the
Project Euler #1 sample data.

Here's the power set that contains the complete set of all subsets
of the rules.

::

    rule_groups = set(powerset([fizz, buzz]))

"Um," you say, "Is that necessary? And powerset() isn't built-in."

Try to add a third or fourth rule and the :math:`\textbf{O}(2^n)`
growth in complexity of checking all combinations of the rules
will become readily apparent. For two rules,
:math:`4 = \lvert\mathcal{P}(\{q(3), q(5)\})\rvert`.

For a general set
of rules, :math:`r`, it's :math:`2^{\lvert r \rvert} = \lvert \mathcal{P}(r)\rvert`.

Four rules? sixteen outcomes. It sure
seems like the power set is absolutely necessary; it describes the
domain of possible outcomes. How could it not be necessary?
Also. There's a nice definition of powerset in the ``itertools``
recipes section of the standard library. It's \*almost\*
built-in.

The domain of possible responses form a power set. However, it's
also clear that we aren't **obligated** to actually enumerate that
set for each value we're testing. We do need to be aware that the
complexity of the classification output is :math:`\textbf{O}(2^n)`
where :math:`n` is the number of rules.
The processing to build each set of classifications, however, is
:math:`\textbf{O}(n)`. Here's how it looks.

::

         for n in range(20):
             m = set(filter(None, (r(n) for r in [fizz, buzz])))
             print(m if m else n)

This locates the set of all matches, m. We apply the rules, fizz()
and buzz(), to the given value. The result of applying the rules
is filtered to remove falsy values. The resulting set, m, has the
values from all rules which matched. This will be one of the sets
from the power set of applying the rules to each value. The match,
:math:`m`, is an element of :math:`\mathcal{P} (\{q(3), q(5)\})`.

I'm delighted that Python has some support for creating partial
functions in a variety of ways. When things are complex, we can
use the **def** statement. We can use functools ``partial()``. When
things are simple, we can even use lambdas.





