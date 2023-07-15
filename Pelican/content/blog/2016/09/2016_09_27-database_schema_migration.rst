Database Schema Migration
=========================

:date: 2016-09-27 08:00
:tags: data migration,database design,database administration,schema migration
:slug: 2016_09_27-database_schema_migration
:category: Technologies
:status: published

Some
thoughts: http://workingwithdevs.com/delivering-databases-migrations-vs-state/


This covers a lot of ground on the **Declarative vs. Procedural**
question. It explains a lot of the considerations that lead to
choosing a procedural schema evolution vs. a declarative schema with
an implied change sequence to migrate to each new declared state.


The article calls the declarative "state-based" and procedural
approach "migration-based".


My 2¢ are focused on this point:


  When using a state-based solution you will most often be using a
  diff tool like those provided by Redgate or Visual Studio to
  examine the differences and generate an upgrade script. While this
  is a very efficient solution for most changes, with table renames
  and a few other types of table refactoring they can do bad things,
  ...


This point about table refactoring is, for me, the show-stopper.
Relational theory tells me that I can map any schema to any other
schema using selection, projection, and join. I can denormalize
data and I can normalize again via group-by clauses. I can reduce
the original schema to a sequence of object-attribute-value
triples, and restructure this into any desired new schema.


Given enough time, a change tracking tool should be able to find a
minimal-cost transformation from schema to schema. This might
involve a complex search over a large state space, and it
certainly involves creating costs for each alternative query
plan.


Pragmatically, I'm not sold on this being a good idea. And I'm rarely
sure I even want to get involved in a fully automated solution. While
a tool might be able to detect and automate a variety of simple
changes, I think that developers must **always** vet those change
scripts.


In particular, the search space is emphatically **not** limited to
select, project, and join. There are also database unload-reload,
index create and drop. There are even more complex operations like
creating intermediate results which aren't part of the final database
structure. With proper indices, these might actually be beneficial.

In some cases, the continuous operation requirements are such that we
might have two copies of a database: one being used and the other
being transformed. A logger tracks transactions in the older copy and
a synchronizer replicates those transactions in the new copy. After
the data is moved, the customer access is moved via a feature toggle
from the old database to the new database.


Semantic Drift
--------------

Also important is the issue of semantic drift. When we're making
structural changes where the "before" column names match the "after"
column names, then there's little chance for semantic drift. There's
still some possibility, though. We can (and sometimes do) repurpose
columns, preserving the original name. In some cases, we might change
a database constraint without renaming the column.


In the larger case, of course, it doesn't require "‘hot-fix’ changes
to QA or even production databases" to create profound semantic
changes. All it takes is an app developer deciding that a column
should be repurposed. There's may be no structural change on the
schema overall.


A non-structural change in some past release could have implications
for structural change in a future release. Imagine three columns in
three tables with the same names. Two started out life as simple
foreign keys to the third. But one became optional, and now the
semantics don't match but the names do. Automated tools are unlikely
to discern the intent here.


Conclusion?
------------

It's all procedural migration. I'm not declarative ("state") tools
can be trusted beyond discerning the changes and suggesting a
possible migration.





