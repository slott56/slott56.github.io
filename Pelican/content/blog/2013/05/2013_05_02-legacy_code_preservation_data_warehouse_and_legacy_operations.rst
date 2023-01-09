Legacy Code Preservation: Data Warehouse and Legacy Operations  
================================================================

:date: 2013-05-02 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_05_02-legacy_code_preservation_data_warehouse_and_legacy_operations
:category: Technologies
:status: published

A data warehouse preserves data.

It can be argued that a data warehouse preserves **only** data. This,
however, is false.

To an extent, a data warehouse must also preserve processing details.

Indeed, a data warehouse exemplifies knowledge capture because the
data and its processing steps are both captured.

The ETL process that prepares data for loading into the warehouse is
tied to specific source applications that provide data in a known
form and a known processing state. A warehouse isn't populated with
random data. It's populated with data that is at a known, consistent
state.

For example, when loading financial data, the various accounting
applications (like the General Ledger) must be updated with precisely
the same data that's captured for data warehouse processing. Failure
to assure consistency between ledger and warehouse makes it difficult
to believe that the warehouse data is correct.

.. rubric:: Preserving Details
   :name: preserving-details

In some cases, legacy applications have a tangled architecture.
Code can be repeated because of copy-and-paste programming. This
can make it difficult to be sure that a data warehouse properly
captures data in a consistent state.

What's distressingly common is to have a "code" or "status" field
where the first or last position has been co-opted to have
additional meanings. A "9" in the last position of a product
number may be a flag for special processing.

These cryptic flags and indicators are difficult to identify in
the first place. They are often scattered throughout the
application code base. Sometimes they reflect work-arounds to
handle highly-specialized situations. Other times, they're
pervasive changes that were done via cryptic flags rather than
make a first-class change to a file format.

When populating a warehouse, these codes and flags and secret
processing handshakes need to be found and properly normalized.
This may mean that an ETL program will recapitulate different
pieces of special-case logic that's scattered around a number of
legacy programs.

This is the essence of knowledge capture.

It also drives up the cost and expense of maintaining the ETL
pipeline that feeds the data warehouse.

After all, the source application can make processing changes that
aren't properly reflected in the ETL processing pipeline.

As if this isn't bad enough, many organization permit technology
that makes processing even more obscure.

.. rubric:: The Evils of Stored Procedures
  :name: the-evils-of-stored-procedures

In far too many cases, software architectures place code into two
locations.

-  Application programs.
-  Data bases.

Putting code into a database is simply a mistake. There's no
rational justification. None.

The irrational justifications include the following farcical
claims.

-   Stored Procedures are faster.

    Not really. There's no reason why they should be faster, and
    simple benchmark measurements show that application programs
    outside the database will be as fast or faster than stored
    procedures. A process running **outside** the database doesn't
    compete for database resources the same way the stored
    procedure engine does.

-   Some processing is essential to data integrity.

    This is absurd, since it presumes that the folks writing stored
    procedures are trustworthy and folks writing non-stored
    procedure applications are a lying bunch of thieving scoundrels
    who will break the data integrity rules if given half the
    chance.

Let's look at this second justification.
The argument has two variants.

#.  Some logic is so essential to interpreting the contents of
    the database that it cannot meaningfully be packaged any
    other way.

    This makes the claim that all sharable programming technology
    (Java packages, Python modules, etc.) simply don't work, and
    the database is the only effective way to share code.

#.  Some logic is so essential to correct status of the
    database, that no application developer can be trusted to
    touch it.

    This presumes that application developers are willing to cut
    corners and break rules and force bad data into an otherwise
    pristine database. Data integrity problems come from those
    "other" developers. The DBA's can't trust anyone except the
    stored procedure author.

When confronted with other ways to share logic, the stored
procedure folks fall back on "faster" or possibly the "Us vs.
Them" nature of the second variant.

.. rubric:: Stored Procedure Consequences
   :name: stored-procedure-consequences

Stored procedures really are code. They should not be separated
from the rest of the code base.

Stored procedures are maintained with different tools and through
different organizations and processes. This leads to conflict and
confusion.

It can also lead to weird secrecy.

A stored procedure can be difficult to extract from the database.
It may require privileges and help from DBA's to locate the
unencrypted original source text.

In a huge organization, it can take weeks to track down the right
DBA to reveal the content of the stored procedure.

Why the secrecy?

Once exposed, of course, the stored procedure can then be
rewritten as proper code, eliminating the stored procedure.
The proper question to ask is "Why is critical business knowledge
encoded in so many different places?" Why not just application
code? Why also try to encode some knowledge in database stored
procedures? How does this bifurcation help make the origination
more efficient?



-----

For a related article on the subject, check out Ho...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2013-05-04 08:58:23.063000-04:00

For a related article on the subject, check out How To Survive a
Ground-Up Rewrite Without Losing Your Sanity - aka: Screw you Joel
Spolsky, We're Rewriting It From Scratch!
http://onstartups.com/tabid/3339/bid/97052/How-To-Survive-a-Ground-Up-Rewrite-Without-Losing-Your-Sanity.aspx





