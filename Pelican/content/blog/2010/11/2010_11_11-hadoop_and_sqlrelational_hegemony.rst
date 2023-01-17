Hadoop and SQL/Relational Hegemony
==================================

:date: 2010-11-11 08:00
:tags: RDBMS,hadoop,map-reduce
:slug: 2010_11_11-hadoop_and_sqlrelational_hegemony
:category: Technologies
:status: published

Here's a nice article on why Facebook, Yahoo and eBay use Hadoop:
"`Asking Any Question Of All Your
Data <http://www.forbes.com/2010/11/05/facebook-yahoo-ebay-technology-hadoop.html>`__".

The article has one tiny element of pandering to the SQL hegemonists.

Yes, it sounds like a conspiracy theory, but it seems like there
really are folks who will tell you that the relational database is
effectively perfect for all data processing and should not be
questioned. To bolster their point, they often have to conflate all
data processing into one amorphous void. Relational transactions
aren't central to all processing, just certain elements of data
processing. There, I said it.

Here's the pandering quote: "But this only works if the underlying
data storage and compute engine is powerful enough to operate on a
large dataset in a time-efficient manner".

What?

Is he saying that relational databases do not impose the same
constraint?

Clearly, the RDBMS has the same "catch". The relational database only
works if "...the underlying data storage and compute engine is
powerful enough to operate on a large dataset in a time-efficient
manner."

Pandering? Really?
------------------

Here's why it seems like the article is pandering. Because it worked.
It totally appealed to the target audience. I saw this piece because
a DBA -- a card-carrying member of the SQL Hegemony cabal -- sent me
the link, and highlighted two things. The DBA highlighted the
"powerful enough" quote.

As if to say, "See, it won't happen any time soon, Hadoop is too
resource intensive to displace the RDBMS."

Which appears to assume that the RDBMS isn't resource intensive.

Further, the DBA had to add the following. "The other catch which is
not stated is the skill level required of the people doing the work."

As if to say, "It won't happen any time soon, ordinary programmers
can't understand it."

Which appears to assume that ordinary programmers totally understand
SQL and the relational model. If they did understand SQL and the
relational model perfectly, why would we have DBA's? Why would we
have performance tuning? Why would we have DBA's adjusting
normalization to correct application design problems?

Weaknesses
----------

So the weaknesses of Hadoop are that it (a) demands resources and (b)
requires specialized skills. Okay. But isn't that the exact same
weakness as the relational database?

Which causes me to ask why an article like this has to pander to the
SQL cabal by suggesting that Hadoop requires a big compute engine? Or
is this just my own conspiracy theory?





