NoSQL Befuddlement: DML and Persistence
=======================================

:date: 2013-07-18 08:00
:tags: #python,persistence,architecture,noSQL,Apache,csv,RDBMS,SQL
:slug: 2013_07_18-nosql_befuddlement_dml_and_persistence
:category: Technologies
:status: published


It may be helpful to look back at '`How Managers Say
"No" <{filename}/blog/2013/07/2013_07_16-how_managers_say_no_the_rdbms_hegemony_example.rst>`__'
which is about breaking the RDBMS Hegemony.

I got an email in which the simple concepts of "data manipulation" and
"persistence" had become entangled with SQL DML to a degree that the
conversation failed to make sense to me.

They had been studying `Pandas <http://pandas.pydata.org/>`__ and had
started to realize that the RDBMS and SQL were not an essential
feature of all data processing software.

I'll repeat that with some emphasis to show what I found alarming.

They had **started** to realize that the RDBMS and SQL were not an
**essential** feature of all data processing.


**Started** to realize.

They were so entrenched in RDBMS thinking that the very idea of
persistent data outside the RDBMS was novel to them.

They asked me about extending their growing realization to encompass
other SQL DML operations: INSERT, UPDATE and DELETE. Clearly, these
four verbs were all the data manipulation they could conceive of.

This request meant several things, all of which are unnerving.

#.  They were sure—absolutely sure—that SQL DML was **essential** for all
    persistent data. They couldn't consider read-only data? After all, a
    tool like Pandas is clearly focused on read-only processing. What
    part of that was confusing to them?

#.  They couldn't discuss persistence outside the narrow framework of SQL
    DML. It appears that they had forgotten about the file system
    entirely.

#.  They conflated data manipulation and persistence, seeing them as one
    thing.

After some back-and-forth it appeared that they were looking for
something so strange that I was unable to proceed. We'll turn to
this, below.




**Persistence and Manipulation**

We have lots of persistent data and lots of manipulation. Lots. So
many that it's hard to understand what they were asking for.

Here's some places to start looking for hints on persistence.

http://docs.python.org/3/library/persistence.html

http://docs.python.org/3/library/archiving.html

http://docs.python.org/3/library/fileformats.html

http://docs.python.org/3/library/netdata.html

http://docs.python.org/3/library/markup.html

http://docs.python.org/3/library/mm.html

This list might provide some utterly random hints as to how persistent
data is processed outside of the narrow confines of the RDBMS.

For manipulation... Well... Almost the entire Python library is about
data manipulation. Everything except
`itertools <http://docs.python.org/3.3/library/itertools.html#module-itertools>`__
is about stateful objects and how to change state ("manipulate the
data.")

Since the above lists are random, I asked them for any hint as to what
their proper use cases might be. It's very difficult to provide
generic hand-waving answers to questions about concepts as fundamental
as state and persistence. State and persistence pervade all of data
processing. Failure to grasp the idea of persistence outside the
database almost seems like a failure to grasp persistence in the first
place.

**The Crazy Request**

Their original request was—to me—incomprehensible. As fair as I can
tell, they appeared to want the following.

I'm guessing they were hoping for some kind of matrix showing how
`DML <http://en.wikipedia.org/wiki/Data_manipulation_language>`__ or
`CRUD <http://en.wikipedia.org/wiki/Create,_read,_update_and_delete>`__
mapped to other non-RDBMS persistence libraries.

So, it would be something like this.

..  csv-table::

    SQL,OS,Pandas,JSON,CSV
    CREATE,file(),some pandas request,json.dump(),csv.writer()
    INSERT,file.write(),depends on the requirements,could be anything,csv.writerow()
    UPDATE,file.seek(); file.write(),doesn't make sense,not something that generalizes well,depends on the requirements
    DELETE,file.seek(); file.write(),inappropriate for analysis,depends on the requirements,hard to make this up without more details
    APPEND -- not part of DML,file.write(),depends on requirements,could be anything,csv.writerow()



The point here is that data manipulation, state and persistence is
**intimately** tied to the application's requirements and processing.

All of which presumes you are persisting stateful objects. It is
entirely possible that you're persisting immutable objects, and state
change comes from appending new relationships, not changing any
objects.

The SQL reductionist view isn't really all that helpful. Indeed, it
appears to have been deeply misleading.

**The Log File**

Here's an example that seems to completely violate the spirit of their
request. This is ordinary processing that doesn't fit the SQL DML mold
very well at all.

Let's look at log file processing.

#. Logs can be persisted as simple files in simple directories. Compressed archives are even better than simple files.

#. For DML, a log file is append-only. There is no insert, update or delete.

#. For retrieval, a query-like algorithm can be elegantly simple.


Without any brain-cramping, one can create simple map-reduce style
processing for log files. See "`Map Reduce -- How Cool is
that? <{filename}/blog/2010/01/2010_01_10-map_reduce_how_cool_is_that.rst>`__"
for a snippet of Python code that turns each row of an Apache log file
into a record-like tuple. It also shows how to scan multiple files and
directories in simple map-reduce style loops.

Interestingly, we would probably loose considerable performance if we
tried to load a log file into an RDBMS table. Why? The RDBMS file for
a table that represents a given log file is much, much larger than the
original file. Reading a log file directly involves far fewer physical
I/O operations than the table.

Here's something that I can't answer for them without digging into
their requirements.

A "filter" could be considered as a DELETE.  Or a DELETE can be used
to implement a filter. Indeed, the SQL DELETE may work by changing a
row's status, meaning the the SQL DELETE operation is actually a
filter that rejects deleted records from future queries.

Which is it? Filter or Delete? This little conundrum seems to violate
the spirit of their request, also.

**Python Code**

Here's an example of using persistence to filter the "raw" log files.
We keep the relevant events and write these in a more regular,
easier-to-parse format. Or, perhaps, we delete the irrelevant records.
In this case, we'll use CSV file (with quotes and commas) to speed up
future parsing.

We might have something like this:

::

    log_row_pat= re.compile(
        r'(\d+\.\d+\.\d+\.\d+) (\S+?) (\S+?) (\[[^\]]+?]) ("[^"]*?") (\S+?) (\S+?) ("[^"]*?") ("[^"]*?")'
    )

    def log_reader( row_source ):
        for row in row_source:
             m= log_row_pat.match( row )
             if m is not None:
                 yield m.groups()

    def some_filter( source ):
        for row in source:
            if some_condition(row):
                yield row

    with open( subset_file, "w" ) as target:
        with open( source_file ) as source:
            rdr= log_reader( source )
            wtr= csv.writer( target )
            wtr.writerows( some_filter( rdr ) )

This is a amazingly fast and very simple. It uses minimal memory and
results in a subset file that can be used for further analysis.

Is the filter operation really a DELETE?

This should not be new; it should not even be interesting.

As far as I can tell, they were asking me to show them how is data
processing can be done outside a relational database. This seems
obvious beyond repeating. Obvious to the point where it's hard to
imagine what knowledge gap needs to be filled.

**Conclusion**

Persistence is not a thing you haphazardly laminate onto an
application as an afterthought.

Data Manipulation is not a reductionist thing that has exactly four
verbs and no more.

Persistence—like security, auditability, testability,
maintainability—and all the quality attributes—is not a checklist item
that you install or decline.

Without tangible, specific use cases, it's impossible to engage in
general hand-waving about data manipulation and persistence. The
answers don't generalize well and depend in a very specific way on the
nature of the problem and the use cases.





