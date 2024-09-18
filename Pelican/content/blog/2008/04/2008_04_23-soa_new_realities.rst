SOA New Realities
=================

:date: 2008-04-23 10:16
:tags: soa,xml
:slug: 2008_04_23-soa_new_realities
:category: Technologies
:status: published







I'm not a fan of XML as the one true language.  I've griped before about the attractive nuisance of XML.



Recently, I saw Sean McGrath's `New Realities <http://seanmcgrath.blogspot.com/2008/04/new-realities.html>`_ , which lead me to `Project Zero <http://www.projectzero.org/>`_ , a RESTful/JSONic SOA architecture.  Their blog includes postings like `A run-time for "the New Reality <http://www.projectzero.org/wiki/bin/view/Community/JerrysBlog/BlogEntry5>`_ .



I find that I'm totally in sync with many of the key points.



**Scripting**.
    Compiling, building and deploying Java is just tedious busy-work.  Python is amazingly productive.  When I look at doctest comments, I realize that good programming is programming that looks simple.  The best programming is stuff you can type interactively at the >>> prompt in Python.



**ORM**.
    The RDBMS is only useful as persistent storage for objects, and ORM is the way to do this.  Triggers, stored procedures and complex SQL have costs that outweigh their value.  SQLAlchemy and the Django ORM simplify things a great deal.



**REST**.
    The use of HTTP's methods and URI's to accomplish useful work is simple, elegant, extensible, scales well.  SOAP and WSDL is just overhead that helps the statically compiled Java application cope with change.  I'm a big fan of the way REST GETs can be tested with a browser.



**JSON**.
    XML and the associated XSD's are wordy and complex.  JSON, especially in Python, is a first-class data structure that requires minimal almost no programming.  It's a little weird making your Python objects all subclasses of dict, but you get over that quickly.



**WSGI**.
    The WSGI architecture is a tremendous simplification.  Each piece of the application is part of the WSGI pipeline that has the following consistent design pattern:  (1) validate, (2) put something into the environment, (3) pass it on or declare the processing complete.  The "put something into the environment" is such a huge simplification because it allows arbitrary steps to be added, removed or changed without fundamentally breaking anything.





**Agile**.
    Big Design Up Front (BDUF) isn't helpful because you don't know the consequences of each design decision.  With simple REST, ORM and scripting tools, however, you can reverse a design decision in an afternoon.



**TDD**.
    An essential part of Agility is being able to refactor and make changes.  You can't do this without a robust set of unit tests.



Here's what I don't have: a really good REST client library.  urllib2, with an extension to the Request class, works, but it seems clunky somehow.  With all the attention REST has, I'd like to think that someone has a cool REST client.



Here's the code I'm using.

::

    class RESTRequest( urllib2.Request ):
        def __init__(self, method, url, data=None, headers={} ):
            urllib2.Request.__init__( self, url, data, headers )
            self.method= method
        def get_method( self ):
            return self.method

    class Client2( object ):
        def __init__( self, host, port, username, password ):
            self.urlBase= "http://%s:%s" % ( host, port )
            # Create an OpenerDirector with support for HTTP Authentication...
            basic_handler = urllib2.HTTPBasicAuthHandler()
            basic_handler.add_password('testrealm@localhost', self.urlBase, username, password)
            digest_handler = urllib2.HTTPDigestAuthHandler()
            digest_handler.add_password('testrealm@localhost', self.urlBase, username, password)
            self.server = urllib2.build_opener(basic_handler,digest_handler)
        def request( self, method, path, argDict ):
            data= urllib.urlencode( argDict )
            theReq= RESTRequest( method, self.urlBase + "/" + path, data )
            try:
                response= self.server.open( theReq )
                # 200 OK goes here, all others are exceptions
                #print response.code, response.msg
                #print response.info()
                return response
            except urllib2.HTTPError, e:
                if e.code >= 500:
                    raise
                #print e.code, e.msg
                #print e.info()
                return e





While compact and clear, it still doesn't look quite right.



One improvement might be to create subclasses of Basic and Digest handler which quietly handle the short list of REST status codes as return values instead of raising exceptions.  It would eliminate the try: block, but would create Yet More Subclasses to maintain.



Here's what an application does.

::

    srvr= Client2( "localhost", 18000, "slott", "slott" )
        newData= { 'name':"US Test Company  898", 'state':"PA" }
        response= srvr.request( "POST", "realm/schema.1.2/instance", newData )
        print response.code, response.msg
        print response.info() # headers, FWIW
        print eval( response.read() ) # JSON reply will be a dict object





This is a nice-enough API.  The URI's, BTW, have a realm (prod, test, QA, etc.) a schema object (with version number), and the PK for that object as a "typical" REST URI.




