Getting to an Agile process
===========================

:date: 2008-07-30 13:27
:tags: architecture,design,methodology,process,agile
:slug: 2008_07_30-getting_to_an_agile_process
:category: Architecture & Design
:status: published







Here's a great summary of Agile techniques.  It's in ComputerWorld's Development section, in an article by Heather Havenstein: "`Five Web 2.0 app dev lessons for enterprise IT <http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=9110219>`_ ".  I think the article is mis-titled, since it's basically "Agile for Big IT."



Some of the five techniques are motherhood and apple-pie items.  Some are a little too-cleverly worded to pound home the essential points.



1.  Break the barrier between developers and end-users...  This is essential: crowds of managers and business analysts are not adding significant value.  A few key players to help the developers understand the problem domain are important.  A Business Analyst who is "translating" user requirements into IT jargon isn't helping.  A Business Analyst who is acting as architect or designer isn't helping.



2.  Keep it simple.  This is how you get to smaller, faster, better teams.  A bone-headed manager who claims that we have to add features to "justify the cost" or "create sufficient value" is just empire-building.



3.  Stick to the script.  This means use Python or some other powerful, dynamic language.



4.  Release early and often.  In the Computerworld comments, this point raised some ire.  The claim is that the folks in operations won't able to keep up with rapid, small releases.  This assertion is demonstrably false.  Folks in operations can't handle the twice-each-year releases because each release is such a massive change that it (a) never works and (b) there's no going back.  Folks in operations will -- easily -- handle a twice-each-week release because the releases will (a) work, and (b) have a clear fall-back to the previous release (except twice each year when there's no easy fallback.)



5.  Let the users -- not the developers -- determine the new features.  This is stated incorrectly.  The developers sometimes head down dark rat-holes of lost time.  Usually, it's the bone-head manager who started the project with "we have to add features to create sufficient value" that determined a list of useless gold-plating features.   Developers don't mind focus.  Empire-building managers will (a) add features and then (b) demand that something be shipped on-time even if it doesn't work.



:strong:`Making Changes`



This list is a handy recipe for making changes in an IT organization.  First -- of course -- people need to know that there's a problem.  You have to recognize that the waterfall model (Big Design Up Front) doesn't work; don't wait for your users or customers to tell you this.  (See `The Waterfall's Not Working <{filename}/blog/2008/02/2008_02_11-the_waterfalls_not_working_even_a_client_said_so.rst>`_ .)



Once you've recognized that the problem is the bloated process, you have to embrace real change.  Not "process improvement" where you negotiate over the details of how best to post revised project plans, but "process replacement".  Rethink things from the fundamentals.  (See `Why Agile? <{filename}/blog/2008/02/2008_02_14-why_agile_whats_the_point.rst>`_ )



Ultimately, the most significant thing is to recognize that :strong:`LEARNING IS NOT FAILING`.  When a project is cancelled or change, it may not have failed.  If the project's first few deliverables where really useful and valuable, maybe someone learned that the remaining phases wouldn't be valuable enough.  Canceling the project doesn't mean the project failed to deliver :emphasis:`value`.  It just failed to deliver the whole boat-load of crap that was initially set out in the project charter.



Then, consider the points from the Computerworld article.  #1 and #5 -- fold the users in -- are pretty clear.  The reason this simple advice is not followed, however, because IT management knows that users change their minds, which changes the scope of the project.  This "learning" behavior leads to change, and change to a project is usually labelled as "failure".  



After all, you can't plan for all the things the users will learn.  Since Big IT labels all change as "scope creep" and treats it as failure, they force the project managers to segregate users from developers.  In essence, a successful project is one in which nothing was learned and there were no midcourse corrections.  The initial estimates (no matter how fanciful) were met on time and on budget.



:strong:`Even Savings Are A Failure`



When the users learn that they missed something, scope expands.  No one likes this, so IT prevents it by doing BDUF.  It's stupid, of course, to demand omniscience, but it's a long-standing tradition.  The demand for omniscience is one of the biggest barriers to Agile techniques.



No one seems to want to make trade-off decisions.  The Big Design which was done Up Front identified "requirements" and we all know that "required" is absolute, final and non-negotiable.  This is silly.  Few -- if any -- users can unambiguously state what is "required" in the sense of absolute and final.  In reality, all "requirements" fall on the `MoSCoW <http://en.wikipedia.org/wiki/MoSCoW_Method>`_  continuum: Must have, Should have, Can have and Won't have.  In Big IT fantasy land, scope expansion in one area can't be counterbalanced by contraction in another.  It just expands.



When the users learn that they've asked for something of little or no value, scope should contract.  In most organizations, this is also labeled as Big Old Failure.  Project Managers are accused (accused! blamed!) for padding projects with tasks that eventually got cut.  Program Managers and Directors then start playing the "I'll only give you half of what you asked for because I know you're padding" game.



Learning and change should not be equated with failure.  Changes to scope are normal, expected, and hoped-for consequences of software development.  However, Big IT punishes change.   Aggressively.



:strong:`Foundations`



The best advice in the article are items #2, #3 and #4: small feature sets, powerful tools, frequent releases.  These form part of the technology core that supports the other Agile practices.  Without these foundational elements, the rest of the `Agile Manifesto <http://agilemanifesto.org/>`_  can't easily be realized.



To this, I'd add #6: Unit Test everything.




