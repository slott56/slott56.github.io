Why Agile?  What's the Point?
=============================

:date: 2008-02-14 11:06
:tags: architecture,softare design,agile,management
:slug: 2008_02_14-why_agile_whats_the_point
:category: Architecture & Design
:status: published







TC's full quote was "We consume a significant portion of the overall contract generating a functional specification whose sole use is to serve as the outline for the acceptance test. Those who choose to argue this point might like to explain the recurring customer comment 'You did an excellent job and built exactly what we asked for; it’s just not what we really want.'".


I love that customer comment.  It's an admission that the "write requirements, get bids, monitor the contract" waterfall model of software procurement doesn't work for our customers.  This kind of quote means that they'll be open to a practice that tackles problems rather than manages creation of deliverables.



The things that sold Agile methods to me are the following:




1.  **Software is Knowledge**. This means that software development is knowledge capture.  The resulting knowledge has to be so thorough and complete that a lump of fused beach sand can perform the required functions. (If you don't think software development is knowledge capture, what else can you possibly describe it as?)


#.  **Users Lie**.  (Okay, maybe they assume or make mistakes.)  You can either fight against it or leverage it.

    Knowledge is only revealed through an exploratory conversation.  People often make mistakes and assumptions without realizing the consequences.  You can document it, but that invests money in capturing the lie – which helps how?  This isn't a political debate where we're playing "spot the flip-flop."  You need to capture the knowledge as software in a variety of drafts and revisions to reveal the problems.  “It looks good on paper, but…”  It *always*  looks good on paper.

#.  **Risk accrues**.  Either tackle it up front in small pieces, or suffer the consequences of being swamped by a large amount of risk later.  Again, you can try to think your way through all the risks, or you can think your way through the biggest risk first.  Which is a better investment: tackle one really hard problem and **solve**  it, or enumerate all possible problems without solving anything?  I think a solution in hand is worth two problems in the bush.

    Risk has two components.  There’s technical risk (do we really know the technology) and application risk (do we really know the application.)  You can control #1 with education; you cannot control #2 under any circumstances.  Why bother "controlling" it?  How about recognize it and manage it through an exploratory conversation and incremental tackling of risk?


#.  **Scope Creep is Not Bad**.  It's reality (see #2, above).  You can either fight against it or leverage it.  To leverage it, make scope change possible.  In particular, make scope contraction possible.


#.  **Tools Matter**.   Use the highest-level tools possible for this “knowledge capture” exercise.  C++ is not a civilized way to build application software.  A few performance-critical pieces, maybe; but whole applications?  Never.  You absolutely need Test-Driven Development and a toolset that supports it.  Java (and JUnit) are minimally acceptable.  Python (and unittest) rule. 



There's a bunch of education involved in making this case to folks who are habituated to a waterfall methodology.  My suggestion is to start with the `Agile Manifesto <http://agilemanifesto.org/>`_ .  Move on to customer conversations.  Then pitch a `scrum <http://www.controlchaos.com/>`_ -based or scrum-like project.



Current Work
------------



I just sold a multi-year scrum project by telling the customer that it will take several years of 5 to 8 people a year slugging away at it. We start Monday.  The first few years will have more intensive levels of effort.  After a while the work will subside from the initial development to ongoing maintenance and support.  They'd been building and using the software for 30 years -- we weren't going to replace it in 18 months.



I specifically told them that there's no "scope" that they (or we) can properly define in terms a lawyer or accountant could understand.  The software we're renovating is too entrenched, embedded, and deep-seated to cleanly separate as a distinct "system" or "package".  We will renovate until they tell us to stop.  At that point, we guarantee software that's a better fit to the business, more adaptable, more maintainable.  



We can't -- up front -- guarantee a finite, definite scope.  We do, however, promise to use all of the time they allocate to the project for customer reviews, priority settings and unit test development.  We can't work on this alone -- it requires deep end-user engagement.


Where's the Risk?
-----------------



TC's initial comment was on eliminating what he saw as a huge amount risk in a waterfall methodology. He (correctly) saw that an incremental methodology -- badly applied -- doesn't shift the risk burden.



Where are our risks?  Customer knowledge of the business?  We're building incrementally.  They can lie because it only affects the very next sprint.  Not the whole "project".   The "customer cooperation" factor is a huge problem in the waterfall methodology.  Here, it's a sprint's worth of problem, little more.



Knowledge of the technology?  Again, we're tackling things in pieces, we're only looking at one sprint's worth of confusion or problem-solving.




What about the "devastating change" that always seems to occur late in the project?  First, that's often because someone said "Hard-Part-Do-Later".  That's just bad practice.  Second, that's often because of an inflexible, untestable design.  Test-Driven Development and ultra-high-powered tools mitigates this.




