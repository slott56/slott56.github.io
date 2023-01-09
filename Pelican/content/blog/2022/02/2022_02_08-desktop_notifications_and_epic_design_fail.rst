Desktop Notifications and EPIC DESIGN FAIL
##########################################

:date: 2022-02-08 08:00
:tags: notification,workflow,#python
:slug: 2022_02_08-desktop_notifications_and_epic_design_fail
:category: Technologies
:status: published

I was asked to review code that -- well -- was evil.

Not like "shabby" or "non-pythonic". Nothing so simple as that.

We'll get to the evil in a moment. First, we have to suffer two horrible
indignities.

1. Busy Waiting

2. Undefined Post-Conditions.

We'll beat all three issues to death separately, starting with busy
waiting.

Busy Waiting
============

The Busy Waiting is a sleep-loop. If you're not familiar, it's this:

::

   while something has not happened yet AND we haven't timed out:
       time.sleep(2)
       

Which is often a dumb design. Busy waiting is polling. It's a lot of
pointless doing something while waiting for something else.

There are dozens of message-passing and event-passing frameworks. Any of
those is better than this.

Folks complain "Why install ZMQ when I could instead write a
busy-waiting loop?"

Why indeed?

For me, the primary reason is to avoid polling at fixed intervals, and
instead wait for the notification.

The asyncio module, confusing as it is, is better than polling. Because
it dispatches events properly.

This is minor compared with the undefined post-conditions.

Undefined Post-Conditions
=========================

With this crap design, there are two events. There's a race between
them. One will win. The other will be silently lost forever.

If "something has not happened" is false, the thing has happened. Yay.
The while statement ends.

If "something has not happened" is true and the timeout occurs, then
Boo. The while statement ends.

Note the there are two, unrelated post-conditions: the thing has
happened OR the timeout occurred. Is it possible for both to happen?
(hint: yes.)

Ideally, the timeout and the thing happening are well-separated in time.

Heh.

Otherwise, they're coincident, and it's a coin-toss as to which one will
lead to completion of the while statement.

The code I was asked to review made no provision for this unhappy
coincidence.

Which leads us to the pure evil.

Pure Evil
=========

What's pure evil about this is the very clear statement that there are
not enough desktop notification apps, and there's a need for another.

I asked for justification. Got a stony silence.

They might claim "It's only a little script that runs in the Terminal
Window," which is garbage. There are already lots and lots of desktop
apps looking for asynchronous notification of events.

Email is one of them.

Do we really need another email-like message queue?

(Hint: "My email is a lot of junk I ignore" is a personal problem, not a
software product description. Consider learning how to create filters
before writing yet another desktop app.)

Some enterprises use Slack for notifications.

What makes it even worse (I said it was pure evil) was a hint about the
context. They were doing batch data prep for some kind of
analytics/Machine Learning thing.

They were writing this as if Luigi and related Workflow managers didn't
exist.

Did they not know? If they were going to invent their own, they were off
to a really bad start. Really bad.





