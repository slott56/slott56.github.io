The Technology Obsession
========================

:date: 2008-08-16 01:11
:tags: architecture,design,complexity
:slug: 2008_08_16-the_technology_obsession
:category: Architecture & Design
:status: published







An old professor of mine writes "There are lots of pathological propensities at work ..., "Gee, we've got a way to use the computer to ..."  In short, automation for the sake of automation."



See `jbox.dk Quotations on Simplicity <http://www.jbox.dk/quotations.htm>`_ .  The fundamental principle is that simplicity is really important.  But how do we find this mystical simplicity?



Actually, it's easy.  Listen to fewer people.  See Steve Yegge's `Business Requirements are Bullshit <http://steve-yegge.blogspot.com/2008/08/business-requirements-are-bullshit.html>`_ .  The point is :emphasis:`not`  that requirements are crap.  The point is that the :emphasis:`process`  of "Gathering Business Requirements" usually leads to requirements that include a fair amount of crap.  Indeed, the more time and effort you spend in "gathering" the less value you actually gather.

    

    "We're not talking about a failure mode for Gathering Business Requirements (GBR). We're talking about something more fundamental: the GBR phase of a project is a leading indicator that the project will fail.

    


    Put another way: GBR is a virtual guarantee that a project is building the wrong thing, so no amount of brilliant execution can save it."

    






The advice is to understand the problem, then solve it for yourself.  More fundamentally, build the minimum to actually solve it for yourself.  Zero frills.  None of the famous "we'll have to add features to create enough value to entice the users."



Also see Jesse Noller's "`Steve Yegge hits a homer: Your requirements are stupid <http://jessenoller.com/2008/08/12/steve-yegge-hits-a-homer-your-requirements-are-stupid/>`_ ".  "When you're thinking about requirements ask yourself this: If at the start, you can not describe exactly what your product does in under a minute - you've already got a problem."



Here's my takeaway from these folks.



1.  Actually understand the user's problem.  Try to do their job with them looking over your shoulder.  Don't talk hypothetically about "requirements"; don't waste time on `MoSCoW <http://en.wikipedia.org/wiki/MoSCoW_Method>`_  priorities.  Actually do their job.



2.  Once you actually understand the problem, build the software you need to solve the problem.  Focus on a simple, minimal, reliable, provable solution -- something that you can describe "with your hands in your pockets" -- something clear enough that it doesn't require professional educators, a power-point presentation or even on-line help.



3.  Once you have a solution, carefully fold in features.  Add features that you can articulate simply and clearly.  Cover an edge or corner case that you can describe; cover a major piece of functionality that's easy to articulate.  Be sure that the actual users truly "get" your vision.



Written requirements documents are of nebulous value.  A backlog of features -- yes.  A summary of the use cases -- yes.  A data model or some sequence diagrams -- yes.  Detailed, blow-by-blow narrative with "shall" in each legally-binding sentence -- no.



:strong:`How do you create schedule and budget?` 



Isn't a tight, complete requirements document a prerequisite for a budget?



Isn't that what everyone says?  Establish scope (by gathering requirements) and then define the budget?



No.  Requirements are demonstrably NOT part of budgeting.  Most projects have a budget which is lodged in the heads of executives, business owners and buyers.  You can gather all the requirements you want.  If you go over that budget, you will have your requirements cut down to size.  If you run way under the budget, you will be given more work to do to spend all the money.



Budget has nothing to do with requirements.  For that matter, schedule has nothing to do with requirements.  Try and change the schedule of a project.  Go ahead and try.  You're told to work smarter, not harder.  You're told that the date can't be moved.  You're told that some requirements have to be pushed into a later phase.



Schedule and budget are defined long before Gathering Business Requirements is finished.  Often before it's even started.



:strong:`What do we get for our money?` 



While "when will we be done?" is meaningless, "what do we get for are money?" is a meaningful question.  However, there's no simple answer.  Instead, this is a conversation topic, not a simple question.  Each incremental release gets more features.  Each piece of the backlog has a potential price and delivers something.  The priorities, the costs and the order of development reveal that buyers can change priorities, cut off the budget at any time and have some pile of useful software.  



Automation for the sake of automation -- an unhealthy obsession -- leads to thick books of requirements.  A thick book of requirements will have no discernible ordering, no priorities.  A smelly pile of requirements often accompanies a contract that amounts to all-or-nothing development.  All requirements or none of them.  If none is a possible outcome, how valuable can this be?





