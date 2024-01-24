Requirements
============

:date: 2005-09-29 10:39
:tags: architecture,software design,methodology,agile,requirements
:slug: 2005_09_29-requirements
:category: Architecture & Design
:status: published





Requirements describe the problem, and provide a
direction for composing a solution.  The remaining deliverables, leading up to
the creation of software, are created from the requirements.    These includes
the architecture, design, implementation and deployment
documents.



By defining the problem, the
requirements document also serves to bracket the scope of the effort. It
describes the context, the details of problem and the constraints on candidate
solutions. It evolves from a business use case through system use cases. It also
includes a conceptual or business model that depicts enties and relationships
named by the use cases.



A **use case** defines an actor's interactions with the system and how those interactions
produce business value. There are many templates for use cases. Simpler is
better.



An **actor**  is a person or an automated interface, external to the system.  An actor has goals
behind their interactions with the system.  These goals define the business
value the actor creates through their interaction with the
system.



The **system** is the hardware, software or procedures (or combination) under consideration.
When doing use case analysis, the system is a "black box" or "tool" with which
the actors interact.  Further steps in the process will decompose this black
box.  That activity has to wait until the system, as a whole, has been
described.




**Business value**  is some kind of benefit, either
intellectual, emotional or economic created through interaction with the system.
Generally, it is informational in nature and leads an actor to make a decision
or take an action outside the
system.



The uses cases form "functional
requirements" - things the system will *do*.
The constraints form "non-functional requirements" - other attributes of the
system. The non-functional requirements should be organized according to the SEI
`Quality Measures Taxonomy <http://www.sei.cmu.edu/str/taxonomies/view_qm.html>`_.



Do
not start any other activities until requirements gathering is complete. All
time spent prior to understanding the problem is
wasted.



A use case should identify the
following; for information see the `Zachman framework <http://www.zifa.com/>`_.

-   Actor (who?)

-   Goal and Business Value Proposition (why?)

-   Trigger (when? where?)

-   Sequence of Interactions (what? how?)



Content
--------


The activity of analysis can create three models of the business problem.  Each
model has a different point of view, but describe the same value-creating
activities.

-   Business Use Case Model -
    business-oriented actors and processes - what people do to create
    value.

-   Business Model - definitions of the
    busines entities with attributes and relationships.

-   Use Case Model - system-oriented actors
    and their interactions - how people create the business
    value.



Process
-------



The
following four process steps outline the requirements analysis
process.

1.  Write the short summary overview of the system
    If you can't write a pithy paragraph, continue refining and simplifying. Try
    explaining it to your mother to see if she understands.

#.  Identify the actors. Each actor has a reason
    for interacting with the system: collect their goals and the business value they
    create.

#.  Identify the interactions. Each actor does
    something to create value. Generally, actors make decisions and take action. A
    use case without decision or action does not have any "interaction" and must be
    questioned.

#.  Develop a business model based on the nouns in
    the pithy summary and the use cases. See the Object Modeling document for a
    procedure. Reconcile the model, the summary and the use cases to get complete,
    consistent terminology. There will be much rework and scope
    creep.



Note that this is a discovery
exercise, and is inherently unscopable. Active management of scope and potential
scope creep issues is critical.



Note
that this often proceeds in several phases: a scoping or inception phase for
planning purposes, a high-level analysis phase to decompose the problem and then
detailed analysis for individual subject
areas.



Note that is iterative: often,
the initial results will be refined until they are usable.  Common problems
include early specification of implementation details, failure to completely
identify actors or use cases.  These kinds of problems are resolved by iteration
through the
process.

Standards
---------


Requirements must be finite, definite and effective.

-   Finite means that they are measuable or
    quantitative.

-   Definite means there is a specific
    threshold or target. Failure to meet the threshold makes the solution
    unacceptable or useless.

-   Effective means that they consistently
    describe a specific business
    problem.



Risk. Failure to define the problem typically leads to a premature effort to define a
solution.



Examples of problems include
the following.

-   Too narrow a definition of data,
    processing or interfaces.  This document is focused on a specific solution
    without having fully defined the problem.

-   Focus on non-functional requirements. 
    This document does not provide information on interactions with actors or the
    creation of business value; rather than define the problem, it defines
    constraints on a solution.

-   No interactions with actors is really a
    complex step within a larger use case. This is often the result of detailed
    analysis without adequate problem definition.










