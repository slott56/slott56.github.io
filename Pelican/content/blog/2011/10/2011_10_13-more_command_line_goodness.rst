More Command-Line Goodness
==========================

:date: 2011-10-13 08:00
:tags: stingray reader,#python,CLI
:slug: 2011_10_13-more_command_line_goodness
:category: Technologies
:status: published


In `Command-Line Applications <{filename}/blog/2011/10/2011_10_06-command_line_applications.rst>`__,
we looked at a Python main-import switch which boiled down to this.

::

    for file in args.file:
        with open( file, "r" ) as source:
            process_file( source, args )

The point was that each distinct file on the command-line was
processed in a more-or-less uniform way by a single function that
does the "real work" for that input file.

It turns out that we often have flat files which are spreadsheets or
spreadsheet-like.   Indeed, for some people (and some organizations)
the spreadsheet is their preferred user interface.  As I've said
before,

Spreadsheets are the universal user interface. Everyone likes them,
they're almost inescapable. And they work. There's no reason to
attempt to replace the spreadsheet with a web page or a form or a
desktop application. It's easier to cope with spreadsheet vagaries
than to replace them.

They have problems, but they are surprisingly common.

Enter `Stingray
Reader <http://sourceforge.net/p/stingrayreader/home/Stingray%20--%20Schema-Based%20File%20Reader/>`__.
This is a small Python library to make it easy to have programs
which read workbooks--collections of spreadsheets--or
spreadsheet-like files with a degree of transparency.

And.  It allows a clean command-line interface.

With a little care, we can reduce the main-import switch to something
like this.

::

    if __name__ == "__main__":
      logging.basicConfig( stream=sys.stderr )
      args= parse_args()
      logging.getLogger().setLevel( args.verbosity )
      builder= make_builder( args )
      try:
          for file in args:
              with workbook.open_workbook( input ) as source:
                  process_workbook( source, builder )
          status= 0
      except Exception as e:
          logging.exception( e )
          status= 3
      logging.shutdown()
      sys.exit( status )

The bold lines are specific to workbook ("spreadsheet") processing.
A "builder" creates application-specific Python objects from
spreadsheet rows.  The "workbook.open_workbook" is a function that
builds a workbook reader based on the file name.  It can handle a
number of file types.

The process_workbook function is the "real work" function that
handles a workbook of individual spreadsheets (or a spreadsheet-like
file).





