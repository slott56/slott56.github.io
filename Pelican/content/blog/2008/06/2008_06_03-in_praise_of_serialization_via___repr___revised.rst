In Praise of Serialization via __repr__ (Revised)
=================================================

:date: 2008-06-03 09:50
:tags: architecture,design,data structure,algorithm
:slug: 2008_06_03-in_praise_of_serialization_via___repr___revised
:category: Architecture & Design
:status: published







The problem is this: parsing HTML from a variety of sources to create pleasant, easy-to-manipulate spreadsheets.  HTML can represent the same data in a variety of ways, even within a single web site.  What we have are several layers of parsing; layers which must be linked with increasingly simplified intermediate representations.



The initial HTML lexical scanning and parsing gives us the Document Object Model (DOM) objects.  Mostly, these are elements and attributes that uncover the fine-grained structure of the original document.  Sadly, this level of detail is not something we can make direct use of.



Here's where Python is toweringly cool.



The issue is this: parsing one page all the way to the final spreadsheet will not provide a general solution.  Indeed, it can barely be made to work.  The obvious algorithm for creating the spreadsheet from the HTML doesn't even work for some rows in the table on the first page we examined.  Moving to another page on the same site reveals more and more HTML "errors" and oddities.  



[**HTML Note**.  Some HTML syntax errors aren't really errors, they're an artifact of the SGML legacy; that doesn't make them any easier to parse.  Worse, the presence of errors is compounded by **Rule One of the Browser**: All HTML Gets Rendered No Matter How Malformed.  Because of Rule One, HTML can be crap and the QA folks just nod and say "it displays OK".]



Once we've figured out the content of the page, we can extract it, parse it and use it all we want.  In some cases, the data is historical, and one-time parsing as all we need.  In other cases, however, getting a page of HTML is -- currently -- the way some particular web service is implemented.  Some organizations offer some data in HTML only.



What do to?  



One solution is to try and use `Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`_  to get past the HTML errors.  While this is helpful, it doesn't get past the irregularities in the way HTML was used by the author.


The Pipeline
-------------



The trick is to do what compilers do: create a pipeline of intermediate representations.  Stage one is a transformation from HTML to DOM objects (Document, Element and Attribute).  This is (relatively) easy, and any of the available parsers can do this nicely.



I'm picky, however, and I like to have first-class support for the `Visitor <http://exciton.cs.rice.edu/javaresources/DesignPatterns/VisitorPattern.htm>`_  design pattern.  The built-in Python `xml.com <http://www.python.org/doc/current/lib/module-xml.dom.html>`_  library doesn't have this.  So, I built my own version of `xml.dom.minidom <http://www.python.org/doc/current/lib/module-xml.dom.minidom.html>`_  with proper Visitor support.



And one additional feature: a nice __repr__ that will serialize the entire Document as a proper Python expression.   You wind up with a file that looks like this:

::

    Element( 'body', {'alink': '#000080', 'text': '#000000', 'bgcolor': '#FFFFFF', 'link': '#0080C0', 'background': 'sitebck7.gif', 'vlink': '#808080'}, *[Text( '\r\n\r\n' )
    , Element( 'ul', {}, *[Text( '\r\n' )
    , Element( 'ul', {}, *[Text( '\r\n' )
    , Element( 'ul', {}, *[Text( '\r\n' )
    , Element( 'ul', {}, *[Text( '\r\n' )
    , Element( 'center', {}, *[Element( 'p', {}, *[Element( 'img', {'src': 'top2sml.gif', 'alt': '...some text...', 'width': '406', 'height': '77'}, *[] )
    ] )
    ] )
    , Text( '\r\n\r\n' )
    , Element( 'center', {}, *[Element( 'p', {}, *[Element( 'b', {}, *[Element( 'font', {'color': '#000052', 'size': '3', 'face': 'Arial'}, *[Text( 'SOME TITLE' )
    , Element( 'br', {}, *[] )
    etc.





While bulky, this is a lot easier to work with than the output from `pickle <http://docs.python.org/lib/module-pickle.html>`_ .  And it's first-class Python, allowing us to explore with it.



[**Scalability Note**.  There are limitations to this.  Truly huge expressions will break the Python parser.  Your mileage may vary.  You may need to break giant documents into logical pieces and assemble the pieces. You may have something like p1= ...; p2= ...; p *n* = ...; doc = [ p1, p2, ..., p *n*  ] to manage bigness.]



Once we've explored, we can write our stage two parser which actually works reliably and handles all of the special cases properly.


Stage Two
----------



The second stage of the pipeline can work from Python source.  Rather than write more parsing and loading functions, stage two starts with the following:

::

    dom1= eval( file("stage1.out","r").read() )





Yes, we've deserialized the output from stage 1 with a simple call to eval().  



Turns out, this is very, very handy for "exploring" the data structure.  We can also import the structure into interactive Python and play around with it at the command prompt.



This stage can focus on filtering and building up the next representation, one that is less like a document and more like objects in the problem domain.  We have to be a little cautious how we create those problem domain objects, however.



The domain model is the thing we wanted in the first place.  The two-stage parser was how we could get to this point.



Dimensional Model
-----------------



While the problem domain objects are (usually) pretty obvious from the organization of the content in the HTML pages, the issue is to avoid naively assembling objects without thinking about the organization of the inputs.



In many cases, the web content we're parsing is a dimensional (or `star schema <http://en.wikipedia.org/wiki/Star_schema>`_ ) view of the data.  You'll be building several kinds of objects:



**Dimensional Entities**.
    Dimensional entities are the "descriptions" of each dimension.  Dimensions include the obvious time and space (geography), but can also include demographic groupings, economic groups (SIC codes), etc.



**Facts**.
    Facts are measures (with units) that can be categorized  by the dimensions to which they belong.



When you look at displayed information, you'll often see titles or headings that define specific dimensional entities.  "Northeast Region", "January 2006", "Hourly Employees", "Retail", and the like are examples of dimensional entities.  These are objects in one of the (many) dimension classes.



Each measurable fact object will be associated with one or more dimensional objects.



Stage two builds the dimensional model objects from the DOM objects.  (The DOM objects were built from HTML.)



Stage Three
------------



The final bit of processing is to unify the HTML pages into a single star-schema model for analysis and reporting.  Generally, the Stage 2 outputs will be a bunch of collections.  Most of the collections will be dimension definitions, the remaining collection is a sequence of facts.



Each dimension is collected into a mapping from the unique identifier for a dimension entity to the other attributes we know about the entity.  For instance, "January 2006" might be the identifier, but we know several other attributes of this entity:  the year is 2006, the month is January, it's in the first quarter.



The facts are a simple sequence (list or tuple) of measures with references to the dimension entities.



It's appealing to simply serialize the fact table with __repr__.  This isn't the best approach, however.  Generally, a large number of facts will have references to a common dimension value.  If we simply serialize the facts with something like the following, we'll have a lot of redundancy.

::

    def __repr__( self ):
            return "Fact( %r, %r, %r, %f, %d)" % (
                self.dim1, self.dim2, self.dim3, self.measure1, self.measure2 )





It's slightly smoother to provide just the unique object ID's for each dimensional entity, and rebuild the required structure at eval time.



Our facts are represented in the stage three input as follows.  Rather than include the entire dimension object, we include a dictionary lookup to locate a reference to the dimension entity.




::

    time = { 'January 2006': Time( "January 2006", 2006, 1, 1 ), ... }
    space = { 'Northeast': Geography( "Northeast", "US", "EN" ), ... }
    demo = { 'Full-Time': Demographic("Full-Time"), ... }
    facts = [
        Fact( time['January 2006'], space['Northeast'], demo['Full-Time'], 3.14, 42 ),
        ...
        ]






These files are quite easy to unify.  We can import each file and merge the dimensions to develop the complete set of entities in each dimension.  Once the dimensions are unified, we can do a simple append of all the facts.  This model can be used to write reports or populate a datamart or whatever our goal was when we started down this road.




The real power comes from using the `Inverted Index <http://en.wikipedia.org/wiki/Inverted_index>`_  technique of having each dimension entity reference the set of facts associated with that entity.  This is done by having the __init__ of a Fact register itself with the various dimensions.




::

    class Fact( object ):
        def __init__( self, time, space, demo, m1, m2 ):
            self.time= time
            self.time.addFact( self )
            etc.





Staging Our Analysis



Stage 1 transforms HTML to a Python model of the document. This is very, very cool, and supports easy exploration of the Python version of the document to find algorithms for parsing the structure.



Stage 2 transforms the Python document model into a Python dimensional model, emitting a mapping for each dimension and a sequence for the facts. 



Stage 3 merges the dimensional model values into a single datamart that we can then use for analysis.  The resulting datamart is the same dimensional model from Stage 2.



The remaining work is (usually) involves locating all facts with a particular dimension value and producing the expected reports.

::

    q1Total= 0
    for q in [ t for t in time.values() where t.quarter == 1 ]:
        for f in t.facts:
            q1Total += f.m1





This dimensional model gives us all of the analytical capabilities we might want.  



The best part is that each step uses Python notation, making it easy to visualize and easy to experiment with the data looking for the unifying patterns.




