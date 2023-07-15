Essay 9 - Getting Started
=========================

:date: 2005-09-12 14:51
:tags: architecture,software design
:slug: 2005_09_12-essay_9_getting_started
:category: Architecture & Design
:status: published





How do we get started writing requirements (or
doing architecture or even design)?



The
important thing is to recognize the
*what* 
vs.
*how* 
distinction.  Following Pressman's advice, we note a whole waterfall of
*what* 's
and
*how* 's.
It breaks down something like the following four phases.  For information on
techniques for Inception and Elaboration ("Analysis"), see Essay 13, "`Analysis Without Running Aground <{filename}/blog/2005/09/2005_09_17-essay_13_analysis_without_running_aground.rst>`_ ", for
guidance.



**Inception** 



Identify
the problem.  This is often very hard to do clearly and precisely.  See Essay
17, "`Solution or Workaround? <{filename}/blog/2005/09/2005_09_22-essay_17_solution_or_workaround.rst>`_ " for guidance.  The
solution to this is
*What* 
we are doing, the biggest, summarized
"*what* "
for the entire effort.  All that follows will be a
"*how* "
to accomplish this.  Also known as a goal, objective, charter, critical success
factor, etc.  Central in importance here to write an active-voice "what the
system and users will accomplish" statement.  A passive voice ("sales will be
increased by 2%") is part of the benefits, but not what we will be able to do
that we cannot do today.



This will be
broken down into one or more
"*how* 's"
that are sometimes called the Business Use Cases (BUCs).  The BUCs provide the
top-level interactions to show how the what can be achieved by actors using some
kind of
system.



**Elaboration** 



The
analysis of the problem spins off System Use Cases (often called just Use Cases,
UCs).  This elaboration "drills into the details" of the business problem. 
These use cases accept a BUC as a given, a
"*what* "
to be accomplished, and specifies
"*how* "
that will be done.   Note that the Business Use Case was a
"*how* ",
when viewed from the top, but is now a given -- a
"*what* "
-- as we move toward
implementation.



Note that we are still
describing the problem, using the problem's terminology.  We are specifying
actor interactions with a hypothetical "Black Box" System that will be built,
but does not yet exist.  We are elaborating the problem by describing the
interactions actors' would like to engage in to accomplish their
goals.



**Design (Architecture)** 



The initial, high
level design, or architecture, accepts each of the UCs as
"*what* "
statements, and defines a technical implementation that shows
"*how* "
that will be accomplished.  This is where we step out of purely business problem
domain language into system and software
language.



This is the top of the
design, and identifies components that can be used to accomplish the use cases. 
The quality assurance test of the architecture is to walk through each use case,
and identify the components involved in the interactions.  Responsibilities are
allocated to each component based on the role in the
interactions.



**Construction** 



**Detailed Design** 



The detailed design accepts
the architecture as the
"*what* "
and determines
"*how* "
each component must be constructed to achieve the architectural goals (which
achieve the UC goals, which achieve the BUC
goals).



**Programming** 



Programming
moves down the
*what-how* 
tree to the final level of determing
*how* 
to implement the design.  Generally, the design should provide enough guidance
in selection of fine-grained data structures and algorithms.  If it does not,
the architectural goals (or even high-level goals) should supply the missing
guidance.








