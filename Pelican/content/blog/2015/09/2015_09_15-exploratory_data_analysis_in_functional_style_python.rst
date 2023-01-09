Exploratory Data Analysis in Functional-Style Python
====================================================

:date: 2015-09-15 08:00
:tags: #python,functional programming,Data Science
:slug: 2015_09_15-exploratory_data_analysis_in_functional_style_python
:category: Technologies
:status: published


Here are some tricks to working with log file extracts. We're looking
at some Enterprise Splunk extracts. We can fiddle around with Splunk,
trying to explore the data. Or we can get a simple extract and fiddle
around with the data in Python.

Running different experiments in Python seems to be more effective
than trying to do this kind of exploratory fiddling in Splunk.
Primarily because there aren't any boundaries on what we can do with
the data. We can create very sophisticated statistical models all in
one place.

Theoretically, we can do a lot of exploration in Splunk. It has a
variety of reporting and analytical features.

But...

Using Splunk presumes we know what we're looking for. In many cases,
we don't know what we're looking for: we're exploring. We may have
some indication that a few RESTful API transactions are slow, but
little more than that. How do we proceed?

Step one is to get raw data in CSV format. Now what?

Reading Raw Data
----------------


We'll start by wrapping a CSV.DictReader object with some additional
functions.

Object-Oriented Purists will object to this strategy. "Why not just
extend DictReader?" they ask. I don't have a great answer. I lean
toward functional programming and the resulting orthogonality of
components. With a purely OO approach, we have to use more
complex-seeming mixins to achieve this.

Our general framework for processing logs is this.

::

    with open("somefile.csv") as source:
       rdr = csv.DictReader(source)




This allows us to read the CSV-formatted Splunk extract. We can
iterate through rows in the reader. Here's trick #1. It's not
**really** very tricky, but I like it.

::

    with open("somefile.csv") as source:
       rdr = csv.DictReader(source)
       for row in rdr:
           print( "{host} {ResponseTime} {source} {Service}".format_map(row) )



We can -- to a limited extent -- report raw data in a helpful format.
If we want to dress up the output, we can change the format string.
Maybe "{host:30s} {ReponseTime:8s} {source:s}" or something like that.

Filtering
---------


A common situation is that we've extracted too much, and only need to
see a subset. We can change the Splunk filter, but, we hate to
overcommit before we've finished our exploration. It's far easier to
filter in Python. Once we've learned what we need, we can finalize in
Splunk.





::

    with open("somefile.csv") as source:
       rdr = csv.DictReader(source)
       rdr_perf_log = (row for row in rdr if row['source'] == 'perf_log')
       for row in rdr_perf_log:
           print( "{host} {ResponseTime} {Service}".format_map(row) )




We've injected a generator expression that will filter the source
rows, allowing us to work with a meaningful subset.

Projection
----------


In some cases, we'll have additional columns of source data that we
don't really want to use. We'll eliminate this data by making a
projection of each row.

In principle, Splunk never produces an empty column. However, RESTful
API logs may lead to data sets with a huge number of unique column
titles based on surrogate keys that are part of request URI's. These
columns will have one row of data from the one request that used that
surrogate key. For every other row, there's nothing useful in that
column. Life is much simpler if we remove the empty columns from each
row.

We can do this with a generator expression, also, but it gets a bit
long. A generator function is somewhat easier to read.

::

    def project(reader):
       for row in reader:
           yield {k:v for k,v in row.items() if v}




We've built a new row dictionary from a subset of the items in the
original reader. We can use this to wrap the output of our filter.

::

    with open("somefile.csv") as source:
       rdr = csv.DictReader(source)
       rdr_perf_log = (row for row in rdr if row['source'] == 'perf_log')
       for row in project(rdr_perf_log):
           print( "{host} {ResponseTime} {Service}".format_map(row) )


This will reduce the unused columns that are visible in the inside of
the for statement.

Notation Change
---------------

The row['source'] notation will get clunky. It's much nicer to work
with a types.SimpleNamespace than a dictionary. This allows us to use
row.source.

Here's a cool trick to create something more useful.

::

  rdr_ns = (types.SimpleNamespace(**row) for row in reader)

We can fold this into our sequence of steps like this.

::

  with open("somefile.csv") as source:
      rdr = csv.DictReader(source)
      rdr_perf_log = (row for row in rdr if row['source'] == 'perf_log')
      rdr_proj = project(rdr_perf_log)
      rdr_ns = (types.SimpleNamespace(**row) for row in rdr_proj)
      for row in rdr_ns:
          print( "{host} {ResponseTime} {Service}".format_map(vars(row)) )

Note the small change to our format_map() method. We've added the
vars() function to extract a dictionary from the attributes of a
SimpleNamespace.

We could write this as a function to preserve syntactic symmetry with
other functions.

::

  def ns_reader(reader):
      return (types.SimpleNamespace(**row) for row in reader)

Indeed, we could write this as a lambda construct which is used like
a function.

::

  ns_reader = lambda reader: (types.SimpleNamespace(**row) for row in reader)

While the ns_reader() function and ns_reader() lambda are used the
same way, it's slightly harder to write a document string and doctest
unit test for a lambda. For this reason, a lambda should probably be
avoided.

We can use map(lambda row: ``types.SimpleNamespace(**row), reader)``.
Some folks prefer this over the generator expression.
We could use a proper for statement with an internal yield statement,
but there doesn't seem to be any benefit from making a big statement
out of a small thing.

We have a lot of choices because Python offers so many functional
programming features. We don't often see Python touted as a
functional language. Yet, we have a variety of ways to handle a
simple mapping.

Mappings: Conversions and Derived Data
--------------------------------------

We'll often have a list of data conversions that are pretty obvious.
Plus, we'll have a growing list of derived data items. The derived
items will be dynamic and are based on different hypotheses we're
testing. Each time we have an experiment or question, we might change
the derived data.

Each of these steps: filtering, projection, conversions, and
derivation, are stages in the "map" portion of a map-reduce pipeline.
We could create a number of smaller functions and apply them with
map(). Because we're updating a stateful object, we can't use the
general map() function.  If we wanted to achieve a more pure
functional programming style, we'd use an immutable namedtuple
instead of a mutable SimpleNamespace.

::

  def convert(reader):
      for row in reader:
          row._time = datetime.datetime.strptime(row.Time, "%Y-%m-%dT%H:%M:%S.%F%Z")
          row.response_time = float(row.ResponseTime)
          yield row

As we explore, we'll adjust the body of this conversion function.
Perhaps we'll start with some minimal set of conversions and
derivations. We'll extend this with some "are these right?" kind of
things. We'll take some out when we discover that the don't work.
Our overall processing looks like this:

::

  with open("somefile.csv") as source:
      rdr = csv.DictReader(source)
      rdr_perf_log = (row for row in rdr if row['source'] == 'perf_log')
      rdr_proj = project(rdr_perf_log)
      rdr_ns = (types.SimpleNamespace(**row) for row in rdr_proj)
      rdr_converted = convert(rdr_ns)
      for row in rdr_converted:
          row.start_time = row._time - datetime.timedelta(seconds=row.response_time)
          row.service = some_mapping(row.Service)
          print( "{host:30s} {start_time:%H:%M:%S} {response_time:6.3f} {service}".format_map(vars(row)) )

Note that change in the body of our for statement. Our ``convert()``
function produces values we're sure of. We've added some additional
variables inside the for loop that we're not 100% sure of. We'll see
if they're helpful (or even correct) before updating the ``convert()``
function.

Reductions
-----------

When it comes to reductions, we can adopt a slightly different style
of processing. We need to refactor our previous example, and turn it
into a generator function.

::

  def converted_log(some_file):
      with open(some_file) as source:
          rdr = csv.DictReader(source)
          rdr_perf_log = (row for row in rdr if row['source'] == 'perf_log')
          rdr_proj = project(rdr_perf_log)
          rdr_ns = (types.SimpleNamespace(**row) for row in rdr_proj)
          rdr_converted = convert(rdr_ns)
          for row in rdr_converted:
              row.start_time = row._time - datetime.timedelta(seconds=row.response_time)
              row.service = some_mapping(row.Service)
              yield row

We've replace the ``print()`` with a ``yield``.
Here's the other part of this refactoring.

::

  for row in converted_log("somefile.csv"):
      print( "{host:30s} {start_time:%H:%M:%S} {response_time:6.3f} {service}".format_map(vars(row)) )

Ideally, all of our programming looks like this. We use a generator
function to produce data. The final display of the data is kept
entirely separate. This allows us to refactor and change the
processing much more freely.

Now we can do things like collect rows into Counter() objects, or
perhaps compute some statistics. We might use a defaultdict(list) to
group rows by service.

::

  by_service= defaultdict(list)
  for row in converted_log("somefile.csv"):
      by_service[row.service] = row.response_time
  for svc in sorted(by_service):
      m = statistics.mean( by_service[svc] )
      print( "{svc:15s} {m:.2f}".format_map(vars()) )

We've decided to create concrete list objects here. We can use
itertools to group the response times by service. It looks like
proper functional programming, but the implementation points up some
limitations in the Pythonic form of functional programming. Either
we have to sort the data (creating a list object) or we have to
create lists as we group the data. In order to do several different
statistics, it's often easier to group data by creating concrete
lists.

Rather than simply printing a row object, we're now doing two things.

#.  Create some local variables, like svc and m. We can easily add
    variance or other measures.

#.  Use the vars() function with no arguments, which creates a
    dictionary out of the local variables.


This use of ``vars()`` with no arguments -- which behaves like
``locals()`` -- is a handy trick. It allows us to simply create any
local variables we want and include them in the formatted output.
We can hack in as many different kinds of statistical measures as
we think might be relevant.

Now that our essential processing loop is for row in
``converted_log("somefile.csv")``, we can explore a lot of processing
alternatives in a tiny, easy-to-modify script. We can explore a
number of hypotheses to determine why a some RESTful API transactions
are slow and others are fast.





