How Managers Say "No": The RDBMS Hegemony Example
=================================================

:date: 2013-07-16 08:00
:tags: project management,architecture,RDBMS,noSQL,SQL
:slug: 2013_07_16-how_managers_say_no_the_rdbms_hegemony_example
:category: Technologies
:status: published

Got an email looking for help in attempting break through the **RDBMS
Hegemony**. It's a little confusing, but this is the important part of
how management says "no".


    "Their response was nice but can you flush [*sic*] it out more"


[*First: the word is "flesh": "flesh it out." Repeat after me:
"Flesh it out," "Flesh it out," "Flesh it out." Flesh. Put flesh
on the bones. No wonder your presentation went nowhere, either you
or the manager or both need help. English as a second language is
only an excuse if you never read anything in English.*]

There's a specific suggestion for this "more". But it indicates a
profound failure to grasp the true nature of the problem. It
amounts to a drowning person asking us to throw them a different
colored brick. It's a brick! You want a life preserver! "No," they
insist, "I want a brick to build steps to climb out."


Yes, **RDBMS Hegemony** is a real problem. I've talked about it
before "`Hadoop and SQL/Relational
Hegemony <{filename}/blog/2010/11/2010_11_11-hadoop_and_sqlrelational_hegemony.rst>`__".
Others have noted it: "`NoSQL and NewSQL overturning the
relational database
hegemony <http://features.techworld.com/applications/3305706/nosql-and-newsql-overturning-the-relational-database-hegemony/>`__".
You can read more concrete details in articles like this:
"`Introduction to Non-Relational Data Storage using
Hbase <http://www.deerwalk.com/blog/non-relational-data-storage-using-hbase/>`__".


RDBMS Hegemony is most visible when every single in-house project
seems to involve the database. And some of those uses of the
database are clearly inappropriate.

For example, trying to mash relatively free-form "documents" into
an RDBMS is simple craziness. Documents—you know, the stuff
created by word processors—are largely unstructured or at best
semi-structured. For most RDBMS's, they're represented as Binary
Large Objects (BLOBs). To make it possible to process them, you
can decorate each document with "metadata" or tags and populate a
bunch of RDBMS attributes. Which is fine for the first few
queries. Then you realize you need more metadata. Then you need
more flexible metadata. Then you need interrelated metadata to
properly reflect the interrelationships among the documents. Maybe
you flirt with a formal ontology. Then you eventually realize you
really should have started with document storage, not a BLOB in an
RDBMS.

Yes, some companies offer combo products that do both. The point
is this: avoiding the RDBMS pitfall in the first place would have
been a big time and money saver. Google Exists. The RDBMS is not
the best choice for all problems.


The problem is this:


-  Getting away from RDBMS Hegemony requires management thinking and action.
-  Management thinking is a form of pain.
-  Management action is a form of pain.
-  Managers hate pain.


In short, the only way to make progress away from the RDBMS is to
create or expose existing pain. Or make it possible for the
manager to avoid pain entirely.


Let's look at the various approaches.


**Doing A "Presentation"**


The email hinted at a conversation or presentation on the problem
of RDBMS Hegemony.


    "I finally convinced my current client that RDBMS's are expensive in
    terms of adding another layer to the archtiecture [*sic*] and then
    trying to maintain it."


It's not clear from the email what the **details** of this
conversation or presentation were, but it clearly involved the two
key technical points (1) the RDBMS has specific use cases, and (2)
not all applications fit those use cases.


However. Those two key technical points involve no real management
pain.


Real pain comes from cost. And since the RDBMS license is usually
site-wide, there's no obvious cost to the technology.


The labor cost for DBA support, similarly, is side-wide and already
in the budget. So there's no obvious cost to the labor.


No cost means no pain. No pain means no change.


Asking a manger to think, however, causes actual pain. Managers want
technical people to do the thinking for them.


Asking a manager to consider the future means they may have to take
action in the future. That's **potential** pain.


Either way, a management **presentation** on database hegemony is
pure pain. No useful action will ever come from a simple, direct
encapsulation of how the RDBMS is not really the universal data tool.
Management said "no" by asking for more information.

We'll return to the "more information" part below.

It was good to start the conversation.

It's good to continue the conversation. But the specific request was
silliness.

**Exposing the Existing Pain**


What's more important than a hypothetical conversation is showing how
the RDBMS is causing pain right now. It's easier to convince managers
of the hidden cost of the RDBMS by exposing existing **actual** pain
in the **current** environment. And it has to be a level of pain that
exceeds the pain of thinking and taking action.


What's most clear is a specific and avoidable labor cost. Ideally,
this specific—and avoidable—labor cost will obviously be associated
with something obviously database-related. It must be obvious or it
won't yield a technology-related management understanding. If it's
not obvious, management will say "no", by asking for more data;
they'll claim it's people or process or measurement error.

The best place to look for avoidable labor is break-fix problem
reports, bugs and enhancements. Another good source of avoidable
costs are schema migrations: waiting for the DBA's to add columns to
a table, or add tables to a database.

If you can point to specific trouble tickets that come from wrong use
of an RDBMS, then you might be able to get a manager to think about
it.

**The Airtight Case**

Your goal on breaking RDBMS Hegemony is to have a case that is
"airtight". Ideally, so airtight that the manager in question sits
up, takes notice, and demands that a project be created to rip out
the database and save the company all that cost. Ideally, their
action at the end of the presentation is to ask how long it will take
to realize the savings.

Ideally.

It is actually pretty easy to make an airtight case. There are often
a lot of trouble tickets and project delays due to overuse and misuse
of the RDBMS.

However.

Few managers will **actually** agree to remove the RDBMS from an
application that's limping along. Your case may be airtight, and
compelling, and backed with solid financials, but that's rarely going
to result in actual action.

"If it ain't broke, don't fix it," is often applied to projects with
very high thresholds for broken. Very high.

This is another way management says "no". By claiming that the costs
are acceptable or the risk of change is unacceptable. Even more
farcical claims will often be made in favor of the status quo. They
may ask for more cost data, but it's just an elaborate "no".

It's important to make the airtight case.

It's important to accept the "no" gracefully.

**Management Rewards**

When you look at the management reward structure, project managers
and their ilk are happiest when they have a backlog of huge,

long-running projects that involve no thinking and no action. Giant
development efforts with stable requirements, unchallenging users,
mature technology and staff who don't mind multiple-hour status
meetings.

A manager with a huge long-running project feels valuable. When the
requirements, people and technology are stable, then thinking is
effectively prevented.

Suggesting that technology choices are not stable introduces
thinking. Thinking is pain. The first response to pain is "no".
Usually in the form of "get more data."

Making a technology choice may require that a manager facilitate a
conversation which selects among competing technology choices. That
involves action. And possible thinking.

Real Management Pain. The response? Some form of "no".

Worse. (And it does get worse.)

Technology selection often becomes highly political. The out-of-favor
project managers won't get projects approved because of "risky
technology." More Management Pain.

War story. Years ago, I watched the Big Strategic Initiative shot
down in flames because it didn't have OS/370 as the platform. The
"HIPPO" (Highest Paid Person's Opinion) was that Unix was "too new"
and that meant risk. Unix predates OS/370 by many years. When it
comes to politics, facts are secondary.

Since no manager wants to think about potential future pain, no
manager is going to look outside the box. Indeed, they're often
unwilling to look at the edge of the box. The worst are unwilling to
admit there is a box.

The "risk" claim is usually used to say "no" to new technology. Or.
To say "no" to going back to existing, well-established technology.
Switching from database BLOBs to the underlying OS file system can
turn into a bizzaro-world conversation where management is sure that
the underlying OS file system is somehow less trustworthy than RDBMS
BLOBs. The idea that the RDBMS is using the underlying file system
for persistence isn't a compelling argument.

It's important to challenge technology choices for every new project
every time.

It's necessary to accept the "no" gracefully.

The "stop using the database for everything" idea takes a while to
sink in.

**Proof Of Concept**

The only way to avoid management pain (and the inaction that comes
from pain avoidance) is to make the technology choice a `fait
accompli <http://en.wiktionary.org/wiki/fait_accompli>`__.

You have to actually build something that actually works and passes
unit tests and everything.

Once you have something which works, the RDBMS "question" will have
been answered. But—and this is very important—it will involve no
management thought or action. By avoiding pain, you also default into
a kind of management buy-in.

**War Story**

The vendors send us archives of spreadsheets. (Really.) We could
unpack them and load them into the RDBMS. But. Sadly. The
spreadsheets aren't consistent. We either have a constant schema
migration problem adding yet another column for each spreadsheet, or
we have to get rid of the RDBMS notion of a maximalist schema. We
don't want the schema to be an "at most" definition; we'd need the
schema be an "at least" that tolerates irregularity.

It turns out that the RDBMS is utterly useless anyway. We're barely
using any SQL features. The vendor data is read-only. We can't
UPDATE, INSERT or DELETE under any circumstances. The delete action
is really a ROLLBACK when we reject their file and a CREATE when they
send us a new one.

We're not using any RDBMS features, either. We're not using
long-running locks for our transactions; we're using low-level OS
locks when creating and removing files. We're not auditing database
actions; we're doing our own application logging on several levels.
All that's left are backups and restores. File system backups and
restores. It turns out that a simple directory tree handles the
vendor-supplied spreadsheet issue gracefully. No RDBMS used.

We had—of course—originally designed a lot of fancy RDBMS tables for
loading up the vendor-supplied spreadsheets. Until we were confronted
with reality and the inconsistent data formats.

We quietly stopped using the RDBMS for the vendor-supplied data. We
wrote some libraries to read the spreadsheets directly. We wrote
application code that had methods with names like "query" and
"select" and "fetch" to give a SQL-like feel to the code.

Management didn't need to say "no" by asking for more information.
They couldn't say no because (a) it was the right thing to do and (b)
it was already done. It was cheaper to do it than to talk about doing
it.

**Failure To See The Problem**

The original email continued to say this:

"how you can achieve RDBMS like behavior w/out an actual RDBMS"

What? Or perhaps: Why?

If you need RDBMS-like behavior, then you need an RDBMS. That request
makes precious little sense as written. So. Let's dig around in the
email for context clues to see what they **really** meant.
"consider limting [*sic*] it to

1)  CREATE TABLE

2)  INSERT

3)  UPDATE
    An update requires a unique key. Let's limit the key to contain only 1 column.

4)  DELETE
    A delete requires a unique key. Let's limit the key to contain only 1 column."


Oh. Apparently they really are totally fixated on SQL DML.


It appears that they're unable to conceive of anything outside the
SQL DML box.


As noted in the above example, INSERT, UPDATE and DELETE are **not**
generic, universal, always-present use cases. For a fairly broad
number of "big data" applications, they're not really part of the
problem.


The idea that SQL DML `CRUD
processing <http://en.wikipedia.org/wiki/Create,_read,_update_and_delete>`__
forms a core or foundational set of generic, universal,
always-present use cases is part of their conceptual confusion.
They're deeply inside the SQL box wondering how they can get rid of
SQL.


Back to the drowning person metaphor.


It's actually not like a drowning person asking for a different
colored brick because they're building steps to walk out.


It's like a person who fell face down in a puddle claiming they're
drowning in the first place. The brick vs. life preserver question
isn't relevant. They need to stand up and look around. They're not
drowning. They're not even in very deep water.


They've been laying face-down in the puddle so long, they think it's
as wide as the ocean and as deep as a well. They've been down so long
it looks like up.


**Outside the SQL Box**


To get outside the SQL box means to actually stop using SQL even for
metaphoric conversations about data manipulation, persistence,
transactions, auditing, security and anything that seems relevant to
data processing.


To FLESH OUT [*"flesh", the word is "flesh"*] the conversation on
breaking the SQL Hegemony, you can't use hypothetical hand-waving.
You need tangible real-world requirements. You need something
concrete, finite and specific so that you can have a head-to-head
benchmark shootout (in principle) between an RDBMS and something not
an RDBMS.


You may never actually **build** the RDBMS version for comparison.
But you need to create good logging and measurement hooks around your
first noSQL application. The kind of logging and measurement you'd
use for a benchmark. The kind of logging and measurement that will
prove it actually works outside the RDBMS. And it works well:
reliably and inexpensively.


This is entirely about asking for forgiveness instead of asking for
permission.


Managers can't give permission, it involves too much pain.


They can offer forgiveness because it requires neither thinking nor
action.





