Agility and following a "Strictly Agile" approach
=================================================

:date: 2011-05-24 08:00
:tags: software process improvement,waterfall,scrum,agile
:slug: 2011_05_24-agility_and_following_a_strictly_agile_approach
:category: Management
:status: published

I've seen some discussion on Stack Overflow that is best characterized
by the question: "What is Strictly Agile?", or "What's the Official
Agile Approach?".

Someone shared this with me recently: "`Process kills developer
passion <http://radar.oreilly.com/2011/05/process-kills-developer-passion.html>`__".

I have also heard some great complaints about organizations that
claim "Agile" and actually do nothing of the kind. In some cases it's
not a "crunchy agile shell" around a waterfall process; it's a simple
lie. Nothing about the process is Agile except a manager insisting
that all the status reporting, planning and unprioritized lists of
random requirements are Agile.

Finally, I got this weird suggestion: "consider writing a blog about
how to test if you are agile or not". It's weird because testing for
Agile is like testing for breathing; it's like testing for
flammability.

The Agile Test
--------------

Testing if your project is Agile can be done two ways.

#.  **Practical**. Make a change to the project. Any change.
    Requirements, architecture, due dates, staff, *anything*. Does it
    derail? If so, it wasn't very Agile, was it?

#.  **Theoretical**. Reread the `Agile
    Manifesto <http://agilemanifesto.org/>`__. Make a score card that
    evaluates the project on each of the eight basic criteria in the
    Agile manifesto. Convene all the project stakeholders. Conduct
    careful surveys and have structured walkthroughs to determine the
    degree of Agility surrounding each person, deliverable,
    collaborative relationship and issue.

An important point is that Agile is not absolute. Some practices
are more Agile than others. There's no "strictly" Agile. There are
ways to make a project more Agile; that is, it can effectively
cope with change. There are ways to make a project less Agile;
that is, change causes problems and can derail the project
completely.

The canonical example is a missing, misstated or contradictory
requirement that gets uncovered after coding and during user
acceptance test. Clearly, that feature has been built and is
absolutely wrong. What happens next?

Agile? The product can be released with with the broken feature
relegated to the next release. A hack is put in to remove the
buttons or menu items or links until they work.

Not Agile? Everyone works around the clock to make that feature
work no matter what. Paraphrasing Admiral Farragut: "Technical
debt be damned. Development must proceedfull speed ahead." All of
this irrespective of the relative value of what's being developed.
Schedule comes first; features second.

How Much Process?
-----------------

The "Process Kills..." blog entry repeats observation that a lot of
carefully-defined process isn't really all that helpful. It
identifies a cause ("process kills passion") that's can be true, but
it's largely irrelevant. Process is—essentially—work that's not
focused on delivering anything of real value. Complex processes are
"meta" work; it's work focused on IT internals; it's work that
creates no value for the users of the software; work that replaces
the more valuable elements of the Agile Manifesto.

One can argue that processes, documentation, contracts and plans
"assure" success or demonstrate some level of quality. To an extent
all the process and meta-work creates trust that—eventually—the
resulting software product will solve the original problem.

The mistake is that non-Agile methods use a series of
surrogates—processes, documentation, contracts and plans—instead of
actual software. The point of Agile methods it to release software
early and often and avoid using surrogates.

Key Points of Agile
-------------------

Here are the key points of the Agile Manifesto.

-   **Individuals and interactions** over processes and tools. A more
    Agile project will use the best people and encourage them to talk
    amongst themselves. A less Agile project will write a lot of
    things (which folks don't have time or reward for reading.) There
    will be misunderstandings, leading to large, boring meetings where
    someone reads powerpoint slides to other folks to try and clear up
    misunderstandings.

-   **Working software** over comprehensive documentation. A more
    Agile project uses frequent release cycles of incremental
    software. A less Agile project attempts to gather all
    requirements, do all design and then try to do all the coding even
    though the requirements have already been found to be less than
    crystal clear.

-   **Customer collaboration** over contract negotiation. A more Agile
    project uses constant contact with customer and product owner to
    refine and prioritize the requirements. A less Agile project uses
    a complex change control process to notify everyone of a
    requirements change, which leads to design and code changes, and
    has cost and schedule impact that must be carefully planned and
    documented.

-   **Responding to change** over following a plan. A more Agile
    project uses incremental releases, conversation and a modicum of
    discipline to build things of value. Just because someone thought
    it should be included in the requirements doesn't mean the feature
    is really required.

The "Process Kills Passion?" Question
-------------------------------------

There Process Kills Passion blog lists a bunch of things that—it
appears—some folks find burdensome:

-   Doing full TDD, writing your tests before you wrote any implementing code.

-  Requiring some arbitrary percentage of code coverage before check-in.

-  Having full code reviews on all check-ins.

-  Using tools like Coverity to generate code complexity numbers and requiring developers to refactor code that has too high a complexity rating.

-  Generating headlines, stories and tasks.

-  Grooming stories before each sprint.

-  Sitting through planning sessions.

-  Tracking your time to generate burn-down charts for management.

This list has three different collections of practices.

-   **Good**. TDD, code reviews, generating headlines, stories and
    tasks, grooming stories before each sprint and doing some planning
    for each sprint are all simply good ideas. They must be done.
    "Pure Coding" is not a good way to invest time. Planning and then
    coding is much smarter, no matter how boring planning appears.

-   **Difficult**. Test code coverage can be helpful, but can also
    devolve to empty numerosity. 20% more coverage doesn't not mean
    20% fewer bugs. Nor does it mean 20% less chance of uncovering a
    bug at run time. Code complexity ratings are also fussy because
    they don't have a direct correlation with much. They **must** be
    done and used to prioritize work that will reduce technical debt.
    But mindless thresholds are for cowards who don't want to mediate
    deep technical discussions.

-   **Silly**. Creating burn-down charts for management shouldn't be
    necessary. Everyone must read and understand the backlog. Everyone
    should build the summary charts they want from the backlog. The
    product owner or even the eventual customer should do this on
    their own. They must be given a profound level of ownership of the
    features and the process for creating software.

I don't agree that process kills passion. I think there's a fine
line between playing with software development and building
software of value. I think that valuable software requires some
discipline and requires executing a few burdensome tasks (like
TDD) that create real value. Assuring 80% or 100% code coverage
doesn't always create real value. Spending time keeping the
backlog precise and complete is good; spending time making
pictures is less good.



-----

amazing ....
------------

Chris Shayan<noreply@blogger.com>

2011-05-26 13:21:57.130000-04:00

amazing ....





