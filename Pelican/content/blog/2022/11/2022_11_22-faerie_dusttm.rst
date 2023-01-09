FAERIE DUST™
============

:date: 2022-11-22 16:39
:tags: design,architecture
:slug: 2022_11_22-faerie_dusttm
:category: Technologies
:status: published

Here's how to recognize a **Faerie Dust** request:

#. We have identified a problem. It can be with almost anything:
   scalability, reliability, auditability, any Quality Measure.
#. We're pursuing a specific technology. Typically, something that has
   the lowest impact on our architecture.
#. We can't address anything other than this specific technology
   variation -- we can't change the application software or buy
   hardware.

Once we're in the **Faerie Dust** realm, what can we do?

Laughing doesn't help. They have a serious problem, they need a
solution. The fact that they won't address the cause isn't completely
relevant -- we have to work on the denial, anger, negotiation,
depression cycle first. Hopefully skipping past the anger, or assuring
the anger is directed elsewhere.

Helping doesn't help. If we join the quest for their Faerie Dust, what
will we accomplish? We'll burn billable hours to -- eventually -- reach
an equivocal non-solution with a complex write-up and recommendations
that won't be implemented.

Not helping doesn't help. If we obstinately refuse to join the quest for
the Faerie Dust... well... then we've done nothing. We haven't advanced
their understanding of their problem.

What's left? Is there a middle road that allows us to join the Faerie
Dust quest, but still point out the side roads, other monsters and other
treasures along the way?

Perhaps there is, but it would require a kind of saintly patient
persistence. We would have to start with an enumeration of problem
causes, prioritize them, and then focus on their selected bit of Faerie
Dust. My idea is that enumerating the possible causes allows us to
identify the missed opportunities, and the possible magnitude of fixing
something essential (algorithm or data structure) instead of throwing up
window-dressing to cover problems in something inessential (reducing the
time required for a table scan).

Example
-------

Here's a concrete example of Faerie Dust.

#. Pick a data model that doesn't fit the use cases. i.e., lumped many
   discrete details into a single text field that has "rich semantic
   content". Work around this mistake by using wild-card matches.
#. Complained about performance and dug into nuanced details of LIKE
   clause and full-text search. Lots of study time spent on LIKE clause
   processing and how to improvement performance.
#. Refused to discuss the actual use case or the mismatch between data
   structures and requirements.

The design didn't match the use cases. **Faerie Dust** won't help.



-----

&quot;Helping doesn&#39;t help. If we join the que...
-----------------------------------------------------

TechNeilogy<noreply@blogger.com>

2011-01-27 09:27:52.554000-05:00

"Helping doesn't help. If we join the quest for their Faerie Dust, what
will we accomplish? ...Not helping doesn't help."
This really hits home. I once had to make this agonizing decision
regarding a project to which I had pledged commitment.


The clients who request &quot;Faerie Dust&quot; ar...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-01-30 20:11:13.261000-05:00

The clients who request "Faerie Dust" are also the ones that will
probably also claim that they are "special" and nobody has ever had a
problem like they currently have. Pointing out a web page or a book
which describes a similar problem to theirs will at best get you dirty
looks and sometimes even a boot out the door.





