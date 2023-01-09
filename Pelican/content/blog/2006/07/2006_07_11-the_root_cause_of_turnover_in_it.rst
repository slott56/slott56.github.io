The Root Cause of Turnover in IT
================================

:date: 2006-07-11 14:40
:tags: management
:slug: 2006_07_11-the_root_cause_of_turnover_in_it
:category: Management
:status: published





Why does IT have such a high turnover?

-   Technology appeal?

-   Money?

-   Boredom?



No.  None of those.  We can
look at Maslow, but it's too high-level.  

-   Self-Actualization?

-   Self-Esteem?

-   Belonging?

-   Safety and Security?

-   Physical Needs?



Most IT jobs pay pretty well,
above the median income.  Look at `MCP Magazine <http://mcpmag.com/salarysurveys/>`_  or `InformationWeek <http://www.informationweek.com/731/salsurvey.htm>`_ , for example.   Compare this
with `census <http://www.census.gov/hhes/www/income/income.html>`_  data on income
levels.



So, we're into the belonging,
self-esteem and self-actualization levels of Maslow.  This post isn't going to
beat the standard drums of bad management.  This isn't about managers who don't
listen, or managers who aren't flexible, or that
junk.



No, the reason IT people turn
over so quickly is because they are **forced**
out by a manager's appallingly bad problem-solving
skills.



**The Curtain Rises** 



Projects start with an
initiating incident, a situation, a stumbling block.  It's generally something
trivial, but it's the last straw, the one that broke the camel's
back.



For example, we have a data feed
that contains labor records that are filled with errors.  We can't, however,
reconcile those errors unless we put the labor records side-by-side with
invoices, bills, production schedules and some other stuff to get really solid
comparison reports.



While ugly, it
isn't a problem until someone gets sick while someone else is on vacation, and
management discovers this rat's nest of spreadsheets, MS-access databases, and
ad-hoc processing to try and locate the labor hour reporting
problems.



Management's solution:
**This Requires Software** ™.   Note that we haven't stated
a problem, or really talked rationally about candidate solutions.  We've leaped
past all of the thinking and picked the latest and greatest buzzword; in this
case, **Data Warehouse** .



**The First Act** 



Once we've determined
that our labor hour problem is repaired by a Data Warehouse, we immediately hire
someone to build one of those warehouse things. 
Immediately.



The important thing about the *immediately*
is that we haven't really spent too much time thinking this through.  We've
drafted a project charter that amounts to the following:

1.  Problem: We don't have a data
    warehouse.

#.  Forces:  We can build or we can buy.  We can
    use contractors or in-house staff.

#.  Solution: Build a data warehouse.

#.  Consequences:  We can use this for things like
    resolving labor reporting.



Note that
the real problem (incorrect labor reports) is tangential -- almost irrelevant --
to the project charter.  We've managed to refocus from the real problem to some
technical thing that we *hope*
will solve the problem.  We can't prove anything, since we leapt past problem
definition to designing the software solution.



There are two branches in the road: Contractors or Staff.



There's a
hiring freeze (or we can't justify hiring more staff), and we have to bring in
Contractors.  

-   If we're disciplined, we require a
    Statement of Work, and an estimate.  The estimate shows that this project is
    expensive and daunting.  We're forced to actually think through the "situation",
    the "problem" and what we're pitching as a solution.  This is unpleasant, and
    often causes us to abandon the DW, and just fix the reporting problem.  Note
    that we didn't pay the contractors for their help; indeed, we complained about
    their solution being "too vague" because it reflected the vagueness in the
    request for proposal.

-   If we're not disciplined, we bring in
    contractors, and start paying.  After a while, the warehouse they're building
    diverges from the situation we hoped it would address.  We fire the contractors
    after spending millions on a non-solution to the unstated problem.  Consequence:
    turnover in the contractor
    organization.



We hire someone, and explain the situation.  They're happy to have a job.

-   If we're disciplined, we demand a project
    plan.  It proves expensive and daunting.  Now we're forced to think through the
    "situation", the "problem" and what we're pitching as a solution.  We reassign
    our warehouse person.  Effectively lying to them about the job and the goals. 
    Consequence: turnover.

-   If we're not disciplined, but still
    managed to hire a self-starter, they start work.  After a while, the warehouse
    they're building diverges from the situation we're addressing.  We wind up
    reassigning the warehouse person.  We have -- effectively -- lied to them about
    the job and the goals.  Consequence:
    turnover.



**The Second Act** 



The contractors (or the staff)
have built a warehouse-like thing that doesn't quite address the situation. 
Performance is bad, and it's mission critical.  Why is performance bad?  We told
people to stop gold-plating the application, just get something into production
on the given date.  In effect, we mandated bad performance by insisting that the
date was more important than anything
else.



Since performance of the
warehouse-like thing is bad, and it is also mission-critical, we now need
someone to speed up the performance of the application.  Recall that we either
fired the contractors or reassigned the staff.  After being lied to, they left.




We are forced to bring in more
contractors (or more staff) to address performance.  We describe the half-baked
data warehouse.  We describe the situation.  Neither add up to a "problem" with
a "solution".  Instead, it is a rapidly worsening
"situation".



Indeed, we are
specifically asking the new person for a `Faerie Dust Solution™ <{filename}/blog/2006/06/2006_06_19-faerie_dusttm.rst>`_ ; something that it
is impossible to deliver.  We want it faster, but we won't allow changes to the
data structures or algorithms.  Indeed, we don't really have time for a lot of
analysis, we just need it fixed.  And we all know that "analysis" is just a
rat-hole of lost time.



In spite of the
obvious Fairy Dust, who wouldn't stick around to catch a few paychecks?  It's
okay if the underlying problem is off limits, technology change is off limits,
and the existing architecture is sacred; it's okay if the organization must
"preserve the investment."  Getting paid to listen to this nonsense is better
than not getting paid.  Anyone would listen to this for as long as we're willing
to pay them.



So, when the contractors
(or staff) fail to make significant performance improvements, they're fired or
reassigned.  In effect, we lied to them to get them on board.  We told them
about a thing we're calling a warehouse which doesn't really exist.  We told
them about an architecture that doesn't really work.  And, best of all, when
they found the real labor hour reporting problem, they stopped making progress
on the **Software** we've been imagining since the curtain went up.




We reassign them.  They quit.  We created more turnover in IT.



Note that the fantasy **Software**
(which somehow improves something about labor hour reporting or error
correction), may be little more than a hack-around to one or more broken
business processes.   It also may be a solution that got conflated with random
Data Warehouse buzzwords.  Either way, we're lying about the problem and the
solution.



**The Third Act** 



The third act is a strategic
refocus on -- whatever.  The project is either cancelled, or suspended, or put
on hold, or rescoped.  The words don't matter.  What matters is that there's a
change in the project and the people involved are not doing what we originally
asked them to do.



We have, in essence
asked them to be something, and then devalued that thing.  They quit.  We create
turnover by creating a situation in which people cannot
succeed.



**We can't fix it** 



Clearly, this is the way IT is. 
It is an inescapable consequence of applying technology to information that
projects get cancelled, scope changes, people get
reassigned.



Right? 




I disagree.  Scope-change is not a
logical consequence of IT.  Scope-change is a logical consequence of wrong
scope.  Wrong scope happens for two reasons.

1.  Defining scope in the first place.  If we do
    away with "scope", we do away with "scope creep".  This is -- superficially --
    ridiculous.  However, after reading an `Agile Manifesto <http://agilemanifesto.org/>`_  and looking at Agile
    methodologies, part of the reason Agile techniques work is because the static,
    fixed, **Grand and Glorious Greater Scope** , is set aside for something more
    realistic and useful.

2.  Defining the wrong scope.  If we must have a
    scope, why can't we have a scope that defines real problems that real people
    really have?  Why do we have to write vague (incorrect, misleading) statements? 
    A generalization is the same thing as under-specification; why do we complain
    when our specific problem isn't solved by a general
    solution?


We define the wrong scope for a number of reasons.

-   We're afraid of "point solutions".  Why
    solve this one problem?  That's a lot of money.  Why can't we solve something
    more general, and get more bang for our buck? 
    *We don't want to solve the "labor hours problem", that's too specific.  We want to solve all data reconciliation problems.* 

-   We're afraid of "naming names". 
    Identifying a specific problem can result in embarrassment, termination or legal
    action.  *The labor hour reporting involves subcontractors behaving badly, or it involves purchasing behaving badly.  Some of it could -- actually -- be illegal.* 

-   We're afraid of "root causes". 
    Identifying the root cause of a problem can require a lot of cooperative work,
    and may put us in the position of naming names.  If we focus on the technology,
    not the organization, we don't have to do as much work, and we don't run the
    risk of embarrassing (or angering) someone important. 
    *If we locate the real reason for contractors misreporting their hours, it may involve incomplete work planning or incomplete task assignments.  It may involve rotten communication with our subcontractors at any of a large number of organizational touch-points.* 

-   We're afraid of "becoming a target".  If
    we're very specific, someone else may fix the problem another, cheaper way and
    we're left with nothing to do.  Worse, if we're specific, the Talmudic scholars
    and lawyers can spring out of the woodwork, split hairs, and prove that our
    specific problem never existed in the first place.  Either way, we're an
    embarrassing nay-sayer, describing problems that are already solved or never
    existed as described.  *After writing an RFP, the manager of purchasing may fix the touch-point, providing better and more complete information to the contractors.  Or, a legal-eagle may say the the definition of "labor hour input" is incorrect, and "input" doesn't happen when they enter the hours, but when the hours are accepted.  The "incorrect" situation happens "before input".  The problem is reframed into something new.* 



**The Illusion of Control** 



What do these things have
in common?  Most of these are about the
**Illusion of Control** .   When we wring our hands over the
cost of a point solution, we're really admitting that (a) the problem isn't that
valuable and (b) we can't find a fix with a cost commensurate with the value. 
Who wants to admit that they can't control what's going on?  When we avoid names
and root causes, we're protecting someone else's Illusion of Control.  If the
problem slips away from us (solved or reframed out of existence) we appear to
have lost control.



To maintain our
Illusion of Control, we define scope badly.  Sometimes we don't define the scope
at all, which gives us a very satisfying feeling of control.  By failing to
define the scope correctly, we wind up misleading people, reassigning them, and
creating IT turnover.



Turnover isn't
part-and-parcel of IT.  Nor is scope creep.  It's all just failure to focus on
the actual problem.  It's really our feeble efforts to maintain the Illusion of
Control.



**What do we do?** 



How do we reduce IT turnover? 
Easy:  be honest.  Define project scope correctly.



Define the real problem: if
the cost to fix is out of line with the cost to leave it alone, so be it.  Name
the names: if people don't like it, either you've fixed the organization, or
you'll be invited to leave a dysfunctional organization.  It doesn't look bad on
your resume, since you can document the real reason you were pressured out.  It
isn't "just political" anymore, it's specific bad
behavior.



Find the root causes: 
they're cheaper to fix, and the fix is permanent.  Be a target:  if the problem
gets solved (or reframed out of existence), act like you own the solution;
follow up with metrics on how well you did the problem identification and how
well you motivated others to solve
it.



When you hire (or rent) people,
they'll actually do what they're expecting to do.  There won't be the same
egregious level of scope creep.  People will tend to stay where they're
valued.






























