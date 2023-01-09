Fighting Against Over-Engineering
=================================

:date: 2022-11-08 16:18
:tags: design,architecture,methodology
:slug: 2022_11_08-fighting_against_over_engineering
:category: Technologies
:status: published

I've been trying to help some folks who have a "search" algorithm that's
slow.

They know it's slow -- that's pretty obvious.

They're -- unfortunately -- **sure** that asyncio will help. That's not
an obvious conclusion. It involves no useful research. Indeed, that's a
kind of magical thinking. Which leads me to consider the process of
over-engineering.

The Problem
-----------

Over-engineering is essentially a technique for burning brain-calories
on planning to build something instead of building something.

The distinction is "planning" vs. "doing."

Lots of folks subscribe to Methodology Magic Thinking (MMT™). The core
tenet of MMT is that some  methodology is good, and more methodology is
better.

The classic waterfall methodology expects requirements, design, code,
test, and what-not, all flowing downhill. A series of waterfalls.

The more modern agile-fall methodology expects requirements, design,
code, test, and what-not all being done in tiny MVP slices.

Why is this bad?

Its bad because it falls apart when confronted with really difficult
algorithm and data structure problems.

What Breaks?
------------

The thing that breaks is the "learn about the technology" or "learn
about the problem domain" things that we need to do. We like to pretend
with understand the technology -- in spite of the obvious information
that we're rarely **experts**. We're smart. We're capable. But. We're
not **experts**.

This applies to both the solution technology (i.e., language,
persistence, framework, etc.) and the problem domain.

When we have a process that takes \*forever\* to run, we've got a bad
algorithm/data structure, and we don't know what to do.

We need to explore.

And.

Managers rarely permit exploration.

They have a schedule. The waterfall comes with a schedule. The agilefall
sprints have timelines. And these are rarely negotiable.

What Are Some Wrong Things to Do?
---------------------------------

One wrong thing to do is to pick some technology and dig in hard. The
asyncio module is not magical pixie dust. It doesn't make arbitrary bad
code run faster. This is true in general. Picking a solution technology
isn't right. Exploring alternatives -- emphasis on the plural -- is
essential.

Another wrong thing to do is demand yet more process. More design docs.
More preliminary analysis docs. More preliminary study. More
over-engineering.

This is unhelpful. There are too many intellectual vacuums. And nature
abhors a vacuum. So random ideas get sucked in. Some expertise in the
language/tool/framework is required. Some expertise in the problem
domain is required. Avoid assumptions.

What Should We Do?
------------------

We have to step back from the technology trap. We're not **experts**: we
need to learn more. Which means exploring more. Which means putting time
in the schedule for this.

We have to understand the problem domain better. We're not **experts**:
we need to learn more. Which means putting time in the schedule for
this.

We have to step back from the "deliverable code" trap. Each line of code
is not a precious gift from some eternal god of code. It's an idea. And
since the thing doesn't run well, it's provably a **bad** idea.

Code needs to be deleted. And rewritten. And rewritten again. And
benchmarked.

Frustration
-----------

I like fixing bad code. I like helping people fix bad code.

I can't -- however -- work with folks who can't delete the old bad code.

It's unfortunate when they reach out and then block progress with a
number of constraints that amount to "We can't focus on this; we can't
make changes rapidly. Indeed, we're unlikely to make any changes."

The only way to learn is to become an expert is something. This takes
time. To minimize the time means work with focus and work rapidly.

Instead of working rapidly, they want magical pixie dust that makes
things faster. They want me to tell them were the "Turbo Boost" button
is hidden.

Sigh.





