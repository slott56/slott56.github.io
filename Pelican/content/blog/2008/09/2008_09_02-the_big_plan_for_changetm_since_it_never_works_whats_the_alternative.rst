The Big Plan For Change™ -- Since it never works, what's the alternative?
=========================================================================

:date: 2008-09-02 10:23
:tags: architecture,design,complexity
:slug: 2008_09_02-the_big_plan_for_changetm_since_it_never_works_whats_the_alternative
:category: Architecture & Design
:status: published







See `Fast, but Slowly <http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=324808>`_ .  ComputerWorld, Frankly Speaking, August 25, 2008, by Frank Hayes.



This is a very cool restatement of some essential Agile principles.



:emphasis:`Sure, we can train and plan -- and we should. But there are too many unknowns to train and plan for everything. A slow ramp-up lets us discover and kill problems as we go, reducing complexity at every step. Going slowly means fewer changes at once, fewer nasty surprises, fewer problems leaking out of the data center. It also means direct, desperately needed experience.`



:emphasis:`But to go slowly, we have to move fast. We can't wait for an ROI analysis or a line item in the budget to start getting that experience. We can start right now, today, with a tiny pilot that gets us moving.`



Thank you Frank Hayes.  



:strong:`Planning Is Important`



The last refuge of the technologically obsolete manager is planning.  If you can't understand all the new techno-mumbo-jumbo, you can at least understand dates and budgets.  Right?



Wrong.  If you don't get the techno-mumbo-jumbo, you need to invest more time with real technical people soaking up the technology.  Watch the team at work.  Don't coach.  Watch.  Don't answer your phone.  Don't yammer.  Watch.  I've seen this done, and it works.



A realistic plan requires a realistic understanding of the technology. 



:strong:`A Case Study`



For example, let's talk about introducing some kind of configuration management for the DBA's.  (See `The Schema Evolution Problem <{filename}/blog/2008/08/2008_08_06-the_schema_evolution_problem.rst>`_.)  Doesn't that require a :strong:`BPFC` ?  How will we achieve "control" without a plan?



A plan is not step one.  A plan is not important or even very helpful.  At best it's a distraction.  At worst it takes on a life of its own and replaces real work with servicing the plan through short-cuts and work-arounds.



Step one is to understand what we mean by "control."  Not the dictionary definition.  Not the wikipedia definition of `Configuration Management <http://en.wikipedia.org/wiki/Configuration_management>`_  or `Change Management <http://en.wikipedia.org/wiki/Change_Management_(ITSM)>`_ .  That's evasive -- evasive in a criminal kind of way.



Before embarking on a formalized Schema Evolution exercise, step one is to gather specific use cases for the configuration management processes.  In the current organization, who are the stakeholders?  What do they need to know about the current configuration?  What will the developers do?  What will QA do? What will the DBA's do?



Before doing anything, we need to identify who has a stake in configuration control, schema version control and change management.  Everyone's involved.  Who's committed?  Who should control configuration of the various development, test and production realms? What are the various actor's goals?



Review the old saw about the ham and eggs breakfast.  The chicken is involved.  The pig is committed.  Who are the pigs?  Who are the chickens?



The point is :strong:`not`  to write specific, detailed scenarios.  We're just going to summarize their goals; summarize their interactions with some "system" that will manage change and control configurations.  We need guidance on tool use.  We don't need yet another set of "requirements" that allow someone to engage in lots more programming.  The point is to increase control and reduce cost, not write more stuff.



[The most dangerous person in the organization is the person who wants to spend all day writing Visual Studio plug-ins to "automate" some task that isn't very complicated in the first place.  Sigh.]



:strong:`Now Do We Plan?`



Now that we have identified stakeholders, goals and use case summaries (no steps, just overviews), we have a jumping-off point.  But not for planning.



What we have at this point are people who make all kind of outrageous claims.  Everyone wants to be in charge -- they claim they're pigs -- but they're mostly just chickens.  The claims are contradictory.



The DBA's, generally, claim that they own the configuration.  They control the stored procedures, but not the application software; leading to a split in the software.  They can't really justify their position, it's got too many holes in it -- they answer to users for production operations as well as new development. 



The Developers, generally, claim that they own the configuration, since the database is just there to support their fancy new applications.



QA, interestingly, often says that they don't own the configuration.  I've met a fair number of QA folks that are behind the technology curve and don't feel comfortable "owning" the configuration.  Instead, they tolerate someone else owning configuration and track the changes from a safe distance.



Project Managers will often try to control the configuration by issuing random orders from time to time.  "Don't change anything without checking with me" and "Fix something as soon as you know it's wrong" being the usual contradictory orders.



:strong:`You Say You're A Stakeholder`



The phrase Stakeholder is usually a broad, vague thing that encompasses everyone.  But who has something "at stake?"  Who has something they'll lose?  And how significant is that loss?



DBA's, for example, have no skin the game.  If nothing changes, they're happiest.  For them, an immutable configuration where they do backups and run SQL as part of production operations is the ideal.  Why try to introduce change management or version control to people who explicitly reject it?  DBA's often act as the technical hands pushing buttons on behalf of the users.  The users have more to loose than the DBA's.



[Most DBA's will tell you that change control on a schema is impossible.  They reject `Agile Database Tools and Scripts <http://www.agiledata.org/essays/tools.html>`_ .]



Developers have a something at stake.  If they're doing bug fixes, they need changes to be marched through some QA into production.  They're interested in improving existing production operations.  Developers doing new development, they have a new environment or application they need created, qualified and commissioned for production use.  They're interested in creating new production operations.



In my opinion, QA has everything at stake.  They are -- in principle -- responsible for production operations, change fixes and new development.  QA has to be an active participant in change management procedures; they (and only they) can manage the configurations running in each working realm (production, test, development, etc.)  QA has to be able to use SVN (or CVS or whatever) to confirm what's there and what's supposed to be there.



I think QA are the pigs in this ham-and-eggs breakfast.  Everyone else is just a chicken.  The users should be working directly with QA.  QA should be actively managing DBA and developer changes to provide an Information Technology architecture that meet the user's needs.



:strong:`Okay, We've Resolved the Conflicts, Now Can We Plan?`



Once we've worked out who the actors really are, and what they need to know, the rest is simply following Frank Hayes' advice.



Start a pilot.  Without a plan.



Start with one person working with QA to put one thing under configuration control; create the necessary change management; identify how to do version control.  Often, we have some of this in place for some of the source code.  Rarely does anyone have this in place for DDL and configuration files.



So, simply expand the existing repository to contain one more thing.  Just one.  Pick the highest priority, most problematic, biggest, ugliest problem.



Usually, it's something like stored procedures not matching between databases.  Just start there.  We already have some application source; why not get the rest of the application code under control?



Get just the stored procedures into SVN.  Get the checkout areas squared away for each realm (test, production, QA, development, etc.)  Get things in and out.  Create branches and start tagging just the stored procedures.



Live with this a while.  Get this under control.  Don't put a date or a deliverable around it.  Learn some lessons.  Make changes.  Back away from mistakes.



:strong:`Okay, We Finished The Pilot.  Now Can We Plan?`



Planning prematurely is a mistake.  One set of lessons learned doesn't reveal too many reproducible patterns.  Patterns become visible after you've done something two or three times.



So, find the :strong:`Next Big Thing`.  Start a "round 2 pilot".  Not a full implementation.  No concrete plan.  Nothing so serious as that.  Just pick something that's out of control.



For example, table definitions that don't match.  Start putting DDL into SVN.  Work out a way to compare a schema in the database with the DDL in the SVN source area.  (This is pretty hard, and often involves creating a temp DB and comparing the an established schema with the temp schema.)



Work out a solution for the ALTER problem.  It's often best to rewrite the table CREATE statement, and provide a separate ALTER as a kind of one-use-only script.  Some people can't -- for some reason -- make this work, and have to execute the historical sequence of creates and alters to get a schema into a trusted configuration.  You need a way to match what you start with -- a change -- and what you end up with -- a schema.





Expand the repository to contain one more thing.  Live with this DDL management for a while.  Create branches and start tagging the CREATEs and ALTERs.



Live with this a while.  Get this under control.  Don't put a date or a deliverable around it.  Learn some lessons.  Make changes.  Back away from mistakes.



:strong:`Fine.  We've Done The Pilot Twice.  Now Can We Plan?`



Now that you have useful lessons learned -- and enough experience to see patterns emerging -- feel free to plan away.



What's left is usually the configuration files themselves.  All of the various settings and what-not that configure each piece of the technology stack.  That's usually pretty straightforward to put under control.



You'll notice that what's left after that is minor.  You've already tackled the stored procedure and DDL problems.  There won't be much budget or enthusiasm for the few things that remain.  Feel free to plan -- that will allow for lots of high-level meetings where nothing gets done because nothing's at stake.



The remaining things will be resolved by people saying "Why isn't the index creation in the repository?"  Or "Why aren't the backup scripts in the repository?"



At that point, stuff will move into the repository with no plan, no powerpoint, no budget, no management buy-in.  Folks will have the experience and the enthusiasm to put stuff under control without an elaborate management ritual.



:strong:`Wait -- what?`



How did something happen without a plan?  How can we fix our CM problem without a BPFC?  



Easy.  If you start small enough, you don't need a big plan.  The Big Plan for Change usually fails to identify what's at stake, and who's bearing the brunt of failure.  With nothing at stake, nothing needs to change, and nothing gets done.



Configuration Management -- like many things -- can be tackled incrementally.  You don't have to boil the entire ocean; you just need to establish one best practice cheaply, simply, quietly and -- above all -- immediately.  Find the biggest problem.  What's at stake?  For whom?



The "whole job" may appear big.  But that doesn't mean it requires a big plan.  It requires a small statement of vision.  Then, use the following two words: "Start Now."




