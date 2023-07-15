Quantum Time: Dates, Times, DateTimes and Timestamps (3rd ed.)
==============================================================

:date: 2008-02-09 12:57
:tags: architecture,software design,data structure,algorithm,database design
:slug: 2008_02_09-quantum_time_dates_times_datetimes_and_timestamps_3rd_ed
:category: Architecture & Design
:status: published







Time is simple.  You can make it complicated with any one of a large number of dumb-as-dirt decisions.



In the **Real World**\ ™, time may be a quantum field (read stuff by `'t Hooft <http://books.google.com/books?id=uPao7ThZEZAC>`_ ).  For that matter, space itself may have some quantum granularity.  Or, this could be a handy hack the physicists have devised because it makes the math work out more simply.



In Relational Databases, the digital representation of time does have a specific resolution.  A quantum of time is the microsecond.  Mostly, but not always.



Time is simple, it's the calendar that's complicated.  [Okay, time may not be that simple, `read here <http://books.google.com/books?id=lSEXAFwHvcsC>`_ .]  For our purposes, time is linear and unidirectional, with a 1-microsecond resolution.



The Gregorian calendar, on the other hand, has two sets of interlocking dimensions.



-   Days - which are just another unit of time: weeks, days, hours, minutes, seconds.

-   Months and Years - which are random boundaries among days.



Bad Old Days
------------



The calendar can be made much more complicated by adhering to a 1970's view of data processing -- the view that said things like "this software won't be in use in 2000, don't worry about centuries."  When I was a child (and thought like a child) we were told, explicitly, to omit century information.  The extra two digits, which were always "19" and were always going to be "19" didn't have any useful information.



Further, we rarely had pleasant, easy-to-use calendrical calculation libraries.  The *idea*  of a book like `The Standard C Date/Time Library <http://www.amazon.com/Standard-Date-Time-Library-Programming/dp/0879304960>`_  didn't exist.  Rather than refer to great books like `Calendrical Calculations <http://emr.cs.uiuc.edu/home/reingold/calendar-book/index.shtml>`_ , we "rolled our own".  Often with profound bugs.



Horror Story.  At one client site, Mike had a yellow sticky note on his workstation to remind him to fix a date calculating routine in 2000.  The bug had surfaced in '92 and they worked around it.  In '96 it had surfaced again.  Rather than write the proper leap year calculation, Mike planned -- with malice aforethought -- to patch the software every four years as long as he worked there.



It's the 21st century.  Using any home-brewed date or calendar library is at least crazy and perhaps criminal.



Useless Data Types
-------------------



The **Bad Old Days**  lead folks to put some useless data types in the SQL standard.  By useless, I mean absolutely without value.  I consider their use a potential quality defect, and lift it up as a bug every time I encounter them.



Winner of the **Useless**  category is Time as a distinct data type.  Time means "Time-of-Day", and is just the least-significant portion of a proper DateTime.  It is not atomic data except in one very specialized situation.  I'll get back to that.



Runner-up in the **Useless**  category is Date as a distinct data type.  Date means "DateTime with time set to midnight" and is just a way of rounding a DateTime down to the nearest Date.  Sometimes, you can make the business case that time didn't matter.  In some instances you truly have a date with no relevant time (examples follow).  More often, you have users who only want to see the Date portion of a full DateTime; this is a matter of formatting, not a matter of intentionally dropping precision.



Which leaves us with DateTime (a/k/a Timestamp).  This is generally what we mean -- a point in time.  We might display just the date, or the full date and time.  We might omit fractions of seconds, or we might show just hours and minutes.



Using any data type other than a full DateTime (or TimeStamp) requires some careful justification.



Waste of Storage
----------------



I've been hearing the "waste of storage" malarkey for 30 years.  I'm tired of it.  A full date can be persisted in just 10 bytes.  You only need 4 bytes for a day counter, 3 bytes for a seconds-of-the-day counter (range 0 to 86,400), and 3 bytes for a microsecond counter.   A pleasant DateTime class may have dozens of methods, but not require much persistent real storage.



"That's fine in theory," they counter, "but we like human readable dates in our files."  Yes, that does require 20 characters to record yyyy-mm-dd hh:mm:ss.ssssss.  In short, some folks prefer to (a) demand a storage wasting format and then (b) complain about the storage their storage-wasting format requires.  Sigh.  We have to truncate a perfectly good DateTime to Date.



The cost of storage is falling rapidly.  We can waste serious money analyzing and justifying each date.  Or we just buy storage and move on to more interesting questions.


Other Date Round-Offs
-----------------------



While we have built-in support for rounding off a DateTime to the nearest date, we rarely have much support for rounding off a DateTime to the nearest month.  I worked an application where manufacturing could only provide month and year of manufacture.  For inexplicable reasons we didn't simply call this a DateTime with a day of 1, and a time of midnight.



No one could figure out how to work with a (*year*, *month* ) pair.  When I arrived on the scene numerous interactive pages and reports had been developed which simply did not work correctly except for a tiny test case that involved a single record.



Particularly disturbing was their mishandling of the 18-month rolling report which showed a summary of over a year of manufacturing data.  There were if-statements of a complexity that absolutely baffled me.   How could these programmers be clever enough to write that horrible, complex, opaque if-statement and not see the essential simplicity of using a month counter?




::

    monthCount = year*12 + month

    year= monthCount // 12
    month= monthCount % 12






There's nothing more complex than the above formulas to reduce their hideous, unreadable morass of logic to  a proper "between" clause. [BTW, the project manager balked.  He wanted to deliver on-time, irrespective of readability.  I had to concoct test cases that failed before he would consider their mountain of trash as a problem.]




The Data Warehouse Round-Off
----------------------------




Data Warehouse applications have to work with the simplest possible GROUP-BY constructs.  [That's one important theme of Kimball's Data Warehouse Toolkit.]  A full DateTime, however, is often too fine-grained for data warehouse use.  Doing calculations to round a DateTime to the nearest Date (or week, or month, or quarter or year) is impractical.  What to do?




The DW trick is to have a "Date" table which enumerates every day under consideration in the data warehouse.  It provides all calendrical attributes for each day, replacing all calculation with simple joins.




[Don't bother saying "That's too much storage."  Do the math first: it's not big; if you've got 20,000,000 rows of account facts, 36,524 rows of dates isn't worth discussing. You'll rarely preload a whole century of dates; if you just put in a decade, your chart of accounts will be bigger.]




How do we join to the Date table?  Consistent with other DW technique, you need to break the Third Normal Form rule ("no derived data") and carry an additional attribute that is derived from your DateTime: the FK reference to your Date table.  This FK reference is based on rounding the DateTime down to the Date only for the purposes of locate the proper Date row.




If you're really strapped for storage, you might can try to separate the Date and Time parts of a DateTime.  Then you'd use both the Date and the Time as a kind of DateTime, or you'd use Date alone.  I don't like this because you orphan the Time portion of the original DateTime; Time is not an atomic attribute.  




Date Range Comparisons
------------------------




Date range comparisons are ubiquitous.  In data warehouse applications, they are an essential ingredient to managing a slowly-changing dimension.




One common situation is to have a table of records that are supposed to fit together providing a seamless coverage through time.  Let's say we're working with something simple like territory changes.  A customer belongs to territory A for some range of dates, then is switched to territory B for another range of dates.




We have a Customer to Territory association (sometimes called a bridge table in data warehousing circles.)





..  csv-table::

    "Customer","Territory","Starting Date","Ending Date"
    "1","A","3/4/05","4/5/06 *(end A)* "
    "1","B","4/5/06 *(start B)* ","5/6/07"
    "1","C","5/6/07","12/31/2199 (""foreseeable future"")"












This is common, and very easy to query incorrectly.




Specifically, look at the dates labeled *end A* and *start B*.  We have two choices for ways to encode these date relationships.  In both cases, we're comparing some query date, *d*, for membership in a date range; between the start time, :math:`T_s`, and the end time, :math:`T_e`.




-   **Closed Interval**.  This is the case expressed by SQL BETWEEN: ``d BETWEEN T_s AND T_e``.  Some math textbooks might write this :math:`[T_s, T_e]`.  We can also say :math:`T_s \leq d \leq T_e`.  Depending on the quantum resolution of time you're using, this can be pleasant or nasty.

-   **Half-Open Interval**.  This is the case expressed by :math:`T_s \leq d < T_e`.  Some math textbooks might write this :math:`[T_s, T_e)`, to show that the interval doesn't include one end.  If you simply ban use of BETWEEN, this representation has several advantages.




We'll look at each more closely to provide reasons why Closed Intervals (and the BETWEEN operator) are a problem waiting to happen.  Half-Open Intervals work out better. 




Closed Interval
----------------




Using a Closed Interval requires that the dates marked *end A*  and *start B*  above are not equal.  If they were equal, then both records would be in the result set for that matching time.  There can, however, be no gap between these two times.  If we use Date data types, then they must differ by exactly one day.




However, if we use DateTime, then the DateTime value from the end of one range must differ from the end of the next range by the exact time resolution value, 1 microsecond.  Nasty.




[I've had programmers say that 1 second is good enough, and the odds of a time falling into the crack are really low.  What?  We're building something that doesn't pass simple unit tests and we're going say that the odds of failure are "good enough"?]




In order to insert the next territory change, we need to do two things.  We have to set the end date of the previous territory so it is no longer "the foreseeable future" and instead is the actual end date.  We have to increment that date by 1 microsecond and use that as the start date for the next territory record.




Half-Open Interval
-------------------




The Half-Open Interval requires that the dates marked end A and start B above are simply equal.  We're going to simply forbid the use of BETWEEN and force everyone to write Ts &lt;= d AND d &lt; Te.  Time quanta don't enter into this, since the end of one range is the same Date or DateTime value as the beginning of the next range.




This is much simpler; trivially proven to be absolutely reliable and correct.  All we have to do is forbid the use of BETWEEN for dates.




I've been told this will be confusing to "other users" of the database.  For this, I have one question: "Who specifically?"  We can write them a memo.  I've been told that removing BETWEEN is too onerous a burden on the developers.  Again, I have one question, "Who specifically?"  I'll work with them as long as it takes to show them the alternative formulation.




The knottiest problem is "What about end-user queries?"  I'm a-waffle on this.  I don't think end-users should be afflicted with SQL.  However, if we tie up all reporting in an inefficient IT department, end-users will immediately take active steps to write their own queries.  If we aim high and provide everyone a license to a reporting tool like Business Objects, then the date ranges are hidden in the BO universe definitions.  If we can't afford that... well, **Bad Things**  are pretty much inevitable. 




Either get proper reporting tools or provide enough education so that end users are actually coached through using the data model correctly.  A few hours of coaching beats flawed software and endless troubleshooting.




Pure Dates
------------




Some business rules are based on a date, and the time isn't available.  These rules are universally situations where humans must supply a date.  When the system itself supplies a date, it's always a portion of a DateTime.  When humans are asked to supply a date, they are not able to provide a full DateTime.  Examples include all of the standard life milestone events like birth date, marriage date, employment start and end dates, etc.  




Unbound Times
--------------




There's one potential use for Time, separated from DateTime.  That's when we're defining a scheduling rule.  In this very rare case, we have a time of day that is not bound to a specific date.  That's the only instance where a Time is an atomic piece of data.  In all other cases, Time is just the least significant part of DateTime.




Summary
---------




Time is simple.  Use DateTime.  Format DateTime values to show only the date portion if that's what users want.  Use Half-Open Intervals, and don't use BETWEEN.




