NoSQL -- Old Wine, New Bottle
=============================

:date: 2010-10-18 10:15
:tags: architecture,noSQL,design
:slug: 2010_10_18-nosql_old_wine_new_bottle
:category: Technologies
:status: published

Got an email with links about NoSQL. Links like "`Going NoSQL with
MongoDB <http://msdn.microsoft.com/en-us/magazine/ee310029.aspx>`__".
This -- like many such articles -- includes the phrase "the NoSQL
movement" as if there's something new going on. Thank goodness Ted
Neward includes quotes around "new". This isn't new. And doubly good,
Neward doesn't use words like "excitement".

Some folks like to link to http://en.wikipedia.org/wiki/NoSQL. This
is misleading, of course, since avoiding SQL isn't new or even that
interesting. If you're going to treat avoiding SQL specially, then
you should have a NoProceduralProgramming, NoFunctionalProgramming,
NoAssembler, NoShellScript and NoHTML movements, also.

Why stop there? Why not have a **NoDumbAssArchitecture** movement,
too?

If you want to see dumb, breathless stuff, however, use Google and
search for "nosql excitement". You'd think that the `file
system <http://en.wikipedia.org/wiki/File_system>`__ was new
technology. In particular, posts like "`NOSQL Movement - Excited with
the coexistence of Divergent
Thoughts <http://java.dzone.com/news/nosql-movement-excited>`__" seem
silly.

Unless -- I guess -- you've been solving all data management problems
with a relational database. I guess when you discover that you don't
have to use the hammer, then it's exciting to see that everything
isn't simply a nail, either.

If avoiding the hegemony of SQL seems important, or even interesting,
perhaps you've been living in a cave. Seriously. The file system has
always been there and has always worked nicely for lots of problems.
My 2002-era Ralph Kimball Data Warehouse Toolkit books are very clear
that large, high-volume data warehouses are mostly flat files. Data
marts are SQL databases suitable for ad-hoc SQL queries. But the
RDBMS isn't always the best place for large volumes of data.

**Bottom Line**

NoSQL isn't new or even very interesting.

**Consequences**

If you're an architect, but you're not looking at alternatives to the
RDBMS -- and running benchmarks to compare the choices -- you're not
really doing architectural work. You're probably a glorified
programmer and should consider working in a place that doesn't stifle
you by imposing a "one world -- one architecture" viewpoint.

If you're a manager and think that "everything in SQL" is a
risk-reducer, you need to actually talk to your people. If you think
that your people's skills are limited to SQL, you're doing your team
(and your customers) a disservice. Consider a skill upgrade of your
own. Your team can learn other non-RDBMS technologies. Perhaps you
should stop stifling them.

If you're a DBA and you know -- for a fact -- that the relational
database is perfect and complete, you should perhaps pause a moment
and consider things the relational databases don't do well.
Graph-theory problems and hierarchies require fairly complex
workarounds. Even a many-to-many relationship requires this extra
association table. Perhaps those things are the signs of
force-fitting data into the RDBMS model.



-----

NoSQL is a marketing brand, not a technology or ar...
-----------------------------------------------------

Bill Karwin<noreply@blogger.com>

2010-07-27 13:36:31.339000-04:00

NoSQL is a marketing brand, not a technology or architecture term. All
the hype and "newness" and "excitement" makes more sense if you view it
in this context.

As for many-to-many tables, this is not a good example of
"force-fitting".

Take for example regular expressions. Making a regular expression to
match any problem you throw at it is really easy! Here it is: .\*
The hard part is making a regular expression that matches your valid
input, but also rejects invalid input.
So it is with relational databases. Accept valid input, reject invalid
input.


NoSQL means Not Only SQL. So, it&#39;s not about a...
-----------------------------------------------------

Luca Bruno<noreply@blogger.com>

2010-07-28 14:00:49.129000-04:00

NoSQL means Not Only SQL. So, it's not about avoiding SQL, it's about
enhancing data management with a different approach when it makes sense.
It's about integration.


Big Data and NoSQL March to the Enterprise
By GARY...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-11-01 12:21:28.428000-04:00

Big Data and NoSQL March to the Enterprise
By GARY ORENSTEIN of GigaOm
Published: October 30, 2010
url:
http://www.nytimes.com/external/gigaom/2010/10/30/30gigaom-big-data-and-nosql-march-to-the-enterprise-73963.html?ref=technology


Notes from A NOSQL Evening in Palo Alto 
DateThurs...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-30 15:11:42.222000-04:00

Notes from A NOSQL Evening in Palo Alto
DateThursday, October 28, 2010 at 10:35AM
url:
http://highscalability.com/blog/2010/10/28/notes-from-a-nosql-evening-in-palo-alto.html


Snowflake data warehouse
-----------------------------------------------------

Lafay Tech Plaza<noreply@blogger.com>

2021-08-13 10:55:17.852000-04:00

`Snowflake data
warehouse <https://www.indiumsoftware.com/data-warehouse-services/>`__
is a cloud-based data warehouse that uses a unique data model optimized
to manage both structured and unstructured data at scale. It
dramatically simplifies ETL processes, allowing users to focus on data
modeling and business insights.





