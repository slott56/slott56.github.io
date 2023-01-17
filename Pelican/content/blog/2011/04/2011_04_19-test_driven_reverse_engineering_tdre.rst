Test-Driven Reverse Engineering (TDRE)
======================================

:date: 2011-04-19 08:00
:tags: unit testing,#python,reverse engineering,test-driven reverse engineering
:slug: 2011_04_19-test_driven_reverse_engineering_tdre
:category: Architecture & Design
:status: published

Another case study on TDRE.

Provided: 2,938 lines of Python code which process a handful of large
files to create a number of outputs. [Details can't be disclosed.]

Objective: Refactor to distinguish between the overall sequence of
transformational steps and the details of each individual step.

Observations
------------

The code is almost purely procedural. There are 11 class definitions.
6 of these wrap built-in types with type conversion and
null-handling. 1 is a new exception. 1 is a generic "table" that
essentially duplicates features of SQLite. The remaining 3 are
actually part of the problem domain.

One reason for reverse engineering is that the code has reached an
intellectual limit. It's small, but "dense" with highly-optimized
processing steps. The `cohesion
type <http://en.wikipedia.org/wiki/Cohesion_(computer_science)#Types_of_cohesion>`__
is almost all "Temporal". Processing is grouped into successive
processing loops; each loop contains a cluster of processing steps.
Consequently, it's quite hard to tease apart the algorithm to get a
"big picture" of what's going on. It's just a dense stand of trees.
No forest.

Another reason for reverse engineering is to support the endless
adaptation and modification of the code base. The program is a kind
of "spreadsheet on steroids". This isn't a simplistic collection of
cells and formulæ that permits simple what-if analysis. This is a
more complex set of formulæ that would be challenging (but not
impossible) to implement as a spreadsheet. The use case, however, is
the spreasheet use case: think, tweak, create results, repeat.

TDRE Approach
-------------

Start with an **Initial Survey** of the legacy code base and sample
files.

**Create an Outline** or "sketch" of the domain model and main
program. This will be a modules (or a package) with comments and some
preliminary class definitions. Little more.

**Pick a processing Step** in the legacy code. This often requires
creating processing summaries of the legacy code. Most legacy code is
procedural, so the processing tends to be sequential in nature.

**Instrument the Legacy Code** with print statements to gather data.
This can be simple. The output can be challenging to interpret.

::

    with open("tdre_results_1","w") as tdre:

    # some legacy processing

    print( "Case:", foo, bar, ", Expect:", baz, file=tdre )

From the output, **Build Unit Test Cases**. Fill in parts of the
processing sequence and domain model. Debug code until the tests
pass.

Initial Survey
--------------

The **Initial Survey** locates several things.

#.  The usable, working modules. It appears that all reverse
    engineering involves a code base with dead or unused code. Even a
    small project (3,000 lines) will have a remarkable amount of dead
    code.

#.  Priorities for the implemented functionality. Not every "main"
    module is relevant.

#.  Example inputs and outputs.

If the software cannot be run (as is the case with organically
developed systems that depend on large, complex corporate
databases), then the example inputs and outputs may not actually
match the software. If the software can be run, it should be run
and the actuals compared against the samples to confirm that the
code base supplied really produced the sample outputs.

Expect that the provided legacy code is slightly different from the
code in production use. In some cases, this cannot be resolved; for
example, when the executables are older than the source. In other
cases, the code matches and no further work is required to establish
the legacy baseline.

The sample outputs point in the direction of an acceptance test case.
The sample output cannot be taken literally as the one-and-only
acceptance test. While it's desirable for reverse engineering to
reproduce the sample output, most reverse engineering will involve
enhancements or bug fixes. Expect that errors will be found (or may
be known to exist) in the sample output.

Create Outline
--------------

The outline is -- initially -- just generic MVP. There must be a
domain model, some "presenter" that has the application logic, and
some "view" for displaying the outputs.

In our case study, above, the "view" is a collection of (mostly text)
output files. The model was undefined in the legacy code, which was
all "presenter" application logic.

The goal was to extract the underlying model, break the application
"presenter" logic into two layers (forest and trees) and build some
views for each of the output files.

Pick a Processing Step
----------------------

This can be challenging, depending on the legacy code base. There are
two paths through a procedural code base.

-   Back to Front. Start with the final results and unit test the
    final steps based on previous steps that will be defined later.

-   Front to Back. Start with the first recognizable intermediate
    result based on the input files. Unit test the initial steps.

It's more rewarding to work front-to-back because progress can be
shown a little more clearly.

A better architecture can be created by working back-to-front since
dependencies are easier to understand.

Unit Test Volume, Edges and Corners
-----------------------------------

There are two unit test design challenges when doing reverse
engineering.

-   Volume. The sample data can be large. 100,000 rows of sample data
    is too many to test. Finding a "representative" subset is
    difficult. Generally, arbitrary subsets have to be used to get
    started. Once the application mostly works, more refined unit
    tests need to be created.

-   Edge and Corner Cases. While the code may be riddled with
    **if**-statements, it can still be difficult to locate sample
    inputs that exercise the various conditions in the code. It's
    risky to create data -- we have to assume that the legacy code
    does unexpected things. In many cases, print statements have to be
    put into complex if statements to locate any actual data that
    exercises that logic path.

Once the unit tests are built, this is just Test-Driven
Development (TDD).



-----

Really great post! I got some similar advice from ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-04-19 15:21:45.848000-04:00

Really great post! I got some similar advice from another developer. It
is helpful to see the process clearly explained for reference.


Helpful tools to measure windows and pipe connecti...
-----------------------------------------------------

samia87<noreply@blogger.com>

2019-04-01 02:09:36.781000-04:00

Helpful tools to measure windows and pipe connections reduce the work
involved. Automatically create and export drawings with borders and
folding marks: data can be printed without the need for further
processing. `Reverse engineering Denver,
Colorado <https://onsite3d.ca/>`__





