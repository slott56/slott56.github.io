Lean Projects — Not Deficient Projects
======================================

:date: 2008-09-02 19:59
:tags: architecture,software design,complexity,management,agile
:slug: 2008_09_02-lean_projects_not_deficient_projects
:category: Architecture & Design
:status: published







Here's a great quote from a reader regarding `Big Plan for Change <{filename}/blog/2008/09/2008_09_02-the_big_plan_for_changetm_since_it_never_works_whats_the_alternative.rst>`_ : "[the advice] doesn't account for project tracking requirements of the organization. Budgeting. Metrics. Hiring. Documenting. Transitioning to new staff."



Good point.  Let's look at these in a little bit of depth.  We'll cover the three management practices first: Budgeting, Metrics and Personnel (Hiring and Transitioning to new staff.)



Budgeting
---------



Got to have budgets.  How much does a project cost?  How do we estimate the costs?  Two ways.  



In "`Why Agile? What's the Point? <{filename}/blog/2008/02/2008_02_14-why_agile_whats_the_point.rst>`_ " I talked a little about the cost and risk question.  Mostly from a risk point of view.  In short, with an Agile approach, the risks have almost no associated cost.  What little cost there is should be easy to manage.



But what about overall cost?  What's the "total cost to do [X]?"  Well...  First, we have to define [X] so we can define the total cost.  In order to define [X], we have to throw Agile out the window and create a **Big Plan Up Front**.  Oops.  That didn't work, did it?



So, what do we do about total cost?  The question has to be reframed.  There's a central issue here.  The central issue is this.



We Can't Know What "Done" Means
--------------------------------



We don't want to waste time trying to talk about "Totally Done" -- it's unknowable.  We can only talk about "Done Enough".  Projects often die because the scope is too ambitious or too nebulous.  



We can't know the total cost for [X] because we really don't know everything there is to know about [X].  Further, we know that the users are prone to lying, so we we can't ever be sure we really know what the totality of [X] is; [X] gets shifty and is hard to pin down.  Rather, we have to find out what the biggest share of [X] is; what part of [X] causes the most pain.



We have to avoid questions of total cost.  Instead, we have to reframe budget conversations as questions of the rate at which money is spent and the rate at which features arrive.  If we have people we trust with high-powered tools, they'll build us stuff at an acceptable rate.



At some point, the stakeholders will run out of high-priority, high-value things to do.  That's when we're approaching "Done Enough".



The Real Questions
-------------------



There are two questions more important than "budget" -- budget in the simplistic sense of "total cost".



The first question is one of performance.  At what rate will features arrive?   With an established staff and established tools, they should be able to commit to a rate of delivery that doesn't include a lot of surprises.



The second question is one of expectations.  At what rate do we need features?  This is a question to the stakeholders.  If they need a lot of features right away, we might have to assign a big team.  If they're willing to wait, we might get away with a smaller team.  After the first few releases, we can probably cut back on the rate of delivery.



Once we know our rate of delivery and our stakeholder's demands, we can figure out how many people we'll need.



But what's the duration?  



For large projects, the duration is "the rest of this year."  After all, that's the real answer most of the time.  And everything will be renegotiated next year.  Why pitch a multi-year plan when you have to redo it every single year?  Just pitch a "for the rest of this year" plan; that's the honest, useful truth.



For small projects, you might know that it's only a few releases or a few sprints.  For bug fixes it's usually one sprint-one release.  And you often have historical data with which to confirm this.



Bottom Line -- budget is easy.  It requires an honest assessment of multi-year projects: namely, you'll plan them one year at a time, since they're only approved one year at a time.



Metrics
-------



Many people are in favor of metrics.  `Jim Bullock <http://www.dorsethouse.com/authors/bullock.html>`_  says they're essential.  However, let's not waste a lot of time and effort on measurements we can't make much use of.



[I'm enamored of the "project dashboard" efforts to try and boil project status down to red, green and yellow lights.  The first thing everyone does is debate the metrics, since there's no standard practices for this.  Then, no one can supply "quality" data.  Why?  Standard reason: No stakeholders, nothing's at stake.  It's barely even a convenience item.  Seriously, what are the use cases?]  



Generally, metrics are either a part of the culture or they're a roadblock.  If you already measure and count stuff, then you've got metrics covered, and you can Start Now on meaningful work.



Metrics are a roadblock when you have to organize the metrics as part of defining scope and deliverables and budget and staffing and all the folderol we're trying to skip over.  If you feel metrics are necessary, then you've got to get started.  As with all things, start with one person; have them watch and count work products of one other person.  



They say "you are what you measure".  Consequently, the most important thing to measure is "delivered features".  Measure the following: request backlog, sprints and releases.  Start there.  For that matter -- since these are the things the stakeholders see -- end there, too.



They say "you can't control what you can't measure".  What's important, however, is that "you may *not*  be able to control the things you can measure".  You can measure the height of the tide, but you can't change it.  Be sure you understand cause and effect in the things you're measuring.  Don't measure stuff where you don't know or can't control the cause.



The hardest part about a metrics program is trying to use metrics to achieve organizational change.  It's really hard -- harder than you'd believe possible.  I saw one group try to achieve better reuse by measuring code delivered and code reused.  They, essentially, didn't count the reused code as part of a manager's overall delivery.  However, they measured productivity in lines of code per day.  So, when a manager elected to reuse some code, the team did some work for which there were no lines of code delivered.  The productivity metric would decline if you reused something.  This is the Unintended Consequence problem of trying to shape behavior with metrics.



Hiring and Staffing



First, I don't have much to say here that hasn't already been said.  Start by reading everything there is on `Pair Programming <http://www.agileadvice.com/archives/2005/04/pair_programmin.html>`_ .



I'm not sure that staffing is a proper project cost, *per se.*   I think it's an organizational cost.  I don't think a specific project should be hiring and training people.  You need to apportion those costs across all projects.  Maybe renting contractors, but not hiring permanent staff.



The customer sees the flow of features -- from backlog to sprint to release.  They don't see -- or care a whit -- about staffing to produce those features.  Since it's all about the feature, the customer is paying for features, not training.



As with backups, restores, networks, firewalls, storage, heating, ventilation, air conditioning, clean water and coffee service, staff is a kind of infrastructure.  Perhaps the most important infrastructure.



"But," folks say, "it takes time/effort/money/risk to bring a new person up to speed."  Agreed.  Do it quietly and quickly.  Agile suggests pair programming.  Two people linked with a chat client (or sitting in the same office) can get a lot done.  One can be junior and one can be senior.  It works great.  The cost to introduce someone new is really quite low when done this way.



Documentation



This is generally technical.  You've got to have it.  I didn't mention it because I thought it went without saying.  However, identifying it is good; it clarifies it as an Agile practice and prevents it from being overlooked.



I think that powerful documentation tools are essential.  And MS-Word (or Open Office) isn't one of those tools.  I really like tools like `epydoc <http://epydoc.sourceforge.net/>`_  for producing nice API docs from code.  I also like the `docutils <http://docutils.sourceforge.net/>`_  rst2html.py script for producing nice docs from simple text files.  90% of documentation is text.  Make life simple and simply type the text.  Formatting can be done separately using the simple rules of `ReStructuredText <http://docutils.sourceforge.net/rst.html>`_ .



Summary
-------



The bottom line is still embodied in two words: Start Now.  It means going easy on the up-front junk.



Getting started on an Agile project does not mean that we casually toss out "Budgeting. Metrics. Hiring. Documenting. Transitioning to new staff."  What it means is to do these things realistically.  You can't know everything.  Don't waste time making assumptions, then discovering the assumptions are wrong and revising the project plans.



Ask what the stakeholders need to know to commit to a decision.  They don't know everything, either.  They need to know enough.



Budget is a flow of money.  For big, multi-year projects, it's a flow for the foreseeable future -- so just plan one year at a time.  Don't make up a five-year plan that will get rewritten 20 times.



Metrics are a reflection of what has happened.  Be sure to measure things that matter. 



Hiring and staffing are the heart of Agile methods.  





Documentation is essential.  Tools matter.  Use the most productive tools you can find.




