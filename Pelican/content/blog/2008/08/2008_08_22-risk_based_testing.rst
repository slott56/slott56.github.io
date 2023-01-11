Risk-Based Testing
==================

:date: 2008-08-22 10:29
:tags: architecture,design,unit testing,tdre
:slug: 2008_08_22-risk_based_testing
:category: Architecture & Design
:status: published







First, read Bach's `Heuristic Risk-Based Testing <www.satisfice.com/articles/hrbt.pdf>`_ .  Clear and simple.



Then, read Amland and Garborgsv `Risk-Based Testing and Metrics <www.stickyminds.com/getfile.asp?ot=XML&id=13289&fn=XUS31659994file1.doc>`_ .  Not so clear -- probability gets folded in, confusing the issue.  Also check out Schaefer's `Risk-Based Testing <www.cs.tut.fi/tapahtumat/testaus04/schaefer.pdf>`_ .  Probabilities are waved around like they're important.  They aren't.



Risk management shouldn’t be confused with random Roulette/Craps/Blackjack kind events.



The odds of failure aren't what matters -- it's always 1.0.  It's the *cost*  of failure that matters.  And even that is just the overall importance of the feature.



We have to be very careful with the work "Risk".   Software risk management is about three simple things: (a) bad management, (b) gathering information (managing ignorance) and (c) planning for specific contingencies.



Risk as Bad Management



Risks aren't vague, blurry, random casino events.  There aren't odds.  Most risks are things which **will**  happen unless we take steps to prevent them.



Nothing -- except developer death or serious disease -- is about random risks.  It's about specific bad management that will unconditionally be a problem.  The only thing we may not know is the magnitude.  For example, let’s say we write an estimating assumption that there’s a risk that the test server won’t be ready on time.  This isn't "random".  It's totally under our control.  We don't really "mitigate" this risk, we just order the server on time.



You might say that there's a risk that sys admins won't have it ready on time -- the risk is that their time to deliver is variable -- could be a week, could be three weeks.  It appears random.  Even though you might want to describe it as random, it's a controllable, knowable event.  In this case, it's someone stealing the sysadmin resources out from under you.



Most bad management leads to rework.   You can't control everything, but the things you can't control aren't random.  They’re just irritating – and they're just rework.  You don't use random-event risk management.  You say "What if we’re wrong?  It will cost us $50K to get out of that mess."  That's your contingency budget: a specific rework plan.  $50K for specific actions to solve a specific potential problem.  Not 10% of the project, but a plan to remedy the problem.



Knowledge and Ignorance
-----------------------



Some of what passes for "risks" are "Things we don’t Know" mixed with "Things we didn’t even know to ask".  Throw in the attitude of "New information looks like scope creep", and learning becomes a problem.  These aren't a roll of the dice.  They're things we didn’t know, but figured we'd learn as we went along. 



For example, "How many users?"  That's a business analysis question; they'll get to it.  We assumed it was a dozen.  If it’s 100, we have a change control issue.  This isn't a risk -- we assumed something going in, we knew we'd learn something during the project.



You might say that there’s a "risk" that we guessed wrong in our initial assumptions.  It isn't, however.  It's learning.  Either we left room in the project to learn, or it devolves to basic bad management.  The answer wasn't known in advance, but it wasn't random, either.  It just wasn't known.  Guessing ("assuming") isn't random – it's just that we could guess wrong.  



This is simply a budget change.  If the number of users is 100 instead of 12, then we have to refigure the budget with the new information.  Unless you're saddled with "All Scope Change is Bad" mind-set, that's just a change.  Change based on stuff that was learned.  This isn't **rework**; this is learning.  You say "What if this assumption is wrong?  It will cost us $50K to get out of that mess." A specific rework plan.  



Specific Contingency Plans
--------------------------



Bottom-line: It’s all about contingency planning.  For each thing we don't know, we make up a number (an "assumption") and a *x* $ multiplier to turn that number into a project cost.  When we finally get the real number, we apply the *x* $ multiplier and get the new project cost.  This is how change management happens -- each new thing we learn revises the budget.  Each mistake we make has to be corrected.



A mistake -- when things that go wrong -- leads to rework.   This rework is a specific budget number we have to add.  For things we didn't know to ask in the first place, that’s plain old scope change based on stuff we learned.  It's also a budget number we add.



Management risks aren’t random.  They’re not like casino gambling or insurance.



Risk-Based Testing
-------------------



Risk-based Testing builds priorities around two things: the importance of the feature and the impact of failure.  No odds involved in this:  importance is fixed, failure is certain, the cost of failure is predictable.  We simply rank our tests using importance and cost of failure to determine what gets tested first.



Since importance also drives Agile development, this is essentially a kind of Agile testing. 



Build stuff in order of importance -- test it in the same order.  I don't think Risk-Based Testing is very "interesting"; I think it's just the Agile practice renamed.



What about "Impact of Failure?"  That is usually parallel with importance.  If it the impact of failure is low, then you don't really need software to automate it, do you?  If the risk of failure is low, you have work-arounds, fall-backs; you have contingency plans that aren't complex or expensive.




