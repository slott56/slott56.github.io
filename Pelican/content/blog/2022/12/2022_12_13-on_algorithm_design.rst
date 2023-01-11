On Algorithm Design
####################

:date: 2022-12-13 11:00
:tags: algorithm,design,Design Principles
:slug: 2022_12_13-on_algorithm_design
:category: Technologies
:status: published

Some background: `FAERIE DUST™ <{filename}/blog/2022/11/2022_11_22-faerie_dusttm.rst>`__,
`Obstinate Idiocy <{filename}/blog/2013/06/2013_06_06-obstinate_idiocy_updated.rst>`__,
`Obstinate Idiocy, Expanded <{filename}/blog/2022/11/2022_11_22-obstinate_idiocy_expanded.rst>`__,
and even `Permutations, Combinations and Frustrations <{filename}/blog/2022/11/2022_11_22-permutations_combinations_and_frustrations.rst>`__.
I want to set up algorithm design as the diametric opposite of Obstinate
Stupidity. To do that, let's look at Obstinate Stupidity.

The theme?

    **We did something wrong, and we don't want to fix it.**

I emphasize this because it takes many forms. Another common variant is
"We can't afford to continue the way we are, but we can't afford the
time to fix it, either." Sometimes, "Management wants this fixed, but we
don't have any budget." You know how it is.

The current go-round is someone who has an algorithm of intensely stupid
(and largely irrelevant) complexity. See `My algorithm performs badly,
do I need
asyncio? <{filename}/blog/2022/12/2022_12_06-my_algorithm_performs_badly_do_i_need_asyncio.rst>`__.

The situation is touchy. They have pre-reasoned an answer -- ``asyncio``
-- and they're looking for (a) confirmation that they're obviously right
and (b) help rewriting something needlessly complex to somehow be faster
even when it's compute-bound. Specifically, they want Faerie Dust.

Frivolous Complexity
====================

How do I know it has needless, frivolous complexity?

Here are two symptoms.

#. The problem has a lot of context. In thise case, there's a hierarchy.
   The hierarchy may seem irrelevant, but it has this mind-numbingly
   complex back-story, that they can't seem to ignore or abstract out of
   the essential problem. There's a (large) number of details that don't
   really explain what the hierarchy means or why it has to be
   preserved. but somehow make it essential.
#. The problem can only be described by repeating the legacy algorithm.

Let's dwell on this second symptom for a moment. We have two competing
issues:

-  The legacy algorithm is too slow. AND,
-  There's no other way to describe the problem.

This should make it clear they are looking at ``asyncio`` as a kind of
Faerie Dust that will magically make the bad algorithm good. Without
fixing the bad algorithm.

I want to emphasize the existence of details which can neither be
explained nor removed. The hierarchy must be there simply because it
must be there. Bizarre complications to walk the hierarchy are,
therefore, essential even if no one can explain them.

Algorithm Design
================

To actually improve the processing they need a new algorithm.

I can't emphasize this enough: **they need a new algorithm**. (This
often means a new data structure.)

"Tuning" in any form is nothing more than nibbling around the edges to
make a bad algorithm run 15% faster.

Rewriting may replace 
:math:`\textbf{O}(2^n)` with :math:`\textbf{O}(n \log n)`.
This would be dramatically better. From seconds to milliseconds. You know, 1,000% faster.

There's a disciplined approach to this. Here are the steps.

#. Write the post-condition for the processing as a whole.
#. Write code that achieves the post-condition. (This may involve
   decomposing the big problem into sub-problems, each of which is
   approached by the same two-step process.)

The intensely painful part of this is creating the post-condition.

I suggested they "write an assert statement that must be true when the
algorithm has completed, and computed the right answer."

Hahahah.

What an idiot I was.

They didn't know how to write an ``assert`` statement. And at this
point, they stopped. Brick Wall. Dead in the water. Cannot proceed.
Done. Failed.

The ``assert`` statement has become the end-of-the-line. They can't (or
won't) do that. And they won't ask about it.

Me: "Do you have a question?"

Them: "I have to think before I can even begin to ask a question."

Me: "How about think less and ask more. Do you have trouble writing the
word assert? What's stopping you?"

Them: [silence]

Okay.

Post-Conditions
===============

The post-condition is true when you're done. Let's look at my favorite,
M must be the maximum of A and B.

..  math::

    M \geq A \textbf{ and } M \geq B

This becomes an ``assert`` statement through (what seems to me, but boy
was I wrong) the following kind of translation.

::

   assert M >= A and M >= B, f"Algorithm Failed {M=} {A=} {B=}"

Again, I acknowledge I was wrong to think
creating an ``assert`` statement from a post condition was in any way
clear. It's absolutely bewilderingly impossible.

It's also important to note that the above condition is incomplete. The
value :math:`M = A+B` will also satisfy the condition. We need to test our
test cases to be sure they really do what we want.

We really need to be more complete on what the domain of values for
:math:`M` is.

..  math::

    M = A \textbf{ or } M = B \textbf{ and } M \geq A \textbf{ and } M \geq B

We could rewrite this slightly to be

..  math::

    M \in \{A, B\} \textbf{ and } M \geq A \textbf{ and } M \geq B

This version directly suggests a potential set comprehension to compute
the result:

::

   M = {m for m in {A, B} if m >= A and m >= B}.pop()

This is the advantage of writing post-conditions. They often map to
code.

You can even try it as pseudo-SQL if that helps you get past the
``assert`` statement.

::

   SELECT M FROM (TABLE INT(X); A; B) WHERE M >= A AND M >= B

I made up a ``TABLE INT(X); A; B`` to describe a two-row table with
candidate solutions. I'm sure SQL folks have other sort of "interim
table" constructs they like.

The point is to write down the final condition.

I'll repeat that because the folks I was trying to work with refused to
understand the assert statement.

**Write down the final condition**.

The Current Problem's Post-Condition
====================================

The problem at hand seems to involve a result set, :math:`R`, pulled from
nodes of some hierarchy, :math:`H`, :math:`R \subseteq H`. Each element of
the hierarchy, :math:`h \in H` has a set of strings, :math:`s(h)`. It
appears that a target string, :math:`t`, must be a member
of :math:`t \in s(r), r \in R`. I think.

Note that the hierarchy is nothing more than a collection of identified
collections of strings. The parent-childness doesn't seem to matter for
the search algorithm. Within the result set, there's some importance to
the tier of the hierarchy, :math:`t(h)`, and a node from tier 1 means all
others are ignored or something. Can't be sure. (The endless backstory
on the hierarchy was little more than a review of the algorithm to query
it.)

If any of this is true, it would be a fairly straightforward ``map()``
or ``filter()`` what could be parallelized with ``dask`` or
``concurrent.futures``.

But we can't know if this really is the post-condition until someone in
a position to know writes the post-condition.

Things To Do
============

The post-condition defines the results of test cases. The
``assert`` statement becomes part of the pytest test cases. In a kind of
direct copy-and-paste process to shift from design aid to test result
condition.

Currently, the algorithm they have seems to have no test cases. They
can't write a condition to describe correct answers, which suggests they
actually don't know what'a correct.

If they wrote test cases, they might be able to
visualize an ``assert`` statement that confirms the test worked. Might.
It appears to be asking a lot to write test cases for the legacy
algorithm.

Indeed, if they wrote a conditional expression that described the
results of any working example, they'd have taken giant steps toward the
necessary ``assert`` statement. But that's asking a lot, it appears.

And Then What?
==============

Once you have a target condition, you can then design code to satisfy
some (or all) of the target condition. `Dijkstra's A Discipline of
Programming <https://www.google.com/books/edition/A_Discipline_of_Programming/MsUmAAAAMAAJ?hl=en>`__
has a thorough description of the "weakest precondition" operator. It
works like this:

#. Imagine a statement that might satisfy some or all of your
   post-condition.
#. Substitute the effect of the statement into the post-condition.
#. What's left is the weakest pre-condition for that statement to work.
   It's often the post-condition for a statement must precede the
   statement you wrote.

You write the program from the desired post-condition moving forward
until you get a weakest pre-condition of True. Back to front. From goal
to initialization.

Post-condition gives you statements. Statements have pre-conditions. You
iterate, writing conditions, statements, and more conditions.

(You can also spot useless code because the pre-condition matches the
post-condition.)

For the silly "maximum" problem?

Try M := A as a statement. This only works if A >= B. That's the
pre-condition that is derived from substituting M = A into the
post-condition.

Try M := B as a statement. This only works if B >= A. That's the
pre-condition that is derived from substituting M = B into the
post-condition.

These two pre-conditions describe an if-elif statement.

Note that this feels weirdly arbitrary and exploratory. It's a kind of
empiricism where we try statements and see if they're helpful. There
don't need to be any constraints. The post-condition is all that's
required to explore the space of statements that might work, or at least
might help.

Of course, we're not stupid. And we're lazy. We don't search the
infinite space of statements. We can often imagine the statements
without a **lot** of complex work. The formal weakest pre-condition
process is necessary to confirm our intuition. Or to assert that
something is free of astonishing side-effects.

It all depends on one thing: a clear, formal statement of the
post-condition.

Since I made the mistake of describing the post-condition as a line of
code, we've hit some kind of brick wall related to "I won't write code."
Or "I don't want to be seen writing code." or "I don't want you to
critique my code."

Dunno.





