Notable Failure of Use Cases - Part 4
=====================================

:date: 2006-04-28 10:32
:tags: architecture,design
:slug: 2006_04_28-notable_failure_of_use_cases_part_4
:category: Architecture & Design
:status: published





I recently reviewed some end user-authored use
cases, and they -- of course -- reflect the way people actually work.  The
computer system was largely incidental to what they
did.



Each use case listed half a dozen
actors, had a dozen or more steps, and involved many off-line interactions among
the actors.  All of these are signs of business process definitions.  These can
be considered as use cases, but they are use cases written at a higher level of
abstraction than a single application
system.



What went
wrong?



First, I think it takes
training, spread over several days, to get a grip on use case writing.  The core
definition ("an actor interacting with a system to create business value") isn't
obvious, even to professional business analysts.  The basic features of "actor"
and "interaction" require many examples, many writing exercises, and many
group-level discussions.



The "business
value" part of the equation is often a show-stopper.  In an earlier experience
with end-user use-case writing, we spent four hours discussing what "business
value" really means.  Time and energy get expended in pursuing what I call an
"attractive sink" <{filename}/blog/2005/10/2005_10_31-notable_failure_of_use_cases_part_3.rst> that isn't really  of any value at all.
One of those sinks is the "**Technology Workaround** ", another is the
"**Reviews and Approvals** ".



**Documenting the Technology.** 



The users had
written a use case with dozens of individual steps.  They received their source
data on a CD.  In those days, CD players were rare and specialized, and only
servers had them.  The nearest server was in Hartford, so they mailed the CD to
Hartford where it was loaded onto a network drive.  The data from the CD was
FTP'd to the mainframe where a tape could be made.  The tape was then shipped to
another processing center where the actual processing happened.  The result of
that processing was FTP'd back to Hartford, where someone with root privileges
could move the final result to a shared area that the end users could copy to
their local file
server.



Really.



And
what was the business value?  Somewhere in the word "processing" was some kind
of algorithm that actually created something of business value.  This was -- to
the author -- so obvious that it didn't bear repeating in the use case
document.



The more important question
is "where is the interaction?"  The use case didn't say what the actual business
user really does to initiate this process, make decisions or take actions.  The
business value was lost in a welter of
technology.



The users were focused on
the **Technology Workaround**  in this process.  It took a long
time to develop and it was deeply technical.  To many people, the point of use
cases is to capture the technology issues, not the creation of business
value.



It wasn't until I threatened to
walk out of the meeting, and walk over `CompUSA <http://www.compusa.com/>`_ `  <{filename}/blog/2005/10/2005_10_31-notable_failure_of_use_cases_part_3.rst>`_ to buy a CD drive that the people started to
get the "business value" part of use case writing. 




Threatening to go to CompUSA wasn't
the "aha" moment, however.  I had to write down the numbers.  Six people times
$50 per hour times four hours is $1,200.  The CD player was $500.  And that
still wasn't the "aha" moment.  



The
"aha" moment came when they finally realized that IT would have proposed this
from the very beginning if they'd only described the problem instead of
insisting on this particular solution.  To get to the "aha" moment, we had to
review the various conversations that led to the implementation of the technical
work-arounds.  As they recapitulated the conversation, I provided the color
commentary from IT's point of view.  Mostly with comments like "why do they need
that?" and "we don't know what problem this solves, but the users are demanding
it."



**Documenting Reviews.** 



Many manual operations
exist to check the results of other manual operations.  There are two reasons
for this:

1.  The manual operation is
    error-prone.

#.  The manual operation is governed by rules
    which are murky, incomplete, or too complex for one person to
    implement.



We cope with this by
defining business processes with numerous reviews and approvals.  In many cases,
the reviews are legacy operations to prevent a recurrence of of some
particularly visible mistake.  In these cases, the manual operations that we are
describing don't *create value* , they prevent loss, which is not quite
the same thing.  



We see the effects of
these kinds of processes when the users document their off-line meetings,
notifications; the **Reviews and Approvals** .  They are capturing details for the
things that are happening among human beings without support from an automated
system.   



What is the business value? 
The standard answers include "we have to notify everybody (or that person, or
that team)."  But if we probe a bit, "everybody" or the named person don't need
the information to make a decision or take action. 




Sometimes the answer includes "we have
to be sure the results are correct."  But the reason for incorrect results is
the manual process that creates the results in the first place.  Automating the
process eliminates the need for all the checking and review.  Some people are so
enamored with the processes that they don't see the irony in writing detailed
specifications for the exact processes automation is supposed to eliminate.




We might see a step in the use case
like "when all five groups approve..."   Which means that we don't have an actor
interacting with the system.  Instead, we have five similar interactions on
behalf of five separate actors: each looks at the information, makes the
approval decision, and responds to the system with that decision.  Do all five
actors need the same information?  Doubtful.  What is unique about each of these
five brains that requires their
participation?



The more interesting
question -- omitted from the use case -- was what happens when someone vetoes
the decision.  If all five don't approve, then what?  How are people notified? 
What is the interaction?  Has it ever happened?  What did people do? 




**What can we do?** 



What can we do to get the users
on track, writing use cases that express their interaction with a system to
create business value?  How do we get away from describing the manual processes
we're trying to eliminate?



In the case
of documenting the **Technology Workarounds** , it's a hard habit to break.  Many
-- too many -- people think the business analysis job is to translate the
business problem into IT techno-speak.  In doing this, they generally presume a
solution to a poorly-framed problem, and then document all kinds of irrelevant
technical details.



Few -- too few --
realize that the business analysts job is to capture the business problem
accurately and completely.   So, one important piece of training is in
recognizing and describing problems irrespective of your favorite (or despised)
solution.



It helps to work on
non-technology problems like moving topsoil into the backyard or finding out why
the windshield wiper keeps breaking.  Getting out of the technology framework
can help develop the skill of isolating underlying problems. 




In the case of documenting the
**Reviews and Approvals** , it's difficult to separate the
business process from the business value created by the process.  However, with
some training and practice, it's possible to distinguish between the cook, the
toast, and the toaster used to prepare the
toast.



In the restaurant setting, the
distinctions seem obvious.  But when users document reviews and approvals as
part of the business value, they may have conflated preparation or presentation
into the meal itself.



I like to ask the
question "Are you describing the toaster or the toast?"  The toast is an
important part of the use case goal; it's the business value we are creating. 
The user will interact with a toaster.   The trick is that neither of these are
the central feature of the use case.  The use case is about "making toast".  The
use case will be used to design a better toaster.  The toaster, in turn, will be
used to make
toast.



**Consequences.** 



One
consequence of getting away from technology workarounds is that many, many
things get questioned.  This, ultimately, is a good thing.  However, it does
lead to some frustration as people locate the boundaries of what can be
questioned, and what cannot be
questioned.



One consequence of
separating the toaster from the toast is that we are often left with a
dependency loop.  A use case -- in a way -- depends on seeing a user interface. 
The user interface will be designed from the use cases.  Which comes first,
interface or use case?  If we draw an interface to help the users write the use
cases, we've -- in a way -- designed the entire application.  Once we've drawn
the interface, why bother with all the other work, why not just write technical
specifications?



One way to cut this
tangle is to draw UI sketches on paper.  Use them to help visualize potential
screens, displays, reports and buttons.  Add, change and delete while writing
the use cases.  Then, throw the paper sketch away.  Leave it to the GUI
designers to craft a presentation that fits the use cases.   It might
reconstruct the sketch, or it might be a lot
better.



It's important that people who
write use cases are able to articulate the business value, and describe ways to
create that value.  Their job isn't to wrestle with technology, but to determine
how people should interact with a system to create the value they're
describing.










