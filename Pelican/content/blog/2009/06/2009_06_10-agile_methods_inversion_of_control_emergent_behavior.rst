Agile Methods, Inversion of Control, Emergent Behavior
======================================================

:date: 2009-06-10 09:14
:tags: agile
:slug: 2009_06_10-agile_methods_inversion_of_control_emergent_behavior
:category: Technologies
:status: published

I've run in to some Agility questions recently.  Questions that indicate
that some people just don't like the Inversion of Control aspect of
Agile methods.

We used to call IoC "Emergent Behavior".  The system isn't designed
from top-down to fill specific use cases.  Instead, the system is
designed so that the interaction of various objects will fill the use
cases.  Overall control does not reside in one place.

An Agile project is the same phenomenon.  We're not going to plan the
entire effort.  Instead, we're going to do some things that -- in the
long run -- will lead to more useful software.

Agile Question 1
----------------

"Why focus on a few use cases up front?  If we do that, then new
requirements will arrive as we develop, leading to endless rework.
Why can't we enumerate all use cases now?"

Right and Wrong.  Right: we will do endless rework.  Wrong: we will
deliver something that works before starting the rework cycle.

For some reason, focus on a use case is really hard.  Some people
feel that they can't build "just enough" software, but must
completely understand every nuance before they can do anything.

I think this is a paralyzing fear of failure, coupled with bad
experiences from management that equated all rework with failure.

The Agile approach of "build something now" is trumped by their
personal failure/rework issues, leading to bizarre designs that
include lots of things that aren't in the use case under
construction.  It leads to lots of "why are you doing this?"
conversations with lots of "it might be needed in the future."

It isn't needed now.  Let it go.  Merely having thought of it, and
leaving a stub in the design, is enough for now.  When faced with
"attribute vs. property vs. method" questions, those future
considerations can help steer you to one or the other.  But don't
give in to designing and building the future.  Just leave space for
it.

An Agile approach is about an emergent behavior.  It's built from the
edges in.  There's an inversion of control here.

Agile Question 2
----------------

"Can't you just add a button that says X?  You're supposed to be
Agile, why can't you just add this button to the page?"

First, we're not done with what you asked for two weeks ago.  Until
that's done and approved, we're not on speaking terms.

But, more importantly, "adding a button" isn't part of any existing
use case.  You're not changing priorities with this request, you're
making stuff up.

Making stuff up isn't bad, per se.  Making up a random piece of
behavior, with no actor, no goal, and no business value is bad.  Who
will click that button?  What will the business purpose be?  What
result will help that person make a decision and take action?

"It's just to show a customer."  Good start.  What's the customer's
role?  What do they do?  Are we showing the customer's sales folks
how they use this application?  Are we showing the customer's finance
folks how they use this application?  Are we showing the operational
folks?  Are we showing the underwriting folks?  In short, "who's the
actor?"

An Agile approach is about building software someone can use.
Without a use case, we're just building software haphazardly.  A use
case isn't an elaborate document, it's just an actor with a goal who
interacts with the system to create something of value.  Four simple
clauses.

From the use case, we can work out an implementation.  There is no
"inversion of control" when moving from requirements to design.   The
requirements do not emerge from the design.



-----

Wonderful blog &amp; good post.Its really helpful ...
-----------------------------------------------------

poona<noreply@blogger.com>

2012-07-06 07:48:47.082000-04:00

Wonderful blog & good post.Its really helpful for me, awaiting for more
new post. Keep Blogging!
`Agile
Coaching <http://www.cprime.com/agile/agile-coaching-consulting.html>`__





