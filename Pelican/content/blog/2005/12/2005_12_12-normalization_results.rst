Normalization Results
=====================

:date: 2005-12-12 12:16
:tags: architecture,design,data structure,algorithm
:slug: 2005_12_12-normalization_results
:category: Architecture & Design
:status: published





Experimental results depend on details of the
database server and the data model used.  Actual application software may have
other confounding problems that make these results less dramatic or more
dramatic when applied to a existing application
design.



I compared three table designs
described in a previous posting `Normalization Experiment Protocol <{filename}/blog/2005/12/2005_12_01-normalization_experiment_protocol_revised.rst>`_:

-   The multiple entity sub-species MESS with
    many NULL columns and updates.

-   A partially normalized table with "core"
    entities and "extension" entities.

-   A fully normalized table that extracts
    all of the extra entities to create rows from related clusters of
    columns.



I used three update scenarios
for each design.  The first job did only two updates -- one to update each
sub-entity's attributes.  I compared this with scenarios doing five updates and
ten updates.  The higher number of updates would show the effects of any storage
reclamation strategy the RDDBMS
used.



The MESS storage grew by a factor
from 1.58 to 2.67, as expected.  Each update replaced NULL's or short strings
with longer strings, taking up more storage, leading to rows being placed
elsewhere in the file structure.



The
MESS query time, however, did not grow as rapidly as the storage did.  There is
only a 12% penalty from fragmentation.  This is interesting, and most likely
reflects the very small size of the sample data (100 rows).  Since the database
only occupies a few physical blocks, it can be read quite rapidly in spite of
fragmentation.  A larger database would have a larger performance
penalty.



The partially normalized
storage grew by a factor from 1.62 to 2.12.  Separating the columns which change
from the columns which are static reduces fragmentation.  Query performance, as
expected from doing joins and using unique indexes, was 49% to 56% longer after
a series of updates to this
structure



The fully normalized storage
grew by a factor from 1.73 to 2.23.  The fully normalized version had one row in
each table before fragmentation, and a number of rows after fragmentation. 
Query performance took between 46% and 104% longer after the updates due to the
change in cardinality from 1:1 to 1:n. 




Comparison between structures reveals
that the partially normalized has a performance penalty of just 14%.  Without
fragmentation, the partially normalized structure may actually return results
faster than the denormalized MESS.  The fully normalized structure, with a 1:n
join has a performance penalty of 68% to 131%.




**Bottom Line** 



The MESS has a storage penalty
as well as processing complexity and a risk of failure when defragmenting.  For
these reasons, it is unacceptable for transactional processing.  However, query
performance is 23% better than a fully normalized design, so it is suitable for
the Write Once Read Many world of data warehousing.  Making changes to this
table can be devastating to transactional
applications.



The fully normalized
design has a performance penalty, but is a big enhancement and maintainability
win.  While it uses more storage, application changes involve merely adding
rows, not adding columns.  This immunizes the application programs against
change.  There is some fragmentation from updates, but since the rate of growth
is smaller, the frequency of defragmentations is reduced which reduces the risk
of failure during defragmentation.



A
semi-normalized design does not endure the same level of fragmentation as a
denormalized MESS design.  Since it uses a 1:1 join instead of a 1:m join, the
performance is generally quite good.  Further, change can often be isolated to
the extension table, offering some protection from devastating change.  The rate
of fragmentation is the lowest and the performance penalty from a 1:1 join is
also quite low.



The management overview
is this:

-   Normalization is slow, but low
    maintenance and easy to enhance.

-   Denormalization is fast but suffers
    fragmentation; it is high maintenance and hard to
    enhance.



This semi-normalized version,
however, requires the most insight to create.  It requires understanding the
attributes and their semantics.  Since a MESS design is little more than a
collection of attributes, the investment in understanding is minimal.  A fully
normalized design requires a complete understanding of the entities are defined,
but less knowledge of the update use
cases.



Investments made in
understanding the application data and processing can pay dividends by reducing
administrative busy-work and reducing the risk of problems that are caused by
that administrative overhead.  Further, understanding the application can lead
to optimization of the data and the associated processing.













