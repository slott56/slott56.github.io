The Python "Connection Reset By Peer" Problem
=============================================

:date: 2008-11-01 00:42
:tags: architecture,design
:slug: 2008_11_01-the_python_connection_reset_by_peer_problem
:category: Architecture & Design
:status: published







We've got a fairly complex application that fits the "broker" pattern.  It offers web services and it consumes web services.  It does some complex calculations of it's own and it's got a pretty complex database.



One thing I like to have is a "ready for deployment" test suite that exercises pretty much everything.  This is several layers of testing



-   Django Unit Tests

-   Python Unit Tests (for non-Django components)

-   Integration Tests (built on unittest.TestCase, but somewhat more complex)



It takes several minutes to run through the test sequence.



REST Integration Tests
----------------------



Some of our tests are pretty big REST tests.  We launch the Django "testserver" version of the server (with a known set of fixtures) and use a REST client to execute sequences of transactions.  



Sometimes we would get a urllib2 IOError which contained a socket.error (10054 on Windows, 104 in Linux).  Sometimes.



The text was "Connection Reset by Peer".  First, it was intermittent.  Second, we had bigger fish to fry.



This week, it became the long pole in the tent, and I dug into it.  Part of the reason is the count-down to deployment, and the resulting turnover to sysadmins.  But another part of the reason was that we have very stable software (finally) and we're starting to expand the unit tests to cover more obscure edge cases.



Consistently Intermittent
-------------------------



The most maddening thing about Connection Reset by Peer is the pattern of getting it.  And not getting it.



For a while, it appeared randomly.  Then we stopped getting it in development.  Problem fixed, right?



On VMWare, however, it was -- mostly -- reproducible.  On Windows, it never happened.  And yes, they're both Python 2.5.2.



Which Side?
-----------



We're debugging REST transactions.  Since we see it solidly under VMWare, let's dig in.  Which side?  From the logs, it  becomes clear that it's on the client side.  The Django server looks to be rock-solid.  When Django's WSGI server logs the status code and size of the response, this is followed immediately by flush and close.  No opportunity for something bad to happen to the socket.



So we're focused at our client, based on urllib2.  Sometimes we get it the error, sometimes we don't.  When we get it, however, it's in exactly the same point in the test sequence.   And under VMWare, we're getting it consistently enough that we can work with it.



Interestingly, as we move code around, the "Connection Reset By Peer" moves around.  When it occurs, it occurs in a consistent location in the test sequence.  



I've upgraded our client to retry the transaction.  Generally, a half-dozen retries (or fewer) and the transaction completes normally.



The Global Interpreter Lock
----------------------------



At this point, I'm convinced I've found something in Python itself.  Since we're running client, server, and MySQL database all under VMWare, I think we're looking at some small bug within urllib2.  I think it's threading.



I read up on the GIL.  The article by Aahz in PyZine, `Threading the Global Interpreter Lock <http://www.pyzine.com/Issue001/Section_Articles/article_ThreadingGlobalInterpreter.html>`_  has some notes on the way that time.sleep() changes thread scheduling.



When I changed the positions of time.sleep() calls in our client library or unittest sequence, the "Connection Reset by Peer" error moved, also.  It looks like we're suffering from some kind of interlock that's interfering with the client side of the socket.



The GIL is switched every 100 Python byte-code instructions.  That leads to very consistent behavior.  That's why it can be the same test in the test sequence or not at all.



So, now what?



Does It Matter?
---------------



Actually, I think it doesn't matter.  The all-on-one box testing is contrived.  With the retry loop, we can get to 100% success, it just takes a passel of retries.  For now, the log of connection reset retries is a side-light.  As we move toward scalability testing across multiple, independent boxes, we'll see if the problem persists.  





