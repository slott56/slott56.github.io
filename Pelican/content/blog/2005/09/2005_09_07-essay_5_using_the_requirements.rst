Essay 5 - Using the Requirements
================================

:date: 2005-09-07 10:10
:tags: architecture,software design
:slug: 2005_09_07-essay_5_using_the_requirements
:category: Architecture & Design
:status: published





Requirements have a number of
uses.

1.  They document progress.  This management value
    is sometimes the only value placed on requirements.  This happens when
    requirements are really just high-level design and don't describe the problem
    adequately.

#.  They test candidate architectures.  This is
    done well when there is a back and forth between requirements are architecture. 
    We gather requirements and propose an architecture.  If the architecture isn't
    desirable, either the requirements are incomplete, or the architecture is
    incorrect.  We add or adjust the requirements, or we modify the architecture. 
    This process can and should iterate until the requirements cannot be changed
    further.

#.  They quantify and qualify design alternatives.
    Once the overall architecture for a solution has been chosen, the requirements
    should continue to add value by providing guidance into selection of design
    patterns for implementation.

#.  They describe the final acceptance test.  If
    the requirements are not measurable enough to act as a final test, then they
    need clarification.



The back-and-forth
between requirements and architecture takes many paths, each of which helps
clarify the requirements. 



Sometimes an
architecture is too complex or expensive.  The requirements often include some
non-functional features that drive up costs.  Other times, a use case has too
much automation, or is otherwise poorly constrained and leads to large costs in
software purchases or
development.



Sometimes an architecture
is incomplete.  The requirements are often vague or incomplete, allowing a
too-simple architecture to appear to be a
solution.



Sometimes the architecture
seems to have the wrong components or focus.  This is often the case when the
requirements writers had a specific technology in mind, and weren't open to
alternative solutions to the problem.  In this case, the traceability between
architecture and requirements has to be examined to see if a change to the
requirements is really necessary.  Sometimes a formal proof of concept is
necessary to convince the reviewers that the proposed architecture does meet the
requirements, even when it is not the expected
solution.



The big failures occur when
the project plan has a strict, one-way waterfall from requirements to
architecture to implementation with no back-and-forth.  That is madness because
then every bad idea in the requirements becomes an architectural feature adding
cost and risk; any attempt to revoke a bad idea becomes scope creep and the
project collapses.  



Cause of death: a
lack of useful interplay between requirements and architecture.












