Wrestling with REST
===================

:date: 2008-06-25 10:18
:tags: architecture,design,data structure,algorithm
:slug: 2008_06_25-wrestling_with_rest
:category: Architecture & Design
:status: published







REST is cool because there's less protocol there -- little more than HTTP and some kind of representation for objects (XML, JSON or whatever.)   It seems to me that REST with JSON is a very lightweight approach to implementing web services.  Doing this in Python further trims down the technology stack by limiting the amount of source code and the amount of work required to build something.



The fundamental design issue for REST is -- as cleanly as possible -- to make your application's resources available through URI's.  In order to do this, you need to understand your resources.  The process looks something like the following.



From IBM's `RESTful SOA <http://www.ibm.com/developerworks/library/x-restfulsoa/>`_  paper, we see a four-step summary of REST design.  This presumes you have some design already completed.



1.  Decide on the resources and their descriptive URLs.

#.  Choose a data format for communication on each URL.

#.  Specify the methods on each resource.

#.  Specify the returned data and status codes.



From Ben Ramsey's presentation on `RESTful Design <http://benramsey.com/media/talks/ipcse07-rest.pdf>`_ , we have six steps.



1.  Determine your resources

#.  Decide what methods each resource will support

#.  Link the resources together

#.  Develop your data schemas

#.  Rationalize your schemas

#.  Choose the best content type/format to represent your schemas



Both of these help, but they seem incomplete.



:strong:`Implementation Details` 



Since Django does a lot (ORM, URL mapping, free admin interface) it's my personal jumping-off point for web applications.  Django's essential design principles are RESTful from the beginning.  See the `URL dispatcher <http://www.djangoproject.com/documentation/url_dispatch/>`_  documentation.  This references the `Cool URI's Don't Change <http://www.w3.org/Provider/Style/URI>`_  document by Tim Berners-Lee.



Further, Django encourages us to get the model right to begin with, then we can (easily) define RESTful access to that model.  



Here's the problem.  We have two interfaces: a human interface and a WS API; these are comingled.  Along with multiple interfaces, we've also got several applications that are part of the overall service offering.  With an interface dimension and a application dimension, how do we distinguish among the various URI's?



:strong:`Enumerating The Choices` 



We've got the application dimension (also known as subject areas).  For example, there might be separate applications for Customer, Services Catalog, Order Pricing, etc.  



We've also got the "interface" dimension: human via HTML vs. WS API via JSON (or XML).



With two independent dimensions we've got the kind of matrix design that gives people gas and makes them invent `aspect-oriented programming <http://en.wikipedia.org/wiki/Aspect-oriented_programming>`_ .  Matrix designs aren't a reason to invent a new paradigm, it just requires a little care with the paradigms we have.



Our URI's are linear -- even though our design isn't -- and we have to group our URI's into tree-like paths.  We can put application first, or interface first.



/customer/xml/ID vs /xml/customer/ID



As an alternative, we can also use the HTTP headers to determine the intent behind a request.  It turns out that the HTTP Accept header provides us a handy hint.  We could make our WS API calls fill in a MIME type like "application/json".  Our human interface would have whatever the browser typically fills in for the Accept header (usually a long string of alternatives starting with "text/xhtml").



:strong:`A Big Push` 



The `Django-REST Interface <http://code.google.com/p/django-rest-interface/>`_  package makes the URI-based identification pleasantly simple.  This package makes a lot of design decisions for me.  The process looks like this.



1.  Define the data schema.  Build it.  Unit test test it.  Use the admin interface to work with it.



2.  Define the access URI's and representations.  These go together.  Human access is usually represented in HTML.  WS API access can be any combination of JSON, XML, YAML or some other serialized object representation.  



3.  Define the WS methods (GET, POST, PUT, DELETE).  The status codes could be defined more elaborately, but Django-REST provides a good implementation.



4.  Unit test all of this. Use the Django TestCase -- it provides a nice WS client.  See the Django-REST test cases for examples of how to curry in methods for put and delete methods.



5.  Rework the URI's and data model.  You'll never get it right the first time.  It's often hard to correctly model the business entities.  A lot of what passes for SQL design doesn't properly reflect real-world entities very well.  If you start from classes and implement them in SQL, you'll do a lot better than starting from SQL and trying to map SQL to objects.



:strong:`RPC Edge Case` 



The most notorious edge case is the Remote Procedure Call (RPC); places where there doesn't seem to be a proper resource.  Sometimes, these are thought of in strictly RPC terms -- a POST request with a payload of argument values.  A result is calculated and returned as an appropriate document.



I submit that in all cases, the RPC is in reality the creation of that result document.  The result document should -- trivially -- be made into a first-class persistent Django model.  The POST request to "create" the model may provide only a few attributes, the rest are then developed as part of handling the POST.  For all that it matters, they can be implemented in the save() method of the model!



This, however, breaks us out of the Django-REST interface.  Our GET requests can still be handled by the Simple or Basic examples.  The POST request, however may break the mold, since the basic POST request isn't a good match for the resulting document.



:strong:`But Wait` 



What we have is a POST request that isn't really a good match with the schema object.  Indeed, the point of an RFC-style request is that we have complex transformations (calculations, lookups, etc.) occurring somewhere in the POST processing.  



I looked closely at the `Generic Resource <http://django-rest-interface.googlecode.com/svn/trunk/django_restapi_tests/examples/generic_resource.py>`_  example.  Very closely.  But it wasn't really helping too much, since the inputs were not very close to the final document.



So, after spending hours of reading the Django-REST code, I finally realized what was going on.  Once we're out of the Django-REST sweet spot, we're just doing ordinary Django.  It's just a Django view.



A special-purpose POST request can be an ordinary Django view.  This can do the elaborate RPC-like calculations.  It can persist the resulting document.  Then it can -- without much difficulty -- use a Django-REST responder to provide the expected HTTP response.



Indeed, the underlying algorithm is shared between a number of closely-related views.  The JSON or XML view works one way.  The HTML view has a slightly different behavior (since it can display error messages to a person), but has the same underlying algorithm.





