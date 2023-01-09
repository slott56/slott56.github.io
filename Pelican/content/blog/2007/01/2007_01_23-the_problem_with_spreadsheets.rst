The Problem with Spreadsheets
=============================

:date: 2007-01-23 11:13
:tags: architecture,design,data structure,algorithm
:slug: 2007_01_23-the_problem_with_spreadsheets
:category: Architecture & Design
:status: published





See "`When a Column is Not a Column <{filename}/blog/2005/09/2005_09_27-essay_102_when_a_column_is_not_a_column.rst>`_ " for a rant on
failed attempts to scale spreadsheets up into relational databases.  Bottom
Line:  A spreadsheet column is rarely an RDBMS column.  Often the SS column's
label is a key value, just like the SS row's label, and the cell's value is
RDBMS data in the RDBMS row.  Both models borrow terminology, but the concepts
under those terms don't map very well.  It's almost universally a mistake to
transform a spreadsheet page (which is table-like) into a proper RDBMS
table.



Here's the interesting problem
*du jour* .  The customer has a collection of
massive spreadsheets (20 tabs) that are prepared by 20 or so people.  This
collection of 20 copies of the same template must then be consolidated into one
amalgam.



If the spreadsheets were just
data entry vehicles, we'd be replacing them with a simple web application, and
that would be straight-forward.



The
essential problem (to consolidate the data) is compounded by the spreadsheets
having some pretty fancy calculations and feedback. We could replace them with a
web application that had enough AJAX to be similar to the `Google Docs <http://docs.google.com/>`_  spreadsheet: it would
provide a rich user interface, and the data would be centrally
located.



**Collaboration and Consolidation.** 



In this case, the
collaboration is more than just consolidation.  While the proximate problem is
consolidation, we quickly uncovered additional use cases.  There are at least
three classes of actors: directors who originate the templates, managers who
fill in the templates, and analysts who consolidate and report on the
data.



The managers filling in the
templates, in some cases, actively use them to control their business.  They
create alternate scenarios, they make decisions, they take action and they
compare predicted results with actual results.  Other managers, however, don't
do more than fill in the templates and dutifully post them to the
analysts.



Our collaboration goes beyond
simple consolidation.  The superficial collaborative task is only the tip of a
larger iceberg of use cases for the spreadsheets.  What is a technology choice
that supports consolidation, but preserves the other use
cases?



**Excel Extraction.** 



Some managers make
extensive use of the original spreadsheet functionality; the spreadsheet's
native use cases are essential to the enterprise.  In addition to the
spreadsheet use cases, consolidation and refreshing history must be added to
this.  One of the decisions we have to make is where we allocate the additional
ETL (Extract Transform Load) processing that produces consolidated information. 
Since we working with (against?) MS-Office products, we're talking about some
fairly complex use cases with Excel at the center. 




Note that we have to strike a fine
balance between two opposing forces.

-   The Managers tinker with the spreadsheets
    as part of their business modeling.  The Directors also tinker with the
    templates as part of the larger planning cycle.

-   The Analysts need a fixed, standard set
    of spreadsheets they can consolidate without a lot of study and reverse
    engineering.  They need to prevent
    tinkering.



We have a spectrum of
platform alternatives.

-   Excel.  We can write gloriously complex
    macros and VB scripts and embed them in the spreadsheet.  This makes them large,
    difficult to email, and presents a security nightmare.  First, some email and
    firewall programs are grumpy about this kind of embedded functionality.  Second,
    and more important, managers are tinkering with the spreadsheets, but directors
    need standardization in the spreadsheets.  If we "lock things down" for the
    analysts' benefit, we prevent the managers from making good use of the tool.  If
    we allow the managers the freedom to use the tool, the analysts struggle to
    consolidate.

-   Desktop Application.  We can write a
    desktop application; this will exploit the .Net API's to extract from the local
    spreadsheet and load to a remote database.  This has to use more sophisticated
    parsing and pattern matching to tolerate tinkering.  However, it can also
    provide immediate feedback if names are dropped or changed, or cells moved in a
    way that makes the results hard to use.

-   Web Application.  We can write a web
    application to which people upload their spreadsheet, do the ETL on the web
    server, and then provide reports (or pivot tables) to help them manage their
    business.  Like a desktop application, this must have more sophisticated parsing
    and pattern-matching.  However, this can't even make good use of the .NET API's,
    but must work around a number of tragic
    limitations.



**A Show Stopper.** 



Here's a potential
show-stopper for the web alternative, "`Considerations for service-side
Automation of Office <http://support.microsoft.com/kb/257757>`_ ":  "Microsoft does not currently recommend, and
does not support, Automation of Microsoft Office applications from any
unattended, non-interactive client application or component (including ASP,
DCOM, and NT Services), because Office may exhibit unstable behavior and/or
deadlock when run in this environment." 




Ouch.



The
web application could have had a pretty nifty overview:

1.  The Director creates a new template and
    populates it with the most recent plan and the actual performance information. 
    It's posted to the collaboration website.

#.  The Manager gets the template from the web,
    makes changes, creates models, does the managerial thing.  The Manager uploads
    spreadsheets from time to time.  At some point, one is the "current" plan, and
    is canonized for purposes of overall enterprise consolidated business
    planning.

#.  The Analysts have all of the Manager's uploads
    to consolidate and report on.



The
end-user experience would be slightly different than today's mass-emailing
frenzy.  There'd be a nice collaboration web site for upload and download.  The
upload would validate and provide feedback as part of the upload
process.



It appears that we can't make
this work very easily.



**Desktop and Excel Platforms.** 



I'm not a big
fan of the desktop as a platform.  Primarily, I hate the configuration
management problem: who has what version of the
application.



"But there are tools to
help."  



While true, desktop deployment
tools merely plaster over the essential problem:  the people who "control" the
desktop aren't very disciplined.  We can only make desktop software work as part
of a total lock-down of the end-user's computer.  Since the client doesn't do
this (and won't for this one business application), we can't really make use of
the desktop as a platform.



Excel is a
viable programming platform.  However, it, too is prone to getting out of
control.  The current 20-plus-tab monstrosity is packed full of macros and VB
modules and doesn't work reliably.  In addition to bugs, people can easily add
inter-workbook links to documents on their C: drive and in their Windows TEMP
directory.  The whole thing rapidly spins out of control when we try to make use
of the clever features of Excel.  We need something simpler and more
reliable.



**Enter POI and XML.** 



We can exploit two
technologies to make a simple, reliable web-based solution.  First, we have
`Jakarta
POI <http://jakarta.apache.org/poi/>`_ , which allows us to read Excel files directly.  This is pleasant,
and the HSSF reliably picks apart a spreadsheet.  Second, we can use XML
versions of the spreadsheets, making them readable by `SAX <http://sax.sourceforge.net/>`_  or `Xerces <http://xerces.apache.org/>`_ .



Here's
the overall Compiler design pattern, and how we would implement it:

-   Lexical scanning is done by POI or SAX. 
    From this, we get a sequence of tokens which are Worksheets, Rows and
    Cells.

-   Parsing is done by our application.  From
    the sequence of Cells, Rows and Worksheets, we assemble higher-level constructs
    that are the essential Business Entities described in the spreadsheets.  If the
    user has made the wrong kinds of changes, we can't interpret the spreadsheet,
    and must reject the upload with an error.  Since we know the Worksheet, Row and
    Cell where parsing fell apart, we can report an error pretty
    precisely.



Once we've parsed the
spreadsheet and have the Business Entities, we can then do the required
transform and load operations.  These will lead to the consolidated data.  We
can then cough out the next generation template, or a reporting pivot table, or
simply redirect the user to a typical data warehouse reporting
portal.



**Spreadsheet as Syntax.** 



This leaves us with the
spreadsheet document filling an interesting role in this processing.  Rather
than being an active platform, the spreadsheet is downgraded to a mostly passive
document with a few active elements. 




Once we look at a spreadsheet as a
kind of syntax -- a sequence of tokens -- we can parse it using either of a
couple of techniques.  We can try to create an `LR <http://en.wikipedia.org/wiki/LR_parser>`_
or `LL <http://en.wikipedia.org/wiki/LL_parser>`_   kind of grammar, which may work out,
depending on how complex the spreadsheet is.  Often, user inputs are preceded by
labels which allow us to do very simple LR(0) parsing.




We can, for example, look for the cell
which contains the "Weekly Forecast" data.  In the next row, a cell will have a
product name, and the following cell will have a forecast number of cases
sold.



The other technique is to use a
more sophisticated `regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_  technique where we need to
see a longer sequence of cells or rows to determine the pattern.  These aren't
as easy to implement because most RE processing software works with individual
characters.  We would need to write a RE matcher as a `non-deterministic finite automaton <http://en.wikipedia.org/wiki/Nondeterministic_Finite_State_Machine>`_  that worked
with Cells and Rows instead of
characters.



**Solution Outline.** 



Here's a fun kind of
solution.  It works best if the spreadsheets are pared down to just the input
sections with just enough calculation and history to facilitate creating
high-quality plans.  From the current spreadsheets, we would delete the various
tabs that are simply reporting and consolidation within the
spreadsheet.

1.  Directors build their templates, including
    ODBC queries which pull historical data into the spreadsheets for use by
    managers.  They save them as XML documents.  These are large, but also very easy
    to cope with.  They post them to the web site for use by managers.

#.  Managers download the spreadsheets and work
    with them.  They upload their various planning scenarios so that the plans can
    be validated, and reports can be generated from plans and actuals.

#.  Analysts use the same reporting tools that
    managers use.  The only practical difference between an analyst and a manager is
    the breadth of information which is visible.  A manager can see their plan, an
    analyst can see multiple plans.



The
upload process uses a SAX application to parse, validate, extract, transform and
load the spreadsheet.  In the (all-too-common) situation where the spreadsheet
doesn't parse successfully, there are two kinds of feedback:

-   An error page in the web
    application.

-   A revised spreadsheet with a different
    style for the erroneous section.



We'll
come back to spreadsheet as syntax in future posts.























