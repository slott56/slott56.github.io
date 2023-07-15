Spreadsheet as Syntax
=====================

:date: 2007-01-25 16:11
:tags: architecture,software design,data structure,algorithm,spreadsheet
:slug: 2007_01_25-spreadsheet_as_syntax
:category: Architecture & Design
:status: published





If we look at a spreadsheet as a document we can
develop a parser that locates the user-supplied information in that document. 
Like any language, we'll have to treat some elements of the spreadsheet as pure
syntax, little more than punctuation.  In the case of embedded formulas, these
are elaborate punctuation that is an important part of overall usability. 




We'll look at parsing an XML version
of a spreadsheet, since that is a delightfully simple exercise in Python. 
Looking back at "The Problem with Spreadsheets", we're looking at simplifying
some of the business processes, and saving the spreadsheets as XML files so that
we can write application programs to extract meaningful information from the
spreadsheets.



Generally, parsing
happens at two levels: `lexical analysis <http://en.wikipedia.org/wiki/Lexical_analysis>`_  and `syntax
analysis <http://en.wikipedia.org/wiki/Parsing>`_ .  A lexical scanner will break the stream of input characters
into discrete tokens.  The syntax analysis looks at the stream of tokens to
create a usable representation, often called an `abstract syntax tree <http://en.wikipedia.org/wiki/Abstract_syntax_tree>`_
(AST).



**Layers of Meaning.** 



Compounding the essential
parsing problem are the number of layers of syntax that we have to work
with:

-   XML.  XML lexical analysis locates tags,
    and punctuation, building up a document object model of Nodes, Elements and
    Attributes.

-   Spreadsheet.  The spreadsheet analysis
    interprets the XML nodes are parts of a Workbook, with Worksheets, Rows and
    Cells.

-   Business Process Objects.  What we
    observe in the spreadsheet is really an implementation of some essential
    business process.  There are business objects which have been written down in
    the cells of the spreadsheet.  The mapping from business entity to spreadsheet
    representation is sometimes haphazard.  The objects we find in the spreadsheet
    rows and cells are something we'll call Business Process Objects.  They aren't
    the real essence of the processing, they're just one possible implementation.


-   Essential Business Entities.  These are
    the fundamental business entities that we are really interested in.  These are
    plans for selling or making product, commitments from vendors, prospective
    customers, financial arrangements, etc.  These get encoded in a number of forms,
    one of which is Business Process Objects in a spreadsheet. 




Since there are multiple levels of
meaning, there are multiple abstract syntax trees that we will be developing. 
In essence we work from the bottom up, accreting information to create the
essential business entities.  Our SAX parser will examine the XML syntax.  We
can use a generic Document Object Model (DOM) for the XML
structure.



We can traverse the DOM to
uncover spreadsheet objects.  We can traverse the spreadsheet objects to uncover
the Business Process Objects (BPO).   Typically, we can optimize some of these
traversal steps and locate the BPO's while traversing the DOM.  The essential
business entities, however, can present a more complex problem.  Business
Entities often exist as dimensions in a star schema, leading us toward
conforming the BPO's into a data warehouse for analysis
purposes.



**Basic SAX Parsing.** 



The Python SAX and DOM
libraries can be used to build a complete DOM from an XML document.  For our
purposes, we'll elide some features which aren't a common part of parsing
spreadsheets.  This
xml.sax.ContentHandler
does the minimal work required to create a DOM structure that contains our
spreadsheet XML.  We'll have to do more to make sense of this DOM
structure.



::

    import xml.sax, xml.dom.minidom
    
    class DOMContentHandler( xml.sax.ContentHandler ):
        """A SAX ContentHandler which creates a simple DOM object."""
        def __init__( self ):
            """Initialize this handler."""
            self.dom= xml.dom.minidom.getDOMImplementation()
            self.document= self.dom.createDocument(None,None,None)
            self.context= [ self.document ]
        def startElement( self, name, attrs ):
            """Starts a new Element, pushing this onto the stack."""
            new= self.document.createElement( name )
            for k,v in attrs.items():
                new.setAttribute( k, v )
            self.context[-1].appendChild( new )
            self.context.append( new )
        def endElement( self, name ):
            """Ends an Element, popping the matching Element off the stack."""
            while self.context[-1].nodeName  != name:
                self.context.pop( -1 )
            self.context.pop(-1)
        def characters( self, content ):
            """Captures characters, creating a Text Node."""
            new= self.document.createTextNode( content )
            self.context[-1].appendChild( new )
        def getDocument( self ):
            """Returns the DOM object."""
            return self.document





To use this
DOMContentHandler
we have to create a SAX parser and initiate
parsing on an input source.  Note that this creates a generic DOM object, which
we have to examine to locate the spreadsheet
structure.



::

    class XMLParser( FileParser ):
        """SAX2 parsing of entire DOM."""
        def __init__( self, aFile ):
            """Initialize parsing a given XML file which contains a SpreadSheet."""
            FileParser.__init__( self, aFile )
            handler= DOMContentHandler()
            myReader= xml.sax.parse( self.file, handler )
            self.xmlDoc= handler.getDocument()





**The Spreadsheet Object Model (SSOM)** 



The low-level DOM structure
is a large collection of Element and Text Nodes with Attribute values.   It's
much more pleasant to work with proper Worksheet, Row and Cell objects.  We can
condense the DOM into something more usable through a fairly simple algorithm
that makes good use of Python's
generators.



First, we'll need class
definitions for the various spreadsheet entities we're going to deal
with:

-   Style.  The spreadsheet style
    information is spread through a number of tags and attributes.  Most of the tag
    values are single-occurence elements and the list-oriented
    getElementsByTagName()
    and
    getAttribute()
    aren't the most convenient API. 

-   **Workbook** .  The Workbook is a collection of
    Styles, Names, and "SupBook" references to external files.  It is also a
    collection of Worksheets.

-   **WorkbookLink** .  This is the Path information of
    a "SupBook" reference in a Workbook.

-   **Worksheet** .  A Worksheet is essentially a
    container for Rows.  It can also be looked at as a container for columns, but we
    won't often need to make use of this representation.  Unlike the pure XML model,
    which is row-oriented, our spreadsheet object model can include additional
    indexing.

-   **Row** .  A Row is a container for
    Cells.

-   **Cell** .  A Cell has a number of attributes:
    data, an optional formula, and an optional style.  We'll need these to parse the
    spreadsheet document.  We can safely ignore any other attributes of a
    cell.

-   **WorksheetReference** .  This is an reference
    embedded in a formula.  These references are usually a subset of the "SubBook"
    references.



Most of these class
definitions are relatively simple.  They are containers with basic accessor
methods to put and get specific components.  A Workbook, for example, uses a
number of dictionaries to keep Names, Styles and Worksheets.  A Row is little
more than a simple list of
Cells.



However, since these are formal
containers, the accessors create a very convenient API for accessing spreadsheet
structure.  Rather than a complex XPATH expression to locate a given cell of a
given row of a given sheet, we can provide a pleasant method in the Workbook
class to locate the Sheet, delegating the row and cell lookup.  Within Worksheet
we can locate the requested Row, and within Row we locate the requested
Cell.



**Generating SSOM Objects.** 



We can handle the creation
of SSOM objects via Python generators.  Here's a method that yields the
top-level Worksheet instances.  It also assures that each Worksheet is properly
contained in the parent Workbook. 



::

    def nextSheet( self ):
            """Generator which yields the next, empty L{Worksheet}."""
            wsList= self.xmlDoc.getElementsByTagName("Worksheet")
            for ws in wsList:
                self.currentWS= ws
                name= ws.getAttribute( "ss:Name" )
                self.sheet= Worksheet( name )
                self.document.addSheet( self.sheet )
                yield self.sheet





Our final application can use this
method something like the following.  This snippet looks for worksheets named
"Assumptions", and examines only those pages of a
Workbook.



::

    parse= ssDOM.XMLParser( file(aFile,'r') )
        doc= parse.getWorkbook()
        for ws in parse.nextSheet():
            if ws.name != "Assumptions":
                continue
            print ws





Generating the Rows (and Cells) is
somewhat more complex because of the very rich information content in an
individual Cell.  However, the essential processing is pretty straightforward. 
We need to collect all the Cells within a row, along with any style or comments
associated with the Cell.  Then we bundle it into a SSDOM object that we can
work with in our next level of parsing.



::

    def nextRow( self ):
            """Generator which yields a complete L{Row}."""
            for table in self.currentWS.getElementsByTagName("Table"):
                self.rowNumber= 0
                for row in table.getElementsByTagName("Row"):
                    aRow= Row()
                    for cell in row.getElementsByTagName("Cell"):
                        styleID= cell.getAttribute( "ss:StyleID" )
                        index= cell.getAttribute( "ss:Index" )
                        formula= cell.getAttribute( "ss:Formula" )
                        data = cell.getElementsByTagName("Data")+cell.getElementsByTagName("ss:Data")
                        ... some thrashing omitted ...
                        aRow.addCell( Cell(text,formula,style) )
                    self.sheet.addRow( aRow )
                    yield aRow
                    self.rowNumber += 1





**Business Process Objects.** 



Once we've got Rows, Cells
and Worksheets, we can then do useful analysis of the resulting spreadsheet to
locate the user's inputs.  As one example, we'll peel the assumptions off the
assumptions worksheet in the
workbook.



In the following case, we're
only looking at the Worksheet named assumptions.  The worksheet contains a
formula which repeats some identifying information on this worksheet.  We'll
need that to establish some business context for the following
data.



The rows of the sheet have some
instructions and examples, which we have to skip.  Once we get to the "Summary
P&amp;L Assumptions" cell, everything below that will be user-entered
Assumptions.  The interesting part of the parsing is recognizing headings for
areas that group the assumptions assumptions and the detailed assumptions within
an area.  The headings for an area have a style that involves a color plus a
single underline.  Unlike parsing text, where we simply compare strings, here we
have to compare one attribute of a cell's style to see if the cell has special
meaning.



::

    for ws in parse.nextSheet():
            if ws.name != "Assumptions":
                continue
            print ws
            rowIter= parse.nextRow()
            for row in rowIter:
                if row[0].formula == u"='Summary PNL LC'!RC":
                    print "Title:", row[0].data
                if row[0].data == u"Summary P&L; Assumptions":
                    # Keep rows after the assumptions header.
                    break
            area= ""        
            for row in rowIter:
                if row[0].data.startswith( u"Examples " ):
                    continue
                if len(row) == 0 or len(row[0].data) == 0:
                    continue
                if len(row) == 1 and row[0].style.fontUnderline == u"Single":
                    area= row[0].data
                else:
                    txt= "; ".join( [ c.data for c in row if c.data ] )
                    a= Assumption( area, txt, w_fk )
                    print a





Since iterators maintain state, we can
use the iterator to implement a very clean
**Skip The Headers**  design pattern.  The first
"for row in
rowIter" loop will process rows until we find the
last of the "overhead" rows.  The second "for
row in rowIter" loop will process the remaining
rows; we skip blank rows and rows that contain
examples.



**Essential Business Entities.** 



Our Business Process
Object may be the essential business entity or it may only be selected
attributes of a more complex entity.  In this case, the Assumption object that
we parsed is just a puddle of text, and not very interesting.  It is, however, a
label on a more complete business model, which pervades the
spreadsheet.



By accumulating the
individual BPO's, we can accrete enough information to reconstruct the business
model which is implemented as a spreadsheet.   Extracting the parameters from
this model is the heart of what our spreadsheet parser is doing.


















