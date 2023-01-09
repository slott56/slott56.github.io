What a Data Warehouse Can Never Do
==================================

:date: 2007-01-12 14:40
:tags: #python,database
:slug: 2007_01_12-what_a_data_warehouse_can_never_do
:category: Python
:status: published





In one form, the question is "How do we handle
the [X] transaction in the warehouse?"  Another form of the question is "What do
we do when [Y] changes?"   The third form is less clear, but essentially the
same: "How do we maintain [Z] in the
warehouse?"



All of these are questions
that superficially cover change management, but we're not really talking about
Kimball's **Slowly Changing Dimension**  (SCD) design pattern.  It turns out,
we're talking about something more subtle and
confusing.



**System of Record.** 



The real questions are
**System of Record**  (SoR) questions.  In short, each
question is a version of "Where's the authoritative copy, and how do I keep it
current?"

-   The [X] transaction is, at least in
    theory, part of a source application, a System of Record.  It is extracted from
    SoR, transformed, and loaded into the warehouse.  The [X] transaction does not
    change when the warehouse is implemented.  Unless, of course, there is no
    SoR.

-   The changes to [Y], similarly, should be
    made in the SoR.  This is almost the same question as the "[X] transaction"
    question, but it's asked about a piece of data, not a named business process. 
    The distinction reveals much about the processes which the warehouse must
    support.

-   The maintenance of [Z], clearly, should
    be made in the SoR.  This is similar to the "changes to [Y]" question, but shows
    a different point of view on what data is and why it
    exists.



We'll look at these questions
in a bit of depth.



**Transactions in the Warehouse.** 



When someone asks
about the "[X] transaction," they're often summarizing a business process.  In
general, every business process is either informal, or formalized.  Informal
transactions are done manually using desktop tools: email, spreadsheet, word
processing, etc.  No piece of software captures, manages and enforces the
transaction.



Formal transactions have
three general patterns for their SoR: one SoR, many SoR's and a badly-chosen
SoR.  When there's one SoR, life is good.  The transaction happens in some
system (SAP, Oracle, QuickBooks, Aptiva, etc.)  It propagates through the
organization through ordinary Enterprise Application Integration (EAI)
techniques.  It winds up in the warehouse through ordinary
Extract-Transform-Load (ETL)
processing.



When there are multiple
SoR's, we have some challenges.  Sometimes, the relationship is
*horizontal* :
two peer business units have separate sources for similar data.  One unit has
SAP, the other has Aptiva.  This means that there may be common data which must
be conformed into a warehouse dimension.  So far, so good. 




Sometimes the relationship between
SoR's is
*vertical* :
the parent company uses SAP, the subsidiary uses Great Plains.   This means that
there may be contradictions between the views of the common data.  When data is
moved up from the subsidiary, it may be aggregated: business entities are
elided, and the data is difficult (or impossible) to
conform.



Sometimes the relationship
between SoR's is
*psychotic* .
This often leads to a badly-chosen SoR.  A single organization can have the same
data in two applications and neither can be trusted to be the SoR.  They may
have customer data in Siebel and JDE, and the data is different, and can only be
reconciled manually.  Sigh.  No amount of Data Warehouse ETL can sort this out. 
The organization must pick something as the SoR, and revise their business
processes to reflect that.



In summary,
there are no transactions in the warehouse.  Transactions happen in the SoR, and
the results of those transactions are applied to the warehouse.  You must pick
an SoR.



**Change in the Warehouse.** 



Sometimes, there is no
System of Record.  There are two common cases: the data is maintained manually,
and the data is maintained through a cryptic transaction buried in the legacy
reporting application.  When data is maintained manually, we have a rather
difficult **Master Data Management**  (MDM) issue because we don't have
an official SoR.  We're often in a bad position, here, because we're forced to
stop data warehouse development work to put a SoR in place.  This extra work can
be hard to justify; managers say "we never needed a system for that before, why
now?"



The answer is simple, but
unpleasant.  "It never worked before, either."  People put in data warehouses
because their legacy reporting tools are incorrect or inconsistent.  One root
cause of errors is lack of a public, well-understood truth because of manual or
informal changes.  



The cryptic
transaction is the worst thing to ferret out.  Let's say we have two
applications, B and C which each do parts of a business function.  Further, each
has it's little quirks, and we periodically must reconcile B and C's results
against each other.  How do we do this reconciliation when the two applications
are largely disjoint except where they have to be
reconciled?



The usual solution is to
merge the data into a kind of data warehouse.  However, when there are
reconciliation problems, we hate to make a change to B or C, and re-run the
complete ETL cycle.  Instead we make the change directly in the warehouse.  Who
wants to duplicate this change in B or C?  No one, so we back-propagate the
change from the warehouse into the SoR's.  In effect, we've made the warehouse
the SoR.



In summary, change in the
warehouse is limited to a historical snapshot of change in the SoR.  Change
happens in the SoR, and the results of the changes are applied to the warehouse.
You must pick an
SoR.



**Maintenance in the Warehouse.** 



The question of
maintaining data in the warehouse usually stems from a warehouse design which
involves something more complex than simple facts and dimensions.  Generally, a
bridge table (often for a hierarchy) becomes a source of confusion.  Most
business entities (dates, accounts, products, documents, etc.) are pretty clear
in the source applications.  The facts are usually
obvious.



It's the reporting
relationships that get confusing.  Something like product family can be a very
difficult thing to handle.  Something like a bill of materials (BoM) or
Organization Hierarchy (OH) can be even more
complex.



In the product family case,
the reporting is an organization fiction.  It doesn't tie back to anything
except how managers chunk information.  In this case, the reporting hierarchy is
entirely a feature of the warehouse itself.  This is the pure Master Data
Management problem, where business entities are grouped in the warehouse
exclusively for the user's
convenience.



In the BoM or OH case,
however, the reporting hierarchy does have an independent existence.  In the
case of the BoM, it ties to engineering or product configuration.  In the case
of OH, it ties to some project structure or accounting structure.  However,
these hierarchical structures don't often exist in the same simple form that
they do in the warehouse bridge table.  And this leads to confusion on how we
maintain the bridge table.



In summary,
maintenance in the warehouse is limited to loading a historical snapshot of the
relationships in the SoR.  Maintenance happens in the SoR, and the results of
the maintenance are applied to the warehouse.  You must depend on an
SoR.



**Bridge Tables Maintenance.** 



There are several
varieties of Bridge Tables.  We'll address hierarchy, since it seems to lead to
the most confusion.  We'll touch on minidimension and outrigger tables, also,
since the same design pattern applies to
those.



The essential worry about
hierarchies stems from the fact that a hierarchy bridge table can have many more
rows than the  dimension it bridges.  Generally, it's an
*n* log(*n* )
kind of multiplication, where
log(*n* )
is an estimate of the depth of the
hierarchy.



As a practical matter,
moving one child to another parent is a single row change in the original data. 
However, the expansion in the bridge table means that
2*d* 
rows will change, where
*d*  is
the depth of the node in the hierarchy.  For some reason, this is
intimidating.



There are two
solutions:

-   Reload the entire bridge table with each
    source change.  This is easy to implement but slow.  If you use SCD change
    tracking, you'll have lots of nearly identical rows that are labeled with change
    dates because they were associated with a source node change.

-   Recompute just the changed parentage,
    updating only those rows of the bridge table.  This is not significantly more
    complex.  First, write a "find-all-parents" function, and apply this across
    every element of the source data to populate the bridge initially.  Then, you
    can use the "find-all-parents" function to compute just the relevant bridge
    table changes when a source node changes. 




A similar pattern is appropriate for
minidimensions and outriggers, which are based on subsets of a dimension.  The
lazy approach is to rebuild these each time the dimension changes.  A slightly
more efficient approach is to derive just the changed rows from the changes in
the dimension.



**Bottom Line.** 



Change doesn't happen in the
warehouse.  Change happens in the SoR.  The warehouse merely captures the effect
of that change.













