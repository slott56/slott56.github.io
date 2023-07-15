Python and the Star Schema
==========================

:date: 2008-05-09 10:37
:tags: architecture,database design,data structure,algorithm,python,pycon
:slug: 2008_05_09-python_and_the_star_schema
:category: Architecture & Design
:status: published







The star schema represents data as a table of facts (measurable values) that are associated with the various dimensions of the fact.  Common dimensions include time, geography, organization, product and the like.  I'm working with some folks whose facts are a bunch of medical test results, and the dimensions are patient, date, and a facility in which the tests were performed.



I got an email with the following situation: "a client who is processing gigs of incoming fact data each day and they use a host of C/C++, Perl, mainframe and other tools for their incoming fact processing and I've seriously considered pushing Python in their organization.". 



Here are my thoughts on using Python for data warehousing when you've got Gb of data daily.



Small Dimensions
----------------



The pure Python approach only works when your dimension will comfortably fit into memory -- not a terribly big problem with *most*  dimensions.




Specifically, it doesn't work well for those dimensions which are so huge that the dimensional model becomes a snowflake instead of a simple star.  When dealing with a large number of individuals (public utilities, banks, medical management, etc.) the "customer" (or "patient") dimension gets too big to fit into memory.  Special bridge-table techniques must be used.  I don't think Python would be perfect for this, since this involves slogging through a lot of data one record at a time.  




However, Python is considerably faster than PL/SQL.  I don't know how it compares with Perl.  Any programming language will be faster than any SQL procedure, because there's no RDBMS overhead.







For all small dimensions.  Load the dimension values from the RDBMS into a dict with a single query.  Read all source data records (ideally from a flat file); conform the dimension, tracking changes; write a result record with the dimension FK information to a flat file.  




Iterate through the dimension dictionary and persist the dimension changes.  The details vary with the Slowly Changing Dimension (SCD) rules you're using.




The conformance algorithm is is essentially the following:




::

    row= Dimension(...)
    ident= ( row.field, row.field, row.field, ... )
    dimension.setdefault( ident, row )





In some cases (like the Django ORM) this is called the get-or-create query.





The Dimension Bus
------------------




For BIG dimensions, I think you still have to implement the "dimension bus" outlined in The Data Warehouse Toolkit.  To do this in Python, you should probably design things to look something like the following.





For any big dimensions, use an external sort-merge utility.  Seriously.  They're way fast for data sets too large to fit into memory.  Use CSV format files and the resulting program is very tidy.   The outline is as follows:





First, sort the source data file into order by the identifying fields of the big dimension (customer number, patient number, whatever).  





Second, query the big dimension into a data file and sort it into the same order as the source file.  (Using the SQL ORDER BY may be slower than an external sort; only measurements can tell which is faster.)   





Third, do a "match merge" to locate the differences between the dimension and the source.  Don't use a utility like diff, it's too slow.  This is a simple key matching between two files.  The match-merge loop looks something like this.






::

    src= sourceFile.next()
    dim= dimensionFile.next()
    try:
       while True:
          src_key = ( src['field'], src['field'], ... )
          dim_key= ( dim['field'], dim['field'], ... )
          if src_key < dim_key:
             # missing some dimension values
             update_dimension( src )
             src= sourceFile.next()
          elif dim_key < src_key:
             # extra dimension values
             dim= dimensionFile.next()
          else: # src and dim keys match
             # check non-key attributes for dimension change.
             src= sourceFile.next()
    except StopIteration, e:
        # if source is at end-of-file, that's good, we're done.
        # if dim is at end of file, all remaining src rows are dimension updates.
        for src in sourceFile:
            update_dimension( src )






At the end of this pass, you'll accumulate a file of customer dimension adds and changes, which is then persisted into the actual customer dimension in the database.  This pass will also write new source records with the customer FK.  You can also handle demographic or bridge tables at this time, too.




Fact Loading
------------





The first step in DW loading is dimensional conformance.  With a little cleverness the above processing can all be done in parallel, hogging a lot of CPU time.  To do this in parallel, each conformance algorithm forms part of a large OS-level pipeline.  The source file must be reformatted to leave empty columns for each dimension's FK reference.  Each conformance process reads in the source file and writes out the same format file with one dimension FK filled in.  If all of these conformance algorithms form a simple OS pipe, they all run in parallel.  It looks something like this.





::

    src2cvs source | conform1 | conform2 | conform3 | load






At the end, you use the RDBMS's bulk loader (or write your own in Python, it's easy) to pick the actual fact values and the dimension FK's out of the source records that are fully populated with all dimension FK's and load these into the fact table.





I've written conformance processing in Java (which is faster than Python) and had to give up on SQL-based conformance for large dimensions.  Instead, we did the above flat-file algorithm to merge large dimensions.  The killer isn't the language speed, it's the RDBMS overheads.  Once you're out of the database, things blaze.  Indeed, products like the `syncsort <http://www.syncsort.com/>`_  data sort can do portions of the dimension conformance at amazing speeds for large datasets.





Hand Wringing
--------------





"But," the hand-wringers say, "aren't you defeating the value of the RDBMS by working outside it?"   The answer is NO.  We're not doing incremental, transactional processing here.  There aren't multiple update transactions in a warehouse.  There are queries and there are bulk loads.  Doing the prep-work for a bulk load outside the database is simply more efficient.  We don't need locks, rollback segments, memory management, threading, concurrency, ACID rules or anything.  We just need to match-merge the large dimension and the incoming facts.




