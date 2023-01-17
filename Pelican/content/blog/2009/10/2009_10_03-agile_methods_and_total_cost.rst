Agile Methods and "Total Cost"
==============================

:date: 2009-10-03 07:35
:tags: COCOMO,TCO,agile,estimating
:slug: 2009_10_03-agile_methods_and_total_cost
:category: Technologies
:status: published

Many folks ask about Agile project planning and total cost. As our
internal project managers wrestle with this, there are a lot of
questions.

Mostly these questions are rejections of incremental delivery ("All
or Nothing") or rejections of flexibility ("Total Total Cost"). We'll
look at these rejections in detail.

Traditional ("waterfall") project planning creates a master plan,
with all skills, all tasks, all effort, and all costs. It was easy
to simply add it up to a total cost.

Software development, unlike -- for example -- carpentry, has
serious unknowns. Indeed software development has so many unknowns
that it's not possible to compare software project management with
the construction trades.

A carpenter has a task ("frame up these rooms") that has an
absolute boundary with no unknown deliverables. No one says things
like "we need to separate the functions of these users from those
users." They say "build a wall, surface dry-wall, tape, paint, add
molding." The carpenter measures, and knows precisely the
materials required.

The carpenter rarely has new technology. The pace of change is
slow. A carpenter may switch from hand-held nails to a nail gun.
It's still nails. The carpenter may switch from wooden 2x4's to
metal supports. It's still vertical members and nails. The
carpenter may switch brands of wall-board. It's still wall-board.

The consequence of this is that -- for software projects --
**Total Cost Is Hard To Predict**.

Hack-Arounds
------------

Total cost is hard to predict, but we try to do it anyway. What we
do is add "risk factors" to inflate our estimate. We add risk
factors for the scope of delivery. We add risk factors for our
ability to deliver.

We can organize these risk factors into several subtle buckets.
The `COCOMO <http://en.wikipedia.org/wiki/COCOMO>`__ model breaks
scope down into three Product Attributes and four Hardware
Attributes. It breaks delivery down into five Personnel Attributes
and three Project Attributes.

This is a hack-around because we simply cannot ever know the
*final* scope, nor can we ever know our ability to deliver. We
can't know our ability to deliver because the team is constantly
changing. We should not cope with this expected constant state of
flux by writing an elaborate plan and then reporting our failure
to meet that plan. That's stupid.

Worse still, we can't know the scope because it's usually a fabric
of lies.

Scope Issue 1: "Required"
-------------------------

Customers claim that X, Y and Z are "required". Often, they have
no idea what "required" even means. I spent a fruitless hour with
a customer that had a 24×7 requirement. I said, "you haven't
purchased hardware that will give you 24×7, so we're submitting
this change order to remove it from the requirements."

They said, "It's more of a goal. We don't want to remove it."

I said, "It cannot be achieved. You will not pay us because we
will fail. Can we remove it and rewrite it as a 'goal'?"

They said, "No need to remove it: we wouldn't failure to meet that
requirement as a 'failure'."

"Okay," I said, "what's the minimum you'll put up with before
suing us for failing?"

They couldn't answer that. They had no "required" up-time and
could not determine what was "required". They had a goal, but no
minimum that would trigger labeling the project a failure.

Of course, the project failed. But not because of up-time. There
were dozens of these kinds of poorly-worded requirements that
weren't really required.

Scope Issues 2: "The Game"
--------------------------

I worked with some users who were adept at gaming IT. They knew
that IT was utterly incapable of delivering everything in the
requirements document. They knew this and planned on it.

Also, the users knew that a simple solution would not "add enough
value"; a simple solution would get rejected by the governance
committee. They knew this and planned on it also.

The users would write amazing, fabulous, wondrous requirements,
knowing that some of them were sacrificial. The extra requirements
were there to (1) force IT to commit serious resources to the
project and (2) convince governance that the software "added
enough value".

IT spent (wasted?) hours planning, architecting, designing,
estimating and tracking progress against **all** of the
requirements. Then, when we got to acceptance testing, there were
numerous "requirements" that were not required, nor even desired.
They were padding.

What To Do?
-----------

Okay. Scope and delivery are unknowable. Fine. In spite of this,
what do we do to provide a reasonable estimate of development
effort?

#.  Gather the "requirements" or "desires" or "wishes" or "epics"
    or "stories" or whatever you've got that provides some scope
    definition. This is the "analysis" or "elaboration" phase.
    Define "what", but not "how". Clearly define the business
    problem to be solved. Avoid solution-speak like "database",
    "application server", and the like.

#.  Decompose. Define a backlog of sprints based on what you know.
    If necessary, dig into some analysis details to provide more
    information on the sprints. Jiggle the sprints around to get a
    consistent size and effort.

#.  Prioritize based on your best understanding. Define some
    rational ordering to the sprints and releases. Provide some
    effort estimate for the first few releases. This estimate is
    simply the sum of the sprint costs. The sprints should be all
    about the same effort and about the same cost. About. Not
    exactly. Fine tune as necessary.

#.  Prioritize again with the users. Note that the sprint costs and
    the sprints required to release are all in their face. They can
    adjust the order only. Cost is not negotiable. It's largely
    fixed.

Rejection 1: All Or Nothing
---------------------------

One weird discussion point is the following: "Until release X,
this is all useless. You may as well not do release 1 to X-1,
those individual steps are of no value."

This is not true, but it's a way some folks try to reject the idea
of incremental releases.

You have two possible responses.

-   "Okay." In this case, you still create the releases, you just
    don't deliver them. We watched two members of the customer's
    management team argue about the all-or-nothing issue. One
    bone-head kept repeating that it was all-or-nothing. Everyone
    else claimed that Release 1 and 2 were really helpful, it was
    release 3 to X-1 that were not so useful.

-   "What not?" In this case, you suspect that the priorities are
    totally wrong and -- for some reason -- the customer is
    unwilling to put them in the correct order.

Everything can be prioritized. Something *will* be delivered
first. At the very least, you can play this trump card. "We need
to do incremental releases to resolve any potential problems with
delivery and turn-over."

Rejection 2: Total Total Cost
-----------------------------

The most frustrating conversations surround the "total cost"
issue.

The trick to this is the prioritization conversation you had with
your users and buyers. Step 4, above.

You gave them the Release - Sprint - Cost breakdown.

You walked through it to put the releases and sprints into the
correct order.

What you have to do is add another column to the spread-sheet:
"Running Cost". The running cost column is the sum of the sprint
costs. **Each running cost number is a candidate total cost**.
It's just that simple.

It takes several tries to get everyone's head wrapped around the
concept.

Customer Control
----------------

You know the concept has started to sink in when the customer
finally agrees that they can pull the plug on the project after
any sprint. They grudgingly admit that perhaps they control the
costs.

You know they really get it when they finally say something like
this.

"We can stop at any time? Any time? In that case, the priority is
all wrong. You need to do X first. If we were -- hypothetically --
going to cancel the project, X would create the most value. Then,
after that, you have to do Z, not Y. If we cancel after X and Z,
we've solved most of the real problems."

When they start to go though hypothetical project cancelation
scenarios with you, then they get the way that they control the
total cost.

This tends to avoid the tedious of negotiations where the customer
then changes the requirements to meet their budget. Nothing is
more awful than a customer who has solicited bids via a Request
for Proposal (RFP) process. They liked our bid, but realized that
they'd asked for too much, and want to reduce the scope, but don't
have priorities or cost-per-release information.

If you do the priorities interactively -- with the customer --
there's no "negotiation". It's just decision-making on their part.



-----

Thanks for the answer!

I see, that&#39;s like eve...
-----------------------------------------------------

etienned<noreply@blogger.com>

2009-10-02 13:06:01.238000-04:00

Thanks for the answer!
I see, that's like everything else, I have to teach and educate my
clients.





