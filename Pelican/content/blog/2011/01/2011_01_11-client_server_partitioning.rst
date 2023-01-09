Client-Server Partitioning
==========================

:date: 2011-01-11 08:00
:tags: REST,architecture
:slug: 2011_01_11-client_server_partitioning
:category: Technologies
:status: published

I have slowly grown to love RESTful web services.

I was asked about a nearly empty section in the code repository
labeled "Java client".

"Yes," I said, "it's a place-holder for a Java package that includes
classes to wrap our RESTful web services."

"Really?" I was asked, "Why? We use FLEX for the client, not Java
Applets."

"Today we use FLEX. In the past, we weren't sure. We have a complete
Python client library. Indeed, the original concept was to support
our customer's building their own web site to use our web services.
The Java package would plug into a J2EE web app. No one wanted that,
so we built FLEX clients instead."

Then they said that the super-clean separation between all these
clients and the RESTful server was taking "flexibility to a whole new
level."

I pointed them to this. `EWD340: The Humble
Programmer <http://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html>`__.
It has this killer quote:

    The competent programmer is fully aware of the strictly limited
    size of his own skull; therefore he approaches the programming
    task in full humility, and among other things he avoids clever
    tricks like the plague.

I find that this really helps keep the focus on simplicity. I suppose
that it leads to flexibility, but that's not the real point. The real
point was simplicity.





