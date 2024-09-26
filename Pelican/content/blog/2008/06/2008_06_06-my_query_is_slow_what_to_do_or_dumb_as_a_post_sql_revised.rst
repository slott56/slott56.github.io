My Query Is Slow -- What To Do?  Or Dumb-As-A-Post SQL (Revised)
================================================================

:date: 2008-06-06 22:30
:tags: database,jquery,sql,design
:slug: 2008_06_06-my_query_is_slow_what_to_do_or_dumb_as_a_post_sql_revised
:category: Python
:status: published







First, let me point out that the Data Cartel ("DBA" means Don't Bother Asking) won't release all the information I requested, so some of this is a guess.



We'll look at a number of dumb-as-a-post SQL techniques.  This is proof -- if any were needed -- that bad SQL is worse than no SQL.



The table appears to have 2 columns, a date and a floating-point value in the range 0.0 to 1.0.  Rows arrive at the rate of 500 an hour.  



Someone wants a weekly summary (about 90,000 rows) binned into 10 ranges 0.0 to 0.1, 0.1 to 0.2, 0.2 to 0.3, etc.  The algorithm might be slightly more complex (to separate :math:`n = 0.1` from :math:`0.1 < n \leq 0.2`.)



[Again, the DBA steadfastly refuses to provide the use cases, so I'm doing a lot of this with minimal information.  However, I did get a spreadsheet showing an Excel version of the algorithm.  Not PL/SQL, not pure SQL, not Java, but Excel.]



What's the Issue?
-------------------



The issue is that some programmers can't be trusted to find their ass groping with both hands.  I was sent three versions of the obvious SQL query, each more contrived and senseless than the last.



I was asked -- really -- "What is a more scalable approach to the problem ?".  "Scalable"? WTF?  Scalable with respect to what?  Rows?  Physical I/O's?  Elapsed Time?  CPU use?  User queries?  Web page hits?  Shots of Tequila?  If I look at the `Zachman Framework <http://www.zifa.com/>`_  or the `SEI Quality Measures Taxonomy <http://www.sei.cmu.edu/str/taxonomies/view_qm_body.html>`_ , I can come up with at least a half-dozen more dimensions of potential "scalability".



[Yes, I asked.  No, I didn't get an answer.  "Scalability" appears to mean the same thing as "Better".]



I'm assuming that the volume has increased or something, and the old query isn't fast enough.  Or something.  There's a claim that some query is run 83 million times each week; that's 138 times per second, a number I just don't believe.



Fetishize a Feature
-------------------



Someone has an Oracle Bulk Bind fetish.  I've listened to this tripe before.  There are probably places where it helps.  I haven't seen any, but I haven't really made a study of the feature.   Apparently, they couldn't get it to work for the required 80,000 rows.  It gets what they call "the standard ORA-04030 error."  



The sent me a copy of solution one: a big pile of PL/SQL including some BULK COLLECT stuff.  PL/SQL they couldn't get it to work.  I'm not sure what's going on here, but it's clearly the first dumb-as-a-post SQL programming technique:  **Fetishize a Feature**.  You pick something and stick with it.  



Drown it in Documentation
--------------------------



Here's the best part of solution one.  It didn't work.  And they provided me with extensive documentation -- on the feature they couldn't get to work.  I like that.  So technique two is to quote a lot of documentation -- as if **Drowning It In Documentation**  somehow make the feature start working.



I suppose I could try and debug it, but I really don't have the patience.  There are simpler, provably faster techniques.  Why debug something that is highly Oracle-specific, and doesn't seem to work very well?



Write More Code
----------------



Solution two was to purge the bulk-bind syntax from solution one and see if a big pile of PL/SQL will work.  PL/SQL is a demonstrably slow platform.  There are some anecdotal stories of applications that were made faster by replacing external application programs with PL/SQL.  I believe that those stories involve comparing the performance of a Bentley with an Etap 37S.  One's a car, the other's a boat.  PL/SQL is faster when you change your application design to make better use of PL/SQL features.



In this case, the PL/SQL solution is a huge amount of code for something that is -- as far as I can tell -- a SELECT COUNT(*) GROUP BY operation.  It's hard to be completely sure, since the code is bad, and obscures the intent.



Rather than summarize and simplify, they **Wrote More Code**.



Don't Do The Obvious
---------------------



Another generally dumb technique is to avoid writing the obvious SQL because -- well -- I don't know why.  I don't have the actual requirements.  However, each example strives to produce one line of output with the frequency table spread out horizontally.  This is fairly hard to do in SQL, and requires lots of copy and paste programming to repeat the CASE expressions over and over again.



The basic SELECT COUNT(*) GROUP BY produces a number of rows, each of which has a key and a count.  This can be rotated into a horizontal configuration by a reporting program.  For some reason, we're locked into a single form for the report, making it so we can't **Do The Obvious**.  



Refuse to Change the Structure
-------------------------------



Data structures and algorithms are two complementary sides of the same coin.  You can't fix the algorithm without fixing the data structure, and vice versa.  In this case, the table design was bad, but no one seemed prepared to fix it.



About a year ago, I had told a member of data cartel to read Ralph Kimball's Data Warehouse Toolkit.  They claimed they read it.  Since they got nothing out of it, I'm not sure what they meant by "read".  Data warehouse folks know that you have to denormalize for reporting.  A relentless focus on "normalization" -- when dealing with non-updatable reporting-only data -- is simply wrong.



In this case, the floating point numbers had to be split up into bins.  The calculation must be done at load time, and must be a permanent part of the table.

::

    TABLE data(
    time DATETIME,
    value FLOAT );





This isn't really sufficient for reporting.  You need something more like the following:

::

    TABLE data(
    time DATETIME,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    value FLOAT,
    bin INTEGER );





The various derived values are all trivial to calculate at load time.  Once they're calculated, your query reduces to a trivial SELECT bin, COUNT(*) FROM DATA GROUP BY bin.  It isn't the absolutely fastest way to process the data, but it's a far, far sight faster than on-the-fly CASE expressions or PL/SQL loops.



The Hubris of Time Calculations
--------------------------------



There's more that's wrong in the various examples I was sent.   Specifically, they use "closed-ended date ranges".  A serious mistake that is caused by simple hubris.  Time is subtle and complex and easy to get wrong.



Here's their code.

::

    time >= TO_DATE( '05/01/2008 00:00:00', 'MM/DD/YYYY HH24:MI:SS') AND
    time <= TO_DATE( '05/08/2008 23:59:59', 'MM/DD/YYYY HH24:MI:SS');





It can't -- in general -- work.



There's a 1-second gap between the two times.  You have use half-open intervals to avoid losing a row that happens to have a timestamp in the gap.  [Don't waste time adding .999's, either, because the decimal value doesn't provide down-to-the-last bit way to encode the internal binary values.]

::

    time >= TO_DATE('05/01/2008','MM/DD/YYYY')
    AND time < TO_DATE('05/08/2008','MM/DD/YY' )





This has NO gap. 



However, this still isn't very good.  As shown in the table definitions above, you need to denormalize the time-stamp into the buckets you actually want to use for selection and grouping.



Real Speed
-----------



I don't have the table or sample data, so I can't compare my results with their performance numbers.  However, their numbers are sad.



First, they couldn't get the bulk bind to work, but sent me the code, as if it mattered.



Second, their massive PL/SQL loop ran for an hour.  Apparently, this is unacceptable, but they sent me the code, as if it mattered.  Which is sad.



Third, their SQL GROUP-BY with all the CASE expressions ran in 12 minutes.  I don't know if that's too long or uses too much memory or takes too many tequila shots.  



The real SELECT COUNT(*) GROUP BY, with denormalized data, is fast.  On my little 1Gb RAM, 1.7Ghz Dell, running Fedora Core 8 and using SQLite, a basic SELECT COUNT(*) processes 100,000 records in about 3 seconds.



That's about as fast as this little drip of code.


::

    import collections
        count= collections.defaultdict(lambda:0)
        for row in q.execute().fetchall():
            b, exact = divmod( int(row[1]*100), 10 )
            band= "==0.%d"%(b,) if exact == 0 else "0.%d-0.%d"%(b,b+1)
            count[band] += 1
        print count





In SQLite, for 100,000 rows, this is the same speed as SQL.  Why?  Because we're not asking the database to do anything much more than fetch rows.



Interestingly, in Oracle, the ``SELECT COUNT(*) GROUP BY`` is much, much faster.  Why?  Because Oracle queries involve a context switch, where SQLite does not.  A simple fetch loop in Oracle is relatively slow without using some kind of buffering.



The database fetch time still dominates what we're doing.  A table design change, and doing all processing at load time will minimizes the query time.



How Many Bad Things Can We Do?
-------------------------------



Let's enumerate them:



- **Fetishize a Feature**



- **Drown It In Documentation**



- **Write More Code**



- **Refuse to Change the Structure**



- **The Hubris of Time Calculation**



All of these habits get in the way of a simple denormalization that makes the obvious query work at amazing speeds.




