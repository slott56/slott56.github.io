SOA: Cheaper?  Simpler?
=======================

:date: 2007-09-24 16:58
:tags: architecture,design,complexity
:slug: 2007_09_24-soa_cheaper_simpler
:category: Architecture & Design
:status: published







My experience is that an SOA has the potential to be cheaper and simpler.  However, cheaper and simpler may not be the only value proposition.



`Kontrawize <http://kontrawize.blogs.com/kontrawize/>`_  says:  "there is only something to gain with SOA for the parts of your software that genuinely have re-usable functionality, and are expected to be re-used in the shorter term."  Further, "in some circumstances it won't win you anything, and could cost you more to implement."



Interesting points.



The reuse potential of an SOA is the core issue.  We wrestle with it constantly.  I don't know where the SOA = Reuse came from, but it's certainly a strong feeling.  When I Google "SOA Reuse" I get a score or more of hits on why SOA ≠ Reuse.



I'm not sure how to tackle the SOA = Reuse problem, either.  Generally, we remind our customers that SOA isn't about reuse, :emphasis:`per se`.  Reuse can happen, which is good, but it requires a disruptive change in software development and IT governance.  Rather than tackle that, we'd just like to solve your business problems quickly and simply.



:strong:`The Point of Services.`



We try to sell SOA services based on Agility.  Since an overall composite application can be decomposed into loosely-coupled services and some flexible collaborations among those services, we should be able to rework the application cheaply.



There is a big should, however.  If we aren't careful, we can embed business rules in the wrong piece of the architecture.  There's a central principle, here, that gets us to cheaper and simpler.  I call it :strong:`Allocation of Responsibility`.



I can see a `spectrum of mutability <{filename}/blog/2005/09/2005_09_18-essay_14_mutability_analysis.rst>`_  in any application.  It works like this: some parts of an application are based on laws (political or natural) and are unlikely to ever change.  These must be services.  Some parts of an application are based on the overall industry or the organization of the company.  These don't change much either, and must be services, also.



Some things are local to a line of business, a product, customer, vendor or even a specific contract.  These are things which vary, and may not make good candidates for services.  These are the kinds of special cases that catastrophically break application software.  These are the things that we need to put in scripts or collaborations.



:strong:`Services Aren't Mutable.`



The central tenet is that faster and simpler flow from having some fixed services, defined clearly and plainly without too many odd special cases.  These are easy to write, and very easy to get into production.  The users should be able to cough out standard test cases for the standard situations without burning many brain calories.



The exceptions, oh-by-the-ways, alternative courses, and extensions, however, take a bit longer to craft.  Often, these are best handled in a collaboration or higher-level application.  These components will rely on the fundamental service, but add value by handling a unique oddness correctly.  We rarely (if ever) have all the answers for these special cases.



Indeed, one of the causes of "scope creep" (in the negative sense) and subsequent project cancellation is IT's inability to deal with ongoing flux in the business.  Each time some executive works out a new, bigger, more bizarre contract, IT learns one of two lessons in agility: how to respond or how to dig in and refuse to cooperate.



:strong:`The Prevent Change Defense.`



IT project managers are penalized for permitting change.  Consequently, IT departments can build really effective prevent-change defensive strategies.  Often, complex "gatekeeping" exercises, scope statements, project reviews, program offices and other management shackles are used to prevent change.  



We penalize IT many ways.  First, our terminology indicates our preferences.  "Scope Creep" is pejorative: it's a failure.  Everyone wants to know the final, total price and the deadline date.  Any change -- any change at all -- is greeted badly.  If you reduce the cost, then your initial estimate was sand-bagging and you're a useless liar.  If you increase the cost, then your initial estimate was just a psych-bid to win the work, now you'll make up the difference with endless change control.



Since users often add features during the life of a project, the budget will always grow.  Even if we play the `XP Planning Game <http://www.xprogramming.com/xpmag/whatisxp.htm>`_ , we only adjust the priorities and the order in which work gets done.  We never balance or contract the budget.



Ultimately, Project Growth = Bad.  Therefore, we put as many obstacles in place to prevent the users from learning or changing.  Once the project starts, it's like water flowing down a series of waterfalls... You know the metaphor: it can't be diverted or changed, you can't add to or subtract from it.  The initial specification is the only specification.



:strong:`Responding to Change.`



If we elect to respond positively to change, we have to fundamentally rethink the ways we measure project management.  Blind and stupid measures ("on time", "under budget") tell us nothing about what the users got out of the deal.  We need to look at what got delivered that people used.  What made a difference in the business?  What business value did we enable through software?



Consider putting some services in place which handle the 80% cases, and using those services in some applications.  We build the simplest, dumbest cases first.  We can usually build this very, very quickly because we already know this about the business.



The next 20% has to be considered very carefully.



Is it subject to change?  Stable features of the business are more valuable than changeable features.  Rather than program the living daylights out of something, expose it as a well-thought out manual operation and be done with it.



Does it have growth potential?  A feature of the business that users (executives, vendors, customers, etc.) like will be used more heavily in the future.  Perhaps this defines a new service to capture the next 16% (80% of last 20%).



Is it a significant change from what we have in place?  Does it lead to devastating software changes?  This happens when something about the business model was encoded badly in software, and became a feature of the business.  Often the software and the business are conflated into the user's mental model of what can be done and what can't be done.  Anyone who starts thinking outside the box will force us to rethink this.  Why should cruddy software limit what the business can and cannot do?  And why should IT be enforcing that cruddy view of the business?



:strong:`Resulting Architecture`



The architecture that results from an SOA exercise will be simpler because we have the opportunity to practice :strong:`Allocation of Responsibility`.  The immutable features of the application are the core services.  We may write these or we may make use of our vendor's API's; either way, we have a base set of features that don't change much.



These services are supplemented with collaborations that fill in the special cases.  Perhaps they choose between two services to manage the 80-20 general case-exceptional case processing.  In some cases, the collaborations may actually implement the special case because it's too specialized or mutable or depreciable to require a stable service.



I think the big value of SOA is in allow us to pursue an Agile methodology.  We want to have frequent releases, learn our lessons quickly, and adjust as we go.



We want to value change, not revile it.  We want to measure our success in business impact, not budget and schedule.  (People say "in the real world, we still have a fixed budget" as a way of playing their favorite prevent defense.  An agile approach doesn't spend more; at the worst, it spends the same amount incrementally, permitting change.  By welcoming change, however, it can spend less.  In the real world, the users change their minds.  Picking a schedule today for software that won't into production for two more years is insanity.  Rewarding managers for adhering to an insane schedule is, well, even less sane.)



:strong:`Drop Reuse.  Pick up Cheap.`



My position is this: use SOA to reduce the complexity of your software.  Rather than big programs, write small collaborations that implement special cases on top of the general-case services.  A good :strong:`Allocation of Responsibility`  will simplify your software. 




