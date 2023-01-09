Code Deletion
=============

:date: 2011-03-30 16:55
:tags: refactoring,architecture
:slug: 2011_03_30-code_deletion
:category: Technologies
:status: published

A joyous milestone today. Removed much of our
pre-`Piston <https://bitbucket.org/jespern/django-piston/wiki/Home>`__
RESTful web services code.

We started with the `Django-REST
Interface <http://code.google.com/p/django-rest-interface/>`__. While
nice, it imposed a number of restrictions that were onerous. In
particular, we have a lot of non-model responses. They're model-like
data that we serialize to be compatible with Django, but without
actually being first-class Django Model objects.

In order to provide a generic, but detailed "status" message, we
actually defined a Model that we never instantiated in the database.
We'd build (but not save) instances, just to make it easy to
serialize them.

What a hack.

To further complicate things, I failed to really understand the way
that the alternate user authentication sources worked, and how much
of the Django authentication process was better handled through
middleware. Failing to fully understand that, I wrote too much code.
We tinkered with incoming requests to extract HTTP Authorization
headers. We tinkered to handle Amazon-style key/signature values in
the GET or POST. And we tinkered to handle OpenAM authentication
cookies.

Too much code.

And it gets worse. I tried to use
`urllib2 <http://docs.python.org/library/urllib2.html>`__ for a wide
variety of RESTful requests. This means more than GET and POST. That
was a mistake.
`httplib <http://docs.python.org/library/httplib.html>`__ works out a
little better for doing RESTful web services requests. If you don't
have a lot of complex proxy server handling. And if you don't have a
lot of complex authentication.

In our case, the urllib2 was handling the 401 retries, cookies and
also had some extra handler code to treat a 201 Created response as a
non-error (by default, urrlib2 gagged on 201 Created). Also, urllib2
appears to be lazy and doesn't send everything or close the sockets
in the event of a problem. This makes unit testing just a bit more
complex than necessary. Also, urllib2 required a couple of monkey
patches to let us use PUT and DELETE without problems.

Needless Complexity.

It turns out that handling a 401 retry in httplib isn't really all
that difficult. That ended the use case for urllib2.

What's nice is

#. Being able to unmake some bad decisions.

#. Rerunning the entire unit test suite to ferret out the remaining concealed dependencies.

#. Removing hack-arounds, volume and complexity.

We still have a lot of work to make full use of Piston. That will
lead to removing yet more code. It will, however, also change the
API's slightly because the ".../xml/..." URL's will have a
different format and we'll introduce ".../django/..." URL's which
will have the current format.






