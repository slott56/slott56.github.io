What's Central Here?
====================

:date: 2008-07-12 15:25
:tags: architecture,design,data structure,algorithm
:slug: 2008_07_12-whats_central_here
:category: Architecture & Design
:status: published







The requirements are a sequence diagram showing a complex back-and-forth with the vendor's web service.  Each request and reply is detailed, but there's no overview or summary stated.  It's implied, and all of the business folks can articulate it, but no one wrote any of it down.



This looks like a relatively clean, RESTful kind of service -- our customers send us requests, we gather information from vendors, do our value-add processing, and send a response.



It looks like the classic Web Services Proxy design pattern.  We define a nice Python class that's a proxy for the external services (and their goofy protocols).  We can then define a simple WSGI application to use those services and do our value-add processing.

::

    class SomeService( object ):
        def someMethod( self, **args ):
            Create XML request object
            Create Request with a method of POST
            urllib2.open( )
            Parse XML response



::

    class OurApplication( object ):
        def __init__( self, service ): 
            self.service= service
        def __call__( environ, start_response ): 
            request= simplejson.load( wsgi.input )
            self.service.someMethod( ... )
            self.service anotherMethod( ... )
            self.service.step3(...)
            self.service.moreAndMore(...)
            self.ourValueAddProcessing( ... )
            start_response( '200 OK', [('Content-type','application/json')]
            return [ simplejson.dumps( reply ) ]
        def ourValueAddProcessing( self, **kw ):
             some processing that we're going to charge for





Ideally, the project plan is to debug the service proxy and write the application.  Using Python and the widely available WSGI tools, this isn't a lot of programming.  We should be up and running inside of a month.  Right?  Wrong.



Focus on Value
---------------



Everyone's focus was on the "rocket science" part of this: using an external vendor for information.  This is where the business owners had spent a lot of time.  The value add was so obvious, it didn't need to be written down.  But the negotiations with the vendors -- the service level agreements, the contracts, the terms and conditions, the commercial considerations -- had soaked up a lot of brain calories.  



I had a long list of vendor contacts.  I had examples, documents, URL's, all kinds of supporting material for the vendor data gathering.  



But for our "value add", I had nothing.  I had bupkes.  It was a "calculation" or a "lookup" or something.  I didn't even have the name of the internal folks who knew this.  I had a spreadsheet, and it wasn't consistent enough to make sense of.



Invertability
-------------



After some digging, the question arose as to what the essential processing scenario should be.  It sure looks like the main processing has the following outline.



1.  Some internal value-add steps.



2.  Gather Vendor data (a long back-and-forth)



3.  A final internal value-add step to combine everything.



Which view is right?  The Vendor-centric sequence?  A sequence focused on our value-add?  More importantly, how can we make it irrelevant?  The answer is an "invertable" design.  Each step is a separate object, the overall service merely combines the various steps in some useful order.



The Command Design Pattern
---------------------------



This works out well if each step follows the GoF `Command <http://en.wikipedia.org/wiki/Command_pattern>`_  design pattern.  A sequence of steps is also a Command; this permits me to reswizzle this with every rise and fall in the slowly-solidifying requirements.

::

    class Command( object ):
        def __init__( self, service ): 
            self.service= service
        def __call__( self, state ):
            return NotImplemented
    
    class OurStep1( Command ):
        def __call__( self, state ):
            state.onething= our value-add
    
    class OurStep2( Command ):
        def __call__( self, state ):
            state.anotherthing= another value-add
    
    class VendorStep1( Command ):
        def __call__( self, state ):
            self.service.someMethod(...)
    
    class VendorStep2( Command ):
        def __call__( self, state ):
            self.service.anotherMethod(...)
    
    class Vendor( Command ):
        def __init__( self, *args ):
            super( Vendor.self).__init__( *args )
            self.vs1= VendorStep1( self.service )
            self.vs2= VendorStep2( self.service )
        def __call__( self, state ): 
            for step in ( self.vs1, self.vs2 ):
                step( state )
    
    class OurValueAdd( Command ):
        def __init__( self, *args ):
            super( OurValueAdd, self ).__init__( *args )
            self.our1= OurStep1( self.service )
            self.our2= OurStep2( self.service )
            self.vend= Vendor( self.service )
        def __call__( self, state ):
            for step in ( self.our1, self.vend, self.our2 ):
                step( state )





Now, we can use any of the steps in any order.  And we can recombine them, extend them, replace them, contract them.



All That Overhead
-----------------



It appears like we've micro-managed a simple thing.  We took a simple piece of procedural programming, turned each step into an object, and added a lot of overheads.



However, the "simple" piece of programming isn't fully defined.  Any one of the "steps" could expand, contract or get replaced.  Our impact is controlled. 



There's one big change, however, may be pervasive.  Additional service definitions will change the constructor.  We'd have to switch to a dictionary, ``**services``, and each class would have to pick a specific member in the collection of services.





