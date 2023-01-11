Problems, problems, problems
============================

:date: 2007-08-08 19:39
:tags: architecture,design,methodology,process,agile
:slug: 2007_08_08-problems_problems_problems
:category: Architecture & Design
:status: published







Centuries ago -- it seems -- Jim Coplien facilitated a session for us at `CiliPLoP <http://hillside.net/chiliplop/>`_ .  Eventually, I figured out that patterns are a solution to a problem in a context which resolves various alternative forces, and has some understood consequences.  Context - Problem - Forces - Solution - Consequences.



In this month's CACM, the article on "`Involving Top Management In IT Projects <http://portal.acm.org/citation.cfm?id=1278201.1278206&coll=portal&dl=ACM&idx=1278201&part=periodical&WantType=periodical&title=Communications%20of%20the%20ACM&CFID=26238735&CFTOKEN=67485512>`_ " describes a technique called *Problem Mapping*.  Wow!  I think this is the other side of the pattern coin.  The article's a tough read -- it requires careful study because it makes a rigorous philosophical argument about the nature of truth in requirements analysis.



I find that too many people jump past the problem, past the requirements, straight into design.  I complained about this recently in `Use Cases, Why Cases and the Bentley Test <{filename}/blog/2007/08/2007_08_05-use_cases_why_cases_and_the_bentley_test.rst>`_ .



This Problem Mapping thing may be just what's required to stop the blind leap into specifying a solution before the problem is really understood.  The technique is gloriously simple, and requires three relatively simple steps: gathering, organizing and criticizing.



Three Step Process
-------------------



Gathering is what analysts and consultants do anyway.  Interview people, read code, find the problem, document the problem.



During the organizing phase, the real magic happens.  Your findings are partitioned into four buckets.



-   **Problems and Needs.**   These are the going-in problems or organizational needs.  Things don't work, or don't work well.  Things are complex, expensive, risky, error-prone.

-   **Causes.**  These are the answers to "Why does this problem exist?"  This is critical, and often under-documented.  There's a chain of root-cause analysis that leads to things like "That's just the way it is" or "Darned if I know why".  The whole root-cause analysis isn't as important as separating problems from causes.

-   **Consequences.**   These are the consequences of the problem.  If something's complex, expensive, risky or error-prone, what's wrong with that?  What's the consequence to the enterprise of something being complex?  Complexity -- in and of itself -- isn't a problem; but it can have consequences that include cost, risk, time, pain.

-   **Suggested Solutions.**   This is the part that can now be set aside.  Without this four-part map, the solutions get muddied in with everything else.  With this problem map, they can be neatly set aside for what they're worth.



Calling the Baby Ugly
---------------------



The final, criticizing, step is where we bring the interviewees together to learn what the consultants learned.  The point is to achieve a common organizational understanding.  There will be pain involved.  One person's problem may point a finger at someone else's cause.  You can't call someone's baby ugly without the situation becoming tense.



Fundamentally, change involves perception of a problem, which can be stressful.  It also requires disruption of the bad situation; disruption by itself is stressful, even if the outcome is better for everyone.



Most importantly, this technique coaches everyone in the essential logic of causality.  Something's broken, that breakage has a cause and consequences.  Will the solution actually address the breakage?  Would addressing the cause be smarter?



Follow-Up
---------



I've fumbled around with something a little bit like this.  I didn't have the clear-headed approach that Simonsen describes.  I merely tried to separate problem, cause and solution so that I could keep folks from implementing their favorite technology when it wouldn't actually help solve the problem.



I found it helpful to recast the lessons learned in the Pattern mold.  Document the Context, Problem, Forces, Solution and Consequences to capture the information in a concise, story-like format.  When you have a problem in a context, it's like reading a screenplay.  The second act of the screenplay -- the forces -- is where the conflict plays out.  The solution and consequences are the third act of the story.



Having an arc makes the whole something we can understand and use.  It makes it possible for top management to articulate the reasons for the technology solution and maintain some focus and follow-through.




