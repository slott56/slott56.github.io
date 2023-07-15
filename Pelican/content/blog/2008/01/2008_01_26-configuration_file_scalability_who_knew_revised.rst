Configuration File Scalability -- Who Knew? (Revised)
=====================================================

:date: 2008-01-26 23:12
:tags: architecture,software design,data structure,algorithm
:slug: 2008_01_26-configuration_file_scalability_who_knew_revised
:category: Architecture & Design
:status: published







Background: I'm looking at parsing certain X12N messages.  There's a Perl program on CPAN to do `X12 parsing <http://search.cpan.org/~prasad/X12-0.08/lib/X12/Parser.pm>`_ ; the program itself isn't useful, but the X12 messages are defined via INI files.  There's also a `Python X12 <http://pyx12.sourceforge.net/>`_  parser with the X12 messages defined via XML files.  I don't really like working with the INI or XML definitions because the INI or XML merely defines a Python object that does the real work.



My idea was to replace the configuration files in these two examples.  It it clearly better to build a Python object that actually is the X12 parser rather than read a bunch of files which build the Python.  This Python parser definition can be build with relative ease from the the X12 standards coupled with a business partner's Implementation Guide (IG).



Based on partner IG's and two sets of helpful examples of config files, I built the necessary set of classes.  Then I built an example X12 message parser.  



Here's the problem: it was too big.   Python died.  (Well... not *dead*, but it threw an exception that said that the Python parser had run out of memory.)



I didn't reckon on how big an X12 message definition actually is.  I was shocked -- shocked -- that an object construction would be a problem.  I was already to start dashing off angry messages.



Then I looked closely at my example.



It was a single object construction expression that covered over 1200 lines.  It created about 774 or so distinct objects.  It appears that a single expression of this scale is a bad idea.



It looks like this (but is 1200 lines long).



::

    parse278= Message( "278", Properties(...), 
        Loop( "ISA_LOOP", Properties(...),
            Segment( "ISA", Properties(...),
               Element( "ISA01", ... ),
               Element( "ISA02", ... ),
               ...14 more...
            ),
            Loop( "GS_LOOP", Properties(...), ...long, long list... ),
            Loop( "GE_LOOP", Properties(...), ... ),
            Segment( "IEA", Properties(...),
                Element( "IEA01", ... ),
                Element( "IEA02", ... ),
            ),
        )
    )






A single, 1200-line statement doesn't actually compile.  After I thought about it, I realized I was asking a lot.




The good news is that changing this massive expression into a series of discrete assignment statements requires relatively little real work.  And the X12 message structure (based on nested Loops) encourages the definition of the overall message as a series of Loop objects.




Now it looks like this.



::

    ST_LOOP = Loop( ... )
    GS_LOOP = Loop( u'GS_LOOP', Properties(...),
      Segment( 'GS'...),
      ST_LOOP,
      Segment( 'GE'... ), )
    ISA_LOOP = Loop( u'ISA_LOOP', Properties(...),
      Segment( u'ISA', Properties(...),
        Element( u'ISA01', ...),
        ...
      )
      GS_LOOP,
      Segment( u'IEA', Properties(...),
      Element( u'IEA01', ... ),
      Element( u'IEA02', ... ),
      ),
    )
    x278_res = Message( u'278', Properties(...), ISA_LOOP
    )






Persistence
-----------




Beyond marshalling and unmarshalling, we also need to look at persisting messages.  We can choose to store individual Segments (a bad idea) or the higher-level Loops of Segments (a slightly better idea).  The Loop-based structure of our parser configuration leads to creating a Loop-based data model.




It's important that the SQL model and the Parser structure are completely isomorphic.  We need to take a block of text, unmarshal the message, map it to tables, and load it into a database.  And we need the whole to be driven by a Python configuration which comes from the Implementation Guides in an obvious way.




In the long run, I need to transform an Implementation Guide into a Python configuration, confident that we can accept, parse, and persist X12 messages in spite of multiple business partners and evolution of the X12 model.




Since X12 isn't an open standard, this isn't easy.  But Python's flexibility makes it work out well.




