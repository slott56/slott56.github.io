Just for a moment, I though I'd found something SQLAlchemy doesn't do perfectly.
================================================================================

:date: 2007-05-18 17:40
:tags: #python,database
:slug: 2007_05_18-just_for_a_moment_i_though_id_found_something_sqlalchemy_doesnt_do_perfectly
:category: Python
:status: published







After having written a number of application-specific object-relational mappers, I have been on the prowl for an elegant, enduring solution.  I had started to come to grips with `Django <http://www.djangoproject.com/>`_ , and like much of the approach.  Django has a tiny infrastructure feature (the settings.py file) which made it unpleasant to separate the ORM from the rest of the framework.  (Not impossible, just fleetingly unpleasant.)



My first look at SQLAlchemy made it look over the top.  However, after the PyCon 2007 presentation, I realized that the layers were cleanly separated, and I could use the ORM without messing about in the SQL-in-Python-Notation layer.



Then, I figured out ("`PL/SQL vs. Java, Which One is Really Faster? <../C465799452/E20070322201220/index.html>`_ ") that stored procedures were slow.  Given that PL/SQL is slow, what else in the RDBMS world is slow?  How much SQL is too much SQL, when speed matters?  That answer is forthcoming -- I'm still fussing around with experiments.



Problem Child
-------------



The central issue started out as the all-too-common situation of **Disjoint Subentities**.  This is where a single table has distinct classes of entities.  The usual symptoms of this are indicators or NULL columns.  Often, both are used.  Sometimes, the indicator is omitted, and the pattern of NULLs has to be used to discriminate among the entity classes.



In this specific experiment, a single table has two subentities, each with different granularity.  One subentity has to be summed to match the grain of the other.  This gives us a union of two kinds of SQL queries: detailed and summary.



The detailed query, in SQLAlchemy, looks like this:

::

    qrySingle= select(
        [stuff.c.groupName,stuff.c.amount,literal(1)],
        and_(stuff.c.status=='unmatched',
            stuff.c.subtype=='single'))


In SQL, this is 

::

    SELECT "stuff"."groupName", "stuff".amount, ?
    FROM "stuff" WHERE "stuff".status = ? AND "stuff".subtype = ?


This is precisely the SQL that would be coded "by hand".  The literals (1, 'unmatched' and 'single') are bound into the SQL at run-time.



The summary query looks like this in SQLAlchemy.

::

    qryMulti= select(
         [stuff.c.groupName,func.sum(stuff.c.amount),literal(2)],
         and_(stuff.c.status=='unmatched',
                 stuff.c.subtype=='multi'),
         group_by=[stuff.c.groupName])


And produces the following SQL.


::

    SELECT "stuff"."groupName", sum("stuff".amount), ? 
    FROM "stuff" 
    WHERE "stuff".status = ? AND "stuff".subtype = ?
    GROUP BY "stuff"."groupName"


This is all very pleasant.  You can see that the literals (2, 'unmatched', 'multi') are bound in at run-time.  This technique often leads to a speed-up because the SQL statement can be reused by the RDBMS.  When coding by hand, this is easily overlooked.



Real World
----------



In the "real world", that is, the world of my clients, this kind of query is distressingly common.  And doing simulations and architectural recommendations is often made complex by having to cope with these kind of table designs.  



To work with this table, I needed a union, and (for a brief time) SQLAlchemy couldn't generate the correct SQL.



Here's my union in SQLAlchemy.

::

    invQry= union( qrySingle, qryMulti )



Here's the SQL which was generated.  Note that the GROUP-BY vanished.

::

    SELECT "stuff"."groupName", "stuff".amount, ? 
    FROM "stuff" 
    WHERE "stuff".status = ? AND "stuff".subtype = ?
    UNION SELECT "stuff"."groupName", sum("stuff".amount), ? 
    FROM "stuff" 
    WHERE "stuff".status = ? AND "stuff".subtype = ?



Very disappointing.  However, it's since been fixed.  And the amazing speed of that fix is more reason to love SQLAlchemy and the folks who support it.  Many thanks!



Now we can continue investigating which is faster: "Pure SQL" (i.e., complex stored procedures) or some programming language which uses SQL as necessary for persistence.




