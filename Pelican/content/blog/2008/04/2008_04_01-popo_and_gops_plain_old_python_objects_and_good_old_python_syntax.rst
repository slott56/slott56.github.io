POPO and GOPS - Plain Old Python Objects and Good Old Python Syntax
===================================================================

:date: 2008-04-01 10:01
:tags: architecture,design,complexity
:slug: 2008_04_01-popo_and_gops_plain_old_python_objects_and_good_old_python_syntax
:category: Architecture & Design
:status: published







Processing XML and X12 messages is a struggle.  You have a number of use cases (I listed a bunch of features in `Synchronicity and Document Object Models <{filename}/blog/2008/03/2008_03_31-synchronicity_and_document_object_models.rst>`_ ).  These can be tackled a number of ways.



What spoils me is the Object Relational Mapping (ORM) in `SQLAlchemy <http://www.sqlalchemy.org/>`_  and the `Django <http://www.djangoproject.com/>`_  ORM layer (among others).  With SQLAlchemy I can create Mapper that bridges between a :strong:`Plain Old Python Object`  and a SQLAlchemy table definition.  The Table definition really SQL with :strong:`Good Old Python Syntax`.



In Django, the two Python and SQL are combined -- a Django table definition is also a POPO.  There are some limitations, but not too many.  Most importantly, navigation may imply additional queries which are handled silently.



When working with X12 and XML messages, I want similar coolness.  I thought I wanted POPO's, until I got a comment leading me to `Atom Models <http://blog.ianbicking.org/2007/08/02/atom-models/>`_ ; that clarified the distinction.



:strong:`POPO`



While using Plain Old Python Objects is a lofty ideal, it isn't always practical.  If we want purely Python objects then we have three-step unmarshalling.



1.  :strong:`Lexical`.  This breaks the source text into tokens.  Either XML constructs like tags and text or X12 constructs like Segments and Elements.



2.  :strong:`Syntactical`.  This assembles meaningful objects from the tokens.  This is either XML elements and attributes (properly nested) or X12 Loops, Segments, Composites and Elements (again, properly nested).



3.  :strong:`POPO`.  This builds the desired POPO objects out of the XML (or X12) structure, through a big-old structure-by-structure mapping.  When you work with tools like the `Java CAPS <http://www.sun.com/software/javaenterprisesystem/javacaps/index.jsp>`_  eDesigner (or `webMethods <http://www.softwareag.com/corporate/products/wm/default.asp>`_ ) you spend a fair amount of time dragging mapping lines from one structure to another structure.



As Ian Bicking points out in the Atom Models, you now have three representations: text, XML and your final POPO.  That's at least one too many.



This is a helpful insight, and it highlights the distinction between POPO and GOPS.



:strong:`GOPS`



Ian's claim is that a better approach is wrapping the syntactical representation in Good Old Python Syntax.  



We have a couple of alternatives here.



1.  Subclass the built-in classes to add the desirable syntax.



2.  Build Bridge/Facades over the the built-in structures.  This allows us to offer GOPS, but this syntax is really a pass-through to the underlying objects.  



There are reasons for both.  Ordinary subclassing, while appealing, may leave you rooting around in things that are Rat Holes of Lost Time.   On the other hand, a Bridge/Facade has a possible disadvantage of leading to rather complex constructors, since the bridge is really a pass-through to some underlying structure.



However, when trying to cope with xml.dom.minidom, a Bridge or Facade makes sense.  It gives us better search than the minidom getElementsByName capability.



:strong:`Aha`



In my case, I've got several toweringly complex XML messages that have to be synthesized.  I don't want to hard code a big puddle of XML text.  In the future, I may get a proper XSD for the message, from which the various elements can be built.  



For now, I don't have XSD or DTD, just a few examples plus an MS-Word .doc with message elements in a big, indented layout.  Creating proper POPO's for this hierarchy isn't too bad.  I have a simple parser that transforms an indented outline into Python class definitions.



Creating a Bridge to XML, similarly, isn't too bad.  It just makes the POPO's a bit more complex.  Each element is a descriptor that contains navigation into the underlying XML.  Creating a message from scratch adds enough complexity that it's a headache.  Either we introspect our POPO's or do additional parsing of the indented layout to create an XML constructor in addition to the Bridge class definitions.



The real win however, will come from upgrading to the 1.3 release of ElementTree, which has more complete XPath support.  The ElementTree find method provides a pleasant, Pythonic encapsulation of the XPath that makes life relatively simple.  Bridges and Facades are no longer desirable.  



The Hierarchy Parser



Here's a way to parse a big block o' text and create a proper XML structure from the content.  Similar algorithms can be used to emit Python class definitions, XML loop structures, etc.



The message is the top-level Element.  The description is simple indented block of text, for example

..  code:

::

    someMsg= """
    HTML
        HEAD
            TITLE
        BODY
            P
            P
    """



..  code:

::

    import xml.etree.ElementTree as dom
    def makeXML( message, description ):
        msg= dom.Element( message )
        indent= [ (-1,msg) ]
        for lineRaw in description.splitlines():
            line= lineRaw.rstrip()
            if len(line) == 0: continue
            tag= line.lstrip()
            spaces = line.find(tag[0])
            prevSpaces, context = indent[-1]
            if spaces < prevSpaces:
                # outdent: pop to matching level, then pop to this level
                while spaces < prevSpaces:
                    indent.pop(-1)
                    prevSpaces, context = indent[-1]
                assert spaces == prevSpaces
            if spaces == prevSpaces:
                # prevailing indent: pop to parent
                indent.pop(-1)
                prevSpaces, context = indent[-1]
                assert spaces > prevSpaces
            # indent: append a child
            new= dom.SubElement( context, tag )
            indent.append( (spaces,new) )
        spaces, topElt = indent[0]
        return dom.ElementTree( topElt )







Now, I'm happy.  I can unmarshall and marshall using ElementTree.  I can manipulate with simple things like ``msg.find("SOME/NESTED/PART").text = "new value"`` .  I can build using the above ``makeXML``  function.




