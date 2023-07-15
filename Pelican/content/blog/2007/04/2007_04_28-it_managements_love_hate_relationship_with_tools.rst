IT Management's Love-Hate Relationship with Tools
=================================================

:date: 2007-04-28 13:04
:tags: architecture,software design,management
:slug: 2007_04_28-it_managements_love_hate_relationship_with_tools
:category: Architecture & Design
:status: published





Mr. Hayes says that "...we’re afraid that
programmers simply won’t use the hot new technology and that the money we
spend on it will be wasted."  He plays up this fear factor, providing lots of
programmer-centric reasons: "Either programmers don’t use the tools at
all, or they use them half-heartedly, or they find reasons to subvert them,
..."



He even provides a plausible
logical contradiction: "But programmers won’t waste their time trying a
new approach unless they really believe it’s better than what
they’re already using. And they won’t believe it’s better
until they’ve given it an honest, committed try. But they’re not
going to waste their time doing that unless they already
believe."



This is mostly false.  The
consequences are true.  The logical conundrum is largely
true.



Here's the real answer:  It's Not
Programmers; It's Their
Managers.



**Managers Buy Tools And Subvert Their Use.** 



How do
managers subvert tool use?  Let me enumerate the
ways.



Here's the root cause: 
**All software development is project-centered, deadline driven, with fantasy budgets.** 



This root cause leads managers to
deprecate tool use in every possible way.  Let's say we're considering
Application Portfolio Management to automate code inspections.  Subversion One:
there's no time, no budget and no staff to install, configure, develop standards
or train.  Subversion Two: once the project gets close to delivery, the tool use
is rejected with the magic phrase "our customers expect on-time delivery, they
don't expect code inspections" (or source-code control, CASE diagrams, or
requirements repository or whatever the tool does.) 




The consequence is that management
eventually sets the tool aside.  They stop asking for the code inspection
results, the source-code check-in reports, the CASE diagram reviews or the
requirements summaries.  They fall back to "is it running?" kind of management,
bypassing all testing, configuration control, code standards, design patterns or
requirements clarity.  If it isn't running right now, they demand immediate
patching and subversion of all disciplined effort or tool
use.



**Project-Centrism.** 



Since
there is a project, and the project is the only goal, tools are a distraction. 
While they might help, every manager is deeply suspicious of anything which
differs from the previous project.  Therefore, the following conversation is
standard.

Manager:  "Is it done
yet?"

Programmer:
"No."

Manager:  "What's the hold up?  Let's
stop using the APM and go back to the way we used to do
it."

Programmer:
"What?"

Manager: "Tools are out of scope for
this project.  Stop using
them."



Management's short-sighted,
narrow project focus tends to subvert tool
use.



**Deadline Driven.** 



Since there is a deadline,
there is no time for tool training.  Nor is there time for rework or
improvements.  We must -- from thin air -- develop a strategy for using the tool
and implement that strategy with no budget or schedule of any
kind.



Since each software product is
unique, each project is unique.  (Yes, each product is unique; it if wasn't
unique you'd either buy something or download something.)  Since each project is
unique, the team organization, workflow and tool use will be unique. 
Introducing new tools on top of new requirements and a new team is too many
unknowns.  To mitigate schedule risk, we must replace unknowns with
knowns.



Faced with a looming deadline,
a late start, mushy requirements, and no available resources, training is
eliminated.  Prototyping, proof-of-concept and pilot projects to understand the
tooling are eliminated.  The main deliverable project is both pilot and final
deployment for the toolset.



Any delays
in tool use are delays in the project as a whole.  Therefore, management will be
very clear that deliverable deadlines preclude use of
tools.



**Fantasy Budgets.** 



The ROI is a lie to
justify the project.  The project costs are a lie to make a respectable ROI. 
Everyone does this for every project.  Managers ask the programmers how long it
will take.  Then the manager repeats the magic phrase "I don't want a
gold-plated Bentley, I just want a solid, reliable Trabant."  Then the
programmers reduce the schedule to fit the manager's fantasy price.  The scope
can't change, the effort can't change, so the schedule and budget shouldn't
change.  Managers demand that the programmers change the price without changing
the scope.  



Small wonder that many
projects run over budget and under-deliver on
features.



More importantly, the lack of
budget realism means that tools, tool training, and tool pilot projects cannot
be funded.  The only path left is for programmers to attempt on-the-job training
by playing with the tools.  When it turns out that critical modules were not
purchased (they were too expensive) then the budget crunch means that they
cannot ever be purchased.  This project can't afford them and the lack of
resounding success means no future project will ever use this tool set
again.



**Agreement.** 



Here's
how I know I'm right.  I ask for budget, schedule and a pilot project to
introduce a new tools.  Managers say that my fantasy realm of tool introduction
isn't realistic.  In the real world all projects are narrowly scoped, tightly
budgeted and have a fixed deadline.  They claim that budget, schedule and a
pilot project are "unrealistic" or "impossible" and I need to fold in new tools
in a way that doesn't require money, time or scope
changes.



**Conclusion.** 



Tool
use makes programmers more effective.  Tool use requires three
things:

1.  Purchasing the tools in the first
    place.

#.  Paying for and scheduling training in tool
    use.

#.  Paying for and scheduling a pilot project for
    tool use that is not constrained by other
    projects.



Lacking these three things,
software tools cannot be used in big IT shops.  It isn't fear that prevents tool
use.  It's management.










