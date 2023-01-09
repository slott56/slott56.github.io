An Epic Fail Example
====================

:date: 2017-06-06 08:00
:tags: fail,epic fail,design
:slug: 2017_06_06-an_epic_fail_example
:category: Technologies
:status: published

What's the most Epic Fail I've ever seen?
I was a traveling consulting for almost 35 years. I saw a lot. I did
learn from epic fail scenarios. But. I haven't really spent a lot of
time thinking about the lessons learned there. I never have a glib
answer to this question. Mostly because the stories are incomplete: I
came in during a awful mess and left and it was still an awful mess. No
arc. No third act. No punchline.
These aren't really stories as much as they're vignettes -- just sad
fragments of some larger tragedy. Consequently, they don't leap to front
of mind quickly.
One example is a smallish company that had built some pretty cool
software in MS-Access. They had created something that was narrowly
focused on a business problem and they were clever, so it worked. And
worked well.
They leveraged this success, solving another major business problem. In
MS-Access. Clever. Focused on real user's real needs. It doesn't get any
better than that.
Well, of course, it does get better than that.
They replicated their success seven times. Seven interlocking MS-Access
databases. They had subsumed essentially all of the company's
information and data processing. Really. It's not that hard to do.
Companies buy General Ledger software that doesn't really do very much.
You can write a perfectly serviceable ledger application yourself. (Many
people ask "why bother?")
When I talked with them they had finally been swamped by the inevitable
scalability problem. They had done all the hackarounds they could do.
Their network of MS-Access servers and interlocked cluster of databases
had reached it's limit of growth.
Unsurprisingly.
Questions I did not ask at the time: Who let this happen? Who closed
their eyes to the scalability problem and let this go forward? Who
avoided the idea of contingency planning? How do you back this up and
restore it to a consistent state?
They were in a world of trouble. I told them what they had to do and
never saw them again. End of vignette.
(In case you want to know... I told them to get a real server, install
SQL-Server, and migrate each individual MS-Access table to that central
SQL-Server database, replacing the Access table with an ODBC connection
to the central DB. This would take months. Once every single database
was expunged from MS-Access, they could start to look at a web-based
front-end to replace the Access front-end.)
There are others. I'll have to ransack my brain to see if I've got other
examples.





