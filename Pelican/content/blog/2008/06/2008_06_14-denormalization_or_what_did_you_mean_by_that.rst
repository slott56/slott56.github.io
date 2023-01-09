Denormalization or "What did you mean by that?"
===============================================

:date: 2008-06-14 11:59
:tags: #python,database
:slug: 2008_06_14-denormalization_or_what_did_you_mean_by_that
:category: Python
:status: published







I use the word denormalization heavily, to make a point to a certain class of developers.  Other developers object to the term, since it doesn't have a precise meaning.



The point I often have to make this:  



1.  3rd Normal Form is for Updates.  



2.  Data Warehousing is about Insert and Select; there are no Updates (to speak of).



3.  Consequently, the traditional normalization rules (Third Normal Form a/k/a 3NF) doesn't apply to data warehousing.



My habit is to describe the star-schema (or snowflake schema) as "denormalized".  This isn't really correct, but it does emphasize my point.  I have to make this point emphatically because we have to get past the Data Cartel's Standard Objection: :strong:`New Technology Won't Work`.  Most DBA's who are new to Data Warehousing and the star schema will exercise their veto authority over new technology, claim that the design is "inefficient" and stop (or delay) the project.



:strong:`DBA Objections`



DBA's can object in `Passive-Aggressive <{filename}/blog/2007/11/2007_11_29-the_passive_aggressive_programmer_or_why_nothing_gets_done_revised.rst>`_  (and `Passive-Aggressive Part II <{filename}/blog/2008/03/2008_03_24-the_passive_aggressive_programmer_part_ii.rst>`_ ) mode -- where they don't have a better solution, they just have "concerns" about the standard DW solution.  Here are some things I've heard.



1.  :strong:`It isn't normalized`.  Which is a WTF? kind of point.  It isn't normalized for updates because there aren't any (to speak of).  It's normalized for SELECT SUM(*) GROUP BY, which is the canonical dimensional query.  I call this "denormalization" to make the point; perhaps I should call it star-schema normalization.



2.  :strong:`It doesn't use "natural keys" correctly`.  I'm pretty sure that natural keys don't actually exist.  Almost everything is either an attribute (which can change) or a surrogate key (which isn't very likely to change).  A changeable attribute isn't really a key, is it?



When writing ETL programs, we sometimes have a blurry edge when an external application assigns a truly permanent surrogate key.  In these cases, the external surrogate is often something that the organization uses heavily -- as if it was a natural key.  In other cases, they have a surrogate-like key that can (it turns out) change, making it just an attribute.  In the warehouse, it's usually best to simply assign warehouse surrogates and not burn up brain calories trying to make too many distinctions in the source applications.



3.  :strong:`All those joins are inefficient`.  This can -- in the extreme case -- lead to :strong:`The Uni-Table`.  This is the pre-joined ur-fact table that contains all dimensional attributes and all fact values.  It works, but it repeats all of the dimensional attributes and it doesn't track dimensional change at all.  Yes, I've seen it done.



4.  :strong:`It uses too much storage`.  This is just silly, but it comes up.  Once, I caught the sysadmins and DBA's in a meeting where they were quibbling about log sizes so that they could micro-manage storage at the 100Gb increment.  "There's four people in this meeting.  At your hourly cost, I could have bought 400Gb at Circuit City."  And the price of storage continues to plummet.  Nowadays, I think I could buy a terabyte.



5.  :strong:`Fact updates can be inefficient`.  This is crazy, because changing a fact's measurement value is a single row update; it's fine if you're correcting errors.  Changing a batch of fact's measurements is -- what? -- criminal mischief?  Who changes batches of facts?  Considerer deleting the incorrect ones and reloading correct ones.



Changing the association between a batch of facts and a dimension is even spookier.  The historical fact is what you recorded.  You don't get to change the facts; it's called perjury.  If you're restating your books, you usually have new facts that apply to a historical time period.



:strong:`Star Schema Normalization`



To get past the DBA objections, we need to have several heart-to-heart conversations on star-schema normalization.  Generally, these are painful because DBA's are overworked and sometimes underqualified.  Examples on paper don't help much.  Telling them to read Kimball does nothing.  Loading up realistic sets of data is the only workable approach to showing them that the storage is manageable, the joins won't kill you, surrogate keys work, and the star schema is a "real" thing.



Once we've aired out an example, we then have to revisit the star schema thing over and over again.  Most DBA's are so habituated to 3NF that they can't get past it to see that a star schema is an alternative normal form.  Except in rare cases, the best we get is grudging tolerance.  [In the rare cases where the DBA's embrace a star schema approach, no one needs me, except to validate the design.]



The basic 1NF and 2NF rules apply to the star schema normal form as well as transactional normal form.  Arrays are still a bad idea in the relational world.  Foreign attributes (those not functionally dependent on the key) are still a bad idea.  However, 3NF is out the window -- derived data is a helpful thing.



:strong:`Derived Data?  What About Updates?`



DBA standard objection #5 -- updates hurt -- often surfaces when discussing the approach of persisting derived data.  This is a focused "denormalization" that unwinds just 3NF to avoid repeating a calculation.  In the case of a data warehouse (load once, query an infinite number of times) all calculations done at load time are amortized across an infinite number of queries, making them delightfully efficient.



The "update" issue can't arise.  Let's look at some common dimensions.



:strong:`Time`.  You don't change the day of the week for March 8, 1987.  It is, was, and always will be Sunday.



:strong:`Space`.  Geographical boundaries change.  However, this is the canonical Slowly Changing Dimension (SCD) problem that Kimball covers in detail.  [If you have what Kimball calls a "type 3" SCD, you have the most common example of an update in a data warehouse; the change of status from "current" to "previous".]



:strong:`Customer`.  Your customers (either individuals in huge collections or other businesses in small collections) have numerous changes.  However, they often have attributes which can't change as well as attributes which frequently change.  For example, demographics change very slowly (if at all).  Customers often requires more sophisticated "snowflake schema" techniques.  There still aren't any updates, but there are SCD techniques for handling this.



:strong:`Product`.  Your products, product lines, product families, product groupings, solutions, technologies, platforms, services, etc., are all grouped by marketing in the randomest ways.  These groupings and hierarchies and clusters and affinities are just ways that marketing tries to portray your company; and it changes with every whim and brain-fart.  This is also a basic SCD issue; you simply add the alternative hierarchies and groupings and do alternate joins on the facts.



:strong:`Cost Centers`.  Your internal cost structure changes.  Sometimes frequently.  This is still SCD.  No updates, just inserts.



:strong:`Recent Example`



`Recently <{filename}/blog/2008/06/2008_06_06-my_query_is_slow_what_to_do_or_dumb_as_a_post_sql_revised.rst>`_ , I aired out some brain-dead non-solutions to a simple reporting problem where number of rows (500 new rows per hour) might have been the design problem being solved.  The non-solution involved a five ways of avoiding a viable solution.  As follow-up to my suggestions, I was given the following variations on DBA objection 1; each affixing blame somewhere else.



1.1.  The customer cannot accept a "denormalized" table that pre-computes the values.  [The customer is at fault.]



1.2.  Since we can't directly use the "denormalized" table in your blog posting, the idea of denormalization is broken, and we can never talk about it in any form whatsoever.  Temporary tables, materialized views and other techniques are off the table, :emphasis:`a priori`.  [I'm at fault for not providing the expected solution, which involved some kind of :strong:`Faerie Dust`\ ™ that would make a bad table process quickly.]



1.3.  The organization can't learn anything new.  Talking about "denormalization" would be new, and is therefore forbidden.  The idea of persistent derived values is off the table, :emphasis:`a priori`.  [The organization is at fault.]



At this point, any suggestion I might have has been trumped by the DBA's opposition to denormalization.  Blame has been assigned everywhere.  I think this is because I used the word "denormalization" incautiously and set myself up for three flavors of DBA objection #1 ("It isn't normalized.")



Perhaps, if I'd said "persistent derived values" instead of "denormalization" we might have gotten somewhere.  Ideally, they would have suggested a temporary table or materialized view as an implementation technique.  But, we stalled out at my incautious use of a loaded buzzword.




