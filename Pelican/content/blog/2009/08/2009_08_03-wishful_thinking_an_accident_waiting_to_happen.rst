Wishful Thinking -- An Accident Waiting To Happen
=================================================

:date: 2009-08-03 07:39
:tags: agile,object-oriented design
:slug: 2009_08_03-wishful_thinking_an_accident_waiting_to_happen
:category: Technologies
:status: published

Some assumptions are really hard to identify as "assumptions". Some
assumptions are more "wishful thinking" than "assumption".

We process a lot of spreadsheets. As far as I'm concerned, the
Spreadsheet User Interface (SUI) is a first-class part of any
application. Users understand them, and you don't have to code as
much.

We have a library that wraps
`XLRD <http://pypi.python.org/pypi/xlrd/0.5.2>`__,
`csv <http://docs.python.org/library/csv.html>`__,
`zipfile <http://docs.python.org/library/zipfile.html>`__ and
`ElementTree <http://docs.python.org/library/xml.etree.elementtree.html>`__
XML parsing to read a wide variety of spreadsheet formats.

However, we were recently stabbed by an assumption. I had to spend
over 40 hours restructuring our workbook library and application
code.

Go With What You Know
---------------------

The point of an Agile approach is to build high-value things first.
In the olden days, we would have spent months (really) writing a
sophisticated set of hypothetical use cases for the workbook library
and then designing something that would cover all possible bases.

Rather than spend endless hours on the potential workbook features, I
wrote what we needed to read the workbook files we actually had. We
had a mixture of XLS, XLS in ZIP files, and CSV files. So we unified
those with a fairly simple model of a "Row Source" that provided
information on sheets, and provided the sequence of rows.

However, all those spreadsheets had a common feature. They were built
by people with a strong IT background, people who -- even if they
couldn't define "Normalization" -- knew what normalized data looked
like. They provided everything as proper columns.

Recently, we got some data for a new customer pilot that was just
enough different that it was a costly problem.

What Changed?
-------------

The change was the use of the sheet tab names to carry meaningful key
information.

Every previous example either had sheets with names like "sheet1",
"sheet2" and "sheet3", or the sheet name was something we could
filter on.

This workbook had the time dimension coded in the sheet names, not a
column of data on each sheet. Suddenly, the worksheet name was
significant. And that's not all.

How Bad Can It Be?
------------------

The extensive breakage came from a bad design decision buried in the
workbook library and all application layers that depend on the
workbook libraries. Assuming that data was in columns -- instead of
sheet names -- didn't create a big problem. Unwinding that assumption
was an easy to fix.

What was bad was a design that permitted the various mappings to be
independent of each other. The "operation" classes that stepped
through rows were designed so that a simple list of independent
mappings could be used to extract relevant columns from a row and
process them. Each independent mapping created a Python object from
columns.

It turns out that each mapping needed a context (with worksheet
name). Also, it turns out that some mappings actually depend on other
mappings.

When the mappings are picking up columns, having several mappings
depending on a single column is easy. Having several mappings depend
on the context, wasn't too bad. Having one mapping that parsed the
sheet name, exposed our wishful thinking.

We needed to have mappings that depended on each other. When we map
the sheet name to a Python object, we did parsing and database
lookups. Other mappings now must be "aware" of this mapping so they
don't redo the parsing and database lookups.

Lessons Learned
---------------

The trivial (and wrong) lesson learned could be "don't make so many
assumptions". That's silly. We didn't casually make assumptions. We
had example data; the sample data was biased and didn't show all
conceivable permutations.

Another trivial (and wrong) lesson could be "document all your
assumptions". That's silly, too. We did document them. That doesn't
make the breakage significantly easier to fix.

The real lesson is to avoid wishful thinking . We'd tried too hard to
make all of the mappings into independent objects. The phrase "shared
nothing" is our mantra. While shared nothing gave us a very
composable design, it wasn't actually correct.





