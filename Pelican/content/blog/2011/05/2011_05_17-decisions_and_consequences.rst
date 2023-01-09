Decisions and Consequences
==========================

:date: 2011-05-17 08:00
:tags: #python,API Design
:slug: 2011_05_17-decisions_and_consequences
:category: Technologies
:status: published

A single poorly-made decision can have profound ripple-effects. Once
your stuck with it, you make accommodations, hacks and work-arounds.
Eventually, things work, but the result is less than ideal.


Changing tack requires sometimes pervasive rework to the application.
How can we reduce the risks and improve the value created?


**A Recent Example**


When dealing with bulk econometric data (Bloomberg, D&B, Moody's,
etc.) you get BIG files with lots of fields. Depending on what
you're paying for, the file layouts are frequently different even
though the content is similar. I'm a big fan of plain-old CSV
data. Even the tab-delimited variant of CSV is not bad to work
with.


Further, most vendors will slap some heading rows on the file so
that the column names are--more or less--identified. Surprisingly,
this doesn't work out well in practice because there are often
multiple columns with the same name. Sigh.


Using Python's
`csv <http://docs.python.org/release/3.1.3/library/csv.html>`__
library module lets us cope with CSV (and tab-delim) quite
gracefully.


What's wrong with that decision? Nothing.


**Variant Column Names**


The question arises when you've purchased several files of
econometric data and the column names are slightly different. This
happens with a single vendor and across vendors. It's part of the
game that can't easily be avoided. Column names vary.


What to do?


Here's the less-than-ideal decision. **Make the column names a
parameter**.


In Python, this is not terribly difficult. The csv module's
DictReader provides us a dictionary for each row. Each column name
becomes a key. We can access the fields with
some_row['this_field'] and some_row['that_field']. How bad can it
be?


The extra punctuation is fairly hideous.


More importantly, however, is the nature of the metadata.


**Consequence One -- Dynamic Metadata**


Dynamic metadata, in this case, means that any indexing of the
data is done based on character string column names.


::

    index[index_name][row[column_name]].append( row )


That's rather more complex than the alternative where the metadata
has a fixed definition.

::

    some_index[row.column].append( row )


**Consequence Two -- Murky ORM**


Once we have dynamic metadata, we're largely frozen out of
ordinary SQL database implementations. We don't know the column
names, we don't know the indices. We can't do simple CREATE TABLE
statements because we don't really have the column names until we
open the working files.


We have to grub through all the code to find out where the dynamic
mapping is reasoned out. Once we find that, we can then consider
how to make the metadata fixed enough to tackle a SQL database.


We could, of course, generate the SQL CREATE INDEX statements
on-the-fly. There's nothing wrong with it. But it slows down
analysis and decision-making when we're not sure what indexes
there are or what leads to a choice of index.


What's important here is that we want to use SQLite because it
ships with Python. We want our application to *use* an ORM (like
`SQLAlchemy <http://www.sqlalchemy.org/>`__ or
`SQLObject <http://sqlobject.org/>`__). We don't want our
application to *become* a kind of ORM because of the dynamic SQL
and dynamic column names.


**Cleanup**


The cleanup road is clear.


#. Map all variant inputs to one common structure. Rather than
work with raw dictionaries from csv, map each row to a standard
set of names. For now, we can replace the dictionaries with
named tuples to prepare for a migration to an ORM when that's
possible.
#. Replace the row['some field'] syntax with row.some_field
syntax. Of course, there's a lot of this. This is a pervasive
change.
#. Find all the dynamic index creation and refactor that into a
more static "database-like" place for now.


Item 1 is pretty easy to unit test. We're adding a function to
map from dynamic names to fixed names. Nothing much to this
testing-wise.



Item 2 requires unit tests with really good code coverage or
there's no earthy way we can be sure that each mapping-syntax
name has been transformed into an attribute-syntax name.


Item 3 barely requires testing. Indexes and other features are
performance enhancements that can be removed and added without
altering functionality.





