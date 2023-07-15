Python as Config Language -- Forget XML and INI files
=====================================================

:date: 2008-01-12 01:54
:tags: architecture,software design,data structure,algorithm,python
:slug: 2008_01_12-python_as_config_language_forget_xml_and_ini_files
:category: Architecture & Design
:status: published







See Sean McGrath's `Spot the warning signs in configuration file design <http://itworlddaily.blogspot.com/2008/01/spot-warning-signs-in-configuration.html>`_  for thoughts on the ever-gnarly problem of how to provide a workable set of configuration parameters to a program.



A programming language has all the advantages as a language for encoding parameters.  I see why it's rare -- too many programmers have spent too much time with MS's abominable INI files and think it's "normal".



Recently, I started working on reverse engineering an venerable C program that relied on a set of INI-like files.  It isn't cost-effective to write (or even download) an INI-file parser for Java.  Instead, most of the configuration parameters could be simply moved into a garden-variety Java properties file.



Some parameters, however, didn't fit the INI format well.  I'd almost completely eliminated any need for the INI file parser until these additional, complex parameters surfaced.  It was a head-scratcher until I reframed the problem.



How Would I Do This In Python?
------------------------------



In Python, I could -- trivially -- declare the relationships as a bunch of class constructors.  The simple elegance of the Python constructors lead me to a version in Java that was -- while not as nice -- a lot better than writing Yet Another Parameter File Parser.



The INI syntax was -- to an extent -- close enough to a Python (or Java) class constructor that I could transliterate the original INI file into application source.



The business rules in the config file looked like this:



Rule_AP = 2, AP, DCO, EXACT, FULL, PAIR, OPENHELD, ALLOW



I rewrote them to look like this in Java:



new Rule_AP( 2, AP, DCO, EXACT, FULL, PAIR, OPENHELD, ALLOW ),



I transformed an ad-hoc INI syntax into first-class Java syntax.  This eliminates a thousand or so lines of useless code.  It also reduces the complexity of the required documentation.  Rather than explain the syntax rules for the INI construct, we simply have to explain what this class does and what the constants mean.



Also, we don't have to dwell on the business rule translation from the old format to the new format.  They're essential the same.  The look nearly identical.  



Really Complex Configuration
----------------------------



Earlier today I was looking at the problem of parsing `X12 messages <http://publib.boulder.ibm.com/infocenter/wmbhelp/v6r0m0/index.jsp?topic=/com.ibm.etools.mft.doc/ad09580_.htm>`_ .  It's a pain in the neck because you need a ton of ancillary information to make sense of the X12 segments and the X12 Loops.



After an hour of poking around, I found a Perl program on CPAN to do `X12 parsing <http://search.cpan.org/~prasad/X12-0.08/lib/X12/Parser.pm>`_ .  The perl code is of no value.  However, the configuration files -- which describe some of the X12 messages I need to work with -- were very handy.



But they were in a home-brewed INI-like format.  A format that was just enough *UN* like INI files that ConfigParser choked on it.



After spending a day on the problem, I slowly evolved a configuration that was palatable.  The X12 message descriptions look something like this.  (*Warning*: elision, syntax errors may sneak in.)




::

    isa= Loop( "ISA",
        Segment("ISA"),
        Loop( "GS",
          Segment("GS"),
          Loop( "ST",
              Segment( "ST", (1,"278"), Required, 1 ),
              Segment( "BHT", None , Required, 1 ),
              ... 
              ),
          Loop( "SE",
             Segment ("SE" ),
             ),
          ),
          Loop( "GE", Segment ("GE" )
      )
    iea = Loop( "IEA", Segment( "IEA" ) )
    x278 = Message( isa, iea )





The configuration constructors actually build a recognizer that attempts to match the received message structure with the various parts of the configuration.  It wasn't easy, but when I was done, I could translate the configurations provided in the CPAN X12 package into proper Python object constructors.



In the outer realms of X12 messages, the Loops only have a single Segment.  The inner portions of the message (all of the Loop2000's, for example) have a much interesting structure.



One Syntax
-----------



Rather than cob up a syntax that is based on INI file syntax, I prefer to just use Python.  And rather than parse XML, I prefer to execute the Python directly.



I'll post a more complete example in the not-too-distant future.




