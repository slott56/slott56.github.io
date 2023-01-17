Map-Reduce, Python and Named Tuples
===================================

:date: 2010-01-25 07:44
:tags: map-reduce,#python
:slug: 2010_01_25-map_reduce_python_and_named_tuples
:category: Technologies
:status: published

A year and change back, I wrote this on "`Exploratory
Programming <http://homepage.mac.com/s_lott/iblog/architecture/C551260341/E20081005191603/index.html>`__".

It turns out that it was a mistake. While the subclass-expansion
technique is a cool way to bang out a program incrementally, in the
long run, the subclassing is ill-advised.

The more I look at Python generator functions and the idea of using
Map-Reduce, the more I realize that Visitors and Subclass Extension
are not the best design pattern. The same kind of exploration can be
done with map-reduce techniques, and the resulting application is
slightly simpler.

Design Coupling
---------------

The problem with design-by-subclass is that the map and reduce
operations are often defined relatively informally. After all,
they're just method invocations within the same class. You can,
unthinkingly, create obscure dependencies and assumptions. This can
make the Visitor rather complex or make subclass features hard to
refactor into the Visitor.

As a concrete example, we have an application that processes
directories of files and file archives (ZIP and TAR) of workbooks
with multiple sheets. All of this nesting merely wraps a source of
spreadsheet rows. This should be a collection of simple nested map
operations to transform directories, files, archives of files, etc.,
into a spreadsheet row source.

Part way through our class hierarchy, however, a subclass introduced
a stateful object that other method functions could use. However,
when we tried to refactor things into a simple Visitor to visit all
of the workbooks (ignoring all the directory, archive and file
structure), we worked around the hidden stateful object without
realizing it.

Named Tuples and Immutability
-----------------------------

A much cleaner solution is to make use of Python's
`namedtuple <http://docs.python.org/dev/library/collections.html#collections.namedtuple>`__
constructor and write generator functions which map one kind of
namedtuple to another kind of namedtuple. This has the advantage that
-- unless you've done something really bad -- you should be able to
pickle and unpickle each tuple, easily seeding a multi-processing
pipeline. Maximal concurrency, minimal work.

Each stage in a map-reduce pipeline can have the following form.

::

    SomeResult = namedtuple('SomeResult',['a','b','c'])
    for x in someSource():
        assert isinstance( x, SomeSource )
        yield SomeResult( some transformation of x )

The assertion should be obvious from inspection of the someSource
function. It's provided here because it's essential to creating
map-reduce pipelines that work. It's better to prove that the
assertion true through code inspection and comment out the assert
statement.

Pipelining
----------

What pops out of this are stateless objects. Since named tuples are
immutable, it appears that we've done some purely functional
programming without really breaking a sweat.

Further, we can see our way toward encapsulating a generator function
and it's resulting namedtuple as a single MapReduce object. The
assertion can then be plucked out of the loop and refactored into a
pipeline manager.

This might give us several benefits.

#.  A way to specify a pipeline as a connected series of generator
    functions. E.g., Pipeline( generator_1, map_2, map_3, reduce_4 ).

#.  Inspection of the pipeline to be sure that constraints will be
    met. The head of the pipeline has a resulting type, all other
    stages have an required source type and a result type. Since
    they're named tuples we only care that the required attributes are
    a subset of the previous stage's result attributes.

#.  Implementation through injection of a pickle/unpickle wrapper
    around each stage.

#.  Distribution through a "runner" that forks a subprocess pipeline.
    This should yield map-reduce operations that swamp the OS by
    having multiple concurrent stages.

Goals
-----

Generally, our goal is to get the CPU 100% committed to the right
task. Either 100% doing web services, or 100% doing database
queries or 100% doing batch processing of massive flat-file
datasets.

Currently, we can't get much past 66%: one core is close to 100%,
but the other is only lightly involved. By growing to
multi-processing, we should be able to red-line a processor with
any number of cores.





