Data Warehousing and SQL -- Tread Carefully
===========================================

:date: 2011-09-01 08:00
:tags: data warehouse,#python,performance,star-schema
:slug: 2011_09_01-data_warehousing_and_sql_tread_carefully
:category: Technologies
:status: published

"Are you implying that a scalable Data Warehouse solution could be
implemented using Python and serialised files?"

Not "implying".  I'm trying to state it as clearly as I can.
A scalable data warehouse solution involves a lot of flat file
processing.

ETL, for example, is mostly a flat-file pipeline.  It starts with source
application extract (to create a flat file) and proceeds through a
number of transformation steps to filter, cleanse, recode, conform
dimensions, and eventually relate facts to dimensions.  This is
generally very, very fast when done with simple flat files and
considerably slower when done with a database.

This is the "Data Warehouse Bus" that Kimball describes in chapter 9 of
*The Data Warehouse Lifecycle Toolkit*.

Ultimately, the cleansed, conformed files will lay around in a "staging
area" forever.  When a datamart is built, then a subset of these files
can be (rapidly) loaded into an RDBMS for query processing.

Doing this in Python is no different from doing it in Java, C++ or
(for that matter) `Syncsort <http://www.syncsort.com/>`__.  Yes.
You can build a data warehouse using processing steps written
around Syncsort and be quite successful.

The important part of this is to recognize the following.

When trying to do data warehouse flat-file processing in C++ (or
Java) you have the ongoing schema maintenance issue.  The source
data changes.  You must tweak the schema mapping from source to
warehouse.  You can encode this schema mapping as property files
or some such, or you can simply use an interpreted language like
Python and encode the mappings as Python code.

The "Data Warehouse Bus" is a lot of applications that are
trivially written as simple, parallel, multi-processing, small,
read-match-write programs.  Forget threads.  Simply use
heavy-weight, OS-level processes so that you can maximize the I/O
bandwidth.  (Remember: **when one thread makes an I/O request, the
entire process waits**; an I/O-bound application isn't helped by
multi-threading.)

::

    with open('some_data','rb') as source:
        rdr= csv.DictReader( source )
        wtr= csv.DictWriter( sys.stdout, some_schema )
        for row in rdr:
          if exclude( row ): continue
          clean = cleanse( row )
          wtr.writerow( clean )

This example writes to stdout so that it can be connected in a
pipeline with other steps in the processing.  Programs running in
an OS pipeline run concurrently.  They tie up all the cores
available without any real programming effort other than
decomposing the problem into discrete parallel steps that apply to
each row being touched.

Simple file processing is much, much faster than SQL processing.
Why?  No overheads for locking or buffer pooling or rollback
segments, or logging, or after-image journaling or deadlock
detection, etc.

Note that a data warehouse database has no need for sophisticated
locking.  All of the "updates" are bulk loads.  80% of the
activity is "insert".  With some Slowly Changing Dimension (SCD)
operations there is a trivial status-change update, but this can
be handled with a single database-wide lock during insert.

The primary reason for using SQL is to handle "SELECT something
... GROUP BY" queries.  SQL does this reasonably well most of the
time.  Python does it pretty well, also.

::

    sum_col1 = defaultdict( float )
    count_group = defaultdict( int )
    with connection.cursor() as c:
      c.execute( "SELECT COL1, GROUP FROM..." )
      for row in c.fetchall():
          sum_col1[row.group] += col1
          count_group[row.group] += 1
    print( sum_col1, count_group )

That's clearly wordier than SQL.  But not *much* wordier.  The
SELECT statement embedded in the Python is simpler because it
omits the GROUP BY clause.  Since it's simpler, it's more likely
to benefit from being reused in the RDBMS.

The Python may actually run *faster* than a pure SQL query because
it avoids the (potentially expensive) RDBMS sort step.  The Python
defaultdict (or Java HashMap) is how we avoid sorting.  If we need
to present the keys in some kind of user-friendly order, we have
limited the sort to just the distinct key values, not the entire
join result.

Because of the huge cost of group by, there are two hack-arounds.
One is "materialized views".  The idea is that a group-by view is
updated when the base tables are updated to avoid the painful cost
of sorting at query time.  In addition to this, there are
reporting tools which are "aggregate aware".  They can leverage
the materialized view to avoid the sort.

How about we avoid all the conceptual overhead of materialized
views and aggregate aware reporting. Instead we can write simple
Python procedures that do the processing we want.

Bottom Line
-----------

Data Warehouse does not imply SQL.  Indeed, it doesn't even
suggest SQL except for datamart processing of flexible ad-hoc
queries where there's enough horsepower to endure all the sorting.



-----

"Remember: when one thread makes an I/O reque...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-09-01 13:17:16.823000-04:00

"Remember: when one thread makes an I/O request, the entire process
waits; an I/O-bound application isn't helped by multi-threading."
Um, what? That's not true at all. In fact, that's the number one reason
to use multi-threading.


Indeed, the process-vs-thread decision for CPython...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2011-09-01 19:51:19.242000-04:00

Indeed, the process-vs-thread decision for CPython is exactly the
reverse of what you describe here. Due to the Global Interpreter Lock,
threads are great for I/O-bound applications (since I/O operations
release the GIL, allowing other threads to run), but lousy for CPU-bound
processes on multi-core machines (since the GIL and memory
synchronisation issues will effectively limit each process to one
processor).

In terms of the wider topic of the article, I definitely agreed that
manipulating files directly in the filesystem is often a preferable
alternative to letting the database handle things. Filesystems are
primarily designed for bulk storage, databases are primarily designed
for record keeping (although the lines obviously get blurred in both
directions in practice).

However, it's also important to be careful to avoid premature
optimisation. For cases like the sort example at the end, I'd start with
the version that let the database handle everything, and only pull logic
out into the application code if it offered a demonstrable improvement
in performance. Otherwise it's easy to fall into the trap of trying to
solve problems yourself that RDBMS authors have already handled for you.


While I agree that DW != SQL and your analysis of ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-09-06 18:27:33.788000-04:00

While I agree that DW != SQL and your analysis of using Python is very
interesting; I have to wonder if you're creating a custom tool here that
could be done better by other tools. What about MDX as it is implemented
in MS Analysis Services, Hyperion, and other products. This language
(MDX) is built from the ground up for the type of cube queries you
outline like the "Group By" SQL statement.


When visiting blogs, i usually discover a very goo...
-----------------------------------------------------

mariyamkhan<noreply@blogger.com>

2021-09-29 13:50:31.651000-04:00

When visiting blogs, i usually discover a very good content like yours
`see here <https://www.linkedin.com/in/scott-korn-62546a19/>`__





