70% of Modern Python Cookbook 2e...
===================================

:date: 2020-03-17 08:00
:tags: packtpub,#python,modern python cookbook
:slug: 2020_03_17-70_of_modern_python_cookbook_2e
:category: Technologies
:status: published


At this point, we're closing in on 9/13 (70%) of the way through the
2nd edition rewrite.

Important changes.

#. Type Hints

#. Type Hints

#. Type Hints


First.
    Every single class, method, or function has to be changed to
    add hints. Every. Single. One. This is kind of huge. The book is
    based on over 13,000 lines of example code in 157 files. A big bunch
    of rewrites.


Second.
    Some things were either wrong or at least sketchy. These
    rewrites are important consequences of using type hints in the first
    place. If you can't make **mypy** see things your way, then perhaps
    your way needs rework.


Third.
    Dataclasses, frozen dataclasses, and NamedTuples have some
    nuanced overlapping use cases. Frequently, they differ only by small
    type hint changes.


I hate to provide useless non-advice like "try them and see which
works for you." However, there's only so much room to try and beat
out a detailed list of consequences of each alternative. Not every
decision has a clear, prescriptive, "do this and you'll be happy."
Further, I doubt any reader needs detailed explanations of
\*potential\* performance consequences of mutable vs. immutable
objects.


Also. I'm very happy cutting back on the overwrought, detailed
explanations. This is (a) not the only book on Python, and (b) not my
only book. When I started the first drafts 20 years ago, I wrote as
though this was my *magnum opus*, a lifetime achievement.  A Very Bad
Idea (VBI™).

This is a resource for people who want more depth. At work, I spend
time coaching people who call themselves advanced beginners. The time
spent with them has helped me understand my audience a lot better,
and stuck to useful exposition of the language features.


