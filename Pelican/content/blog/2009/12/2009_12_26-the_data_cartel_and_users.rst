The Data Cartel and "Users"
===========================

:date: 2009-12-26 10:14
:tags: database administration,design
:slug: 2009_12_26-the_data_cartel_and_users
:category: Technologies
:status: published

I work with a CIO who calls the DBA's "The Data Cartel". They control
the data. Working with some DBA's always seems to turn into hostage
negotiation sessions.

The worst problems seem to arise when we get out of the DBA comfort
zone and start to talk about how the data is actually going to be
used by actual human beings.

The Users Won't Mind
--------------------

I had one customer where the DBA demanded we use some Oracle-supplied
job -- running in crontab -- for the LDAP to database
synchronization. I was writing a J2EE application; we had direct
access to database and LDAP server. But to the data cartel, their SQL
script had some magical properties that seemed essential to them.

Sadly, a crontab job introduces a mandatory delay into the processing
while the user waits for the job to run and finish the processing.
This creates either a long transaction or a multi-step transaction
where the user gets emails or checks back or something.

The DBA claimed that the delays and the complex workflow were
perfectly acceptable to the users. The users wouldn't mind the delay.
Further, spawning a background process (which could lead to multiple
concurrent jobs) was unacceptable.

This kind of DBA decision-making occurs in a weird vacuum. They just
made a claim about the user's needs. The DBA claimed that they
wouldn't mind the delay. Since the DBA controls the data, we're
forced to agree. So if we don't agree, what? A file "accidentally"
gets deleted?

The good news is that the crontab-based script could not be made to
work in their environment in time to meet the schedule, so I had to
fall back to the simpler solution of reading the LDAP entries
directly and providing (1) immediate feedback to the user and (2) a
1-step workflow.

We wasted time because the data cartel insisted (without any factual
evidence) that the users wouldn't mind the delays and complexity.

[The same DBA turned all the conversations on security into a
nightmare by repeating the catch-phrase "we don't know what we don't
know." That was another hostage negotiation situation: they wouldn't
agree to anything until we paid for a security audit that illustrated
all the shabby security practices. The OWASP list wasn't good
enough.]

The Users Shouldn't Learn
-------------------------

Recent conversations occurred in a similarly vacuous environment.

It's not clear what's going on -- the story from the data cartel is
often sketchy and missing details. But the gaps in the story indicate
how uncomfortable DBA's are with people using their precious data.

It appears that a reporting data model has a number of many-to-many
associations. Periodically, a new association arrives on the scene,
and the DBA's create a many-to-many association table. (The DBA makes
it sound like a daily occurrence.)

Someone -- it's not clear who -- claimed this was silly. The DBA
claims the product owner said that incremental requirements causing
incremental database changes was silly. I think the DBA is simply too
lazy to create the required many-to-many association tables. It's a
table with two FK references. A real nightmare of labor. But there
were 3 or maybe 4 instances of this. And no end in sight.

It appears that the worst part was that the data model requirements
didn't arrive all at once. Instead, these requirements had the
temerity to trickle in through incremental evolution of the
requirements. This incremental design became a "problem" that needed
a a "solution".

Two Layers of Hated User Interaction
------------------------------------

First, users are a problem because they're always touching the data.
Some DBA's do not want to know why users are always touching the
data. Users exist on the other side of some bulkhead. What the users
are doing on their side is none of our concern as DBA.

Second, users are a problem because they're fickle. Learning -- and
the evolution of requirements that is a consequence of learning -- is
a problem that we need to solve. Someone should monitor this
bulkhead, collect all of the requirements and pass them through the
bulkhead just once. No more. What the users are learning on their
side is none of our concern as DBA.

What's Missing?
---------------

What's missing from the above story? Use Cases.

According to the DBA, the product owner is an endless sequence of
demands for data model features. Apparently, adding features
incrementally is silly. Further, there's no rhyme or reason behind
these requests. To the DBA they appear random.

The DBA wanted some magical OO design feature that would make it
possible to avoid all the work involved in adding each new
many-to-many association table.

I asked for use cases. After some back and forth, I got something
that made no sense.

It turns out that the data model involves "customers" the DBA started
out describing the customer-centric features of the data model. After
all, the "actor" in a use case is a person and the database contains
information on people. That's as far as the DBA was willing to go:
repeat the data model elements that involved people.

If It Weren't For the Users
---------------------------

The DBA could not name a user of the application, or provide a use
case for the application. They actually refused to articulate one
reason why people put data in or took data out. They sent an angry
email saying they could not find a reason why anyone would need these
many-to-many association tables.

I responded that if there's no user putting data in or getting data
out then there's no system. Nothing to build. Stop asking me for help
with your design if no person will ever use it.

To the DBA, this was an exercise in pure data: there was no purpose
behind it. Seriously. Why else would they tell me that there were no
use cases for the application.

Just Write Down What's Supposed to Happen
-----------------------------------------

So I demanded that the DBA write down some sequence of interactions
between actual real-world end-user and system that created something
of value to the organization. (My idea was to slide past the "use
case" buzzword and get past that objection.)

The DBA wrote down a 34-step sequence of steps. 34 steps! While it's
a dreadful use case, it's a start: far better than what we had
before, which was nothing. We had a grudging acknowledgement that
actual people actually used the database for *something*.

We're moving on to do simplistic noun analysis of the use case to try
and determine what's really going on with the many-to-many
associations. My approach is to try and step outside of "pure data"
and focus on what the users are doing with all those many-to-many
associations.

That didn't go well. The data cartel, it appears, doesn't like
end-users.

The Final Response
------------------

Here's what the DBA said. "The ideal case is to find a person that is
actually trying to do something and solve a real end user problem.
Unfortunately, I don't have this situation. Instead, my situation is
to describe how a system responds to inputs and the desired end state
of the system."

Bottom line. No requirements for the data model. No actors. No use
case. No reality. Just pure abstract data modeling.

Absent requirements, this approach will turn into endless
hypothetical "what if" scenarios. New, fanciful "features" will
inevitably spring out of the woodwork randomly when there are no
actual requirements grounded in reality. Design exists to solve
problems. But the DBA has twice refused to discuss the problem that
they're trying to solve by designing additional tables.



-----

When I was working for a big mining company I was ...
-----------------------------------------------------

Carl Trachte<noreply@blogger.com>

2009-12-25 22:13:47.947000-05:00

When I was working for a big mining company I was quite fortunate in
this regard, although at the time I didn't appreciate it.

As I user I was one of the "subject matter experts" who worked with the
dba's and corporate developers to take our one off system and integrate
it into the bigger one.

Everyone was pretty cooperative, and the main question was usually, "How
are you using the data?"

Probably the reason a consultant was brought in in the case above is
that the situation was so messed up only a consultant would have the
objectivity and ability to make it right.

As I've said before, Mr. Lott, think of it as job security :-\\





