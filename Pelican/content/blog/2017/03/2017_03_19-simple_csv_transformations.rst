Simple CSV Transformations
==========================

:date: 2017-03-19 07:07
:tags: csv,#python
:slug: 2017_03_19-simple_csv_transformations
:category: Technologies
:status: published


Here's an interesting question:

    I came across your blog post "`Introduction to using Python to
    process CSV
    files <https://github.com/slott56/introduction-python-csv>`__" as I'm
    looking to do something I'd *think* is easy in Python but I don't
    know how to do it.

    I simply want to examine a column then create a new column based on
    an if-then on the original column. So if my CSV has a "gender" field
    I'd like to do the Python equivalent of this SQL statement:

    ::

       case when gender = 'M' then 1 else 0 end as gender_m, case when
       gender = 'F' then 1 else 0 end as gender_f,...


    I can do it in Pandas but my CSVs are too big and I run into memory
    issues.


There are a number of ways to tackle this.

First -- and foremost -- this is almost always just one step in a much
longer and more complex set of operations. It's a little misleading to
read-and-write a CSV file to do this.

A **little** misleading.

It's not wrong to write a file with expanded data. But the
"incrementally write new files" process can become rather complex. If
we have a large number of transformations, we can wind up with many
individual file-expansion steps. These things often grow organically
and can get out of control. A complex set of steps should probably be
collapsed into a single program that handles all of the expansions at
once.

This kind of file-expansion is simple and fast. It can open a door
previously closed by the in-memory problem  of trying to do the entire
thing in pandas.

The general outline looks like this

::

   from pathlib import Path
   import csv
   source_path = Path("some_file.csv")
   target_path = Path(source_path.stem + "_1").with_suffix('.csv')

   def transform(row):
       return row

   with source_path.open() as source_file:
       with target_path.open('w', newline='') as target_file:
           reader = csv.DictReader(source_file)
           columns =  reader.fieldnames + ['gender_m', 'gender_f']
           writer = csv.DictWriter(target_file, columns)
           writer.writeheader()
           for row in reader:
               new_row = transform(row)
               writer.writerow(new_row)


The goal is to be able put some meaningful transformation processing
in place of the build new_row comment.

The overall approach is this.

1.  Create ``Path`` objects to refer to the relevant files.

2.  Use ``with``-statement context managers to handle the open files. This
    assures that the files are always properly closed no matter what kinds
    of exceptions are raised.

3.  Create a dictionary-based reader for the input.  Add the additional
    columns and create a dictionary-based writer for the output. This
    allows the processing to work with each row of data as a dictionary.

This presumes that the data file actually has a single row of heading
information with column names.

If column names are missing, then a fieldnames attribute can be
provided when creating the DictReader(), like this:

::

    csv.DictReader(source_file, ['field', 'field', ...]).

The **for** statement works because a csv Reader is an iterator over
each row of data.

I've omitted any definition of the transformational function. Right
now, it just returns each row unmodified. We'd really like it to do
some useful work.

Building The New Row
--------------------


The transformation function needs to build a new row from an existing
row.

Each row will be a Python dictionary. A dictionary is a mutable
object. We aren't **really** building a completely new object --
that's a waste of memory. We'll modify the row object, and return it
anyway. It will involve a microscopic redundancy of creating two
references to the same dictionary object, one known by the variable
name row and the other know by new_row.

Here's an example body for transform()

::

   def transform(row):
       row['gender_m'] = 1 if row['gender'] == 'M' else 0
       row['gender_f'] = 1 if row['gender'] == 'F' else 0
       return row




This will build two new keys in the row dictionary. The exact two keys
added to the fieldnames to write a new file.

Each key be associated with a value computed by a simple expression.
In this case, the logical if-else operator is used to map a boolean
value, row['gender'] == 'M', to one of two integer values, 1 or 0.

If this is confusing -- and it can be -- this can also be done with if
statements instead of expressions.

::

   def transform(row):
       if row['gender'] == 'M':
           row['gender_m'] = 1
       else:
           row['gender_m'] = 0
       row['gender_f'] = 1 if row['gender'] == 'F' else 0
       return row




I only rewrite the 'M' case. I'll leave the rewrite of the 'F' case to
the reader.

Faster Processing with a Generator
----------------------------------


We can simplify the body of the script slightly. This will make it
work a hair faster. The following statements involve a little bit of
needless overhead.

::

           for row in reader:
               new_row = transform(row)
               writer.writerow(new_row)




We can change this as follows:

::

           writer.writerows(transform(row) for row in reader)




This uses a generator expression, transform(row) for row in reader, to
build individually transformed rows from a source of data. This
doesn't involve executing two statements for each row of data.
Therefore, it's faster.

We can also reframe it like this.

::

           writer.writerows(map(transform, reader))




In this example, we've replaced the generator expression with the
map() function. This applies the transform() function to each row
available in the reader.

In both cases, the writer.writerows() consumes the data produced by
the generator expression or the map() function to create the output
file.

The idea is that we can make the transform() function as complex as we
need. We just have to be sure that all the new field names are handled
properly when creating the writer object.



-----

your article on data science is very interesting t...
-----------------------------------------------------

Komal<noreply@blogger.com>

2019-08-30 01:18:55.687000-04:00

your article on data science is very interesting thank you so much.
`Data Science Training in
Hyderabad <https://aditidigitalsolutions.com/data-science-training-hyderabad?ref=gmb/>`__


thank you for the valuable information giving on d...
-----------------------------------------------------

Aditi Digital Solutions<noreply@blogger.com>

2019-08-30 01:17:36.825000-04:00

thank you for the valuable information giving on data science it is very
helpful.
`Data Science Training in
Hyderabad <https://aditidigitalsolutions.com/data-science-training-hyderabad?ref=gmb/>`__





