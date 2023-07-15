Permutations, Combinations and Frustrations
===========================================

:date: 2022-11-22 17:21
:tags: algorithm,software design
:slug: 2022_11_22-permutations_combinations_and_frustrations
:category: Technologies
:status: published

The issue of permutations and combinations is sometimes funny.

Not funny weird. But, funny "haha."

I received an email with 100's of words and 10 attachments. (10.
Really.) The subject was how best to enumerate 6! permutations of
something or other. With a goal of comparing some optimization algorithm
with a brute force solution. (I don't know why. I didn't ask.)

Apparently, the programmer was not aware that permutation creation is a
pretty standard algorithm with a standard solution. Most "real"
programming languages have libraries which already solve this in a tidy,
efficient, and well-documented way.

For example

https://docs.python.org/3/library/itertools.html#itertools.permutations

I suspect that this is true for every language in common use.

In Python, this doesn't even really involve programming. It's a
first-class expression you enter at the Python ``>>>`` prompt.

::

   >>> import itertools
   >>> list(itertools.permutations("ABC"))
   [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

What's really important about this question was the obstinate inability
of the programmer to realize that their problem had a tidy, well
understood solution. And has had a good solution for decades. Instead
they did a lot of programming and sent 100's of words and 10 attachments
(10. Really.)

The best I could do was provide this link:

`Steven Skiena, The Algorithm Design
Manual <https://www.algorist.com>`__

It appears that too few programmers are aware of how much already
exists. They plunge ahead creating a godawful mess when a few minutes of
reading would have provided a very nice answer.

Eventually, they sent me this:

http://en.wikipedia.org/wiki/Heap's_algorithm

As a grudging acknowledgement that they had wasted hours failing to
reinvent the wheel.





