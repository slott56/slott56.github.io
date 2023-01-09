Essay 10.1 - When A Column Is Not A Column
==========================================

:date: 2005-09-14 10:00
:tags: architecture,design
:slug: 2005_09_14-essay_101_when_a_column_is_not_a_column
:category: Architecture & Design
:status: published





Recently, I've seen a number of data structures
that evolved from 2-dimensional data models.  They devolved into a morass of
complications because they started out violating First Normal Form rules.  Once
that rule has been broken, the door is shut on the benefits of the relational
model of data.



For another viewpoint on
this, see `How many parents do you have? <http://kontrawize.blogs.com/kontrawize/2005/09/how_many_parent.html>`_   It provides
another example of
multi-dimensionality.



How does this
happen?



Consider subcontract
management.  Each contact has a number of milestone events and status changes
that get recorded.  For the first few contractors, a spreadsheet lists the
contractor going down the page, and the events across the
page.



..  csv-table::

    " ","Events"
    "Contract","This Form","That Form","A Meeting","A Report"
    "Vendor 1","3/19","4/18","planned","(null)"
    "Vendor B","3/21","4/5","4/12","planned"

    






Then complications set in.  First, there
were contract-specific events.  Then there were more contracts with
contract-specific events.  Eventually, the 255 column limit was reached in their
database.



Clearly,
*contract* 
and
*event* 
are two dimensions of a common fact.  The relational table has a row for each
cell in the original spreadsheet.



..  csv-table::

    "Contract","Event","Status"
    "Vendor 1","This Form","3/18"
    "Vendor 1","That Form","4/18"
    "Vendor 1","A Meeting","planned"
    "Vendor B","This Form","3/21"
    "Vendor B","That Form","4/5"
    "Vendor B","A Meeting","4/12"
    "Vendor B","A Report","planned"

    








However, this row-at-a time structure
is inconvenient for seeing a summarized contract-by-contract report.  The
original spreadsheet did this properly, but the normalized table requires extra
processing to denormalize it for presentation purposes.  This denormalization is
often done via a complex view that places specific values for event into
specific columns.  In pure SQL, it looks like this, and produces a result that
is hard to read.


::

    select contract,
    status, null, null, null
    from table
    where event = 'This Form'

    union

    select
    contract, null, status, null, null
    from table where event = 'That Form'

    union

    select
    contract, null, null, status, null
    ...



Most
SQL's have extensions to help denormalize the columns of the report from rows of
individual data elements.

::

    select
    contract, 
    (select status from table col 
         where col.contract=row.contract 
         and event='This Form'), 
    (select status
        from table col 
        where col.contract=row.contract 
        and event='That Form'),
    ...
    from
    table row



You're better off creating an
extract file and loading MS-Excel Pivot Tables from the normalized
representation and letting people slice and dice on their desktop.  The pure SQL
approach to denormalization makes the problem appear more complex than it really
is.








