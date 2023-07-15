Notable Failure Of Use Cases - Part 3
=====================================

:date: 2005-10-31 19:52
:tags: architecture,software design
:slug: 2005_10_31-notable_failure_of_use_cases_part_3
:category: Architecture & Design
:status: published





**Forces** 

While
the intent of the use case technique is clear, it requires some discipline and
creativity to execute
successfully.



There seem to be three
attractive sinks for time and
energy.



**Stepping In Sequence** .  Often, the first use cases
developed are often those that occur “early” in the business
process.  In many cases, these are focused around inputs, or authentication, or
an overview of the processing steps.  In
*W* ’s
case [`Notable Failure of Use Cases <{filename}/blog/2005/10/2005_10_26-notable_failure_of_use_cases.rst>`_ ], the login scenario was described in
detail.  The web-based customer interactions assumed that customer segmentation
had already occurred.  There were no uses cases that described the mysterious
process of customer
segmentation.



**Free-Running Imagination** .  Business actors can find it hard
to separate what could
*possibly* 
be implemented in software from what must
*minimally* 
be implemented in software.  As an outsider, I like to use the “would you
sue us if that was omitted” question to separate needed from desired.  For
internal development teams, this question lacks resonance, making it difficult
to determine the actual business value of a use case.  In
*H* 's
case [`Notable Failure of Use Cases - Part 2 <{filename}/blog/2005/10/2005_10_28-notable_failure_of_use_cases_part_2.rst>`_ ], they were very uncomfortable with the
idea that something the user mentioned once was not absolutely
essential.



**Follow the Precedent** .  Business actors who can become
narrowly focused on current operations, or an early proof-of-concept (POC). 
Where the current operations include workarounds for incomplete or
non-integrated software applications, these are often canonized as processing
steps rather than constraints that could be changed.  When a POC embodies a
particular scenario, this is often considered as the only possible processing
scenario, and the use cases are simply details to supplement this processing
sequence.  In both
*W* 's
and
*H* 's
cases, early proof-of-concept thinking dominated the
implementation.



**Solutions** 

The
**Stepping In Sequence**  problem appears to stem from a
failure to characterize the overall business value of the application.  Lacking
any guidance, the use-case writers attempt to begin with the process that seems
to occur first, then moving on to the process that seems to produces the most
tangible results.  This tends to omit preparatory steps that have an indirect
effect on the final results.  It helps to work backwards from the results, not
forward following the existing
process.



The
**Free-Running Imagination**  problem appears to stem from a
failure to focus on the business value that is created.  In many cases,
additional features do not create any additional value.  In some cases, the
additional flexibility or maintainability concerns increase the overall cost of
development and operational use, diluting the value
created.



The
**Follow the Precedent**  problem appears to stem from an
emphasis on business process without an understanding of the business value. 
Process-oriented end-users often fail to understand the purpose behind the
process, and the value created by successful execution of the process.  In many
cases, processes create intangible or indirect benefits, like confidence in
correct execution of other
processes.



The most critical portion of
any use case is the creation of business value.  The interaction scenarios
should be derived from the kind of value that is created.  Business value is
often intangible or indirect; examples include confidence, assurance,
compliance, certification, or authorization. For example, customer marketplace
segmentation may involve creation of user-specified segmentation rules.  These
user-specified rules are entered by an actor; the immediate business value is
the improved segmentation; this leads in turn to improved web sales which has
numerous other business consequences.  The user-specified rules must be
validated prior to their actual use on live customers.  This validation process
creates confidence in the rules.



I feel
that a business analyst should (1) help users identify the indirect or
intangible value created by a use case, and (2) challenge every part of a use
case that does not contribute to the expressed value.








