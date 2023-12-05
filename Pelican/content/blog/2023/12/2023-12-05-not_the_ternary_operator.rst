It's Not THE Ternary Operator -- there are many
===============================================

:date: 2023-12-05 08:01
:tags: language,semantics
:slug: 2023_12_05-not_the_ternary_operator
:category: Python
:status: published

I'm sick of reading about **THE** Ternary Operator.

There is not merely **a** single operator that is ternary.
There are many operators that are ternary.

Here's one example:

::

    >>> 6+1 >= 6 >= 6-1

The ``>= >=`` operator is ternary. It has 3 operands.  Count them.

There are a 36 of these ternary operators.

"Oh, pish-tosh," you say. "It's an example of two binary operators."

Really?

In a sense, you're almost right, it's equivalent to ``6+1 >= 6 and 6 >= 6-1``. Which is three binary operators.

But it's **not** three binary operators. It's one ternary operator.

"Whoa. What about ``5 < 6 < 7 < 8``?" you reply triumphantly. "That has four operands!"

Right. It's quaternary. There a lot of ways to create quaternary (and higher) operators in Python.
There are 216 of quaternary operators.  1296 quinary.

There is not **A Ternary Operator**.  The phrase is meaningless.  You can stop using it.

There's more
------------

We're not done.

::

    >>> (2*a + 1
    ...    for a in range(5)
    ...    if a % 2 == 0
    ... )

Is ternary.

I'll clarify:

1.  ``2*a + 1`` -- expression #1

2.  ``range(5)`` -- expression #2

3.  ``a % 2 == 0`` -- expression #3

Admittedly, the two pieces of interstitial syntax are complicated.

a.  ``for a in``  -- kind of big; and it names a bind variable.

b.  ``if`` -- more typical for ternary operators.

But. There are three operands separated by punctuation.

It is, therefore, ternary.

And yes. When we have multiple ``for`` clauses or multiple ``if`` clauses, we clearly have quaternary and quinary operators.
That's part of my point: there are a number of *arities* and a number of operators of each arity.

I could go on
-------------

A Big Pointless Beef (BPB™) is often this.

**The ternary operator** (by which I presume they mean the conditional expression) **evaluates the middle first.**

Which is kind of a "so what?"

Many things in Python are left-to-right.

But not everything is trivially left-to-right.

::

    >>> noisy = lambda x: print(x) or x
    >>> list(noisy(2*a + 1)
    ...   for a in noisy(range(5))
    ...   if noisy(a % 2 == 0)
    ... )
    range(0, 5)  # expression 2, the range(...)
    True  # expression 3, the if.
    1  # expression 1, the 2*a+1.
    False
    True
    5
    False
    True
    9
    [1, 5, 9]

The ``range(5)`` -- in the middle of this particular ternay operator -- is evaluated first.
And only evaluated once, where the outer expressions are evaluated on right-to-left order over and over again.

We're not done
--------------

Consider, if you will,

::

    >>> a = list(range(5))
    >>> a[1:-1]
    [1, 2, 3]

The ``a[1:-1]`` is ternary. It has three expressions. Count them yourself.

Also, ``a[:-1:2]`` and ``a[-1::-1]``.  All ternary subsets of a more general quaternary operator.

"That'a wrong! You can't call a slice part of an operator," you claim.

Perhaps I am pushing it. But it sure looks like ``a`` is one expressions, ``1`` is another and ``-1`` is the third.
And it sure looks like ``[`` is one separator, ``:`` is another, and there's an extra closing
punctuation mark of ``]``.

"You've jumbled up indexing and slicing!" you claim. "They're clearly separate syntactic categories!"

Clearly? If I can only using slicing in the context of indexing, I'm not completely sold that these two concepts
are separate and foreign.  They seem pretty tightly coupled.

Summary
--------

Stop writing (and saying) "The Ternary Operator". Please.

There are a lot of ternary operators.

If you don't like the **Conditional Expression** because it's too much like a list comprehension with that "evaluate something not on the left first" semantics,
please say that you don't like **The Section 6.13 Conditional Expression**.

Please.  Please try to be precise.

Otherwise, the rest of your rant on evaluation order looks like you haven't really taken the time to think things through.
Maybe you have, but the use of "The Ternary Operator" dilutes your message.

Other languages use phrases like "the ternary operator." That doesn't really mean much.
We're talking about Python, where there's more than one.
