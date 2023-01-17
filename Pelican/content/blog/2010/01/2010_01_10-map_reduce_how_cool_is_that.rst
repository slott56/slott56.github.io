Map Reduce -- How Cool is that?
===============================

:date: 2010-01-10 12:57
:tags: map-reduce,#python,design
:slug: 2010_01_10-map_reduce_how_cool_is_that
:category: Technologies
:status: published

From time-to-time I hear a few mentions of MapReduce; up until recently,
I avoided looking into it.

This month's `CACM <http://cacm.acm.org/magazines/2010/1>`__,
however, is chock-full of MapReduce goodness.

After reading some of the articles, I decided to look a little more
closely at that approach to handling large datasets.

Python Implementation
---------------------

Map-Reduce is a pleasant functional approach to handling several
closely-related problems.

-  Concurrency.
-  Filtering and Exclusion.
-  Transforming.
-  Summarizing.

The good part is that it works with no magic. The best part is that
you can build map-reduce processors very easily with readily
available tools.

Map-Reduce on the Cheap
-----------------------

The basics of map reduce can be done several ways in Python. We could
use the built-in
`map <http://docs.python.org/library/functions.html#map>`__ and
`reduce <http://docs.python.org/library/functions.html#reduce>`__
functions. This can lead to problems if you provide a poorly designed
function to reduce.

But Python also provides generator functions. See `PEP
255 <http://www.python.org/dev/peps/pep-0255/>`__ for background on
these. A generator function makes it really easy to implement simple
map-reduce style processing on a single host.

Here's a simple web log parser built in the map-reduce style with
some generator functions.

Here's the top-level operation. This isn't too interesting because it
just picks out a field and reports on it. The point is that it's
delightfully simple and focused on the task at hand, free of clutter.
::

    def dump_log( log_source ):
        for entry in log_source:
            print entry[3]

We can improve this, of course, to do yet more calculations,
filtering and even reduction. Let's not clutter this example with too
much, however.
Here's a map function that can fill the role of log_source. Given a
source of rows, this will determine if they're parseable log entries
and yield up the parse as a 9-tuple. This maps strings to 9-tuples,
filtering away anything that can't be parsed.
::

    log_row_pat= re.compile( r'(\d+\.\d+\.\d+\.\d+) (\S+?) (\S+?) (\[[^\]]+?]) ("[^"]*?") (\S+?) (\S+?) ("[^"]*?") ("[^"]*?")' )
    def log_from_rows( row_source ):
        for row in row_source:
            m= log_row_pat.match( row )
            if m is not None:
                yield m.groups()

This log source has one bit of impure functional programming. The
tidy, purely functional alternative to saving the match object, m,
doesn't seem to be worth the extra lines of code.
Here's a map function that can participate as a row source. This will
map a file name to an sequence of individual rows. This can be
decomposed if we find the need to reuse either part separately.
::

    def rows_from_name( name_source ):
        for aFileName in name_source:
            logger.info( aFileName )
            with open(aFileName,"r") as source:
                for row in source:
                    yield row

Here's a mapping from directory root to a sequence of filenames
within the directory structure.
::

    def names_( root='/etc/httpd/logs' ):
        for path, dirs, files in os.walk( root ):
            for f in files:
                logging.debug( f )
                if f.startswith('access_log'):
                    yield os.path.join(path,f)

This applies a simple name filter. We could have used Python's
fnmatch, which would give us a slightly more extensible structure.
Putting it Together
This is the best part of this style of functional programming. It
just snaps together with simple composition rules.
::

    logging.basicConfig( stream=sys.stderr, level=logging.INFO )
    dump_log( log_from_rows( rows_from_name( names_from_dir() ) ) )
    logging.shutdown()

We can simply define a of map functions. Our goal, expressed in
dump_log, is the head of the composition. It depends on the tail,
which is parsing, reading a file, and locating all files in a
directory.

Each step of the map pipeline is a pleasant head-tail composition.

Pipelines

This style of programming can easily be decomposed to work through
Unix-style pipelines.

We can cut a map-reduce sequence anywhere. The head of the
composition will get it's data from an unpickle operation instead of
the original tail.

The original tail of the composition will be used by a new head that
pickles the results. This new head can then be put into the source of
a Unix-style pipeline.

Parallelism

There are two degrees of parallelism available in this kind of
map-reduce. By default, in a single process, we don't get either one.
However, if we break the steps up into separate physical processes,
we get huge performance advantages. We force the operating to do
scheduling. And we have processes that have a lot of resources
available to them.

    [Folks like to hand-wring over "heavy-weight" processing vs. threads.
    Practically, it rarely matters. Create processes until you can prove
    it's ineffective.]

Additionally, we can -- potentially -- parallelize each map
operation. This is more difficult, but that's where a framework helps
to wring the last bit of parallel processing out of a really large
task.

Until you need the framework, though, you can start doing map-reduce
today.

A Link: http://hadoop.apache.org/mapreduce/



-----

Regarding heavy processes - windows does indeed ha...
-----------------------------------------------------

Mark Mc Mahon<noreply@blogger.com>

2010-01-12 04:10:03.584000-05:00

Regarding heavy processes - windows does indeed have a big difference
between processes and threads. (Creating processes is quite slow in
Windows). See
http://stackoverflow.com/questions/1289813/python-multiprocessing-vs-threading-for-cpu-bound-work-on-windows-and-linux


I wouldn&#39;t count saving the match object &#39;...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-01-14 11:26:27.622000-05:00

I wouldn't count saving the match object 'm' as 'impure'. You don't
redefine 'm' or mutate it. The fact that the underlying implementation
(which creates a variable in a locals dict) can allow mutation doesn't
really affect this issue - you are using variable assignment in a pure
way.





