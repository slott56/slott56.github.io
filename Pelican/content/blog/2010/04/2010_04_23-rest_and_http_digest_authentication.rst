REST and HTTP Digest Authentication
===================================

:date: 2010-04-23 13:14
:tags: #python,architecture,Apache,WebServices,REST
:slug: 2010_04_23-rest_and_http_digest_authentication
:category: Technologies
:status: published

It seems so simple: use the HTTP Digest Authorization with the Quality
of Protection set to "auth".

It's an easy algorithm. A nonce that encodes a timestamp can be used
to be sure no one is attempting to cache credentials. It's
potentially very, very nice.

Except for one thing: Apache.

Apache absorbs the Authorization header. And that's the end of that.
It seems so simple, but I think I've been burned by it twice, now. I
write unit tests that work with simplified Python wsgiref (or
similar) servers. And I believe that those unit tests are equivalent
to integration tests.

Ouch.

There's another reason why HTTP Digest authentication for RESTful
services is a poor idea.

It involves too much traffic. HTTP authentication is usually a
two-step dance to establish a session. Two steps in one too many, and
RESTful services don't usually have any kind of session.

Schemes like this can actually work:
http://broadcast.oreilly.com/2009/12/principles-for-standardized-rest-authentication.html

The comments on this post are almost as helpful as the post itself.

The three points are straight-forward.

#.  Use SSL. Always.

#.  Multiple Key/Secret credentials. Read this as username/password if
    that's helpful. We store hashes of "username:realm:password" as
    part of a RFC 2167 Digest Authentication. We plan to continue to
    use those hashes. This is a bit touchy, but we think we can handle
    this by a slight change to our user profile table.

#.  The "signed query" principle requires some thought. We don't make
    heavy use of query strings. Indeed, we make almost no use of the
    query strings. So the hand-wringing over this is a bit silly. We
    simply ignore any query string when signing the request.

I just wish I did integration testing with Apache sooner, not later.
Sigh.



-----

I wonder what Apache buys us anymore, now that the...
-----------------------------------------------------

brian<noreply@blogger.com>

2010-04-23 16:21:30.109000-04:00

I wonder what Apache buys us anymore, now that there are so many
battle-tested options out there. I started writing a digest auth mixin
for tornado applications. It works, but it's missing one or two finer
points of the protocol (time allowing...)
http://github.com/bkjones/curtain
Also, what about putting Apache behind a proxy to handle auth for you?


Are you sure, that 2 HTTP requests cost more than ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-04-23 16:49:50.654000-04:00

Are you sure, that 2 HTTP requests cost more than 1 SSL session
initialization? I'm not ready to answer this question without
experiments. I guess that double round-trip time is more than shared
secret generation, but I'm not sure. Double round-trip means 4 TCP
packets before the actual data can be sent it the best case. But the PKI
thing...



http://code.google.com/p/modwsgi/wiki/Configuratio...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2010-04-26 07:06:57.031000-04:00

http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIPassAuthorization.
Aha! I've already rewritten things to use the query string for
authentication -- in the style of AWS. But. This is an important
alternative.


What Apache hosting mechanism are you using for WS...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-04-24 01:49:54.484000-04:00

What Apache hosting mechanism are you using for WSGI to claim that
'Apache absorbs the Authorization header'?

It is true that Apache absorbs it for CGI. This is because it is viewed
as a security risk in typical setup to pass it. You can tell Apache to
pass it through anyway, but you have to recompile Apache from source
code and define 'SECURITY_HOLE_PASS_AUTHORIZATION'.

In Apache/mod_wsgi, again because of the security issues, it doesn't by
default pass the Authorization header to WSGI application. You can
override this by setting the WSGIPassAuthorization directory or
pass-authorization option to appropriate mod_wsgi directives.

From memory, for the mod_fastcgi and mod_fcgid modules it depends on
what headers you tell it to pass through in the configuration
And for mod_scgi, it doesn't care and I believe passes it straight
through without any concern about security issues.

When proxying with Apache it should pass Authorization header straight
through because obviously the final destination server should be
worrying about it.

So, have you ensured you have configured your server appropriately.


Digest authentication doesn&#39;t strictly require...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-07-23 19:31:46.001000-04:00

Digest authentication doesn't strictly require two steps all the way.
When the client does the first request, the server will issue a
challenge key that SHOULD stay valid for a certain time.

The client can then pre-authenticate future requests against that
challenge key, thus, no double-ping-pong happens anymore.





