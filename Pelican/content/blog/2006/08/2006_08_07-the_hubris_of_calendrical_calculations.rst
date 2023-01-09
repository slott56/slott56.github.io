The Hubris of Calendrical Calculations
======================================

:date: 2006-08-07 13:34
:tags: architecture,design,data structure,algorithm
:slug: 2006_08_07-the_hubris_of_calendrical_calculations
:category: Architecture & Design
:status: published





Here's the
example:



"I need to calculate first
'business day' of the month.  Last 'business day',
too."



Note that the problem which this
solves is unstated.  Why does anyone need to "calculate" this? 




Here's a single tidbit of technical
context, not useful really, but all I know: it's a polyglot environment with
.NET and Java.



**Worst Solution.** 



A PL/SQL package called
"date_calculations" is perhaps the worst possible implementation.  Why is this
so bad?



First, and foremost,
**it duplicates existing information** , stored elsewhere in the
organization.  I don't even need to ask if there's a business calendar in a
database.  The General Ledger application (among others) has a business
calendar, which has these facts in it.  The calendar is often a table, and can
be queried trivially.  



If you -- for
inexplicable reasons -- must wrap everything in a slow, complex and error-prone
stored procedure, you can write a PL/SQL package which queries this table.  Then
your Java or .NET objects can use that stored procedure to construct the
necessary object.  (I love the indirection of doing Object-Relational Mapping
through a stored procedure, the pointless wasted time and processing appeals to
me.)



The second reason this is so bad
is that **it attempts to impose business rules on something that is the province of hand-wringing policy-makers** .  While several months have
ordinary, simple rules for 'first business day', January and September are often
complex.  There are Federal rules for the New Years Day holiday.  Further, when
New Years Day falls on a weekend, it may be celebrated on the following Monday. 
Just to compound this, the fiscal year may actually end on December 30 or 31 or
Jan 1 or 2 in order to make four full 13-week periods: what does this mean
regarding first business day of the
"month"?



Can you really codify all of
the subtlety of the orbit of the planet, US federal and state law, GAAP, and
business policy in a stored procedure?  What's wrong with a table that simply
lists this information?



The third
reason is **it requires the overhead involved of JDBC/ODBC connections for a relatively simple one-shot Q&amp;A** .  If you've already got an RDBMS
connection open, then it isn't so bad.  But -- check above -- the problem is
free of useful context, so we just don't know if this is appropriate or
not.



The fourth reason is
**the vague (and misleading) name of the package** .  "date_calculation" is far from true.
It answers two questions about the business calendar.  The package happens to
use dates, but doesn't really do much
calculation.



**A Better Approach.** 



Since the problem is (a)
unstated and (b) free of usable context, it's challenging to propose a better
approach.  However, there are some universal truths about the calendar that
point to an approach that makes sense almost all of the
time.



A table.  Yes,
**load the business calendar into a table** , and use that table.  The calendar is a
complex fact, touched by many people, and the rules are nearly impossible to
codify.  When confronted with that kind of complexity, punt.  Just put in a
table.



Two stupid (yes, stupid)
objections I've heard: **the storage**  and
**the performance** .  The storage is a ridiculous
objection.  Let's say we explode each date into a 9-tuple of facts about that
date (year, month, day, day of week, day of year, quarter, day of quarter,
business day, holiday).  With the exception of year, these are tiny numbers.  We
have a bunch of one- and two-digit fields plus a four-digit field.  Let's punish
ourselves and allocate 80 bytes for this to include every possible overhead,
large numbers, everything.  Let's store dates for the entire 80-year history of
the company, plus the next 200 years into the future.  That's 280 years x 365.25
date records x 80 bytes = 8Mb.  That's 8 Mb of date information.  Why are we
talking about the storage?  



If you
think 8Mb matters, then price 80Gb disk drives.  At roughly $1/Gb, this is
$0.008 of storage.  Almost a penny's
worth.



The second objection is
performance of the table.  This question presumes that somehow a 102,000 row
table is profoundly slow and cannot be indexed, while a 7M row customer table is
the price of doing business.  If the 102,000 row table is intimidating, then
only put in a few decades of dates, and cut down to 7,300 rows of date
information.   Our candidate query needs year and month to locate the first
business day of the month.  Since we'll be doing this for the "current" month,
that cluster of rows is likely going to get pinned into
cache.



If you still think that a 7,300
row table is slow (and you can't run any performance tests to prove that indexes
really are fast), you can write a PL/SQL procedure to cache the results, and
feed them back when asked.



If you still
think that a table is slow, try getting out of the mental box you're in.  Your
LDAP server can provide this information.  Define a schema for the business
calendar and a domain into which you place dates, not people.  Weird, but really
fast if you use a no-binding
connection.



If you still think that a
table is slow, try writing a special-purpose Servlet and put it on a web server
somewhere.  It can cache all kinds of calendar information and respond to very
simple GET queries with a text response (not HTML) that has just the relevant
date.



**Bottom Line.** 



The bottom line on dates is
this:  **The Business Calendar is Static: Calculation is Silly** .



Why
is calculation silly?  Things don't change; the "first business day" is a
persistent fact.  While derived from complex rules, it doesn't change once it's
established.  Further, there are so few instances of this fact, that a
calculation isn't really
appropriate.



What we're doing, in
essence, is reconstructing a Date object.  We have a Calendar which is a
container for Dates.  Any given Date is associated with a number of other dates,
including "first business date in the same month", and "last business date in
the same month."  We simply want these persistent objects reconstructed in our
program.  They can be shelved, hibernated, serialized, fetched from a relational
database by an Object-Relational Mapping, or brought in via Container Managed
Persistence.



We aren't "calculating"
anything.  We're chasing a simple
relationship.



We need to have a
Calendar object with Calendar Month and Business Month containers.  We want to
work with a Business Month container, examining the individual Date objects. 
These -- in general -- should just come from the database through simple
queries.








