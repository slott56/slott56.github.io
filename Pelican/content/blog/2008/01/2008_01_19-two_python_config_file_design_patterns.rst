Two Python Config-File Design Patterns
======================================

:date: 2008-01-19 13:23
:tags: architecture,design,data structure,algorithm
:slug: 2008_01_19-two_python_config_file_design_patterns
:category: Architecture & Design
:status: published







I hate to complain, but there's a Python syntax rule that has slightly cramped my style.  The problem stems from a need to describe a really complex and extensible structure.



We need to describe X12N messages, which have a rather complex structure, and the structure can be customized.  While the core syntax is pretty simple, you need your business partner's Implementation Guide (IG) to make sense of the data.  



Most IG's are a big table-like document, but aren't properly distributed as a tidy, easy-to-work with table.  [BTW, The documents are usually published as PDF files for two reasons.  One, lawyers understand a file that is hard to edit and don't understand an MD5 digest to show tampering.  Second, X12 parsing seems to be considered a proprietary feature of an application.]



Open-Source X12 Parsers
-----------------------



In `Python as Config Language -- Forget XML and INI Files <{filename}/blog/2008/01/2008_01_12-python_as_config_language_forget_xml_and_ini_files.rst>`_
I mentioned my quest for X12 parsers.  The embarrassing part was that I totally missed one.   On my own, I found a Perl program on CPAN to do `X12 parsing <http://search.cpan.org/~prasad/X12-0.08/lib/X12/Parser.pm>`_ .  The program itself isn't useful, but the configuration files are basically a summary of an IG.  As INI files.



Then one of my co-workers asked if I'd seen the `Python X12 <http://pyx12.sourceforge.net/>`_  parser.  I'm a Python bigot, and totally missed this.  [Thanks, Vinny.]  As with the Perl example, the parsing code isn't terribly useful, since it is too complex.  However, the configuration files are a very useful unwinding of an IG.  As XML files.



A More Useful Configuration
---------------------------



The INI-file version of the IG makes some potentially invalid assumptions about message structure.  Specifically, each X12 Loop is defined as starting with a series of Segments and ending with a series of Loops.  Nesting -- in the form of header Segments, Loops and trailer Segments -- isn't tolerated.



The XML-file version of the IG -- while more descriptive -- creates a needless level of indirection.  First, we have to build a usable Python structure from the XML.  Then, we use that Python structure to parse the messages.  Further, we have to do this two-pass parsing for each batch of messages we're going to process.



The structure is readily defined by a few Python classes.




::

    class Parser( object ):
        """Superclass for all parsing components."""
    class Element( Parser ):
        """A single Element within a Segment."""
    class Composite( Element ):
        """A composite Element within a Segment contains Elements."""
    class Segment( Parser ):
        """"A collection of Elements and Composites.
    class Loop( Parser ):
        """A collection of Segments and Loops."""
    class Message( Loop ):
        """A collection of Loops."""






With this structure, we can define messages in a relatively pleasant way.  Except for a Python syntax rule that leads to a small bit of ickyness. 




The Structural Declaration Pattern
-----------------------------------




Here's the **Structural Declaration**  that I settled on.  This can be built from the Perl .CF files or the Python X12 XML files.  Then it can be customized to match the business partner's Implementation Guide.  [Ideally, it would be build directly from an IG; where the IG is based on a usable spreadsheet -- hopefully in `Open Office XML <http://xml.openoffice.org/>`_ .  Often, Micro$oft Office files can be saved in an open format.]




This example only names the various Segments without providing the Element-by-Element definitions.  That gets rather long, and isn't always necessary.  Even so, the full 278 message is about 120 lines of code.




::

    x278 = Message(
        "278", "Referral Request/Response",
        Loop( "ISA", "ISA", "R", "1",
            Segment("ISA"),
            Loop( "GS", "GS", "R", "1",
                Segment("GS"),
                Loop( "ST","ST","R","1",
                    Segment("ST",(1,"278"),"Transaction Set Header","R",1),
                    Segment("BHT",None,"Beginning of Hierarchical Transaction","R",1),
                    loop2000A, loop2000B, loop2000C, loop2000D, loop2000E, loop2000F,
                ),
                Loop( "SE","SE","R","1",
                    Segment("SE")
                ),
            ),
            Loop( "GE","GE","R","1",
                Segment("GE")
            )
        ),
        Loop( "IEA", "IEA", "R", "1", 
            Segment("IEA") 
        ),
    )






Each of the loop2000x variables is a moderately complex Loop definition.  Ultimately, these will become database tables, but that's another complicated piece of design.




This is much more expressive than the .INI files.  It is also considerably easier to read and work with than the XML files.  As cool as it is, this isn't *precisely*  what I was looking for.




Evolving of the API
-------------------




When we look at the resulting parser description -- even for a Segment-level overview of a simple 278 message -- we have some obscurities that crop up.  In particular, we have some evolution management problems.




First, each Loop and Segment has both descriptive information and a complex structure. This extra information include a description, required/situational flags, repeat limits, and any helpful information required to disentangle the Loop structure from a message that is just a flat sequence of Segments.




Second, we can't easily evolve our meta-metadata model.  If we want to add parameters to Loop or Segment, we run the risk of invalidating all message parsers previously built and manually tweaked.




We have two opposing forces.  I want a simple declaration but I also want extensibility.  The simplest declaration is a flat list of parameters.  It has the form:





::

    def __init__( self, name, *loops ):
            """Build a structure of sub-elements.
            @param name: Name of this Message, Loop or Segment
            @param loops: Loop and Segments that belong to this Loop (or Message).
            """
            self.name= name
            self.structure= []
            self.occurance= None # distinguish repeated Segment types
            self.parent= None
            for loop_seg in loops:
                self.append( loop_seg )






This has the advantage that we can simply contain all the subordinate structure within a Loop or Segment definition.  The syntax melts away to simple commas.  This is very nice.




This suffers from the disadvantage that we can't easily handle an evolving puddle of attributes.  To have a completely flexible definition, we'd really like to use keyword parameters for the additional descriptive information.  Using keywords leaves us the flexibility to add or change the parameters without breaking an installed base of parsers.




I'd like to say something like the following.




Loop( "2000A", desc="Some Desc", required="S", repeat="1", Segment(...), Segment(...), Loop(...), ... )




But Python can't parse this, since the keywords are in front of the positional parameters.  Darn it.  I'm forced to think.




I have a couple of choices.  First, I could bundle the structural elements into a sequence.  This would lead to an "extra" set of parenthesis or brackets.  Cconsidering that the matching ()'s will be separated by 100's of lines of code, we can't be expected to manage this without errors.




A Properties Bundle
-------------------




The alternative is to bundle the descriptive parameters into some kind of Properties or Description object which simply carries the extra attributes in a tidy, easy-to-extend object.




This leads us to change the style to something that could be called a **Bundled Properties**  design.  [Something I first saw in Django.]  This means that our constructor has just two positional parameters followed by an unlimited number of structural elements.  We can live with two positional parameters; it is unlikely to turn into a maintenance problem.







Loop( "2000A", Properties( desc="Some Desc", required="S", repeat="1" ), Segment(...), Segment(...), Loop(...), ... )




This is much more manageable.  But -- to an extent -- it feels like a workaround for a Python syntax rule.  Actually, it's a more extensible design, since it separates the structure from the non-structural properties of a construct.  We can now update the Properties class definition to add as many properties as we find are necessary to process X12 messages.




Our Properties class can be as simple as the following.





::

    >>> class Properties( object ):
    ...     def __init__( self, **kw ):
    ...         self.__dict__.update( kw )
    ... 
    >>> p= Properties( hi="mom", num=22, denom=7 )
    >>> p.hi
    'mom'
    >>> p.num
    22






This lets us refer to properties with simple names.








