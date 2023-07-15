Architecture
============

:date: 2005-10-01 13:34
:tags: architecture,software design,methodology,agile
:slug: 2005_10_01-architecture
:category: Architecture & Design
:status: published





An architecture document not only describes the
solution, it must trace back to individual functional requirements, and also
should satisfy the non-functional requirements.  In most cases, the requirements
must be prioritized, and there will be tradeoffs for meeting absolutely all of
the requirements.



In some cases, an
architecture exists, and the requirements must be matched to the existing
architecture.  This will lead to iteration in requirements gathering.  The
tradeoffs between what might be nice to have, and what is available at a
reasonable cost and level of risk require revisiting the requirements and
managing the scope of the overall
effort.



In some cases, the solution
leads to a novel architecture.  In this case, the development process will
complex as various alternatives are explored.  In other cases, the architecture
already exists, and the solution is simply a new application, or an extension to
an existing application.  In this case, the architecture process is simpler, and
the resulting document is more of a high-level
design.



The architecture can be
examined in both layers and partitions.  The partitions depend in part on some
patterns established by the` Zachman framework <http://www.zifa.com>`_ : data, processing,
communications, people and motivation.  The layers should correspond to one of
the multi-layer design patterns for systems.  One five layer approach
is:

1.  Presentation or View

#.  Control

#.  Model (or Domain)

#.  Access (or Data Transport or Mapping, e.g.
    JDBC or CORBA)

#.  Persistence (or Database)



Some applications may require
fewer layers, or may collapse layers together.  For example, a "fat client"
application may have the top four layers in a client-side component and the
bottom two layers on a database
server.



**Content** 



The
architecture transforms the analysis model into an implementation model.  It
"turns the corner" from analysis and elaboration -- in the problem domain -- to
technology.  It adds the component and deployment views to a model that starts
with the use case, logical and functional
views.



**Process** 



Architecture
seeks to optimize the allocation of responsibility.  Unlike the requirements,
which clearly define the problem, architecture balances the tradeoffs between
costs and benefits to arrive at a
solution.



The number of choices that
confront an architect require a disciplined approach to problem solving.  This
is best done by clearly stating context, problem, forces, solution and
consequences and being prepared to refine solutions and consequences as the
forces are more fully understood.  The process is iterative, and may cycle
several times to arrive at an acceptable solution.

**A metaphor** .  An architecture begins as a
chemical solution.  Decisions act as a nucleus for crystalization.  A software
incompatibility is a fault, and a different decision must be used as anucleus
for crystalization.  When the solution crystalizes fault-free, this is an
acceptable architecture.



There are a
number of background issues that must be added to the requirements.  These
include: implementation of associations and collections, history, security,
persistence, state, startup, shutdown, failure and recovery from failure.  These
issues are rarely appropriate for the requirements, but are essential features
of an implementation.

1.  Identify the regulatory, industry, business
    and application context.  Other constraints from within the business (customer,
    vendor, product, organization, time or geography) shouldn't alter the
    architecture, but will alter the design or implementation.  Identify all
    available components through reuse, commercial or open sources.

#.  Subdivide the exisiting problem into layers
    and partitions.  Identify components with responsibility for each layer of the
    architecture.  Note that some components may be defined by the context (i.e.,
    they are preferred by the business as part of a standardized framework). 
    Consult design patterns available and document the context, problem, forces,
    solutions and consequences for each decision.

#.  Identify the interfaces between layers and
    assure that all connectivity is properly addressed through available or
    to-be-built components.

#.  Identify infrastructure requirements for all
    components, with a focus on compatibility.  Incompatibilities will require
    adding a constraint to the context and reworking the process from the
    beginning.



The available components may
require considerable analysis.  Additionally, the to-be-built components must
have some broad overview of their responsibilities, interfaces, behaviors and
non-functional attributes.  This information creates the Analysis Model, as well
as a target Implementation and Deployment
model.



The modeling effort follows the
general outline of Object Modeling.  However, the starting point is not nebulous
prose or powerpoint slides.  The starting point is the business model in the use
cases.  This Analysis Model is really an elaboration of the Business Model, not
a new effort, built from
scratch.



**Standards** 



The
architecture must address all Zachman topics (data, process, communication,
people and motivation).



The
architecture must identify components to be used and to be built.  To be used
components must have specific source and version information.  To be built
components must have an overview of responsibilities, interfaces, behaviors and
non-functional attributes.



Note that
the architecture is essentially a check-list of components to acquire, install,
configure, test, implement and
deploy.



The architecture must trace
back to the requirements:  everything in the architecture supports a
requirement, and every requirement is satisfied by one or more elements of the
architecture.  This can be done by a "walkthrough:"  follow the execution of a
use case through the various components, assuring that the responsibilities and
operations will meet the needs of the use
case.



Additionally, the architecture
must be proven.  If it is not currently in use by the development team or the
business, a working small-scale reference installation must be
created.



Risk.
Failure to create the working reference architecture is a leading indicator of
project failure.  Until you have the architecture working, it doesn't matter how
simple or widespread the
adoption.



Risk.
Failure to verify the trace between architecture and requirements can create an
architecture that is too complex or inadequate to meet non-functional
requirements.


















