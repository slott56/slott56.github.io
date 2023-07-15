Name Matching Alternatives
==========================

:date: 2009-05-21 17:05
:tags: metaphone,soundex,regular expressions,software design,SQL
:slug: 2009_05_21-name_matching_alternatives
:category: Technologies
:status: published


The users want to locate people by last name.  They want flexible
matching.  That's not very hard.

The DBA wants to do some wild-card searches efficiently.  The DBA may
not be responding to the users actual request, making this more
complex than it needs to be.

I'm not in contact with the users, so I don't know the real
requirements.  I'm hearing this through the DBA-filter ("all singing,
all dancing, all SQL".)  I may also be hearing this through IT
management filter ("only use technology I recognize from my
programming days".)

In my experience, wild-card searches are rarely the user's first
choice.  They want more flexible matching.  While the SQL LIKE-clause
is one solution that might work, it is rarely what the users really
want.

The DBA knows that the SQL LIKE-clause effectively defeats indexing
and forces row-by-row comparison.  And we all know that row-by-row
processing is evil.

Premature Optimization
----------------------

Question 1.  Is this premature optimization?

There's no way to tell.  The database server may be beefy enough and
the query rare enough that a basic LIKE-clause regular expression
will work just fine.

Step 1.  Benchmark this baseline solution.

As Fast as Possible -- in SQL
-----------------------------

One way to find names quickly is to denormalize the data base.  In
addition to the proper names, also store the soundex of the name.
Since this is stored, and there's no function call in the WHERE
clause, and this is fully indexed, it will find "similar-sounding"
names very quickly.

Soundex has limitations, so some folks use
`metaphone <http://forums.oracle.com/forums/thread.jspa?messageID=1304206>`__.
The principle is the same.  When inserting or updating the name,
also insert (or update) the metaphone of the name.

This, BTW, does not involve any wild-card.  Except in unusual cases,
it always returns a set of candidates.  And the set of candidates is
a better fit than any wild-card search.   More focused, and the whole
name is considered.

Step 2.  Prototype the soundex solution.  It's hard to explain, and
impossible to visualize.  Actual result sets make it concrete.
Throw Memory At It

Here's an alternative that works really well.

Stop using the database.

Don't waste brain cells trying to write this kind of super-flexible
search in SQL. It's better done in code.  Write a simple materialized
view with name and PK and nothing else.  Create the smallest possible
table that can be used just for name matching -- nothing else in this
table.  It's little more than an index.

Write a simple web service that queries this physically small table,
doing a search algorithm.  The web service will locate near-matches
in this small table.  It could return full rows for the top matches,
or simply return the names and PK's for users to pick from.

You have several candidate algorithms for this server.  A
wisely-written web service can use a combination of algorithms and
return a match score along with the names and PK's.

-  Soundex/Metaphone match.

-  `Levenshtein distance <http://en.wikipedia.org/wiki/Levenshtein_distance>`__.

Web Service for Wildcards
--------------------------

An alternative web service can query the name/PK table using a
nice regular expression library.  Since RE syntax can be complex,
you would translate from a user-friendly syntax to a proper RE
syntax.

For instance, the LIKE-like syntax can be reformulated to proper
RE syntax.  The %'s become .\* and the \_'s become .'s.  Or
perhaps you offer your users shell-like syntax.  In this case, the
\*'s become .\* and the ?'s become .'s.

Either way, the user's wild-card becomes a proper regular
expression.  The web service queries the table, matching all input
against the RE.  The service could return full rows for the top
matches, or simply return the names and PK's for users to pick
from.

This little web service can be granted a large amount of memory to
cache large row sets.  Boy will it be fast.

Also, depending on the pace of change in the underlying table, it
may be possible for this service to query all names into a cache
once every few minutes.   Perhaps it can do this by first making a
SQL request to refresh the materialized view and then a query to
fetch the updated view into memory.

What the DBA wants
-------------------

The DBA wants some magical pixie dust that somehow makes a query with
a LIKE clause use an index and behave like other properly indexed
columns.

The actual email enumerated four of the possible ways a LIKE clause
could be used.  I'm guessing the hope was that somehow the
enumeration of a subset of candidate LIKE clauses would help locate
the pixie dust.

Here's my advice.  If this magical LIKE clause feature already
existed, it would be in the DBA guide.  Since it isn't in the DBA
guide, perhaps it doesn't exist.   Enumerating four use cases (name,
\*name, name\* and \*name*) doesn't help, it's still not going to
work out well.  Remember, SQL's been around in this form for decades;
the LIKE clause continues to be a challenge.

First, benchmark.  Second, offer the users soundex.  Then, well,
you've got work to do.





