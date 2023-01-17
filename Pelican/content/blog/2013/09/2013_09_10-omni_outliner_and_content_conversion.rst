Omni Outliner and Content Conversion
====================================

:date: 2013-09-10 08:00
:tags: data conversion,#python,ETL,csv
:slug: 2013_09_10-omni_outliner_and_content_conversion
:category: Technologies
:status: published


First, and most important, `Omni
Outliner <http://www.omnigroup.com/products/omnioutliner/>`__ is a
super-flexible tool. Crazy levels of flexibility. It's very much a
generic-all-singing-all-dancing information management tool.

It has a broad spectrum of file export alternative formats. Most of
which are fine for import into some kind of word processor.

But what if the data is more suitable for a spreadsheet or some more
structured environment? What if it was a detailed log or a project
outline decorated with a column of budget numbers?

We have two approaches, one is workable, but not great, the other has
numerous advantages.

Answer 1: Workable
------------------

Sure, you say, that's easy. Export into a Plain Text with Tabs (or
HTML or OPML) and then parse the resulting tab-delimited file.

In Python. Piece of cake.

::

   import csv

   class Tab_Delim(csv.Dialect):
       delimiter='\t'
       doublequote=False
       escapechar='\\'
       lineterminator='\n'
       quotechar=''
       quoting=csv.QUOTE_NONE
       skipinitialspace=True
       
   rdr= csv.reader( source, dialect=Tab_Delim )
   column_names= next(rdr)
   for row in rdr:
      # Boom. There it is.    




That gets us started. But.

Each row is variable length. The number of columns varies with the
level of indentation. The good news is that the level of indentation
is consistent. Very consistent. Year, Month, Topic, Details in this
case.

[*When an outline is super consistent, one wonders why a spreadsheet
wasn't used.*]

Each outline node in the export is prefaced with "- ".

It looks pretty when printed. But it doesn't parse cleanly, since the
data moves around.

Further, it turns out that "notes" (blocks of text attached to an
outline node, but not part of the outline hierarchy) show up in the
last column along with the data items that properly belong in the last
column.

Sigh.

The good news is that notes seem to appear on a line by themselves,
where the data elements seem to be properly attached to outline nodes.
It's still possible to have a "blank" outline node with data in the
columns, but that's unlikely.

We have to do some cleanup

Answer 1A: Cleanup In Column 1
------------------------------

We want to transform indented data into proper first-normal form
schema with a consistent number of fixed columns. Step 1 is to know
the deepest indent. Step 2 is to then fill each row with enough empty
columns to normalize the rows.

Each specific outline has a kind of schema that defines the layout of
the export file. One of the tab-delimimted columns will be the
"outline" column: it will have tabs and leading "-" to show the
outline hierarchy. The other columns will be non-outline columns.
There may be a notes column and there will be the interesting data
columns which are non-notes and non-outline.

In our tab-delimited export, the outline ("Topic") is first. Followed
by two data columns. The minimal row size, then will be three columns.
As the topics are indented more and more, then the number of columns
will appear to grow. To normalize, then, we need to pad, pushing the
last two columns of data to the right.

That leads to a multi-part cleanup pipeline. First, figure out how
many columns there are.

::

       rows= list( rdr )
       width_max= max( len(r) for r in rows )+1




This allows us the following two generator functions to fill each row
and strip "-".

::

   def filled( source, width, data_count ):
       """Iterable with each row filled to given width.
       Rightmost {data_count} columns are pushed right to preserve
       their position.
       """
       for r_in in source:
           yield r_in[:-data_count] + ['']*(width-len(r_in)) + r_in[-data_count:]

   def cleaned( source ):
       """Iterable with each column cleaned of leading "- "
       """
       def strip_dash( c ):
           return c[2:] if c.startswith('- ') else c

       for row in source:
           yield list( strip_dash(c) for c in row )




That gets us to the following main loop in a conversion function.

::

       for row in cleaned( filled( rows, width_max, len(columns) ) ):
           # Last column may have either a note or column data.
           # If all previous columns empty, it's probably a note, not numeric value.
           if all( len(c)==0 for c in row[:-1] ):
               row[4]= row[-1]
               row[-1]= ''
           yield row




Now we can do some real work with properly normalized data. With
overheads, we have an 80-line module that lets us process the outline
extract in a simple, civilized CSV-style loop.

The Ick Factor
--------------

What's unpleasant about this is that it requires a fair amount of
configuration.

The conversion from tab-delim outline to normalized data requires some
schema information that's difficult to parameterize.

1. Which column has the outline.

2. Are there going to be notes on lines by themselves.

We can deduce how many columns of ancillary data are present, but the
order of the columns is a separate piece of logical schema that we
can't deduce from the export itself.





