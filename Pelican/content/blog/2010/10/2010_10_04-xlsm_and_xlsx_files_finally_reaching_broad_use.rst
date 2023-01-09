.xlsm and .xlsx Files -- Finally Reaching Broad Use
===================================================

:date: 2010-10-04 08:00
:tags: #python,xml,spreadsheet,xlsx,xlsm,zipfile,excel
:slug: 2010_10_04-xlsm_and_xlsx_files_finally_reaching_broad_use
:category: Technologies
:status: published

For years, I've been using `Apache POI <http://poi.apache.org/>`__ in
Java and `XLRD <http://www.lexicon.net/sjmachin/xlrd.htm>`__ in Python
to read spreadsheets. Finally, now that .XLSX and .XLSM files are in
more widespread use, we can move away from those packages and their
reliance on successful reverse engineering of undocumented features.

Spreadsheets are -- BTW -- the universal user interface. Everyone
likes them, they're almost inescapable. And they work. There's no
reason to attempt to replace the spreadsheet with a web page or a
form or a desktop application. It's easier to cope with
spreadsheet vagaries than to replace them.

The downside is, of course, that users often tweak their
spreadsheets, meaning that you never have a truly "stable"
interface. However, transforming each row of data into a Python
dictionary (or Java mapping) often works out reasonably well to
make your application mostly immune to the common spreadsheet
tweaks.

Most of the .XLSX and .XLSM spreadsheets we process can be
trivially converted to CSV files. It's manual, yes, but a quick
audit can check the counts and totals.

Yesterday we got an .XLSM with over 80,000 plus rows. It couldn't
be trivially converted to CSV by my installation of Excel.

What to do?

**Python to the Rescue**

Step 1. Read the standards. Start with the Wikipedia article: "`Open
Office XML <http://en.wikipedia.org/wiki/Office_Open_XML>`__". Move
to the `ECMA
376 <http://www.ecma-international.org/publications/standards/Ecma-376.htm>`__
standard.

Step 2. It's a zip archive. So, to process the file, we need to
locate the various bits inside the archive. In many cases, the zip
members can be processed "in memory". In the case of our 80,000+ row
spreadsheet, the archive is 34M. The sheet in question expands to a
215M beast. The shared strings are 3M. This doesn't easily fit into
memory.

Further, a simple DOM parser, like Python's excellent
`ElementTree <http://docs.python.org/library/xml.etree.elementtree.html>`__,
won't work on files this huge.

**Expanding an XLSX or XLSM file**

Here's step 2. Expanding the zip archive to locate the shared strings
and sheets.

::

    import zipfile
    def get_worksheets(name):
        arc= zipfile.ZipFile( name, "r" )
        member= arc.getinfo("xl/sharedStrings.xml")
        arc.extract( member )
        for member in arc.infolist():
            if member.filename.startswith("xl/worksheets") and member.filename.endswith('.xml'):
                arc.extract(member)
                yield member.filename

This does two things. First, it locates the shared strings and the
various sheets within the zip archive. Second, it expands the sheets
and shared strings into the local working directory.

There are many other parts to the workbook archive. The good news is
that we're not interesting in complex workbooks with lots of cool
Excel features. We're interested in workbooks that are basically
file-transfer containers. Usually a few sheets with a consistent
format.

Once we have the raw files, we have to parse the shared strings
first. Then we can parse the data. Both of these files are simple
XML. However, they don't fit in memory. We're forced to use SAX.

**Step 3 -- Parse the Strings**

Here's a SAX ContentHandler that finds the shared strings.

::

    import xml.sax
    import xml.sax.handler

    class GetStrings( xml.sax.handler.ContentHandler ):
        """Locate Shared Strings."""
        def __init__( self ):
            xml.sax.handler.ContentHandler.__init__(self)
            self.context= []
            self.count= 0
            self.string_dict= {}
        def path( self ):
            return [ n[1] for n in self.context ]
        def startElement( self, name, attrs ):
            print( "***Non-Namespace Element", name )
        def startElementNS( self, name, qname, attrs ):
            self.context.append( name )
            self.buffer= ""
        def endElementNS( self, name, qname ):
            if self.path() == [u'sst', u'si', u't']:
                self.string_dict[self.count]= self.buffer
                self.buffer= ""
                self.count += 1
            while self.context[-1] != name:
                self.context.pop(-1)
            self.context.pop(-1)
     def characters( self, content ):
            if self.path() == [u'sst', u'si', u't']:
                self.buffer += content

This handler collects the strings into a simple dictionary, keyed by
their relative position in the XML file.

This handler is used as follows.

::

    string_handler= GetStrings()
    rdr= xml.sax.make_parser()
    rdr.setContentHandler( string_handler )
    rdr.setFeature( xml.sax.handler.feature_namespaces, True )
    rdr.parse( "xl/sharedStrings.xml" )

We create the handler, create a parser, and process the shared
strings portion of the workbook. When this is done, the handler has a
dictionary of all strings. This is string_handler.string_dict. Note
that a `shelve <http://docs.python.org/library/shelve.html>`__
database could be used if the string dictionary was so epic that it
wouldn't fit in memory.

**The Final Countdown**

Once we have the shared strings, we can then parse each worksheet,
using the share string data to reconstruct a simple CSV file (or JSON
document or something more usable).

The Content Handler for the worksheet isn't too complex. We only want
cell values, so there's little real subtlety. The biggest issue is
coping with the fact that sometimes the content of a tag is reported
in multiple parts.

::

    class GetSheetData( xml.sax.handler.ContentHandler ):
        """Locate column values."""
        def __init__( self, string_dict, writer ):
            xml.sax.handler.ContentHandler.__init__(self)
            self.id_pat = re.compile( r"(\D+)(\d+)" )
            self.string_dict= string_dict
            self.context= []
            self.row= {}
            self.writer= writer
        def path( self ):
            return [ n[1] for n in self.context ]
        def startElement( self, name, attrs ):
            print( "***Non-Namespace Element", name )
        def startElementNS( self, name, qname, attrs ):
            self.context.append( name )
            if name[1] == "row":
                self.row_num = attrs.getValueByQName(u'r')
            elif name[1] == "c":
                if u't' in attrs.getQNames():
                    self.cell_type = attrs.getValueByQName(u't')
                else:
                    self.cell_type = None # defult, not a string
                self.cell_id = attrs.getValueByQName(u'r')
                id_match = self.id_pat.match( self.cell_id )
                self.row_col = self.make_row_col( id_match.groups() )
            elif name[1] == "v":
                self.buffer= "" # Value of a cell
            else:
                pass # might do some debugging here.
        @staticmethod
        def make_row_col( col_row_pair ):
            col = 0
            for c in col_row_pair[0]:
                col = col*26 + (ord(c)-ord("A")+1)
            return int(col_row_pair[1]), col-1
        def endElementNS( self, name, qname ):
            if name[1] == "row":
                # write the row to the CSV result file.
                self.writer.writerow( [ self.row.get(i) for i in xrange(max(self.row.keys())) ] )
                self.row= {}
            elif name[1] == "v":
                if self.cell_type is None:
                    try:
                        self.value= float( self.buffer )
                    except ValueError:
                        print( self.row_num, self.cell_id, self.cell_type, self.buffer )
                        self.value= None
                elif self.cell_type == "s":
                    try:
                        self.value= self.string_dict[int(self.buffer)]
                    except ValueError:
                        print( self.row_num, self.cell_id, self.cell_type, self.buffer )
                        self.value= None
                elif self.cell_type == "b":
                    self.value= bool(self.buffer)
                else:
                    print( self.row_num, self.cell_id, self.cell_type, self.buffer, self.string_dict.get(int(self.buffer)) )
                    self.value= None
                self.row[self.row_col[1]] = self.value
                while self.context[-1] != name:
                    self.context.pop(-1)
                self.context.pop(-1)
        def characters( self, content ):
            self.buffer += content

This class and the shared string handler could be refactored to
eliminate a tiny bit of redundancy.

This class does two things. At the end of a tag, it determines what
data was found. It could be a number, a boolean value or a shared
string. At the end of a tag, it writes the row to a CSV writer.

This handler is used as follows.

::

    rdr= xml.sax.make_parser()
    rdr.setFeature( xml.sax.handler.feature_namespaces, True )
    for s in sheets:
    with open(s+".csv","wb") as result:
        handler= GetSheetData(string_handler.string_dict,csv.writer(result))
        rdr.setContentHandler( handler )
        rdr.parse( s )

This iterates through each sheet, transforming it into a simple .CSV
file. Once we have the file in CSV format, it's smaller and simpler.
It can easily be processed by follow-on applications.

The overall loop actually looks like this.

::

    sheets= list( get_worksheets(name) )

    string_handler= GetStrings()
    rdr= xml.sax.make_parser()
    rdr.setContentHandler( string_handler )
    rdr.setFeature( xml.sax.handler.feature_namespaces, True )
    rdr.parse( "xl/sharedStrings.xml" )

    rdr= xml.sax.make_parser()
    rdr.setFeature( xml.sax.handler.feature_namespaces, True )
    for s in sheets:
        with open(s+".csv","wb") as result:
            handler= GetSheetData(string_handler.string_dict,csv.writer(result))
            rdr.setContentHandler( handler )
            rdr.parse( s )

This expands the shared strings and individual sheets. It iterates
through the sheets, using the shared strings, to create a bunch of
.CSV files from the .XLSM data.

The resulting .CSV -- stripped of the XML overheads -- is 80,000+
rows and only 39M. Also, it can be processed with the Python
`csv <http://docs.python.org/library/csv.html>`__ library.

**CSV Processing**

This, after all, was the goal. Read the CSV file and do some useful
work.

::

    def csv_rows(source):
        rdr= csv.reader( source )
        headings = []
        for n, cols in enumerate( rdr ):
           if n < 4:
               if headings:
                   headings = [ (top+' '+nxt).strip() for top, nxt in zip( headings, cols ) ]
               else:
                   headings = cols
               continue
           yield dict(zip(headings,cols))

We locate the four header rows and build labels from the the four
rows of data. Given these big, complex headers, we can then build a
dictionary from each data row. The resulting structure is exactly
like the results of a csv.DictReader, and can be used to do the "real
work" of the application.



-----

You know you could use elementtree to do this ...
-----------------------------------------------------

Tim<noreply@blogger.com>

2010-10-04 11:12:16.217000-04:00

Hi
You know you could use elementtree to do this processing. Elementtree
can do pull style processing see http://effbot.org/zone/element-pull.htm
or use iterparse http://effbot.org/zone/element-iterparse.htm


Umm, good article but...

You state: &quot;Spreads...
-----------------------------------------------------

Paddy3118<noreply@blogger.com>

2010-10-04 18:51:06.258000-04:00

Umm, good article but...

You state: "Spreadsheets are -- BTW -- the universal user interface.
Everyone likes them, they're almost inescapable. And they work."
Unfortunately they don't work. Some auditors such as KPMG say that
around 95% of the spreadsheets they audit have errors. It is
notoriousely difficult to both audit spreadsheets, and to spot
changes/errors.

I would agree that spreadsheets are heavily used, but the error rate
seems to be high, in critical documents submitted in important tax
claims.

See http://staffweb.cms.gre.ac.uk/~cd02/EUSPRIG/


Hi,

Very useful. I didn&#39;t know that I could u...
-----------------------------------------------------

amuhsen<noreply@blogger.com>

2011-12-06 11:23:39.355000-05:00

Hi,
Very useful. I didn't know that I could unzip an excel file :)
One thing i noticed though, the code doesn't write the last column to
the CSV.

you need to change the line in GetSheetData.endElementNS(self, name,
qname):
::

    ...
    ...
    self.writer.writerow( [ self.row.get(i) for i in
        xrange(max(self.row.keys())+1) ] )


Hi,
This is a very useful example of how covert hu...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2012-03-05 10:15:17.216000-05:00

Hi,
This is a very useful example of how covert huge xlsn files to csv using
Sax.
Thanks for sharing.


Quan Ho, you have not got a brain
---------------------------------

Unknown<noreply@blogger.com>

2012-06-20 01:00:59.543000-04:00

Quan Ho, you have not got a brain


Can you convert the code to JavaScript?
---------------------------------------

Quan Ho<noreply@blogger.com>

2012-06-04 11:46:16.764000-04:00

Can you convert the code to JavaScript?





