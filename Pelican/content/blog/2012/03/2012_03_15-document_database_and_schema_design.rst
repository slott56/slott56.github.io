Document Database and Schema Design
===================================

:date: 2012-03-15 08:00
:tags: couchdb,#python,noSQL,couchdbkit
:slug: 2012_03_15-document_database_and_schema_design
:category: Technologies
:status: published

As part of coming to grips with CouchDB (and a particularly odious
graph-theory problem) I've been looking around for design guidelines,
hints and tips.

This MongoDB `Schema
Design <http://www.mongodb.org/display/DOCS/Schema+Design>`__ document
is quite helpful.  The Link vs. Embed section clarifies the essential
tradeoff here.  In SQL world, link is the only tool.  In this
document-database world of CouchDB and MongoDB (as well as XML schema
design) we have a link vs. embed decision.

Here is a presentation on trees (a specific kind of graph) in a document
database:  `Trees in MongoDB <http://www.mongodb.org/display/DOCS/Trees+in+MongoDB>`__.  It
enumerates a number of alternatives that are part of this new, larger
design space for databases.

I found this because it was referenced in the
`myNoSQL <http://nosql.mypopescu.com/>`__ blog, which seems to be a
collection of sometimes useful links.

A September 2011 DAMA-NY meeting included a presentation on NoSQL Data
Stores.  It's findable on Google if you search for "dama nisql data
stores" [*sic; it is misspelled*].  However, it's hard to link to
directly because of the way Google obscures the target of their search.

What's important in this presentation is the slightly defensive posture
it takes about data modeling.  It seems to describe ways that relational
database modelers can cling to relevance in spite of threats represented
by "NoSQL" databases.

**The Transit System Problem**

For a particularly gnarly problem, look at the `Google Transit Feed
Specification <https://developers.google.com/transit/gtfs/reference>`__.

Then, look at `Hampton Roads
Transit <http://www.gtfs-data-exchange.com/agency/hampton-roads-transit-hrt/>`__
on the GTFS Data Exchange.

How do we build a CouchDB document-centric view of this
highly-normalized graph?

Route-centric?  Each route has multiple trips.  Each trip has a sequence
of stop times.  Do we repeat the stop definition over and over again?

Seems silly, so perhaps it's Route - Trip - Stop-Time as a single
document with links to Stop definitions.

Stop-centric?  Each stop has multiple stop-times, and each stop has a
parent route (based on trips along a route.)  While this allows us to
have a Stop document with a list of stop times and a (generally) single
Route definition, it's not too useful.

We generally use transit based on the routes, not based on a single
stop.  So we need to query the stops based on a Route as well as based
on a Stop Time.  We may be able to use the CouchDB map definitions to
provide some of these alternative views of  a stop (i.e., by stop time,
by route).

**Some No SQL Lessons**

What's really important here is that NoSQL schema design is not
precisely the same as RDBMS schema design.  In the RDMS world, with a
single, fixed schema, proper up-front design is life-or-death.  A great
deal of design hand-wringing is required to get the relational model
correct.  In a good organization, this design effort
involves prototyping, modeling and experimentation.  In a bad
organization, this design effort follows trivialized rules of thumb
without too many second thoughts.

On the other hand, the No SQL schema design is essentially the same as
RDBMS schema design.

In the NoSQL world, we still have to do prototyping, modeling and
experimentation.  We still have the three-tier separation between
conceptual, logical and physical.    Unlike the relational database,
however, these tiers are more closely aligned in a document-oriented
database.  The conceptual tier is usually very, very close to the
logical tier document structure.  The conceptual gaps are filled by
map-reduce views.  The physical tier is just the logical tier document
structure with some description of the sharding policies.

We do have to be more circumspect about committing to a design.  In SQL
world, DDL is a formal commitment to a design.  DDL changes lead to
breakage; making the dependencies more clear.  In NoSQL world, there
isn't the same depth of commitment.  A technical spike which looks
promising can lead to a gradual path of progressive dependence on the
model.

The breakage that comes from schema change is more manageable but can
spin out of control.  It's more manageable because we can design our
application around optional, missing and variant definitions of a
document.  It can become less manageable if we introduce too layers of
useless abstraction to handle schema evolution.

The discipline of an ORM-like mapping between documents and Python
classes is somewhat helpful for keeping the design focused around
documents that have first-class meaning in the problem space.  For that
reason, `couchdbkit <http://couchdbkit.org/>`__ seems useful.



-----

&gt;odious graph-theory problem
Why use CouchDB? W...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-03-16 07:44:55.282000-04:00

>odious graph-theory problem
Why use CouchDB? Why not a true graph database like neo4j.org


Please consider taking a step back and blogging ab...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-03-15 20:30:23.021000-04:00

Please consider taking a step back and blogging about the "four main
NoSQL database categories". Check out "NoSQL and Graph Databases –
Neo4j’s Emil Eifrem at QCON London 2010"
(http://glennas.wordpress.com/2011/04/02/nosql-and-graph-databases-neo4js-emil-eifrem-at-qcon-london-2010/)





