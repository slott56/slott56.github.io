How to Derail Use Case Analysis: Focus on the Processes
=======================================================

:date: 2009-06-14 15:14
:tags: analysis,use case
:slug: 2009_06_14-how_to_derail_use_case_analysis_focus_on_the_processes
:category: Technologies
:status: published

It's easy to prevent successful use case analysis: make it into an
exercise of defining lots of "processes" in excruciating detail.

First, ignore all "objects" definition.  All business domain entities
-- and actors -- must be treating as second class artifacts.

Second, define everything as a process.  A domain entity is just some
stuff that must be mapped between processes.  Act like the entity
doesn't really have independent existence.

Symptoms
--------

You may be trying to do use case analysis, but if you have these
symptoms, it might be time to step away from the process flows and
ask what you're really doing.

**There Are No Actors**.  Well, actually, there's one actor: "user".
When all of your use cases have one actor, you've forgotten the
users and their goals.  Stop writing the processes and take a step
back.  Who are the users?  What are they trying to accomplish?
Where is their data?  When is it available?  What interactions
with a system would make them happier and more productive?

**Every Action Defines A New Class of Actors**.  You have actors like
content creators, content updater, content quality assurance,
content refinement, content link checking, do this and do that.
Too many actors is easy to spot because the attributes and
behaviors of all those actors are essentially identical.  In this
example, they all edit content.

**Each Use Case is a Wizard**.  If each use case is a strictly
sequential input of a data element followed by "click next to
continue", you've taken away the actor's obligation to make
decisions and take action on those decisions.  If you're lucky,
you've got a use case for each individual goal the actor has.
More typically, you've overlooked a fair number of the actor's
goals in your zeal of automating every step of one goal.

**You Need an "Overall Flow" or Sequence for the Use Cases**.   If
your use cases have to be exercised in one -- and only one --
order, you've taken away the actor's goals

Collaboration
-------------

Use Case analysis describes the collaboration between actors and a
system to create something of value.  If the system is described
by wizards or modal dialogs that completely constrain the
conversation to one where the system asks the actor for
information, something's terribly wrong.

The point is to describe the system as a series of "interfaces",
each of which has a use case.  The actors interact with the system
through those interfaces.    The actor is free to gather
information from the system, make decisions, and take action via
the system.

War Story
---------

The users had a legacy "application" that was a pile of SAS code
that did some processing on the source data before reporting.

The use cases were -- essentially -- "1.  Actor runs this program
2. System does all this stuff."  The "all this stuff" was usually
a lengthy, complex reverse engineering exercise trying to discern
what the SAS code did.

No mention of the business value.  No reason why.  And no room to
implement a better process.

War Story
---------

Analyst is pretty sure the user wants collaborative editing.  The
analyst has a pretty good "epic" (not a proper user story, but a
summary of a number of user stories) that describes creating,
modifying and extracting from a collaboratively edited document.

The initial discussion lead to every single verb somehow defining
a separate actor.  In the original epic, there were exactly two
actors, one who added or elided certain details for the benefit of
another.

Later discussions lead to a single "User" actor and the craziest
patchwork of use cases.  Random "might be nice to have"s crept in
to the analysis, and the original "epic" was dropped.  No trace of
it remained, making it very difficult to determine priorities.

War Story
---------

Users had developed a complex work-around because they didn't have
all the equipment they needed in their local office.  It involved
mailing CD's from one office to another to prevent network
bandwidth problems.  The business analysts wanted to capture this
process, even though parts of it created no value.

It took a fair amount of work to get the analysts to stop
documenting implementation details (mailing addresses, Fedex
account numbers) and start documenting interactions and the
business value that was created.

Many process steps are physical moves and don't involve making
information available for decision-making.  Those no-decision
physical move steps should not be described in a use case.
Perhaps in an appendix, but their incidental because they're just
the current implementation.  A use case should have the essence of
the business value and how the actor uses the system to create
that value.





