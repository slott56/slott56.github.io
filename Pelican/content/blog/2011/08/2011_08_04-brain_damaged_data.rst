Brain-Damaged Data
==================

:date: 2011-08-04 08:00
:tags: csv,#python
:slug: 2011_08_04-brain_damaged_data
:category: Technologies
:status: published

We process a fair amount of externally-prepared datasets.  40,000 rows
of econometric data that we purchased from a third-party.  Mostly, the
data is in a usable format: .CSV or .XSLX.

Once in a while, we get CSV with ``|``.  A few times, we got
fixed-format COBOL-style records.

Recently, we got a CSV-with-pipe that included 2 records with embedded
``\n`` sequences in the middle of a CSV row of data.  Really.

**Painful Elimination**

There are two ways to "eliminate" this problem.

-  Subclass our input processing to handle this special CSV-with-pipe
   case.

-  Actually read and parse the source file creating a clean intermediate
   file that we can simply process with an existing CSV-with-pipe
   configuration.

I elected to do the first.  The second is (to my mind) an auditing
nightmare because we touched the file.  We have to prove that we
didn't disturb any other fields.  While not impossible, it becomes a
very strange special case for this one-and-only file.

**CSV Simplicity**

The CSV module's epic simplicity makes it easy to work around this
kind of goofy data.  Our subclass for this case had the following
extra foolishness put in

::

   def make_reader( self ):
           def filter_damage( aFile ):
               file_iter= iter(aFile)
               for row in file_iter:
                   if row.rfind('"') >= len(row)-3:
                       logger.error( "Damaged Line: %r", row )
                       rest= next(file_iter)
                       line= row[:row.rfind('"')] + rest[3:]
                       logger.warning( "Repaired Line: %r", line )
                       yield line
                   else:
                       yield row
           tweaked_file= filter_damage( self.sourceFile )
           return csv.reader( tweaked_file, delimiter='|', doublequote=False, escapechar='"' )


That's it.  Since the Python CSV reader merely wants an iterator over
lines, we can (with a simple generator function) provide the necessary
"iterator-over-lines".

Delightful.

**Apology**

The murky-looking ``row.rfind('"') >= len(row)-3`` condition is one of
those consequences of trying to find just a few irregular line endings
in an otherwise regular file.  For CSV processing, files often have to
be opened in "rb" mode because they originate (or will be used with)
MS-Excel.  This makes the damaged line-ending either ``\n`` or maybe
``\\r\\n``.  Rather than spend too much time negotiating with Python's
universal newline and "rb" mode, it's slightly easier to look for a
``"`` near the end.

We're hoping this is a one-time-only subclass that we can safely
ignore in the future.  If hope is dashed, it's a distinct subclass, so
it's easily reused and didn't break anything else.


