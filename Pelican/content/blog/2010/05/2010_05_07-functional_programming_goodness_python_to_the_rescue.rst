Functional Programming Goodness -- Python to the Rescue
=======================================================

:date: 2010-05-07 08:00
:tags: #python,threads,functional programming
:slug: 2010_05_07-functional_programming_goodness_python_to_the_rescue
:category: Technologies
:status: published

Here's the situation.

A vendor sent us three separate files which need to be merged.
70,000+ records each. They're CSV files, so column *position* doesn't
much matter. The column *name* (in row 1) is what matters.

I looked at three solutions. Two of which are merely OK. The third
was some functional programming that was very cool.

Option 1 -- OS Sort/Merge
-------------------------

To get the files into a consistent order, we need to sort. The Linux
sort, however, is biased toward columns that are known positionally.

So, we need to exploit the **Decorate-Sort-Undecorate** design
pattern. So we have a shell script something like the following.

::

    decorate.py a.csv | sort >a_sorted.csv
    decorate.py b.csv | sort >b_sorted.csv
    decorate.py c.csv | sort >c_sorted.csv
    sort -m a_sorted.csv b_sorted.csv c_sorted.csv | undecorate.py >result.csv

This works well because decorate.py and undecorate.py are such simple
programs. Here's decorate.py.

::

    from __future__ import print_function
    import csv
    import sys
    with open(sys.argv[1],"rb") as source:
        rdr= csv.DictReader( source )
        for row in rdr:
            print( row['the key'], row )

Undecorate is similar. It uses the str.partition() method to remove
the decoration.

Note that the initial "decorate" steps can be run concurrently,
leading to some time reduction. This scales well. It doesn't use much
memory; the OS concurrency management means that it uses every core
available.

I didn't benchmark this, BTW.

Option 2 -- Big In-Memory Dict
------------------------------

Since the files aren't insanely big, they do fit in memory. This is
pretty simple, also.

::

    import csv
    from collections import defaultdict

    # build the result set
    result = defaultdict( dict )
    for f in ( 'a.csv', 'b.csv', 'c.csv' ):
        with open( f, 'rb' ) as source:
             rdr = csv.DictReader( source )
             for row in rdr:
                 result[row['key']].update( row )

    # find the column titles
    keys = set()
    for row in result:
        keys |= set( result[row].keys() )

    # write the result set
    with open( 'output.csv', 'wb' ) as target:
         wtr= csv.DictWriter( target, sorted(keys) )
         wtr.writerow( dict(zip(keys,keys)) )
         for row in result:
             wtr.writerow( result[row] )

This isn't too bad. For insanely big files, however, it won't scale
well.

Elapsed time for the real files (which were zipped, adding processing
that's not relevant to this posting) was 218 seconds on my little
laptop.

Option 3 -- Functional Programming
----------------------------------

The functional programming approach is a bit more code than option 1.
But it's way cool and very extensible. It offers more flexibility
without the memory limitation of the big dictionary.

Let's start with the end in mind.

We're doing a 3-file merge. The algorithm for 2-file merge is really
simple. The algorithm for an *n*-file merge, however, is not so
simple. We can easily build up an *n*-file merge as a composition of
*n*-1 pair-wise merges.

Here's how it should look.

::

    with open('temp.csv','wb') as output:
        wtr= csv.DictWriter( output, sorted(fieldNames) )
        wtr.writerow( dict( zip( fieldNames, fieldNames )))
        for row in merge( merge( s1, s2 ), s3 ):
            wtr.writerow( row )

We're doing merge( merge( s1, s2 ), s3 ) to compose a 3-file merge
from 2 2-file merges. And yes, it *can* be just that simple.

Composable Sort
---------------

To be "composable", we must write iterator functions which read and
write data of the same type. In our case, since we're using a
DictReader, our various functions must work with an iterable over
dicts which yields dicts.

In order to merge, the input must be sorted. Here's our composable
sort.

::

    def key_sort( source, key='key' ):
        def get_key( x ):
           return int(x[key])
        for row in sorted(source, key=get_key ):
           yield row

Yes, we need to pre-process the keys, they're not simple text;
they're numbers.

Composable 2-File Merge
-----------------------

The composable merge has a similar outline. It's a loop over the
inputs and it yields outputs of the same type.

::

      def merge( f1, f2, key='key' ):
          """Merge two sequences of row dictionaries on a key column."""
          r1, r2 = None, None
          try:
              r1= f1.next()
              r2= f2.next()
              while True:
                  if r1[key] == r2[key]:
                      r1.update(r2)
                      yield r1
                      r1, r2 = None, None
                      r1= f1.next()
                      r2= f2.next()
                  elif r1[key] < r2[key]:
                      yield r1
                      r1= None
                      r1= f1.next()
                  elif r1[key] > r2[key]:
                      yield r2
                      r2= None
                      r2= f2.next()
                  else:
                      raise Exception # Yes, this is impossible
          except StopIteration:
              pass
          if r1 is not None:
              yield r1
              for r1 in f1:
                 yield r1
          elif r2 is not None:
              yield r2
              for r2 in f2:
                  yield r2
          else:
              pass # Exhausted with an exact match.

This runs in 214 seconds. Not a big improvement in time. However, the
improvement in flexibility is outstanding. And the elegant simplicity
is delightful. Having the multi-way state managed entirely through
the Generator Function/Iterator abstraction is amazing.

Also, this demonstrates that the bulk of the time is spent reading
the zipped CSV files and writing the final CSV output file. The
actual merge algorithm doesn't dominate the complexity.



-----

Python 2.6 includes ``heapq.merge(*iterables)`` than d...
----------------------------------------------------------

Unknown<noreply@blogger.com>

2010-05-07 17:47:14.333000-04:00

Python 2.6 includes ``heapq.merge(*iterables)`` than does an N-way merge.
For earlier versions you can use the recipe at
http://code.activestate.com/recipes/491285-iterator-merge/


Utilize technology to the point that will help wit...
-----------------------------------------------------

protein powder<noreply@blogger.com>

2010-06-18 06:39:28.642000-04:00

Utilize technology to the point that will help with all aspects of your
business and you’ll see very quickly how beneficial it can be for you.


While some project managers prefer to have each te...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-06-16 06:50:30.552000-04:00

While some project managers prefer to have each team leader present the
status of the recent work, many insist on having the project coordinator
present the status since they will be unbiased. As a result, true
project problems will be surfaced in the project status review meetings.
It will then be up to the project manager, and the “problem owner” to
work out a corrective action plan.


The Program (Investment) Life Cycle integrates the...
-----------------------------------------------------

protein powder<noreply@blogger.com>

2010-06-15 07:23:21.969000-04:00

The Program (Investment) Life Cycle integrates the project management
and system development life cycles with the activities directly
associated with system deployment and operation. By design, system
operation management and related activities occur after the project is
complete and are not documented within this guide.
`Project Management Software <http://www.project-drive.net/>`__





