Use Cases, Why Cases and The Bentley Test
=========================================

:date: 2007-08-05 23:09
:tags: architecture,software design,requirements
:slug: 2007_08_05-use_cases_why_cases_and_the_bentley_test
:category: Architecture & Design
:status: published







See `So What Are Requirements? <http://www.ddj.com/architect/201202946?cid=RSSfeed_DDJ_All>`_  in Dr. Dobb's.



I've seen requirements done badly.  I've seen some notable failures of the use case technique: almost entirely because people refuse to actually apply the technique; they refuse to write use cases from the actor's point of view.  I've whined about this before in Notable Failures of Use Cases, `part 1 <{filename}/blog/2005/10/2005_10_26-notable_failure_of_use_cases.rst>`_ , `part 2 <{filename}/blog/2005/10/2005_10_28-notable_failure_of_use_cases_part_2.rst>`_ , `part 3 <{filename}/blog/2005/10/2005_10_31-notable_failure_of_use_cases_part_3.rst>`_ , and `part 4 <{filename}/blog/2006/04/2006_04_28-notable_failure_of_use_cases_part_4.rst>`_ .



The interesting point that Wiegers makes is that there are different species of requirements.  Failing to recognize this is what can lead to diluting the use cases with junk.



The summary definition (from `Coyote Valley Software <http://www.coyotevalley.com/tools.htm>`_  principal Brian Lawrence) appears to be that the line between requirements and design is that requirements lead to design choices.  While I like this, it has to be refined a bit.



Pressman calls this the "What vs. How" distinction.  Requirements specify what must happen.  Design chooses how this will happen.  Again, this needs some refinement.  In a way, Pressman throws up his hands in despair, noting only that there is a hierarchy of what's and how's.  For example, interface requirements are "how" we'll implement some business requirement.  On the other hand, the interface requirements are a "what" to a lower-level piece of software that opens and closes sockets.



Exacerbating this hierarchy problem is more fundamental confusion on techniques to capture requirements in the first place.



Point of View
-------------



Recently we were working through some use cases where the author had identified a document as the actor.  The body of the use case was a bunch of technical processing details for the document.  It's painful to claim that all 20 use cases weren't use cases because the actual actor (the user who needed to see the document's processing) was never mentioned even once.



At some point, the customer trotted out a use case with no actor.  The use case summary had a passive-voice construction ("will be notified")  At that point I could drop the bomb that use case actors are usually people (sometimes they are interfaces) by asking "for whom?"



The customer's project manager made the claim that he thought that use cases were written from the system's point of view.



"Technical" Requirements
------------------------



I told the customer's team that it was a common misconception.  It arises because of the vast wealth of technical details with no obvious home when writing use cases.  They wanted to call the details "technical requirements".  I balked.



Wiegers suggests that we have business requirements, user requirements (the proper use cases) and functional requirements.  This certainly peels the outermost layers of the onion, and is a potential tool for guiding people into writing usable requirements.  But it has a small problem.



The name "functional" requirements is a fairly serious problem with Wieger's breakdown.  Most people don't know what constitutes non-functional requirements.  Consequently, they just throw the phrase around more-or-less at random.  I have to object strongly when I'm shown a document with dozens of pages related to performance, maintainability, and ownership issues -- all non-functional requirements. 



The core issue is that everyone wants to design the solution.  The more people you interview, the more you discover that everyone is an architect, and everyone has very strong opinions on precisely how to build the software solution.



At every level of the organization, you'll hear the following: "I'm not technical, but wouldn't it be simpler if..." followed by some kind of design.  If I remark on how their solution might have issues, they'll explain to me that one of their non-technical staff built something like their preferred solution in MS-Access during lunch-hours over the previous week.  



The Why Cases
-------------



Rather than ask "If your staff member is such a hot-shot programmer, why am I here?" it becomes important to dig into the real requirements.



I find that we have the following kinds of requirements.  These aren't presented in a top-down order, but in an inside-out order.




-   **What the user sees.**   These are the use cases.  The wisdom here is that we can use the definition ("A user interacts with a system to create business value") to locate users, interactions, the system and value.  Absent these elements, we don't have a use case, and can set it aside as a solution design.  One of the acid-tests is to see if the use case addresses the "for whom?" question.  If this isn't someone's job, it isn't a use case.

-   **Why the user's even doing this.**   These are the **Why Cases**\ ™ that bracket the Use Cases.  We can ask "why?" and locate the overall business requirements that create the use cases in the first place.  Generally, the use cases are a solution to a business problem; in some cases, they're a bad solution.  Asking "why?" periodically helps to focus people on the rational behind the use cases.  It helps us recognize that we're only building software to make someone happier and more productive. 

-   **How we'll support the user.**   This is a high-level design for the solution.  We can't call it functional requirements because few people know what the non-functional requirements are.  We can't call them "technical requirements" because this also leads to more confusion than it prevents.  We need to call it design.




Passive Voice Reporting
-----------------------




One of the best indicators of confusion seems to be the passive voice constructs like "the exception report will be generated daily."  This invites us to ask two questions:




**For whom?** This question will let us locate the proper use case.  Generating an exception report doesn't involve any interaction.  Someone looks at the exceptions, makes a decision, and takes action.  Who does this?  What are they supposed to do?




**Why?**   This question will let us locate the driving business requirement.  For example, we may have a contractual obligation for a particular service level.  Someone must investigate each exception, determine a root cause, and take action to correct problems that are internal and finish processing the exceptional transaction.




Customer Guidance
-----------------




What do we do when we're confronted with stuff that isn't really a requirement?  Generally, we're given design documents with titles like "Software Requirement Specification" or "Use Case".  Since the documents don't allow us any design choices, they aren't really requirements; they're specifications.




All too often, folks have downloaded an SRS template (like `Wieger's <http://www.processimpact.com/goodies.shtml>`_ ) and then abused the template.  I've seen SRS documents with the titles and template instructions still in place, essentially ignored by the author.  Large sections of the SRS template are left empty, because the author wasn't writing requirements.




I think that we need to look at the design documents we're given ask the two fundamental questions: why? and for whom?  From these two questions we can back up to the business requirements and the use case.




Hopefully, we can achieve a fundamental rethinking of the specifications to improve their value in a number of ways.




The Architect Gets a Bentley
----------------------------




Defining who does the job gets us away from writing software that seems necessary to the author ("of course we need notification of exceptions".)  It can help us locate software that really is essential ("typically, Frank checks the exceptions each once or twice a week by looking at the logs, not a report").  If it isn't going to be done daily, why over-engineer the system?  If the logs satisfy the need, why design a report?  Why not target the implementation for what people will actually do?




Including the business requirements can simplify or focus the use cases.  If we can't articulate the business need, then we have the **I Get A Bentley**\ ™ requirements.




I had a customer claim that they required 24x7 availability.  But they would not consider any hardware changes, and the hardware they had purchased couldn't provide the level of availability they were asking for.  When I brought this up, they claimed that 24x7 wasn't really a "requirement" it was more of a "goal."  My follow-up question was "Where's the line?  What's the least availability that you'll tolerate before you sue me."  They chuckled nervously, and said that any talk of lawsuits was irrelevant.  




It isn't irrelevant.  "Required" means required, as in "if the system doesn't do this, you don't get paid."  




If 24x7 availability is a requirement, then "Architect gets a Bentley" is also a requirement.  There's no business justification for either position.  They were clearly a 12x5 operation, and could justify requiring 18x6 to cover weekends and west-coast timezones.  They could not show a business reason for 24x7 any more than I could show a business reason for a Bentley.  It may have been my goal, but I couldn't justify it as a contractual requirement.




The Bentley Test
-----------------




If the answer to "why?" is isomorphic to "because I'm the customer," then you've located a place to apply **The Bentley Test**\ ™.  If you get feature [**X** ] because you're the customer, then I get a Bentley because I'm the architect.  It sounds fair to me.  Prove that it isn't.




Phrases like "you must have known we wanted this when you wrote the proposal" or "if we didn't want that feature, why would we be building software?" are isomorphic to "because I'm the customer."  Other examples include 





-   "Don't bother trying to save us money with Linux, we're an all-[**Y**] shop."  

-   "We absolutely have to have all of our purchased applications share a single common database -- without any of that schema mumbo-jumbo."  

-   "You must fix our database without changing the user interface." 

-   "You have to achieve acceptable performance with no hardware or data model changes."  Followed by "no, we can't define acceptable."






Sure, and I get a Bentley.




