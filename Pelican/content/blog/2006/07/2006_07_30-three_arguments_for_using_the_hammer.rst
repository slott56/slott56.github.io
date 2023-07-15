Three Arguments for Using the Hammer
====================================

:date: 2006-07-30 16:42
:tags: architecture,software design,complexity
:slug: 2006_07_30-three_arguments_for_using_the_hammer
:category: Architecture & Design
:status: published





When we're
**Holding the Hammer** , everything's a nail.  There are a
number of supporting arguments for this.  I won't beat down the
**All Those Features** ™ decision-making pattern again.
That, and some part of **Tomorrow's Dollars Don't Exist** ™ decision-making pattern are
in "`Is it Over-Solving or Exploiting
Technology? <{filename}/blog/2006/07/2006_07_21-is_it_over_solving_or_exploiting_technology.rst>`_ "



From `Improving-NAO <http://improving-nao.blogspot.com/>`_ : "I [struggle] with the Tomorrows
Dollars Don't Exist argument. Every other application or component of my app
that really requires the RDBMS will already be paying for its mass of features,
so the incremental cost to my app using a limited set of the features is
limited."



Clearly, we agree that the
basic **Tomorrow's Dollars Don't Exist** ™ management pattern is flawed.  
My point is that
**all**  of
the cost -- no matter how limited -- is money that's wasted.  Limited is still
non-zero, and I find all cost to be
objectionable.



Additionally, I argue
that the "limited" costs are surprisingly large.  It takes a lot of work and
coordination to do schema migration, when a file format change has almost zero
impact.  It takes a lot of work and coordination to back up a message-queue
database where the message queue data is transient;  A restore could lead to
serious problems stemming from duplicating
transactions.



The real issue is that
**all**  of
the costs associated with applying the RDBMS to transient data are
wasted.



Here's the nub of the
**It's Already Here** ™ decision
pattern.



"Since it exists in the
organization already ... The app requiring queuing does not live in a
vacuum."



True, we're making
*additional* 
use of the RDBMS.  We have the organization and the skills to make use of the
RDBMS.  However, we will wind up canonizing many worthless features into
essential parts of the solution architecture. 




I strongly object to this canonization
of the RDBMS as an essential feature of the solution.  It leads to the following
problem:

When the RDBMS doesn't scale, we diddle
around with queries and indexes.  This won't make it scalable, since the
insert/update interleaved with full table scans is what slows everything
down.



We won't consider viable
solutions to the scaling issue.  Instead, we waste time putting lipstick on a
pig.  None of this solves the real, underlying message queueing problem. 




Using the RDBMS defers costs to
tomorrow, raising the TCO.  Using the RDBMS throws features at the problem,
which don't contribute to the solution, and raise the TCO.  Using things because
they are ready to hand specifically avoids comparing the solution against the
problem.  



Each of these is a way of
dodging our responsibility as problem-solvers.  Rather than engage with the
users to determine what's wrong and how we can fix it, we start bashing away at
various kinds of fasteners with our hammer.  And when it doesn't work, we demand
a bigger hammer.









