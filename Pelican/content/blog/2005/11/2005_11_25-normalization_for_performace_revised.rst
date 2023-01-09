Normalization for Performace (revised)
======================================

:date: 2005-11-25 20:27
:tags: architecture,design,data structure,algorithm
:slug: 2005_11_25-normalization_for_performace_revised
:category: Architecture & Design
:status: published





Perhaps this is heresy.  Perhaps it merely shows
that the orthodox may be focused on short-term delivery, not long-term
value.



**CONTEXT AND PROBLEM** 



The client has a table we
could describe as following the M.E.S.S. -- Multiple Entity Sub-Species --
design pattern.  The hallmarks of this design are a large number of optional
columns, a large number of null attributes values, and generally sparse
data.



The business reason is that raw
materials ("prospects") are supplied from a variety of customers.  A number of
services are performed, all of which will update the prospect.  Each customer
relationship involves slightly different features of each prospect, but the
overall value-add business process is substantially similar.  The business
processes, viewed from a distance, are all nearly identical; they differ in some
details, but are more alike than
different.



In this case, the situation
is compounded by a C.R.E.E.P. -- the Continuously Re-Evolving Entity Pattern. 
Each "prospect" has an almost indefinite number of features, including events,
conditions, services, processes and relationships.  A CREEP object is often
miscast as a relational row, with each feature modeled as a column.  The
attributes may not be sparse, but they grow without any practical boundary, and
the naive mapping from attribute to column is often
inappropriate.



The biggest consequence
of a MESS + CREEP design is that we have columns which are initially null, but
get filled with large text comments or dates.  We also have text comments which
evolve; rarely getting smaller.  This often leads to issues with the space
allocation in the RDBMS.  Before too long we have highly fragmented storage.  In
the case of Oracle, we have row chaining.   This fragmentation and chaining is a
performance burden with a number of candidate
solutions.



How do we prevent storage
fragmentation and the associated
slow-down?



**FORCES** 



We
can attempt to prevent fragmentation.  On the one hand, an ounce of prevention
has a historical ROI of 1600%.  On the other hand, this is radical surgery to
our way of looking at the problem.  It means one of two approaches: a higher
degree of normalization or pre-allocating storage.  We can easily pre-allocate
storage by using data types like
CHAR(*x* )
which often pre-allocates all
x positions. 
In this case, our rows will never change size when null fields are replaced with
data.  On the other hand, our rows wind up as gigantic objects; we can rarely
fit them within a database block of 4096 characters, making this approach
unworkable.



We can attempt to cure
fragmentation.  On the one hand, we can design any old table, and compound this
design with lots of additional processing to defragment storage periodically. 
While complex and slow, this does permit an incomplete design to be put into
production quickly.  In principle, something good could be said about this
approach, but it's hard to say something good about an incomplete design.  The
"solution" commonly adopted is to throw more processing at a simple problem;
something that is hard to characterize as good
design.



When we look closely at the
normalization of this data we can identify two closely intertwined issues. 
First, we have a MESS table, a number of "prospect" sub-species are collected
into a single, large table.  There are several ways to handle subclasses in a
relational database.  One approach is the unified MESS table, which unifies all
sub-species by providing the union of all possible attributes and making liberal
use of null.  Another approach is to decompose each subclass into distinct
tables.  This makes the processing more complex, since a number of tables must
be used, leading to a number of similar programs that differ in a few column
names and a table name.  



A third
choice is to mirror the sub-species inheritance in the table design.  A core
table contains the superclass attributes: those features which are truly common
(or very nearly common) to all subclasses.  Other tables contain subclass-unique
attributes and are joined to the core table as needed by specific applications. 
When we look at this design closely, we often see that the core table attributes
are not really CREEP-style attributes: they are remarkable stable values.  Rows
go into the core table and stay in one place; minimizing fragmentation in the
normal course of events.



The second of
the intertwined issues is the CREEP problem: we keep tacking features onto this
entity, some of which may not attributes in the narrow sense that attributes
should be understood.  By narrow, we mean the third normal form definition that
each attribute depends on the key and nothing but the key.  What we find is that
some attributes are part of a data tuple that has a timestamp, an actor's name,
a comment string, and possibly an official event or condition.  This is clearly
a subsidiary entity, not a cluster of related columns in the "prospect"
entity.



**SOLUTION** 



When
we find MESS tables that also implement CREEP, the best solution is to properly
normalize the table into a number of distinct entities.  The MESS sub-species
should be split apart based on the commonality of the attributes.  A few
optional columns can help create an intellectually manageable number of tables. 
There's no reason to be overly formal and rigidly denormalize each potentially
distinct sub-entity.  Where entities differ markedly in attributes as well as
processing, clean separate is appropriate.  Where entities differ in only a few
attributes and a bit of optional processing, separation isn't
necessary.



The CREEP attributes are not
really columns in the first place.  The cluster of timestamp, actor's name,
comment string, the official event or condition should be a separate "event" or
"contact" fact table, with the "prospect" being a complex dimension associated
with a long sequence of events.  For performance reasons, a sequence of events
may be aggregated into a summary
attribute.



In this case, adding events,
conditions, situations, and the like merely adds another kind of event to the
event fact table.  This is merely a row in the event-type dimension. 




**CONSEQUENCES** 



Normalizing
the MESS table to separate the sub-species adds tables to the database.  The new
tables, however, are not as sparse.  Further, the separation of data elements
will tend to reduce fragmentation of the data.  Updates will often be focused on
a sub-entity, moving around rows in a smaller and more densely-packed
tables.



Many operations will now
require joins.  However, measurements typically reveal that there are fewer
physical data blocks with the more dense data model.  Further, only the core
"prospect" table has a large number of rows.  The normalized design reduces the
number of data blocks.  The various sub-species tables that are joined in are
often considerably smaller than the core
table.



Many application programs will
have to be rewritten to use the core table plus a sub-entity table.  Generally,
this is done by defining application-specific views to conceal the join and
leave the original program largely unchanged, except for a rename of the
original table to the view of more properly normalized tables.








