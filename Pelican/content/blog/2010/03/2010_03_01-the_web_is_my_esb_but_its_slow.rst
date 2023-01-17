The Web is my ESB, but it's slow...
===================================

:date: 2010-03-01 08:00
:tags: architecture
:slug: 2010_03_01-the_web_is_my_esb_but_its_slow
:category: Technologies
:status: published

Transaction design seems to be really hard for some people. The
transactions they build seem to based on some crazy assumptions. The
problem is that benchmarking is hard because you have to build enough
stuff to get a meaningful benchmark. Everyone thinks your done when
really, all you did was show that you've got a rotten design.

One reason is that people people roll their own ESB. There are many
nice ones, but they seem big, complex and expensive. Wikipedia has a
handy list of
`ESB <http://en.wikipedia.org/wiki/Enterprise_service_bus#Commercial_and_Open_Source_Vendors>`__'s
and vendors. Instead of using a purpose-built ESB, it seems sensible
to use the the web as an ESB. There's nothing wrong with using the
web as an ESB. What's wrong is assuming that the web has our
imaginary level of performance.

It appears that there are two assumptions people make. Here's what
happens.

Shoddy Design
-------------

They design a really complex web transaction and then complain.
Attributes of these complex web transactions:

-  They're part of the presentation, for example, a response to an HTML-based GET request. With a person watching it execute.

-  They involve aggregating information from other web services.

-  Sometimes, they involve multi-step workflows.

The complaints include the following:

#. It's slow. The user is forced to wait for a long time.

#. It's unreliable. Sometimes an information source doesn't respond at all.

So, the assumptions appear to be that the actual web is as
fast as your integration test mock web. And the actual web
is as reliable as your mock web.

Alternatives
------------

In the case that the transaction is an "order from stock"
(it involves competition for physical goods) then the user
must wait. When ordering books from inventory, or airplane
seats, or hotel rooms, the web site **must** display a
clever animation while it grinds away doing the transaction.

But, when the transaction is placing an order, or it
involves aggregating information, then there are better
things than making the user sit there and watch the
beach-ball spin while your transaction grinds away.

-   Make them wait while you grind. This is the "do nothing"
    solution; if it's slow or crashes, the user will
    complain.

-   **Queue Up a Work Request**. Tell the user you're
    queueing it up. Allow them to monitor the status of their
    queued work request.

-   **Pre-Cache**. We can often gather the expected
    information in advance and store it locally. When we're
    providing some kind standard information aggregates, we
    should gather it in advance.

Work Queues
-----------

The work queue is no different from an eBay auction. You
place an order or request and monitor the status.
Information aggregation shouldn't take a week; it should
be quick.

The user fills in their form, or uploads their request.
Your web transaction puts it into the queue, and gives
immediate feedback that it was accepted.

Your web site must include, therefore, a background
processor that actually handles the request. You can
spawn a "nohup" subprocess. You can have a "crontab"
schedule that checks the queue every minute. You can have
a proper daemon spawned by "init".

The background process dequeues the request, gathers the
data. It handles slow, timeout, crashes, etc. When it's
done, the status is updated. Maybe an email is sent.

Pre-Cached Data
---------------

Many applications aggregate data. Except in the rare case
that the data involves competition over physical goods
(inventory levels, current availability, etc.) the data
doesn't change constantly.

Indeed, many times the data is changed on a pretty slow
schedule. Weather forecasts, econometric data, etc.,
changes slowly. It's easy to query this data and cache it
locally. This gives the illusion of immediate response.

In some cases, the data may involve something like a
Twitter feed, where there is a constant flow of data, but
there's no competition over physical goods. Folks like to
wring their hands over getting the absolute
up-to-the-second Twitter information. This is, of course,
impossible because the Internet is (1) slow and (2)
unreliable. What does up-to-the-second mean when your
request is trashed by a momentary problem with your web
host's DNS server?

Even Twitter postings can be pre-cached. Polling the
Twitter server -- and caching the interesting tweets --
every few minutes will yield results that are every bit
as current as trying to get a "live" feed. Remember, the
folks tweeting have latency and unreliability at their
end. The Twitter servers have latency and unreliability.
Your web server has latency and unreliability. Your
user's browser has latency and unreliability.

High-Value Data
---------------

In some applications, the data is very high value.
Electronic Health Records, for example. Econometric Data
from commercial sources (see the `NABE
Tools <http://www.nabe.com/publib/links/tools.html>`__
page) for example. In the case of high-value data we have
to account for (1) slow and we have to resolve (2)
unreliable.

We can't fix slow. We have to handled it by a combination
of pre-caching and managing request work queues. Use Case
1: users make a standard econometrics request; we have
the current data that we've subscribed to. Done. Use Case
2: users make a non-standard request; we queue up the
task, we gather the information from sources, when we've
finished the job, we close the task and notify the user.

The unreliable is handled by service level agreements and
relatively simple work-flow techniques. When integrating
data from several sources, we don't simply write a dumb
sequence of REST (or SOAP) requests. We have to break the
processing down so that each source is handled separately
and can be retried until it works.

Background Processing Tier
--------------------------

This says that a standard web architecture should have
the following tiers.

#.  Browser.

#.  Presentation Tier. JSP pages, Django View Functions and Templates.

#.  Services Tier. An actual ESB. Or we can write our own
    Backend Processor. Either way, we must have a separate
    server with it's own work queue to handle long-running
    transactions.

#.  Persistence Tier. Database (or files). Your
    presentation and ESB (or Backend) can share a common
    database. This can be decomposed into further tiers
    like ORM, access and actual database.

You can try some other architectures, but they are
often painful and complex. The most common attempt
appears to be multi-threading. Folks try to write a
web presentation transaction that's multi-threaded and
handles the long-running background processing as a
separate thread. Sadly threads compete for I/O
resources, so this is often ineffective.

WSGI-Based ESB
--------------

Writing a REST+WSGI ESB (in Python) is relatively
straight-forward.

Use
`wsgiref <http://docs.python.org/library/wsgiref.html>`__,
or `werkzeug <http://werkzeug.pocoo.org/>`__. Create
the "services" as WSGI applications that plug into the
simple WSGI framework. Add authentication, URL
processing, logging, and other aspects via the WSGI
processing pipeline. Do the work, and formulate a JSON
(or XML) response.

Need your services tier to scale? Use
`lighttpd <http://www.lighttpd.net/>`__ or
`nginx <http://nginx.org/>`__ to "wrap" your WSGI
services tier. You can configure WSGI into nginx
(`link <http://wiki.nginx.org/NginxNgxWSGIModule>`__).
Also, you can configure WSGI into lighttd
(`link <http://redmine.lighttpd.net/projects/lighttpd-sandbox/wiki/Howto_WSGI>`__);
you can mess around with FastCGI configuration to
create multiple instances of the server daemon.

It's much, much easier to make the OS handle the
background processing as a separate heavy-weight
process. Apache, lighttpd or nginx can make the
background processor multi-threaded for you.



-----

Nice post. Some good stuff on Queue's and Pre-...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-03-08 11:43:26.748000-05:00

Nice post. Some good stuff on Queue's and Pre-Caching. Thanks.





