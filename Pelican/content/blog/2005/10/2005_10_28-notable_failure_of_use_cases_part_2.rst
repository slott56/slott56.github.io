Notable Failure of Use Cases - Part 2
=====================================

:date: 2005-10-28 10:38
:tags: architecture,software design
:slug: 2005_10_28-notable_failure_of_use_cases_part_2
:category: Architecture & Design
:status: published





**Context** 

The
company,
*H* , is
a large, well-established financial services firm.  In order to meet regulatory
reporting requirements, they elected to build a data warehouse that would
integrate information from 40 applications to feed an application that would
produce the regulatory
reports.



*H* put together a team of business analysts and
end-users to determine the use cases, and document these.  Training consisted of
a half-day presentation on use
cases.



**Problems** 

The
use cases, while partially narrative in form, were not interactive and were
dominated by processing details, including algorithms, database structures, and
processing components.



The operational
processing focus reached the point where the sequence of application programs
that was run during a particular production cycle was written up as a “use
case”.  This sequence involved no user interaction, no decision-making, no
confirmation, nor any controls for stopping or restarting.  The business value
for this "use case" was identical with the business value proposition for the
overall application; meaning that no additional information was supplied. 
Indeed, this simply described the
implementation.



There were many gaps in
the use cases.  One notable gap was the absence of any mechanism for validating
changes to the processing rules encoded in the database.  Lacking any defined
user interaction, the processing steps presumed that the rules appeared as if by
magic -- all consistent, complete and correct -- and were then processed through
an elaborate pipeline of programs.



When
it was discovered that user rules did not appear in a final, perfect form, the
error handling and rerun processing immediately devolved into a quagmire of
ad-hoc steps and procedures.  Precisely the thing use case analysis is supposed
to prevent.  The use cases had not addressed interaction with users, but instead
became traditional program specifications.  Faced with issues where users must
analyze, make decisions, and take action, use cases were, in effect, abandoned. 




An additional problem with the highly
procedural and operational use cases appeared when database optimizations were
attempted.  After a year, and three production releases, it became apparent that
a large number of rows were moved from warehouse to datamart, these rows were
then processed through an elaborate pipeline, finally a subset of these rows
were used to do end-user reporting.  A little reflection showed that only the
final subset needed to be moved from warehouse to datamart, reducing the volume
of data to two percent of the original
volume.



However, since the use cases
gave a very specific processing sequence, irrelevant to the actual results
desired, it was not possible to make otherwise transparent changes to the
processing.  We found that the end-user’s mental model of the processing
sequence could not be easily separated from the results obtained.  Moving the
subset selection predicates forward in the pipeline was not seen as a reduction
in data volume, but as a reduction in processing scope.  The users demanded a
complete proof-of-concept demonstration plus parallel testing to assure that the
predicates produced the same results irrespective of their position in the
pipeline. 








