IT's Drive to Self-Destruction
==============================

:date: 2007-02-18 22:32
:tags: management
:slug: 2007_02_18-its_drive_to_self_destruction
:category: Management
:status: published





My approach to preventing IT insignificance
begins with firing the good programmers, since they're saddled with low-value
work to begin with.  In order to see what that means, let's look at the three
phases of an IT organization's collapse to irrelevance.  Then we'll see why some
specific reorganization steps can revitalize
IT.



Phase 1, Hubris
---------------



During the **Hubris** phase, projects are undertaken which boggle the mind.  CIO's, swayed by reading
books and magazine articles believe that they can make any kind of project work.
The CIO's job is to promote anything that makes sense.  In order to justify this
approach, the impact of each project must be
pervasive.



The projects undertaken in
this phase are grand and sweeping; projects like replacing a hodge-podge of
back-office systems with some unified ERP application like Oracle Financials or
SAP.  It's the ledger system, the backbone of the back-office.  It can't be any
more central and sweeping.  



The focused conversion of data from old applications to the new application gets
circumvented by extensive customization, extension and interfaces.  Highly
optimized in-house software is supplanted.  Rather than replace strange,
non-standard processes with processes that fit the off-the-shelf software, the
pinnacle of hubris is rewriting the off-the-shelf application so that a peculiar
business process is optimized in an unusual
way.



This isn't seen as hubris.  It's
seen as necessary customization.  It requires a high degree of programming
skill.  And it also requires incremental
delivery.



However, the reason I call it
hubris is that the organization is not often able to deliver on this
customization.  Even a flashy SOA programming toolset, in the hands of
improperly managed programmers, can't deliver on the promise of making an
off-the-shelf package fit every user's individual, contrived whims.  It isn't a
skill issue, it's a management focus issue.  See "`To
rewrite or not rewrite, that is the question <http://codecraft.info/index.php/archives/69/>`_ " for related thinking on
cost and complexity considerations that will kill any software
project.



There's something good about the **Hubris** phase: programmers get to program.
However, the grandiose projects wind up failing.



Root Cause
----------



The failure of over-the-top
development efforts comes from a single root cause:  not solving the business
problem.  A software development effort must demonstrably solve a business
problem.  However well-intentioned, carefully planned, meticulously executed the
project is, when it doesn't obviously solve an easy-to-articulate business
problem, it's useless.



The business
value proposition for software has to be boiled down to something so pithy and
in incontrovertible that a hands-off executive can remember it and repeat it
when asked.  It helps to position the business value like this:
*[X] is broken; installing software fixes [X]* .
It helps to be sure that each executive can describe exactly how *[X]*
is broken, so they know what will be fixed.



Note that we're not talking
about features and benefits.  We're talking about broken and fixed.  The
difference is that features are nice-to-have.  Broken is essential to stay in
business.  If the project doesn't fix something that's broken, it is pure hot
air.  



If a project contains elements
that stray outside the boundaries of **Was Broken-To Be Fixed** ™ (WBTBF), those
elements will (and should) be cut.  If these logical extensions and add-ons
can't be separated from the **Fixing a Business Problem** ™ (FBP) elements, then
the whole project will (and should) be cancelled. 




Once a hubristic project is cancelled,
the organization chills down to a **Conciliation** phase.



Around the Edges
----------------



When an organization
operates in the **Hubris** phase, there is often a main, resource-hogging project, and many small,
around-the-edges projects.  The smaller projects are also mismanaged in a way
that cripples the organization.  They are managed by a process of
**Descope and Drop into Production** ™ (DDP).  In this phase, a
cool solution to a business problem, one which takes more than 10 months to
complete, is descoped, dropped into production, and the developers moved on to
something else.



The incomplete
application is now a burden on the organization.  For the entire life of the
application, someone will be fiddling with it, doing ad-hoc work, fixing broken
data, rerunning programs with patches and hacks.  The cumulative effort spent on
"maintenance" and "support" will exceed the effort to put permanent fixes in
place.  However, maintenance is paid for with **Next Year's Dollars** ™ (NYD), which don't really
count.



Often a top-shelf developer is
saddled with ad-hoc queries and data reloads.  Their creative spark is ground
out by the boot-heel of bad management.  They get bored doing "programming
lite", when they could be writing real software.




Phase 2, Conciliation
---------------------



During the **Conciliation** phase, all projects must be meticulously cost-justified.  CIO's humbled by
earlier failures (or hired to replace a failed CIO) believe that most projects
are doomed to fail.  The CIO's job is to prevent anything that involves risk. 
In order to justify this approach, the impact of each project must be
meticulously measured.



Extensive ROI analysis and score-carding are the order of the day.  This reaches a level of
absurdity when ordinary Business Analysis to justify IT changes has to be
justified.  We have mini-projects to create the budget for the analysis and
planning to create the budget for the first phase of some initiative.  In order
to justify the justification, the initiative has to have a provable
ROI.



Since IT is all about cost
reduction, the ROI is based on reduced cost.  We can never really measure cost
savings because we rarely have usable cost baselines.  Some easy project plans
will shave a number of people out of the organization.  Most projects, however,
will make existing people more efficient, and more able to focus on business
growth.  What's the ROI of "less fooling around reconciling a bunch of
badly-designed spreadsheets"?  It wasn't an entire department, or even a
full-time job.  But it is the source of occasional multi-million dollar
goof-ups.   It carries a vast down-side risk; what's the ROI of avoiding
risk?



The IT-initiated ROI analysis
never seems to work out well.  The business starts to trump IT, doing things on
their own.  Often, the business will bring in their own developers, justify
their own projects to themselves, and spend their own investment dollars in
their own Hubris phase.  This creates shadow and duplicate IT organizations
within the enterprise.



In the **Conciliation** phase, programmers don't program.  At best, they integrate.  The most common
situation, however, is the programmers become glorified operators; they run
queries and extracts for the users.  They manually correct problems because of
incomplete or poorly-integrated software.  Rewrites and repair can't be
justified but endless maintenance and support is the order of the
day.



The Desktop Solution
--------------------



In the conciliation phase, few things can be approved, so end-users are forced to work with desktop
tools like Excel and Access.  IT can't (or won't) respond to user requests for
automation, so the users become power Excel hacks, learn Access or hire an
Access hack to kludge something together.  The desktop is there, why not use
it?



Desktop products don't scale well;
the solutions are often little better than
**Personal Programming Projects** ™ (PPP) applied to enterprise
information assets.  To improve these solutions, the users often beg for someone
to **Scale Our Spreadsheet**  (SOS).  It's a plea for help, and it goes unrecognized.



The Tipping Point
-----------------



There is a tipping
point that occurs in the organization.  This tipping point is passed when the IT
focus slips away from building and using software, to Keeping the Lights
On™ (KLO).  At some point, the CIO starts shooting down ideas because
there isn't enough new development money.  The budget is allocated for KLO work
only, and nothing new is possible.



Once we can't afford change, we've devolved to the level of maximum entropy.



Phase 3, Maximum Entropy
------------------------



While there are degrees of
entropy (from clumsiness to chaos to criminality), it's all essentially the same
net effect to the business.  IT is a large, fixed cost.  The CIO is simply the
head of computer maintenance.  Business initiatives come and go, and the CIO's
role is to provide the kind of cost information that helps executives choose the
lesser of a number of evils.



There are a number of reasons why entropy is maximized:

#.  All software is interconnected.  There's no
    focus, no nucleus, no easily identifiable "architecture", "data flow" or "system
    of record" for a piece of information.  It takes days of meetings just to get an
    overview of the mission-critical systems.  Something as simple as adding
    software to predict order volumes requires a day to uncover the nuances of a
    architecture of truly Byzantine complexity.

#.  All people are of equal skill levels.  There's
    no technical giant who can be trusted to write software and make it work. 
    There's no architect who can summarize the best way to implement something. 
    There's no QA person who can speak with authority on process or the software
    portfolio.

#.  All processes are hopelessly complex. 
    Everything is a special case, and nothing can be changed.  For example, all
    executables are built by programmers and put into production that way because
    the production support people can't be trusted to run a build.  There's no
    standardized build process, and endless meetings only reveal that no one
    considers it possible to achieve a standardized build process.  No one has heard
    of "open source software" (except in the negative sense of buggy, and
    virus-ridden); no one has ever seen
    configure; make; make
    install as the entire set of instructions for
    building software.




Consequences of Entropy
-----------------------



Every move is fraught with
"risks".  The "risks" aren't risks (like cancer, stroke, heart disease), they're
just failure to manage ignorance.  The root cause of this level of ignorance,
BTW, is the baffling complexity of the application software.  There's no
"probability" of failure; it's essentially certain that any effort will be
under-analyzed, under-designed, under-scheduled, and under-funded.  Failure
isn't a chance, it's essentially certain.  Success is only possible in the
unlikely event that some of the self-serving statements happen to be true.




To make anything happen at all, the
end-users are forced to an exaggerated level of mendacity.  At inception, they
require everything, providing fabulous ROI analysis.  At the transition to
production, they settle for almost none of what they required at inception.  And
they're satisfied, because they knew IT would never deliver on the full set of
requirements.  They only wrote the full set of requirements to make the project
seem important enough that it would rise above the `grey
goo <http://en.wikipedia.org/wiki/Grey_goo>`_  of IT.



The Conversation
----------------



I listen to conversations that go like this.



**Business**:  We need to fix X (order entry, order value analysis, etc.)

**IT**:  Problem X is based on
software S1, S2 and S3, which are unique to each division.  Your problem, X, is
really only part of divisions 1 and 2, so you can't impact division 3.



**Business**:  What if we all use S3?



**IT**:  It doesn't scale, we can't
support it, the licensing is complex, we don't have the hardware, our skills
aren't current, it isn't strategic, it isn't compatible with R2.



The conversation doesn't end there.
I'm brought in to sort out these various architectural details.  In particular
the "not compatible" one is a killer.  If we're retiring S2, why can't we also
retire R2?  Again, IT has some baffling, complex story that the user's can't
easily refute.  There's usually some technology issue that doesn't have any FBP
aspect to it; since no obvious business problem is being fixed, no one can
determine the value of the
software.



A Solution
----------



Here's a candidate
solution.  If we structure IT properly, we can more easily control what is done
and by whom.  First, we need to structure the overall IT organization around
available services.  We build IT as if we are going to outsource everything.  We
look at the network and hardware operations as if they are a hosting services
provider.  We look at our help desk as if we were outsourcing their skills and
knowledge.  



The most important thing
is to partition software development into a wholly-owned subsidiary.  IT, in
general, would then be run by a core group of business analysts who knit
together solutions to business problems.  They "subcontract" to an
infrastructure group.  They create operation units who work with end-users to
successfully use the software
solutions.



The main IT organization now
"subcontracts" software development to the in-house software development
company.  That development company creates software solutions as if it had a
number of external customers.  It writes comprehensible, tidy, intellectually
manageable packages.



The In-House Subsidiary
-----------------------



The in-house
software subsidiary creates the products that are used to solve business
problems.  The subsidiary also provides "level 3" help-desk support, much like
all of the other outside software vendors.  The programmers don't run random
queries and data extracts for end-users.  The operations folks handle that. 




The programmers, rather than
hand-holding, have to focus on delivering new, expanded value to justify their
maintenance agreements.  They have to respond to trouble tickets and bug
reports, as well as put in enhancements that fit with their software product
line.



The programmers aren't the
dutiful drudges that turn user whims into software.  They interpret the user
requirements into a tidy, comprehensible, compatible, usable package of
software.  They adhere to in-house interface standards to assure compatibility
and interoperability.  They provide usable API's for the operations ETL
programmers who are integrating, loading, and extracting data for the
end-users.



The Advantage of Distance
--------------------------



We'll separate programmers into two groups: our developers and our operations support folks.
By separating the developers we do several things:



1.  We lift the developers out
    of the grey goo of the **Maximum Entropy**  phase, and give them a way to effect
    change.  Rather than micro-managing hellishly complex tangles of requirements,
    we let them cut the Gordian knot by proposing a solution which they can build
    and maintain.  We assign operation support programmers to migrate the data to
    this solution, handling any integration and operation.  We keep a firm hand on
    the tiller to prevent the operations folks from creating complex applications
    under the rubric of creating an
    interface.



2.  We end the second-guessing of the **Conciliation**
    phase.  The programmers own the solution; they create it, they maintain it.
    Most importantly, they are able to extend it.  Projects aren't cut off at 10
    months because managers are bored.  Projects become products, which can have a
    long, productive life.



3.  We prevent the pitfalls of **Hubris** phase.
    The software developers have to create a product which solves a business
    problem.  They are, like any vendor, responsible for competing against similar
    products, and positioning their solution.  They have to provide pithy,
    intelligible summaries.  They can't hide inside IT as just another cost of doing
    business.


They can't (initially)
compete on price with an external vendor: they don't have enough products or
customers.  After a few years of product development, however, they will have
enough products in use that the aggregate maintenance fees for those products
will keep a development organization running.  Each individual product fee would
be competitive on the open market.


Since the programmers are --
technically -- outside the main IT organization, they turn over source for IT to
compile, build and install.  In this respect, they are now competing against
best practices in the open source community.  The open source quality bar is set
very, very high.  



Next Steps
----------



Fire your best programmers. 
Re-hire them in a subsidiary that creates products.  Cut them off from running
reports and extracts.  Connect them up with their customers: the business
analysts that have to solve business problems with software
products.



Make that subsidiary
responsible for quality and supportability.  Make them compete with the best
open-source products for quality and reliability. 











