Extracting Data Subsets and Design By Composition
=================================================

:date: 2017-07-11 08:00
:tags: #python,functional python programming
:slug: 2017_07_11-extracting_data_subsets_and_design_by_composition
:category: Technologies
:status: published

The request was murky. It evolved over time to this:

   Create a function file_record_selection(train.csv, 2, 100,
   train_2_100.csv)

   First parameter: input file name (train.csv)

   Second parameter: first record to include (2)

   Third parameter: last record to include (100)

   Fourth parameter: output file name (train_2_100.csv)


Fundamentally, this is a bad way to think about things. I want to
cover some superficial problems first, though.


First superficial dig. It *evolved* to this. In fairness to people
without a technical background, getting to tight, implementable
requirements are is difficult. Sadly the first hand-waving garbage
was from a DBA. It *evolved* to this. The early drafts made no sense.


Second superficial whining. The specification -- as written -- is
extraordinarily shabby. This seems to be written by someone who's
never read a function definition in the Python documentation before.
Something I know is **not** the case. How can someone who is
marginally able to code also unable to write a description of a
function? In this case, the "marginally able to code" may be a hint
that some folks struggle with abstraction: the world is a lot of
unique details; patterns don't emerge from related details.


Third. Starting from record 2, seems to show that they don't get the
idea that indexes start with zero. They've seen Python. They've
written code. They've posted code to the web for comments. And they
are still baffled by the start value of indices.


Let's move on to the more interesting topic, functional composition.

Functional Composition
----------------------


The actual data file is a .GZ archive. So there's a tiny problem with
looking at .CSV extracts from the gzip. Specifically, we're exploding
a file all over the hard drive for no **real** benefit. It's often
faster to read the zipped file: it may involve fewer physical I/O
operations. The .GZ is small; the computation overhead to decompress
may be less than the time waiting for I/O.


To get to functional composition we have to start by decomposing the
problem. Then we can build the solution from the pieces. To do this,
we'll borrow the interface segregation (ISP) design principle from OO
programming.


Here's an application of ISP: Avoid Persistence. **It's easier to add
persistence than to remove it**. This leads peeling off three further
tiers of file processing: Physical Format, Logical Layout, and
Essential Entities.

We shouldn't write a .CSV file unless it's somehow required. For
example, if there are multiple clients for a subset. In this case,
the problem domain is exploratory data analysis (EDA) and saving .CSV
subsets is unlikely to be helpful. The principle still applies: don't
start with **persistence** in mind. What are the Essential Entities?
This leads away from trying to work with filenames, also. It's better
to work with files. And we shouldn't work with file names as strings,
we should use pathlib.Path. All consequences of peeling off layers
from the interfaces.


Replacing names with files means the overall function is really this.
A composition.


::

   file_record_selection = (lambda source, start, stop, target: 
       file_write(target, file_read_selection(source, start, stop))
   )


We applied the ISP again, to avoid opening a named .CSV file. We can
work with an open file-like objects, instead of a file names. This
doesn't change the overall form of the functions, but it changes the
types. Here are the two functions that are part of the composition:

::

      import typing
      Record = typing.Any
      def file_write(target: typing.TextIO, records: Iterable[Record]):
          pass
      def file_read_selection(source: csv.DictReader, start: int, stop: int) -> Iterable[Record]:
          pass

   
We've left the record type unspecified, mostly because we don't
know what it just yet. The definition of Record reflects the
Essential Entities, and we'll defer that decision until later. CSV
readers can produce either dictionaries or lists, so it's not a
complex decision; but we can defer it.

The .GZ processing defines the physical format. The content which
was zipped was a .CSV file, which defines the logical layout.
Separating physical format, logical layout, and essential entity,
gets us code like the following:

::

         with gzip.open('file.gz') as source:
             reader = csv.DictReader(source)  # Iterator[Record]
             for line in file_read_selection(reader, start, stop):
                 print(line)

We've opened the .GZ for reading. Wrapped a CSV parser around
that. Wrapped our selection filter around that. We didn't write
the CSV output because -- actually -- that's not required. The
core requirement was to examine the input.

We can, if we want, provide two variations of the file_write()
function and use a composition like the file_record_selection()
function with the write-to-a-file and print-to-the-console
variants. Pragmatically, the print-to-the-console is all we really
need.

In the above example, the Record type can be formalized
as  List[Text].  If we want to use csv.DictReader instead, then
the Record type becomes Dict[Text, Text].

Further Decomposition
---------------------

There's a further level of decomposition: the essential design
pattern is **Pagination**. In Python parlance, it's a slice
operation. We could use itertools to replace the entirety of
file_read_selection() with itertools.takewhile() and
itertools.dropwhile(). The problem with these methods is they
don't short-circuit: they read the entire file.

In this instance, it's helpful to have something like this for
paginating an iterable with a start and stop value.

::

         for n, r in enumerate(reader):
             if n < start: continue
             if n = stop: break
             yield r

This covers the bases with a short-circuit design that saves a
little bit of time when looking at the first few records of a
file. It's not great for looking at the last few records, however.

Currently, the "tail" use case doesn't seem to be relevant. If it
was, we might want to create an index of the line offsets to allow
arbitrary access. Or use a simple buffer of the required size.

If we were really ambitious, we'd use the Slice class definition
to make it easy to specify start, stop, and step values. This
would allow us to pick every 8th item from the file without too
much trouble.

The Slice class doesn't, however support selection of a randomized
subset. What we really want is a paginator like this:

::

         def paginator(iterable, start: int, stop: int, selection: Callable[[int], bool]):
             for n, r in enumerate(iterable):
                 if n < start: continue
                 if n == stop: break
                 if selection(n): yield r

         file_read_selection = lambda source, start, stop: paginator(source, start, stop, lambda n: True)

         file_read_slice = lambda source, start, stop, step: paginator(source, start, stop, lambda n: n%step == 0)

The required file_read_selection() is built from smaller pieces.
This function, in turn, is used to build file_record_selection()
via functional composition. We can use this for randomized
selection, also.

Here are functions with type hints instead of lambdas.

::

         def file_read_selection(source: csv.DictReader, start: int, stop: int) -> Iterable[Record]:
             return paginator(source, start, stop, lambda n: True)

         def file_read_slice(source: csv.DictReader, start: int, stop: int, step: int)  -> Iterable[Record]:
             return paginator(source, start, stop, lambda n: n%step == 0)

Specifying type for a generic iterable and the matching result
iterable seems to require a type variable like this:

::

         T = TypeVar('T')
         def paginator(iterable: Iterable[T], ...) -> Iterable[T]:

This type hint suggests we can make wide reuse of this function.
That's a pleasant side-effect of functional composition. Reuse can
stem from stripping away the various interface details to
decompose the problem to essential elements.

TL;DR
-----

What's essential here is Design By Composition. And decomposition
to make that possible.

We got there by stepping away from file names to file objects. We
segregated Physical Format and Logical Layout, also. Each
application of the **Interface Segregation Principle** leads to
further decomposition. We unbundled the pagination from the file
I/O. We have a number of smaller functions. The original feature
is built from a composition of functions.

Each function can be comfortably tested as a separate unit. Each
function can be reused.

Changing the features is a matter of changing the combination of
functions. This can mean adding new functions and creating new
combinations.





