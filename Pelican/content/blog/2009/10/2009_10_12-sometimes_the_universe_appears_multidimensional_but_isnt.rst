Sometimes the universe appears multidimensional -- but isn't
============================================================

:date: 2009-10-12 18:23
:tags: star-schema,dimensional data,database design
:slug: 2009_10_12-sometimes_the_universe_appears_multidimensional_but_isnt
:category: Technologies
:status: published

Had a knock-down drag-out fight with another architect recently over
"status" and "priority".

She claimed that the backlog priority and the status where the same
thing. I claimed that you can easily have this.

Priority: 1, Status: Not Started

Priority: 2, Status: In Process

Priority: 3, Status: Completed

See? It's obvious that they're independent dimensions.

She said that it's just as obvious that you're doing something wrong.

Here's her point:

-   If you have priority 1 items that aren't in process now, then
    they're really priority 2. Fix them to honestly say priority 2.

-   If you have priority 2 items that "somehow" jumped ahead of
    priority 1 items, they were really priority 1. Fix them to say
    priority 1. And don't hand her that "in the real world, you have
    managers or customers that invert the priorities". Don't invert
    the priorities, just change them and be honest about it.

-   The only items that are done must have been priority 1, passed
    through an "in-process" state and then got finished. Once they're
    done, they're not priority 1 any more. They're just done.

-   Things that hang around in "in-process, not done" have two parts.
    The part that's done, and some other part that's in the backlog
    and not priority 1.

She says that priority and status are one thing with the following
values.

-  Done.
-  Priority 1 = in process right now.
-  Priority 2 = will be in process next. Not eventually. Next.
-  Priority 3 through ∞ = eventually, in order by priority.

Any more complex scheme is simply misleading (Priority 1 not being
done right now? Is it a resource issue? A priority issue? Why
*aren't* you doing it?)



-----

Say I have a Priority 1 tasks like say solving my ...
-----------------------------------------------------

Chris<noreply@blogger.com>

2009-10-12 20:52:52.115000-04:00

Say I have a Priority 1 tasks like say solving my app's use of the
enterprise LDAP for security but I cannot progress because the whole
LDAP team is in training for the week. Does this mean my Priority 1 is
really a Priority 3 because of totally external factors? I'd think my
security architecture/implementation would be pretty important to solve
early.


I'd agree with her: it's easier to keep pr...
-----------------------------------------------------

EOL (Eric O LEBIGOT)<noreply@blogger.com>

2009-10-13 03:49:45.466000-04:00

I'd agree with her: it's easier to keep priorities simple
(unidimensonal). Reassessing priorities is indeed a fact of life. I
think I first read about this in David Allen's famous Getting Things
Done…


IMO, Priority and Status are two different attribu...
-----------------------------------------------------

Michael Levy<noreply@blogger.com>

2009-10-13 19:17:49.116000-04:00

IMO, Priority and Status are two different attributes owned by two
different roles. The Product Owner owns the Priority and the dev team
owns the status.


There is also the public priority, and a persons p...
-----------------------------------------------------

Paddy3118<noreply@blogger.com>

2009-10-14 03:13:54.435000-04:00

There is also the public priority, and a persons private priority that
don't have to agree in practice.
Or,
Tasks may have high priority but cannot be worked on due to resource
limitations. You don't wait around, you get something else done which
becomes your personal top priority.
- Paddy.


I'd agree with her _if_ you have control over ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-13 09:13:07.179000-04:00

I'd agree with her \_if\_ you have control over all resources necessary
to complete your task. But, if you work in a multi-departmental team
with non-overlapping / conflicting priorities, \*your\* priority 1 task
may need to wait for someone else's priority 2 task to become a priority
1.
So, while you wait to get back to your priority 1, you spend time on
your 2s & 3s.





