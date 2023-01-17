A NoSQL Conversation
====================

:date: 2016-04-19 18:20
:tags: mongodb,SQL,noSQL
:slug: 2016_04_19-a_nosql_conversation
:category: Technologies
:status: published



This cropped up recently. It's part of a "replace Mongo with
Relational DB" conversation.



I'm going to elide the conversation down to five key points. The
three post-hoc nonsensical ideas, and the two real points.



What's (to me) very telling is that someone else published the five
reasons in this order. As if they larded three on the front. Or
included the two at the end out of guilt because they were avoiding
the real issues.



**Relational Queries are Desired**. "the only way to find [the
documents] would be to write a query that literally trolls through
the entire database in order to find the most recent values".



I beg to differ. "Only way" is a strong statement. Mongo has indexes.
To suggest that they don't exist or don't work is misleading. The
details of the use case involved searching by date. It's possible to
contrive a database that does bad searches by date; the implication
being that Mongo couldn't do date matching or something.



**To Enforce Constraints and Schema**. "It is still possible for the
application layer to ensure the constraint, but that relies on every
single point in the application code enforcing it – a single error
can lead to inconsistent data".



This runs perilously close to the "what if some bonehead bypasses the
API and hacks into the database directly?" question. Which is
isomorphic to "what if all corporate governance disappeared
tomorrow?" and "what if an evil genius hacks all our database
drivers?"



**Lack of Document-Oriented Access Patterns**.  "If there are more
complex access patterns (like reading certain fields from many
records, or frequently updating single fields within a record) then a
document-oriented database is not a good fit"



That's nonsense. Mongo has field-level updates. There was one example
of a long-running transaction that appeared to be mis-designed. I
suggested that an improved design might be less complex and expensive
than rewriting the API's and moving the data.





Desire to Utilize [Relational DB]
---------------------------------

**More Support Available for [Relational DB]**



Clearly, these last two are the real reasons. Everything above looks
like post-hoc justification for the real issue.


    We're not sure we like Mongo.



My point in the conversation was not to talk them out of making a
switch. The last two reasons included the kind of compelling
rationalization that can't be disputed.  The best I could do was to
challenge the errors in the first three reasons so that everyone
could be honest about the change. It's not technical. It's
organizational.








