The SortedContainers Package for Python
=======================================

:date: 2014-04-10 08:00
:tags: performance,#python,object-oriented design
:slug: 2014_04_10-the_sortedcontainers_package_for_python
:category: Technologies
:status: published

See this: `SortedContainers — sortedcontainers 0.6.0
documentation <http://www.grantjenks.com/docs/sortedcontainers/>`__

Here's some text from the invitation.

    *You may find the the performance comparison and implementation
    details interesting because it doesn't use any sophisticated tree
    data structure or balancing algorithms. It's a great example of
    taking advantage of what processors are good at rather than what
    theory says should be fast.*

The documentation is extensive. The implementation details are
interesting. The claim of faster is supported nicely. I have two
quibbles.

#. It actually **does** use a sophisticated tree data structure. A list of lists really is a kind of tree.

#. "rather than what theory says should be fast" doesn't make any sense to me at all.


A claim that Computer Science theory isn't right bothers me. If
theory says some algorithm is fast, there are only two possibilities:
(1) theory is actually right and it really is fast and the
demonstration was incomplete or (2) the theory is incomplete, and the
implementation extends (or replaces) the old theory; the
implementation is **new** theory.


It's never the case that theory is "wrong." That fails to understand
the role of theory.


It's always the case that an implementation either **confirms**
theory or **extends** theory with new results.


To me, this package demonstrates one of two things.


#. The theory was incomplete and this package is a new theory that replaces the old, wrong theory.

#. The theory was right and this package demonstrates that the theory was right by being a good, solid, usable implementation.


I would suggest the second option here: this package shows the
value of Python's list-of-lists as a high-performance technique
for implementing sorted structures. It's not an example of "taking
advantage of what processors are good at." This is an example of
using Python **properly** to squeeze excellent performance out of
the available structures.


The really important insight is this "The sorted container types are
implemented based on a single observation: bisect.insort is fast,
really fast."


This is a profound observation.  Read more
here: http://www.grantjenks.com/docs/sortedcontainers/implementation.html


