Tackling the Spreadsheet Problem
================================

:date: 2008-04-27 12:50
:tags: architecture,design,data structure,algorithm
:slug: 2008_04_27-tackling_the_spreadsheet_problem
:category: Architecture & Design
:status: published







It's not that spreadsheets are evil incarnate, it's just that there are so many ways to abuse them.  Spreadsheets put a veneer of structure over some information.  Bad spreadsheet design, worse yet, puts unstructured information into a hard-to-manipulate format.



I've complained about this before.  See `Great Quotes about the Spreadsheet Problem™ <{filename}/blog/2007/02/2007_02_07-great_quotes_about_the_spreadsheet_problemtm.rst>`_ .



Compounding the problem is the casual way that some folks deal with the dimensionality of their data.  I've started working with researchers.  They know the distinction between independent and dependent variables -- it's often part of their experiment design.  However, their spreadsheet is just a flat list of columns, concealing the meaning in their data.



There are three hard parts to these kinds of problems:



:strong:`The design of the database`.  DB design isn't always easy to deduce from the spreadsheets.  Other programs can (and often do) exacerbate the problem by claiming that a dimensionally normalized database isn't to helpful -- they just need persistent storage.  In the long run, that won't work out.



:strong:`Inconsistency of the spreadsheets`.  We can write rules, pass laws, build macros, rant and rave.  The spreadsheet is still a flexible desktop tool.  We can try to replace it with MS-Access, but the security model is still all-or-nothing.  If you have any access, you can add, change or delete anything you want to  touch.



:strong:`Getting data out of an XLS file`.  There are many, many ways to approach this problem.  We might:



-   Save the file as CSV.  There are issues here; principally, who can you trust to save the various sheets consistently?  The "end users" aren't generally all that happy with this level of technical busy-work.  Save As... is so much harder than Save that the odds of success are nearly zero.

-   Save the file as XML.  This is pleasant, but again, you have to trust someone to do this correctly, since it isn't the MS-Office default.  Worse, if you try to make it the default, everyone in IT worries about the increase in file size.

-   Stop using MS-Office, and use Open Office.  This has lots and lots of merit, but often suffers from goofy organizational road-blocks.  Primarily the endless list of open source "issues": who provides support? who do we sue? bugs?  malware? licenses?  I ranted about this in` The Cost (and Benefit) of Open Source <{filename}/blog/2006/04/2006_04_24-the_cost_and_benefit_of_open_source.rst>`_ .

-   Write VBA scripts to convert the XLS spreadsheet to XML or a sequence of CSV files.  This compounds a yucky problem with more yuckiness.

-









:strong:`Enter XLRD`




It turns out that the Open Office organization has managed to reverse engineer enough of the mystery that is XLS files.  This has two important consequences: the `Apache POI project <http://poi.apache.org/>`_  and the Python `xlrd <http://www.lexicon.net/sjmachin/xlrd.htm>`_  package.




With XLRD I can read the XLS file directly, cutting down on the user's busy-work to save the file in a usable format.  Using Python allows me to work through the consistency problem.  This usually leads to a class hierarchy which handles variations on the expected spreadsheet.




A bonus is that we can unify XLRD-based readers with XML parsers to deal with a wide variety of spreadsheet data sources.




We're still left with the remaining two hard parts -- DB design and consistency.  With Python we can easily build something meta-data driven.  In particular, we can use Python's introspection capabilities to have flexible high-level mappings from various kinds of spreadsheets to the RDBMS tables.




