The TLA Problem -- Over-Engineering Three-Letter Acronyms
=========================================================

:date: 2017-12-19 08:00
:tags: #python,architecture
:slug: 2017_12_19-the_tla_problem_over_engineering_three_letter_acronyms
:category: Technologies
:status: published

| Here's something we can gleefully over-engineer. Because anything
  worth doing is worth over-engineering until it morphs into a different
  kind of problem.
| I'm unclear on the backstory, so try not to ask "why are we doing
  this?" I think it has something to do with code camp and there are
  teenagers involved.
| What we want to do is generate a pool of 200 TLA's. Seems simple,
  right?
| The first pass may not be obvious, but this works well.

::

   import string
   import random
   from typing import Iterator

   DOMAIN = string.ascii_lowercase
   def tlagen() -> Iterator[str]:
       while True:
           yield "".join(random.choice(DOMAIN) for _ in range(3))

   tla_iter = tlagen()
   for i in range(200):
       print(next(tla_iter))

| 
| This makes 200 TLA's. It's configurable, if that's important. We could
  change tlagen() to take an argument in case we wanted four-letter
  acronyms or something else.
| However. This will generate words like "cum" and "ass". We need a
  forbidden word list and want to filter out some words. Also, there's
  no uniqueness guarantee.

The Forbidden Word Filter
-------------------------

| Here's a simple forbidden word filter. Configure FORBIDDEN with a set
  of words you'd like to exclude. Maybe exclude "sex" and "die", too.
  Depends on what age the teenagers are.

::

   def acceptable(word: str) -> bool:
       return word not in FORBIDDEN

| 
| Here's another handy thing. Rather than repeat the "loop until" logic,
  we can encapsulate it into a function.

::

   from typing import TypeVar, Iterator
   T_ = TypeVar("T_")
   def until(limit: int, source: Iterator[T_]) -> Iterator[T_]:
       source_iter = iter(source)
       for _ in range(limit):
           item = next(source_iter)
           yield item

| 
| Okay. That's workable. This lets us use the following:

::

   list(until(200, filter(acceptable, tlagen())))

| 
| Read this from inside to outside. First, generate a sequence of TLA's.
  Apply a filter to that generator. Apply the "until" counter to that
  filtered sequence of TLA's. Create a list with 200 items. Nice.
| The TypeVar gives us a flexible binding. The input is an iterator over
  things and the output will be an iterator over the same kinds of
  things. This formalizes a common understanding of how iterators work.
  The **mypy** tool can confirm that the code meets the claims in the
  type hint.
| There are two sketchy parts about this. First the remote possibility
  of duplicates. Nothing precludes duplicates. And we're doing a bunch
  of string hash computations. To avoid duplicates, we need a growing
  cache of already-provided words. Or perhaps we need to build a set
  until it's the right size. Rather than compute hashes of strings, can
  we work with the numeric representation directly?

Numeric TLA's
-------------

| There are only a few TLA's.
| $$26^{3} = 17576 $$
| Of these, perhaps four are forbidden. We can easily convert a number
  back to a word and work with a finite domain of integers. Here's a
  function to turn an integer into a TLA.

::

   def intword(number: int) -> str:
       def digit_iter(number: int) -> Iterator[int]:
           for i in range(3):
               number, digit = divmod(number, 26)
               yield digit
       return "".join(DOMAIN[d] for d in digit_iter(number))

| 
| This will iterate over the three digits using a simple
  divide-and-remainder process to extract the digits from an integer.
  The digits are turned into letters and we can build the TLA from the
  number.
| What are the numeric identities of the forbidden words?

::

   def polynomial(base: int, coefficients: Sequence[int]) -> int:
       return sum(c*base**i for i, c in enumerate(coefficients))

   def charnum(char: str) -> int:
       return DOMAIN.index(char)
       
   def wordint(word: str) -> int:
       return polynomial(26, map(charnum, word))

| 
| We convert a word to a number by mapping individual characters to
  numbers, then computing a polynomial in base 26. And yes, the
  implementation of polynomial() is inefficient because it uses the \*\*
  operator instead of folding in a multiply-and-add operation among the
  terms of the polynomial.
| Here's another way to handle the creation of TLA's.

::

   FORBIDDEN_I = set(map(wordint, FORBIDDEN))
   subset = list(set(range(0, 26**3)) - FORBIDDEN_I)
   random.shuffle(subset)
   return list(map(intword, subset[:200]))

| 
| This is cool. We create a set of numeric codes for all TLA's, then
  remove the few numbers from the set of TLA's. What's left is the
  entire domain of permissible TLA's. All of them. Shuffle and pick the
  first 200.
| It **guarantees** no duplicates. This has a lot of advantages because
  it's simple code.
| This, however, takes a surprisingly long time: almost 17 milliseconds
  on my laptop.

Numeric Filtering
-----------------

| Let's combine the numeric approach with the original ideal of
  generating as few items as we can get away with, but also checking for
  duplicates.
| First, we need to generate the TLA numbers instead of strings. Here's
  a sequence of random numbers that is confined to the TLA domain.

::

   def tlaigen() -> Iterator[int]:
       while True:
           yield random.randrange(26**3)

| 
| Now, we need to pass unique items, and reject duplicate items. This
  requires a cache that grows. We can use a simple set. Although, a
  bit-mask with 17,576 bits might be more useful.

::

   def unique(source: Iterator[T_]) -> Iterator[T_]:
       cache = set()
       for item in source:
           if item in cache:
               continue
           cache.add(item)
           yield item

| 
| This uses an ever-growing cache to locate unique items. This will tend
  to slow slightly based on memory management for the set. My vague
  understanding is the implementation will double the size when hash
  collisions start occurring, leading a kind of log\ :sub:`2` slowdown
  factor as the set grows.
| The final generator looks like this:

::

   list(until(200, unique(filter(lambda w: w not in FORBIDDEN_I, tlaigen()))))

| 
| Reading from inner to outer, we have a generator which will produce
  numbers in the TLA range. The few forbidden numbers are excluded. The
  cache is checked for uniqueness. Finally, the generator stops after
  yielding 200 items.

tl;dr
-----

| Of course, we're using timeit to determine the overall impact of all
  of this engineering. We're only doing 1,000 iterations, not the
  default of 1,000,000 iterations.
| The original version: 0.94 seconds.
| The improved number-based version: 0.38 seconds.
| So there.  Want to generate values from a limited domain of strings?
  Encode things as numbers and work with the numeric representation.
  Much faster.





