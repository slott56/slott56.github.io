Technical Debt, the Cost of Cheap and "Get This Done ACAP"
==========================================================

:date: 2008-03-08 15:30
:tags: management
:slug: 2008_03_08-technical_debt_the_cost_of_cheap_and_get_this_done_acap
:category: Management
:status: published







See Martin Fowler's essay on `Technical Debt <http://www.martinfowler.com/bliki/TechnicalDebt.html>`_ .  Also see Steve McConnell's thoughts <http://blogs.construx.com/blogs/stevemcc/archive/2007/11/01/technical-debt-2.aspx.



We can use Agile techniques to get things done ASAP and ACAP (As Soon As Possible and As Cheap As Possible).  However, we still need to make clear the volume of work we're likely to encounter before we have a usable product.  And we have to clarify the :strong:`Cost of Cheap™`  -- better known as Technical Debt.



We inherited some software from a client that we're going to maintain and enhance.  Further, we're considering ways to distribute it to some other prospective customers  The Use Cases are spot on a big, clear business problem.  The opportunities for solving this problem are huge.



:strong:`Aside` :  [Every time my company and a client have this kind of "support us, please; sell additional customers if it helps" conversation in the past, it always falls apart on the licensing and sale of the intellectual property.  In this instance, we've finally moved off the "who gets revenue from the sale" question by adopting what we call the "GPL Business Model" (`GPL V3 Section 4 <http://www.gnu.org/copyleft/gpl.html#section4>`_ ).  Source is free, support is where we make the money.



Services are where the money is.  It's the 21st century, there will always be free software that does more-or-less the same thing.  You can't compete on price of the initial sale.  You can only compete on the thing which is not a commodity -- skills.]



:strong:`Change to the Architecture` 



The problem we're going to have is the distribution and support of a VB app that was designed only for in-house deployment.  It isn't designed for debugging, support, configuration or even testing.  It doesn't have any unit test cases of any kind.  Indeed, there are bugs that can be spotted through simple inspection.



:strong:`Another Aside` : [A is not NULL AndAlso A != " " is the problem.  The inverse is A is NULL OrElse A = " ".  Any other variation on these two is a common logic error.  For example, A is not NULL OrElse A != " " doesn't do anything useful.]



I'd rather not mess around with remote desktop support for widely distributed communities of users.  It's really hard to do that, and it isn't a skill we have a lot of.  I'd rather provide this in a SaaS model.  We run a central sever farm, if you must have a desktop deployment, we build desktop apps that use our SaaS web services.



One of the reasons the customer is handing it over to us is because they'd rather have a web-based deployment.  They can't easily convert it from desktop to web, so they're asking us to do that as part of our taking control of the application.  There's that technical debt piling up and preventing progress.



However, almost every part of VB program is intimately tied to the VB desktop GUI processing.  Even the essential algorithms are full of bonus code to update the display or change the highlights on buttons or check boxes.  



:strong:`The Technical Debt Question` 



The software we inherited :emphasis:`can`  be deployed to another customer's desktop.  We have to rewrite significant pieces, however.  



"What's the least we can do to generate a revenue stream?" a manager asked.



I can, of course, lie about it and say we can deploy it "as-is".  It won't work, even a little bit, but it will be deployed.  Everything after that can be called "configuration" or "tuning".  It will take months of this fooling around, but it will be deployed.  We can charge for the software; eventually, we'll have to give some of the revenue back because it won't be usable for months, but that's a management call, right?



Management knows that the code has database and configuration dependencies that are tightly bound to the customer who's transferring the source to us.  We know about the missing pieces the customer haven't been able to transfer because "someone else controls that."  These are things we really have to fix before trying to deploy this to another customer as if it's a ready-to-use product.  That's possibly what the manager wanted to know.  But it isn't the whole story.



Once we start looking at the taking these configuration features apart, we're looking at creating regression tests for those changes.  And there are no test cases.  So, there's a hidden cost of making changes: we also need to develop tests for those changes.  And in the process of trying to define those tests, we find bugs, missing components, bad design, conflicting comments, all the usual detritus of years of doing support ACAP.  In short, we have to pay back the accumulated technical debt.



If we deploy a minimally modified app, and fly people out to some new client to support and configure that software, what will our revenue stream be?  Probably a net loss, when you figure in the various costs we're going to endure.  And then, when we do offer SaaS, what do we do for those early adopters?



:strong:`The Dollar Value Of Technical Debt` 



It's difficult to put a dollar value on the Technical Debt of this particular product.  It's difficult because it's hard to say how much of the original application software we're preserving.  Ideally, the technical debt is just the stuff we're fixing.  But, if we're fixing everything, what exactly was transferred to us?



The architecture -- desktop VB -- goes.  The DB table structure -- with a set of FK's that the current developers say was a mistake imposed by an argumentative DBA -- will have to be discarded.  The VB code for the user interface has to be discarded.  The core algorithms are intimately tied to the GUI and have to be discarded and reimplemented disentangled from the GUI.  What's left are about eight lower-level class definitions that -- technically -- are the "model" of the MVC design pattern.  Even this has a lame X12 parser built into it -- a parser I'd like to discard in favor of something simpler.



Since we're discarding almost everything but the use cases and some design elements, the current cost of the software is almost entirely of the "debt servicing" kind.  Indeed, the customer hates maintaining this program for that exact reason: all of the maintenance is debt servicing.  It's too expensive for them to try to add new features.



:strong:`What To Do?` 



The debt has many different sources, each of which requires an investment to create something useful.  The architecture -- web -- requires that the whole UI is rebuilt from scratch.  The existing GUI and use cases can be used as the template, simplifying the effort for analysis and design.  Renovation is easy when you have a working application as a baseline: create test cases, and implement.



The data model requires that most of the existing SQL implementation is rebuilt from scratch.  And, since we're moving to SaaS, we're going to expand and refine the data model.  This is almost new work. The existing model provides the conceptual framework for understanding the use cases.



My approach is to apply Test Driven Reverse Engineering.  We'll concoct the missing unit tests and build an application that seems to do what the original application did.  It's easy to do this in Python.  Harder in Java.  Since we're discarding almost all of the VB, there's no compelling reason for messing with the .Net framework.



Since Python is such a high-productivity environment, it's easiest to rewrite tis in Python.  Easier than it is to write specifications for Java programmers to work from.  The bulk of the reverse engineering time is spent writing and arguing over the unit test cases.  The actual application programming time is much less.



Once we have something web-enabled, with a proper data model and a proper object model we can begin the maintenance cycle again.  Of course, future managers will make short-sighted, :strong:`As Cheap As Possible™`  (ACAP) decisions and we'll accrue technical debt until we are overwhelmed by the :strong:`Cost of Cheap` .





