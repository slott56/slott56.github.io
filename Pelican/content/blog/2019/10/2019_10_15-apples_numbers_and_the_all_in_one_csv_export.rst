Apple's Numbers and the All-in-One CSV export
=============================================

:date: 2019-10-15 08:00
:tags: #python,spreadsheet
:slug: 2019_10_15-apples_numbers_and_the_all_in_one_csv_export
:category: Technologies
:status: published


Author F. L. Stevens has a hellishly complex (and irregular)
spreadsheet with agents, agencies, and query status. (This is how
fiction gets marketed: querying agents.) The spreadsheet has become
unmanageably complex, with multiple pages. Each page has multiple
tables. Buried in this are three "interesting" tables with agent query
information.

Can we talk about drama? There is the dark night of the soul for
anyone interested in regular, normalized data.

We have some fundamental choices for working with this mess:

#. Export each relevant table to separate files. Lots of manual
   pointy-clicky and opportunities for making mistakes.
#. Export the whole thing to separate files. Less pointy-clicky.
#. Export the whole thing to one file. About the same pointy-clicky and
   error vulnerability as #2. But. Simpler still because there's one
   file to take care of. Something a fiction author should be able to
   handle.


The all-in-one CSV export is (initially) exasperating. Each table is
wrapped in a prefix and suffix.

The prefix is a line with "Sheet: Table" Yes. There's a ": " (colon
space) separator. The suffix is a simple blank line, essentially
indistinguishable from a blank line within a table.

If the table was originally in strict first normal form (1NF) each row
would have the same number of commas. If cells are merged, however,
the number of commas can be fewer. This makes it potentially difficult
to distinguish blank rows in a table from blank lines between tables.

It's generally easiest to ignore the blank lines entirely. We can
distinguish table headers because they're a single cell with a sheet:
table format. We are left hoping there aren't any tables that have
values that have this format.

We have two ways to walk through the values:

-  Preserving the Sheet, Table, Row hierarchy. We can think of this as
   the *for s in sheet: for t in table: for r in rows* structure. The
   sheet iterator is Iterator[Tuple[str, Table_Iterator]].
   The Table_Iterator is similar: Iterator[Tuple[str, Row_Iterator]].
   The Row_Iterator, is the most granular Iterator[Dict[str, Any]].
-  Flattening this into a sequence of "(Sheet name, Table Name, Row)"
   triples. Since a sheet and table have no other attributes beyond a
   name, this seems advantageous to me.

The hierarchical form requires a number of generator functions for
Sheet-from-CSV, Table-from-CSV, and Row-from-CSV. Each of these works
with a single underlying iterator over the source file and a fairly
complex hand-off of state. If we only use the sheet iterator, the
tables and rows are skipped. If we use the table within a sheet, the
first table name comes from the header that started a sheet; the
table names come from distinct headers until the sheet name changes.

The table-within-sheet iteration is very tricky. The first table is a
simple yield of information gathered by the sheet iterator. Any
subsequent tables, however, may be based one one of two conditions:
either no rows have been consumed, in which case the table iterator
consumes (and ignores) rows; or, all the rows of the table have been
consumed and the current row is another "sheet: table" header.

The code sample below involves a fair amount of repetition. It's not
appealing to refactor this because it's ungainly in its complexity,
and doesn't create any tangible value. (I haven't even tried to get
the type hints right.)

::

   class SheetTable:
       def __init__(self, source_path: Path) -> None:
           self.path: Path = source_path
           self.csv_source = None
           self.rdr = None
           self.header = None
           self.row = None

       def __enter__(self) -> None:
           self.csv_source = self.path.open()
           self.rdr = csv.reader(self.csv_source)
           self.header = None
           self.row = next(self.rdr)
           return self

       def __exit__(self, *args) -> None:
           self.csv_source.close()

       def _sheet_header(self) -> bool:
           return len(self.row) == 1 and ': ' in self.row[0]

       def sheet_iter(self):
           while True:
               while not (self._sheet_header()):
                   try:
                       self.row = next(self.rdr)
                   except StopIteration:
                       return
               self.sheet, _, self.table = self.row[0].partition(": ")
               self.header = next(self.rdr)
               self.row = next(self.rdr)
               yield self.sheet, self.table_iter()

       def table_iter(self):
           yield self.table, self.row_iter()
           while not (self._sheet_header()):
               try:
                   self.row = next(self.rdr)
               except StopIteration:
                   return
           next_sheet, _, next_table = self.row[0].partition(": ")
           while next_sheet == self.sheet:
               self.table = next_table
               self.header = next(self.rdr)
               self.row = next(self.rdr)
               yield self.table, self.row_iter()
               while not (self._sheet_header()):
                   try:
                       self.row = next(self.rdr)
                   except StopIteration:
                       return
               next_sheet, _, next_table = self.row[0].partition(": ")

       def row_iter(self):
           while not self._sheet_header():
               yield dict(zip(self.header, self.row))
               try:
                   self.row = next(self.rdr)
               except StopIteration:
                   return


Clearly, this is craziness.

Flattening is much nicer.

::

   def sheet_table_iter(source_path: Path) -> Iterator[Tuple[str, str, Dict[str, Any]]]:
       with source_path.open() as csv_source:
           rdr = csv.reader(csv_source)
           header = None
           for row in rdr:
               if len(row) == 0:
                   continue
               elif len(row) == 1 and ": " in row[0]:
                   sheet, table = row[0].split(": ", maxsplit=1)
                   header = next(rdr)
                   continue
               else:
                   # Inject headers to create dict from row
                   yield sheet, table, dict(zip(header, row))




This provides a relatively simple way to find the relevant tables and
sheets. We can use something as simple as the following to locate the
relevant data.

::

       for sheet, table, row in sheet_table_iter(source_path):
           if sheet == 'AgentQuery' and table == 'agent_query':
               agent = agent_query_row(database, row)
           elif sheet == 'AAR-2019-03' and table == 'Table 1':
               agent = aar_2019_row(database, row)




This lets us write pleasant functions that handle exactly one row from
the source table. We'll have one of these for each target table. In
the above example, we've only shown two, you get the idea. Each new
source table, with its unique headers can be accommodated.
