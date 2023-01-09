Legacy Code Preservation: What's the Story?  
=============================================

:date: 2013-04-18 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_04_18-legacy_code_preservation_whats_the_story
:category: Technologies
:status: published

.. container:: section
   :name: what-s-the-story

   Wind back the clock to the late 1970's. Yes, there were computers in
   those days.

   Some of my earliest billable gigs where conversions from old OS to
   new OS. (Specifically DOS/VSE to OS/370, now called Z/OS.) Back when
   a company owned exactly one computer, all of the in-house customized
   software had to be rewritten as part of the conversion.

   For the most part, this was part of a corporate evolution from an IBM
   360-series to 370-series computer. That included revisions of the
   operating system toward OS/370.

   A company's custom software often encoded deep knowledge of business
   operations. Indeed, back in the day before desktop computers, that
   software **was** the business. There was no manual fallback if the
   one-and-only computer didn't work. Consequently, the entire IT
   department could be focused on converting the software from old
   operating system to new.

   Every line of code was carefully preserved.

   Not all software encoded uniquely valuable knowledge, however.

.. rubric:: Flashback
   :name: flashback

In the days before relational databases, all data was in files.
File access required a program. Often a customized piece of
programming to extract or transform a file's content.

In old flat-file systems, programs would do the essential
add-change-delete operation on a "master" file. In some cases
programs would operate on multiple "master" files.

In this specific conversion effort, one program did a kind of join
between two files. In effect, it was something like:

.. code-block:: sql

    SELECT * FROM BIG_TABLE
    JOIN OTHER_TABLE ON BIG_TABLE.CODE = OTHER_TABLE.CODE
    ...

What's interesting about this is the relative cost of access to
OTHER_TABLE.

A small subset of OTHER_TABLE rows counts for most of the rows
that join with BIG_TABLE. The rest of OTHER_TABLE rows were
referenced once or a very few times in BIG_TABLE.

Clearly, a cache of the highly-used rows of OTHER_TABLE has a huge
performance benefit. The question is, of course, what's the
optimal cache from OTHER_TABLE? What keys in OTHER_TABLE are most
used in BIG_TABLE?

Modern databases handle this caching seamlessly, silently and
automatically. Back in the 70's, we had to tailor this cache to
optimize performance on a computer that---by modern
standards---was very small and slow.

.. rubric:: The Code Base
   :name: the-code-base

In the course of the conversion, I was assigned a script ("JCL" is
what they called a shell script on Z/OS) that ran two programs and
some utility sort steps. Specifically, the sequence of programs
did the following:

.. code-block:: sql

 SELECT CODE, COUNT(*)
 FROM BIG_TABLE
 GROUP BY CODE
 ORDER BY 2

Really? Two largish programs and two utility sort steps for the
above bit of SQL?

Yes. In the days before SQL, the above kind of process was a
rather complex extract from BIG_TABLE to get all the codes used.
That file could be sorted into order by the codes. The codes could
then be reduced to counts. The final reduction was then sorted
into order by popularity.

This program did not encode "business knowledge." It's purely
technical.

At the time, SQL was not the kind of commodity knowledge it is
today. There was no easy way to articulate the fact that the
program was purely technical and didn't encode something
interesting. However, I eventually made the case that this pair of
programs and sorts could be replaced with something simpler (and
faster.)

I wrote a program that used a data structure like a
Python defaultdict (or a Java TreeMap) and did the operation in
one swoop.

Something like the following:

.. code-block:: python

 from collections import defaultdict
 counts= defaultdict( int )
 total= 0
 with read( "big_table" ) as source:
     reader= BigTable_iter( source )
     for row in reader:
         counts[row.code] += 1
         total += 1
 by_count= defaultdict( list )
 for code,count in counts.items():
     by_count[count].append( code )
 for frequency in sorted( by_count, reverse=True ):
     print( by_count[frequency] )

 def BigTable_iter( source ):
     for line in source:
      yield BigTable( line[field0.start:field0:end], etc. )

Except, I did it in COBOL, so the code was much, much longer.

.. rubric:: Preservation
  :name: preservation

This is one end of the spectrum of legacy code preservation.
What was preserved?

Not business knowledge, certainly.

What this example shows is that there are several kinds of
software.

-  Unique features of the business, or company or industry.
-  Purely technical features of the implementation.

We need to examine each software conversion using a yardstick that
measures the amount of unique business knowledge encoded.




-----

You are probably aware but just in case, you shoul...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2013-04-18 20:33:11.083000-04:00

You are probably aware but just in case, you should check out python's
pandas join on 2 data frames. By using pandas, you avoid having to screw
around w/ a database and all it's associated work. Also, you avoid
having to write plumbing code.


Maybe it wasn&#39;t clear, but the blog post descr...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2013-05-04 10:33:42.680000-04:00

Maybe it wasn't clear, but the blog post describes a situation that
occurred 30 years ago. Python, Pandas didn't exist. SQL databases were
an academic exercise.





