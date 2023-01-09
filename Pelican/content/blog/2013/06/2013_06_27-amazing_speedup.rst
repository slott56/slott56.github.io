Amazing Speedup
===============

:date: 2013-06-27 10:16
:tags: performance,algorithm,#python
:slug: 2013_06_27-amazing_speedup
:category: Technologies
:status: published

A library had unit tests that ran for almost 600 seconds. Two small
changes dropped the run time to 26 seconds.


I was amazed.


Step 1. I turned on the cProfile. I added two methods to the slowest
unit test module.

::

  def profile():
      import cProfile
      cProfile.run( 'main()', 'the_slow_module.prof' )
      report()

  def report():
      import pstats
      p = pstats.Stats( 'the_slow_module.prof' )
      p.sort_stats('time').print_callees(24)


Now I can add profiling or simply review the report. Looking at the
"callees" provided some hints as to why a particular method was so
slow.


Step 2. I replaced ElementTree with cElementTree (duh.) Everyone
*should* know this. I didn't realize how much this mattered. The
trick is to note how much time was spent doing XML parsing. In the
case of this unit test suite, it was a LOT of time. In the case of
the overall application that uses this library, that won't be true.


Step 3. The slowest method was assembling a list. It did a lot of
list.append(), and list.__len__(). It looked approximately like the
following.

::

    def something( self ):
      result= []
      for index, value in some_source:
          while len(result)+1 != index:
              result.append( None )
          result.append( SomeClass( value ) )
      return result


This is easily replaced by a generator. The API changes, so every use
of this method function may need to be modified to use the generator
instead of the list object.

::

    def something_iter( self ):
       counter= 0
       for index, value in some_source:
           while counter+1 != index:
               yield None
               counter += 1
           yield SomeClass( value )
           counter += 1


The generator was significantly faster than list assembly.


Two minor code changes and a significant speed-up.




-----

Interesting.  You may consider just using a list c...
-----------------------------------------------------

Kurt Rose<noreply@blogger.com>

2010-12-29 13:10:57.074000-05:00

Interesting. You may consider just using a list comprehension or
generator expression as well for that second piece:

::

    [ [None]*index + [SomeClass(value)] for index,value in source ]
    itertools.chain.from_iterable( ( itertools.chain( itertools.repeat(None,
    index), [SomeClass(value)] ) for index, value in source ) )

This arguably simplifies the code by removing the explicit "counter"
variable, and the nested loop.


I take it index from some_source must be increasin...
-----------------------------------------------------

Fred<noreply@blogger.com>

2010-12-29 16:36:17.569000-05:00

I take it index from some_source must be increasing and start at least
with 1? (The latter because starting at zero, which seems more natural
for a general index, results in an infinite loop: counter + 1 will never
equal 0. Was this an error in simplifying for the blog?)

@Kurt: You can't eliminate counter as in either of those, as the number
of Nones depends on the difference between successive indexes, not on
index alone. Your code gives a different result.

And realizing the importance is the difference between successive
indexes leads me to write (how to format code for blogspot?):
def something_iter():

::

..cur_index = 1 # instead of 0 for reason above
..for next_index, value in some_source:
....for \_ in xrange(cur_index, next_index):
......yield None
....cur_index = next_index
....yield SomeClass(value)

I don't consider this any significant improvement over the while loop
version, but I think it would help prevent misunderstandings similar to
Kurt's.


The index is 1-based.  It&#39;s the column number ...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2010-12-29 17:29:38.903000-05:00

The index is 1-based. It's the column number from reading Excel
spreadsheets.




Oh, I see. The data is the index and value from a ...
-----------------------------------------------------

Kurt Rose<noreply@blogger.com>

2010-12-29 18:41:11.579000-05:00

Oh, I see. The data is the index and value from a column, and the code
is to fill in the "missing" numbers with Nones?

A defaultdict may be perfect for this. Since source is already in the
form of a series of a list of (index, value) tuples, we can just pass
this straight to the constructor.

::

    >>> source = [ (1, 'a'), (5, 'b') ]
    >>> import collections
    >>> data = collections.defaultdict(lambda: None, source)

(add a list comprehension to call SomeClass constructor:
collections.defaultdict(lambda: None, [(k, SomeClass(v)) for k,v in
source])
Then your code can just treat data as if it were a list for indexing.

::

    >>> data[1]
    'a'
    >>> data[2]
    >>> data[3]
    >>> data[4]
    >>> data[5]
    'b'

If you want to make it into a real list (for slicing, etc) you can do
this with a simple comprehension:

::

    >>> datalist = [data[a] for a in xrange(max(data.keys())+1)]
    >>> datalist
    [None, 'a', None, None, None, 'b']

You could also replace this with a generator expression if you wanted to
save memory I guess, but you may as well leave it as a defaultdict in
that case.





