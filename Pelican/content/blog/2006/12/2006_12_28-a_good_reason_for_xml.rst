A Good Reason for XML
=====================

:date: 2006-12-28 15:39
:tags: technologies,xml
:slug: 2006_12_28-a_good_reason_for_xml
:category: Technologies
:status: published





I harp on
**Design Goal 6**  in the `XML 1.0
Standard <http://www.w3.org/TR/2006/REC-xml-20060816/>`_ , "XML documents should be human-legible and reasonably
clear".  In Kontrawize, the response is XML editors help meet this design goal. 
"There are plenty of good XML-aware editors around, some of which are free." 
While true, I think this violates the spirit of the standard, while adhering
only to the letter of the law.



If we
allow tools to mediate "human-legible and reasonably clear", then too many
things meet this standard.  We could provide a bunch of SQL DDL and DML and
claim that it was a reasonably clear document.  Then, we can also claim that an
MS-Word .DOC file is reasonably clear because we have a copy of
Word.



While it's true that "anything
written in XML is a first class piece of data," I'm not clear on the origin of
the distinction.  "Textual scripting languages are at best second class data." 
I can't discern why -- precisely -- a Domain Specific Language (DSL) or
scripting solution isn't first class.  Presumably, the second class status comes
from one of these origins: 

-   Dependence on a script tool.

-   Parsing ease.

-   XML semantic richness (i.e., how well it
    describes the problem).



It is clear
that dependence on a tool isn't the reason for second-class status: we're
allowed to use tools to make XML legible; we're equally allowed to use tools to
process the XML or script.  What's left are the
**Parsing ease**  and
**Semantic richness**  advantages of
XML.



**Parsing Ease.** 



This is an interesting point.
Especially in light of this posting: "`When do you use XML, again? <http://blogs.tedneward.com/2005/08/22/When+Do+You+Use+XML+Again.aspx>`_ " where the use of
XML was principally for the parsing ease.  This is -- in a way -- a little
silly.  A scripting language has it's own parser, the script interpreter.  So,
ease of parsing isn't a great reason for using XML.  Other DSL's, however, may
require additional software for
parsing.



Python, Ruby (and any other
object-oriented scripting language) has it's own parser, every bit as good as
`Expat <http://expat.sourceforge.net/>`_
or `Xerces <http://xerces.apache.org/>`_ .  And if you choose a free scripting
language, you get the parser and substantial libraries also for free.  For
non-script-based DSL, you don't get a handy
parser.



Here's the bonus for me: my
definition is part of the application.  The definitions aren't
*input* 
to an application which reads, parses, and then performs some functionality
based on the input.   The definitions
*are* 
the application, essentially a specialization of the framework, directly
executable.



**Semantic Depth.** 



Indeed, one of the strong
points of script-based tools is the data structure that describes targets, 
dependencies and actions is often a simple bunch of object creation statements. 
The resulting objects have precisely the same semantics as the XML used by Ant. 
These precisely identical semantics, however, are parsed by Python (or Ruby),
not Expat or Xerces.



I find that a
bunch of Python objects that are are surrogates for other objects makes
compelling sense.  `SCons <http://www.scons.org/>`_  is
appropriate to building things like Java where compiles and jar-ear-war-building
predominates.  Each source is an object, as is each target.  But SCons also
describes static web content where HTML files are built from `Cheetah <http://www.cheetahtemplate.org/>`_
templates.  It also describes a Data Warehouse load where logs and exception
reports are built from source application extracts. 




In short, an SCons script-based
control file has the same semantics as an XML non-script-based control
file.



**What I Learned.** 



The "XML is First Class"
seems to mean that XML has an independent, widely-agreed-to existence, separate
from a language community.  From this I learned that there are a number of
dimensions of comparison:



**Tool Complexity** 

-   XML has moderately high tool complexity. 
    The parsers are already built, but everything else has to be built and some kind
    of relationship with XML worked out.  In short the processing application is a
    kind of interpreter for rules written in XML.

-   DSL has very high tool complexity.  The
    parsers have to be written, and everything else has to be built and some kind of
    relationship with the DSL worked out.

-   Python (or Ruby) has low tool complexity.
    The parser is built, and everything else is just a library, extended by the
    "control"
    file.



**Clarity** 

-   XML has moderately low clarity.  Yes, we
    can use tools, but I think that's a fussy letter of the law interpretation. 
    Compared with Python or a DSL, it's relatively opaque.  However, compared with
    the cryptic binary mumbo-jumbo of many file formats, it's a model of
    readability.

-   DSL has outstanding clarity, since it's
    purpose-designed for clarity. 

-   Python (or Ruby) has good clarity.  Our
    object definitions match the problem domain precisely and a little bit of
    syntactic sugar can lead to a nicely readable control
    file.



**Extensibility** 

-   XML is -- technically -- extensible. 
    However, since we're tied to our application, we have two kinds of extensions.  
    We have to extend our schema or DTD, and extend the processing application. 
    While not all bad, it creates the exact parallel development structure that
    leads to the Subtle Incompatibility Bug: it should work but doesn't
    always.

-   A DSL is also extensible.  However, the
    Tool Complexity consideration slows us down here.  While we'd like to add
    extensions, the parsing complexity is often a barrier to novel
    applications.

-   Python (or Ruby) has the data as
    first-class language constructs.  The control file is actually
    *in* 
    the Python language.  It is -- in a very real sense -- an extension built into
    the
    framework.



**Recommendations.** 



For
my money, the low complexity, good clarity and immediate extensibility of a
scripting solution is an award-winning technology application.  The XML solution
runs a distant second, and a purpose-built DSL has little to offer.  The reason
a purpose-built DSL is dead last is because "clarity" isn't worth much.  As
Kontrawize points out, we can solve the obscurity problem with more tools.  We
can't create extensibility or reduce complexity the same
way.



Between the original "`Stamp
on the ants <http://koti.welho.com/jpakaste/blog/stamp_out_the_ants.html%22%20target=%22NewWindow>`_ " (referencing "`Raven
1.1: Build Java with Ruby <http://www.theserverside.com/news/thread.tss?thread_id=42923%22%20target=%22NewWindow>`_ " thread), and Kontrawize's "`XML is first class, scripting languages are second
class <http://kontrawize.blogs.com/kontrawize/2006/12/xml_is_first_cl.html>`_ " the lessons are similar.

-   **Don't choose XML uncritically** .  It has to be an optimal
    solution to the problems we actually have.  Otherwise, it's just technology, and
    technology can be a barrier between users and their problems.

-   **Don't defend XML uncritically** .  The eight low-value reasons in
    "`XML
    - One Ring to Rule them All... <{filename}/blog/2006/12/2006_12_23-xml_one_ring_to_rule_them_all.rst>`_ " are little more than uncritical
    justification for a decision that seems to have been made somewhere else in the
    organization.  Kontrawize provides a good reason for using XML, but for this
    application domain, I still think I can see some gaps in his logic.

-   **Don't overuse XML** .  As a Data Warehouse hack, I've spent too
    long debating the "XML as our middleware" issue.  XML isn't needed when there is
    a lot of data and the relationships among the application programs is reasonably
    intimate.  In in-house data warehousing, too much XML is just no-value overhead.
    Also, when we need to add extensions -- as we do with any build tool -- XML is
    of limited value.



In one case, more
than one person suggested that we extract 20 million customer accounts in XML. 
The idea was to do the transformation using XSLT to implement a number of
business rules for standardizing data representations.  We could also link
business entities with dimensions, and identify the facts through another series
of XSLT transformations.  Finally, we would load the relational tables from the
XML documents.  Sigh.  All that XML parsing and marshaling will paralyze
processing.  We'll get nothing done -- the heaviest CPU user will be Xalan, and
our disks will be tied up with terabytes of XML source files that create mere
gigabytes of usable database.  























