Physical Database Design Questions -- Some Inner Mysteries
==========================================================

:date: 2008-03-01 19:35
:tags: architecture,database design,data structure,algorithm
:slug: 2008_03_01-physical_database_design_questions_some_inner_mysteries
:category: Architecture & Design
:status: published







I have to say this first -- just because ERwin calls it "physical" that doesn't mean anything.  ERwin uses "physical" model to mean "product-specific logical" model.  They use "logical" to mean "product-independent logical" model.



ERwin doesn't do *physical*  modeling.  Not even a little bit.  The physical layer of a relational database occurs down at the file system level.  Codd's "Rule 8" (Physical Data Independence) says that the things we're designing in ERwin (and similar tools) are the things our application depends on; the things we're **not**  designing, therefore, must be physical.



The physical implementations underlying Oracle, Postgres, DB2, MySQL, SQL/Server (and even SQLite) are all different.  These physical models have *nothing*  to do with the SQL standard; that's the central tenet of Codd's Rule 8.  These implementations are so different as to defy a standardized modeling tool.  All you can ever use for physical modeling is a generic UML tool.



Compression
-----------



I was asked about the value of compression.  Years ago, we depended on the clever compression schemes of `Oracle RDB <http://www.oracle.com/technology/products/rdb/index.html>`_ .  Oracle 10g has table compression.  DB2 has tablespace compression.



This is a physical design technique.  It's invisible to the SQL application programmer.  It can speed up certain types of queries.



The final trade-offs can only be determined empirically.  You have to process real data through a reasonably complete application to get a benchmark.  Then you rework your database to compress things and see if it runs faster where you need it to run faster, and hasn't gotten any worse elsewhere.



I was shocked that someone would ask about the value of compression.  Anything that involves a table scan will be faster with compressed data.  Fewer physical reads means faster.  It's that simple.  (Yes, there's a CPU cost, the impact depends on the actual mix of updates, inserts and selects.)



I tried to probe the DBA to see precisely what the confusion was, but didn't get much of an answer.  As near as I can tell, there are some restrictions imposed by Oracle on how one can alter a compressed table; this had somehow confounded things.  As a practical matter, the restrictions imposed by the RDBMS don't matter much.  Many database structural changes are the kind of thing that can't be done with ALTER; you have to clone the old table, drop and rebuild it, and then reload the new table(s) from the clone.



Administration aside, compression is simple.  For data warehouses, it helps a lot.  You have to measure the impact across all use cases.



Partitioning
------------



I was asked about partitioning.   Oracle has some performance tuning guidelines which were bothersome or confusing or both.  



Note that there are several dimensions to partitioning.  One can do "vertical" partitioning where a table is split into two portions that have a mandatory 1:1 relationship.  This can be done to separate data elements, potentially improving concurrency.  This is a logical design technique, since an application programmer will have to know which partition has the appropriate columns.



A "horizontal" partition splits a table into sections that can be allocated to multiple physical tablespaces.  This is a physical design technique, since it's invisible to the SQL programmer.  Partitions can be defined around some key or can be more-or-less arbitrary.



The idea is to spread the I/O load around among multiple devices, improving concurrency.  This isn't like compression, where we do fewer reads.  However, doing the reads concurrently can improve the elapsed time to query data.



Note that storage arrays often do this for us, seamlessly, silently and outside the database.  If we define the right kind of striped logical volume, then the file system itself will spread the file blocks across multiple physical locations.  The kind of sequential read that implements a table scan will work with multiple, concurrent physical reads.



If the file system can't do this, we can have the RDBMS do it.  Having it done in both tiers of the architecture is actually bad because one tier can undo the other tier's performance optimizations.



Tuning
-------



Oracle says that -- if you can -- keep your partition sizes approximately equal.  This is silly advice, since it can be very hard to implement.  Your data has the distribution it has.  Further, the equal-sized partition rule is only to get "optimal" performance.  If all partitions are about the same size, they can all be scanned in about the same amount of time.



If one partition is bigger, it will be slower.  This may be sub-optimal, but it still beats the performance of an unpartitioned table.



This "balancing" issue becomes a kind of fetish for DBA's.  They start to do sophisticated statistical summaries and analysis of the various keys trying to locate a way to even out the partition sizes consistent with the application design and architecture.



This can become a burdensome load of hooey.  Use partitions that make sense.  For those rare, ultra-high-performance applications, use a hash partition and be happy knowing it's faster than unpartitioned data.  Don't fetishize about keeping the partitions equal.



VSAM Files
----------



Yes, `VSAM <http://publib.boulder.ibm.com/infocenter/pdthelp/v1r1/index.jsp?topic=/com.ibm.entcobol4.doc/cpvsm04.htm>`_  flat-files are still in use.  All VSAM I/O (in spite of the V meaning "Virtual") is essentially physical I/O.  VSAM files can be read, written, and searched using ultra-complex algorithms.  Algorithms that aren't remotely compatible with SQL's simplified view of the world.  I know, I wrote some.



Recently, we've spent a lot of time talking about replacing some VSAM files with a proper relational database.  The fantasy is that we can neatly excise this physical I/O and replace it with SQL statements, leaving the rest of the program more-or-less intact.  Clearly, they haven't spent enough time trying to reverse engineer COBOL programs. 



COBOL programs that process VSAM files rarely have a structure that involves an algorithm like a simple cursor fetch loop or SQL update statement.  Instead, these programs have obscure structures that depend on numerous details of the file organization.



Unifying Theme
--------------



Here's the unifying theme: a few programmers have gotten so used to SQL that they think it's low-level I/O.  They've forgotten the underlying physical implementation.



They've lost sight of the physical reads and how reducing the physical reads makes table scans go faster.



They've fetishized subtle load-balancing issues, forgetting that any parallel I/O is better than no parallel I/O.



They think that all programs have elegant SQL-like fetch loops, updates or inserts.  Legacy COBOL programs can be peculiarly obscure.  It is often simpler to dispose of the old VSAM program rather than rewrite it to use SQL.





