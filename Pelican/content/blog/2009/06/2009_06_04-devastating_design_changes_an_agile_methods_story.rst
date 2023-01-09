Devastating Design Changes -- An Agile Methods Story
====================================================

:date: 2009-06-04 09:10
:tags: #python,csv,xlrd,agile
:slug: 2009_06_04-devastating_design_changes_an_agile_methods_story
:category: Technologies
:status: published

We have a design, we have code and we have tests that all pass.


Tuesday, we got some new input data that just wouldn't work.


What -- if anything -- went wrong?


Agile is as Agile Does


We're following an Agile approach for several reasons.


#.  I'm too lazy to draw up an elaborate project plan full of lies
    ("assumptions").

#.  Our requirements were two versions of a powerpoint slide  that
    showed one use case at the tail-end of a long information
    life-cycle.

#.  Outside the one slide, we had no concrete actors or use cases.  We
    had some clue what we were doing, but it involved inventing new
    business models for customers -- a challenging thing to
    "automate".


The Agile approach is that we pick a use case, build some stuff,
and put it into production.


One consequence of this is rapid response to requirements changes.
Another consequence is fundamental changes to the design.  A
small change to a use case could lead to devastating design
changes.


Learning is Fundamental
-----------------------


Since we didn't have all the requirements (indeed, we barely  had
any,) we knew we'd be learning as we went.  Tuesday's data drop
was one example.


We have a nice library to handle many of the vagaries of the
Spreadsheet-As-User-Interface (SAUI™) problem.  We use
`xlrd <http://www.lexicon.net/sjmachin/xlrd.htm>`__ and
`csv <http://docs.python.org/library/csv.html>`__ modules to
handle basic spreadsheet file formats.  (We have the ElementTree
parser standing by to handle xml, if  necessary.)  We use the rest
of the Python
`archiving <http://docs.python.org/library/archiving.html>`__
packages to handle ZIP files of spreadsheets.


We've broken spreadsheet processing down into layers.


-   Data Source.  All of our various sources offer methods to step
    through the sheets and rows.  This minimizes the various file
    format differences.  Note that CSV provides cells that are
    text, where xlrd provides cells in a variety of data types.  We
    have a Cell class hierarchy to implement all the conversions
    required.

-   Operation.  Each operation (validate, load, delete, etc.) is a
    subclass of a common Operation.  This operation is given a
    sheet and processes the rows of that sheet.  It doesn't know
    anything about the Data Source.

-   Builders.  Each row, generally, builds some model object which
    is either validated or validated and persisted in the database.
    The builder handles the mapping from spreadsheet column to DB
    column, along with data type conversions.


Sadly, we left something out.

  
  
The Devastating Change
----------------------

  

We had no use cases, so we were making things up as we went
along.  We'd made an implicit assumption in our sheet
operations.  All the data we'd been loading was polluted with
rows we had to ignore.  So we tossed a quick-and-dirty little
if-statement down inside one of the sheet operations.



The new data had slightly different rules for rows we were
supposed to ignore.  The quick-and-dirty little if-statement
broke the loads.



We have to refactor our sheet operations to hoist out this
if-statement.  We have to use the Strategy pattern to replace
the statement with a formal appeal to a Filter object that
implements the decision.



What If Analysis
-----------------


The Cost Of Learning (COL™) was two days.  Half of one day to
find the problem.  Half of another to reason out the root cause
and determine a solution.  Finally, a full day to code and test
the revisions.



Yes, it took two full days of effort (spread over three
calendar days) to figure out what was wrong.



What if we had tried a waterfall design?  Would we have found,
designed and resolved this problem in two days?  No earthly
way.  It would have taken two days of brainstorming to think of
the use case.  It would have taken a week of hand-wringing to
work out a be-all-and-do-all processing pipeline for
spreadsheet data -- one that included dynamic filtering.



Instead, we built a processing pipeline that worked.  Now we're
expanding that processing pipeline to add a feature.







