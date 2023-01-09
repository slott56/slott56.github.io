Exploratory Programming -- Incremental Development in Python (Revised)
======================================================================

:date: 2008-10-05 23:16
:tags: architecture,design
:slug: 2008_10_05-exploratory_programming_incremental_development_in_python_revised
:category: Architecture & Design
:status: published







After some processing by customers and us and vendors and god-alone-only-knows who else, our statistician has 4 zip files, each about 15Mb.



Step one is to look inside the zip archives and see what we have.  Clearly, we can do this any of several ways.  Looking manually doesn't get us any software, so we may as well write  a Python program to explore.



There's a pattern that develops to this kind of exploration.  It uses basic inheritance to extend and extend and extend simple file processing.  Further, it uses inheritance to extend instead of rewrite.



Let's look at the first class definition.  It isn't very interesting, but it shows the design pattern.

..  code:

::

    class Operation( object ):
        def process( self, files ):
            for fileName in files:
                self.processFile( fileName )
        def processFile( self, fileName ):
            pass





Essentially, the process method is the "entry point" and it applies some yet-to-be defined process to each file.



Here's a subclass that provides that process.

..  code:

::

    class ZipContent( Operation ):
        def processFile( self, fileName ):
            zip= zipfile.ZipFile( fileName )
            for member in zip.infolist():
                print "%s: %s %s" % ( fileName, member.filename, locale.format("%d",member.file_size,grouping=True) )





This implements processFile with a simple exploration of the zip files we were sent.  



We're essentially done with sprint 1.  We can use this to explore our files.  Turns out that each zip file contains a single XLS document.  Consistency is pleasant.  On to Sprint 2.



:strong:`Exploring The Zip Members` 



Here's sprint two of the application.  There are two significant changes.  First, we make a small incremental change to the previous ZipContent class.  Then we add a subclass.



Here's the revised processFile.

..  code:

::

    def processFile( self, fileName ):
            zip= zipfile.ZipFile( fileName )
            for member in zip.infolist():
                print "%s: %s %s" % ( fileName, member.filename, locale.format("%d",member.file_size,grouping=True) )
                self.examineMember( zip, member )





The change is to add a "next level of detail" processing step: examineMember.  We merely provide a stub definition that does nothing.



Here's the next subclass.  It opens each zip archive member as a workbook, using the `xlrd <http://www.lexicon.net/sjmachin/xlrd.htm>`_  module.




..  code:

::

    class WBZipContent( ZipContent ):
        def examineMember( self, zipFile, member ):
            contents= zipFile.read( member.filename )
            wb= xlrd.open_workbook( file_contents=contents, filename=member.filename )
            for sheet in wb.sheets():
                self.examineSheet( wb, sheet )
        def examineSheet( self, wb, sheet ):
            print ">  Sheet %s %d rows" % (sheet.name, sheet.nrows )






This shows the "next level of detail" method.  Once we've opened the workbook, we can then hand each sheet to another method.  Initially, that other method just prints the sheet.




We haven't replaced any previous piece of code.  We've added some procedure calls to previous version, but we focused on extension, not revision.




We're done with sprint 2.  We can use this to explore our files.  We find that each zip archive has an XLS file.  We find that each XLS file has a consistently-named set of sheets -- just what we think we should have received.  




Now, we can subclass this -- yet again -- to build the next sprint and dump selected rows from each book.




:strong:`Exploring the Workbook sheets` 




Here's sprint three of the application.  This is yet another subclass.




..  code:

::

    class TopRowsWBZipContent( WBZipContent ):
        def __init__( self, topnRows=5 ):
            super( TopRowsWBZipContent, self ).__init__()
            self.topnRows= topnRows
        def examineSheet( self, wb, sheet ):
            print ">  Sheet %s %d rows" % (sheet.name, sheet.nrows )
            if self.topnRows is None:
                limit= sheet.nrows
            else:
                limit= min( self.topnRows, sheet.nrows )
            for r in xrange(limit):
                row= sheet.row(r)
                print r, [ c.value for c in row ]





We can use the sprint 3 version to confirm that each sheet of each book of each ZIP archive has the expected format.  



Now we're ready to subclass this yet again and actually extract the relevant rows and columns.



:strong:`Incremental Extension` 



This incremental extension is a big time-saver.  Rather than have several programs, or several complex options, our main program now does several things.  Which specific thing is does is simply a choice of which class it instantiates.



Here's a version of main.

..  code:

::

    def manual():
        """Change the options manually."""
        #op= ZipContent() # What's in the ZIP files?
        #op= TopRowsWBZipContent( topnRows=5 ) # What does the data look like?
        op= ExtractCSVWBZipContent("../data")
        files = glob.glob( "../data/*.zip" )
        op.processList( files )





If we instantiate ZipContent, we get the sprint 1 version -- the one that explores the zip archives.



If we instantiate TopRowsWBZipContent, we get the the sprint 2 version that shows the top few rows.



This incremental feature set is very handy and stems directly from two things: incremental development and two extending the inheritance hierarchy. 





