Third Time's the Charm: the version 3.0 phenomenon
==================================================

:date: 2014-02-21 10:52
:tags: unit testing,software process improvement,OO design,requirements
:slug: 2014_02_21-third_times_the_charm_the_version_30_phenomenon
:category: Architecture & Design
:status: published


Somewhere, I have a vague recollection of reading advice from someone
(Bill Gates?) that it takes three versions to get things right. The
context may have been a justification of the wild success of Windows
3.0.

Or, I could be just making it up.

But one thing I have noticed is that there's a definite bias toward
looking at software three times.

I worked (briefly) with an agile project management group that
suggested that everything will be released three times, called the
"Good", "Better", "Best" releases.

-  The good release passed the unit tests.

-  The better release included any non-functional (performance, auditability, maintainability, etc.) improvements required.

-  The best implementation possible.

Not everything required three releases. Simpler components can merge
better and best. Some components simply start out in really, really
good shape.

Teaching Moment
---------------

What I've also noticed is that the explanation of the component --
writing documentation, presenting to peers in a walkthrough -- leads
to profound rethinking.

May things may appear to be better or best in the sense above. Until
we have to explain them. Then they're no longer "best" but merely
"better" or perhaps even "good."

A few minutes spent hand-waving through a design often points to
things that aren't quite to easy to explain. A walkthrough is very
beneficial to the person doing the presentation.

But, not too early.

When I made military software, we had Preliminary Design Reviews that
were done before coding begins. The idea was to surround the
difficult coding work with yet more process steps and yet more
deliverable intermediate results.

The intent was noble: if a walkthrough reveals so much, then do the
walkthroughs early and often.

However. I'm beginning to think that early isn't ideal.

I think that the design walkthrough should be delayed until after
minimally working code exists. Once there's code -- with automated
unit tests -- then refactoring to meet non-functional quality factors
(like performance) is easier and more likely to be successful.

Also, refactoring to make the software clear, simple, and elegant
should probably wait until it works and has a complete suite of
automated unit tests.





