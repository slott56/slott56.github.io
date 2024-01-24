How to Avoid Problem-Solving
============================

:date: 2006-07-30 13:41
:tags: architecture,software design,methodology,agile
:slug: 2006_07_30-how_to_avoid_problem_solving
:category: Architecture & Design
:status: published





One of the best ways to avoid problem solving is
to treat the problem as fluff.  Often, our users begin the conversation with
this assumption, and we play along.  Other times, we make this choice because
we're just too lazy (or negligent) to make an effort. 




Here's how it plays out.



**User**:  "I need a workflow solution."



**IT Person**:  "Great, I'll find one and install it.  We use [X] brand infrastructure components, I'll locate something compatible."  Fill in Sun, IBM, Oracle or Microsoft for [X].



Note the things that are missing from the previous -- and all-too-typical -- conversation:

-   Who has a problem?

-   What problem do they have?

-   Where, when and why does this problem occur?

-   What happens when we solve this problem?

-   What happens if we don't solve this problem?

-   What are the constraints on potential solutions?



Since we don't know any of
the above, we can buy and install anything -- anything at all -- and the odds of
success are just random chance.



Better
yet, we can draft a random set of purely technical requirements that are little
more than quality factors, and avoid the tedious process of understanding the
actors and the use cases.  I find that many requirements documents are
essentially the SEI `Quality Measures Taxonomy <http://www.sei.cmu.edu/str/taxonomies/view_qm.html>`_ ; they barely mention
users, business value, or business
context.



The consequence is the following:



**User**:  "I need a workflow solution."



**IT Person**:  "We already installed one and you didn't use it.  So we installed a different one and you didn't use that either.  What does it take to make you happy?"



Another way to avoid
problem solving is to assure that all solutions involve programming.  Some
management-types deny they are mandating programming solutions.  No matter how
much they deny it, no other choice is ever on the table.  Lacking any
alternative problem-solving strategy, we're left with writing expensive and
ineffective programs.



Note that this
can be the result of ignorance or malice.  An IT manager can be simply ignorant
of IT's role in organizational structure and operations; they could be under the
manifestly false impression that end-users can put together a logical process
better than IT people.  An IT manager can be malicious in spreading their
preference for programming (and the resulting empire of programmers and
maintainers) over solving problems.  The root cause doesn't matter.  What
matters is that software is the solution of
choice.



What's wrong with that?  Since
we aren't allowed to talk about organizational change, and how an ineffective
process can create errors, we are put into patch mode.  We're accreting
functionality that turns a problem into a
feature.



First, system X has a bug,
leading to process defects.  Management dictates that we write new programs Y1
and Y2 to work around that bug.



"No one would ever do that," you say.  Which is far from true.  There are a million
reasons why people do this every day.  System X is a legacy, it's an investment
that we must preserve, it's too expensive to fix, we don't know what the bug
really is, it's a packaged product, it's someone else's problem, it's slated for
replacement anyway, ...  The list is long and
sickening.



Second, we note that the results of Y1 and Y2 aren't quite right, so we institute manual procedures to
check Y1 and Y2.  These are complex and error-prone procedures.  Our defect rate
is reduced in one area, but increased in others.  Note that adding process to
correct another process, means we're losing ground
here.



So we decide to add a workflow solution to make sure that the manual repairs for Y1 and Y2 is executed flawlessly.



Wait!  Hold the phone!
----------------------



We have a *bug* in X.  We have *incorrect* fixes in Y.
We have *incomplete* manual procedures to fix the problems in Y that fix the problems in X.
We're now going to canonize this whole mess with a workflow product, W.  Adding
software only serves to compact this aggregate into expensive, complex
coprolite.  



Here's what happens next. 
We try to replace X, only to conflate it with Y and W.  We can't tease apart the
essential processing from the workarounds.  The original bug in X is now a
feature of the overall Gordian knot of
processing.



What were we doing in the first place?



It doesn't matter what we
were doing.  IT management needs software to make X, Y and W play nicely
together.  We have a mandate to reduce cost.  The cost of X is high.  The cost
of Y is relatively low, but the cost of W is large.  The workflow package, in
particular, is enabling (or infrastructure) software, not a complete solution;
it requires skilled people to implement solutions.   And, it's only used for one
thing, the workflow to fix the problems in Y (which were supposed to fix the
problems in X.)



How can we reduce the cost of this mess?  Easy.



The standard answer is to write more software.  Replace the whole thing with a new
application that enshrines the bug in X and the workarounds in Y.  The
maintenance cost of a solution developed in house is negligible.  If not zero,
it's always acceptable.  As a consultant, I'm often involved in empire-spreading
software construction efforts that add maintenance cost far beyond the projected
small number of FTE's.



How does this avoid work?  It keeps us from the tedious process of understanding the actors
and the use cases.  We know that's just fluff.














