Essay 23 - Jumping the Technology Ship
======================================

:date: 2005-09-22 20:42
:tags: architecture,software design
:slug: 2005_09_22-essay_23_jumping_the_technology_ship
:category: Architecture & Design
:status: published





We're told, repeatedly, to avoid changing horses
in mid-stream.  We're told not to follow the crowd blindly. 




Once upon a time, we made a technology
decision that -- at the time -- was right.  But things have shifted around a
bit, and what was once prudence is now folly.  When do you jump
ship?



Clearly, the politics of this
decision are paralyzing.  I generally throw up my hands and appeal to the
nebulous "strategic direction".  If anyone wants to declare the new
tools/language/infrastructure/platform "strategic", that can quell most
pointless hand-wringing.



When you
switch from mixed Oracle + DB2 to all DB2, you'll piss off all the developers
and support people who like Oracle.  They'll tell you that it's a mistake to
switch away from their favorite product.  They'll have a lot of reasons to stick
with or switch to their favorite product.  The decision, ultimately, **is** political.
It can't be looked at as anything but serving a constituency to
curry favor.  Yes, there's *some* engineering sense to it, but don't think that there is one "correct," rational
engineering decision which will win the day.  Engineering is trade-offs; it's
just applied politics using math and
physics.



Here's a model that might help frame up the decision in a
way that makes it possible to bypass the politics of the situation and move on
to something perhaps more
fruitful.


**Timing**. Or, the cost of doing nothing. What will it really cost if we wait until later,
and it gets worse (i.e., things start to break for want of compatibility,
upgrades, bug-fixes,
etc.)

**Quality**. How sure are we that we will continue to create products of comparable quality?
Note that we have a current level of success, and it doesn't really depend on
the technology, but rather on process and
organization.

**Productivity**. What will the productivity drop be as we switch?  Will there be an improvement
with newer technology?



Let's apply this
model to the age-old PL/SQL vs. J2EE web development
question.



**Timing** of jumping ship.  Currently, we're building our web pages with PL/SQL.  As we
move into the portal-based architecture, and look around at open-source
solutions, we find that they're all J2EE.  Are things broken?  No.  Things
aren't broken today.  



Will they break?
Not until Oracle turns its back on PL/SQL.  Considering their vast size, PL/SQL
has a good decade run left in it.  Indeed, if someone had real guts, they'd open
source it and let it stand as a competitor to Perl, PHP and
Python.



**Quality**. Currently, we're pretty good at PL/SQL web pages.  Would we be better with J2EE?
Would STRUTS improve the overall quality?  Specifically, which of the quality
factors might be touched: Need Satisfaction, Resource Use, Maintainability,
Adaptability, TCO?  



PL/SQL -- lacking effective object definition -- can impose limitations on reuse and
understandability.  While Java has the capability of producing larger and more
sophisticated applications, the quality of work that I've seen in Java indicates
that it isn't the norm.   PL/SQL has limited adaptability.  But that puts us
back into the "Oracle Viability" question; and PL/SQL has a long
future.



**Productivity**. While jumping ship does lead to a dip in deliverables, it may lead to
improvements in the long run.  First, STRUTS can be a big simplification, as can
JSP's.  Second, there's a lot of open source out
there.



While it is clear that we
shouldn't consider jumping ship yet, we now have criteria for revisiting the
decision.  When someone brings it up again, we can look at timing, quality and
productivity and see if anything has changed that would make us rethink any of
these factors.








