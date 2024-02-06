Not the first time...
=====================

:date: 2003-12-13 19:23
:tags: technologies,xml
:slug: 2003_12_13-not_the_first_time
:category: Technologies
:status: published





From an email I got recently, lightly edited.  Responses to follow



**Problem**: The data layer of application architecture must be flexible enough to adapt to
virtually any new data-driven functional requirement demanded by today's
client..right...well to support such adaptability in client deployments, the
data model must allow almost arbitrary categorizations and groupings of data
within the system without hindering development speed, system response time,
ease of use and system simplicity.




**Proposed Architecture**: I am really started to
take a liking to Java/XSLT that is driven by XML...well here is my
thinking:

1.  Client requests can
    easily be transformed into client-independent XML
    structures

2.  EAI tools or APIs could
    handle both receiving and transmitting events via
    XML

3.  SQL result sets can possibly
    be naturally modeled as XML
    fragments

4.  The XML tree fragments
    returned from the API and database queries may be used to generate dynamic
    queries.

5.  Client side response
    should first be represented as XML to capture the data structure. Of course this
    XML could be converted to whatever format required by the
    client



Benefits
--------

1.  Both data and events are naturally modeled in a similar structure:
    XML

2.  A single tool, XSLT, is able
    to transform and generate both data and
    events

3.  Using a standard XML format
    for both incoming client requests and outgoing response allow clean client
    independence.




Weaknesses
------------

1.  No interactive debugging tools. However this could be mitigated by extensive
    debug logging by the application
    server.

2.  XSLT is a recursive
    functional language and requires you to adapt a new methodology other than
    object oriented.

3.  Abstraction
    hurdles would not be enforced by the interpreter but possibly with superb coding
    discipline. 








