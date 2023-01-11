The Waterfall's Not Working -- Even A Client Said So
====================================================

:date: 2008-02-11 11:23
:tags: architecture,design
:slug: 2008_02_11-the_waterfalls_not_working_even_a_client_said_so
:category: Architecture & Design
:status: published








TC Writes "With 30 years in the biz, I’ve experienced all the pains associated with a rigid linear approach (functional spec -> design doc -> code -> integrate -> acceptance test, always being sure to maintain a current version of the traceability matrix). An iterative approach is inherently more appealing, but I’m damned if I can see how you can use this approach in [a Firm Fixed Price] environment without a huge amount of contingency/risk money buried in the costing."

Clearly, some kind of iterative approach that allows us to fine-tune the deliverables is needed.  However, The core objection is the hand-wringing over risk management.

We need to get past our standard going-in position of “The Software we build will be X, the whole X and nothing but X so help us God.”

There are two approaches.

- You can iterate the waterfall approach with smaller waterfalls.  

- You can ditch waterfalls, entirely, and try to step outside the box to take an Agile tack on this.

What's important is this.  There’s no more risk in Agile (or small waterfalls) than there was in the big waterfall.  Each small waterfall is small risk, and it’s spread through the project.  People (specifically, project managers) try to say that iterative approaches have "a huge amount of contingency/risk" because they worry that a later waterfall will have a devastating change an earlier earlier waterfall, leading to a giant wave of unplanned rework.  They’re simply wrong about later phases devastating earlier phases.

If you want to iterate successfully, you have to start with the hardest part first.  The part that entails the most business or technical risk (or both, if things are really bad.)  By doing the hard part first, the remaining waterfalls will NEVER have as much risk as the ones already past.  And you know early on how you stand regarding business (or technology) problems.  They call this the “Spiral Model”.  You spiral out from the really hard, high risk bits, doing Functional Spec -> Design Doc -> Code/Test -> Release over and over again.

Sometimes this isn’t very satisfying because it’s still a series of fixed, unthinking waterfalls, in which a lesson learned isn’t an improvement, it’s scope creep.  When lessons learned are considered bad – because they knocked the Fixed out of Firm Fixed Price -- you can’t really be very successful, only marginally better at risk reduction.


Can We Iterate Without the Customer’s Buy-In?
----------------------------------------------


You can start doing iterative spiral development any time you want.  You don't need to involve the customer.  To do this, you must rank the business or technology problems from high risk to low risk and focus on the high risk first.  













It's really important to note that you haven’t added any risk dollars by iterating.  Indeed, you’ve probably reduced the practical impact of risk by tackling the worst cases first.  Each solved problem reduces your risk budget, but you never reduce your price.  Each solved problem transfers money from contingency to profit.  Why not start with the hardest problem first?

This, however, doesn’t really help the customer much.  You’ve just optimized your side of the risk equation without giving them a chance to optimize their side.  Enter the Agile approach.  If you pass the savings on to them, you will probably do even better at this.


Agility
--------



Your initial problem sounds like you’re describing the **Standard Relationship**: (1) define X, then (2) execute a plan which can only lead to X.  Some like to call this "risk reduction".  Any deviation from the plan is a "risk" of "slippage" or "scope creep".  Even meaningful lessons learned – if they alter the scope – are evil.








Remember, managers don’t understand the functionality or the value.  They only understand cost and schedule.  Since they don’t get the delivered functionality, they can’t manage the delivery of value, they can only manage the calendar.









So, there’s no way to avoid a rigid linear approach if you’re forced to make a rigid, linear promise.










Response (chime in with me, if you’ve heard this one before): "But that’s what our customers expect/demand: a rigid promise to build X for $."










Really?  Do our customer's really expect this, or is this a cultural bias that our company has?





















Don't our customers really want us to solve problem Y for them?  And aren't they suggesting that software X is a good approach?  A notional approach?  Or are they claiming that they're giving us the absolute, final, non-negotiable approach?












Agile specifically requires that you change the relationship from “Build X or Get Sued” to “Sneak up on solving problem Y through a series of software releases, each of which does something useful.”






Agile says that problem Y must be solved.  It further says that software X seems like the solution, for now.  Most importantly, it requires the buyers and the developers have a dialog where the buyers prioritize meaningful, valuable pieces of the problem and the developers commit to something that solves that valuable, meaningful piece of the problem.  No one promises or expects delivery of X, but they do require that we (collectively) solve a piece of problem Y.








If your customer really does expect/demand “Build X or Get Sued”, then Agility doesn’t interest them.  They’re playing a game with “risk” and you’re not going to get far unless you are allowed to sit down and talk candidly about what’s realistic and how they might be able to sneak up on solving Y without a formal, rigid contract.  You may not get far with this because many, many people don’t see the distinction between Build X and Solve Y.  They have to assume that X is the ONLY solution to Y, otherwise, well, anything could be on the table and that’s just chaos.  Dogs and cats sleeping together.  Dead rising from the grave.


























Firm Fixed Price is specifically Anti-Agile
--------------------------------------------
















Here’s the Horror Story that our management worries about.

















You pitch developing a solution using Iterative (or even Agile) techniques.  The Customer agrees and allocates full-time end-user resources to solving the problem.  You sit at the whiteboard on day 1 and ask them what’s the biggest, knottiest, most horrible part of the problem?



















They tell you about a MS-Access spreadsheet that’s just crap and makes their lives miserable.




















Wait! you say.  "Wasn’t this about fixing the scanning and the shipping and the label printing?"  "Well," they admit, "Sure, that’s nice, too."  It turns out that the high cost item isn't some slick new functionality, it's their inability to do some high-value, high-visibility business function because they started in MS-Access and it didn't scale.





















So, you replace the MS-Access database, providing an 80% solution.  Users happy.  Sadly, merely 8 weeks of budget spent.  Hardly any real money involved in this.  Nowhere near your budgetary estimate of 6 people for 8 months.






























Now, priority two is to fix the various feeds to and from the database.  This COULD involve reworking the scanning and the label printing and the Symbol-brand hand-held scanners.  But, you’ll solve 80% of what’s left with some relatively low-rent data transformations written in Python.   The scanning and printing and Symbol stuff bumps down to priority three.




















After the feeds and reports are fixed, priority three isn’t looking very interesting any more because – uhhh – the database you fixed on step 1 – it’s wrong.  Has always been wrong.  Before, they couldn’t see how wrong it was, but now that you fixed it and got the feeds right… uhhh… this is embarrassing, but, the fundamental business model has a gap in it.  So, could you kindly pack up and go home while they figure out what to do next?



The project was – what? – cancelled?  Successful?  Scope-crept out of existence?  On hold?  What exactly happened there?




The good news is that it was hugely valuable.  The bad news is that it did not actually deliver the original vision, using the original budget or scope.  Or anything.  



Good News / Bad News
---------------------


No one wants to be involved in this kind of good news/bad news project.  Bad News always Wins.  This is universally derided as a failure.  Cancellation.  Scope problems.  Poor requirements definition.  Fail.  Fail.  Epic Fail.



Agile, however, specifically demands that you look at this as delivery of value (because it was).  You didn’t meet the “original” vision because, frankly, the original vision was junk.  You did identify and make big strides toward solving the actual problem.  And, it turns out, the problem had gnarly, deeply buried root causes, that aren’t amenable to a software solution.  Few things can be better than to uncover serious institutional problems.  



To do this, however, you’re not building software with a firm fixed price and delivery schedule.


Paralyzed by the Procurement Process
-------------------------------------



In many cases, the procurement process tends to gloss over the problem definition – the users merely think they know, and IT has to pretend that the users actually know.  IT's governance process requires that someone fabricate some financial projection (phrases like “ROI” and “payback period” are prominently featured in the projection.)  [It’s insane because there aren’t a lot of facts backing it up; often none.]  So, IT then writes a “requirements document” full of techno-mumbo-jumbo in which the *problem*  is not well characterized.  The solution, however, is described in glorious detail -- most of it non-functional quality attributes.





You – as vendor – can’t figure out the priorities of any requirements because you can’t see what’s the biggest, costliest, ugliest part of the original problem, and what software features would make a meaningful dent in the costly, ugly part.


If they want a firm, fixed price, you can’t really have Agile (or even Iterative) conversations, because they can’t adjust their priorities and still have a fixed price.  Further, they may not be able to disentangle the proposed solution, X, from the original business problem, Y.  It’s not that they won’t.  It’s that they aren’t empowered to make trade-off decisions, since tradeoffs would change scope, which changes price which takes “fixed” out of it.  And scope changes, as noted above, are evil.  




What to Do?
------------




The “fixed price” question is sometimes rather silly.  Often, it’s a question of “I have $$$ to spend, do you think you can solve problem Y?”  So they give you specs for X, you quote a price, it’s too high so they amend the specs for X2 and you circle around.  Or the price is too low, and they're suspicious and don’t award it.  They don’t learn much; neither do you.  They have the price of $$$ in mind, and you have to guess the number they’re thinking of.





On the other hand, some customers are doing legitimate thinking, and just want to know how much they need to allocate.  The problem is real and they’re not just playing risk/cost/budget/schedule games.  However, their procurement policy may still stymie them.



The only way to start the Agile conversation is to convince them of the following:


- **It will take a long time and a lot of money.**


- **You can fork it over now as a Firm-Fixed Price payment.**


- **Or you can fork it over in pieces.**   We’ll commit the first piece, only.  After that, you can decide to fork over more, or declare the problem solved.  You only pay for the Next Thing; but you have to actively manage the selection of the Next Thing.




“What about an over-all budget for this so-called-Agile-process?”  [“I won’t hold you to it, I just need a number for next year’s budget.”  Right.  And you’ll still respect me in the morning.]


Here’s the easy answer:  “What’s it costing you today?” Problem Y costs you $$$ per month?  Base the budget on that.  Throw four months of money at it and we’ll deliver something that will take a big chunk out of the $$$.  The savings will probably fund the remaining phases.  If they don’t, you have an easier decision 16 weeks from now: you'll know know specific, detailed, focused things that worked or didn’t work.  They'll have made a prudent, low-risk investment in information and a partial solution.




Here’s the hard answer:  “How long will you be working on this?”  The team will cost $$$ per month.  Base the budget on that.  The team’s going to be in place for as long as it takes.  12*$$$ per year.  How many years?  Until the customer is satisfied.  Remember, they only budget on a yearly basis, so next year’s 12*$$$ budget is a decision they'll have to make then, not now.  Think of it this way: there are no multi-year projects, just a series of 8-week Agile deliveries. 


Recommendations
---------------


Read the `Agile Manifesto <http://agilemanifesto.org/>`_ .   Look closely at the Boehm Spiral Model, for instance in `Metrics and Models in Software Quality Engineering <http://safari.oreilly.com/0201729156>`_ .  Read up on `Scrum <http://www.controlchaos.com/>`_ .



Go back to the customer that recognized that we didn't solve their problem and have a frank discussion on an Agile approach.  How would they want us to structure an Agile deal?




