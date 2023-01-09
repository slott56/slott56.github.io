Architecture Change: Breaking Conway's Law
==========================================

:date: 2010-03-23 10:16
:tags: software process improvement,architecture,conway's law
:slug: 2010_03_23-architecture_change_breaking_conways_law
:category: Technologies
:status: published

In `Architecture Change: Recognizing Conway's
Law <{filename}/blog/2010/03/2010_03_22-architecture_change_recognizing_conways_law.rst>`__
we looked at the profound influence Conway's Law has on architecture.

Recently I've looked at two gutsy declarations that an architecture
was broken. One recognized that a three-tiered architecture was too
complex for their needs. The other recognized that the Ontology tools
weren't performing well, and perhaps weren't helping.

My point is that these architectural mistakes are the result of
Conway's Law. They aren't inherently flawed.

**The Root Cause**

What's flawed is **not** the architecture. What's flawed is the
organization that built the architecture.

A three-tiered architecture is workable. In some cases, it's
necessary. In other cases it could be overkill. But it isn't the
cause of the problems.

An Ontology is often a good thing. However, using the ontology to
represent what is -- essentially -- a **Star Schema** fact table is
poor use of the technology.

Declaring the architecture broken is not a technical statement. It'
an organizational statement. It says that the organization, the
teams, the areas of responsibility are broken.

    **Rule 1: A Broken Architecture Is A Broken Organization**

**Complexity**

One can try to make a distinction between *Essential Complexity* and
*Accidental Complexity*. One can claim that essential complexity is
part of the solution and accidental complexity is just other staff
that accretes. This doesn't make any sense, since software
development is not "accidental". Software doesn't "happen". It's hard
to call something "accidental complexity" without saying that
software involves random accidents. Blaming "accidental" complexity
is a dodge, an attempt to obscure the root cause.

One might call it incidental or tangential complexity. But that still
hides the fundamental problem.

To be more honest, one must separate Problem Complexity from Solution
Complexity. The Problem Domain may be inherently complex. In which
case, simplification is hard and 2 tiers, 3 tiers or N tiers don't
matter. The problem itself is hard, no matter what architecture is
chosen.

An ontology, for example, is very helpful when the problem itself is
inherently hard. The formalization of relationships in an ontology
can help beat a path through a tangled problem domain.

In most cases of a broken architecture, the solution is has grown out
of scale with the problem's inherent complexity. If we're doing
actuarial risk analysis, we don't really need an ontological model of
"Risk": we need facts that help us measure the risk factors.

    **Rule 2: A Broken Architecture Means the Solution Doesn't Fit the Problem**

    **Corollary: The Organization Doesn't Fit the Problem**

**Kinds of Broken**

Why would we declare an architecture broken? Generally, we've got a
grotesque failure due to the very structure of the solution. These
can be decomposed into five areas.

-   Failure to satisfy the need; i.e., the software doesn't have the
    required functions or features.

-   Failure to use resources effectively; i.e., the software is slow,
    uses too much disk or too much network traffic.

-   Failure to be maintainable; i.e., bugs cannot be fixed.

-   Failure to be adaptable; i.e., new features cannot be added.

-   Failure to fit other organizational needs (cost, licensing, etc.);
    i.e., it's too expensive.

The two broken architectures I've heard about recently have
different problems. One is unacceptably slow (as well as hard to
adapt). The other is described by some as impossible to maintain
and adapt.

    **Rule 3: All Architectural Problems Are Symptoms of Organizational Problems**

In short, a broken architecture is not a simple technical problem
and it doesn't have a simple technical solution. It's an
organizational problem, and it has a multi-part solution.

**Making Progress**

It's important to acknowledge that Conway's Law, like Mutual
Attraction and Thermodynamics is a feature of the universe. It
cannot be "broken" or even "subverted". You cannot win, you cannot
break even, you cannot quit the game.

    **Axiom: Conway's Law Cannot Be Broken.**

Given that Conway's Law is like Thermodynamics, you have to work
with it.

    **Conclusion: Architecture Must Drive Organization; Problem Must Drive Architecture**

The only way to make progress is to restart the project at a
fundamental level. You have to -- effectively -- fire everyone and
rehire then to create brand-new team. The broken architecture came
from a broken organization. To fix the architecture, you need to
fix the organization.

**Example #1, Unmaintainable Stored Procedures**

Consider an application with stored procedures (SP) so badly
broken as to be unmaintainable. Let's say it's many hundreds of
lines of code. A Cyclomatic Complexity so high as to be laughable.
Clearly, the folks responsible for building this need to be
reassigned and new folks need to be brought in. If the new folks
are simply assigned to the same old separate SP/DBA group, then a
new unmaintainable mess will eventually replace the existing
unmaintainable mess.

Conway's Law applies: If the SP developers are separate, they will
evolve in their own direction. If you want to have a "technical"
reason for SP's, then you have to prove that they're more
effective than a non-SP implementation. That means spike solutions
to compare SP's and your other application programming languages
point-by-point.

To prevent stored procedures from getting out of control there are
two choices.

#.  Don't use stored procedures. Put that logic in with the rest of
    the application, where it belongs. Same code base, not a
    separate language buried in the database. One team, one
    language.

#.  Don't make stored procedure writing a separate "team". The
    stored procedure writing must be part of application writing.
    One team, multiple languages.

Note that choice #2 leaves it to the team to use stored
procedures if they have a provable improvement on performance.
Things are not handed over to the DBA's because SP's must do
all database interface or SP's must maintain "low-level" rules
or other blurry lines. Things are not handed to the DBA's --
the team solves the problem.

**Example #2, Too Many Tiers**

Consider an architecture with too many tiers. The inter-tier
communication is blamed as creating "accidental complexity".
This is a dodge. The coordination between teams is what creates
complexity.

To prevent inter-tier communication from being a problem, one
doesn't need to remove tiers. One needs to remove
organizational structure. There's really only one choice.

    **Fail: Team Follows Technology**

    **Win: Team Follows Features**

For a given feature set, everyone involved has to become part
of one, unified team working one one sprint attending one daily
stand-up meeting.

"But that's unwieldy," you say. "DBA's have to be kept
separate."

That's Conways' Law in action.

To work *with* Conway's Law, you must create a team that owns
the feature set -- all tiers -- all technologies -- and can
make all the implementation choices required to bring that
feature set to the users.

**Example #3, Overuse of Ontology**

Consider an inappropriate use of an Ontology where a Database
would have been a better choice.

#.  Remove the old team. Assign them to hard problems where the
    ontology pays dividends, get them away from easy problems
    where the ontology is a solution looking for a problem.

#.  Create a new team around the new solution. Each feature has
    a team that has a complete skill set -- front-end, bulk
    processing, persistence, web server, database, network --
    everything.

#.  The new team stands alone and builds the solution.

**Excuses Excuses**

The number one cultural impediment is the "Skill Focus"
excuse. These are just Conway's Law in action.

-   "We can't have application programmers doing database
    design. They might 'mess things up'."

-   "We don't want our DBA's assigned to application
    development teams. They have operational responsibilities
    that trump new development."

The number two cultural impediment is the authorization
excuse. These are also Conway's Law, wrapped in the mantel
of "security".

-   "We can't allow application developers sudo privileges to
    configure Apache (or MySQL, or Oracle, or -- frankly --
    anything.)"

-   "We can't assign a DBA or SysAdmin or anyone to support
    new development..."

**Conclusion**

Stop organizing teams by skills.

Start organizing teams by deliverable.

Stop carving out random technology features without proof
that the technology solves a problem. Stored Procedures,
Middle Tiers, Ontologies are just *potential* solutions.
Don't commit to them until they're proven.

Start creating spike solutions to measure the value of a
technology. If a spike solution doesn't work, stop
development, change the plans, change the schedule and
start again based on the lessons learned.

Stop forcing a deadline-driven death march.

Start learning technology lessons and making project
changes based on what was learned.



-----

A lot of these points definitely resonate, but the...
-----------------------------------------------------

Shekhar Vemuri<noreply@blogger.com>

2012-05-16 22:37:21.044000-04:00

A lot of these points definitely resonate, but there is something to be
said about having teams around skills, where people with similar skill
sets are able to work together to improve upon what they do and bring
around better ways of solving problems. this gets diluted when the focus
is just around deliverables. also on a larger scale each of these
individual teams then start making choices which makes the landscape
more and more diverse than what it should be.

I am not refuting the point around having cross functional scrum teams
together who own the solution end to end, i want to add to it by saying,
that there should also be virtual teams that allow people like DBAs or
QA personnel, release folks, sys admins go back to to hone their skills
to form a strategy and vision to solve the problems they run into in
each scrum team and avoid reinventing the wheel evertyime a team runs
into it.





