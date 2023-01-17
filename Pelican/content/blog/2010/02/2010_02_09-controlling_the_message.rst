Controlling the Message
=======================

:date: 2010-02-09 06:50
:tags: software process improvement
:slug: 2010_02_09-controlling_the_message
:category: Technologies
:status: published

I finally figured out what is so bad about folks who need to "control
the message."

Architecture is as much politics as technology. And some folks think
that political spin and message control is required. I think it's a
mistake because the urge to control the message points up a deeper
problem with the message itself.

Here's one of many examples of architecture being as much politics as
technology.

A really good platform for web development is Linux, Apache, MySQL,
Python, Django and mod_wsgi. Really good. Inexpensive, scalable,
simple, and reliable. Standards-compliant.

However, when a client asks what they should use, that's almost never
an acceptable answer. If the client is a VB/ASP shop, you can't tell
them to ditch their installed technology. You can suggest looking at
C# and ASPX and .NET, but even that simple change is going to get you
into arguments over the upgrade costs. Many times customers just want
Pixie Dust that magically makes things "better" without being a
disruptive change.

("What about the personnel cost of a change? You can't ignore the
people" Yes, actually, I can. Those people where **not** considered
when VB and ASP were introduced. If they were, they'd still be using
COBOL and CICS. Why consider them now when it's time to make another
change? The "personnel cost" question is an excuse to veto change.
The people will be more productive using C#. Start changing, stop
preventing.)

Right vs. Wrong
---------------

I've been told that politics comes first when making a technical
decision. That's perhaps the dumbest, most defeatist attitude I've
ever heard (and I told them that, more than once.) There **are**
right answers. There are -- in some cases -- answers that are
*absolutely* right, but a political problem.

Anyone who puts politics first rejects the opportunity to know what's
right. It's essential to have facts and evidence for the technically
right answer, even if you never use those facts, and simply accept
the politically-determined sub-optimal answer.

And there's no reason to be a jerk about political decisions. They
may be bad decisions made for political reasons. They may be good
decisions made for the wrong reasons. Your hard-won technical input
may get disregarded. Publish your findings and move on.

My number one example of this is the slowness of most stored
procedure languages. Benchmarks reveal that they're slow when
compared with Java or even Python. That shouldn't be a surprise, but
the politically-motivated response is that Stored Procedures *have* a
place and *will* be used in spite of the problems. Politics trumps
technology.

Controlling the Message
-----------------------

In my trips to the top of the IT food chain -- the CIO's office -- it
seems like everything is political. It may not be, but the technical
content is approximately zero and is often diluted by the political
considerations of influence, favors and power.

I'm sure this is sampling bias. I don't meet a lot of CIO's. And I
don't meet them to talk about things on which they are already deeply
knowledgeable. I'm there because folks are lost and struggling.

The thing I like least, however, is any "Controlling the Message"
part of the discussion. It happens in governmental politics as much
as it happens in technology. In government, it's particularly odious.
Elected officials often have separate public and private messages.
They have a public message that is nothing more than pandering to the
"shouting class" at the party fringe.

Why Control It?
---------------

Here's my lesson learned. If you need to control the message, then
the message itself is flawed.

If the communication "requires appropriate background", or if the
remarks "could be misinterpreted if taken out of context", then the
message is inappropriate or -- perhaps -- wrong.

Here's an example. We're talking about teaching C programming. The
customer says "We're not planning on re-educating a lot of our
existing staff, we're mostly going to train the new hires." This
message needed to be "controlled".

Why can't we simply say that we're going to teach C to new hires?

Because that message is fundamentally flawed. So it needs to be
controlled to hide the flaws.

If you think you need to control your message, take the hint and
rethink your message.





