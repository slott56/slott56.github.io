The Question of Risk (Revised)
==============================

:date: 2007-01-06 15:16
:tags: management
:slug: 2007_01_06-the_question_of_risk_revised
:category: Management
:status: published





Yes, it's an omission and, yes, it's a mistake. 
I should have said something along the lines of "risk is an uninteresting
complication" or "risk is just a euphemism for bad
management."



Why is risk
uninteresting?



First, the seeds (Chad
Fowler's "`The
Big Rewrite <http://chadfowler.com/2006/12/27/the-big-rewrite%22%20target=%22NewWindow>`_ ", and CodeCraft, "`To
Rewrite or not to rewrite, that is the question <http://codecraft.info/index.php/archives/69/%22%20target=%22NewWindow>`_ ") don't mention
risk.



Second, and more important,
"risk," as commonly used in IT planning, usually means "bad management".  Most
people will discuss risk in a broad, unfocused, intangible, "$#!+ Happens" kind
of way.  They say vague things like "How much risk is associated with this
project?" as if risk is a quantity.  Rarely will they talk about a specific
thing that might not turn out as planned. 




I think any discussion of risk has to
be separated into bad management and actual unplannable events.  The unplannable
events are
**real** 
risks like heart disease, cancer, stroke or motor vehicle accidents.  Almost
everything else that can go wrong is little more than bad
management.



There is no single, broad
"risk" associated with a software development project.  There are a number of
specific risks, each one is unique, and each is a symptom of bad management. 
Software development risks cannot easily be aggregated, except in a theoretical
`expected value <http://en.wikipedia.org/wiki/Expected_value>`_  calculation.  And even then,
that's dead wrong for software.



There
are many lists of specific risk factors.  The Visual FoxPro Wiki, for example,
has a Software Development Risk Factors http://fox.wikis.com/wc.dll?Wiki~SoftwareDevelopmentRiskFactors~VFP  page that's
handy.  Here is the heart of the problem:
**failing to address risks as discrete kinds of mistakes** .  Almost all of the things we see
as software risks are just bad management, each a kind of failure to cope with
ignorance.  I believe that, like an `architecture <{filename}/blog/2006/08/2006_08_22-a_new_architecture_involves_ignorance.rst>`_ , software development involves
strategies to manage ignorance.



[The
worst conversations are the "we don't know what we don't know, anything could
happen" conversations.  Those are exasperating.  You do, in fact, have tangible
risk models and lists of risk factors, better termed "potential
problems."]



**Software Risks are Different.** 



Software development
isn't like other construction trades.  We aren't building something, but
learning something.  Software development is all about knowledge capture.  Even
if we don't build the application software that was in the "Goals" section of a
project charter, we still learned something of
value.



From the old `Max Headroom TV series <http://en.wikipedia.org/wiki/Max_Headroom_(TV_series)>`_ , I learned,
"**There are no failed experiments, only more data** ."  This appears to be a paraphrase
of a quote from R. Buckminster Fuller, but I can't find a reference to Fuller's
original quote.



Software development
risk factors don't fit the standard mold.  Most risk analysis is based on the
probability of a loss: the house burns down, the bridge collapses, the culvert
washes out, the footings are undermined, the boat sinks.  Software doesn't
involve the same kinds of loss.  Indeed, it rarely involves any loss at all. 
Unless a server actually burns up, or all the people leave the organization --
taking all their notes with them -- you don't have a total
loss.



In software development, a
"failure" isn't like a classical "loss": you still learned something, and the
thing you learned
**is**  of
real value.  You may think that you only learned that you can't deliver 10
person-years of software in 1/2 a person-year.  But your requirements, designs,
and partial solutions all have real, tangible value, and can be reworked into
something.  The team that remains grew in experience, management gained some
knowledge, the organization learned
something.



**But the Labor was Wasted.** 



A software project failure
isn't even a total loss of labor hours.  You can only lose the labor hours by a
two step process: failing to deliver a solution to the problem and then firing
the every single person who learned the lessons.  When this happens, it
indicates a criminal disregard for how an organization accumulates knowledge and
skills.



Generally, a software project
"failure" is little more than excessive labor hours for relatively low-value
lessons learned.  You may, for example, learn that your customers lie, or can't
focus on a problem, or get distracted, or have no sense of perspective. You may
learn that your developers aren't very good.  You may learn that your tool
vendors misrepresented their products.  These can be learned more cheaply or
more dearly.  The most expensive way to learn these lessons is by investing
millions in software development only to learn that `everybody
lies <http://www.fox.com/house/>`_ .



Often, software
development projects are labeled "failure" for the wrong reasons.  For example,
we have some random business problem ("can't consolidate 85 spreadsheets").  We
have over-blown user requirements ("must include an in-ground swimming pool with
wide-screen underwater TV").  We fail to deliver on the requirements, the
project is labeled a failure and people are sacked.  However, the users changed
their processes and tools and can now consolidate with fewer errors.   The
business problem is solved, or perhaps reduced in scope or impact.  The
organization is satisfied and elects to focus on something that's more valuable.
How -- precisely -- is that a failure, other than a failure to deliver on
undeliverable
requirements?



**What Not To Do.** 



A software development risk
isn't a risk of a
**loss** . 
It doesn't have a win
*vs.* 
loss potential the way we see it in a simple expected-value calculation.   It's
just an unexpected outcome.  Or, more precisely, an outcome with a value that
isn't commensurate with the
cost.



Here's the biggest possible
project planning mistake:  adding contingency fees.  For example, there's a risk
of key staff not being available.  This has a defined project premium of 5%. 
This is unjustifiable since each situation is unique.  You should be asking
which specific key staff member?  Unavailable for what reason?  How do we
prevent that?  You should not be tacking money onto the
project.



Here's the second biggest
project planning mistake: trying to do expected value calculations.  For
example, there's a risk of low productivity.  We assign a cost ($100,000), we
assign a probability (0.10) and we compute an expected value of $10,000 for low
productivity.  Funny, this looks like the 5% premium, with more assumptions
folded in.  Again, this is unjustifiable.  Specifically, if you anticipate a
cost of $100,000 for low productivity, what's the investment to prevent this? 
You should be doing ROI calculations on your prevention
strategy.



Don't waste time on the odds
of "$#!+ Happens" and take action to prevent "$#!+ From
Happening."



**Project Strategies.** 



For now, we're stuck
with "potential problems" being called "risk factors".  It's common terminology
and hard to dislodge.  For each software development risk factor, you have two
strategies: prevent the problem and recover from the problem.  Indeed, all of
the software development risk factors I've ever seen are simply lists of
management mistakes, all of which are avoidable or
preventable.



You shell out money to
prevent problems.  Having done that, you can set aside contingency money to
recover if something doesn't go according to plan.  Since this is software,
there's
**always**  a
kind of recovery available; something of value can be retained. 




[What's distressing is the management
distaste for making intelligent choices that preserve value.  Instead we see
sweeping reorganizations that assure that little of value is
retained.]



If the technology doesn't
work out, you can switch to a new technology.  If your developers aren't up to
the job, you can hire or rent new developers.  If your users lie -- well --
you've got big problems, but there are techniques for managing even this.




Looking at list of `Software
Development Risk Factors <http://fox.wikis.com/wc.dll?Wiki~SoftwareDevelopmentRiskFactors~VFP%22%20target=%22NewWindow>`_ , we see that each one is a simple,
discoverable, preventable situation.  Some situations, appear to be difficult to
prevent.  Specifically, if we run afoul of the eight things in "`To
Rewrite or not to rewrite, that is the question <http://codecraft.info/index.php/archives/69/%22%20target=%22NewWindow>`_ ", we've done something
colossally stupid.  We've guaranteed that the project -- as planned -- can't
meet the expectations.



This leads us to
two kinds of project problems: **planning for failure** , and
**mismanaging ignorance** .  Both of these are labeled "risk",
but they're not random "$#!+ Happens".  They're not like ramming a `submerged shipping container <http://www.oceannavigator.com/article.php?a=1008>`_  and losing your
boat.  They're management dumbosity (a cross between dumbness and
pomposity.)



**Planning for Failure.** 



Here's a great example
from "To Rewrite..": "Do you honestly believe that if you rewrote it without
adding any features the resulting code would be 33% smaller than the current
code?"  If you can't simplify during the rewrite, then you've assured that you
will not achieve the desired simplification, and reduction in maintenance cost. 
Your plan --
**not**  to
simplify -- won't meet anyone's expectation of a better product after the
rewrite.



This isn't risk.  This is dumb
management.  Someone specifically planned to fail.  They may even write the plan
-- the plan that won't achieve the desired simplification -- down in glorious
detail.



**Failing to Manage Ignorance.** 



Here's an example risk
factor: "Large number of complex external interfaces".  When you think about it,
this is just ignorance.  This is basic dumb project management: proceed from a
position of ignorance and insist on a budget or schedule or
both.



Often, my customers demand a
price for something where I'm ignorant of scope or complexity.  I have to make
up a real number based on what I know and what I expect.  My assumptions (the
cost factors that are unsupported by facts) are sometimes called "risk" or
"contingency".  In reality, it's the cost of ignorance, and our expected labor
to overcome the ignorance.  We just can't call it "ignorance" in a
proposal.



This isn't risk.  Proceeding
without the facts is just dumb management.   There are better ways to manage
this than simply proceeding or declaring the potential cost too high and
canceling the project. 



**Bottom Line.** 



The usual sense of "risk"
doesn't exist for software development projects.  Unless you take "risk" as a
synonym for bad management.  



Yes, bad
things can happen that are not foreseeable.  However, for a software development
project they are the same as they are for throwing a party with the same number
of people.  They risks are microscopic, and involve things like "heart disease",
"cancer", "stroke", "motor vehicle accident" that you'd find any `leading
cause of death <http://www.cdc.gov/nchs/fastats/lcod.htm>`_  or `odds of
dying <http://www.nsc.org/lrs/statinfo/odds.htm>`_  table.  (Note that the top three killers are diseases often
managed by life-style
changes.)



Projects don't "fail" in a
broad and vague way.  Managers either create a plan that can never meet
expectations or they create a plan that doesn't manage ignorance.  Then they
execute that plan until someone with budget authority realizes that the plan
isn't producing value commensurate with the
cost.



Maybe I've spent too much time
reading `Software
Craftsmanship <http://www.mcbreen.ab.ca/SoftwareCraftsmanship/%22%20target=%22NewWindow>`_ , but I think that the incremental, `Scrum approach using TDD <http://www.scrumalliance.org/index.php/scrum_alliance/for_everyone/learning_scrum/weekly_column/weekly_column_5_15_2006>`_  is the only thing that
makes any sense.  Build in small pieces, each one of which creates
value.








