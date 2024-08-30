Estimating, and the Unknown Unknowns
====================================

:date: 2007-11-11 20:17
:tags: Risk,Unknowns,Estimating,Planning,Project Management
:slug: 2007_11_11-estimating_and_the_unknown_unknowns
:category: Management
:status: published







Back in the olden days (ca. 1981) Barry Boehm's Software Engineering Economics provided a detailed and definitive guide to estimating.  It did one really important thing: it provided a conceptual model of software development that had a (relatively) focused set of degrees of freedom, an input driver and a couple of outputs.  This model, the Constructive Cost Model (COCOMO) had the advantage of formality and a solid basis in repeatable metrics.



The problem is that the model is circular.  Ideally, we want a model that's like the Function Point model: **Requirements In → Software Out** .  The function point folks evaluate five aspects of the requirements and from those aspects determine the effort, schedule and cost.  The FP aspects are Internal Logical Files, External Logical Files, External Inputs, External Outputs and External Inquiries.  Note the emphasis on externally visible features, and the emphasis on the essential ingredients of software.



COCOMO, unfortunately, gives us a model that is **Lines of Code In → Software Out** .  Wait, how can we know the lines of code going in?  We can't, but we can estimate the lines of code going in, and from that, deduce the effort, schedule and cost.



You could deprecate this by saying that we've merely replaced estimating everything with estimating lines of code.  The problem hasn't gone away, it's only shifted.  The good news is that we've replaced a vague estimation of everything, with a fact-based estimate of lines of code.  From that, the model gives us effort, schedule, staffing and cost.



Joel's technique isn't really modeling software development, per se.  Joel's technique is to model the estimating process and show how well people adhere to their estimates.  In short,**Estimate In → Estimate Out** .  This is clearly indirect stuff, since we're modeling our ability to manage estimating, not the work itself.



Accuracy Issues
---------------



Of course, COCOMO (or Function Points) or even Joel's "Evidence Based Scheduling" have no basis in reality.  More precisely, they have no basis in the reality in which you are currently working.  Clearly, all of the COCOMO numbers are true; but only for those projects, that technology, those managers and customers.



Joel suggests (just like Boehm before him) that it's all about repeatability.  He says that small steps, clear measurements (elapsed time in Joel's case, effort in Boehm's case), a model and active management are essential.  He also says what Boehm says in chapter 32: gather data to fine-tune your estimating.



The modeling can't be emphasized enough.  The original idea was that duration (or effort) are defined by a function that varies with the scope of work.  Joel's indirect model refines this by saying that actual duration is defined by a function that varies with the person and their original estimate.



With enough history, the estimates will tend to get very accurate.  As long as everything else is held constant.  Sadly, nothing else is ever held constant.



Into the Fog
------------



If we're doing anything of value, it almost always involves some novelty.  As I said in "`A New Architecture Involves Ignorance <{filename}/blog/2006/08/2006_08_22-a_new_architecture_involves_ignorance.rst>`_ ," we don't start software development unless there's something we don't know.  If the solution is perfectly well understood, we're very likely to be talking about something we can just download and use.  If the problem is well understood, it's likely that we already have some software in place, and we can measure that software.  Many times, the technology involves something new or untried.



The alternative -- where everything is known -- is little more than a classroom exercise.  The only way to know everything is to have working software that we're essentially re-implementing.  What's the value in that?



Once we're tackling a new problem, creating a new solution or using a new technology, our previous estimating history database is of limited value.  Our new technology projects can't be compared to our old technology.  My personal database of C programming measurements just don't apply to Java programming.



While it's important to gather data, it's also important to recognize the limitations of gathering data when there are few constants.



Design First
-------------



A colleague pointed out Joel's article.  They said that this was a way to show that estimating requires a design first.  I think that the points from my colleague were the following:



There's a management fantasy that initial estimates actually mean something.  We have limited knowledge, but managers ask for estimates anyway.



Once we start designing, we're chided for changing the estimates.  As we gain knowledge, everything we learn is treated as a problem.  Trying to adjust scope is called "scope creep".  Trying to adjust estimates upward is called "out of control".  Trying to adjust estimates downward is called "sandbagging".  We can't win.



My colleague wanted the article to somehow help clarify the relationship between estimates and knowledge.  I don't think it can.



The Unknowns Have It
--------------------



I think that our human tendency to be deeply risk-averse makes it nearly impossible to produce an estimate of software development effort.  We have to guess about something (unless we're just doing a classroom exercise.)  



If we guess, we stand a chance of being wrong.  Each mistake -- each course correction -- is a potential failure.  Ask anyone who has budgetary responsibility for software development: change is magnified to include "loss", "devastation", "waste", "mistakes", "errors", and every other kind of negative connotation.



We all know that software developers are hobos, tramps and thieves.  We're not to be trusted.  We're lazy sandbaggers.  We estimate low so we can win the bid and then charge more through change control.  We estimate high so that can slack off.  We expand scope to build an empire.  We contract scope to make the project worthless.



There's no good outcome.  Joel's advice might be helpful, but you're in a battle you can't win.





