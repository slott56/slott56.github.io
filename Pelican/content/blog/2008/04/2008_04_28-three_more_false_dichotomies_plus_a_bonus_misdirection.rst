Three More False Dichotomies -- Plus a Bonus Misdirection
=========================================================

:date: 2008-04-28 23:46
:tags: architecture,design
:slug: 2008_04_28-three_more_false_dichotomies_plus_a_bonus_misdirection
:category: Architecture & Design
:status: published







What I said: "How about using the RDBMS product appropriately ? It's for persistence. Do processing in another product, appropriate for processing: Java."



What it became: "why not use a file system and skip the expense and overhead of an RDBMS ?"



I was shocked that numerous good features of the RDBMS were blissfully discarded.  Indexing?  Gone.  Separating of logical and physical storage?  Gone.  ACID rules, Locking and transaction management?  Gone.



All I wanted to do was cut down on triggers and stored procedures.  But a true master of the false dichotomy turns that suggestion into a choice between dumb storage and the whole RDBMS bloatware that includes numerous inefficient processing choices.



I tried to lift up a middle-of-the-road feature set.  Above dumb storage, but lacking the endless problems of triggers and stored procedures.  I got a bitter response: "How did we get on to indexes, acid and the like?"  



I tried to introduce the middle ground, and was shot down.  Apparently, the RDBMS is an all-or-nothing proposition.  Since we're already holding the hammer, we might as well treat all problems as nails.



:strong:`The Flat File Folly` 



When confronted with serious performance issues in a database application, a good approach is often to eschew complex SQL.  Indeed, the lesson I learned a few years back working on a big data warehouse was the following:

..  code:

::

    SELECT * FROM SOURCE TABLE into a file.
    Do all processing in Java, creating a resulting file.
    Use SQL*Loader to reload the resulting file






I was told that this would clearly use too many I/O operations, making this design pattern unacceptable.  Processing must be done either entirely in SQL or entirely in memory as Java objects.  Since there were too many objects, in-memory wouldn't work, which left no choice but database processing.  There is no middle ground.  




:strong:`Optimization in a Vacuum` 




Given: some long-winded stored procedure with ill-defined semantics and no data model.  Goal: fix it.  What does "fix" mean?  Here's the deal: it's a stored procedure, but no one wants to produce the data model for the tables involved.




I asked, several times, for the context.  I was shot down.    I was told "I thought that I could address the programming issue of nested if's and long lists of if - elseif - elseif w/out taking into account the context/data model.".





I'm filled with awe at the idea of optimization without making fundamental changes to the algorithm or data structures.  It's remotely possible that the code is so brain dead as to be trivial to optimize.  





At first, this didn't seem like a false dichotomy.  Then I realized that I was being asked to separate data structure from algorithm.  Since that can't be done, it's a kind of false dichotomy.





:strong:`Adding A Little Hibernate` 





I tried to explain that ORM's aren't an "incremental" change.  It fundamentally rearranges how you design and implement algorithms.  Which, in a way, is a kind of dichotomy.  But I don't think it's a false dichotomy.  I think that the ORM world-view is fundamentally different from one where you write long, complex stored procedures and triggers.





I was told that "One guy during the meeting said that if we needed to we could use PL/SQL."






Which, I suppose is true.  But it is the best way to subvert simple, clear, high-performance ORM.






False dichotomy is a technique for rejecting change by going far beyond the proposed change, setting up a false dichotomy and bundling the real change in with the overstatement.  






In my case I had laid out a dichotomy as part of making a change.  This was characterized as a false dichotomy.  Sadly, no one seems to have any examples of any actual best-practice programs using Hibernate, so it stands as a false dichotomy.










