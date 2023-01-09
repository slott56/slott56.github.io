The Old Days -- ca. 2000 -- Empirical Tests of Random Numbers (Python and Chi-Square Testing)
=============================================================================================

:date: 2022-01-11 08:00
:tags: #python,fortran,random numbers
:slug: 2022_01_11-the_old_days_ca_2000_empirical_tests_of_random_numbers_python_and_chi_square_testing
:category: Technologies
:status: published

See `The Old Days -- ca. 1974 Random Numbers Before
Python <{filename}/blog/2021/12/2021_12_28-the_old_old_days_ca_1968.rst>`__
for some background.

We'll get to Python after reminiscing about the olden days. I want to
provide some back story on why
`sympy <https://docs.sympy.org/latest/index.html>`__ has had a huge
impact on ordinary hacks like myself.

What we're talking about is how we struggled with randomness before

#. ``/dev/random``
#. The Mersenne Twister Pseudo-Random Number Generator (PRNG)

Pre-1997, we performed empirical tests of PRNG's to find one that was
random enough for our application. Maybe we were doing random samples of
data to compare statistical measures. Maybe we were writing a game. What
was important was a way to create a sequence of values that passed a
battery of statistical tests.

See https://link.springer.com/chapter/10.1007%2F978-1-4612-1690-2_7 for
the kind of material we salivated over.

While there are an infinite number of bad algorithms, some math reveals
that the Linear Congruential Generator (LCG) is simple and effective.
Each new number is based on the previous number:
:math:`X_{n+1} = (X_n \times a + c) \bmod m`. There's a multiply and an add, modulo some
big number. The actual samples are often a subset of the bits in
:math:`X_{n}`.

After the Mersenne Twister became widely used, we essentially stopped
looking at alternative random number algorithms. Before then -- well --
things weren't so good.

Here are some classics that I tested.

-  The ACM Collected Algorithms (CALGO) number 294 is a random-number
   generator. This is so obsolete, I have trouble finding links to it.
   It was a 28-bit generator.
-  The ACM Collected Algorithms (CALGO) number 266 has code still
   available. See `toms/266 <http://www.netlib.no/netlib/toms/266>`__.
-  The Cheney-Kincaid generator is available. See `random.f plus
   dependencies <https://www.netlib.org/cgi-bin/netlibfiles.pl?filename=/cheney-kincaid/random.f>`__.

These formed a kind of benchmark I used when looking at Python's
built-in Mersenne Twister.

Nowadays, you can find a great list of LCM PRNG's at
 https://en.wikipedia.org/wiki/Linear_congruential_generator.

Python Empirical Testing
------------------------

One of the early questions I had was whether or not the ``random``
module in Python stacked up against these older RNG's that I was a
little more familiar with.

So, I wrote a big, fancy random number testing tool in Python.

When? Around 2000. I started this in the Python 1.6 and 2.1 era. I have
files showing results from Python 2.3 (#2, Jul 30 2003). This is about
when I stopped fooling around with this and moved on to trusting that
Python really did work and was -- perhaps -- the best approach to
working with randomly-sampled data for statistical work.

The OO design for the test classes was Lavish Over The Top (LOTT™) OO:

-  Too Many Methods
-  Too Many Superclasses
-  No Duck Typing

We won't look at that code. It's regrettable and stems from trying to
make Python into C++.

What I do want to look at is the essential Chi-Squared test methodology.
This is some cool stuff.

Comparing Expected and Actual
-----------------------------

The chi-squared metric is a way to compare actual and expected
distributions. You can read about it on your own time. It's a way to
establish if data is random or there's something else going on that's
not random. i.e., a trend or a bias.

The empirical tests for PRNG's that Knuth defines all come with
chi-squared values that bracket acceptable levels of randomness. For the
purposes of writing a working set of tests the magic chi-squared values
supplied by Knuth are fine. Magical. But fine. Really. Trust them.

If you make modifications, you'd use your statistics text-book. You'd
open to the back where it had a Chi-Squared table. That table gave you
chi-squared values for a given degree of freedom and a given probability
of being random.

Or, You could look for the NIST handbook online. It has a section on
chi-squared testing.
See https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm.
Same drill. Degrees of freedom and probability map to a chi-squared
threshold.

But.

Were do these magical Chi-Squared values come from? This gets
interesting in a useless-sidebar kind of way.

Chi-Squared Values
------------------

There's a really, really terse summary of chi-squared numbers
here: https://www.danielsoper.com/statcalc/formulas.aspx?id=11. This is
all you need to know. It may be too terse to help you learn about it,
but it's a handy reference.

We need to evaluate two functions: partial gamma and gamma. These are
defined as integrals. And they're nasty levels of complexity. Nasty.

This kind of nasty:

..  math::

    \gamma (s,z)=\int_{0}^{z}t^{s-1} e^{-t} dt

..  math::

    \Gamma (z)=\int_{0}^{\infty} t^{z-1} e^{-t} dt

These are not easy things to evaluate. Back to the ACM Collected
Algorithms (CALGO) to find ways to evaluate these integrals. There are
algorithms in CALGO 435 and 654 that are expressed as Fortran for
evaluating these. This ain't all, of course, we need Stirling Numbers
and Bernoulli Numbers. So there's a lot going on here.

A lot of this can be transliterated from Fortran. The resulting code is
frankly quite ugly, and requires extensive test cases. Fortran with
GOTO's requires some cleverness to unwind the conceptual for/while/if
constructs.

OR.

Enter Sympy
-----------

In the 20+ years since I implemented my empirical PRNG tests "the hard
way," ``sympy`` has come of age.

Check this out

::

   from sympy import Sum, rf
   from sympy.abc import k, s, z
   from sympy.functions import exp
   from sympy import oo
   Sum(z**s * exp(-z) * z**k / rf(s, k+1), (k, 0, oo)).simplify()

I could use this in Jupyter Lab to display a computation for the partial
gamma function.

.. math::

    z^{s}e^{-z}\sum_{k=0}^{\infty }{\dfrac {z^{k}}{s^{\overline {k+1}}}}

This requires a fancy Rising Factorial computation,
the :math:`s^{\overline {k+1}}` term. This is available in ``sympy`` as the ``rf(s, k+1)``
expression.

It turns out that sympy offers lowergamma() and gamm() as first-class
functions. I don't even need to work through the closed-form
simplifications.

I could do this...

::

   def gammap(s: float, z: float) -> float:
       return (z**s * exp(-z) * Sum(z**k / rf(s, k+1), (k, 0, oo))).evalf()

   def gamma(z: float) -> float:
       return integrate(t**(z-1) * exp(-t), (t, 0, oo)).doit()

It works well. And it provides elegant documentation. But I don't need
to. I can write this, instead,

::

   def chi2P(chi2: float, degF: int) -> float:
      return lowergamma(degF/2, chi2/2) / gamma(degF/2)

This is used to compute the probability of seeing a chi-squared value.

For the frequency test, as an example. We partition the random numbers
into 16 bins. These gives us 15 degrees of freedom. We want chi-squared
values between 7.2578125 and 25.0.

Or.

Given a chi-squared value of 6.0, we can say the probability of 0.02 is
suspiciously low, less than 0.05 level that we've decided signifies
mostly random. The data is "too random"; that is to say it's too close
to the ideal distribution to be trusted.

The established practice was to lookup a chi-squared value because you
couldn't easily compute the probability of that value. With sympy, we
can compute the probability. It's slow, so we have to optimize this
carefully and not compute probabilities more frequently than necessary.

We can, for example, compute chi-squared values for a number of seeds,
take the max and min of these and compute the probability of those two
boundary values. This will bracket the probability that the pseudo
random number generator is producing suitably random numbers.

This also applies to any process we're measuring with results that might
vary randomly or might indicate a consistent problem that requires
evaluation.

Using ``sympy`` eliminates the complexity of understanding these
beautifully hand-crafted antique algorithms. It acts as a kind of
super-compiler. From Math to an intermediate AST to a concrete
implementation.





