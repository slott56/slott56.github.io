On Generator Functions, Yield and Return
========================================

:date: 2016-08-26 07:22
:tags: #python,functional python programming,generator functions
:slug: 2016_08_26-on_generator_functions_yield_and_return
:category: Technologies
:status: published

Here's the question, lightly edited to remove the garbage. (Sometimes
I'm charitable and call it "rambling". Today, I'm not feeling
charitable about the garbage writing style filled with strange
assumptions instead of questions.)

    someone asked if you could have both a yield and a return in the same
    ... function/iterator. There was debate and the senior people said,
    let's actually write code. They wrote code and proved that couldn't
    have both a yield and a return in the same ... function/iterator.
    ....

    The meeting moved on w/out anyone asking the why question. Why
    doesn't it make sense to have both a yield and a return. ...


The impact of the **yield** statement can be confusing. Writing code
to mess around with it was somehow unhelpful. And the shocking
"proved that couldn't have both a yield and a return in the same ...
function" is a serious problem.

(Or a seriously incorrect summary of the conversation; a very real
possibility considering the garbage-encrusted email. Or a sign that
Python 3 isn't widely-enough used and the emil omitted this essential
fact. And yes, I'm being overly sensitive to the garbage. But there's
a better way to come to grips with reality and it involves asking
questions and parsing details instead of repeating assumptions and
writing garbage.)


An example
----------

::

    >>> def silly(n, stop=None):
    ...     for i in range(n):
    ...         if i == stop: return
    ...         yield i

    >>> list(silly(5))
    [0, 1, 2, 3, 4]
    >>> list(silly(5, stop=3))
    [0, 1, 2]

This works in both Python 3.5.1 and 2.7.10.

Some Discussion
----------------

A definition with no **yield** is a conventional function: the
parameters from some domain are mapped to a return value in some
range. Each mapping is a single evaluation of the function with
concrete argument values.

A definition with a **yield** statement becomes an iterable generator
of (potentially) multiple values. The **return** statement changes
its behavior slightly. It no longer defines the one (and only) return
value. In a generator function (one that has a **yield**) the
**return** statement can be thought of as if it raised the
**StopIteration** exception as a way to exit from the generator.

As can be seen in the example above, both statements are in one
function. They both work to provide expected semantics.

The code which gets an error is this:

::

  >>> def silly(n, stop=3):
  ...     for i in range(n):
  ...         if i == step: return "boom!"
  ...         yield i

The "why?" question is should -- perhaps -- be obvious at this point.
The **return** raises an exception; it doesn't provide a value.

The topic, however, remains troubling. The phrase "have both a yield
and a return" is bothersome because it fails to recognize that the
**yield** statement has a special role. The **yield** statement
transforms the semantics of the function to make it into a different
object with similar syntax.

It's not a matter of having them "both". It's matter of having a
**return** in a generator. This is an entirely separate and
trivial-to-answer question.

A Long Useless Rant
-------------------

The email seems to contain an implicit assumption. It's the notion
that programming language semantics are subtle and slippery things.
And even "senior people" can't get it right. Because all programming
languages (other then the email sender's personal favorite) are
inherently confusing. The confusion cannot be avoided.

There are times when programming language semantics **are**
confusing.  For example, the ++ operator in C is confusing. Nothing
can be done about that. The original definition was tied to the
PDP-11 machine instructions. Since then... Well.... Aspects of the
generated code are formally undefined.  Many languages have one or
more places where the semantics are "undefined" or only defined by
example.

This is not one of those times.

Here's the real problem I have with the garbage aspect of the email.
If you bring personal baggage to the conversation -- i.e.,
assumptions based on a comparison between some other language and
Python -- confusion will erupt all over the place. Languages are
different. Concepts don't map from language to language very well.

Yes, there are simple abstract principles which have different
concrete realizations in different languages. But among the various
concrete realizations, there may not be a simple mapping.

It's essential to discard all knowledge of all previous favorite
programming languages when learning a new language.
I'll repeat that for the author of the email.

  **Don't Go To The Well With A Full Bucket.**

You won't get anything.

In this specific case, the notion of "function" in Python is expanded
to include two superficially similar things. The syntax is nearly
identical. But the behaviors are remarkably different. It's essential
to grasp the idea that the two things are different, and can't be
casually lumped together as "function/iterator".

The crux of the email appears to be a failure to get the Python
language rules in a profound way.





