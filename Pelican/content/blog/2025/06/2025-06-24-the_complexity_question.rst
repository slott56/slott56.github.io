The Complexity Question
############################

:date: 2025-06-24 09:59
:tags: solid,complexity,complication,chaos
:slug: 2025-06-24-the_complexity_question
:category: Architecture & Design
:status: draft

I was pointed at the Cynefin® Framework for understanding complexity.
It's a trademark, and a product, and books, and consulting services.
I can't say too much because I don't understand it very well, and haven't paid them any money.

But.

The idea that it's based on is elegant

    Complex and Complicated are different.
    Complicated often has right answers; there are governing constraints.
    Complex is less constrained and rarely has right answers.

BLUF (TL;DR)
=============

I'm not sure this Complex/Complicated distinction is wonderfully helpful.

    "If you should stand, then who's to guide you;
    If I knew the way, I would take you home."

    -- "Ripple", Grateful Dead

You often don't know where you are.
You might be trying to understand something Complicated, with a simplification hidden inside it.
Or, you might be confronting something Complex, but you've over-simplified and mis-understood it.

There seem to be two aspects of interest:

-   Scale -- large systems with many independent parts can tend to Complex with fewer clear constraints.
    With some deeper understanding it may shift to being Clear (or Simple.)

-   Predictability -- Systems with essentially non-deterministic behaviors can be Complex or even Chaotic.
    In retrospect, they can can be summarized into something Complicated or perhaps even Clear.

There's no absolute metric, however.
These are relative to your current degree of understanding, and will shift as you invest effort.
A small problem may -- at first -- be intractably Complex.
But as you dig in, you may find it's merely Complicated.

I don't know how the distinction helps someone make architectural or design decisions.

At best, it seems like it's possibly helpful terminology to justify more time spent learning, and less time spent coding.

Navigation
==========

I used to live on a sailboat. Boats need water.
Sailboats tend to need deep water.
For my boat, it was about 2m depth, minimum, or we'd be in catastrophic trouble.

What's essential is understand the contour of the bottom.
Far enough off shore and the ocean is deep and shoals are rare.
In the coastal waters of the US, they're often meticulously marked with buoys or day-marks.
For "navigable" waters, the shoals are on the charts, clearly marked.
The depths can be marked to the nearest foot (30cm) against an well-defined tidal state (called "Mean Low Low Water").

Which raises the question of "navigable."
I'm pretty sure the Army Corps of Engineers (ACOE) has a crisp, useful definition of the waters
they consider navigable; I don't know what it is, though.
Pragmatically, it's the places commercial shipping can take operate.

We knew when we went too far up a river we'd find the marks starting to thin out.

Creeks and rivers without marks were a risk.

My kind of recreational boating was not wilderness exploration.
I didn't need to push the edge of the envelope to boldly go where no person had gone before.
Nor was I licensed commercial operator with paying customers.
I didn't have to stick to well-charted, know-to-be-safe commercial waterways.

How does one navigate the unknown?
How do we avoid complication?
How do we manage complications or even complexity where we may find some underlying simplicity behind it?

Charted Hazards in Software Development
=======================================

In class-room situations -- and training videos -- and blog posts -- and books --
the problems are well-understood.

A classic from my youth was implementing the Dijkstra algorithm find the shortest path between nodes in a graph.

There are several well-known complications.
A non-Dijkstra algorithm risks :math:`\textbf{O}({\lvert V \rvert}^2)` performance problems.
Use of a priority queue reduces the search time for this path considerably.

What's important is that the shallows are charted.
Known.

Further, programming languages are constructed.
With few exceptions (looking at you, **PERL**) languages are rarely complicated.
There may be complicated constructs available, but they're built from intellectually-manageable pieces and parts.

Even large, sophisticated libraries and frameworks often have elegant patterns.
It may take a while to get past the complications to understand the underlying simplicity.
But with the exception of **matplotlib**, there's rarely any baffling complexity.

Real-world problem domains are where we see real hard-to-handle complexity.

Unknowns
========

We didn't sail casually into uncharted waters.
We only did it after spending some time looking around.
We'd ask other sailors for recommendations.

When approaching, we'd use all of the instruments at our disposal:
binoculars, examination of the color of the water and the shapes of thw waves,
the lay of the land, and -- really important -- if other boats like our were there.
We tried to stay in the places where we could see large, ketch-rigged sailboats.
It meant the water was deep enough.

When anchoring, it's particularly important to anchor near similarly-configured boats.
When the winds and the currents shift, you want to be shifting with a peer group.
We were happiest when all the boats were pointing the same way, with safe spaces between them.

With programming languages, libraries, and frameworks, you can observe how others do things.
You can follow good examples and avoid known problems.
Open-source makes this much easier than it once was, decades ago.
There will be unknowns -- opportunities to learn -- but the risks are manageable.

(In some enterprise software development environments, there can be a needless focus
on schedule, and the time required to learn something new is often treated as time lost.
That's bad management.)

Sailling in uncharted water seems to fit the model's sense of Complicated.
While a location is novel, the novelty wears off quickly.
There are best practices that work.

Unknowables
===========

Foul weather is a profound unknown. That is -- after all -- why we call it "foul".

Unlike a cool anchorage just up the river a bit, foul weather happens no matter what your plans were.

Modern weather forecasting makes it possible to avoid a lot of bad weather.
But sometimes, we were still caught in a storm we couldn't avoid.
The sea state and the wind were unknowable: there was no way to ask for advice or proceed slowly.

What's left is trying to manage the situation we find ourselves in.
It's a moment-by-moment operation.
Weather seems to be essentially complicated.
It appears to be more than merely merely poorly-constrained and Complex.
Indeed, it may transcend Complex into Chaos.

While weather can be summarized and abstracted into patterns that make it simple, this seems to be only possible when eliding a lot of details.
Statistical summaries of climate data, for example, are simple and clearly reveal catastrophic problems.
People who profit from climate destruction deny the facts by manufacturing unknowable complexities.

A specific storm, however, battering our boat right now cannot be brushed off as some complicated situation that has an underlying order and clear best practices.
Holding a course, or holding a position, can be quite challenging.

Is weather really best described as Complex with few constraints?

Or, is it my inexperience with foul weather that makes me claim it's Complex?
People do learn to cope with bad weather.
Or is possible to master it, reducing it to a buddle of complications?

How Do You Know Where You Are?
==============================

What I'm hinting at is this: our perspectives shift.

There are trajectories in our understanding.

The boundaries between Complex and Complicated can be subjective and fluctuate.

For example, something like sailing can seems Clear: wind, water, sail, and keel.
The boat moves.
Then we learn a little more about sail trim and optimizing our performance and it seems to be deeply Complex.
Then we learn even more and we realize it's only Complicated, and the Complications can be managed.

Or.

Weather seems Complex at first until we have strategies to cope with the Complications.
Storm fronts, and sea state, and how the boat -- and the crew -- respond to changing conditions begin to form sensible patterns.
Then -- through experience, and summaries of lessons learned, and abstraction -- we can make it simple again.

An essentially chaotic system is another kind of thing.
Randomness (or really, unpredictability) is part of the system.
Only retrospective analysis using aggregated statistical summaries are possible.
Sometimes, there are rules or patterns, and predictions with error bars around them are possible.
But chaos seems to preclude any sort of certainty.

Things invented by people can be -- and often are -- Complicated.
Sometimes enough participants can make things devolve into Complex.
And when there's not enough coordination, things can devolve into Chaos.

Pushing the Envelope
====================

We can make something as simple as pottering around in a sailboat for an afternoon into something more complicated by trying to live on the boat and cover huge distances.
The system doesn't change much, but our involvement forces a change in our understanding.

But, what's the actionable result of characterizing living on a sailboat as Complicated vs. Complex?

If we're finding it Complex, perhaps, we invest more time in learning and planning.

If we're finding it Complicated, perhaps, we invest less time in learning and planning.

If that's the material impact of the distinction, then it's not a profoundly distinct type of thing.
It's a degree of confusion.

-   Complex? Few constrains, more confusion, more analysis and study time required, every action is risky.

-   Complicated? More constraints, Less confusion, less analysis and study time required, fewer action are risky.

-   Clear? Minimal confusion, no analysis time required, very few actions involve novel or unknown risks.

I think this is what the framework's good for: naming the degree of confusion.
