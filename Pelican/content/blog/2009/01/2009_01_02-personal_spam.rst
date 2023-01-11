Personal Spam
=============

:date: 2009-01-02 01:25
:tags: technologies,web
:slug: 2009_01_02-personal_spam
:category: Technologies
:status: published







In previous years, I had several email lists: my Yahoo! list, my Google list, my desktop.  To figure out what to send, I had to merge the lists, which meant reading vCards, and CSV files.  This is totally the sweet-spot for Python.



The Mac OS X `Mobile Me <http://www.apple.com/mobileme/>`_  has a very nice sync capability that integrates Yahoo!, Google and my desktop (which includes my iPhone).



Mobile Me eliminated my email merging.  Now, everything is in my desktop Address Book.  My holiday mailing list can be trivially exported to a big old .VCF file.



Spamming via VCF
----------------



There's a Python Personal Data Interchange project (http://savannah.nongnu.org/projects/python-pdi), http://pdi.sourceforge.net/.  I, however, made no use of this.



Instead, I rebuilt my old spamulator to simply email to a list of folks identified by vCard.  The application has three principle parts:



1.  The vCard structure itself.



2.  The parsing of vCards.



3.  Sending the spam.



vCard Class Definitions
------------------------



First, we have the core definitions of a vCard.  For information see `RFC 2425 <http://tools.ietf.org/html/rfc2425
http://tools.ietf.org/html/rfc2425>`_  and `RFC 2426 <http://tools.ietf.org/html/rfc2426>`_ .

::

    from collections import defaultdict
    
    class Parameter( object ):
        """A parameter modifies a property."""
        def __init__( self, name, value=None ):
            self.name= name
            self.value= value
        def __str__( self ):
            if self.value is None:
                return self.name
            else:
                return "%s=%s" % ( self.name, self.value )
    
    class Property( object ):
        """A Property of a VCard has a name, and a list of values.  It may also have a 
        sequence of ;-delimited parameters.
        
        A property name can be simple, or use dot notation to group some properties.
        """
        def __init__( self, name, value, parameters=None,  ):
            self.name= name
            if parameters is None:
                self.parameters= dict()
            elif isinstance( parameters, dict ):
                self.parameters= parameters
            else:
                self.parameters= dict(parameters)
            self.valueList= value
        def addParameter( self, parameter ):
            self.parameters[parameter.name]= parameter
        def getValue( self ):
            """Two kinds of values: single and multiple; rarely any ambiguity."""
            if len(self.valueList) == 1:
                return self.valueList[0]
            return self.valueList
        value= property( getValue )
        def __str__( self ):
            value= ";".join( self.valueList )
            if len(self.parameters) == 0:
                return "%s:%s" % ( self.name, value )
            else:
                params= ";".join(map(str,self.parameters.values()))
                return "%s;%s:%s" % ( self.name, params, value )
    
    class VCard( object ):
        """A VCard is a collection of Properties.
        Each named Property can occur any number of times, so the property name is a 
        key to a list of instances.
        """
        def __init__( self, props=None ):
            if props is None:
                self.props= defaultdict(list)
            elif isinstance( props, defaultdict ):
                self.props= props
            else:
                self.props= defaultdict(list,props)
        def addProperty( self, prop ):
            self.props[prop.name].append( prop )
        def __str__( self ):
            propList= []
            for p in self.props:
                propList.extend( self.props[p] )
            #propList.sort( key=lambda p:p.name )
            return "BEGIN:VCARD\n%s\nEND:VCARD" % ( "\n".join(map(str,propList)), )





The essential data structure is the VCard, which has any number of named properties.  A named property has parameters and a value.  Values can be a simple string, or a ;-delimited list of strings.  Very simple, really.



Parsing a VCF File
-------------------



The trickiest part about parsing VCF is the escape rules.  The :, ; and , punctuation marks are sacred, but can be escaped to allow ;'s or :'s to appear in the value of a property.  The , is used to punctuate multiple values for a parameter, something that doesn't enter into email very often, so it can be ignored for now.



Here's the parser, using some cool regex things I found.

::

    import re
    
    class VCFParser( object ):
        def __init__( self ):
            self.colon= re.compile( r"(.*)(?<!\\):(.*)" )
            self.equals= re.compile( r"(?<!\\)=" )
            self.semicolon= re.compile( r"(?<!\\);" )
        def getLines( self, aFile ):
            """Unfold any long lines."""
            fileIter= iter(aFile)
            unfold= fileIter.next()
            for line in fileIter:
                if line[0] == ' ':
                    unfold += line.lstrip()
                else:
                    # Start of the next line
                    yield unfold
                    unfold= line
            if unfold is not None:
                yield unfold
        def getContent( self, aFile ):
            """"Decompose lines into group/name, param and value elements."""
            for line in self.getLines( aFile ):
                propStr, valueStr = self.colon.match( line ).groups()
                prop_params= self.semicolon.split( propStr )
                value= self.semicolon.split( valueStr )
                yield prop_params[0], prop_params[1:], value
        def parseCard( self, aFile ):
            """"Create a Card from a sequence of lines."""
            for name, params, value in self.getContent( aFile ):
                if name.upper() == "BEGIN":
                    assert len(params) == 0 and value[0] == "VCARD", "unexpected value %r" % (value,)
                    currentCard= VCard()
                elif name.upper() == "END":
                    assert len(params) == 0 and value[0] == "VCARD", "unexpected value %r" % (value,)
                    yield currentCard
                else:
                    prop= Property( name, value )
                    for p in params:
                        pfields= self.equals.split( p )
                        prop.addParameter( Parameter( *pfields ) )
                    currentCard.addProperty( prop )
        def parse( self, aFile ):
            return ( c for c in self.parseCard(aFile) )





There are three cool regexes that look for unescaped :, = or ;.  I took a while to track these down in the documentation, but once I found them, my life was much simpler.  Here's the doctest string.

::

    >>> import re
    >>> colon=  re.compile( r"(.*)(?<!\\):(.*)" )
    >>> colon.match( "N:Name;This;That" ).groups()
    ('N', 'Name;This;That')
    >>> colon.match( r"ADDR:Contains\:Colon" ).groups()
    ('ADDR', 'Contains\\:Colon')
    
    >>> semicolon= re.compile( r"(?<!\\);" )
    >>> semicolon.split("EMAIL")
    ['EMAIL']
    >>> semicolon.split("EMAIL;type=pref")
    ['EMAIL', 'type=pref']
    >>> semicolon.split("EMAIL;type=pref\;special;type=work")
    ['EMAIL', 'type=pref\\;special', 'type=work']





This also uses a series of generators to make it easy to unfold long lines and accumulate a mult-line card.  I'm a big fan of this "generator cascade" design pattern to break a fairly complex parsing job up unto manageable pieces.



SMTP Interface
--------------



The final step is actually using SMTP to send the email.  Note that we need to put the destination name into the message itself.  While not hard, it does mean that the message isn't a static object: it has to be tweaked for each outgoing message.  I like to define a Message class to handle this business for me.

::

    import smtplib
    class Message( object ):
        def __init__( self, from_, subject, body ):
            self.text= body.split('\n')
            self.subject= subject
            self.from_= from_
        def flat( self, to_ ):
            return smtplib.CRLF.join( ["From: %s" % self.from_,
                "To: %s" % to_,
                "Subject: %s" % self.subject,
                "" ] + self.text )
    
    def getVCFIter( fileName ):
        vcf = VCFParser()
        src= open( fileName, "rU" )
        addrList= []
        for card in vcf.parse( src ):
            for p in card.props['EMAIL']:
                yield p.value
        src.close()
        
    def send( msg, toList ):        
        s=smtplib.SMTP("smtp.somewhere.com")
        s.login('username','password')
        for t in toList:
            response= s.sendmail("from@somewhere.com",t,msg.flat(t))
            if response: print response
        print len(toList),"sent"
        s.quit()





This is pleasantly short and to the point.  Once the command-line parameters have been parsed, we're down to  parsing the options and then doing the following:

::

    body= file( theMessageFile, "rU" ).read()
    msg= Message( "s_lott@mac.com", options.subject, body )
    send( msg, getVCFIter( theListFile ) )





I like Python.  I really like the subtle way in which all of the steps of processing a vCard are based on generators meaning that I don't read in a large pile of data, but actually read in just enough to process one card at a time.





