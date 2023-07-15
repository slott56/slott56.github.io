Oracle Analytics and Functional Programming
===========================================

:date: 2010-08-30 07:28
:tags: #python,software design,functional programming,SQL
:slug: 2010_08_30-oracle_analytics_and_functional_programming
:category: Technologies
:status: published

As a hypothetical, I was asked about doing Oracle Analytic functions in
Python.

[**Sidebar: Politics**. The question came from a DBA in a C# shop.
That's why it's just hypothetical. Politically, they could never make
use of this information. In C# world, Functional Programming is often
scary and evil. It does exist -- obviously -- but it's called "Oracle
Analytics", which makes it acceptable. If functional programming was
called "functional programming" it would be unacceptable.]

[**Sidebar: SQL**. A big apples-to-oranges issue here is that the
Oracle analytic functions can be composed in subqueries to write
complex reporting queries. When you implement these functions in
Python, you appear to lose some SQL "features" for report-writing.
Actually, you move the SQL functional programming into Python
functional programming. Everyone complains when they have to give up
SQL. The true haterz say that using Python's functional programming
for database processing subverts the database and leads to moral
decay and the end of Western Civilization. Godwin's Law then
applies.]

Specific functions lifted up to me were RANK, FIRST, LAST, ROW_NUMBER
and DENSE_RANK. All of these are relatively simple functional
programming examples.

GROUP BY
--------

First -- and foremost -- SQL GROUP-BY can be slow. No one ever wants
to hear this. The true haterz will claim that it's supposed to be
faster and provide a bunch of non-reasons. Please benchmark.

Every database has to provide a GROUP-BY implementation that's
*perfectly* general; it has to sort. A procedural program can
sometimes do the same operation much more quickly because it doens't
have to be perfectly general; we can make different memory use
tradeoffs than the the database does.

For a fast GROUP-BY, use a hash map of some kind. Read all the rows
in the simplest, fastest array fetch possible. Here's how you can do
a blindingly fast SUM/GROUP-BY.

::

    from collections import defaultdict
    from decimal import Decimal

    groups = defaultdict( Decimal )
    for row in some_query_result_set:
        groups[row['key']] += groups[row['value']]

Writing code like this is based on the assumption that the number of
groups is small enough to fit into memory. That assumption allows us
to avoid a sort. The database can't make this assumption, and can't
easily use this kind of data structure.

Functional Programming
----------------------

The analytical functions are nice applications of a functional style
of programming. The ROW_NUMBER is already part of Python: it's the
internal enumerate function.

We can use enumerate to implement FIRST.

::

    def first( the_limit, some_query ):
        for number, row in enumerate( some_query ):
            if number >= the_limit:
                break
            yield row

This first function can be then used in another loop.

::

    for row in first( 100, some_query ):
        process( row )

LAST is more complex because there's no easy way to skip ahead.
Instead we have to buffer some rows.

::

    def last( the_limit, some_query ):
        queue = []
        for row in some_query:
            if len(queue) == the_limit:
                queue.pop( 0 )
                queue.append( row )
        for row in queue:
            yield row

This can be sped up a little by using an explicit iterator object and
breaking the ``for row in some_query`` loop into two phases to hoist
the nearly-constant if-statement.

These can be composed with Python's sorted function.

::

    for row in first( 10, sorted( some_query, key=lambda row: row['key']) ):
        process( row )

This is elegant, but may only draw a tie in a race against the
database. Python has the potential advantage of in-memory sorting.
Oracle, however, is clever enough to use in-memory sorting on small
sets of data, offsetting Python's advantage.

More Complex Functions
----------------------

The more complex functions of RANK and DENSE_RANK require two-phase
processing of rows. If we assume that we can fit the rows in memory,
this isn't very complex at all. Indeed, the rank function is just a
glorified order-by of a subset of the original data. However, it does
require a potentially slow sort step.

::

    ranked = enumerate ( sorted( some_query, key = lambda row: row['key'] ) )

Okay. So RANK isn't so complex after all. Functional programming
rocks.

DENSE_RANKED is confusing to me, but it look like the key phrase is
"Rows with equal values for the ranking criteria receive the same
rank." This means that the simple built-in enumerate isn't
appropriate, and we need a key-aware enumeration.

::

    def dense_rank( some_query, key ):
        query_iter= iter(some_query)
        rank= 1
        current = query_iter.next()
        yield rank, current
        for row in query_iter:
            if key(current) != key(row):
                rank += 1
                current= row
            yield rank, row

Composition
-----------

One of the strong suits of SQL is that it allows us to define a
functional-programming composition. Rather than write a lot of
looping, we specify a series of functions which are composed and
applied to our data.

For example, using FIRST and DENSE_RANK can be done like this.

::

    for row in first( 10, dense_rank( some_ordered_query, key=lambda row: row['key'] ) ):
        process( row )

This functional programming composition is -- BTW -- precisely what
SQL specifies. SQL describes incremental processing of each row
through a kind of pipeline that does map, filter, reduce and sort
algorithms on the row.

The ORDER-BY clause is an initial sort.

The WHERE clause is an initial filter. It may involve a mapping if
there are calculations in the various parts of the WHERE clause.

The GROUP-BY clause is a reduction into groups.

The HAVING clause is a second filter, applied to the groups. It may
involve a mapping if there are calculations in the various parts of
the HAVING clause.

Finally the SELECT clause is a mapping that does calculations on the
resulting collection of rows.

The analytic functions, like subqueries, are simple complex mapping
operations that involve other query pipelines.



-----

You could use itertools.islice() to implement firs...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-08-30 09:24:04.333000-04:00

You could use itertools.islice() to implement first().
A collections.deque would make last() less inefficient.
In theory you could implement first(10, sorted(...)) more efficiently by
not sorting items past position 10 (e.g. skip quicksort's recursive
calls if they wouldn't touch the first 10 items). I'm not sure if
Python's stdlib has an algorithm for this.


Implementing a similar set of compose-able SQL-lik...
-----------------------------------------------------

Bryan Cole<noreply@blogger.com>

2010-08-30 12:28:28.334000-04:00

Implementing a similar set of compose-able SQL-like sorting and grouping
functions for operating on large datasets led me to create "sendtools":
see http://pypi.python.org/pypi/sendtools
(appologies for the plug). How does this compare?





