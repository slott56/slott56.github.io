Essay 13 - Analysis Without Running Aground
===========================================

:date: 2005-09-17 11:27
:tags: architecture,software design
:slug: 2005_09_17-essay_13_analysis_without_running_aground
:category: Architecture & Design
:status: published





Analysis is a difficult job. It requires
capturing the business problem, including the business entities and the business
processing. It requires endless patience, good interviewing skills and excellent
writing skills. Most important, it also requires the discipline to discover the
whole problem before putting forth any
solution.



This essay provides some
background, followed by the 5-step process, then a summary of the objectives of
the analysis exercise. The process has the following steps:

1.  Problem Description

#.  Nouns and Verbs

#.  Use Cases

#.  Solution Summary

#.  Iterate



**Background** 



Most
analysts have strong IT backgrounds, and immediately solve the problem. Before
the user has finished describing it, the solution forms in their heads. Sadly,
many line-of-business end-users have so much IT experience, they are solving the
problem, also. They describe files, processing, conditions, business rules, and
all the trappings of IT solutions. They also ignore their own actual problem,
and instead describe a solution they think IT can
build.



Frustratingly, there is a lot of
second-guessing that goes on. People say things during analysis that are
calibrated to create a certain kind of response. They don't often report the
whole story, but just enough of the story to get the desired response. This is
often revealed when the condition that is "always true" has "a few minor
exceptions, but you don't need to worry about those, they'll never
occur."



Warning:
user manipulation in
process.



There are two important
subject areas for analysis: data and processing. For others, see the Zachman
Framework. `http://www.zifa.com <http://www.zifa.com>`_  . You can argue which of
these is more enduring and essential. Data if often identified as essential,
since business processes change, but the artifacts (the data) doesn't evolve as
rapidly.  See `Essay 8 <{filename}/blog/2005/09/2005_09_11-essay_8_data_first_user_interface_later.rst>`_ , "Data First, User Interface Later" for
an opinion.  This could be termed functional drift. We also have to resolve the
issue of two organizations using different processes around the same artifact;
e.g., two different invoicing systems. This could be termed functional
heterogeneity.



However, data is not
immune from these problems. Databases are full of attributes where the actual
purpose doesn't match the name. This is either evolution (semantic drift) or
conflict (semantic heterogeneity).

I like to call this the "Third
Christmas Club Problem." Once upon a time, there was a bank service called a
Christmas club. Make deposits for 50 weeks, get your money with a big interest
payment at the end of the year. It's a terrible deal, banks don't offer it
anymore, but their systems still have places to record Christmas Club account
numbers in the customer database. Interestingly, those fields have been reused
for other purposes, but the database column names have not been changed. Now you
find the credit card account number that is tied to a home equity loan hidden in
the otherwise unused XMAS_CLUB_3
field.



We have to start somewhere, and
neither data nor process is perfect. We'll start with
process.



**1. Problem Description** 



Write a narrative of
the problem, from the user's point of view. Focus on the user's purpose,
objectives, goals. Include a high-level summary overview of the essential
processing that can't get done properly. Don't metion solutions; be accurate but
not perfectly precise. You will rework this
heavily.



You are only writing a few
paragraphs. You are, however, describing the business problem. See Essay 17,
"Solution or Workaround?" for guidance on this. Given a problem, it is possible
to define a solution. Lacking a problem to solve ... well ... the entire project
can never be
successful.



**Potential Difficulties** 



**Dry Shoals** 



You can't think of anything
to say. This is writer's block. Everyone gets it. Do two things to cure
it.

1.  Get away from the computer; take notes on
    paper with a pen. Computers are too much like the final, published form. This is
    intimidating. It makes the first draft of the first revision seem like it is
    "for the record". It isn't; it doesn't count for anything. Do it off
    line.

#.  Write anything. List the users; list the
    business entities; list the departments. Jot down phrases in no particular
    order. Call you uncle John and ask him to tell you about the time he bumped into
    Buddy Ebsen in the Philadelphia airport and write that story down, just to write
    something. Eventually, you will start to write down the user's view of what the
    system does and how it helps them.




Warning:
Do not skip this step and move on, hoping to make up for the lack of written
ideas later in the process. If are blocked now, you will be blocked later. You
have to start with something written, but you will evolve it into something
useful.



**The Orinoco Flow** 



You have written 15 pages of
single-spaced material, summarizing all of the powerpoint presentations, email
traffic, process manuals, company policies and the sports section of the Sunday
New York Times. You haven't even begun to scratch the surface on the highly
nuanced and sophisticated capabilities that would provide enduring business
advantage well into the next decade. You've accounted for technology shifts and
opportunities to create additional value above and beyond the project
scope.



You have, of course, solved the
problem without formally defining it. You need to throw this away and begin
again to describe just the user's experience with the system: their
interactions, and how this creates value for the
users.



Warning:
Do not save this original material. It is a thought virus, and will infect
everything you do. Indeed, you may be unable to shake this solution and actually
focus on the user's real problems. Consider recusing yourself from the project
if you can't delete it all and start
again.



**Edge of the World** 



You've written some stuff,
but it's too abstract to be of any use. You can't code from it, or even design
from it. It's high level, pointless fluff. It's incomplete, and cannot be
completed because it's so vague and
purposeless.



This is actually usable
stuff. There's more process to making this valuable, and the process is
iterative. This is at least grist for the mill, and can be
refined.



Warning:
Do not resort to prototyping at this point. All the code you write will be a
thought virus, and will shape your concept of problem and solution. At some
point in the future, you might resort to prototyping to drive out additional
requirements or resolve design issues. Don't do it
now.



**2. Nouns and Verbs** 



While sometimes deprecated as
misleading or simplistic, I found noun and verb analysis to be a good technique
for getting started on understanding the problem
domain.



From your narrative
description, locate nouns and verbs. Nouns should give you big hints about the
actors, the business entities, attributes of the entities. Verbs will help you
identify processing that the business entities are part
of.



You will find that your description
is often incomplete or off-target.




Warning:
Don't rewrite heavily at this time; wait for the end of the iteration before
rewriting.



From the nouns and verbs
concoct a business model, including the static (entity or class) and dynamic
(activity and state) descriptions. This is not a logical model; it doesn't have
all of the attributes, all of the relationships, or even all of the entities. It
is a conceptual model that defines the terms used in the narrative. It will
evolve (eventually) into a more technical, more usable
model.



Advice:
Work quickly, don't spend too much time editing, revising or extending; your job
is to capture information and iterate through a number of
steps.



**3. Use Cases** 



Given the business model and
the narrative description, refine the description into some kind of use
cases.

A use case identifies an actor, the
interactions between the actor and the system, and the business value created by
that interaction.



Note that the use
cases presume some kind of "system". We haven't defined the system, so how do we
describe interactions? This is challenging at first. The secret is an idealized,
hypothetical system which does the minimum to help the user's meet their goals.
Don't over-automate a super-system that does everything automatically. Don't
worry about under-automating.



Start
with the actors. Don't name each person; classify the actors by roles. If you
can't identify the actors from what you know, you can start again at the
beginning. You now know more than you did when you started. The second trip
around will produce better
results.



Each actor has a goal. Write
it down. They'll have to use the system to meet that goal. What will the actor
provide? What will the system provide? What decisions do the actors make? What
actions do they take based on information from the
system?



This will lead you to one or
more sequences of interactions for each actor. Each sequence is discrete when it
has a discrete goal; a purpose; and ending point. Name the sequences (they are
"use cases"); write down the
interactions.



When writing the
interactions, use words from the business entity diagram. Use consistent verbs.
When in doubt, remember that people interact with computers for two fundamental
purposes:

-   To Make Decisions.  Decisions that
    involve information they don't have available without a computer.

-   To Take Action.  Actions that involve
    business information that is already in a computer
    somewhere.



Algorithms, processes,
procedures and the like aren't often interactive.  Go too far down the "detailed
procedures" road and you leave the person out of the picture.  Be sure you can
answer the basic questions: Why is the person doing this?  What is their
goal?



Warning:
Do not over document the system side of the processing; that is part of the
solution. We're iterating, remember. The first thing you write down is not the
final answer, it's only a
draft.



**4. Solution Summary** 



Summarize the use cases
using a well-defined set of nouns and verbs. You are trying to clarify (and
sometimes simplify) the use cases to name the real business entities -- the real
nouns in the problem domain. When writing the summary, you may realize that some
use cases need rewriting. In the process of use case writing, you may have some
summary material that eliminates some tiresome details. You should bounce back
and forth between summary writing and use case
editing.



Your solution should match
your problem. Indeed, this is the final check for proper scope: does the summary
describe a solution to the
problem?



**5. Iterate** 



Now that you have some
entities and some interactions, you know much, much more about the system. You
have to do two things. First, throw away all your notes to date. Second, go back
to the beginning of the process and write a new narrative description. This will
be better (more complete, more accurate, more focused and more useful) than your
first draft. Watch the shoals carefully, and don't create the
solution.



You may have to iterate more
than once to really capture the essence of the user's problem. Actors will come
and go from the model. Business entities will come and go. The focus will
narrow. The implementation details (mainframe vs. server, web vs. batch, Java
vs. COBOL, DB2 vs. Oracle, Army vs. Navy) will drop
away.



**Objective** 



The
objective isn't the problem definition.   However, this is so hard that people
get stalled trying to write this. See Essay 17, "Solution or Workaround" for
guidance. They often jump past problem to solution, omitting any clear
definition of what the problem really is. The real objective is the business
entity model and the use cases. The solution summary simply frames the use cases
up for easy digestion.



The business
entity model has nouns from the use cases. The use case nouns are clarified and
defined in the business entity model. When someone reads a use case, they should
be able to follow along on the business entity diagram.



















