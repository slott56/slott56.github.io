Absurdity?  Consistent Code and Inconsistent Data Structures
============================================================

:date: 2006-10-11 16:27
:tags: architecture,design,data structure,algorithm
:slug: 2006_10_11-absurdity_consistent_code_and_inconsistent_data_structures
:category: Architecture & Design
:status: published





First, see "`OSCON - Open Data <http://www.tbray.org/ongoing/When/200x/2006/07/28/Open-Data>`_ " by Tim Bray, then see "`Set My Data Free <http://kontrawize.blogs.com/kontrawize/2006/07/set_my_data_fre.html>`_ " in
Kontrawize.



Here are some quotes "At
the end of the day, information outlives software and transcends software and is
more valuable than software."  "Data matters. It shouldn't be an afterthought.
It will outlive your applications." 




Hopefully, these are clear enough to
show where this is headed.  However, since I was asked, I'll press on
anyway.



So that we can start somewhere,
let's start with the `Zachman Framework <http://www.zifa.com/>`_ .  We see several ways to look
at IT.  I'll paraphrase slightly.

-   Data ("what")

-   Processing ("how")

-   Network ("where")

-   Users ("who")

-   Schedule ("when")

-   Value ("why")



Data is first.  Why?  Because
it's the only thing that matters.  



Do
I have any evidence of this, outside the Zachman framework?  Here's some other
anecdotal evidence: "Data Processing", "Data Structures and Algorithms".  Data's
always first.



Now, let's look at some
real evidence.



**Real Evidence.** 



First, let's look at any
SDLC methodology.  They have big sections on "data conversion".  Why? 




Let's think.  We're writing software
to apply new (or different) processing to our data.  We often want to preserve
our data, but not our legacy processing.  Indeed, preserving data so important,
that it becomes a first-class goal in a methodology.  Preserving functionality
(through analysis and reverse engineering) may or may not be important.  It is
rarely a huge, visible part of any
methodology.



Second, let's look at
non-IT people.  They preserve files, documents, and content very carefully.  And
they process this precious data with the most slip-shod manual steps.  People
will have massive spreadsheets on the shared "H:" drive, which anyone can touch.
Why allow other members of the department to touch it?  Because processing is
just processing.  Data, however, is the reason the organization
exists.



Third, let's look outside IT at
our regulatory context.  The IRS doesn't ask how you deposited the money, or how
you signed the receipts to spend the money.  The IRS wants to see the records of
the transactions, not the process for executing the transactions.  You can tell
the auditor that you turned the clipboard around three times, clicked the pen
twice, and signed with a single flourish.  They want to see the receipt: the
thing, the data.  



**Data Model Variants.** 



A variant data model with
a common code base has a number of serious
issues.



First -- and foremost -- it
puts processing ahead of data.  Therefore, it's just the wrong thing to do.  The
processing comes and goes, but the data endures forever.  So, a common data
model with variant processing is the normal case.  That's why we have software
version numbers in two (or more) parts.  Often, version 3.2 has a data structure
which is compatible with version 3.3, but incompatible with version 4.1.  The
processing changes, but we advertise a consistent data
model.



Second -- and this is weird --
how did the data wind up different?  Why aren't both data models the same?  Why
does one have additional data, or why is one missing some data?  Does this
reflect divergent evolution?  What changed?  Or, more important, what failed to
change?



In essence, the questioner
wants software version 3.2 and 4.1 to be the same code base.  This is clearly
silly.  Therefore, there must have been another, deeper
question.



**Options and Extensions.** 



I couldn't make sense
out of the question, so I asked what was really going on.  The response -- while
murky -- appears to indicate that there are two more-or-less parallel
environments, which differ, slightly, in structure.  This smells like an
optional feature which is used in one environment, but not used in another
environment.



On one hand we have two
installations of some software: one with and one without an optional feature. 
On the other hand we have "common code base without a common data model".  The
"no common data model" is absurd, and almost incomprehensible.  The "optional
feature", however, is a much more common, and tractable problem. 




Indeed, the root cause of the question
seems to stem from inflating an "optional feature" into "no common data model". 
It appears as if the minor variation made the two structures appear to be
irreconcilably different.  The molehill of "one optional table" grew to the
mountain of "no common data
model".



**The Real Question.** 



The real request, then,
appears to be this: discuss 'a common code base with an optional table' .  Or,
phrased as a question: "how do I cope with an optional
table?"



Databases are full of optional
features like indexes, triggers and constraints.  These can be added or deleted
without any change to a working application program.  Tables and columns,
however, are different: they must exist for our programs to bind properly.  So,
we have two flavors of optionality in RDBMS world: truly optional, and
present-but-not-used optional.



Optional
features are a touchy subject.  How does the software know that something is
optional?  Clearly, the software must have some kind of configuration
information.  Often, these configuration options are poorly chosen.  In the case
where a single optional table turned into "no common data model", I have
suspicions that the configuration of optional features will be equally
confusing.



There are several
steps:

1.  Don't turn an insignificant optional feature
    into a "no common data model" situation.  Inflating the problem made it
    insoluble.  Please try to stick to specifics wherever possible.  In general,
    don't generalize.

#.  If a table is optional, then it can be present
    but empty.  A similar situation applies to columns: it can be present, but
    filled with NULL's.

#.  Choose a simple design for configuration. 
    PL/SQL can't rely on environment variables or command-line parameters. 
    Therefore, there must be an RDBMS table with configuration options.  Or a
    wrapper program parses environment and command-line information and passes this
    in as parameters to a "main" PL/SQL procedure.

#.  Stop coding.  If code comes first, you're
    probably doing the wrong thing.  Data comes first.  Understand the data
    completely before doing any coding at all.  Get the data model completely
    correct and consistent before doing any coding of any kind.  If you feel
    management "pressure" to "produce" something, stop anyway.  This thing you're
    describing as management "pressure" is entirely your own response to your
    environment.



Stop coding and repeat
after me:  "I can't code until I understand all the data."


















