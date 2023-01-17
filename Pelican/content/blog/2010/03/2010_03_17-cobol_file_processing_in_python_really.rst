COBOL File Processing in Python (really)
========================================

:date: 2010-03-17 08:00
:tags: open source,COBOL,#python
:slug: 2010_03_17-cobol_file_processing_in_python_really
:category: Technologies
:status: published

Years ago (6? 7?) I did some data profiling in Python.

This required reading COBOL files with Python code.

Superficially, this is not really very hard.

#.  Python slice syntax will pick fields on of the record. For
    example: data[12:14].

#.  Python codecs will convert from EBCDIC to Unicode without pain.
c   odecs.get('cp037').decode( someField ).

With some more finesse, one can handle COMP-3 fields. Right?

Maybe not.

Problems
--------

There are three serious problems.

-   Computing the field offsets (and in some cases sizes) is a
    large, error-prone pain.

-   The string slice notation makes the COBOL record structure
    completely opaque.

-  COMP-3 conversion is both ubiquitous and tricky.

Okay, what's the solution?

COBOL DDE Parsing
-----------------

What I did was write a simple parser that read the COBOL
"copybook" -- the COBOL source that defined the file layout.
Given this Data Definition Entry (DDE) it's easy to work out
offset, size and type conversion requirements.

It was way cool, so I delivered the results -- but not the code
-- to the customer. I posted parts of the code on my personal
site.

Over the years, a few people have found it and asked pointed
questions.

Recently, however, I got a patch kit because of a serious bug.

Unit Tests
----------

The code was written in Python 2.2 style -- very primitive. I
cleaned it up, added unit tests, and -- most importantly --
corrected a few serious bugs.

And, I posted the whole thing to SourceForge, so others can --
in principle -- fix the remaining bugs. The project is here:
https://sourceforge.net/projects/cobol-dde/.





