Spreadsheets, COBOL, and Schema-Driven File Processing
======================================================

:date: 2021-08-24 09:00
:tags: #python,stingray reader,EBCDIC,COBOL
:slug: 2021_08_24-spreadsheets_cobol_and_schema_driven_file_processing
:category: Technologies
:status: published

I need to rewrite `Stingray
Reader <https://github.com/slott56/Stingray-Reader>`__. This project
handles a certain amount of file processing using a schema to assure the
Logical Layout is understood.  It handles several common Physical
Formats:

-  CSV files where the format is extended by the various dialects
   options.
-  COBOL files in ASCII or EBCDIC.

The project's code can be applied to text files where a regular
expression can yield a row-level dictionary object. Web server log
files, for example, are in first normal form, but have irregular
punctuation that CSV can't handle.

It can also be applied to NDJSON files (see http://ndjson.org
or https://jsonlines.org) without too much work. This also means it can
be applied to YAML files. I suspect it can also be applied to TOML files
as a distinct physical format.

The complication in the Singran Reader is that COBOL files aren't really
in first normal form. They can have repeating groups of fields that CSV
files don't (generally) have. And the initial data model in the project
wasn't really up to handling this cleanly. The repeating group logic was
patched in.

Further complicating this particular project was the history of its
evolution. It started as a way to grub through hellishly complex CSV
files. You know, the files where there are no headings, or the headings
are 8 lines long, or the files where there are a lot of lines before the
proper headings for the data. It handled all of those
not-first-normal-form issues that arise in CSV world.

I didn't (initially) understand JSON Schema (https://json-schema.org)
and did not leverage it properly as an intermediate representation for
CSV as well as COBOL layouts. It arose as a kind of after-thought. There
are a lot of todo's related to applying JSON Schema to the problem.

Recently, I learned about Lowrance USR files.
See https://github.com/slott56/navtools in general
and https://github.com/slott56/navtools/blob/master/navtools/lowrance_usr.py
for details.

It turns out that the USR file **could** be described, reasonably well,
with a Stingray schema. More to the point, it **should** be describable
by a Stingray schema, and the application to extract waypoints or routes
should look a lot like a CSV reader.

Consequences
------------

There are a bunch of things I need to do.

First, and foremost, I need to unwind some of the COBOL field extraction
logic. It's a right awful mess because of the way I hacked in
``OCCURS DEPENDING ON``. The USR files also have numerous instances of
arrays with a boundary defined by other content of the file. This is a
JSON Schema Extension (not a weird COBOL special case) and I need to use
proper JSON schema extensions and attribute cross-references.

Of course, the ``OCCURS DEPENDING ON`` clauses can nest, leading to
quite complex navigation through a dynamically-sized collection of
bytes. This is not done terribly well in the current version, and
involves leaving little state reminders around to "simplify" some of the
coding.

The field extractions for COBOL apply to binary files and should be able
to leverage the Python ``struct`` module to decode individual fields. We
should be able to also extract data from USR files. The schema can be in
pure JSON or it can be in Python as an internal data structure. This is
a new feature and (in principle) can be applied to a variety of binary
files that are in (approximately) first normal form.

(It may also be sensible to extend the ``struct`` module to handle some
EBCDIC conversions: int, float, packed-decimal, numeric string, and
alphanumeric string.)

Once we can handle COBOL and USR file occurs-depending-on with some JSON
Schema extensions, we can then work on ways to convert source material
(including JSON Schema) to the internal representation of a schema.

#. CSV headers -> JSON Schema has an API that has worked in the past.
   The trivial case of first-line-is-degenerate-schema and
   schema-in-a-separate-file are pleasant. The more complex cases of
   skip-a-bunch-of-prefix-lines is a bit more complex, but isn't much of
   a rewrite. This recovers the original feature of handling CSV files
   in all their various incarnations and dialects with more formally
   defined schema. It means that CSV with type conversions can be
   handled.
#. Parse COBOL DDE  -> JSON Schema. The COBOL parser is a bit of a hacky
   mess. A better lexical scanner would simplify things slightly.
   Because the field extraction logic will be rebuilt, we'll also have
   the original feature of being able to directly decode Z/OS EBCDIC
   files in Python.

This feels ambitious because the original design was so weak.





