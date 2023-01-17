How Expensive is a "Waterfall" Project Plan?
============================================

:date: 2012-08-08 08:15
:tags: software process improvement,waterfall,agile
:slug: 2012_08_08-how_expensive_is_a_waterfall_project_plan
:category: Technologies
:status: published


It's impossible to step into the same river twice; other waters are
flowing toward the sea.  It's impossible to do "head-to-head" project
comparisons.  You can't have the same people doing the same thing with
only one constraint changed.  You can try to resort to having similar
people doing the exact same thing.

It's impossible to provide trivial quantification of the costs of a
waterfall approach.  However, there's a lot of places where "up front"
engineering **adds** cost and risk.  A waterfall plan adds friction,
zero-value administrative costs and (sometimes) extra work.

For software development that doesn't involve "toy" projects, but
apply to the magical "real world" projects, it's difficult to justify
building the same "real world" thing twice.  It's hard to create a
detailed and purely economic analysis of this question.  Therefore, we
have to resort to hand-waving and speculation.

[I put "real world" in quotes, because the "real world" is a kind of
dog-whistle phrase that only project managers understand.  It appears
to mean "projects that fit my preconceived notions" or "projects that
can't be done any other way because of political considerations" or
"projects constrained by a customer to have a farcical structure".
Another variant on this dog-whistle phrase is "the realities of
running a business."  There's something in their real world that they
(a) can't define and (b) prevents any change.]

A few months back, I saw a `http://prezi.com <http://prezi.com/>`__
presentation that was intended to drive architecture, cost and
schedule conversations.  The authors were happy.  I was left
relatively mystified.

There are three relevant issues that don't fit well into a prezi
presentation.

#. Open Technology questions.  If it's **new** software development,
   there are unanswered software API, performance, quality,
   fitness-for-purpose questions.  If it's a clone or a clean-room
   reverse engineering, then there may be few questions.  Otherwise,
   there must be unknowns.

#. Open User Story questions.  If it's **new** software development,
   then the user stories are not complete, consistent and optimized.
   There must be something missing or extra.

#. Open User Experience questions.  I'm not a UX person.  Tinkering with
   an Arduino has taught me that even in the most prosaic, simplistic
   project there is a UX element.


It's easy to trivialize this as "details" or "supporting information"
omitted from the presentation.  Actually, it's considerably more
interesting that simply elaborating details.  Indeed, the missing
stuff is often more important that the elements of the presentation
than were provided.

The Standard Gaps
-----------------

While a presentation can show some elements of UX, it's not
**interactive**.  It cannot provide any useful depth on the UX.
Failure to do UX exploration (with real interaction) is crazy.
Making assumptions about UX is more likely to **create** cost and
risk.

User Stories can be kicked around in a presentation.  However.  Once
the highest-priority user stories are built, and lessons learned about
the users, the problem and the emerging solution, then the other user
stories can (and should) change based on those lessons learned.
Assuming a list of user stories and then committing to a specific
schedule **enshrines** the costs in a bad plan.  And we all know that
the plan (and the dates) are sacred once written down.

Software does not exist in a vacuum.

I'll repeat that, since it's a hidden assumption behind the waterfall.

   **Software does not exist in a vacuum.**

You have a Heisenberg problem when you start building software and
releasing it incrementally.  The presence of the new software, even
in a first-release, beta-test, barely-working mode changes the
ecosystem in which the software exists.  Other applications can (and
will) be modified to adjust to the new software.  Requirements can
(and should) change.

A waterfall project plan exists to prevent and stifle change.  A long
list of tasks and dates exists to assure that people perform those
tasks on those dates.  This is done irrespective of value created and
lessons learned.

Technology changes.  Our understanding of the technology changes.
One wrong assumption about the technology invalidates the
deliverables for a sprint.  In a project with multiple people,
multiple assumptions and multiple sprints, this effect is cumulative.
Every assumption by every person for every technology is subject to
(considerable) error.

Every technology assumption must be looked at as a needless cost
that's being built into the project.

Recently, I've been working on a project with folks that don't know
Django very well.  Their assumptions are -- sometimes -- alarming.

Part way through a sprint, I got a raft of technical questions on
encrypting passwords.  It's hard to state it strongly enough: **never
encrypt a password**.  What's more useful is this: **always hash
passwords**.  The original password **must** be unrecoverable.  There
are lots of clever hashing techniques.  Some of which are already
part of Django.  A significant portion of the sprint (appeared) to be
based on reinventing a feature already part of Django.

Do the math: a few wrong assumptions made during project planning are
canonized forever as requirements in the project.  With a waterfall
project, they're not easy to change.  Project managers are punished
for changing the project.  You can't increase the project deadline;
that's death.  You can't decrease it, either: you get blamed for
sand-bagging the estimates.

Arduino Technology Lessons Learned
----------------------------------

After buying several 74HC595 shift registers from Sparkfun, I
realized that my assumptions about the interfaces were utterly wrong.
I needed to solder a mix of right-angle header and straight-through
headers onto the breakout boards.  I tried twice to order the right
mix headers.  It seems so simple.  But **assumptions** about the
technology are often wrong.

This is yet more anecdotal evidence that **all** assumptions must be
treated as simple lies.  Some managers like to treat assumptions as
"possibly true" statements; i.e., these are statements that are
unlikely to be false.  This is wrong.  Assumptions always have a very
high probability of being false, since they're not based on factual
knowledge.

Some managers like to treat assumptions as "boundary conditions":
i.e.,  if the assumption is true, then the project will go according
to plan.  Since all of the assumptions will be prove to be incorrect,
this seems like simple psychosis.

[Interestingly, the assumptions-are-boundary folks like to play the
"real world" card: "In the real world, we need to make assumptions
and go forward."  Since all assumptions **will** be shown to be
incorrect, why make them?  Wouldn't it be more rational to say "we
need to explore carefully by addressing high-righ unknowns first"?
Wouldn't it be better to both gather facts and build an early
release of the software at the same time?]

Arduino User Story Assumptions
------------------------------

After building a prototype that addressed two of the user stories, it
slowly became clear that the third user story didn't actually exist.

Sure, the words were there on paper.  Therefore, there's a user
story.

But.

There was nothing to actually **do**.

The whole "As a [role], I need [feature] so that I can [benefit]"
that was written on day one was based on a failure to understand
precisely how much information was trivially available.  The benefit
statement was available with a small software change and no separate
user story.  And no separate hardware to support that user story.

Exploration and tinkering **reduced** the scope of the work.  In the
real world.
[In the "real world" where waterfall is considered important,
exploration is described as unbounded spending of limited resources.
In the real real world, money **must** be spent; it can either be
long hand-wringing meetings or it can be prototype development.]

The user story (written before a prototype existed) was based on a
failure to fully understand the UX.  The only way to fully understand
the UX is to build it.  Education costs money.

Arduino UX Learnings
--------------------

Perhaps the most important issue here is UX.

Once upon a time, UX was expensive, difficult and complex.  So
difficult that special-purpose prototyping tools were created to make
it possible to create a preliminary UX that could be used to confirm
UX and user stories.

This UX prototyping effort was real money spent as part of
"requirements" or "design"; it created documentation that flowed over
the waterfall for subsequent development.

This notion is obsolete.  And has been obsolete for several years.

UX is now so easy to build that it makes much more sense to build two
(or three) competing UX's and compare them to see which is
**actually** better.

Indeed, it makes a lot of sense to build one UX and release it; make
a real effort at solving the user's problems.  Then build a second UX
for A/B testing purposes to see if there's room for improvement.

I'll repeat that for folks who really like the waterfall.

It's now cheaper to actually build two than it is to write detailed
requirements for one.
-----------------------------------------------------------------------------------------

[In the "real world", this is deprecated as "wasting time playing
with the UX".  As if written requirements based on nothing more than
a whiteboard are more "real" than hands-on experience with the UX.]
You can prove this to yourself by actually observing actual UX
developers knocking out pages and screens.  Long "requirements
gathering" meetings with prospective users amount to a waste of time
and money.  Long "brainstorming" sessions, similarly, are wasteful.
Short, ongoing conversations, a build, a release, and a follow-up
review has more value, and costs less.

Do the math.  Several users and business analysts in several
multiple-hour meetings costs how much?

A pair of developers banging out fully-functioning, working UX for a
use case costs how much?

A slavish adherence to waterfall development creates "real world"
costs.



-----

Does the approach scale? How much does each iterat...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-08-22 19:46:20.193000-04:00

Does the approach scale? How much does each iteration/experiment cost?
If it's $100k per go around, well we better think long and hard. How
about saying, lets spend x dollars to try y? If it is a total failure,
we will have spend x dollars to learn z.

Yah, I know, putting x dollars and failure in the same sentence is not a
whining proposition. However, who knows, your might actually find a
customer that might like the truth.


"Does the approach scale".  By definiti...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2012-08-28 07:17:12.529000-04:00

"Does the approach scale?". By definition. Did you read the post?
Cheaper is cheaper at every scale.





