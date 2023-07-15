Normalization Experiment Protocol (revised)
===========================================

:date: 2005-12-01 11:24
:tags: architecture,software design,data structure,algorithm,database design
:slug: 2005_12_01-normalization_experiment_protocol_revised
:category: Architecture & Design
:status: published





The open question is "What is the cost of
fragmentation?"



The cost has some
absolute components and some relative components.  Since fragmentation is
difficult to avoid except through grotesque over-allocation of space, the issue
is to control fragmentation through normalization.  A more important pair of
questions, then, are these:



1.  What
    are the background costs of fragmented
    data?



2.  What are the relative merits
    of normalizing to control
    fragmentation?



The absolute costs are
relatively easy to identify: they are the costs of defragmenting.  These are the
downtime to defragment, and risk of failure in this processing which adds
complexity but does not create
value.



The relative costs can be
measured through a comparison between three designs: denormalized, partially
normalized and fully normalized.

-   The denormalized design is the Multiple
    Entity SubSpecies (MESS) or Uni-table.  Suitable for a number of data warehouse
    purposes, but a poor choice for transactional applications.

-   The partially normalized design
    partitions columns into "core" and "extension" using a rough estimation of the
    relative frequency of update.  Things rarely or never updated are part of the
    core, and will be quite compact.  Things updated -- in particular, things with
    an initial value of NULL -- go in the extension.  The extension is expected to
    fragment, but the fragmentation will be isolated and (hopefully) under some
    control.

-   The fully normalized design partitions
    columns into the dimension and a fact table that records individual events
    separately.  The idea is that events accrete.  Replacing a NULL with event
    information creates a sparse and fragmented table.  This is the CREEP - a
    Continuously Re-Evolving Entity Pattern, where growth is part of the design. 
    Inserts make more sense than updates for evolving
    entities.



Here is the denormalized MESS
design.  The ev's are "Events" which are filled in by updates, leading to
fragmentation.  The business processing makes ev1 mandatory, and the other
events may, or may not happen.


::
   
    CREATE TABLE MESS(
        key    VARCHAR(20),
        ev1text    VARCHAR(100),
        ev1date    TIMESTAMP,
        ev2text    VARCHAR(100),
        ev2date    TIMESTAMP,
        ev3text    VARCHAR(100),
        ev3date    TIMESTAMP );


Here's a normalized design
which controls fragmentation by isolating ev2 and ev3 event data into a separate
table.  The M2 table can be sparse and can
fragment.

::

    CREATE TABLE M1C(
        key VARCHAR(20),
        ev1text VARCHAR(100),
        ev1date TIMESTAMP );

    CREATE TABLE M1X(
        key VARCHAR(20),
        ev2text VARCHAR(100),
        ev2date TIMESTAMP,
        ev3text VARCHAR(100),
        ev3date TIMESTAMP );

    CREATE UNIQUE INDEX M1C_X1 ON M1C( key );

    CREATE UNIQUE INDEX M1X_X1 ON M1X( key );



The most interesting design is the following.  This uses inserts instead of updates
to fold in the additional data.

::

  
    CREATE TABLE M2C(
        key VARCHAR(20) );

    CREATE TABLE M2E(
        key VARCHAR(20),
        evt NUMBER,
        evtext VARCHAR(100),
        evdate TIMESTAMP );
        
    CREATE UNIQUE INDEX M2C_X1 ON M2C( key );

    CREATE INDEX M2E_X1 ON M2E( key );











