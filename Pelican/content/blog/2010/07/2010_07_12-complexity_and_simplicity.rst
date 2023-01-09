Complexity and Simplicity
=========================

:date: 2010-07-12 21:45
:tags: #python,WebServices,design
:slug: 2010_07_12-complexity_and_simplicity
:category: Technologies
:status: published

Here's an interesting -- and common -- question.

    "... any tools that I could use to create a web scraper that I could
    use to interact with a .aspx website?

I want to build a tool that will read an input file (e.g. an excel
spreadsheet) containing a list of property parcel numbers, and for
each parcel number:

-   connect to the property appraiser's website (which happens to be the .aspx page),

-   enter the parcel number,

-   scrape selected data (which is contained in a table on the search results page)

-   store the scraped data in an output file (e.g. in the excel file that contains the input list)

-   repeat the process for each parcel number"

The follow-on is interesting, also.

    "I've created an excel macro which does the above with 'simple /
    plain vanilla html pages using the WebQuery feature, but it can't
    interact with an .aspx page."

Let's consider some of the complexities and simplicities that are
present here.

**Solution-Speak**

First, and most important, this is written in solution-speak. It's an
IT habit, and it's very hard to break. The input appears to be a
spreadsheet. It may not *actually* be a spreadsheet, but this
description essentially forces the solution to be built around the
spreadsheet. The source may be another web page or some other file
format. Since the problem is written in solution-speak, we don't know
and can't -- easily -- explore the alternatives.

Let's assume that the source actually is a spreadsheet. And that this
is the *real* source; it's maintained manually by the person who
really "owns" the data.

The "update-in-place" nature of the question ("e.g. in the excel
file that contains the input list") constrains the solution. This
tends to add complexity because it somehow *seems* simpler to
update a file in place.

What's *actually* simpler is often a process that creates a next
revision of the file, leaving the first one intact and read-only.
It's actually simpler because the "revert" strategy -- in case of
problems -- is trivial. Simply delete the new file, fix the data (or
the software) and run things again. Backup and history are simpler
when creating a new file, also.

**Technology Choices**

Since it's written in solution speak, many technology choices have
been made that might be inappropriate.

First, it appears that Excel is the "database" of choice. This is a
terrible thing, but very, very common. The person has a problem. They
tried to solve it with a spreadsheet. Now they have two problems.

A spreadsheet has a great GUI, but -- sadly -- leads to weird,
inconsistent, undisciplined and generally "out-of-control" data. It
doesn't have to create a mess, but it's hard to constrain it to
prevent creating a mess.

**Alternatives**

This problem is ubiquitous and -- often -- trivial to solve if we cut
Excel out of the picture.

Consider this workflow.

#.  A small Python program uses xlrd to read this "list of property
    parcel numbers" and creates a simple CSV file. Excel is now
    officially out of the picture. If this process can't run (because
    the spreadsheet got tweaked) we can produce elegant reports with
    row and column information so that the person creating the
    spreadsheet can fix their problem. Let's say this is 20 lines of
    code, assuming the spreadsheet is hellishly complex.

#.  Some small Python programs read a CSV file, uses urllib2 to
    "connect to the property appraiser's website (which happens to be
    the .aspx page), enter the parcel number", do the POST and
    retrieve the resulting page. This can be written to a file for
    future reference purposes. Numerous problems will be encountered
    here every time an appraiser's web site changes. It's best to keep
    this separate, since there may be several, each unique to an
    appraiser. There's no reason to generalize. Each of these is under
    20 lines of code. Often under a dozen.

#.  Some small Python program reads the resulting pages, uses
    Beautiful Soup to parse the resulting HTML. Again, numerous
    problems will be encountered here every time an appraiser's web
    site changes. It's pleasant to keep this separate from posting the
    query since this is just parsing result pages and doing nothing
    more. Easy to tweak and fix to keep up with changes. However,
    because of the potential complexity of each page, these might be
    complex. Let's pretend they're 20+ lines of code.

#.  Some small Python program merges the original "list of property
    parcel numbers" and parsed results into a new .CSV file. With a
    double-click, this will be loaded back into Excel to make it look
    like the file was updated more-or-less in place. This should be
    about a dozen lines of code.

Since each step is separate, each can be written, tested and
debugged separately. Once they work, some kind of master script
can sequence through all four steps. That master script should be
under a dozen lines of code.

**Design Patterns**

One important design pattern is to get out of "Office Product" mode
as early as possible. Office Produces (like Excel) are fine for
people, but dreadful for automation. They're too complex.

Another important design pattern is to decompose the problem into
small scripts that can be run independently. Each step creates a work
result that can be viewed and used for debugging. The files aren't
big and can be deleted when the final work product is created. But an
overly automated system is very, very hard to debug.

Another design pattern is to separate the various web services
requests (in this case a form POST) by destination web site. Each
site has unique security and validation considerations. It's too
complex to write a super-universal, uber-form-filler-outer. It's
easier to write a bunch of specific RESTful web services requests
that are tailored to the unique problems present in each site.

Finally, it's important to avoid "update in place". It's hard to do
well, and it's a pain in the neck when something goes wrong and you
want to fall back to the previous version of the database.



-----


Yep, I had a similar experience in 2003.  I was as...
-----------------------------------------------------

Bill Karwin<noreply@blogger.com>

2010-07-13 12:15:32.097000-04:00

Yep, I had a similar experience in 2003. I was asked to write a script
to import a data dump that was emailed in Excel format. I wrote the
script, but the next week the spreadsheet arrived with a new,
incompatible layout. Changes included new columns, new order of columns,
new column header labels, and ad hoc "notes" fields sprinkled
throughout.

Again the third week and the fourth week, the layout of the worksheet
was different from any of the weeks prior.

I rewrote the data import script each week, while I tried in vain to
communicate to my manager that the spreadsheet must be in a consistent
format or else the work I did to "automate" data import would have to be
re-done, and with that much work, we might as well have done data entry
by hand. My explanation had no effect; the spreadsheets continued to be
submitted with a different layout each week.

Finally my contract at that company ended and I departed (somewhat with
relief, as this incident was typical of the communication failures I
faced). I think it's safe to assume that the data import broke again the
next week, and the company would have no understanding of why it broke.

