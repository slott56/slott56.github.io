Abuses of Use Cases - a Failure Taxonomy
========================================

:date: 2008-04-15 01:27
:tags: architecture,software design,requirements
:slug: 2008_04_15-abuses_of_use_cases_a_failure_taxonomy
:category: Architecture & Design
:status: published







I've seen a couple of recent use case problems.  The first recent failure of use cases was particularly alarming.  It was a small application; a few use cases, a couple of actors.  



One of the actors was labeled as "End User".  Seriously.  Few labels could be as vague as End User, except perhaps calling an actor "Actor".



A bunch of the use cases were essentially a GUI specification, which isn't completely wrong.  However, a GUI spec usually requires a ton of background and justification.  Often, a GUI spec relies on an underlying model and a bunch of context that provides the "why" information.



I asked for higher-level use cases to try and drive out what the content of the underlying model really was.  Without the context information, all we knew were GUI objects like characters and cursors and fonts.



I was told -- by the author -- that it was not possible to describe the application in any terms other than the GUI specification.  It was not possible to write a use case at a higher level; it was not possible that one could minimize the technology dependence.



I provided two strategies, the author was 'incapable' of doing either one.  Strategy 1: write multiple drafts, each using a different technology, compare and contrast the resulting drafts to get the "essential" material.  Strategy 2: underline the technology words in red and replace them with something less specific to SWING.  Both were largely impossible.



Consequence: someone has to guess at the underlying model.  That will work out great when -- part way though implementing the GUI -- someone discovers all the things left out of the essential model.  They'll then retro-fit the high-level use cases; usually around the partial implementation so that none of the "investment" is "lost".



Bunching
--------



Another use case problem stemmed from a situation I'll call "Improper Bunching".  A bunch of steps were described as a long use case and allocated to a single actor.  The steps don't really share information and business value; they contribute, but they aren't all the same.



In this case, a few of the steps could be performed by any of a large number of actors.  All of the candidates had the requisite knowledge, the authority to act and compatible business goals.  The choice of actor is really one of "who has the time to do the job", not "who has the knowledge to do the job."



The bunching, however, conflated the long sequence of steps with the smaller steps.  While some elements of the long sequence couldn't be shared of off-loaded, some of the individual steps could be assigned in different ways to change the way people were task-loaded.



Consequence:  The long sequence of steps dominates everyone's thinking.  Worse, it takes some work-flow alternatives off the table; and this takes some technology off the table.  Specifically, it prevents doing things in parallel in the background.



A Taxonomy of Mistakes



Here's my taxonomy of common use case mistakes.





1.  Not Interactive

    1.  Only Features and Technology - no actual interactions between actor and system

    2.  Only Algorithms - no people - the use case is dominated by algorithms and processing details, actors are left out of the picture.



2.  No Business Value

    1.  Incomplete

        2.1.1.  Focus on Sequential Operations - usually login and initial setup; some business operations omitted or summarized.

        2.1.2.  Following the Precedent - rewriting previous business operations.

        2.1.3.  Bunching - use cases are long sequences that could be decomposed into smaller, reusable, independent steps.

    2.  Non-Specific

        2.2.1.  Free-Running Imagination - conflating "possibly" vs. "required"

    3.  Tech Specs

        2.3.1.  The use cases are technical requirements - the solution technology is conflated with the business problem.

        2.3.2.  The use cases are detailed design - the business problem is never stated



3.  No Actor - Often associated with a non-interactive use case



Use Cases for this Taxonomy
----------------------------



I think it's helpful to summarize the common use case mistakes with a common set of names.  The mistakes are prevalent.  Having a common names for these mistakes gives people a gentle reminder on the quality problems.



It isn't helpful to have a bad set of use cases.  When the author dismisses corrections as "that's not my understanding" we now have two problems: broken use cases and someone who doesn't want to help fix them.



The principle use case for this taxonomy is to help coach the authors.  If they have "standard" use case errors, then there are equally standard fixes.  It isn't a gross failure, it's just standard quality issues that everyone has.  The author isn't a moron; this is just a review to find the common kinds of errors and omissions.  The use case review isn't a trial by jury, it's just a chance to find and fix a few mistakes.







