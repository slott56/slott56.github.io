How to Test a Random Number Generator
#####################################

:date: 2022-01-18 08:00
:tags: #python,random numbers,multiprocessing
:slug: 2022_01_18-how_to_test_a_random_number_generator
:category: Technologies
:status: published

Nowadays, we don't have the same compelling reasons to test a random
number generator. The intervening decades have seen a lot of fruitful
research. Good algorithms.

Looking back to my 1968 self, however, I still feel a need to work out
the solution to an old problem. See `The Old Days -- ca.
1968 <{filename}/blog/2021/12/2021_12_28-the_old_old_days_ca_1968.rst>`__
for some background on this.

What could I have done on that ancient NCE Fortran -- with four digit
integers -- to create random numbers? Step 1 was to stop using the
middle-squared generator. It doesn't work.

Step 2 is to find a Linear Congruential Generator that works. LCG's have
a (relatively) simple form:

..  math:: X_{n+1} = (X_n \times a + c) \bmod m

In this case, the modulo value, *m*, is 10,000. What's left is step 3:
find *a* and *c* parameters.

To find suitable parameters, we need battery of empirical tests. Most of
them are extensions to the following class:

::

   from collections import Counter
   from typing import Hashable
   from functools import cache

   class Chi2Test:
       """The base class for empirical PRNG tests based on the Chi-2 testing."""
       
       #: The actual distribution, created by ``test()``.
       actual_fq : dict[Hashable, int]
       
       #: The expected distribution, created by ``__init__()``.
       expected_fq: dict[Hashable, int]
       
       #: The lower and upper bound on acceptable chi-squared values.
       expected_chi_2_range: tuple[float, float]
       
       def __init__(self):
           """
           A subclass will override this to call ``super().__init__()`` and then
           create the expected distribution.
           """
           self._chi2 = None
       
       def test(self):
           """
           A subclass will override this to call ``super().test()`` and then
           create an actual distribution, usually with a distinct seed value.
           """
           self._chi2 = None
           
       @property
       def chi2(self) -> float:
           """Return chi-squared metric between actual and expected observations."""
           if self._chi2 is None:
               a_e = (
                   (self.actual_fq[k], self.expected_fq[k]) 
                   for k in self.expected_fq 
                   if self.expected_fq[k] > 0
               )
               v = sum((a-e)**2/e for a, e in a_e)
               self._chi2 = v
           return self._chi2

       @property
       def pass_test(self) -> bool:
           return self.expected_chi_2_range[0] <= self.chi2 <= self.expected_chi_2_range[1]

This defines the essence of a chi-squared test. There's another test
that isn't based on chi-squared. The serial correlation where a
correlation coefficient is computed between adjacent pairs of samples.
We'll ignore this special case for now. Instead, we'll focus on the
battery of chi-squared tests.

Linear Congruential Pseudo-Random Number Generator
--------------------------------------------------

We'll also need an LC PRNG that's constrained to 4 decimal digits.

It looks like this:

::

   class LCM4:
       """Constrained by the NCE Fortran 4-digit integer type."""
       def __init__(self, a: int, c: int) -> None:
           self.a = a
           self.c = c
       def seed(self, v: int) -> None:
           self.v = v
       def random(self) -> int:
           self.v = (self.a*self.v % 10_000 + self.c) % 10_000
           return self.v

This mirrors the old NCE Fortran on the IBM 1620 computer. 4 decimal
digits. No more.

We can use this to generate a pile of samples that can be evaluated. I'm
a fan of using generators because they're so efficient. The use of a set
to create a list seems weird, but it's very fast.

::

   def lcg_samples(rng: LCM4, seed: int, n_samples: int = N_SAMPLES) -> list[int]:
       """
       Generate a bunch of sample values. A repeat implies a cycle, and we'll stop early.

       >>> lcg_samples(LCM4(1621, 3), 1234)[:12]
       [317, 3860, 7063, 9126, 3249, 6632, 475, 9978, 4341, 6764, 4447, 8590]

       """
       rng.seed(seed)
       def until_dup(f: Callable[..., Hashable], n_samples: int) -> Iterator[Hashable]:
           seen: set[Hashable] = set()
           while (v := f()) not in seen and len(seen) < n_samples:
               seen.add(v)
               yield v
       return list(until_dup(rng.random, n_samples))

This function builds a list of values for us. We can then subject the
set of samples to a battery of tests. We'll look at one test as an
example for the others. They're each devilishy clever, and require a
little bit of coding smarts to get them to work correctly and quickly.

Frequency Test
==============

Here's one of the tests in the battery of chi-squared tests. This is the
frequency test that examines values to see if they have the right number
of occurrences. We pick a domain, *d*, and parcel numbers out into this
domain. We use :math:`\\frac{d \\times X_{n}}{10,000}` because this tends
to leverage the left-most digits which are somewhat more random than the
right-most digits.

::

   class FQTest(Chi2Test):
       expected_chi_2_range = (7.261, 25.00)

       def __init__(self, d: int = 16, size_samples: int = 6_400) -> None:
           super().__init__()
           #: Size of the domain
           self.d = d
           #: Number of samples expected
           self.size_samples = size_samples
           #: Frequency for Chi-squared comparison
           self.expected_fq = {e: int(self.size_samples/self.d) for e in range(self.d)}
       
       def test(self, sequence: list[int]) -> None:
           super().test()
           self.actual_fq = Counter(int(self.d*s/10_000) for s in sequence)

We can apply this test to some samples, compare with the expectation,
and save the chi-squared value. This lets us look at LCM parameters to
see if the generator creates suitably random values.

The essential test protocol is this:

::

   samples = lcg_samples(LCM4(1621, 3), seed=1234)
   fqt = FQTest()
   fqt.test(samples)
   fqt.chi2

The test creates some samples, applies the frequency test. The next step
is to examine the chi-squared value to see if it's in the allowable
range, :math:`7.261 \\leq \\chi^2 < 25`.

The search space
================

Superficially, it seems like there could be 10,000 choices of *a* and
10,000 choices of *c* parameter values for this PRNG. That's 100 million
combinations. It takes a bit of processing to look at all of those.

Looking more deeply, the values of *c* are often small prime numbers. 1
or 11 or some such. That really cuts down on the search. The values of
*a* have a number of other constraints with respect to the modulo value.
Because 10,000 has factors of 4 and 5, this suggests values like :math:`20k + 1` will work. Sensible combinations are defined by the following
domain:

::

   combinations = [
       (a, c)
       for c in (1, 3, 7, 11,)
       for a in range(21, 10_000, 20)
   ]

This is 2,000 distinct combinations, something we can compute on our
laptop.

The problem we have trying to evaluate these is each combination's
testing is compute-intensive. This means we want to use as many cores of
our machine as we have available. We don't want this to process each
combination serially on a single core. A thread pool isn't going to help
much because the OS doesn't scatter threads among all the cores.

Because the OS likes to scatter processes among all the cores, we need a
process pool.

Here's how to spread the work among the cores:

::

       from concurrent.futures import ProcessPoolExecutor, as_completed

       combinations = [
           (a, c)
           for c in (1, 3, 7, 11)
           for a in range(21, 10_000, 20)
       ]

       with Progress() as progress:
           setup_task = progress.add_task("setup ...", total=len(combinations))
           finish_task = progress.add_task("finish...", total=len(combinations))

           with ProcessPoolExecutor(max_workers=8) as pool:
               futures = [
                   pool.submit(evaluate, (a, c))
                   for a, c in progress.track(combinations, task_id=setup_task, total=len(combinations))
               ]
               results = [
                   f.result()
                   for f in progress.track(as_completed(futures), task_id=finish_task, total=len(combinations))
               ]

This will occupy \*all\* the cores of the computer executing the
\`evaluate()\` function. This function applies the battery of tests to
each combination of a and c. We can then check the results for
combinations where the chi-squared results for each test are in the
acceptable ranges for the test.

It's fun.

TL;DR
=====

Use **a=1621** and **c=3** can generate acceptable random numbers using
4 decimal digits.

Here's some output using only a subset of the tests.

::

   (rngtest2) % python lcmfinder.py
   setup ... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
   finish... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
   2361  1  11.46  14.22  46.64  63.76   2.30  11.33   2.16   2.16 
    981  3  10.28  15.24  52.56  66.32   2.28  11.08  10.47  10.47 
   1221  3  10.19  14.12  48.72  62.08   3.03  10.08   2.59   2.59 
   1621  3  11.70  14.91  47.12  69.52   2.23   9.69   0.86   0.86 

The output shows the *a* and *c* values followed by the minimum and
maximum chi-squared values for each test. The chi-squared values are in
pairs for the frequency test, serial pairs test, gap test, and poker
test.

Each test uses about two dozen seed values to generate piles of 3,200
samples and subject each pile of samples to a battery of tests. The seed
values, BTW, are ``range(1, 256, 11)``; kind of arbitrary. Once I find
the short list of candidates, I can test with more seeds. There are only
10,000 seed values, so, this can be done in finite time.

For example, a=1621, c=3, had chi-squared values between 11.70 and 14.91
for the frequency test. Well within the 7.261 to 25.0 range required.
The remaining numbers show that it passed the other tests, also.

For completeness, I intend to implement the remaining half-dozen or so
tests. Then I need to make sure the sphinx-produced documentation looks
good. I've done this
before. http://slott.itmaybeahack.com/_static/rngtest/rngdoc.html It's
kind of an obsession, I think.

Looking back to my 1968 self, this would have been better than the
middle-squared nonsense that caused me to struggle with bad games that
behaved badly.





