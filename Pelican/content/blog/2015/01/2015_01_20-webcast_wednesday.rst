Webcast Wednesday
=================

:date: 2015-01-20 08:00
:tags: #python,python for secret agents,webcast,mastering object-oriented python
:slug: 2015_01_20-webcast_wednesday
:category: Books
:status: published

Be there: http://www.oreilly.com/pub/e/3255

Of course, I've got too many slides. 58 slides for a 60 minute
presentation. That's really about 2 hours of material. Unless people
have questions, then it's a half-day seminar.

Seriously.

I think I've gone waaaay too far on this. But it's my first one, and I'd
hate to burn through all eight slides, take a few questions and be done
too soon.

If this goes well, perhaps I'll see if I can come up with other 1-hour
topics.

I worry a great deal about rehashing the obvious.

On the other hand, I'm working with a room full of newbies, and I think

I could spend several hours on each of their questions.

And straightening out their confusions.

Case in point.

Not directly related to the webcast.

One of my colleagues had seen a webcast which described Python's &, \|,
and ~ operators, comparing  them with and, or and not.

I'm not 100% sure, but... I think that this podcast -- I'm getting this
second-hand; it's just hearsay -- showed that there's an important
equivalence between ``and`` and ``&``.

This is true, but hopelessly obscure. Since & has a higher priority than
the comparison operators, there will be serious confusion when one fails
to parenthesize properly.
Examples like this abound:

::

   >>> 3 == 3 & 4 < 5
   False
   >>> (3 == 3) & (4 < 5)
   True

Further, the fact that ``&`` can't short-circuit had become confusing to the
colleague. I figured out some of what was going on when trying to field
some seemingly irrelevant questions on "Why are some operators more
efficient?" and "How do you know which to use?"

Um. That's not really the point. There's no confusion if you set the
bit-fiddling operators aside.

The point is that ``and``, ``or``, ``not``, and the ``if-else`` conditional expression
live in their own domain of boolean values. The fact that ``&``, ``|``, ``^``, and
``~`` will also operate on boolean values is a kind of weird duplication,
not a useful feature. The arithmetic operators also work on booleans.
Weirdly.

The Python rules are the rules; it makes sense for ``True&True`` to yield
``True``. Results depend on the operands. It would be wrong in that sense
for ``True&True`` to be ``1``. But it would also fit the concept of these
operators a little better if they always coerced bool to int. This
happens for ``*`` and ``+``: ``True+True == 2``.

Why can't it be true for ``&`` and ``|``? It would reduce potential confusion.
I'm sure the person who implemented ``__and__()``, ``__or__()``, ``__xor__()``,
and ``__invert__()`` was happy to create a parallel universe between and
and &. I'm not sure I agree.

And perhaps I should have a webcast on Python logic. It seems like a
rehash of fundamentals to me. But I have colleagues confused by
fundamentals. So perhaps I'm way wrong about what's fundamental and
what's useful information.





