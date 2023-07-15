Business Analysis vs. Architecture
==================================

:date: 2007-04-03 17:41
:tags: architecture,software design,complexity
:slug: 2007_04_03-business_analysis_vs_architecture
:category: Architecture & Design
:status: published





Much of the work called "Business Analysis"
conflates business problem discovery and technical meddling.  I draw a firm line
between the discovery part of analysis and the non-discovery (or design) part. 
Discovery is all about managing ignorance; this can be ignorance of the business
need or ignorance of the available technology.  The idea of analysis is to
reduce ignorance.



The line is crossed
when implementation decisions are made.  Many analysts cross this line in an
effort to "help" the developers by bracketing some technical aspect of the
preferred solution.  This varies from
**Petty Petitions** ™ ("the user expects technology
X") to **Pointless Political Pandering** ™ ("we have a significant
investment in technology Y").  



Users
-- as a practical matter -- rarely care how their business problem is solved.  
I dislike seeing technical decisions in a document that is supposed to describe
the problem and bracket the features of an acceptable solution.  Sometimes I
bother to complain about overly technical business
analysis.



Almost every IT manager (and
most Business Analysts) respond to my complaints with something that includes
the phrase "in the real world...."  Often they lecture me on why the petty or
pandering request is important. 




Sometimes, there are technical
considerations regarding cost and risk that make a Petty Petition or Political
Pandering  into the only viable alternative.  Other times, the technology is a
toss-up, and the existence of a preference is sufficient to tip the tables. 
However, that doesn't stifle my
objection.



**Best vs. Preferred.** 



There's a world of
difference between "best" and "preferred".  Best is something you design, based
on the available information.  By definition, best can't be a going-in
assumption.  If you assume some technology is "best" and it doesn't fit the
problem very well, you have two choices: change the meaning of "best" or change
the problem being solved.  Both are
unappealing.



**Choice 1.** The problem is immutable, and the Petty
Petition or Political Pandering solution technology isn't really "best".  If the
technology is really just a suggestion, it isn't part of the problem and ought
to be documented elsewhere.  Here's the response: "we put it in that document so
we wouldn't forget / lose track / fail to exploit the technology." 




Bah.  If it's important you won't
forget or lose track.  No one ever forgets; writing "preferences" in the
requirements has only negative impact.  If it's good, you'll remember to use it.
Also, two documents can live in the same folder.  One document has the problem,
and a
*separate* 
document tracks unresolved issues, technology suggestions, history, previous
solutions, and other corporate
memory.



There are few things in a
requirements document that are as useless as descriptions of previous solutions.
Requirements aren't the repository for corporate memory.  They're a summary of
what **is** 
and what **will be** , not what once
was.



**Choice 2.** The technology is immutable, and the problem
is subject to some adjustment.  In this case, the problem description must
contain some fluff.  If any part of the problem statement is
**negotiable** ,
then it's not
**required** .
If the solution cannot be amended, then start revising the problem until the
given technology is the "best" and only solution. 




**We'll Listen If It "Makes Sense".** 



My favorite situation is
one where I ask what is going on and the customer tries to explain the
contradiction when the technology doesn't solve the problem, and neither cannot
be changed.



They invoke all kinds of
weird phrasings to resolve the contradiction:  "There's a strategic preference",
a "technology incumbency", a "historical precedent", a "fit with our skills". 
They never seem to realize the basic
issue:



"The problem is that our user's
can't solve 2+3.  Our technology selection for the solution must be the number
4."



After they repeat their rationale a
few times, and it begins to sound hollow, they fall back to the following. 
"We'll listen to an alternative, if it makes sense."  In this case, "makes
sense" remains undefined so that anything outside the box doesn't make sense. 
Even the correct answer of (4*4+4)/4 doesn't make sense.  Either the problem or
solution isn't being stated clearly or
honestly.



**Conclusion.** 



The
business analyst's job should involve business, and the management of ignorance
about that business.  In "`A New Architecture Involves Ignorance <{filename}/blog/2006/08/2006_08_22-a_new_architecture_involves_ignorance.rst>`_ " I
recounted the kinds of ignorance that must be managed, stealing from Armour's
`The Laws of Software Process <http://www.amazon.com/Laws-Software-Process-Production-Management/dp/0849314895>`_ .  Technology
selection, and how well that technology does or does not solve the problem, is
the role of the architect.



Once the
technology appears to solve the problem, we can proceed with an implementation. 
Note that we can't start implementing unless the problem is fixed and immutable.
If the problem could be this ("can't match work orders and labor hours") or
could be that ("can't match labor hours with checks written by SAP") then we
can't solve it.  We can only solve one problem (even if it is one problem with
multiple parts.)  If there are issues, or concerns about priorities, or
alternatives, then we need to manage ignorance more than we need to declare that
the application will use Oracle, PL/SQL, Java and be built in Visual Studio to
run on the desktop.



Some of the
technical ignorance is corrected with reverse engineering.  See `Python and Reverse Engineering, Part 1 <{filename}/blog/2007/04/2007_04_02-python_and_reverse_engineering_part_1.rst>`_  for the
first of several posts on this subject.  Some technical ignorance is corrected
with a Proof of Concept.  But no technical ignorance is corrected by having a
business analyst declare the recommended technology for the
solution.





