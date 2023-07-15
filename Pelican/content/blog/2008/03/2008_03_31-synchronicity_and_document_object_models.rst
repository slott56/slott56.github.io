Synchronicity and Document Object Models
=========================================

:date: 2008-03-31 15:32
:tags: architecture,software design,data structure,algorithm,xml,edi,x12
:slug: 2008_03_31-synchronicity_and_document_object_models
:category: Architecture & Design
:status: published









Message-oriented applications involve an interface defined around messages (or documents).  I've been working on applications that involve a fair amount of manipulation of XML and X12.  Recently I started yet another, and started to recognize the essential design patterns.



There are four use cases.  The first two use cases define the interface: marshall and unmarshall.  The third and fourth use cases are building and manipulating the internal objects, separate from any XML (or X12) considerations.  



The problem recently gave me brain cramps because I wanted something a bit more general than my last (ad-hoc) go-around.



These Use Cases are written from the viewpoint of the Plain Old Python Objects (POPO) application.  While my inbound and outbound interface is XML (or X12), I don't want a program full of text manipulation.  I want to unmarshall the input text into a POPO, work with that POPO and marshall the output as text.



Use Case 1: Marshall
--------------------



The first use case is the easy one: Marshalling.  We want a POPO to marshall itself into an XML (or X12 message).



Use Case 2: Unmarshall (or parse)
----------------------------------



While this is solved by SAX, expat, xml.dom.minidom and xml.etree, there are some distinctions that are important.  The "event-based" parsing of SAX or expat is only part of the use case.  The more important part is the creation of a resulting document object that can be used for further processing.



This document is easiest to work with if it's built of POPO's.  The "manipulation" use case, below, depends on simple, elegant Python syntax.  



Use Case 3: Build
------------------



In additional to receiving XML documents that encode POPO objects, we also need to build POPO objects "from scratch" in Python programs.  The point of POPO's is to have ordinary Python constructors building a complex object that can be manipulated and marshalled as XML.





Use Case 4: POPO Manipulation
-----------------------------



I want to be able to say things like ``msg.LOOP1.DTP.DTP02= "20080330"``



The Python "." is much, much cleaner than the rather complex search references required by the xml.dom structures. 



However, this isn't the only construct I'd like.  Many XML (and X12) constructs can repeat, so we need to use the "[]" or insert a number in the "." path.



XPath is not particularly pleasant for this, since it is not very Pythonic.  [XPath is a useful model, however, because the navigation axes can serve as a template for method design.] 



Solutions
----------



There are a number of solutions, most of them icky.



1.  ``xml.dom.minidom``.  I liked this, right up until yesterday, when I read` Python HTML Parser Performance <http://blog.ianbicking.org/2008/03/30/python-html-parser-performance/>`_ .  It wasn't the "performance" topic that caught my attention, it was the "I do not recommend using minidom for anything" quote that stopped me cold.

#.  A kind of **Bridge**  to create usable POPO's which are a Bridge to the xml.dom model implemented in minidom.  This isn't a pure Bridge, but a kind of `Bridge <http://en.wikipedia.org/wiki/Bridge_pattern>`_ -meets-`Facade <http://en.wikipedia.org/wiki/Fa%C3%A7ade_pattern>`_ .

#.  Custom POPO's.  This requires parsing using a custom (but not too complex) SAX ContentHandler and a simple XML marshaller method of each POPO class.

#.  ``ElementTree``.  This was new to me.



The ``minidom`` solution has two use cases nailed -- marshall and unmarshall fit nicely.  Building doesn't work out so well because the ``document.createElement`` construction is very clunky.  Manipulation is also a pain in the neck because the navigation capabilities are limited.



The "Bridge to A Footing" is something I'd used recently.  In that case, the footing wasn't ``minidom``, but was a low-level representation of X12 messages.  Extending it, however, showed some profound limitations in my original design.



The idea is that each attribute of a Bridge class is implemented as a Python descriptor.  The descriptor's  __get__ method implements the requisite search.  Marshall, Unmarshall and Manipulation are really quite nice.  Building, however, gets complicated.  Mostly because we still have to build the underlying minidom representation from Bridge objects that are heavily biased toward search.



Custom POPO's work out moderately well.  The Python classes parallel the XSD's or DTD's or SEF's of the original message structure.  This isn't always ideal, however, since we have to define every single tag in a complex message structure.  For large X12 messages, this is a LOT of definitions of elements that simply pass through our application.  Its much nicer to have generic definitions (like minidom) that define the bulk of the data and a Bridge that applies to the useful parts.



The Element Tree Solution
--------------------------



Element Tree is new with Python 2.5 and corrects many problems with xml.dom.minidom.  Principally, ElementTree is Pythonic, not a rehash of a Java design.



The Marshall and Unmarshall use cases work out reasonably well.  I have a beef with ElementTree.write, since that always creates a file.  But, I worked around it with:

::

    def toXML( etree ):
        buffer= StringIO.StringIO()
        etree.write( buffer )
        txt= buffer.getvalue()
        buffer.close()
        return txt





Really, I should subclass ``ElementTree`` and incorporate this into it.



Building an Element Tree isn't too bad.  The Element and SubElement constructors are easy enough to use.  The text attribute (missing from the documentation) helps set text values of tags without fuss or complexity.



Manipulating, similarly, isn't awful.  The (currently undocumented) ElementPath module provides a "name/name" XPath-like search functionality.  However, the way that the ElementPath (or _SimpleElementPath) plug into the overall structure of the find method shows how to build more sophisticated versions of ElementPath that handle more complex XPath search axes.  The nasty part of this is parsing the `XPath notation <http://www.w3.org/TR/xpath>`_  itself.



[Specifically, abbreviated notation, which limits searches to the child axis.  The "[*n*]" index construct and "[@ *attr* = *value*]" constructs are the most useful.]



I'd like to write message.loop1.dtp, but I'm willing to settle for message.find("loop1/dtp").



Thanks
--------



No one knew I was having a problem with manipulating complex XML and X12 messages.  But the answer just sort of dropped into my lap by virtual of some cosmic synchronicity.  Or maybe chance favors the prepared mind.




