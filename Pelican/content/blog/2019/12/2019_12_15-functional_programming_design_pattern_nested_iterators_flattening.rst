Functional programming design pattern: Nested Iterators == Flattening
=====================================================================

:date: 2019-12-15 10:29
:tags: #python,functional programming
:slug: 2019_12_15-functional_programming_design_pattern_nested_iterators_flattening
:category: Technologies
:status: published


Here's a functional programming design pattern I uncovered. This may
not be news to you, but it was a surprise to me. It cropped up when
looking at something that needs parallelization to reduced the
elapsed run time.

Consider this data collection process.


::

         for h in some_high_level_collection(arg1):
             for l in h.some_low_level_collection(arg2):
                 if some_filter(l):
                     logger.info("Processing %s %s", h, l)
                     some_function(h, l)

      

This is pretty common in devops world. You might be looking at
all repositories in all github organizations. You might be
looking at all keys in all AWS S3 buckets under a specific
account. You might be looking at all tables owned by all
schemas in a database.



It's helpful -- for the moment -- to stay away from taller tree
structures like the file system. Traversing the file system
involves recursion, and the pattern is slightly different
there. We'll get to it, but what made this clear to me was a
"simpler" walk through a two-layer hierarchy.



The nested for-statements aren't really ideal. We can't apply
any itertools techniques here. We can't trivially change this
to a multiprocessing.map().



In fact, the more we look at this, the worse it is.
Here's something that's a little easier to work with:


      
::

            def h_l_iter(arg1, arg2):
                for h in some_high_level_collection(arg1):
                    for l in h.some_low_level_collection(arg2):
                        if some_filter(l):
                            logger.info("Processing %s %s", h, l)
                            yield h, l

      
::

            itertools.starmap(some_function, h_l_iter(arg1, arg2))


The data gathering has expanded to a few more lines of code. It
gained a lot of flexibility. Once we have something that can be used
with starmap, it can also be used with other itertools functions to
do additional processing steps without breaking the loops into
horrible pieces.

I think the pattern here is a kind of "Flattened Map" transformation.
The initial design, with nested loops wrapping a process wasn't a
good plan. A better plan is to think of the nested loops as a way to
flatten the two tiers of the hierarchy into a single iterator. Then a
mapping can be applied to process each item from that flat iterator.

Extracting the Filter
---------------------

We can now tease apart the nested loops to expose the filter. In the
version above, the body of the h_l_iter() function binds log-writing
with the yield. If we take those two apart, we gain the flexibility
of being able to change the filter (or the logging) without an
awfully complex rewrite.


::

      T = TypeVar('T')
      def logging_iter(source: Iterable[T]) -> Iterator[T]:
          for item in source:
              logger.info("Processing %s", item)
              yield item

      def h_l_iter(arg1, arg2):
          for h in some_high_level_collection(arg1):
              for l in h.some_low_level_collection(arg2):
                  yield h, l

      raw_data = h_l_iter(arg1, arg2)
      filtered_subset = logging_iter(filter(some_filter, raw_data))
      itertools.starmap(some_function, filtered_subset)


Yes, this is still longer, but all of the details are now exposed
in a way that lets me change filters without further breakage.
Now, I can introduce various forms of multiprocessing to improve
concurrency.

This transformed a hard-wired set of nest loops, if, and function
evaluation into a "Flattener" that can be combined with off-the
shelf filtering and mapping functions.

I've snuck in a kind of "tee" operation that writes an iterable
sequence to a log. This can be injected at any point in the
processing.

Logging the entire "item" value isn't really a great idea. Another
mapping is required to create sensible log messages from each
item. I've left that out to keep this exposition more focused.


I'm sure others have seen this pattern, but it was eye-opening to
me.

Full Flattening
---------------

The h_l_iter() function is actually a generator expression. A
function isn't needed.

::

         h_l_iter = (
             (h, l) 
             for h in some_high_level_collection(arg1) 
                 for l in h.some_low_level_collection(arg2)
         )

This simplification doesn't add much value, but it seems to be
general truth. In Python, it's a small change in syntax and
therefore, an easy optimization to make.

   
What About The File System?
---------------------------


When we're working with some a more deeply-nested structure, like
the File System, we'll make a small change. We'll replace the
h_l_iter() function with a recursive_walk() function.


::

      def recursive_walk(path: Path) -> Iterator[Path]:
          for item in path.glob():
              if item.is_file():
                  yield item
              elif item.is_dir():
                  yield from recursive_walk(item)

   
This function has, effectively the same signature as h_l_iter().
It walks a complex structure yielding a flat sequence of items.
The other functions used for filtering, logging, and processing
don't change, allowing us to build new features from various
combinations of these functions.

tl;dr
-----

The too-long version of this is:
      
         **Replace** ``for item in iter: process(item)``

         **with** ``map(process, iter)``

This pattern works for simple, flat items, nested structures, and
even recursively-defined trees. It introduces flexibility with no
real cost.

The other pattern in play is:

      
    **Any** ``for item in iter: for sub-item in item:``
    **processing is "flattening" a hierarchy into a sequence.**

    **Replace it with**
         ``(sub-item for item in iter for sub-item in item)``

These felt like blinding revelations to me.



-----

Having just been exposed to FP and wanting to impl...
-----------------------------------------------------

Fanchen Bao<noreply@blogger.com>

2019-12-06 17:53:21.676000-05:00

Having just been exposed to FP and wanting to implement FP in Python,
this post definitely resonates with me. Will definitely check out your
Functional Python Programming book. Thanks.


Nice breakdown :-)

One small typo under Extractin...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2019-12-11 12:50:58.834000-05:00

Nice breakdown :-)
One small typo under Extracting the Filter:
\`Iteratble[T]\` should be \`Iterable[T]\`


Great examples, thanks a lot
----------------------------

Unknown<noreply@blogger.com>

2019-12-11 12:52:39.138000-05:00

Great examples, thanks a lot





