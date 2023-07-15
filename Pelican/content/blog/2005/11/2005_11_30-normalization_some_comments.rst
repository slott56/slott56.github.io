Normalization - Some Comments
=============================

:date: 2005-11-30 16:53
:tags: architecture,software design,data structure,algorithm,database design
:slug: 2005_11_30-normalization_some_comments
:category: Architecture & Design
:status: published





*"How do we prevent storage fragmentation and the associated slow-down ?"* 



*Why prevent ?* 



This is hard to respond
to.  The ounce-of-prevent-pound-of-cure didn't resonate with the reviewer.  What
would resonate?  An in-depth discussion of the "prevention is an investment with
an indefinite period of return and correction is an ongoing cost" doesn't seem
to be appropriate because it side-tracks the main issue.  It's embarrassing to
have to include the "prevention is smart, ongoing correction is stupid"
phrasing. 



It appears that the value of
prevention vs. the cost of remediation/work-around is not perfectly
clear.



*"On the one hand, we can design any old table, and compound this design with lots of additional processing to defragment storage periodically."* 



*Is this phrase necessary?* 



This is a
slightly different question: Is it appropriate to characterize correction of a
problem as "lots of additional processing".  I can't see any other way to
characterize it.



Both questions point
to the same objection: prevention isn't of any value -- a known work-around is
"better".  Okay, so what is the value proposition between correcting a problem
for the entire service life of the software and preventing that
problem?



1.  Need Satisfaction?  Both
prevention and correction provide the same basic feature set in the application
software.



2.  Resource Use?  Prevention
uses fewer resources, does not require down-time for table maintenance and
performs better.



3.  Maintainability? 
Maybe the normalized application is somehow seen as too complex.  In the case of
a trivial example with one table, normalization doubles the number of tables. 
But when we have 100 tables, normalization adds 1, an increase in complexity of
only 1%.



4.  Adaptability?  Maybe a
correctly normalized application is harder to adapt to new uses in the
enterprise.  However, this is what RDBMS views are for, so this doesn't seem
sensible.



5.  TCO?  Since prevention
adds no ongoing maintenance and support, where correction adds processing (and
the risk of breakage, the resources to do this processing, poor performance,
additional storage and no-value down-time) it's hard to say what TCO benefit
there could be.



In balance, it looks
like correcting the problem is valued strictly because it has a historical
precedent to the reviewer.








