Escaping the Relational Schema Trap
===================================

:date: 2011-02-02 08:00
:tags: design,SQL,noSQL
:slug: 2011_02_02-escaping_the_relational_schema_trap
:category: Technologies
:status: published

We're struggling with our Relational Schema. We're not alone, of course,
everyone struggles with the relational model. The technology imposes
difficult limitations and we work around them.

There's kind of a 4-step process through which the relational schema
erodes into irrelevance. The concept of a schema is not irrelevant.
It's the rigid relational schema that's a problem.

Many DBA's will say that the relational model is the ultimate in
flexibility. They're right, but they're missing the point. The
relational database clearly separates the physical storage from
the logical model as seen in tables and columns. It's flexible,
but the presence of a rigid relational schema limits the pace of
business change.

"Clearly," the DBA says, "you don't know how to use ALTER." I beg
to differ. I can use ALTER; however, it doesn't permit the broad,
sweeping scope of change that the business demands.

In order to attempt to match the pace of business change, we're
using an ORM layer. This allows us to fabricate methods and
properties left, right and center. We can tackle some pretty big
problems with simple code changes. This, however, is no longer
helping.

Straws and Camels
-----------------

When designing a database, we have to be cognizant of the nature
and tempo of change. In highly-regulated, very settled business
applications (back-office accounting, for example) the data model
is well known. Changes are mostly distinctive reporting changes
and the tempo is pretty lethargic. It's the back office. Sorry,
but innovation rarely happens there.

Each change is just a another hand-full of straw thrown on the
camel's back. It happens fairly slowly. And there aren't many
surprises. Hacks, workarounds and technical debt accumulates
slowly.

In innovative, novel, experimental businesses, however, the nature
and tempo are very different. The changes are disruptive, "what
are you saying?" kinds of changes. They are "throw out the
bathwater, the babies, the cribs and fire the nursemaid" kinds of
changes. The tempo is semi-annual reinvent everything. Hacks,
workarounds and technical debt get out of control suddenly.


**Important Lesson Learned**. When the customer misunderstands
the offering and asks for something completely senseless, it's
good to listen and try to build that -- even if it wasn't what
you were offering. In some cases, the original offering was too
complex or contrived. In other cases, the offering didn't
create enough value. But when you offer **[X]** and the
customer asks how much it will cost for **[Y]**, you have
disruptive, sudden, and surprising database changes.

This is bales of hay through onto an unprepared camel. Backs can
get broken.

Coping
------

One common coping strategy is SQL ALTER statements to fiddle with
the logical model. This has to be coupled with CREATE TABLE AS
SELECT scripts to do open-heart surgery on the logical model.
Married with modified ORM definitions. This requires some careful
"schema versioning" techniques.

Another coping strategy is lots of "Expansion" columns in the
tables. These can be renamed and repurposed without physical
storage changes. The rows haven't physically changed, but the
column name morphed from "EXPANSION_INT_01" to
"Some_Real_Attribute". This doesn't prevent the CREATE TABLE AS
SELECT scripts to do open-heart surgery. It still requires some
careful "schema versioning" techniques to be sure that the ORM
layer matches the logical schema.

A third -- and perhaps most popular -- coping strategy is
manpower. Just having dedicated DBA's and maintenance programmers
is a common way to handle this. Some folks object, saying that a
large staff isn't a way to "cope with change" but is a basic "cost
of doing business".

It's false, by the way, to claim that dedicated DBA's are
essential. A solo developer can design and implement a database
and application software with no help at all. Indeed, in most
organizations, developers design and build databases, then turn
them over to DBA's for operational support. If the nature of
change is minor and tempo of change is slow, a solo developer can
deal perfectly well with the database. A dedicated DBA is someone
we **add** when the developer gets swamped by too much change.

(Some DBA's like to claim that the developers never get
normalization or indexing correct. I counter with the observation
that some DBA's don't get this right, either. DBA's aren't
**essential**. They're a popular way to cope with the nature and
tempo of change.)

In the ORM world, there are schema migration toolkits. Projects
like `Storm <https://storm.canonical.com/>`__, this
`list <http://code.djangoproject.com/wiki/SchemaEvolution>`__ for
Django, `Embarcadero Change
Manager <http://www.embarcadero.co.uk/products/db-change-manager-xe>`__
for Oracle, and numerous others attempt to support the schema
evolution and change management problem. All of this is a clever
way to cope with a problem inherent in our choice of technology.

Chaos Theory
------------

Rather than invent clever coping mechanisms, let's take a step
back. If we're inventing technology to work around the fixed
relational schema, it might be time to rethink the relational
schema.

"Oh noes," DBA's cry, "we must have a fixed logical model
otherwise chaos ensues."

Really? How come we're always altering that schema? How come we're
always adding tables and restructuring the tables?

"Oh that? That's 'controlled change'," the DBA responds.

No, that's slow chaos.

Here's how it plays out. We have a disruptive change. We negotiate
with the DBA's to restructure the database. And the test database.
And the QA database. We do the development database without any
help from the DBA's. We fix the ORM layers. We unit test the
changes.

Then we plan and coordinate the production rollout of this change
with the DBA's. Note. We already made the change in development.
We're not allowed to make the change in production. The DBA's then
suggest design alternatives. Normalization isn't "right". Or there
are physical changes that need to be declared in the table
definitions. We redo the development database. And the ORM layer.
And rerun the unit tests.

Because the production database couldn't be touched -- and we had
paying customers -- we copied production data into a development
database and started doing "production" in development. Now that
we're about to make the official production change, we have two
databases. The official database content is out-of-date. The
development database is a mixture of live production and test
data. Sigh.

Rethinking Schema
-----------------

If the schema is a problem, perhaps we can live without it. Enter
NoSQL databases.

Here's how you start down the slippery slope.

**Phase I**. You need a fairly radical database change. Rather
than wait weeks for the DBA's, you ask for a single "BLOB" column.
You take the extra data elements for the radical change, JSON
encode them, and store the JSON representation in the BLOB field.
Now you have a "subschema" buried inside a single BLOB column.

Since this is a simple ALTER, the DBA's will do it without a lot
of negotiation or delay. You have a hybrid database with a mixture
of schema and noSQL.

**Phase II**. You need an even more radical change. Rather than
wait weeks for the DBA's, you ask for a few tables that have just
a primary key and a BLOB column. You've basically invented a
document-structured database inside SQL, bypassing the SQL schema
entirely.

**Phase III**. While waiting for the Phase II changes to be
implemented, you convert the customer data from their obscure,
stupid format into a simple sequential file of JSON documents and
write your own simple map-reduce algorithms in Python. Sure,
performance is poor, but you're up and running without any
database overheads.

**Phase IV**. Start looking for alternatives.

`MongoDB, CouchDB, MySQL Compare Grid <http://www.mongodb.org/display/DOCS/MongoDB,+CouchDB,+MySQL+Compare+Grid>`__

This MongoDB looks really nice.
`PyMongo <http://api.mongodb.org/python/1.7%2B/tools.html#framework-tools>`__
offers lots of hints and guidance.

At least one person is looking at
`mango <https://github.com/vpulim/mango>`__, a MongoDB database
adapter for Django. For us, this isn't the best idea. We use
OpenAM for identity management, so our Users and Sessions are
simply cloned from OpenAM by an `authentication
backend <http://docs.djangoproject.com/en/dev/ref/authbackends/>`__
that gets the user from OpenAM. SQLite works fine for this.

We think we can use Django's ORM and a relational database for
User and Session. For everything else, we need to look closely and
MongoDB.

Wins and Losses
---------------

The big win is the ability to handle disruptive change a little
bit more gracefully.

The big loss in switching away from the Django ORM is we lose the
built-in admin pages. We have to build admin Forms and view
functions. While this is a bit of a burden, we've already
customized every model form heavily. Switching from ModelForm to
Form and adding the missing fields isn't much additional work.

The biggest issue with document-oriented data models is assuring
that the documents comply with some essential or core schema.
Schemas are inescapable. The question is more a matter of how the
schema limits change. Having a Django Form to validate JSON
documents for the "essential" features is far more flexible than
having a Django Model class and a mapping to a relational
database.

Schema migration becomes a non-issue until we have to expand the
essential schema, which changes the validation rules, and may
render old documents retroactively invalid. This is not a new
problem -- Relational folks cope with this, also -- but if it's
the *only* problem, then we may have streamlined the process of
making disruptive business changes.



-----

Before looking at MongoDB and their ilk, ask if AC...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-02-04 18:57:21.271000-05:00

Before looking at MongoDB and their ilk, ask if ACID (atomicity,
consistency, isolation, durability) [ie, the transaction thing] is a
business requirement.
Check out "Dropping ACID with MongoDB"
http://www.slideshare.net/kchodorow/dropping-acid-with-mongodb


Article: Real World NoSQL: Amazon SimpleDB at Netf...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-02-05 10:57:48.187000-05:00

Article: Real World NoSQL: Amazon SimpleDB at Netflix By GUY HARRISON of
GigaOm - February 4, 2011
Relational database transactions were depreciated in favour of
SimpleDB’s optimistic concurrency mechanism, which allows modifications
to proceed only if an item is unchanged since it was last accessed


You can take a look at mongoengine (http://mongoen...
-----------------------------------------------------

Jaime<noreply@blogger.com>

2011-02-02 08:17:07.851000-05:00

You can take a look at mongoengine (http://mongoengine.org/) It's an
"ORM" for MongoDB made to be extremely similar to Django ORM.
In the last version, they integrate the authentication with MongoDB (I
haven't test it)


&quot;Oh that? That&#39;s &#39;controlled change&#...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-02-02 18:17:45.938000-05:00

"Oh that? That's 'controlled change'," the DBA responds.
No, that's slow chaos.
Hilarious.
BTW, awesome blog post!


Check out

How FriendFeed uses MySQL to store sche...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-03-05 16:53:24.035000-05:00

Check out
How FriendFeed uses MySQL to store schema-less data
By Bret Taylor · February 27, 2009
http://bret.appspot.com/entry/how-friendfeed-uses-mysql





