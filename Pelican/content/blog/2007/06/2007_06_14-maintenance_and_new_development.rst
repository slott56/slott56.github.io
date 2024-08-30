Maintenance and New Development
===============================

:date: 2007-06-14 13:23
:tags: maintenance,planning,innovation,productivity
:slug: 2007_06_14-maintenance_and_new_development
:category: Management
:status: published







I read recently a quick note on a `Very productive day <http://blog.vrplumber.com/1870>`_ .  New development feels more productive than maintenance because it's more "linear"; it sounds like that means fewer dead-ends, less exploration.



I also read recently "`How to innovate on time <http://www.scottberkun.com/blog/2007/how-to-innovate-on-time/>`_ " where the trick is to increase your failure rate.  In short, explore more dead-ends to find an innovation in a bounded time period.



So encountering fewer dead-ends feels more productive, but encountering more dead-ends is more innovative?  This superficial contradiction of dead-ends bad/good means that I've missed something.



I think that it isn't the simplistic linearity of work that makes for a productive day.  I think it's the internal vs. external drivers that make for a more productive-feeling day.  



I think that a productive day is a day that includes a great deal of innovation, some failures and rework.  But the failures are ones we could anticipate, and feel good about exploring alternatives.  The failures aren't actual dead-ends where we don't know what to do next.



An unproductive day is where we find blockages that we didn't anticipate and can't easily see any way around.  An unproductive day is where we find that external events have piled up to create obstacles.



Spectrum
---------



So this is the spectrum that I think I see.



Innovation.  Time to explore alternatives through failure and rework.  Boundaries that can be seen, challenges that can be anticipated.  Characterized by "OK, keep trying."



Productivity.  Boundaries that can be seen, challenges that can be anticipated.  Time is constrained, so there isn't so much failure and rework of alternative solutions.  Characterized by "That worked, what's next?"



Low-Productivity.  Vague boundaries that must be discovered; challenges that can't be anticipated.  Failures turn into dead-ends where there aren't any obvious alternatives.  Characterized by "That didn't work either, let me think about this for a while."



Soul-Crushing Evil.  Boundaries are announced dynamically and change with the political climate.  Failures and rework appear random.  Characterized by "You should have known they wouldn't accept that solution; it doesn't matter how well it works."



Consequences
------------



We'd all like to innovate.  How do we get there?



Stepping up from productive to innovative looks like a matter of self-direction.  It's innovative if you explore more alternatives and endure more failure and rework.  If you're already in a productive environment, you can take the next step without too many obstacles.



If we're in a low-productivity environment, how do we increase our pace of exploration?  I think the ticket is to more firmly characterize the boundaries and constraints.  I also think that some maintenance isn't worth the time and effort.



If we're in soul-crushing evil, we have to prevent dead-ends from appearing out of thin air.  It might help to document the boundaries and constraints.  Sometimes this is a personality issue, and the dead-ends are appearing because someone needs to exercise control by creating dead-ends and obstacles.  This isn't technical, so I can't do much more than recognize the situation and hope it will go away.



The Value of Maintenance
------------------------



If maintenance feels low productivity, perhaps it is.  Perhaps doing maintenance on software doesn't really create enough value.



Some maintenance is bug-fixing.  And some bug-fixing is necessary.  We didn't construct the right suite of unit tests, so we don't really have a proper design, and we need to fix it.



Some maintenance, however, is really adaptation to new requirements.  This is where the line needs to get drawn.  In some cases, we can probably write new software more quickly and with higher quality than we can adapt or adjust existing software.



Let's say we have an application that needs expansion in some area.  We need to understand the interface to that area.  This may include coming to grips with file formats, RDBMS structures, API calls, object definitions, packages of classes, XML messages: all kinds of software architectural features.  Once we've got the interface, we've literally only scratched the surface.  We then need to explore all of the internals to make the enhancement.



But, if the internals need to be enhanced, how valuable are they?  Are a component's internals ever worth preserving?



Clearly, there's a enhance-vs.-replace decision to be made.  Just as clearly, many managers are uncomfortable with replace.



Why Not Replace?
----------------



Replacing software is scary for the standard pair of reasons: it appears to introduce cost and risk.



Replacing software appears costly because it's new development, and we all know that new development is more expensive than enhancement.  Anyway, that's the standard management response.  



Replacing software appears risky because there are so many unknowns.  Except -- of course -- in this case where the interface is essentially fixed, the technology is fixed, and the requirements are easy to define based on existing functionality and the desired enhancements.



I think we can all be more productive if we can just convince managers that we can build a replacement before we've even finished the analysis required to do maintenance.  Certainly, there's no risk in a replacement.



It's hard to get permission for this kind of thing.  What it takes is forgiveness.  Each maintenance task needs to be examined critically.  Eventually, you'll find t situation where it's clear to you that new development is obviously cheaper.  Make the business case, get shot down, then do it anyway.  Choose your battles wisely and it becomes "out of the box thinking" not "insubordination."





