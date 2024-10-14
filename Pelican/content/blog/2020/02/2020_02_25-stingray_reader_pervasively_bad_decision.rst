Stingray Reader Pervasively Bad Decision
========================================

:date: 2020-02-25 08:00
:tags: stingray reader,Design Principles,object-oriented design,type hints
:slug: 2020_02_25-stingray_reader_pervasively_bad_decision
:category: Technologies
:status: published


I made some bad decisions when I wrote this a few years
ago: https://github.com/slott56/Stingray-Reader. Really bad. And.
Recently, I've burdened myself with conflicting goals. Ugh.

I need to upgrade to Python 3.8, and add type hints. This exposed
somes badness.

See `Stingray Reader Rewrite <{filename/blog/2020/01/2020_01_31-stingray_reader_rewrite.rst>`_ for some status.

The very first version(s) of this were expeditious solutions to some
separate-but-related problems. Spreadsheet processing was an important
thing for me f. Fixed-format file versions of spreadsheets showed up
once in a while mixed with XLS and CSV files. Separately, COBOL code
analysis was a thing I'd been involved in going back to the turn of
the century.

The two overlap. A lot.

The first working versions of apps to process COBOL data in Python
relied on a somewhat-stateful representation of the COBOL DDE (Data
Definition Element.) The structure had to be visited more than once to
figure out size, offset, and dimensionality. We'll talk about this
some more.

A slightly more clever algorithm would leverage the essential parsing
as a kind of tree walk, pushing details down into children and
summarizing up into the parent when the level number changed. It
didn't seem necessary at the time.

Today
-----


I've been working for almost three weeks on trying to disentangle the
original DDE's from the newer schema. I've been trying to invert the
relationships so a DDE exists independently of a schema attribute.
This means some copy-and-paste of data between the DDE source and the
more desirable and general schema definition.

It turns out that some design decisions can be pervasively bad. Really
bad-foundation-wrecks-the-whole-house kind of bad.

At this point, I **think** I've teased apart the root cause problem.
(Of course, you never know until you have things fixed.)

For the most part, this is a hierarchical schema. It's modeled nicely
by JSONSchema or XSD. However. There are two additional, huge problems
to solve.

**REDEFINES**. The first huge problem is a COBOL definition can
redefine another field. I'm not sure about the directionality of the
reference. I know many languages require things be presented in
dependency order: a base definition is provided  lexically first and
all redefinitions are subsequent to it. Rather than depend on order of
presentation, it seems a little easier to make a "reference
resolution" pass. This plugs in useful references from items to the
things they redefine, irrespective of any lexical ordering of the
definitions.

This means we data can only be processed strictly lazily. A given
block of bytes may have multiple, conflicting interpretations. It is,
in a way, a free union of types. In some cases, it's a discriminated
union, but the discriminating value is not a formal part of the
specification. It's part of the legacy COBOL code.

**OCCURS DEPENDING ON**. The second huge problem is the number of
elements in an array can depend on another field in the current
record. In the common happy-path cases, occurrences are fixed. Having
fixed occurrences means sizes and offsets can be computed as soon as
the REDEFINES are sorted out.

Having occurrences depending on data means sizes and offsets cannot be
computed until some data is present. The most general case, then,
means settings sizes and offsets uniquely for each row of data.

Current Release
----------------

The current release (4.5) handles the ODO, size, and offset
computation via a stateful DDE object.

Yes. You read that right. There are stateful values in the DDE. The
values are adjusted on a row-by-row basis.

Tomorrow
--------


There's got to be a better way.

Part of the problem has been conflicting goals.

-  Minimal tweaks required to introduce type hints.

-  Minimal tweaks to break the way a generic schema depended on the DDE
   implementation. This had to be inverted to make the DDE and generic
   schema independent.


The **minimal tweaks** idea is really bad. Really bad.


The intent was to absolutely prevent breaking the demo programs. I
may still be able to achieve this, but... There needs to be a clean
line between the exposed work-book like functionality, and some
behind the scenes COBOL DDE processing.


I now think it's essential to gut two things:


#.  Building a schema from the DDE. This is a (relatively) simple
    transformation from the COBOL-friendly source model to a generic,
    internal model that's compatible with JSONSchema or XSD. The
    simple attributes useful for workbooks require some additional
    details for dimensionality introduced by COBOL.

#.  Navigating to the input file bytes and creating Workbook Cell
    objects in a way that fits with the rest of the Workbook
    abstraction.


The happy path for Cell processing is more-or-less by attribute
name: row.get('attribute').  This changes in the presence of COBOL
OCCURS clause items. We have to add an index.
row.get('ARRAY-ITEM', index=2) is the Python version of COBOL's
ARRAY-ITEM(3).


The COBOL variable names \*could\* be mapped to Python names, and we
\*could\* overload \__getitem__() so that row.array_item[3] could be
valid Python to fetch a value.


But nope. COBOL has 1-based indexing, and I'm not going to hide that.
COBOL has a global current instance of the row, and I'm not going to
work with globals.


So. Where do I stand?


I'm about to start gutting. Some of the DDE size-and-offset (for a
static occurrences)





