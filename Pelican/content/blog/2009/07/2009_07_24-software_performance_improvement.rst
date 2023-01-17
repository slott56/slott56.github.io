Software Performance Improvement
================================

:date: 2009-07-24 09:49
:tags: software process improvement
:slug: 2009_07_24-software_performance_improvement
:category: Technologies
:status: published

Yesterday, I looked at some marketing material on SPI (Software Process
Improvement). It was quite good. The approach was very pragmatic, the
deliverables very sound.

The hard part is connecting with customers.

I've only worked with a few customers who were actually interested in
process *improvement*. I've worked with close to a hundred customers
who were interested in process *enforcement*, usually called
"compliance".

Laurent Bossavit's Learning Notes has this entry, filed under "`Four
types of process
errors <http://www.bossavit.com/pivot/pivot/entry.php?id=295>`__".


    Of course, what actually matters - what is worth discussing -
    is what people actually do. A 10-page process document or a
    flowchart are nice, but generally irrelevant unless they match
    very closely with what people actually do in the pursuit of
    shipping software.

In thinking about SPI, one has to find a way past the Core
Hubris™. Bossavit identifies four types of errors. His are all
focused on projects that "produce a bad outcome". We'll have to
put this on one bucket, the "problem recognized" bucket. We'll
rename Bossavit's Type I to Type IV as Type R-I to R-IV because a
problem was Recognized.

The Language of Denial
----------------------

What he misses are the process errors that "produce a questionable
outcome". In this case, the outcome can be declared good by the
manager that produced it (it went into production) or declared bad
by the manager that maintains it (quality is appalling.) These are
far, far more insidious and pernicious errors than the four he
ties to a bad outcome.

Delivery is all that matters, right? If it goes into production,
how "bad" can the outcome be?

The answer is -- sadly -- pretty bad. I'm often asked to work with
production code that should have raised red flags, been identified
as a bad outcome, and lead to serious questions about process
improvement. And yet, there's no question raised at all.

Worse, I'm often asked to follow the process that lead to the
horrifying code and the need for rework. What created the mess
we're reworking? A flawed process? Why, then, must our proposal
swear undying fealty to the broken process? So we can fail yet
again?

Even worse, we're sometimes asked to follow a process for which
there is no example. "Produce documentation like this," I'm told.
Followed by, "but that's not a good example of what I mean." It
turns out, there is no example of anyone ever following the
written process. But, we're expected (no required) to comply with
a process that has a nebulous definition and no examples.

Some Questionable Outcome Errors
--------------------------------

I think there are four variations on the theme of process errors.
We call this class "Q" errors because there was a questionable
result. Not a recognized problem but a shadow of a doubt.

-   Type Q-I error (blame) is when you don't follow the written
    process, produce a questionable outcome, and blame
    non-conformance. The point here is that we don't ask why the
    written process was not followed. Why is the actual process
    different? Is it a mistake, or is the written process unusable
    as written?

-   Type Q-II error (fudge) is when you don't follow the written
    process, produce a questionable outcome, and declare the
    situation to be exceptional. Either the technology was new or
    the business problem was not well understood. (Note. All
    interesting projects have one or both features. If the
    technology was understood and the business problem was
    understood, you could download an open source solution.)

-   Type Q-III error (denial) is when you don't follow the written
    process, produce a questionable outcome and ignore the gaps
    between written and actual. No proposed changes. Nothing. Just
    business as usual.

-   Type Q-IV error (insight) is when you don't follow the written
    process, produce a questionable outcome, and ask **two**
    questions. "What was so wrong with the written process that we
    didn't follow it?" and "What was wrong with what we actually
    did?" (Note. I've never seen this happen. But that's just me.)

Marketing Past the Hubris
--------------------------

There's a Core Hubris in many software development organizations.
It's a presumption that, since they have stuff in production, they
know how to deliver more stuff.

Indeed, in many organizations, SPI dies an early death because of
the Core Hubris. They already know what they're doing. They don't
need any help with *that*. This is why the blame-fudge-denial
errors are so common.

The Core Hubris is also why shoddy code goes into production.
There are three paths a project can take.

#.  **The High Road**. The processes mostly work, are mostly
    followed, and code is produced that has reasonable quality and
    gets delivered.

#.  **The Low Road**. The processes don't work well or aren't
    followed and code is produced that's questionable. It's put
    into production anyway, victory is declared and little, if
    anything is learned.

#.  **The Blocked Road**. The processes don't work or aren't
    followed and a bad result is produced. Almost without
    exception, this means the project is cancelled early. Deeper
    questions aren't asked because the reasons for cancellation
    aren't well understood by everyone involved. One day you're
    working, the next day you're reassigned.

Paths 2 and 3 (the Low Road and the Blocked Road) are both
places that need SPI. There are several marketing problems to
overcome.

Getting Help
------------

First, will they acknowledge the problem? Probably not. If
you've delivered anything -- no matter how bad -- you don't
need help. Further, you have two layers of the organization
that need to acknowledge the problem. Management needs to
recognize that they're wasting money on shoddy quality. Staff
needs to recognize that they've got quality problems.

Second, will they ask for help? Probably not. Most of the
process errors involve deflections or denials. To seek outside
support for something as "simple" as software development is a
defeatist attitude. It doesn't matter that software development
actually is very hard. What matters is that it *shouldn't* be
so hard, and asking for help is career suicide.

Third, will they follow through on the help? Probably not.
Change is disruptive. It means grumpy people complaining about
the 8:30 AM Scrum stand-up meeting. It means grumpy project
managers having only one or two sprints carefully planned down
to the last 6 minutes of activity, and the future sprints are
unplanned. It means grumpy business analysts complaining about
being forced to focus on just a few use cases and get those
right, leaving the "big picture" to fall into a black-hole. It
means grumpy DBA's complaining about an evolving data model. It
means grumpy programmers complaining that unit test code is not
deliverable and is a waste of time.

Management can -- and often does -- act schizophrenically
around improvements. They both (a) demand improvement and
simultaneously (b) demand that the improvements be subverted in
order to deliver "on time".

What to Sell
------------

I think the marketing message for SPI has to be something along
the following lines.

    Is your software actually perfect? Is maintenance easy? Is
    adaption and migration a simple administrative step?

    -   Are you sure? Do you have evidence? If not, perhaps your
        processes aren't as perfect as you wish.

    Do you scramble to deliver something that works? Is
    maintenance always more complex than you thought? Have you
    ever had to reverse engineer a system to replace it?

    -  You might want to consider improving your processes.

    Have you failed to deliver?

    -  You need to reconsider your processes.

    Do you have code that's both an asset and a liability?
    Is it so valuable you need to keep it in production,
    but it's in such bad shape that maintenance is an
    expensive nightmare?

    -   The root cause is process problems. Address the
        process issues and you should be able to reduce
        maintenance costs, or get better quality results
        for your maintenance spend.

 This, I think, is the target audience for SPI services. Most IT
 people think they're successful. I've seen their worst code,
 and I disagree.

 By *worst* I mean the following: **So valuable you can't throw
 it away and so broken you can't maintain it yourself**. This
 code is a costly, risky burden on the IT organization but still
 creates value for the enterprise as a whole. Flawed processes
 put it into production, and flawed processes prevents effective
 rework.

 The folks that understand that merely delivering may not be
 enough are the folks that might consider SPI services.



-----

Check out the article

Rethinking Software Ed Sper...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2009-08-04 20:34:19.671000-04:00

Check out the article
Rethinking Software
Ed Sperling, 07.27.09, 06:00 AM EDT
http://www.forbes.com/2009/07/25/parasoft-software-enterprise-technology-cio-network-parasoft.html
It is interesting when a business magazine like Forbes talks about
needing a use case and test case in order to be successful.




