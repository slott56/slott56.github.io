Needless Complexity -- Creating Havoc Leads to Mistakes
=======================================================

:date: 2017-05-16 08:00
:tags: algorithm,#python,analysis
:slug: 2017_05_16-needless_complexity_creating_havoc_leads_to_mistakes
:category: Technologies
:status: published

I received the worst code example ever. The. Worst.

Here's the email.

   I have hurriedly created a blog post titled [omitted] at the url
   below
   [also omitted]
   ...
   Unfortunately, I am neither an algorithm expert or a Python expert.
   However, I am willing to jump in.


   Please review the Python code snippets. I know that they work because
   I ran them using Python 2.7.6. It was the environment available on my
   work PC. Speed to get something to the group so that it does not
   disband outweighs spending time on environments. The goal is not to
   be Pythonic but to have anyone that has written any code follow the
   logic.

   Also, please review the logic. Somehow, I managed to get the wrong
   answer. The entire blog post is a build to provide a solution to CLRS
   exercise 2.3-7. My analysis gave me the answer of O( {n [log n]}**2 )
   and the CLRS answer is O(n [log n] ). Where did I screw up my logic?


    CLRS is https://mitpress.mit.edu/books/introduction-algorithms.


The referenced blog post is shocking. The "neither an algorithm
expert or a Python expert" is an understatement. The "willing to jump
in" is perhaps a bad thing. I sent several comments. They were all
ignored. I asked for changes a second time. That was also ignored.
Eventually, changes were made reluctantly and only after a
distressing amount of back-and-forth.

Havoc was created through a process of casually misstating just about
everything that can possibly be  misstated. It transcended mere
"wrong" and enters that space where the whole thing can't even be
falsified. It was beyond simply wrong.


My point here is (partially) to heap ridicule on the author. More
importantly, want to isolate a number of issues to show how simple
things can become needlessly complex and create havoc.

The Problem
-----------


The definition of the problem 2.3-7 seems so straightforward.

      "Describe a :math:`\Theta(n \log n)`-time algorithm that, given a set
      :math:`S` of :math:`n` integers and another integer :math:`x`, determines whether or
      not there exist two elements in :math:`S` whose sum is exactly :math:`x`."


This brings us to problem #1. The blog post is unable to actually
repeat the problem. Here's the quote:

..

   x + y = x0
   where
   x ∈ N and y ∈ N for some finite set of integer values N
   x0: the integer to which x and y sum
   x != y

It's not at all clear what's going on here. What's x0? What's N? Why is x!=y even introduced?

This is how havoc starts. The requirements have been restated in a way
that makes them more confusing. The original terminology was dropped
in favor of random new terminology. There's no reason for restating
the problem. The consequence of the bad restatement is to introduce
needless features and create confusion.

The Python Nonsense
-------------------

A quote:

   Concepts are demonstrated via code snippets. They code snippets were
   executed using Python 2.7.6. They were written in such a way that
   anyone with basic coding skills could read the code. In other words,
   the goal was not to be Pythonic.

Python 2.7.6 has been obsolete since May of 2014. At the very least,
use a current release.

The goal of using Python without being Pythonic seems to be -- well
-- schizophrenic. Or it's intentional troll-bait. Hard to say.


Another paragraph says this.

      The Python community will be annoyed because I am using Python 2
      and not 3. Their annoyance is appropriate. Unfortunately, I only
      have Windows machines and can't afford to screw them up at this
      point in time.


What? That makes no sense at all. It's trivial to install Python 3.6
side-by-side with Python 2. Everyone should. Right now. I'll wait.
See https://conda.io/docs/. Start here: https://conda.io/miniconda.html.


If you're going to insist on using the quirky and slow Python 2, you
absolutely **must** use this in all of your code:

::

      from __future__ import print_function, division, absolute_import, unicode_literals


Python 2 code without this is wrong. If you're still using Python 2,
add this to all your code, right now. Please. You'll have to fix
stuff that breaks; but we'll all thank you for it. pylint --py3k will
help you locate and fix this.

The code with a -2/10 pylint score
-----------------------------------

I'm trying to reproduce this faithfully. It's hard, because the
original blog post has issues with layout.

::

      SomeIntegerList = [1, 2, 3, 4, 5, 6]
      DesiredSumOfIntegers = 11
      for SomeIntegerA in SomeIntegerList:
       for SomeIntegerB in SomeIntegerList:
        if SomeIntegerA == SomeIntegerB: continue
              SumOfIntegers = SomeIntegerA + SomeIntegerB
              print "SomeInteger A = ", SomeIntegerA, ", SomeInteger B = ", SomeIntegerB, ", Sum of Integers = ", SumOfIntegers
        if DesiredSumOfIntegers == SumOfIntegers:
            print "DesiredSumOfIntegers = ", DesiredSumOfIntegers, " was found"

(The original really could not be copied and pasted to create code
that could even be parsed. I may have accidentally fixed that. I hope
not.)

Almost every line of code has a problem. It gets worse, of course.
There's output in the original blog post that provides a hint as to
what's supposed to be happening here.

Addition is Commutative
-----------------------

Yes. There is an entire paragraph plus a spreadsheet which proves
that addition is commutative. An. Entire. Paragraph. Plus. A.
Spreadsheet.

Meanwhile, factorial, multiplication, and division aren't mentioned.
Why do we need a spreadsheet to show that addition is commutative,
yet, all other operators are ignored? No clue. Moving on.

Permutations
------------

A quote:

      Now, let's talk about the number of computations involved in using
      nested for loops to examine all the possible addition
      permutations. Here I am using the term permutation as it is
      strictly defined in mathematics.

First. The algorithm uses all combinations. :math:`\textbf{O}(n^2)`.

Second. "as it is strictly defined in mathematics" should go without
saying. If you feel the need to say this, it calls the entire blog
post into question.

It's like "honestly." Anyone who has to establish their honesty with
"can I be honest with you?" is still lying.

If we're being strict here, are we not being strict elsewhere? If
we're not being strict, why not?

The algorithm enumerates all **combinations** of n things taken 2 at
a time without replacement. For reasons that aren't clear. The
original problem statement permits replacement. The restatement of
the problem doesn't permit replacement.

The n things taken r or 2 at a time problem
--------------------------------------------

There's a table with values for :math:`\frac{n!}{(n-r)!}`
No hint is given as to what this table is or why it's here.  I think
it's supposed to be because of this:

.. math::

  \frac{n!}{r!(n-r)!} \text{ with } r=2 \equiv
  \frac{n!}{2(n-2)!} \equiv \frac{n\times(n-1)}{2}


It's hard to say why commutativity of addition gets a paragraph,
but this gets no explanation at all. To me, it shows a disregard
for the reader: the reader doesn't understand addition, but they
totally get factorial.

Another Perspective
-------------------

A quote

         Another perspective is to note that the nested for loops result
         in O(n^2). Clearly, the above approach is not scalable.


That's not "another perspective." That's. The. Point. The entire
point of the exercise is that the brute force algorithm isn't
optimal.

The Worst Code Snippet Ever
---------------------------

This is truly and deeply shocking.

::

      SomeIntegerList = [1, 2, 3, 4, 5, 6]
      DesiredSumOfIntegers = 11
      i = 0
      for SomeIntegerA in SomeIntegerList:
          i = i + 1
          j = 0
       for SomeIntegerB in SomeIntegerList:
              j = j + 1
              if j > i:
                  print "i = ", i, ", j = ", j
                  SumOfIntegers = SomeIntegerA + SomeIntegerB
                  print "SomeInteger A = ", SomeIntegerA, ", SomeInteger B = ", SomeIntegerB, ", Sum of Integers = ", SumOfIntegers
            if DesiredSumOfIntegers == SumOfIntegers:
                print "DesiredSumOfIntegers = ", DesiredSumOfIntegers, " was found"


This is what drove me over the edge. This is unconscionably evil
programming. It transcends mere "non-Pythonic" and reaches a realm of
hellish havoc that can barely be understood as rational. Seriously.
This is evil incarnate.

This is the most baffling complex version of a half-matrix iteration
that I think I've ever seen. I can only guess that this is written by
someone uncomfortable with thinking. They copied and pasted a block
of assembler code changing the syntax to Python. I can't discern any
way to arrive at this code.

The Big-O Problem
------------------

This quote:

      Even though the number of computations is cut in half

The rules for Big-O are in the cited CLRS book.

..  math::

    \textbf{O}(\frac{n^2}{2}) = \textbf{O}(n^2)

The "cut in half" doesn't count when describing the overall
worst-case complexity. It needs to be emphasized that "cut in half"
doesn't matter. Over and over again.

This code doesn't solve the problem. It doesn't advance toward
solving the problem. And it's unreadable. Maybe it's a
counter-example? An elaborate "don't do this"?

The idea of ``for i in range(len(S)): for j in range(i): ...`` seems to
be an inescapable approach to processing the upper half of a matrix,
and it seems to be obviously :math:`\textbf{O}(n^2)`.

The Binary Search
-----------------

This quote is perhaps the only thing in the entire blog post that's
not utterly wrong.

      we can compute the integer value that we need to find. We can than
      do a search over an ordered list for the integer that we need to
      find.

Finally. Something sensible. Followed by more really bad code.
The code starts with this

::

      def binarySearch(alist, item):

instead of this

::

      from bisect import bisect

Why does anyone try to write code when Python already provides it?
There's more code, but it's just badly formatted and has a net pylint
score that's below zero. We've seen enough.

There's some further analysis that doesn't make any sense at all:

      Since the integers that sum must be distinct, the diagnol on the
      matrix have values of N/A

And this:

      Secondly, we should remove the integer that we are on from the
      binary search

This is a consequence of the initial confusion that decided that
:math:`x \neq y` was somehow part of the problem. When it wasn't. These two
sentences indicate a level of profound confusion about the essential
requirements. Which leads to havoc.

Added Complication
------------------

The whole story is pretty badly confused. Then this arrives.

      Complicate Problem by Having Integer List Not Sorted


It's not clear what this is or why it's here. But there it is.

It leads eventually to this, which also happens to be true.

      The total computation complexity is O(2 \* n [log n] ) = O(n [log
      n] )

That's not bad. However. The email that asked for help claimed
``O( {n [log n]}**2 )``. I have no idea what the email is talking about.
Nor could I find out what any of this meant.

The Kicker
----------

The kicker is some code that solves the problem in
:math:`\textbf{O}(n)` time. Without using a set, which is interesting.


This was not part of the CLRS exercise 2.3-7. I suppose it's just
there to point out something about something. Maybe it's a "other
people are smarter than CLRS"? Or maybe it's a "just google for
the right answer without too much thinking"? Hard to say.
A sentence or two of introduction might be all that's required to
see why the other result is there.

Lessons Learned
---------------

Some people like to add complexity to the problem. The :math:`x \\neq y`
business is fabricated from thin air. It adds to the code complexity,
but is clearly not part of the problem space.
This creates havoc. Simple havoc.

Some people appear to act like they're asking for help. But they're
not. They may only want affirmation. A nice pat on the head. "Yes,
you've written a blog post." Actual criticism isn't expected or
desired. This is easy to detect by the volume and vehemence of the
replies.

Given a list of numbers, S, and a target, x, determine of two values
exist in the set that sum to x.

::

         >>> S = [1,2,3,4,5,6]
         >>> x=11
         >>> [(n, x-n) for n in S if (x-n) in S]
         [(5, 6), (6, 5)]
         >>> bool([(n, x-n) for n in S if (x-n) in S])
         True

This follows directly from the analysis. It doesn't add anything new
or different. It just uses Python code rather than indented
assembler.

This first example is :math:`\textbf{O}(n^2)` because the in operator is
applied to a list. We can, however, use ``bisect()`` instead of the ``in``
operator.

::

      >>> [(n, x-n) for n in S if S[bisect(S, (x-n))-1] == x-n]
      [(5, 6), (6, 5)]
      >>> x=13
      >>> [(n, x-n) for n in S if S[bisect(S, (x-n))-1] == x-n]
      []

This achieves the goal -- following the parts of the analysis that
aren't riddled with errors -- without so much nonsensical code.
This does require some explanation for what bisect(S, i) does. It's
important to note that the bisect() function returns the position at
which we should insert a new value to maintain order. It doesn't
return the location of a found item. Indeed, if the item isn't found,
it will still return a position into which a new item should be
inserted.

If we want this to be :math:`\textbf{O}(n)`, we can use this:

::

      >>> S = [1,2,3,4,5,6]
      >>> S_set = set(S)
      >>> x=11
      >>> bool([(n, x-n) for n in S_set if (x-n) in S_set])
      True

This replaces the linear list with a set, ``S_set``.
The ``(x-n) in S_set`` operation is :math:`\textbf{O}(1)`, leading to the overall operation
being :math:`\textbf{O}(n)`.

If you want to shave a little time, you can use ``any()`` instead of
``bool([])``. If you're not returning the pairs, you can reduce it to
``any(x-n in S_set for n in S_set)``. Try it with timeit to see what the
impact is. It's surprisingly small.





