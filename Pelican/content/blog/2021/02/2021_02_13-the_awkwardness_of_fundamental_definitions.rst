The Awkwardness of Fundamental Definitions
==========================================

:date: 2021-02-13 13:45
:tags: writing
:slug: 2021_02_13-the_awkwardness_of_fundamental_definitions
:category: Technologies
:status: published

A pragmatic description of a language (like Python) from axiomatic -- or
really axiom-like -- foundations is exasperatingly hard. I don't think I
have any answers, but I sure do have a lot of challenges. I think
there's a path that involves a lot of "don't look down -- just edge
along the face of this cliff a few more feet and it's going to be okay."

The actual language foundations, and a more useful conceptual foundation
don't always match up.

My specific example is trying to use a subset of Python to get started
with.

One of the reasons we write software is to see useful results. So you
need output, i.e., the ``print()`` function. On the other end of this,
you might want to accept inputs. But. But... You could finesse that by
simply assigning literal values instead of reading something.

This leads to the print() function and expressions as a kind of minimal
language to see the essence of programming. (I know this isn't an
original thought. I'm setting up the conflict.)

Do we explain functions in general when we're explaining this subset of
Python? Or do we stick with arithmetic?

::

   print("Hello, world!")

::

   print("355/113=", 355/113)

Maybe the F-string?  Assignment? Or do we really need assignment?
(Spoiler alert, no.)

What about other functions? Python has a bunch of built-ins. The math
and random modules let us build small games without much intellectual
overhead.

And how much can we explain about functions? The whole mathematical
notion of function as mapping from domain to range: does that count? Or
nah? What about Python's flexible argument and parameter handling?

Exceptions? Do we have to explain them? Or do we shrug at division by
zero and kind of ignore it? If we talk about exceptions, do we have to
talk about stack frames and tracebacks?

At the foundation, a language is variable bindings and function
evaluation. But. Do you explain any of that? And if so, how?

The additional complication is multiple authors, technical reviews,
editors, and everyone else involved. There's a complex web of varying
opinions on what's foundational and how much explanation is required.
It's new to one person, so it should be up font. But, a lot of up-front
material is boring. Everything in programming involves a tricky nuance
somewhere; how much of that nuance is relevant now and how much is later
and how much is digressive?

Trust
-----

To an extent, there's a trust relationship between writer and reader. It
may help to build this if the writer can provide a "trust me on this,"
scenario that (eventually) results in a more complete explanation. The
logical conclusion here is that there's no place in the book for "too
advanced, buy my next book." Instead, every difficult and nuanced thing
would need to (eventually) be explained. That seems impossible, though.

With editors, co-authors, and reviewers, the trust relationship is
exactly wrong. Everything needs to be challenged and clarified.

tl;dr Writing is sometimes hard. And that's the expectation. It's a
narrow fairway surrounded by shoals.





