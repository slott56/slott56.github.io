The Secret Architect's Cabal
============================

:date: 2010-01-16 07:37
:tags: object-oriented design
:slug: 2010_01_16-the_secret_architects_cabal
:category: Technologies
:status: published

Recently, I had two very weird "meta" questions on the subject of OO
design.

They bother me because they imply that some Brother or Sister
Architect has let slip the presence of the Secret Technologies that
we Architects are hiding from the Hoi Polloi developers.

These are the real questions. Lightly edited to fix spelling and
spacing.

-   "What are the ways to implement a many to many association in
    an OO model?"

-   "Besides the relational model, what other persistence
    mechanisms are available to store a many to many association?"

These are "meta" questions because they're not asking anything
specific about a particular data model or set of requirements. I
always like unfocused questions because all answers are good
answers. Focus allows people to see through the smoke and mirrors
of Architecture.

The best part about these questions (and some similar questions
that I didn't paste here) is that they are of the form "Is there a
secret technique you're not telling us about?"

It's time to come clean. There **is** a Secret Cabal of
Architects. There **are** things we're not telling you.

Many-to-Many
------------

The many-to-many question shows just how successful the Society of
Secrets (as we call ourselves) has been about creating a SQL bias.
When folks draw higher-level data model diagrams that imply (but
don't show) the required many-to-many association table, the
Architects have failed. In other organizations the association
table is So Very Important that it is carefully diagrammed in
detail. This is a victory for forcing people to think only in
implementation details.

In the best cases, the DBA's treat the association table as part
of the "dark art" of being a DBA. It's something they have to
dwell on and wring their hands over. This leads to developers
getting wrapped around the axle because the table isn't a
first-class part of the data model, but is absolutely required as
part of SQL joins.

It's a kind of intellectual overhead that shows how successful the
Secret Architecture Society is.

The presence of a dark secret technique for implementing
association leads to smart developers asking about other such
intellectual overhead. If there's one secret technique, there must
be many, many others.

It is to laugh.

The Secret Techniques for Associations
--------------------------------------

The problem arises when someone ask about the *OO implementation*
of many-to-many associations. It's really difficult to misdirect
developers when the OO implementation is mostly trivial and not
very interesting. There's no easy to add complexity.

In Python there are a bunch of standard collections. The language
has a bunch that are built in. Plus, in Python 2.6, the
collections module has `Abstract Base
Classes <http://docs.python.org/library/collections.html#abcs-abstract-base-classes>`__
that clearly identify all of the collections.

There isn't too much more to say on the subject of many-to-many
associations. That makes it really hard to add secret layers and
create value as an architect.

The best I can do with questions like this is say "I was sworn to
secrecy by the secret Cabal of Architects, so I can't reveal the
many-to-many association techniques in a general way. Please get
the broomstick of the Wicked Witch of the West if you want more
answers."

Persistence
-----------

The persistence question, however, was gift. When someone equates
"relational model" with a "persistence mechanism", we have lots of
room to maneuver. I know that we're talking about a "relational
database" as a "persistence mechanism". However, it's clear they
don't know that, and that's my opportunity to sow murkiness and
confusion.

Sadly, the OS offers us exactly one "persistence mechanism". Yet,
the question implies that the Secret Cabal of Architects know
about some secret "alternative persistence mechanisms" that mere
programmers can't be told about.

Every device with a changeable state appears as a file. All
databases (relational, hierarchical, object, whatever) are just
files tarted up with fancy API's that allow for performance and
security. Things like indexing, locking, buffering, access
controls, and the like are just "features" layered on top of
good-old files. But those features are So Very Important, that
they appear to be part of persistence.

Excellent.

Logical vs. Physical
--------------------

What's really helpful here is the confusion folks have with
"Logical" vs. "Physical" design layers.

Most DBA's claim (and this is entirely because of ERwin's use of
the terms) that physical design is when you add in the database
details to a logical design. This is wrong, and it really helps
the Architect Secret Society when a vendor misuses common terms
like that.

The Physical layer is the file-system implementation. Table spaces
and blocks and all that what-not that **is** the underlying
persistence.

The Logical layer is what you see from your API's: tables and
views.

The relational database cleanly separates logical from physical.
Your applications do not (indeed, can not) see the implementation
details. This distinction breaks down in the eyes of DBA's,
however, and that lets us insert the idea that a database is
somehow more than tarted-up files.

Anyone asking about the "relational model" and "persistence
mechanism" has -- somehow -- lost focus on what's happening inside
the relational database. This allows us to create Architectural
Value by insisting that we add a "Persistence Layer" underneath
(or on top of or perhaps even beside) the "Database Layer". This
helps confuse the developers by implying that we must "isolate"
the database from the persistence mechanism.

Many-to-many and ORM
--------------------

Sadly, these two questions may turn out to be ORM questions. The
problem with ORM layers is that the application objects are
trivially made persistent. It's really hard to add complexity when
there's an ORM layer.

However, a Good Architect can sometimes find room to maneuver.

A programmer with SQL experience will often think in SQL. They
will often try to provide a specific query and ask how that SQL
query can be implemented in the ORM layer. This needs to be
encouraged. It's important to make programmers think that the SQL
queries are *First Class Features*. The idea that class
definitions might map directly to the underlying data must be
discouraged.

A good DBA *should* insist on defining database tables first, and
then applying the ORM layer to those tables. Doing things the
other way around (defining the classes first) can't be encouraged.
Table-first design works out really well for imposing a
SQL-centered mind-set on everyone. It means that simple
application objects can be split across multiple tables (for
"performance reasons") leading to hellish mapping issues and
performance problems.

No transaction should make use of SQL set-oriented processing
features. Bulk inserts are a special case that should be done with
the database-supplied load application. Bulk updates indicate a
design problem. Bulk deletes may be necessary, but they're not
end-user oriented transactions. Bulk reporting is not
transactional and should be done in a data warehouse.

Subverting the ORM layer by "hand-designing" the relational
database can create a glorious mess. Given the performance
problems, some DBA's will try to add more SQL. Views and Dynamic
Result Sets created by Stored Procedures are good ways to make the
Architecture really complex. The Covert Coven of Architects likes
this.

Sometimes a good developer can be subvert things by creating a
"hybrid" design where some of the tables have a trivial ORM
mapping and work simply. But. A few extra tables are kept aside
that don't have clean ORM mappings. These can be used with
manually-written SQL. The best part is populating these extra
tables via triggers and stored procedures. This assures us that
the architecture is so complex that no one can understand it.

The idea of separating the database into Logical and Physical
layers hurts the Architectural Cabal. Wrapping the Logical layer
with a simple ORM is hurtful, too. But putting application
functionality into the database -- that really helps make
Architecture appear to be magical.

The Persistence Mechanisms
--------------------------

The bottom line is that the Secret Conference of Architects
doesn't have a pat answer on Persistence Mechanisms. We have,
however, a short list of misdirections.

-   API and API Design. This is a rat-hole of lost time. Chasing
    API design issues will assure that persistence is never really
    found.

-   Cloud Computing. This is great. The cloud can be a great
    mystifier. Adding something like the Python Datastore API can
    sow confusion until developers start to think about it.

-   Multi-Core Computing. Even though the OS handles this
    seamlessly, silently and automatically, it's possible to really
    dig into multi-core and claim that we need to rethink software
    architecture from the very foundations to rewrite our core
    algorithms to exploit multiple cores. Simply using Unix
    pipelines cannot be mentioned because it strips the mystery
    away from the problem.

-   XML. Always good a for a few hours of misdirection. XML as a
    hierarchical data model mapped to a relational database can
    really slow down the developers. Eventually someone figures it
    out, and the Architect has nothing left to do.

-   EJB's. This is digging. It's Java specific and -- sadly --
    trumped by simple ORM. But it can sometimes slow the
    conversation down for a few hours.



-----

He he, nice post :)
-------------------

Unknown<noreply@blogger.com>

2009-12-28 13:26:00.245000-05:00

He he, nice post :)


There is no Secret Architectural Society. It is a ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-12-31 04:23:49.563000-05:00

There is no Secret Architectural Society. It is a lie. Mr Lott will be
disciplined. You have not read this post.


&quot;list of misdirections&quot;

I knew it! I ju...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2009-12-28 20:30:33.514000-05:00

"list of misdirections"
I knew it! I just knew it! Architects are like magicians, they make
something happen and then your stuck wondering how they did that. :-)





