A New Architecture Involves Ignorance
=====================================

:date: 2006-08-22 17:07
:tags: architecture,design,methodology,process,agile
:slug: 2006_08_22-a_new_architecture_involves_ignorance
:category: Architecture & Design
:status: published





Without mentioning Armour's
*The Laws of Software Process: A New Model for the Production and Management of Software*  (which includes the Five Orders of
Ignorance, quoted by Paul Freedman in "`Uncovering Ignorance in Software Development <http://www.computer.org/portal/site/software/menuitem.538c87f5131e26244955a4108bcd45f3/index.jsp?&pName=software_level1&path=software/bookshelf/2005&file=2005s1fre.xml&xsl=article.xsl>`_ "),
Purdy has hit the nail on the head regarding gestation of
architectures.



Is Gestation overhead? 
Is it a mistake?  How do we budget for it?  What, exactly, is
it?



Let's compare.

-   **Zero order ignorance: Lack of ignorance** .  Purdy describes this as "the more
    one understands a problem, the more likely one is to precisely predict its
    implementation cost in terms of time".

-   **First order ignorance: Lack of knowledge** .  This is manifested by the
    distinction Purdy makes: "Some implementation unknowns are at most minor
    speed-bumps, while others can be major project de-railers."  If all you need is
    some additional knowledge, it's a speed-bump.

-   **Second order ignorance: Lack of awareness** ... You are unaware that you have
    first order ignorance.  Purdy notes that "architectural timeline slippage could
    be of completely off-the-scale proportions".  Clearly, if you aren't aware of
    your ignorance, you have this off-the-scale phenomena of trying all kinds of
    things just to discover what you don't know.

-   **Third order ignorance: Lack of process** ... You don’t know how to
    discover ignorance.  Purdy reminds us that "An application architecture is not
    fully gestated until the architect can visualize the implementation, and explain
    the architecture to the implementation team clearly enough that they can
    visualize the implementation."  In short, you need to embody the management of
    ignorance in your software development process, expecting that you will have
    awareness problems somewhere along the way.

-   **Fourth order ignorance: Lack of ignorance about the orders of ignorance.** 



I've tried (and failed)
to lift this situation up to customers for just about every project I've been
involved in since people started calling me an architect in the
mid-90's.



**War Stories.** 



I've tried to put in a
project phase for "validating the architecture" or something similar.  I would
try to allocate time to build skills in the processes, technology, management
and governance issues.  



In one case,
they had already bought everything, and felt that their DBA would somehow handle
all of the learning.  I wasn't sure when or how, since we hadn't written the
application software.  We would be -- essentially -- learning as we went.  We'd
originally planned to use one set of tools, and then upgraded to the next set of
tools, hoping that everything would still be just as easy to develop and manage.
Sadly, the toolset was immature, and things didn't go well.  Worse, the
specifications were very focused on a character-mode interface (it was '95), but
the tools were GUI tools.  Everyone's first-order ignorance of using the tools
ground the project to a halt.



In one
case, there just wasn't time to shake out an architecture.  The customer
demanded (repeatedly) that I produce a reliable, definite, indisputable
architecture from thin air.  They wanted to talk about L2 cache and memory bus
options.  I wanted to get a half-dozen servers and a storage array up and
running ASAP so we could start building a web environment.  The customer got
into a shoving match with the IBM representative because the customer wanted
just one Ethernet interface in each server and couldn't see paying for two.  The
whole "standard configuration" meant nothing -- each box had to be customized. 
Eventually, common-sense prevailed and we talked them into commodity servers. 




[As an aside, their CEO had to tell
their CIO to stop badgering me.  The CIO kept repeating the phrase, "I expected
you to give me a recommendation."  And I kept saying "I'm recommending a
half-dozen servers and a storage array."  The CIO would claim that it was too
breezy and informal, and he expected a recommendation, and around we went.  More
than once I asked the CIO what else he wanted, and we would begin at the "I
expected you to give me a recommendation" part again.
]



Since the architecture was done in a
vacuum, when the software began to arrive we learned that we didn't really have
everything under control.  We had second-order ignorance problems getting a very
complex web application built based on use cases that were little more than
titles.  Some of the use cases were performance-critical, but without solid
volume and throughput information, we could only guess what was going to happen
in production.



In another case, the
client insisted that their IT department did this "all the time."  Sadly, that's
an example of fourth-order ignorance which masks some obvious third-order
ignorance.  The IT department didn't do this exact thing "all the time".  No one
had a process for gathering the required awareness and knowledge.  The hubris of
claiming that it was done "all the time" lead to a schedule which presumed a
90-day hardware acquire, setup, install, test, secure, and transition to
operations.  Followed immediately by software installation, testing and
production roll-out.  Clearly, if there was anything we were unaware of, the
whole house of cards would
collapse.



Was anyone aware that the
RDBMS interfaces might not be suitable for high-volume data warehouse transfers?
Was anyone aware that we needed to compare export-FTP-import and
instance-to-instance copies?  



Worse,
how could anyone be aware that business rules might blow up from 100 rows to
9,000 rows?  I couldn't believe it, and didn't even know that users could
concoct 9,000 business rules.  I couldn't imagine putting additional time in the
plan for that kind of thing.  The software, of course, didn't run very
effectively when applying 9,000 more-or-less random rules to the input. 




**Managing Ignorance.** 



Gestation is a good way
to manage ignorance.  If everything isn't rock-solid and well-understood by the
developers, don't plan on getting anything done by a given due
date.



But how can we get started if we
need to understand "everything" before starting?  Excellent
conundrum.



Well... actually, it's only
a conundrum if we conflate everything that is knowable into one unstructured
mass of facts.  Really, we have a series of steps we have to ascend from
business ignorance, through application ignorance to architectural ignorance. 
In principle, we want to know the business processing and know the application
before we select an
architecture.



Purdy's advice gives a
way to structure the work: "get the gestation on the hard architectural problems
started well before you need to nail down a timeline".  In short, guess at what
the hard architectural problems are likely to be.  This is a fourth-order
solution; it creates a process (managing third-order ignorance).  This start
early approach will turn up second-order ignorance (awareness) gaps before they
derail a project.



The fantasy is that
someone conceives of software, begins a project, collects requirements and gives
those requirements to the architect.  We see it in RFP's all the time.  My war
stories above reflect that fantasy. 




As a practical matter, we can do
something more proactive.  For in-house development, nothing is a surprise.  The
users, and the IT folks
*are* 
talking, and the architects can be engaged in this conversation.  In some
organizations, this conversation is made difficult by charge-back accounting,
but everyone knows how to sand-bag the charge-backs and accumulate enough time
to hold forward-looking conversations.  This is a kind of 3rd-order solution;
it's an informal process (hated by the controllers, but essential for success)
that hopes to prevent 2nd-order ignorance from derailing a
project.



For out-of-house developers
(like me) this is much tougher to do.  One approach is to pick a technology and
hope our customers ask for it.  There aren't too many bases to cover (.Net,
J2EE, for example) and as long we have deep expertise, this can work out. 
However, our customers rarely have the same depth (or experience) we do, they
often insist on something unique, essentially forcing 2nd-order ignorance on us.
We can decline the work, hope for the best, or try to educate the customer on
the value of waiting -- investing in risk
reduction.



**The Bottom Line.** 



Until we are aware of all the
knowledge we need, we can't commit to a timeline.   If we recognize that a
gestation period is required for all architectural change, how do we pay for
this?  What is the value of
gestation?



We can monetize gestation. 
The dollar value is measured in risk dollars.  

-   **No Gestation** .  We'll need a huge risk budget to
    work around 2nd-order ignorance.  Indeed, Purdy's lesson learned is that we are
    likely to wind up in a situation where no amount of money can save the
    project.

-   **Gestation** .  Eliminates risk of missing
    deadlines and risk having to spend more money to resolve 2nd-order ignorance. 
    Because "rushing the architectural process will exponentially increase the
    likelihood of project failure," all the money we spend on Gestation has a
    handsome return in predictability, risk reduction, time to market, and all the
    benefits we want from a predictable software
    process.



Essentially, every proposal
for work needs to include "architecture risk reduction."  This is a more
palatable phrase than "validating the architecture." 




Doing a "validation" or a "proof of
concept" may appear silly when planners have already selected the architecture. 
Indeed, I had a customer insist that I write a test plan for Oracle's backup and
recovery.  What -- precisely -- am I testing?  And if it fails the test, what
does that do to the product they already purchased, installed, and built the
application around?



Proposing a "risk
reduction" (or "due diligence") to locate sources of 2nd-order ignorance, may
seem like good business.















