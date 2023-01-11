What I love about Python == What I hate about the HTML mixed-content model
==========================================================================

:date: 2007-07-03 00:01
:tags: FOSS,open-source
:slug: 2007_07_03-what_i_love_about_python_what_i_hate_about_the_html_mixed_content_model
:category: FOSS
:status: published







The `mixed content <http://www.w3.org/TR/REC-xml/#sec-mixed-content>`_  model, defined succinctly in the XML standards, is pleasant enough for human communication, but leaves a lot to be desired.  For example, mapping a `mixed content model to a relational database <http://www.xml.com/pub/a/2001/05/09/dtdtodbs.html?page target=>`_  is a hard problem.



The problem is made worse when the document is HTML.  HTML doesn't have many constraints to begin with; it mixes structural and presentational markup; unless the content is prepared by a simple piece of software it may be wickedly inconsistent.



Python has the tools to make the problem solvable.  It also has a world-view that facilitates solving the kind of problem where there are wicked little inconsistencies.



Enter Python
--------------



The problem is to scrape the content of some web pages to make a regularly structured database out of the stuff floating around in HTML.  The **Cut, Revise and Paste** ™ (CRAP) technology, while available, is  error-prone and hard to perform repeatably.  



The information is mostly structured:  the interesting content on the page has a <blockquote>, <ul> and <li>'s and the data is easy to see in the <li>'s.  The uninteresting content is in separate <ul>'s and <p>'s making it easy to find.  Unfortunately, each list item appears to have a unique combination of inline tags like <font>, <b>, and <a>, but the underlying text is reasonably regular.



Python's HTMLParser module does a little of what we want.  Sadly, it's SAX-like, meaning that we'll have to heavily customize the parser, writing very complex handle_starttag methods.  



Are there alternatives?



Actually, yes, we have some dynamite alternatives.  First, and most important, we can -- without too much effort -- create a proper `Document Object Model <http://www.w3.org/DOM/>`_  from the HTML.  It's a bit of a stretch to apply XML's DOM to HTML (not XHTML, but plain-old `HTML 3.2 <http://www.w3.org/TR/REC-html32>`_ ) but we can make it work.



Here's the essence of a handler which will assemble a reasonable DOM from HTML.

::

    def top( self ):
        return self.stack[-1]

    def buildNode( self, tag, attrs ):
        n= self.document.createElement( tag, dict(attrs) )
        return n

    def handle_starttag( self, tag, attrs):
        t= self.top()
        n= self.buildNode( tag, attrs )
        # Can't tell if <p>'s or <li>'s are nested or adjacent :-(
        # Need the doctype declaration to distinguish HTML and XHTML
        t.appendChild( n )
        # No content (also called empty) tags that HTML doesn't mark specially
        if tag in ( "br", "hr", "img", "link" ): return 
        self.stack.append( n )

    def handle_startendtag( self, tag, attrs):
        t= self.top()
        n= self.buildNode( tag, attrs )
        t.appendChild( n )

    def handle_endtag(self,tag):
        t= self.top()
        while self.stack.pop(-1).tagName != tag:
            pass

    def handle_data(self,data):
        if self.stack: # Special case to handle leading text
            t= self.top()
        else:
            return # Whitespace before the first tag :-(
        if t.nodeType == xml.dom.Node.DOCUMENT_NODE: return
        n= self.document.createTextNode( data )
        t.appendChild( n )

Note that we elided the <p> and <li> issue: these tags do not need to be closed.  For HTML we need to pop the matching predecessor tag off the stack to avoid nesting needlessly.  For XHTML strict, we don't need to do this.



Here's what's so cool.  In just a hundred lines of code, we've read the URL, parsed the HTML and captured the DOM for the content we need.  We can save the DOM structure, peer at it closely, and determine how best to decompose the content into the data we're looking for.



Here's the really cool part.  We can interact with the structure directly.  We can call methods of the DOM objects, find out how deeply the <ul>'s are nested, and create experimental functions to parse things.  We don't have to spend a lot of time sketching DTD's on the whiteboard, writing parsers, trying to get them to compile, only to find out that one of the <li>'s is inconsistent with the other, leading to a devastating change, rewrite, refactoring, and then a struggle to get it to recompile.



We can quickly knock out another hundred lines of code that expose the relevant data.  Of course, we can cut and paste our sample data fragments into docstrings, giving us a handy unit test capability.



Close but Not A Winner
----------------------



Our DOM-based approach is nice.  The DOM methods for getting elements by tag name and iterating through the child nodes are very pleasant.  However, there are several times when the SAX-based "visitor" approach would be handy.



Specifically, when we've dug down to the correct piece of structural markup, we want to elide the confusing and useless presentation markup.  We'd like to just visit each text node, losing the nesting of the presentation markup.  All the inline <font>, <b>, <i> tags don't convey any meaning; and they're inconsistently used in the content we're scraping.



Additionally, we'd like to get the list of <a> tags, but we don't want any part of the presentation tags in and around these anchors.  



The **Visitor**  design pattern is the backbone of the SAX parser.  In principle, we could do everything from the various handler methods in the SAX-based HTMLParser class.  However, we often want nested visitors: when we've located the appropriate <li> tag, we'd like to switch to another visitor which focuses on the text, skipping all the rest of the inline markup until the matching </li> tag.  



We can do this with a stateful SAX parser, one that has a number of processing alternatives depending on the current tag context.  This grows to become complex as we blend in the **State**  design pattern, especially when we're vague on what states are required.



One of the biggest stumbling blocks is the need to "look ahead" to determine what piece of content we're looking at.  Technically, a SAX-based parser can pass through a number of state transitions to determine if the <p> contains an <a><img> or not.  However, it's simpler to look ahead and recognize the kind of content.



DOM + Visitor
--------------



The XML DOM design doesn't support the **Visitor**  design pattern.  If we extend or replace the module with **Visitor**  support, we can build a more functional parser and analyzer.  We can also add additional search and summary methods to this extended DOM.



Our application will have the following overview.  First, we create a DOM, doing as little as possible.  With almost no effort care, our __repr__ methods will effectively serialize the structure.  Then we use existing methods to get elements by tag name and locate the appropriate structural markup.  Finally, we use several nested visitor objects to examine the content, discarding inline presentation markup gracefully.



Python already has xml.dom and xml.dom.minidom implementations.  Can we extend one of these?  The interface requires us to create our own DOMImplementation and Document class as part of extending an existing implementation.  To make our **Visitor**  design work, we'll need to extend Node, Element, and Text classes, also.



However, we're lazy, and it's not too difficult to create a new, unique, and skinny version of minidom that -- because of Python's `duck typing <http://www.voidspace.org.uk/python/articles/duck_typing.shtml>`_  -- is compatible enough with minidom to get us started.



The necessary DOMImplementation class and associated getDOMImplementation function are obvious.  In Java, it's popular to register an implementation, but in Python, it's easier to provide a tidy replacement that can be brought in via import myDOM as theDOM.



The Node class has a number of attributes with obvious meanings.  The appendChild method maintains the invariant conditions around parentNode, childNodes, firstChild, lastChild, nextSibling and previousSibling.  



The interesting addition is a walk method to apply a visitor to a Node and all of its children.

::

    def walk( self, aVisitor ):
        self.typeCallEnter( aVisitor )
        if aVisitor.stopWalk:
            aVisitor.stopWalk= False
        else:
            for c in self.childNodes:
                c.walk( aVisitor )
            self.typeCallExit( aVisitor )



The other interesting additions are some summarizers.

::

    def summary( self ):
        return [ c.nodeName for c in self.childNodes ]

    def elementSummary( self ):
        return [ c.nodeName for c in self.childNodes if c.nodeType == xml.dom.Node.ELEMENT_NODE ]



Given this, we can now write a relatively simple analyzer.



Gathering HTML Pages
---------------------



The first step is to gather the DOM we want to analyze.

::

    def getDOM( url ):    
        source= urllib2.urlopen(url).read()
        p= HTMLDOM()
        p.feed( source )
        p.close()
        p.document.normalize()
        return p.document
    
    def getDOMBody( url ):
        d= getDOM( url )
        topElt= d.documentElement
        bodyList= topElt.getElementsByTagName("body")
        assert len(bodyList) == 1
        body= bodyList[0]
        return body
    
    def DOMBody2File( sourceURL, destFile ):
        body= getDOMBody( sourceURL )
        dest= file( destFile, "w" )
        print >>dest, repr( body )
        dest.close()


Once we have the DOM in a file, we can explore, tweaking our parser until we understand the inconsistencies and confusions.



Analyzing the DOM
------------------



We can easily write simple functions to get through the page structure.  In this case, for example, the page has a <ul> <blockquote> <ul> structure at the highest level.  Within the top-level <blockquote>, there are several nested <blockquote> before we get to our target content.

::

    def parseBody( body ):    
        bq1= body.getElementsByTagName( "blockquote" )[0]
        bq2= bq1.getElementsByTagName( "blockquote" )[0]
        bq3= bq2.getElementsByTagName( "blockquote" )[0]
        bq4= bq3.getElementsByTagName( "blockquote" )[0]
        return bq4



Once we have narrowed the focus to the correct part of the overall page, we can use a **Visitor**  to examine each individual tag within this part of the page.  This visitor will accumulate the target data elements.  When the visitor has finished, it will have a sequence of objects, all ready for storage in an RDBMS using SQLAlchemy or something similar.



Here's the analyzer method.

::
    
    def parseBQ4( bq4 ):
        v= ListVisitor()
        bq4.walk( v )
        for m in v.finalList:
            print m # or SQLAlchemy insert or CVS write
    
    

Here's the top-level Visitor.

::

    class ListVisitor( DOMVisitor ):    
        def __init__( self ):
            DOMVisitor.__init__( self )
            self.dim= None
            self. finalList = []
    
        def elementEnter( self, anElement ):
            if anElement.tagName == "p":
                if anElement.elementSummary() == [ "a", "img", "b" ]:
                    pass
                else:
                    tv= TextVisitor()
                    anElement.walk( tv )
                    self.dim= Dimension( tv.textNodes )
                    self.cut()
            elif anElement.tagName == "ul":
                pass
            elif anElement.tagName == "li":
                tv= TextVisitor()
                anElement.walk( tv )
                av= SearchVisitor( "a" )
                anElement.walk( av )
                new= TargetObject( self.dim, tv.textNodes, av.matches )
                self.finalList.append( new )
                self.cut()
           else:
                print "skipping", anElement



This uses the summary method to look ahead in a <p> tag.  Some <p> tags are useless indexing information.  Other <p> tags are interesting content which we need to parse.  We gracefully pass over the <ul>'s which introduce lists of relevant content.  We apply two other Visitors to the content within a <li>: One accumulates the text, the other accumulates the anchors.



We delegate some of the parsing to our Dimension and TargetObject methods.  The Dimension constructor will receive a simple list of strings.  The TargetObject constructor will get a list of strings and a list of Elements from which it can extract the details using simple Python string operations.



Two Other Visitors
------------------



Here's a Visitor that will pull out non-empty text nodes and ignore inline markup.  The resulting list of strings has a very regular structure, even though though the original HTML was interspersed with random inline markup and <br> tags.

::

    class TextVisitor( DOMVisitor ):    
        def __init__( self ):
            DOMVisitor.__init__( self )
            self.textNodes= []
        def text( self, aText ):
            if aText.nodeValue.strip():
                self.textNodes.append( aText.nodeValue.strip() )



Here's a Visitor which does a deep search for a given tag.

::
    
    class SearchVisitor( DOMVisitor ):    
        def __init__( self, target ):
            DOMVisitor.__init__( self )
            self.target= target
            self.matches= []
        def elementEnter( self, anElement ):
            if anElement.nodeName == self.target:
                self.matches.append( anElement )
    


Conclusion
----------



The essence of scraping HTML involves a number of operations, and Python helps us a number of ways.



-   To get the page Python provides several variations on urllib.

-   To parse the page, Python offers HTMLParse.  We can combine that with xml.dom and xml.dom.minidom to easily produce a data structure. 



More importantly, however, Python helps us by facilitating exploration.  We can use Python interactively to peer at the resulting DOM structure.  Better yet, we can extend, rewrite or replace modules to add functionality.



In this case, we started out with the built-in xml.dom.minidom, validated some parts of our application in just a hundred lines of code and only a few hours of time.  We then replaced minidom with our own home-brewed microdom, confident that it would work because it was factored into a working application.  This is only a few hours of effort.



Once we had a working DOM structure with the Visitor capability, we could experiment with a number of Visitor alternatives in the space of a few more hours.  Without a significant investment in time, we have a working application.



I've omitted the epydoc comments and the unittest TestCase files.  The unit testing served to validate the essential algorithms, and support refactoring.  Since this was exploratory programming, everything was refactored heavily to arrive at a coherent, usable application.





