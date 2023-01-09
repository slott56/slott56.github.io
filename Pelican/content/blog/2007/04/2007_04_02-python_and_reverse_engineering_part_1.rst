Python and Reverse Engineering, Part 1
======================================

:date: 2007-04-02 17:38
:tags: management
:slug: 2007_04_02-python_and_reverse_engineering_part_1
:category: Management
:status: published





Python is
**Batteries Included** ™ programming.  These analysis
tools are either Python **Out Of the Box** , or they are straight-forward downloads of
other open-source components.



Here are
some analytical situations where Python has saved my bacon.  I'll present some
code for several of these.

#.  Legacy Data Domains.  There are legacy (in
    this case Z/OS COBOL) files which are source data for the data warehouse.  What
    are the domains of various attributes?  The "data dictionary" doesn't say, and
    reading the code is hard to do because there's no easy way to determine all of
    the programs which read or write the given files.  Remember, there's not GREP on
    the mainframe.

#.  Source Code Analysis for C, VB, SQL, etc. 
    This varies from simple String operations to moderate use of the
    **re** 
    package to using PLY or similar high-end parsing tools.

#.  Test Data Generation.

#.  Proof of Concept for SOAP adaptations and
    extensions.



**Legacy Data Domain Analysis.** 



Analyzing legacy data
files involves some pleasant features of Python.  It is an easy job, and easy to
extend and refine.  There are a number of sub-problems that have to be solved as
part of this.



We'll look at the
**Transfer Problem** , the
**EBCDIC Problem** , and the
**File Layout Problem**  first.  Then we'll show what the
overall application might look
like.



**The Transfer Problem.** 



One of the first hurdles
is getting files off the Z/OS mainframe and onto a desktop PC where they can be
analyzed.  One client fooled around with the TSO file transfer and declared data
analysis to be impossible.  The TSO file transfer takes HOURS to transfer a
moderately large file; FTP takes seconds. 




Python's `urllib <http://docs.python.org/lib/module-urllib.html>`_  module allows us to write simple,
automated FTP-like scripts that reliably fetch files, produce useful messages
and log their progress.  TSO file moving is silly.  Manual file operations,
while fine for the initial round of development and test, shouldn't be used in
the long run.



**The EBCDIC Problem.** 



Parts of Z/OS files,
generally, are coded in EBCDIC.  Python expects ASCII or Unicode.  Because the
EBCDIC character set is disjoint from ASCII, you'll do well to use Unicode
files.  However, if you can't part with ASCII, you can work out sensible
translation schemes.



Other parts of
Z/OS files, however, are not in EBCDIC.  Numeric data fields may be encoded in
binary, or may be encoded in packed decimal format.  Therefore, there is no
simple transformation from EBCDIC to ASCII or
Unicode.



If you allow FTP to translate
from EBCDIC, all of your binary and packed decimal fields will become useless
coprolite.  Instead, you'll need to know the COBOL record layout.  This will
allow you to pick apart individual fields, doing appropriate conversions: text
to Unicode, binary to integer, and packed decimal to Python
decimal.



Also, Python's `codecs <http://docs.python.org/lib/standard-encodings.html>`_  module has the cp037 (also known as
IBM037 and IBM039) encodings that will translate EBCDIC to something more
useful.



**The Record Layout Problem.** 



COBOL data is rarely in
any kind of delimited format.  It is almost universally in fixed field-length
format.  COBOL has verbs that will create XML or CSV files.  However, you're
adding to your legacy, not replacing it when you start writing mainframe
programs to help you get rid of mainframe programs.  To get rid of the legacy,
you have to stop using it.  This means stopping use of COBOL, even to prepare
files for use in non-COBOL environments. 




Fortunately, it's quite easy to handle
COBOL Data Definition Entries (DDE), also called Record Layouts or "Copybooks". 
These can be parsed in Python, and a Python data structure used to define the
offset, length and coding scheme for each field within a COBOL record.  Since
this structure knows the data type, it has responsibility for conversion from
Z/OS-COBOL encodings to more universal Unicode
encodings.



There are two ways to
approach the DDE parsing.  You can -- without too much effort -- use `PLY <http://www.dabeaz.com/ply/>`_  to create
a lexer and parser for the relevant subset of COBOL.  However, the subset of
COBOL is simple enough that 1,000 lines of code gets you a robust-enough parser
for COBOL DDE files.  I talk a little about this in `My Legacy Nightmares: Coping with COBOL
Coexistence <../C257963460/E20060902151714.html>`_ .



**Analysis.** 



The
data analysis applications devolve to something delightfully
simple.



1.  Get the source file from
the mainframe.

2.  Parse the DDE "copybook"
that defines the file.

3.  Build a "record
analyzer" which picks specific fields out of the file, and accumulates a
dictionary of field values and number of occurrences.  A record analyzer is a
collection of individual field analyzers.  We'll look at a field analyzer
below.

4.  Read each record, apply the record
analyzer to the sequence of bytes which were
read.

5.  At end of file, write the final
results from each field of the record
analyzer.



**Example Field Analyzer.** 



Here's a Field Analyzer. 
There are a number of possible specializations for handling indexed fields and
numeric fields.



..  code:

::

    class FieldValue:
        """Accumulate unique values for a named field of a DDE.
    
        This will have to be subclassed for indexes of occurs clauses.
        """
        def __init__( self, dde, cobolName ):
            """Given a DDE and a COBOL name, set up a field extractor and frequency mapping."""
            self.cobolName= cobolName
            self.usage = dde.get(cobolName).usage
            self.get_field= dde.get(cobolName)
            self.domain= {}
        def getFrom( self, data ):
            """Get the value from the field, then accumulate in the frequency mapping."""
            v= self.get_field.of( data )
            self.domain[v]= self.domain.setdefault(v,0) + 1
        def fqTable( self ):
            """Return a sequence of tuples with value and frequency count, sorted."""
            val_count= self.domain.items()
            # Sort descending by second field (count), ascending by first field (value)
            val_count.sort( lambda a,b: cmp(b[1],a[1]) or cmp(a[0],b[0]) )
            return val_count





**Example Record Analyzer.** 



Here's the canonical
record analyzer.  It is initialized with a sequence of field
analyzers.



..  code:

::

    class RecordAnalyzer:
        def __init__( self, aFieldList ):
            self.fieldList= aFieldList
        def process( self, recno, data ):
            for f in self.fieldList:
                f.getFrom( data )
        def final( self, records ):
            print "\n%d Records" % ( records )
            for f in self.fieldList:
                print "\n%-10s %7s" % ( f.cobolName, "count" )
                for di,c in f.fqTable():
                    print "%-10s %7d" % ( di,c )





**Application Class.** 



Here's the result data
analysis application class.  It is initialized with a parsed DDE and a
RecordAnalyzer.  This will examine one or more files to accumulate a data
domain.  The final report will show the selected fields, the unique values, and
the number of occurrences.



..  code:

::

    class FileScan:
        """Basic file scanning operation."""
        def __init__( self, aDDE, aFieldProcess ):
            self.dde= aDDE
            self.fieldProcess= aFieldProcess
            self.record= 0
        def reclen( self ):
            return self.dde.size
        def process( self, aFileName, end=-1 ):
            self.theFile= file( aFileName, "rb" )
            self.record= 0
            data= self.theFile.read( self.reclen() )
            while data:
                self.record += 1
                self.fieldProcess.process( self.record, data )
                if self.record == end: break
                data= self.theFile.read( self.reclen() )
            self.theFile.close()
            self.fieldProcess.final(self.record)





Perhaps in a future posting I'll
finish describing the COBOL DDE parser.  I'm reluctant to go too far, because I
really ought to rework it to be a proper PLY implementation, rather than a
from-scratch scanner and parser.











