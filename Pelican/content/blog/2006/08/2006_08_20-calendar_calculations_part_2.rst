Calendar Calculations - Part 2
==============================

:date: 2006-08-20 01:26
:tags: architecture,software design,data structure,algorithm,requirements
:slug: 2006_08_20-calendar_calculations_part_2
:category: Architecture & Design
:status: published





First, let's pick the conclusion out of the
middle: "However, the computation for the first and last business day of the
month is trivial. So, just codify this."



Since we still lack any usable
context, we're struggling with the definition of basic terms.
Is this the *calendar* month, or the *fiscal* period that overlaps with that calendar month?
The first business day of a *fiscal*
period that includes a random date in January could very well be Monday,
December 31st of the previous year.



The statement was made; to interpret it, we have to guess at the underlying
assumptions that make it appear true to the poster.

1.  They're talking *calendar* month, not fiscal period.  Why, on earth, would anyone mix the calendar and the
    fiscal periods?  How, precisely does "business day" apply to a calendar month,
    which is separate from a fiscal period?  Any given calendar month may have one,
    two or three relevant fiscal periods.  Since the terminology appears
    contradictory, we'll set this aside as unlikely.  January 2 and January 31 could
    belong to different fiscal periods and have different "first business day"
    definitions.

#.  They're talking about *fiscal*
    period, not calendar month.  However, the original question behind the `Hubris post <{filename}/blog/2006/08/2006_08_07-the_hubris_of_calendrical_calculations.rst>`_  had to do with using the built in
    RDBMS calculation methods, which are for *calendar*
    months, not fiscal periods.  So, we can't be talking about fiscal periods if
    we're also talking about RDBMS calendar functions.

#.  They're talking about fiscal period, and have
    conflated it with calendar month, not realizing there's a difference.  This must
    be the case.  


What we appear to have
is the argument that

(1) the *fiscal* "first business day" can be calculated from the
    *calendar* functions in the RDBMS in spite of the date being defined for a *fiscal*
    period; and

(2) this calculation is simpler that looking up the correct date in
    the G/L calendar.



Since this argument only makes sense if we presume that fiscal period and calendar month are the
same thing, I can't believe a word of it.  Indeed, I find it alarming.



I'd need to see some context -- to define the terms -- and then some code.
And, of course, the appropriate business policy that gives me a reason to believe the code is more reliable and
correct than the manually-prepared calendar. 




Conclusion
----------

**Calendar Calculations involve hubris that stems from conflating calendar and fiscal periods**.



For the second part, let
me rearrange the posting as follows.

    "Banking holidays have to be loaded into a
    table. The rules to compute the banking holidays are too complex and change.
    [*snip*]
    Why is it more efficient to have a human on a yearly basis compute the first and
    last business day of the month. It has to be done on a yearly basis because the
    banking holidays change on a yearly basis."



This is something that I can't fully understand.
It appears to be the following three points: (1) calendar
definition is manual, (2) some of the manual work has to be persisted in a
table, (3) other parts of the manual work should not be persisted in a table. 




To the person posting, points 2 and 3 aren't a contradiction.
Somehow, they've got a secret assumption that resolves the above craziness.
I can only guess.

1.  The fiscal periods don't apply.  See the above
    analysis: somehow we're supposed to get "first business day" from the calendar
    without knowing anything about fiscal periods.

#.  Either the bank holiday definitions or the
    fiscal period definitions don't wind up in the persisted G/L calendar; it *must*
    be calculated.

#.  The person working on the calendar doesn't
    know the fiscal period starting dates, even though they have to allocate the
    bank holidays into fiscal periods.



It's pretty pointless to guess what the unspoken assumptions are.  However, there is
clearly a lot of confusion on what information is already available and why it
shouldn't be treated as a value that can reliably be calculated. 



Recomputing will -- unconditionally --
insert errors.  A person does something to balance fiscal controls, policy, law,
contractual obligations, and regulatory considerations.  Since the software
doesn't have all of this information, it can't produce the same result. 




Imagine -- just for a moment -- the
controls and audits that would have to be in place to assure that this calendar
calculation really worked in production.  We'd have to have some control for the
calculation rules, and a log of results to be sure we did it correctly.  Since
the benchmark data against which we're basing our controls is *manual*,
what do we use for an ongoing audit? 
*Compare the calculation against the manual data?*

Hello?

Isn't the manual data
the answer in the first place?  Why are we recomputing the controls we're using?
Why not just load them and be done with it?



Conclusion
----------

Calendar
Calculations involve ignorance of `The
Data Warehouse Toolkit <http://www.amazon.com/gp/product/0471153370/>`_ .  This may be
unintentional, but the ignorance can be cleared up on page 7 and page 32.  About
four pages of
reading.



Consequence
-----------

Any calendar calculation module based on the confusion between calendar and
fiscal period will have bugs.  It will diverge from other bank calendars.  It
will require almost endless maintenance, and provide essentially no value for
the effort involved.  



As near as I can
tell, Calendar Computations are **An Attractive Time Sink**\ ™:
a nuisance, a source of errors and cost.














