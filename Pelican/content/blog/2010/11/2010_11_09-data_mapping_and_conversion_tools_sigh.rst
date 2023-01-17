Data Mapping and Conversion Tools -- Sigh
=========================================

:date: 2010-11-09 08:00
:tags: ETL,#python
:slug: 2010_11_09-data_mapping_and_conversion_tools_sigh
:category: Technologies
:status: published

Yes, ETL is interesting and important.

But creating a home-brewed data mapping and conversion tool isn't
interesting or important. Indeed, it's just an attractive nuisance.
Sure, it's fun, but it isn't valuable work. The world doesn't need
another ETL tool.

The core problem is talking management (and other developers) into a
change of course. How do we stop development of Yet Another ETL Tool
(YAETLT)?

First, there's products like
`Talend <http://www.talend.com/index.php>`__,
`CloverETL <http://www.cloveretl.com/products/community-edition>`__
and `Pentaho <http://www.pentaho.com/products/data_integration/>`__
open source data integration. Open Source. ETL. Done.

Then, there's this list of `Open Source ETL
products <http://www.manageability.org/blog/stuff/open-source-etl>`__
on the Manageability blog. This list all Java, but there's nothing
wrong with Java. There are a lot of jumping-off points in this list.
Most importantly, the world doesn't need another ETL tool.

Here's a piece on `Open Source
BI <http://www.information-management.com/issues/20060601/1088417-1.html>`__,
just to drive the point home.

Business Rules
--------------

The ETL tools must have rules. Either simple field alignment or more
complex transformations. The rules can either be interpreted
("engine-based" ETL) or used to build a stand-alone program
("code-generating" ETL).

The engine-based ETL, when written in Java, is creepy. We have a JVM
running a Java app. The Java app is an interpreter for a bunch of ETL
rules. Two levels of interpreter. Why?

Code-generating ETL, OTOH, is a huge pain in the neck because you
have to produce reasonably portable code. In Java, that's hard. Your
rules are used to build Java code; the resulting Java code can be
compiled and run. And it's often very efficient. [Commercial products
often produce portable C (or COBOL) so that they can be very
efficient. That's really hard to do well.]

Code-generating, BTW, has an additional complication. Bad Behavior.
Folks often tweak the resulting code. Either because the tool wasn't
able to generate all the proper nuances, or because the
tool-generated code was inefficient in a way that's so grotesque that
it couldn't be fixed by an optimizing compiler. It happens that we
can have rules that run afoul of the boilerplate loops.

Old-School Architecture
-----------------------

First, we need to focus on the "TL" part of ETL. Our applications
receive files from our customers. We don't do the extract -- they do.
This means that each file we receive has a unique and distinctive
"feature". We have a clear SoW and examples. That doesn't help. Each
file is an experiment in novel data formatting and `Semantic
Heterogeneity <http://www.springerlink.com/content/vq07h7701u11852p/>`__.

A common old-school design pattern for this could be called "The ETL
Two-Step". This design breaks the processing into "T" and "L"
operations. There are lots of unique, simple, "T" options, one per
distinctive file format. The output from "T" is a standardized file.
A simple, standardized "L" loads the database from the standardized
file.

Indeed, if you follow the **ETL Two Step** carefully, you don't need
to actually write the "L" pass at all. You prepare files which your
RDBMS utilities can simply load. So the ETL boils down to "simple"
transformation from input file to output file.

Folks working on YAETLT have to focus on just the "T" step. Indeed,
they should be writing Yet Another Transformation Tool (YATT) instead
of YAETLT.

Enter the Python
----------------

If all we're doing is moving data around, what's involved?

::

  import csv
  result = {
    'column1': None,
    'colmnn2': None,
    # etc.
  }
  with open("source","rb") as source:
    rdr= csv.DictReader( source )
    with open( "target","wb") as target:
        wtr= csv.DictWriter( target, result.keys() )
        for row in rdr:
            result['column1']= row['some_column']
            result['column2']= some_func( row['some_column'] )
            # etc.
            wtr.writerow( result )

That's really about it. There appear to be 6 or 7 lines of overhead.
The rest is working code.

But let's not be too dismissive of the overhead. An ETL depends on
the file format, summarized in the import statement. With a little
care we can produce libraries similar to Python's csv that work with
XLS directly, as well as XLSX and other formats. Dealing with
COBOL-style fixed layout files can also be boiled down to an
importable module. The import isn't overhead; it's a central part of
the rules.

The file open functions could be seen as overhead. Do we really need
a full line of code when we could -- more easily -- read from stdin
and write to stdout? If we're willing to endure the inefficiency of
processing one input file multiple times to create several
standardized outputs, then we could eliminate the two with
statements. If, however, we have to merge several input files to
create a standardized output file, the one-in-one-out model breaks
down and we need the with statements and the open functions.

The for statement could be seen as needless overhead. It goes without
saying that we're processing the entire input file. Unless, of
course, we're merging several files. Then, perhaps, it's not a simple
loop that can be somehow implied.

It's Just Code
--------------

The point of Python-based ETL is that the problem "solved" by YATT
isn't that interesting. Python is an excellent transformation engine
ETL. Rather than write a fancy rule interpreter, just write Python.
Done.

We don't need a higher-level data transformation engine written in
Java. Emit simple Python code and use the Python engine. (We could
try to emit Java code, but it's not as simple and requires a rather
complex supporting library. Python's `Duck
Typing <http://www.voidspace.org.uk/python/articles/duck_typing.shtml>`__
simplifies the supporting library.)

If we don't write a new transformation engine, but use Python, that
leaves a tiny space left over for the YATT: producing the ETL rules
in Python notation. Rather than waste time writing another engine,
the YATT developers could create a GUI that drags and drops column
names to write the assignment statements in the body of the loop.

That's right, the easiest part of the Python loop is what we can
automate. Indeed, that's about all we can automate. Everything else
requires complex coding that can't be built as "drag-and-drop"
functionality.

Transformations
---------------

There are several standard transformations.

-   Column order or name changes. Trivial assignment statements handle
    this.

-   Mapping functions. Some simple (no hysteresis, idempotent)
    function is applied to one or more columns to produce one or more
    columns. This can be as simple as a data type conversion, or a
    complex calculation.

-   Filter. Some simple function is used to include or exclude rows.

-   Reduction. Some summary (sum, count, min, max, etc.) is applied to
    a collection of input rows to create output rows. This is an ideal
    spot for Python generator functions. But there's rarely a simple
    drag-n-drop for these kinds of transformations.

-   Split. One file comes in, two go out. This breaks the
    stdin-to-stdout assumption.

-   Merge. Two go in, one comes out. This breaks the stdin-to-stdout
    assumption, also. Further, the matching can be of several forms.
    There's the multi-file merge when several similarly large files
    are involved. There's the lookup merge when a large file is merged
    with smaller files. Merging also applies to doing key lookups
    required to match natural keys to locate database FK's.

-   Normalization (or Distinct Processing). This is a more subtle form
    of filter because the function isn't idempotent; it depends on the
    state of a database or output file. We include the first of many
    identical items; we exclude the subsequent copies. This is also an
    ideal place for Python generator functions.

Of these, only the first three are candidates for drag-and-drop.
And for mapping and filtering, we either need to write code or
have a huge library of pre-built mapping and filtering functions.

Problems and Solutions
----------------------

The YATT problem has two parts. Creating the rules and executing the
rules.

Writing another engine to execute the rules is a bad idea. Just
generate Python code. It's a delightfully simple language for
describing data transformation. It already works.

Writing a tool to create rules is a bad idea. Just write the Python
code and call it the rule set. Easy to maintain. Easy to test. Clear,
complete, precise.



-----

By chance, I was looking at what ETL tools had to ...
-----------------------------------------------------

AB<noreply@blogger.com>

2010-11-10 06:43:22.749000-05:00

By chance, I was looking at what ETL tools had to offer yesterday. At
first glance, it seems `PyF <http://pyfproject.org/>`__ is your kind of
system. Rules in Python; GUI to plug Python rules together if you need
it.





