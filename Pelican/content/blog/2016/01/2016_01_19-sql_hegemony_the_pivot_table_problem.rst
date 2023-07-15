SQL Hegemony -- the "Pivot Table" problem
=========================================

:date: 2016-01-19 08:00
:tags: #python,database design,SQL
:slug: 2016_01_19-sql_hegemony_the_pivot_table_problem
:category: Technologies
:status: published

| As far as I can tell, the **Pivot Table Problem™** only exists for
  people who have actively put on blinders so that they can only see
  data one way.
| This leads to the following.
| The context appears to be millions of rows of data. Hundreds of
  columns.  It appears that someone we'll call DesKtop tried to load a
  spreadsheet to "pivot" the data. And the spreadsheet -- of course --
  breaks because it's too much data.
| DesKtop then calls the DBA.
| DesKtop: "We need to load a table and use the database to create a
  spread-sheet like pivot table."
| DBA: "Okay. Cool. It's complex SQL, though. Check this out..." They
  look at the Oracle 11g PIVOT and UNPIVOT.
| DesKtop: "Oh my. That's really complex. Okay, I guess that's the only
  choice, right?"
| DBA: "Right, it is our only possible choice."
| Wrong.
| [I heard about this from DBA who sent me a "humble brag" about
  something that can only be done with hyper-complex SQL query. DBA had
  found a Python tutorial on Pandas that mentioned pivoting. The humble
  brag point was this: the Python stuff was just as hyper-complex as the
  SQL. Apparently, DBA conflated the entire tutorial with the one line
  of code that was the pivot example.]
| If you restructure the data into (*row key, column key, cell value*)
  triples, you don't have a **Pivot Table Problem™** any more. You have
  a SELECT reduction() GROUP BY row *vs*. SELECT reduction GROUP BY
  column kind of query. There's no "pivot". Maybe it's a conceptual
  pivot but there's no hyper-complex SQL.
| It requires a non-trivial loader to transform data that's in row order
  and explode it into triples. This isn't the kind of thing a program
  like Oracle's SQL*Loader or other bulk loader does particularly well.
  In Python (without using Pandas) we can expand the data into triples
  like this:

::

   for row in reader:
       for column in column_names:
           new_row = row['key'], column, row[column]
           insert...

| 
| The idea here is that we're using something like a csv DictReader. We
  have a list of column names we'd like to pivot. In many row-oriented
  data sets, there are columns we might like to ignore. For example, the
  row key column itself shouldn't be exploded into a (*row key, column
  key, row key*) triple.
| This restructuring idea applies in full force to doing Python-based
  reduction of the data. Forget loading a database in the first place.

::

   by_column = defaultdict(list)
   for row in reader:
       for column in column_names:
           by_column[column].append(row[column])

| 
| We've summarized each column's data into a list of values. This is the
  "GROUP BY" part of the SQL. Now we can do reductions on the values in
  each column-based list.

::

   from statistics import mean
   for column in by_column:
       print(column, sum(by_column[column]), mean(by_column[column]))

| 
| We've done sum and mean reductions on the values in each column. We
  can -- of course -- layer in mapping and filtering if that's required.
| This works well for millions of individual cells of data. We can
  comfortably hold several hundred million individual values in memory
  in a 32Gb desktop computer. You may notice the fan kicks on when this
  is running.
| If this turns out to require too much storage, then the reductions can
  be computed item-by-item rather than simply accumulating a list of
  values. This a hair more complex, but not in an interesting way.

::

   sum_by_column = defaultdict(int)
   count_by_column = defaultdict(int)

   for row in reader:
       for column in column_names:
           sum_by_column[column] += row[column]
           count_by_column[column] += 1

| 
| Minima and Maxima are a trifle trickier. We don't want to initialize
  them to None and have an if current_min is None statement executed
  millions of times. We have to create an iterator and process the first
  row specially, using it to initialize all of the values. The remaining
  rows can then be processed free of any initialization question.

::

   row_iter= iter(reader)
   first = next(row_iter)
   for column in column_names:
       min_by_column[column]= row[column]
       max_by_column[column]= row[column]
   for row in row_iter:
       for column in column_names:
           min_by_column[column] = min( min_by_column[column], row[column])
           max_by_column[column] = max(max_by_column[column], row[column])

| 
| I like to call this the **Head-Tail** design pattern.
| The DBA and DesKtop appear to be married to SQL. Even when it appears
  to be an ineffective solution to their problem.
|





