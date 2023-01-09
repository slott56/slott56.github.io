Great Quotes about The Spreadsheet Problem™
===========================================

:date: 2007-02-07 18:10
:tags: architecture,design,data structure,algorithm
:slug: 2007_02_07-great_quotes_about_the_spreadsheet_problemtm
:category: Architecture & Design
:status: published





Here are some useful quotes:

-   Andrew’s first law of career
    spotting:  Accountants are people who, when confronted with a problem, think
    “I know, I’ll use [A spreadsheet]”. Now they have two
    problems.

-   [A spreadsheet] is a great prototyping
    tool, just don’t let it anywhere near your production
    systems.



While `Panko <http://panko.cba.hawaii.edu/ssr/Mypapers/whatknow.htm>`_  provides a taxonomy of errors, it is
focused on quantitative errors, where an answer is demonstrably wrong.  In `Teo and Tan <http://portal.acm.org/citation.cfm?id=938435.938681&coll=GUIDE&dl=G&CFID=15151515&CFTOKEN=6184618>`_ , there is some discussion of
qualitative errors, but the discussion is limited to "jamming" constants into a
formula and duplicating values around the
model.



**Good Design.** 



Spreadsheet design is
essentially the same as other software design.  There are pretty
well-established patterns, and a spreadsheet that follows well-established
software design patterns is easier to work with than one that is
haphazard.



In particular, a basic
input-output pattern is critical to avoiding constants and duplication.  The
criteria for decomposing modules, based on allocation of responsibility,
minimizing coupling and maximizing cohesion are all essential for avoiding
duplication.  In some cases, a **Hidden Model** ™ page may be essential to cleanly
separating inputs from
reports.



Further, many of the basic
usability design patterns can  also be applied.  A spreadsheet that looks like a
document is useful for a final report.  A spreadsheet that looks like an input
panel is useful for the input side of the document.  Mixing the inputs and the
final report, while possible, isn't always the best
strategy.



**Spreadsheet as Document.** 



When we look at a `spreadsheet as syntax <{filename}/blog/2007/01/2007_01_25-spreadsheet_as_syntax.rst>`_  of a document for
capturing input from people, then we have to pay close attention to
user-interface design patterns.  In particular, most GUI's insist on labels
preceding input fields.  While this is largely taken for granted, anyone who has
worked with a GUI builder knows that you have labels and input controls in an
obvious juxtaposition.  Usually labels are to the left of controls, but
sometimes they are above.



In
spreadsheets, we see the strange and poorly-thought-out documents.  I think that
a substantial number of "qualitative" errors can be stemmed with a few design
guidelines.  Here's an example that could be used to train users in a better way
to use spreadsheets.

-   Sheet 1 - Instructions

-   Sheet 2 - Assumptions and Constants

-   Sheet 3 to *n*  -
    Inputs.  These sheets look like forms with labels and fields.  Some calculations
    are possible, as an aid to data entry, but the final answer isn't
    here.

-   Sheet *n* +1 to the end - Reports.  These sheets look like final documents.  The calculations
    depend on Assumptions and Inputs.



We
can, with a little XML and Python, validate the overall design pattern.  We can
locate constants in formulas, and improper references among
spreadsheets.



Further, we can parse
sheets 3 to
*n*  to
extract the meaningful user inputs and put them into a more sophisticated,
controlled, persistent and widely-shared
repository.



**The Hidden Model™** .



In
a few cases, a spreadsheet has outputs that come from the inputs via a tangle of
intermediate results.  Often that tangle is a business model that started out as
one tidy report and then expanded out of control (usually via copy and paste)
into a number of related reports.



Good
software design (i.e., the MVC pattern) tells us that we have two views of the
underlying model.  We have the input parameters, we have a number of related
reports.  Between the two, we have the model itself, often a pretty simple set
of calculations.   The control is implicit in the way spreadsheets work; we just
build the model and the views.














