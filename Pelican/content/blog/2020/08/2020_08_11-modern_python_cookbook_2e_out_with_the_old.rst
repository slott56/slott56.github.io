Modern Python Cookbook 2e -- Out with the old
=============================================

:date: 2020-08-11 08:00
:tags: @PacktAuthors,#python,modern python cookbook
:slug: 2020_08_11-modern_python_cookbook_2e_out_with_the_old
:category: Books
:status: published

Most of the things that got cut were (to me) obviously obsolete. For
example, replacing collections.namedtuple with typing.NamedTuple seemed
like a clear example of obsolete. A reviewer really thought I should
skip all NamedTuple and use frozen data classes.

More important are some things that I learned about in my formative
years. I think they're important because they'll little nuggets of cool
algorithm. But. Pragmatically? They're too hard to explain and don't
really capture interesting features of Python.

Back in '01. Yes. The turn of the millennium.

(Pull up a chair. This is a long yarn.)

Back in '01, I was starting to look at ways to perfect my Python and
literate programming skills.

(And yes, I was using Python on '01.)

I had a project that I'd learned about in the 80's. That's in the
previous millennium. A thousand years ago. Computers were large,
expensive, and rare.

And. Random Number Generators (RNG's) were a bit of a struggle. In the
80's, more sensitive statistical methods were uncovering biases in the
RNG's of the day. Back in the 70's, Knuth's The *Art of Computer
Programming, Volume 2, Seminumerical Algorithms* had covered this topic
pretty well. But. Not quite well enough for language libraries or OS's
to offer really solid RNG's.

(The popular Mersenne Twister algorithm dates from '97.)

One of my co-workers at the time showed me a technical report that I
have no real bibliographic information for. I read it, captivated,
because it described -- in detail -- Knuth's statistical tests for
random number generators.

This lead me to Knuth Volume 2.

This lead me to implement \*all\* of this in Pascal (in the '80's.)

This lead me to implement \*all\* of this in Python (in the '00's.)

There were 10 tests. Each is a tidy little algorithm with a tidy little
implementation that can run on a big collection of data to ascertain how
random it is.

#. Frequency Test - develops frequency distribution of individual
   samples.

#. Serial Test - develops frequency distribution of pairs of samples.

#. Gap Test - develops frequency distribution of the length of gaps
   between groups samples in a given range.

#. Poker Test - develops frequency distribution for 5-card "hands" of
   samples over a small (16-value) domain.

#. Coupon Collector's Test - develops frequency distribution for lengths
   of subsets that contain a complete set of values from a small
   (8-value) domain.

#. Permutation Test - develops frequency distribution for the
   permutations of ordering of 4-sample selections.

#. Runs Up Test - develops frequency distribution for lengths of "runs
   up" where each value is larger than the previous value; one variation
   covers the case where runs are statistically dependent.

#. Runs Up Test with independent runs and a relatively large domain.

#. Runs Up Test with a "small domain", that has a slightly different
   expected distribution.

#. Maximum of T - develops frequency distribution for the largest value
   in a group of T values.

#. Serial Correlation - computes the correlation coefficient between
   adjacent pairs of values.


What's important here is that we're gaging the degree of randomness
of a collection of samples. All of these are core data science.
Finding a truly random random number generator is the same as looking
at a variable and seeing that it's too random to have any predictive
value. This is the Type I Error problem.


Doing this with RNG's means starting with a specific seed. Which
means we need to run this for a large number of seed values and
compare the results. Lots of computer cycles can be burned up
examining random number generators.


Lots.


The frequency test, for example. We bin the numbers and compare the
frequencies. They aren't the same; they're within a few standard
deviations of each other. That means you don't use 5 bins. You use
128 bins so you can compare the bin sizes to the expected bin size
and compute a deviation. The deviation for expected needs to pass a
chi-squared test.


Back in the day, chi-squared values were looked up in the back of a
handy statistics book.


That seems weak. Can we compute the exact chi-squared values?


(Spoiler alert, Yes.)


Computing expected chi-squared values means computing Sterling
numbers, Bernoulli numbers, and evaluating the partial gamma
function. Knuth gives details on Sterling numbers. I have no
reference material on Bernoulli numbers.


The Log Gamma function is ACM collected algorithms (CALGO) number 291
and 309. The incomplete gamma function is CALGO 435 and 654.


Fascinating stuff.


To me.


Of this, only one thing ever saw the light of day.


The Coupon Collector's test. Given a long sequence composed of
selections from a small pool of distinct values ("coupons"), how many
samples from the overall sequence do you have to examine to collect
one of each distinct coupon value? This yields a kind of Poisson
distribution of the number of samples seen before getting a full set
of coupons.


If there's eight kinds of coupons, the smallest number of samples we
have to examine is eight. Lucky break. One of each and done. But.
Pragmatically, we'll see a distribution that varies from a low of 8
to a high of -- well -- infinity. We'll see a peak at like 15 to 18
samples before collecting all eight coupons and a long, long tail. We
can cut the tail at 40 samples and have a statistically useful
distribution to discern of the source samples were randomly ordered.


Why did this -- of all things -- see the light of day?


It involves set manipulations.

::

   def collect_coupons(samples: Iterable[int]) -> Iterator[int]:
       while True:
           coupons = set()
           count = 0
           for u in samples:
               coupons |= u
               count += 1
               if len(set(coupons)) == 8:
           yield count


I've used a number of variations on the above theme to use set
manipulation to accumulate data.  There are a lot of ways to restate
this using itertools, also. It can be viewed as a clever "reduce"
algorithm.


But.


It's so hard to explain. And. It's not really used much by data
scientists to reject type I errors because few things fit the coupon
model very well.


But.


It's a cool set processing example.


So.


It's safely out of the book.





