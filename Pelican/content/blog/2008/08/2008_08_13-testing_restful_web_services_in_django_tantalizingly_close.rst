Testing RESTful web services in Django -- Tantalizingly Close.
==============================================================

:date: 2008-08-13 10:10
:tags: #python,unit testing
:slug: 2008_08_13-testing_restful_web_services_in_django_tantalizingly_close
:category: Python
:status: published







Here's what's great about `Django <http://www.djangoproject.com>`_  coupled with the `Django-REST Interface <http://code.google.com/p/django-rest-interface/>`_ :  It's almost all model.  You define the model, write some tests.  Add the URL mappings, write some tests using the built-in Django client.



We're almost there, but this doesn't work out perfectly.  To do complete tests, we have to either subclass the Django Client to add "put" and "delete" or curry in methods for "put" and "delete".  Then we can almost test our complete set of web services functions.



At this point, the core of the application is -- well -- done.  It works, it handles the web services requests.  We can then start folding in HTML pages for the endlessly negotiated human interface.



However, we're still not ready for deployment. 



Authorization Differences
-------------------------



First, we haven't really got a solid security model in place.  Sure, we can add @login_required decorators to any view functions.  But that doesn't really secure the REST interface at all.  That's where the going gets tough.



The Django-REST Collection has an 'authentication' attribute that checks passwords.  It has an HttpDigestAuthentication class that handles more-secure password digests.  This looks perfect for web services.  But, it has two problems.



1.  We don't have MD5 digests readily available.  Django uses SHA1 digests of password only, not an MD5 digest of username:realm:password.



2.  We can't easily test using digest authentication with the off-the-shelf Django test Client.  Not only does the test client lack Put and Delete, but it can't handle HTTP Digest authentication, either.



Sigh.  I thought we'd be done in `20 minutes <http://showmedo.com/videos/video?name=2000080&fromSeriesID=200>`_ .  Turns out, I have to actually do some work.



Adding MD5 Digests
------------------



MD5 digests seem to work out best with the 'Profile' extension to the Django authorization application.  The model is delightfully simple, just a single CharField to hold the MD5 hexdigest of username:realm:password.   



One consequence is that we now have two password digests, the default SHA1 in the User model and our Web Services MD5 in the Profile extension.  This means that our page for password resets must have a view that sets both passwords.



Testing Complications
---------------------



In the long run, we have to provide WS client libraries.  While the application is entirely RESTful, the marketplace expects an API library that they can install.  We have to provide Python, .NET and Java libraries to invoke our service.  This isn't very complex.  



For Python, it would be simplest to leverage the `urllib2 <http://docs.python.org/lib/module-urllib2.html>`_  package.   We can provide some classes which act as remote procedure call proxies; these classes have methods that invoke our REST services (GET, POST, PUT and DELETE) on various resources or collections.



Something like the following:

::

    class MyProxy( object ):
        def __init__( self, host, port, username, password, realm ):
            self.urlBase= "http://%s:%s" % ( host, port )
            # Build Handler to support HTTP Digest Authentication...
            digest_handler = urllib2.HTTPDigestAuthHandler()
            if username is not None:
                digest_handler.add_password(realm, self.urlBase, username, password)
            # Build Handler to support HTTP Basic Authentication...
            basic_handler = urllib2.HTTPBasicAuthHandler()
            if username is not None:
                basic_handler.add_password(realm, self.urlBase, username, password)
            # Build Handler to treat 201 as a normal response, not an exception...
            error_handler= RESTHTTPHandler()
            self.server = urllib2.build_opener(digest_handler,basic_handler,error_handler)
        def request( self, method, uri ):
            assert method in ( "GET", "POST", "PUT", "DELETE" )
            data= urllib.urlencode( argDict )
            theReq= RESTRequest( method, self.urlBase + path, data )
            try:
                response= self.server.open( theReq )
                # fold in attributes that are compatible with Django HttpResponse
                response.status_code = response.code
                response.content= response.read()
                return response
            except:
                ... handle various kinds of IOError, HTTPError exceptions...
        def getSomeResource( self, key ):
            response= self.request( "GET", "/path/to/resource/%s" % key )
            ... examine response.content, maybe do simplejson decode or xml.etree parse...





The problem is that the Django test client and the urllib2 packages are wildly incompatible.



Okay, maybe not *wildly* , but seriously incompatible.



First, the Django Client's HttpResopnse includes attributes status_code and content.  The urllib2.addinfourl response uses code and is -- itself -- a file-like object.



Second, and more important, the Django Client's HttpResponse is a dictionary full of headers.  The urllib2.addinfourl is a file with an info() method that contains the headers.



Choices
--------



We have a tantalizing set of alternatives.



1.  Make urllib2's response look more like Django's response.  This requires adding a few additional attributes, and a __getitem__ method.  Not too difficult to do.  But only because our unit tests are not very demanding.



2.  Create a Facade over urllib2.addinfourl and django.http.HttpResponse that is independent of both, and can work with both as implementation classes.  While cool-sounding, and easy to implement in our WS client package, we'd have to do a tiny bit of extra work in our unit tests to create a Facade-based client rather than use the default client.



3.  Get a proper Python RESTful client.  Like `RESTClient <http://restclient.org/>`_  or `Python-rest-client <http://code.google.com/p/python-rest-client/>`_ .  The approach in `RESTful Python <http://www.infectmac.com/2008/08/restful-python.html>`_  -- a decorator -- is another possibility.



The problem with #1 is that the Python client package we distribute will have this odd-looking design that adds a bunch of random-looking features to urllib2.addinfourl.  A lot of explanation (like this Blog posting) doesn't remove the oddness.  The Java and .Net packages will be fine.



The problem with #2 is that the Python client package will be even more complex than #1, with little recognizable value to anyone for the complexity.



There's no problem with #3.  Indeed, this might be best in the long run.





