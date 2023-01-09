Inelegant Python
================

:date: 2020-12-16 08:54
:tags: complexity,#python
:slug: 2020_12_16-inelegant_python
:category: Technologies
:status: published

See https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
This seems to be a popular coding interview problem.

The Python code shown on the site seems almost maliciously misleading.

The full problem is this:

   You are given an unsorted array with both positive and negative
   elements. You have to find the smallest positive number missing from
   the array in O(n) time using constant extra space. You can modify the
   original array.

Here's a common-enough Python solution.

::

   def smallest_missing_1(x):
       """
       >>> smallest_missing_1([2, 3, 7, 6, 8, -1, -10, 15])
       1
       >>> smallest_missing_1([2, 3, -7, 6, 8, 1, -10, 15])
       4
       >>> smallest_missing_1([1, 1, 0, -1, -2])
       2
       """
       try:
           return min(set(range(1, max(x)+2))-set(x))
       except ValueError as ex:
           # min() arg is an empty sequence
           return 1

Some folks don't like the try/except to detect the edge case of all
negative values. If  max(x) <= 0, then the exception will be raised, and
we could use an if statement for a LBYL solution.

What's more important is this solution violates the constant extra space
constraint. It builds two sets, which isn't a simple constant size
object; it depends on the size of the input object.

To avoid the sets, we'll use a generator.

::

   def smallest_missing_2(x):
       """
       >>> smallest_missing_2([2, 3, 7, 6, 8, -1, -10, 15])
       1
       >>> smallest_missing_2([2, 3, -7, 6, 8, 1, -10, 15])
       4
       >>> smallest_missing_2([1, 1, 0, -1, -2])
       2
       """
       try:
           return next(n for n in range(1, max(x)+2) if n not in x)
       except StopIteration as ex:
           # next() found an empty sequence
           return 1

This violates the **O**\ (*n*) constraint with the repeated use of the
**in** operator.

To get to **O**\ (*n*) and no extra storage, we're forced to (a) demand
the input is a mutable list, so we can (b) reuse the input list object
to track which numbers are present and which are absent. This reuse of a
mutable list is atypical for Python programming. Indeed, it seems like a
bad idea.

Consistent with the spirit of the problem, we're constrained to making
arithmetic changes to the values in the original list, x, to track the
state of the computation. The idea is that the value x[i] will have
\*both\* an original input value, and the presence (or absence) of some
value, p+i, in the sequence.

One traditional approach is to use the sign as a way to carry this extra
bit of information. That's why negative numbers are thrown in to the
input data. They make the sign business super confusing. Also. That's
why zero is excluded. Conventional integer math doesn't have a negative
zero, confounding the problem with array slots that have numbers that
make sign processing icky.

I'm not a fan of using the sign for this. I'd prefer to use Least
Significant Bits (LSB's) because we have a fairly large number of
available LSB's. And. We can trivially ignore zero values and their
habit of not having useful signs. Unless the list has 2**62 elements, a
little shifting won't hurt any.

Here's a solution that would \*rarely\* be used in normal Python work.
Maybe on a Circuit Playground Express MicroPython. But not anywhere
else.

::

   from typing import List

   def smallest_missing_3(x: List[int]) -> int:
       """
       >>> smallest_missing_3([2, 3, 7, 6, 8, -1, -10, 15])
       1
       >>> smallest_missing_3([2, 3, -7, 6, 8, 1, -10, 15])
       4
       >>> smallest_missing_3([1, 1, 0, -1, -2])
       2
       """
       # Purge negative numbers. Scale the other numbers.
       for i in range(len(x)):
           if x[i] < 0:
               x[i] = 0
           else:
               x[i] = x[i] << 1
       # Set LSB on positions which are filled; ignoring None values.
       # This can raise an index out-of-bounds exception, which we silence.
       for v in filter(None, (scaled >> 1 for scaled in x)):
           try:
               x[v-1] = x[v-1] | 1
           except IndexError:
               pass
       # Find first value with LSB not set.
       for i in range(len(x)):
           if x[i] & 1 == 0:
               return i+1

This is pretty atypical Python code. I'm kind of shocked folks would use
something like this as an interview question. It's rather complex and
requires some very old-school programming tricks to make the whole thing
remotely palatable.

The index out-of-bounds is particularly nasty. It means there's a
number, n, that's greater than len(x). This is worrisome, but, it also
means any gap MUST be less than this large number n. For this reason, we
can silence array index errors.

I would not be able to simply stand up in a conference room and solve
this without some additional direction. The "making arithmetic changes
to the values in the original list" secret is something I knew about and
did -- when I was younger -- but I haven't done that kind of thing in
decades.





