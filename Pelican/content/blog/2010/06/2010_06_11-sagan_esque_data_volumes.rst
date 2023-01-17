Sagan-esque Data Volumes
========================

:date: 2010-06-11 08:00
:tags: design,architecture
:slug: 2010_06_11-sagan_esque_data_volumes
:category: Technologies
:status: published

About once a week a question shows up on `Stack
Overflow <http://stackoverflow.com/>`__ that involves loading a database
with truly epic volumes of data. For example "billions of rows in a
single table for a month".

Billions of rows per month is a minimum insert rate of 385 row *per
second*.

Also, this quote is killer. "data for the past 5 years". That's a
minimum of 60 billion rows.

This is a really, really poor use of an RDBMS. This requires some
kind of well-planned hierarchy of storage and analytic solutions.
Load and Query can't work.

Goal
----

The question is "What's the Goal"? Some of the Stack Overflow
questions lack essential use cases, making it impossible to determine
what these folks are trying to do.

What's certain, however, is that no human being is going to do an
ad-hoc SQL query on 60 billion rows of anything. Analysis of data
volumes like that will involve fairly narrow and specific queries.

Analysis of a subset may involve ad-hoc SQL queries. But the whole
data set isn't really useful -- as a whole. It's useful when sliced
and diced.

Heresy
------

At this point, many DBA's pronounce me Heretic and Apostate. Anyone
who suggests that a SQL database is (a) slow, and (b) biased toward
ad-hoc queries must have fallen from the true path.

First, SQL is slow. A flat file is always faster. Try it. For
reasonably well-structured data -- arriving at a sustained rate of
385 rows per second -- only a concurrent pipeline of flat-file
processing can keep up. The dimensional conformance and fact table
preparation has to be done in flat files. With no database loads
involved at all.

Second, SQL is for ad-hoc processing. Most applications that have
embedded SQL don't involve queries that the user types at the command
line. However, most applications use SQL specifically to divorce the
application from the physical data model. The idea is that SQL offers
an ad-hoc scale of flexibility in exchange for glacial processing
speed.

Acquisition
-----------

The first step is to acquire the data in some storage that will
handle 60 billion rows of data. Even if the rows are small, this is a
big pile of disk. Super-large files are a mistake, so it means a
complex directory tree of several smaller files.

Ideally, some "sharding" algorithm is used so that perhaps a dozen
files are in use concurrently, each getting 30 or so rows per second.
This is a more sensible processing pace, achievable by heavily loaded
devices.

Data acquisition is -- itself -- a highly parallelized operation. The
rows must be immediately separated into pipelines. Each pipeline must
be a multi-processing sequence of dimension conformance operations.
At the end of each pipeline, a standardized row with all of the
dimension FK's emerges and is appended to a file. Some flushing and
periodic close-reopen operations will probably be reliable enough.

The dimension values can be built into a database. The facts,
however, have to reside in flat files.

Analysis
--------

In the unlikely case that someone thinks they want to analyze all 60
billion rows, there are two things to be done. First, talk them out
of it. Second, write special-purpose flat-file analyzers which do
concurrent map-reduce operations on all of the various source files.

In the more likely use cases, folks want a subset of the data. In
this case, there's a three-part process.

#.  Grab the relevant dimensions. They're in a master-dimension
    database, being constantly updated by the ongoing loads.

#.  Filter the facts. This is a massively parallel map-reduce process
    that extracts the relevant rows from the fact files and creates a
    "data mart" fact file.

#.  Load a datamart. This has dimensions and facts. The facts may have
    to be summarized to create appropriate sums and counts.

This subset datamart can be turned over to people for further
slicing and dicing or whatever it is that they do with 60 billion
rows of data.



-----

Lustre (or similar file-systems) can solve many of...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-07-04 16:34:04.629000-04:00

Lustre (or similar file-systems) can solve many of the performance
problems with commonplace hardware (of course some thinking is needed as
ususal).





