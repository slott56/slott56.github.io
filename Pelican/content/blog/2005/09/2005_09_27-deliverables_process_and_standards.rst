Deliverables, Process and Standards
===================================

:date: 2005-09-27 01:22
:tags: architecture,software design,methodology,agile
:slug: 2005_09_27-deliverables_process_and_standards
:category: Architecture & Design
:status: published





Software development evolves through four phases:


1.  Identification of a problem and inception of a
    project to implement a solution.

#.  Elaboration (analysis) of that problem to
    determine the most effective solution.

#.  Design of software to implement that
    solution.

#.  Implementation of the solution; installing and
    configuring software, training, and everything that goes with creating a
    software product.



Development proceeds
more or less sequentially through these phases.  Where possible, iteration
should be confined to the first two.  Problem identification and elaboration,
being discovery exercises, require careful control of scope.  This is sometimes
accomplished by starting, pruning back the domain of possible problems, and
restarting.  There are not a lot of opportunities for parallelism until
discovery is complete.



The goal is
successful deployment of software that creates value for the users.  The purpose
of producing intermediate documents is to steer toward that goal in spite of the
often overwhelming complexity of the software that will get
built.



Several documents collect
information on the process and serve as specification for future steps of that
process.  A methodology provides guidance on tasks that will create the various
documents and deliverables.  A methodology should also provide techniques for
accomplishing the tasks.



This BLOG
describes five recommended deliverables with some notes on content, process and
standards.  Each of these are independent documents.  However, some elements may
be derived out of a strict linear sequence.  For example, when developing the
architecture, there will be both architectural and design implications; this may
lead to creating some preliminary sections of the design document while
developing the architecture.



The
documents are:

1.  **Scope** or **Problem** .  This is a clear, complete statement
    of the context, problem and constraints on any candidate solution.  This is
    produced during project inception.  It is the "charter" that describes what
    constitutes success by defining the problem.

#.  `Requirements <{filename}/blog/2005/09/2005_09_29-requirements.rst>`_ This is the result of problem
    *elaboration* 
    or analysis.  This is the use case view and analysis versions of the other
    views; they are necessarily incomplete and preliminary.

#.  `Architecture <{filename}/blog/2005/10/2005_10_01-architecture.rst>`_ This is the high-level description of a
    solution.  Where the solution requires a novel architecture, this will be a
    complex document.  If the solution adds application software to an existing
    architecture, this will be a very simple document.

#.  `Design <{filename}/blog/2005/10/2005_10_03-design.rst>`_  This is the description of components to
    be built.

#.  `Implementation <{filename}/blog/2005/10/2005_10_11-implementation.rst>`_ and `Deployment <{filename}/blog/2005/10/2005_10_15-deployment.rst>`_.  This document describes packaging of
    components and their final deployment for value-creating
    work.



Each of these documents are
developed more or less independently and sequentially.  There is no easy way to
start design or implementation until the requirements and architecture are
complete.  Any attempt will typically burn up labor hours that will be
invalidated by changes to the
requirements.



Each of these documents
looks at the system from five distinct points of view.  The first phases
(Inception and Elaboration) merely outline these views.  The architecture,
design and implementation documents add detail to this structure. They call this
the 4+1 model because 4 views are technical and one is non-technical. `Kruchten4+1 <http://www.win.tue.nl/~mchaudro/sa2004/Kruchten4+1.pdf>`_  `UML Overview <http://www.developer.com/design/article.php/1553851>`_ `wi-arch11 <http://www-128.ibm.com/developerworks/wireless/library/wi-arch11/>`_

-   **Use Case View**  - what the interactions are that create
    value.  A use case defines how an actor interacts with the system to create
    business value.  This is the who, when and why of the system.

-   **Logical**  or
    **Static View**  - structure of the information.  The data
    side of "data processing".

-   **Functional**  or
    **Dynamic View**  - the states and activities.  The
    processing side of "data processing".

-   **Component View**  - the technology stack, the hardware and
    software components that build out the solution.   The "Architecture".  This is
    the how of the system.

-   **Deployment View**  - the installation on specific servers
    with specific IP addresses.  This is the where of the
    system.



These are not, of course,
distinct in any way.  Changing one changes the others.  Indeed, merely
attempting to write from one POV is almost impossible, since you have to fill in
functional aspects to support the data model (triggers, constraints, etc.) as
much as you need a data model to explain the functionality of the
system.



This overview omits project
management concerns.  For example, the strategies for team communication, work
procedures, development environment setup, etc. are not covered at all in this
document.  Nor does this approach include any kind of formal quality management
plan.  This is just enough documentation to successfully craft working
software.






















