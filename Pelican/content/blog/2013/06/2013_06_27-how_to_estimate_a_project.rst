How to Estimate a Project
=========================

:date: 2013-06-27 10:28
:tags: budgeting,software process improvement,estimating
:slug: 2013_06_27-how_to_estimate_a_project
:category: Technologies
:status: published


A recent question

   "what we might expect, in terms of 1) Time to completion, 2) Cost to
   implement according to the mockup, 3) Monthly server/maintenance
   costs and 4) approximate team size required"


This question was followed by this acknowledgement:

   "it is hard to make the above estimations, given the lack of clarity
   on the architecture which will be employed, and given the nature of
   software development itself."


This is an understatement. The statement is generally well written,
but the word "hard" is weak. It's not hard. It's essentially
impossible.

**I.  The Conundrum**

Let's say you decide that the budget for "everything" is two point
five kajillion dollars. Clearly, you don't want to just fork that
money over to a roomful of developers and wait a year for something to
happen.

An Agile approach is a sensible alternative. Instead of building
everything, you build a first release that does something. Ideally,
something that creates the most value for potential users.

What's that first release? Presently, you don't have a formal,
testable specification. More work needs to be done to define a first
release. Formal and testable are pretty high barriers.

More important than details is this: there's a nasty circularity
issue. Until you build something, you don't know where the technical
roadblocks are. Once you build something... well... you've built
something. And you're going to be building something potentially
releasable merely to get to the point of being able to write a budget.

There's no way to know the budget without having started to build
something.

Once you start to build something, you did useful work in advance of
having a budget.

One (false) claim floating around the software development world is
that we can somehow do more research to resolve the unknowns before we
start actually building software. This is simply false. As we do
"research" we're doing high-level design: we're building software. You
may resolve a few unknowns, but there will be more.

The only way to know **all** the details about platform and the
application is to build the application using the platform. We don't
know anything until we're done building something that resolves some
unknowns.

Interestingly, the definition of "done" cannot possibly exist. We'll
return to the farcical nature of "done", below.

Worse, there's no way to know the budget without knowing the people
who will be doing the building.

**II. The Productivity Issue**

Until there's a relatively stable team, it's essentially impossible to
know how quickly programmers can build anything. And even then, there
can be unexpected, unforeseeable problems with the team.

Let me tediously pound this point home with an even more detailed
analysis. The point is to make it very clear that the future is
impossible to predict.

Let's say the first release is essentially a clone of an existing open
source project.

This is simple. What's the budget to clone the existing open source
project?

Choice 1. Find an unpaid intern. (This may no longer be legal, but
it's still popular.) Have them clone the repository, rebrand it, and
you have something running. How quickly can they do this? You don't
know until we meet the intern and watch them work. After they've
cloned the existing open source project you then know how long it will
take them. Until you've seen them work, you know nothing about the
time they'll require.

Choice 2. Find a kid still in school who knows the technology. Pay
them sub-minimimum wage to clone the package and rebrand it. How much
will you pay? You don't know until you meet the intern and watch them
work. After they've cloned the existing open source project, you'll
know how much it costs.

Choice 3. Make up a schedule based on what little is known. Put the
"clone the existing open source project"  out to bid on
`http://freelancer.com <http://freelancer.com/>`__ and hope that
others make bids that fit with your expectations. This is fixed price
so the budget is—in principle—known. In order to be sure you get
something high quality and usable, you'll need to write a lot of test
cases and very detailed specifications. Sadly, that pre-work is of
imponderable complexity. When you get bids that are too big, you learn
that your specifications weren't good enough; and you need to fix your
specifications to narrow the scope of work. Now you're doing much of
the work (spec writing and test case writing) in order to get a
proposal that includes your budget. Note the circularity where you're
doing some of the work to figure out the budget for the work you're
doing.

Choice 4. Offer someone a share in the company to clone the existing
open source project.  Now you don't have a budget at all. You merely
have a schedule. When will they be done? You're back to option 1, the
unpaid intern, except now with better incentives to be quick. But you
don't know how long they'll take until you've seen them do it once.

Choice 5. Offer someone an hourly rate plus a share in the company to
clone the existing open source project.  Now you're back to having a
budget, and perhaps it has an upper bound. You can pay up to some
amount, after that the share in the company is their incentive to get
something done.

I beat this point to death because there actually is no answer.  No
matter what strategy you choose, you still can't predict developer
productivity. It varies by a factor of at least 10 to 1. Some studies
show it varying by 100 to 1.

The idea of forecasting development costs is shameful lie created by
accountants. Really. The GAAP requires controls and budgets before
spending money and we're supposed to compare plan and actual. This is
all farcical in software world. Software development is like R&D: it's
structured learning and encoding the learning into software.

**III. The Done Issue**

One of the Great Lies is that software has a defined "done" state.
This only true for reductionist classroom exercises. Real software
grows, often without bounds.

"Wait," you say, "I have a vision of what I want, that defines a
boundary."

Today, that defines a boundary.

In six weeks, after two releases and some trouble support calls and
requests for new features, your original vision is out the window, and
you're off chasing the things your real users really are asking for.

Only in-house IT managers for large (dumb) companies stick to the
original plan in spite of all the lessons learned along the way.

Then you get partnership offers. And you see new platforms and tools,
and you get more user requests. The browser landscape changes. Tablets
become faster. Other changes that are impossible to imagine will
happen.

The vision will not be stable.

It won't even be finite.  A good business model grows and adapts and
expands.

**IV. Strategy 1: Estimate**

What can you do?

Clearly, you want some kind of budget for creating some kind of
software.

Clearly, there's no way to provide a good answer.

You can, however, find a farcical answer.

Step 1: find a developer who's willing to make a sincere commitment to
a cost and schedule.

Step 2: trust the sincerity of their commitment, even though it's is
absolutely going to be wrong. The Great Lie is that we might only
wrong by a factor of 2. In reality we can often be wrong by a factor
of 10: the $100,000 job turned out to cost over a million. (See above,
10:1 productivity is just one of the unknowns.) The million dollar job
was ill-advised and cancelled after the second release, but the users
were happy, so it was successful in many ways. But it was cancelled.

A sincere estimate is just a random number. However, many managers
find that the **sincerity** gives them comfort.

Since productivity is unknowable and "done" is unknowable, a detailed
estimate and plan means you must now spend a lot of time writing
"change orders" and reallocating the budget every time you learn
something new.

I'll repeat that.

When you have an estimate, all you do with it is reallocate the
estimated budget as you learn more about the customers, the
development team and the product. All you do is reallocate; the idea
that there's "plan" which is compared with "actual" is farcical
because the plan changes constantly. So constantly as to be
meaningless.

    [Accountants will claim that this is analysis wrong because the future
    is somehow knowable. I can only stare dumbfounded at them. The future
    is knowable? Really? They'll say that a plan is a commitment and
    comparing actual to plan somehow makes sense. They'll give all kinds
    of weird analogies that don't apply to software. Software development
    is not a "production" task like brick laying or making pins from wire.
    If the future was knowable, the project ROI would be a fixed 150% or
    300% or, well anything. Oh. Right. Somethings **are** unknowable. Like
    the future. Ahem.]

**V. Strategy 2: Agile**

The very best you can do—indeed, the only rational thing you can do—is
to locate talent who are willing to work for an indefinite period of
time.

A person or people you trust.

You establish a release cycle. Two or three weeks are typical sprint
cycle times. two weeks works well for very new development. Three
weeks is better for more established teams.

You identify the first three or so releases by writing those
high-priority, high-value user stories as carefully as you can.
Testable, finite user stories. Clear boundaries on acceptable vs.
unacceptable behavior. Too few user stories makes it difficult to
foresee the future. Too many user stories can be needless preliminary
work since they're going to change anyway.

You do Scrum development with a two-week cycle.
http://www.ambysoft.com/essays/agileLifecycle.html

"Useless," you say, "because there's no overall budget!"

Correct. There's no overall budget. You don't (and shouldn't) have a
legally-binding definition of "done". Done means "business death." You
have a vision for the first release. From that you'll make enough
money to get to the second release. Which gets you to the third
release. You're not done until you're out of ideas and no one wants
your product anymore.

Done should always be defined as "planned release [X] is the last
release." After that, it's donate the intellectual property into the
public domain and move on to something profitable.

"Then logically," you say, "There can be a budget for the **first**
release."

Except, as noted above, you don't know how productive the team is. So
there's no useful budget for even the first release. Ideally, 1 sprint
= 1 release. But. Until you know the team, and the user stories, and
the platform, and the application, you can't assume that.

Which gets us to this:

    The budget is only enough to get you through the next two-week sprint.
    A three-person team for two weeks is 240 hours. $50/hr. $12,000 per
    sprint. Perhaps with a larger team, it may be $20,000.

Each sprint must produce something releasable or everyone is fired.
It's that crisp. The company is out of business—as currently
organized—when the team can't create something releasable. Either the
user stories aren't testable or the sprint planning is too ambitious.
Or someone lacks the skills they were thought to have during the
interview process. Or something is wrong with the team chemistry.

Sometimes, a sprint's work product is not deployed for marketing
purposes. It's saved up into the next sprint so that the monthly
release is far cooler than the bi-weekly release.

I'm aware that this is an unsatisfying answer. It's nice to hope that
software development is a finite, linear process with just minor bumps
in the road. Sadly, it's not. It's a completely out-of-control process
that hurtles down the wave fronts making progress in a reasonably
desirable direction in spite of currents, winds and weather. It's (by
definition) a **learning** process. As knowledge is accumulated, it's
encoded in the form of software. Once all the knowledge is available,
the software happens to be done, also.

Also: http://slott-softwarearchitect.blogspot.com/2011/11/justification-of-project-staffing.html.

And this: http://slott-softwarearchitect.blogspot.com/2010/03/great-lies-design-vs-construction.html.

This, too: http://slott-softwarearchitect.blogspot.com/2009/11/on-risk-and-estimating-and-agile.html.

Okay, fine: http://slott-softwarearchitect.blogspot.com/2009/10/breaking-into-agile.html.



-----

Wonderful post. Love it.
------------------------

Rick Jones<noreply@blogger.com>

2013-06-27 08:04:13.514000-04:00

Wonderful post. Love it.


I disagree with your assertion that Scrum means th...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2013-06-27 17:51:12.435000-04:00

I disagree with your assertion that Scrum means the "Formal Scrum-fall"
version of waterfall. I don't know how I can make this more clear
without adding absurd statements. Why did you assert that I was talking
about a rigid, formal, useless version of Scrum? What could I have said
differently to alert you?


You're conflating a lack of premature analysis...
-----------------------------------------------------

Michael Barnathan<noreply@blogger.com>

2013-06-27 16:07:28.305000-04:00

You're conflating a lack of premature analysis (good) with Scrum (not so
good).

The first thing you do in Scrum is try to estimate how long tasks will
take you and how many you can take in for the next sprint (i.e. the
planning meeting). In my experience in the software industry, which is
extensive, these meetings tend to end in failure and frustration for
precisely the reasons you outlined above - no one can accurately
estimate the sprint beforehand.

A good Scrum team will move on and say "we don't know yet, let's just
get started and do everything we can in that time period", and basically
end the first planning meeting right there. Of course, at that point,
they're not using Scrum anymore. A bad one will waste up to 2 hours in
the planning meeting jumping wildly at estimates, then will run into
problems 3/4 of the way into the sprint: either they'll feel depressed
because they can't get all of it done or they'll run out of work and
start twiddling their thumbs. If you're lucky, they'll rush something
with a bunch of "temporary hacks" out the door so they can say they
delivered something, as there is a dire incentive to release. Next
sprint, the product owner will give them more work and those "temporary"
hacks will become permanent. And the whole cycle will repeat again and
again.

This process killed one of the companies that I worked at, and they had
a very good development team.

The spirit of getting something done before trying to budget is correct
- I just don't think your vision of using formal "Agile" methods will
get you there. I've seen a lot of places implement Scrum - the most
successful ones were the ones who removed process liberally. Just "ship
early, ship often" and you can make do without tons of bureaucracy.

In fact, you'll find that a good team functions best with less process
rather than more. Good teams self-organize to a much greater extent, and
bureaucracy just gets in their way of doing that. We used something very
close to waterfall at Google, and the people there were such mature
developers that it worked brilliantly. Scrum would have just slowed us
down.

If you want the insight without the issues of a synchronous process, use
Kanban. Continuous flow processes are much friendlier to developers and
don't require excessive analysis to get started.


Speaking of Agile software development life cycle,...
-----------------------------------------------------

Maryna<noreply@blogger.com>

2022-02-16 09:10:40.053000-05:00

Speaking of Agile software development life cycle, here is a really
useful `article <https://www.cleveroad.com/blog/agile-sdlc>`__ about
this.





