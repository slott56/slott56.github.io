Data Structures in Python and SQL
=================================

:date: 2009-05-17 19:54
:tags: #python,object-oriented design,SQL
:slug: 2009_05_17-data_structures_in_python_and_sql
:category: Technologies
:status: published

This is -- partially -- about the `object-relational impedance
mismatch <http://en.wikipedia.org/wiki/Object-Relational_impedance_mismatch>`__.

But it's also about the parallel concepts between objects and
relations.  We'll use Python as our object model.


First, the obvious.


A SQL table is a list of rows.  A row is a dictionary that maps a
column name to a column value.  A SQL table has a defined type for a
named column; Python doesn't pre-define the type of each column.


Some folks like to think of a table as a rigidly-defined class, which
is partly true.  It can be rigidly-defined.  However, the extra
meta-data doesn't help much.


Indexing
--------

As a practical matter, most databases go beyond the minimalist
definition of a relationship as a collection of rows.  An index
extends the structure in one of two ways.


A unique-key index transforms the SQL table into a dictionary that
maps a key to a row.


::

      class UniqueKeyTable( object ):
          def __init__( self ):
              self.rows = {}
          def insert( self, aRow ):
              self.rows[aRow.key()]= [aRow]


The non-unique key index transforms the SQL table into a dictionary
that maps a key to a list of rows.


::

      class KeyedTable( object ):
          def __init__( self ):
              self.rows = collections.defaultdict(list)
          def insert( self, aRow ):
              self.rows[aRow.key()].append( aRow )

SQL Operations
--------------


The single-table SELECT algorithm has a WHERE clause that gets broken
into two parts: key filtering and everything else.


The basic SELECT looks something like this.


::

      for k in table.rows[key]:
          for r in table.rows[k]:
              if other_where_clause( r ):
                  select_group_by( r )


That's the essential feature of a basic select -- it expresses a
number of design patterns.  There's a key-to-list map, a filter, and
the "select-group-by" map to results.


In theory, the SELECT operation is the more general "filter"
algorithm, where every row passes through the a general
``where_clause_filter`` process.


The Join Algorithms
--------------------

We have a number of alternative join algorithms.  In some cases, we
have two dictionaries with the same keys.  This leads to a highly
optimized query where one key locates rows on both sides of the join.


In other cases, we have a kind of nested-loops join.  We find a row
in one table, and use this row's attributes to locate a row in
another table.


The "Which is Better?" Question


We always have two alternatives for every algorithm:  the SQL version
and the Python version.  This is an essential issue in resolving the
Object-Relational Impedance mismatch issue.  We can implement our
algorithm on either side: Python objects or SQL relations.


Note that there's no simple "Use SQL for this" or "Use Python for
that" decision process.  The two structures -- objects and relations
-- are completely isomorphic.  There's no specific set of features
that dominate either representation.


The literal question that I got was "Should I use a complex data
structure in a programming language or should I use SQL ?"


Ideally, the answer is "SQL does [X] better", leading to an easy
decision.  But this kind of answer doesn't exist.


The two structures are isomorphic; the correct answer is hard to
determine.  You want the RDBMS to filter rows and return the smallest
relevant set of data to the object representation.  While locating
the fewest rows seems simple, a few things make even this hard to
determine.


While it seems that the RDBMS can be the best way to handle join
algorithms, this doesn't always work.  When we're doing a join
involving small tables, the RDBMS may be less effective than an
in-memory dictionary.  It sometimes occurs that SQL is best for
filtering very large tables only.


Indeed, the only way to chose among two isomorphic representations
(objects vs. relations) is to benchmark each implementation.





