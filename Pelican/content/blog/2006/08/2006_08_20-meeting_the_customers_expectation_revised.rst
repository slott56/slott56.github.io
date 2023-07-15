Meeting The Customer's Expectation (Revised)
============================================

:date: 2006-08-20 15:26
:tags: architecture,software design,complexity
:slug: 2006_08_20-meeting_the_customers_expectation_revised
:category: Architecture & Design
:status: published





The customer -- usually someone from IT -- has
met with the users, and determined what their problem is and what is required to
solve it.  This is the standard procedure, but it rarely works out well.  Here
are some scenarios and some coping strategies.  After some hand-wringing about
scope and budget and how to engage usefully, a two-step process is
identified.



**Unbounded Specifications.** 



The customer wants
a "simple" program to do [X], but hasn't actually written [X] down completely. 
Any further conversation generally points up the lack of a fixed list of
features that constitute [X].  If there is something written, the material turns
out to be incomplete.  Indeed, in many cases, the definition of [X] seems to
vary during the conversation.  At the end of the meeting, we often ask the "what
do you expect?" question, and get answers like "We'll supply more definition,
then you supply an estimate."



So what
was their going-in expectation?  Did they expect to discover their documentation
was non-existent or incomplete?  Clearly not; no one calls and says "would you
QA our Request for Proposal?"  



They
must have thought that their specifications were complete and usable and that we
would thank them and provide an estimate.  Why did they think this?  They don't
seem to have a lot of internal discipline in the first place; it must be that
they rarely involve outsiders; they must be so used to clever people who fully
understand the user's needs that documentation just isn't part of their
world.



Is the customer's expectation
wrong?  By definition, it isn't wrong -- we should sell what the customer is
asking to buy.  How can we satisfy this customer's expectations?  How can we
breeze in and create software without a well-bounded
specification?



**The Problem Doesn't Matter.** 



The customer wants
a simple program to do [Y], but [Y] is nearly incomprehensible.  So, we ask for
the problem which is being solved, or the context in which the software might be
used.  There's a fork in this road: either they refuse to provide it, or they
game the problem.  We'll look at the refusal path, since that's quite
common.



When we ask what problem they
have and how a program to do [Y] addresses that problem, we often get a strange
circumlocution.  In one case, for example, the customer told us that they needed
to reduce their personnel costs.  They had about 120 people on the payroll,
removing one will save less than 1%.  Can we focus on something more serious? 
It was a $500M manufacturing company; clearly their raw materials were
dominating their cost structure, not their personnel costs.  Their whole payroll
couldn't be more than 20% of their
costs.



In  other cases, the description
involves so many unknowns and unknowables that it clearly becomes silly, even to
them.  They can't provide start dates, or test data, or a tool set.  Perhaps
they don't have hardware or infrastructure.  They may be vague on the users, or
who will ultimately control the software.  All they have is a deadline which
cannot be missed, and the specification for
[Y].



My personal favorites were the use
cases which all began with "we could...", or "it would be great if..."  Nothing
was definite, and their current business practices weren't -- it appeared -- a
model for the future business practices.  There wasn't a tangible problem to be
solved.



In other cases, the answer is a
curt, "We've already thought about that, and this is optimal."  And that's the
end of it.  They've already thought it through.  However -- and this is the
interesting point -- they can't (or won't) articulate it.  Maybe they think that
compartmentalizing the solution prevents any one person from seeing the overall
pattern and doing something malicious.  Maybe they're just domineering and feel
that dribbling out information puts them in
control.



What was their expectation? 
They expected us to salute, provide a price, and start programming.  From our
point of view, as vendors, we hate to program up a storm only to have the
product rejected because "it didn't solve the business problem."  It did the
parts of [Y] that could be done (we didn't do the other parts that involved
time-travel, anti-gravity or perpetual motion), but that's not good enough. 
Merely doing what they asked didn't solve the business problem -- and it's now
our fault.



They assure us that we're
not on the hook to solve the business problem, we're only responsible for [Y]. 
But that's often a lie.  When [Y] doesn't solve the business problem, that
ridiculous assurance flies out the window, and we're into doing rework on [Y] to
make it solve the business problem.



How
can we satisfy this customer's expectations?  How can we breeze in and create
software when they won't state the business problem that it solves?  Clearly, we
can play this game by becoming Talmudic scholars, scrutinizing every word,
writing a pile of assumptions and looking out for violations of those
assumptions.  Is this what the customer really wants?  Or do they want the
unstated problem solved, irrespective of the non-solution specified in
[Y]?



**Find A Problem for Our Solution.** 



The customer wants a
simple program to do [Z], but [Z] is nearly incomprehensible.  So, we ask for
the problem which is being solved, or the context in which the software might be
used.   In a few cases, the customer may ask for help in formalizing the problem
in order to assure that [Z] really does solve the business
problem.



In one case, [Z] had only one
sentence of user-oriented requirements, and pages of items out of the `SEI Quality Taxonomy <http://www.sei.cmu.edu/str/taxonomies/view_qm.html>`_ .  They had made an effort
to capture the business problem, but fell short.  They were willing to consider
the possibility that their requirements were not up to snuff.  However, they did
steadfastly refuse to engage in characterizing the business problem, and kept
their focus squarely on building technology.  In the end, we built mountains of
software to work around something that was never very
complex.



What did the customer expect
in this case?  They wanted someone to state a business problem for which [Z] was
the solution.  Failure to do this meant either declaring "Scope Creep", or
gaming the process by editing everything to make [Z] the
solution.



How can we satisfy this
customer's expectations?  How can we breeze in and create software when they
want us to help them look for the business problem that fits their preferred
solution? 



**Strategies for Coping.** 



How can we breeze in and
create software without a well-bounded specification?  Or, if they have a
specification, how can we create software when they won't state the business
problem that it solves?  Worse, how can we create software when they want us to
help them look for the business problem that fits their technology
choice?



Customer Education is
challenging.  Their expectation is that they are right.  They write software. 
**They Know What They're Doing** ™.



How
do we sell into unbounded specifications?  Essentially, we have to ease into it
with them.  An Agile strategy can let us build something quickly, and charge for
each working deliverable.  However, this is "pay as you go," which leaves some
executives confused about how much the whole project will
cost.



How do we sell when the problem
doesn't matter?  Again, an Agile approach may help them see that their
specification was way off base.  As we engage with real users, however, and
uncover the real problem, what happens next will be called "scope creep", and
the project will be cancelled.



How do
we sell when we're looking for a problem that fits their chosen solution?  When
the problem isn't solved by the chosen technology, an Agile approach will
immediately get stopped because it looks like scope creep.  While unpleasant,
this is necessary.



**The Agile Dilemma.** 



An Agile approach can fall
apart when the customer asks for the evil "budgetary" or "overall" estimate. 
This estimate -- BTW -- is silly.  They have a budget already, our input isn't
going to change that budget.  In all cases, the decision is nuanced, but  we're
not allowed to participate at the "negotiate a reasonable solution for the
available budget" conversation, because we're evil and we'll only soak up all
the available money.  



Worse, any
number you name -- especially when they say "we won't hold you to it, we just
need a number" -- becomes the price, and nothing can change that.  A reduction
in scope means you lied about the initial estimate to get more money than it was
worth.  An increase in budget to add features means you lied about the initial
estimate to get in the door and get more money through change
orders.



**Scope and Budget.** 



Balancing scope and budget
is almost impossible because -- as outsiders -- we're not allowed to participate
in that conversation.  If the customer doesn't often formalize things, then
scope is flexible; after all, everyone knows the real business issue and can
make all of the necessary prioritization and tradeoff decisions on a daily
basis.   When we provide a budget, the project gets cancelled:  too expensive. 
We can't put down features as line-items, since they aren't
known.



If the problem doesn't matter,
then tradeoffs are impossible.  The technology is fixed, and the business
considerations aren't on the table.  Our price is a make-or-break; there's no
way to engage in prioritization and tradeoff decisions without knowing the
problem and context.  When we provide a budget, the project gets cancelled: too
expensive.   We can put down features as line-items, but without knowing the
problem, the line items may be irrelevant or confusing. 




If the problem has to be gamed to fit
the solution, then tradeoffs are confusing.  We have business tradeoffs in the
problem space, and technology tradeoffs in the solution space.  Since neither is
fixed, no one can make any decisions, and the project gets cancelled:  too
expensive.  Worse, the customer accuses us of gold-bricking because we want to
charge them money just to restate their business problem, something that may
call their solution technology into
question.



**Engaging Usefully.** 



It's really hard to
engage usefully.  If we give a "let's start with 8 weeks at
*x* K$,
we have to explain what they get for their
*x* K$. 
Now we're back to explaining why no scope, no problem, or a movable problem are
serious issues.  And we look bad for not being able to take their murky
statements and make crystal-clear prognostications about what we'll have done in
8 weeks.



If we develop a big, formal
proposal, with a SOW, WBS, Project Plan, Deliverables, and Quality Plan, we've
often thrown good money after bad.  If the customer didn't provide much scope,
our SOW is far more formality than they want, and the change control provisions
are daunting.  



If the problem's none
of our business, then a SOW plays well, but doesn't address their problem.  We
get paid, we discover the real problem; then they throw us out for initiating
the scope creep; the project gets cancelled.  While everyone's unhappy, at least
we got paid. 



If the problem's
flexible, then the business context and problem statement in the SOW are either
wrong to begin with, or immediately become wrong.  But who wants to replan the
entire project every time we redefine the problem to fit the technology?  The
technology isn't changing, so we should just press on with the implementation. 
When the project gets cancelled because it isn't solving the real problem, at
least we got paid.



**Cancellation is Always Bad.** 



Sadly, we predicted
*x* K$
in revenue, but a project cancellation counts against us.  Wall Street penalizes
us for falling short of our revenue predictions.  Just as badly, a project
extension to actually
*solve* 
the underlying problem (distinct from providing the deliverables they asked for)
means that we can't predict our revenues correctly.  In short, any scope change
is -- for a consulting firm -- **Wall Street Death** ™.



So,
while it gets us engaged and gets us some revenue, it's wholly unsatisfying to
meet the customers where they are and offer them what they want.  I'd much
rather offer them what they
need.



**You Can't Always Get...** 



When they want [X], [Y] or
[Z], their expectation is clear.  They expect us to provide what they want.  In
the same way that they pull up to their local fast food joint and say "I want a
new Bentley."



Here's the fantasy.  You
have a problem you can state ("I'm hungry", "I'm not at the beach").  You pick a
product, you engage a vendor to provide a product that you think will solve your
problem.  If your problem isn't solved, you still have the
product.



Well, almost.  If your problem
is that you aren't at the beach, and you buy a car, and still can't get to the
beach, at least you still have the car.  If your problem is that your hungry,
and you buy a burger, and are still hungry, well, you're still hungry.  I
suppose you could complain about the burger, but you don't possess the burger as
a tangible asset the way you possess the
car.



**Services and The Real World.** 



For services, the fantasy
transaction almost never happens, even in the non-software ("real") world.  When
you engage for services (i.e., lawn-mowing or a manicure), you often contract
for the service
*without* 
stating your real problem.  You may contract a lawn service, but your real
problem is weeds, not tall grass.  You may contract a manicurist, but your real
problem is a lousy social life because you hang around with nerds, not because
your fingernails are shabby-looking.  And when the problem's not solved, you
have no tangible product.



So, you ask
for an estimate from the lawn service: "how much will this cost?"  And she has
no clue what you are talking about.  Sure, she can mow it, but it's a tangle of
weeds: you need it tilled under, fertilized and re-seeded.  No matter how much
she mows it, it will still look like
crap.



And she can't engage you on the
solution, either.  If you are vague on the "make it look better", the formal
specifications will be daunting.  If you are fixed on mowing, then she hasn't
solved your problem.  And if you are willing to negotiate on the problem ("make
the weeds shorter sounds about right, do that") then you're never going to be
satisfied.



Is the customer's
expectation wrong?  By definition, it isn't wrong -- we should sell what the
customer is asking to buy.  Or, perhaps the customer's expectation really is
wrong, after all.  If we can't solve the customer's problem, the customer is in
denial, and we need to apply some more serious consumer therapy, rather than
join their insanity.  Perhaps the customer isn't always
right.



**Solving Problems.** 



The problem with solving
problems is that it's a vague service offering.  "We solve lawn problems", has a
smidgen of focus, but it still doesn't bracket precisely which problems they'll
tackle and which they won't.  "We solve social-life problems" is even worse. 
Sure, fingernail polish is part of the social contract, but the offer is way too
broad to be believed.



What's left? 
Educating the customer.  All of the "this is what I want" meetings -- where the
customer has a specification, and we're expected to ask questions and prepare an
estimate -- ought to be preceded by at least two earlier meetings: 
**This Is Our Approach** , and
**What Is Your Problem?** .  The first meeting is pure sales. 
The second meeting is free
consulting.



During
**This Is Our Approach** , we lay it out as clearly as we can. 
You have a problem, and your users must tell us the problem.  You may have a
preferred solution, and we'd love to hear it.  But, be prepared to demonstrate
how your solution fits your problem, and what you need from us.  And if you
aren't ready for this, we can help you get ready for it.  After that, we can do
architecture, design, programming, installation, whatever you
want.



During
**What Is Your Problem?** , real business users will describe
the business problem; you'll then tell us about your solution, how the solution
fits the problem, and what you need from us.  This is a QA session -- in essence
we will QA your Request for a Proposal.   If there are disconnects, questions,
concerns, unknowns or unknowables, we'll identify them as defects.  We'll then
write a proposal, or we'll suggest rework on your problem, solution or scope.




Central to this is to ferret out the
features that actually solve the user's problem -- and are not negotiable --
from other things that are nice to have but don't focus squarely on the problem.
We want to be able to make informed decisions on priorities and trade offs.  We
don't want to be involved in that peculiar form of RFP negotiation where we
propose and get a "No"; the decision is more nuanced, and boiling it down to a
"No" is a disservice to the users.




**Selling It.** 



Is this harsh?  Yes.  Will it
sell?  Probably not.  Will it prevent bad customer relationships?  Absolutely. 
We'll only engage with customers who are willing to solve problems, and who will
recognize the value of solving the problem rather than building
software.



It won't sell because the
customer's internal IT shop already did all of that problem identification
stuff.  Redoing it with a contractor present is -- to IT folks -- just a waste
of time.  Either it over-specifies, it dwells on non-technical stuff like the
business problem, or it leads to scope creep by taking the focus off the
preferred solution.








