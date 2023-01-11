Open-Ended Date Ranges -- The "From Here to Eternity" Problem
=============================================================

:date: 2008-02-02 03:01
:tags: architecture,design,data structure,algorithm
:slug: 2008_02_02-open_ended_date_ranges_the_from_here_to_eternity_problem
:category: Architecture & Design
:status: published







There aren't too many variations on the open-ended date range problem.  We have a table of events or rules or policies that have start dates.  Some have end dates, because they've been replaced or superseded.  Others don't have end-dates because they apply for the foreseeable future.



There are two kinds of date ranges here: close-ended and open-ended.  The close-ended date ranges have a start and a duration (or a start and an end).  The open-ended date ranges have a start and no end.



There are two design patterns for the open-ended ranges.



We can use the SQL Domain-Independent NULL.  In this case we'll have queries like :x BETWEEN tbl.start AND COALESCE( tbl.end, :x ).



We can define a Domain-Specific NULL for the end dates.  A date in the far, far future works best.  In this case, we'll have queries like :x BETWEEN tbl.start AND tbl.end.



Opinions Vary
--------------



One manager was pretty sure that the NULL case would be faster.  I'm not sure why, but I need to ask when I'm out there next.  I think this was based on the observation that tables with lots of NULL columns process faster.  (For full table scans, this is true because the table is physically smaller.)



I was darn sure that the NULL's would be measurably slower.  Why?  They can't be indexed.  Since they're not in the index, the RDBMS has to resort to full table scans and can't exploit the index.



Boy was I wrong.



I've only tested a few databases, but my results make a lot of sense.  Indexes help the database optimize some kinds of queries, particularly "==" tests and equijoins between tables.



For these "in a range" queries, the RDBMS's I looked at don't appear to leverage the index in terribly clever ways.  They appear to use full table scans.  I'm not really terribly surprised.  Query optimization is hard enough, cleverly using an index for "in a range" would probably be too much thinking for a fairly rare kind of query.



RDBMS performance measurement is hard.  Many things interfere with getting solid performance numbers.  The best approach is long-term averages under load.  So, some of my results may have a great deal of experimental bias built in.



However, what I did see were microscopic differences between the two approaches to open-ended date ranges.  I saw colossal differences between table scans and joins with and without indexes.  I saw colossal differences with different kinds of indexes.  But the two end-date representations seemed equivalent.



My Trump Card
--------------



I got some follow-up comments on my "non-null NULL" approach.  I think they mean "domain-specific" nulls, that is, using a large date instead of a NULL.  That shows a bias where they're equating open-ended dates with NULLs.  As if the "right" implementation were NULLs and I'm proposing something radical and odd with my "non-null NULL".



They worry about documenting the domain-specific NULL.  How do we explain that this "random date in the far future" means "till the end of time as we know it"?  I think they're just hand-wringing because they don't want to change.



They act like the established meaning for NULL is "for the foreseeable future".  Sadly, that's not true; NULL can mean almost anything.  Sometimes it might mean "don't know".  Sometimes it mean "does not apply".  Sometimes it means "the input was incomplete, and we'll update this later."  Sometimes it means, "the input was incomplete, and this record is a place-holder to remind us to fix the error."



I read a lot of other people's code.  While you may be pretty solid on your "standard" use of :x BETWEEN start and COALESCE ( end, :x ), you're in the minority on this.  What I observe about SQL idioms is that one programmer does it that way, and all the other programmers do it other ways.  The stored procedure hack will write define a whole library of procedures to "make the problem go away."  At least one maintenance programmers won't get the idiom, and will write application program loops with IF statements.  Further, what I often have to analyze is the one mystery program with SQL so obscure that no one dares touch it. 



"A COALESCE isn't obscure" you say.  My response is, "if that was the only problem, I'd agree.  But you've got so many other things going on, that it would be good to have just this date thing be simple and obvious."



Bottom Line
-----------



Performance-wise, I couldn't prove that NULLs or far future dates are better.  Reading-wise, I prefer to read simpler code.



In my opinion, simple wins.



Technical Note
---------------



Yes, I used Python to build the SQL and execute it with various kinds of data.  It was handy to collect the results in CSV file and pump it straight into the spreadsheet.



Different RDBMS products have different syntax for these date things, so I had to do a bunch of relatively icky text manipulation.  I wanted to use SQLAlchemy to handle the vagaries of the database engines, but the client would have disputed the results.  Instead I had to build relatively simple Python to run plain-old-SQL in simple, obvious ways.





