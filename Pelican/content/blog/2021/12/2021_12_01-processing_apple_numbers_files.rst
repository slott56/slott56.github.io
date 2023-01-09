Processing Apple Numbers Files
==============================

:date: 2021-12-01 07:00
:tags: open source,#python,workbook,spreadsheet,jsonschema
:slug: 2021_12_01-processing_apple_numbers_files
:category: Technologies
:status: published

Apple's freebie tools -- Pages, Numbers, Keynote, Garage Band, etc. --
are wonderful things. I really like Numbers. I'm tolerant of Pages. I've
used Pages to write books and publish them to the Apple Bookstore.
(Shameless Plug: `Pivot to
Python <https://books.apple.com/us/book/id1586977675>`__.)

These tools have a significant problem. Protobuf.

Some History
------------

Once upon a time, Numbers used an XML-based format. This was back in
'09, I think. At some point, version 10 of Numbers (2013?) switched to
Protobuf.

I had already unwound XLSX and ODS files, which are XML. I had also
unwound Numbers '09 in XML. I had a sense of what a spreadsheet needed
to look like.

The switch to Protobuf also meant using Snappy compression. Back in
2014? I worked out my own version of the Snappy decompression algorithm
in pure Python. I think I knew about
`python-snappy <https://github.com/andrix/python-snappy>`__ but didn't
want the complex binary dependency. I wrote my own instead.

I found the
`iWorkFileFormat <https://github.com/obriensp/iWorkFileFormat>`__
project. From this, and a lot of prior knowledge about the XML formats,
I worked out a way to unpack the protobuf bytes into Python objects. I
didn't leverage the formal protobuf definitions; instead I lazily mapped
the objects to a dictionary of keys and bytes. If a field had a complex
internal structure, I parsed the subset of bytes.

(I vaguely recall the Protobuf definitions are in XCode somewhere. But.
I didn't want to write a protobuf compiler to make a pure-Python
implementation. See the
`protobuf <https://github.com/eigenein/protobuf>`__ project for what I
was looking for, but didn't have at the time.)

Which brings us to today's discovery.

State of the Art
----------------

Someone has taken the steps necessary to properly unpack Numbers files.
See `numbers-parser <https://github.com/masaccio/numbers-parser>`__.
This has first-class snappy and protobuf processing. It installs
cleanly. It has an issue, and I may try to work on it.

I'm rewriting my own Stingray Reader with intent to dispose of my own
XLSX, ODS, and Numbers processing. These can (and should) be imported
separately. It's a huge simplification to stand on the shoulders of
giants and write a dumb **Facade** over their work.

Ideally, all the various spreadsheet parsing folks would adopt some kind
of standard API. This could be analogous to the database API used by SQL
processing in Python. The folks with https://www.excelpython.org
or http://www.python-excel.org might be a place to start, since they
list a number of packages.

The bonus part? Seeing my name in the `Credits for
numbers-parser <https://github.com/masaccio/numbers-parser#credits>`__.
That was delightful.

At some point, I need to make a coherent pitch for a common API with
permits external JSON Schema as part of extracting data from
spreadsheets.

First. I need to get Stingray Reader into a more final form.





