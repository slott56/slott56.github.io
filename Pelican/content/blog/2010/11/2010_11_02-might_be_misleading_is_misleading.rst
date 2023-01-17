"Might Be Misleading" is misleading
===================================

:date: 2010-11-02 08:00
:tags: building skills books,#python,learning
:slug: 2010_11_02-might_be_misleading_is_misleading
:category: Technologies
:status: published

My books (`Building Skills in
Programming <http://homepage.mac.com/s_lott/books/nonprogrammer.html#book-nonprogrammer>`__,
`Building Skills in
Python <http://homepage.mac.com/s_lott/books/python.html#book-python>`__
and `Building Skills in OO
Design <http://homepage.mac.com/s_lott/books/oodesign.html#book-oodesign>`__)
develop a steady stream of email. [Also, as a side note, I need to move
them to the me.com server, Apple is decommissioning the homepage.mac.com
domain.]

The mail falls into several buckets.

**Thanks**. Always a delight. Keep 'em coming.

**Suggestions**. These are suggestions for new topics. Recently, I've
had a few requests for Python 3 coverage. I'm working with a
publisher on this, and hope -- before too long -- to have real news.

**Corrections**. I get a *lot* of these. A lot. Keep 'em coming. I
didn't pay a copy editor; I tried to do it myself. It's hard and I
did a poor job. More valuable than spelling corrections are technical
corrections. (I'm happy to report that I don't get as many of these.)
Technical corrections are the most serious kind of correction and I
try to fix those as quickly as possible.

**Source Code Requests**. No. I don't supply any source. If I send
you the source, what skill did you build? Asking for source? Not a
skill that has much value, IMHO. If you want to learn to program, you
have to create the source yourself. That *is* the job. Sorry for
making you work, but you have to *actually* do the work. There's no
royal road to programming.

The "Other" Bucket
------------------

I get some emails that I file under "other" because they're so funny.
They have the following boilerplate.

    "Code fragment [X] might is misleading because [Y]."

First, it's a complaint, not a question. That's not very helpful.
That's just complaining. Without a suggested improvement, it's the
worst kind of bare negativity.

The best part is that — without exception — the person sending the
email was not mislead. They correctly understood the code examples.

Clearly, the issue isn't that the code is "misleading" in the usual
sense of "lying" or "mendacious". If it was actually misleading, then
(a) they wouldn't have understood it and (b) there'd be a proper
question instead of a complaint.

Since they correctly understood it, what's misleading?

User Interface Reviews
----------------------

In software development, we used to go through the "misleading"
crap-ola in user interface reviews. In non-Agile ("waterfall")
development, we have to get every nuance, every aspect, every feature
of the UI completely specified before we can move on. Everyone has to
hand-wring over every word, every font choice, field order, button
placement, blah, blah and blah.

It seems like 80% of the comments are "label [X] might be
misleading". The least useful comment, of course, is this sort of
comment with no suggestion. The least useful reviewer is the person
who (1) provides a negative comment and, when asked for an
improvement, (2) calls a meeting of random people to come up with
replacement text.

[*Hint: If you eventually understood the misleading label, please
state your understanding in your own words. Often, hilarity ensues
when their stated understanding cycles back to the original label.*]

The "label [X] might be misleading" comment is — perhaps — the most
expensive nuisance comment ever. Projects wind up spinning through
warrens of rat-holes chasing down some verbiage that is acceptable.
After all, you can't go over the waterfall until the entire UI is
specified, right?

Worse, of course, the best sales people do not interpose themselves
into the sales process. They connect prospective customers with
products (or services). Really excellent sales people can have
trouble making suggestions. Their transparency is what makes them
good. It's not sensible demanding suggestions from them.

Underneath a "Might Be Misleading" comment, the person complaining
completely understood the label. They were not *actually* mislead at
all. If it was misleading, then (a) they wouldn't have understood it
and (b) there'd be a proper question instead of a complaint.

Thank goodness for Agile product owners who can discard the bad kind
of negativity. The right thing to do is put a UI in front of more
than one user and bypass the negativity with a consensus that the UI
actually is usable and isn't really misleading.

Might Be Misleading
-------------------

The "Might be Misleading" comments are often code-speak for "I don't
like it because..." And the reason why is often "because I had to
think." I know that thinking is bad.

I understand that Krug's famous `Don't Make me
Think <http://www.sensible.com/>`__ is the benchmark in usability.
And I totally agree that some thinking is bad.

There are two levels of thinking.

-  Thinking about the problem.

-  Thinking about the UI and how the UI models the problem.

Krug's advice is clear. Don't make users think about the UI and how
the UI models the problem. Users still have to think about the
problem itself.

In the case of UI labels which "Might Be Misleading", we have to
figure out if it's the problem or the UI that folks are complaining
about. In many cases, parts of the problem are actually hard and no
amount of UI fixup can ever make the problem easier.

Not Completely Accurate
-----------------------

One of the most common UI label complaints is that the label isn't
"completely" accurate. They seem to object to fact that a UI label
can only contain a few words and they have to actually *understand*
the few words. I assume that folks who complain about UI labels also
complain about light switches having just "on" and "off" as labels.
Those labels aren't "completely" accurate. It should say "power on".
Indeed it should say "110V AC power connected". Indeed it should say
"110V AC power connected through load". Indeed it should say "110V AC
15 A power connected via circuit labeled #4 through load with
ground".

Apparently this is news. **Labels are Summaries**.

No label can be "completely" accurate. You heard it here first. Now
that you've been notified, you can stop complaining about labels
which "might be misleading because they're not completely accurate."
They can't be "completely" accurate unless the label recapitulates
the entire problem domain description and all source code leading to
the value.

Apologies
---------

In too many cases of "Might Be Misleading," people are really
complaining that they don't like the UI label (or the code example)
because the problem itself is hard. I'm sympathetic that the problem
domain is hard and requires thinking.

Please, however, don't complain about what "Might Be Misleading".
Please try to focus on "Actually Is Misleading."

Before complaining, please clarify your understanding.

Here's the rule. **If you eventually understood it, it may be that
the problem itself is hard**. If the problem is hard, fixing the
label isn't going to help, is it?

If the problem is hard, you have to think. Some days are like that.
The UI designer and I apologize for making you think. Can we move on
now?

If the label (or example) really is **wrong**, and you can correct
it, that's a good thing. Figure out what is actually misleading.
Supply the correction. Try to escalate "Might Be Misleading" to
"Actually Mislead Someone". Specifics matter.

Also, please remember that labels are summaries. At some point,
details must be elided. If you have trouble with the concept of
"summary", you can do this. (1) Write down **all** the details that
you understand. Omit nothing. (2) Rank the details in order of
importance. (3) Delete words to pare the description down to an
appropriate length to fit in the UI. When you're done, you have a
suggestion.





