Stingray 4.4 Update -- the Posix split command applied to COBOL files
=====================================================================

:date: 2014-05-29 08:00
:tags: #python,RECFM,EBCDIC,COBOL,mastering object-oriented python
:slug: 2014_05_29-stingray_44_update_the_posix_split_command_applied_to_cobol_files
:category: Technologies
:status: published

Here's an interesting problem. Implement the
`split <http://man7.org/linux/man-pages/man1/split.1.html>`__ command
for mainframe COBOL EBCDIC files with their BDW and RDW headers.

The conventional **split** can't handle COBOL EBCDIC files because
they don't have sensible \\n line breaks. Translating an EBCDIC file
to ASCII is high-risk because COMP and COMP-3 fields will be trashed
by the translation.

If the files include Occurs Depending On, then the FTP transfer
**should** include the RDW/BDW headers. The SITE RDW (or LOCSITE RDW)
are essential. It's much faster to include this overhead. Stingray
can process files without the headers, but it's slower.

There are two essential Python techniques for building file splitters
than involve parsing.

-  The itertools.groupby() function.

-  The **with** statement.

Along with this, we need an iterator over the underlying records.
For example, the stingray.cobol.RECFM subclasses will parse the
various mainframe RECFM options and iterate over records or
records+RDW headers or blocks (BDW headers plus records with RDW
headers.

The itertools.groupby() function can break a record iterator into
groups based on some group-by criteria. We can use this to break into
sequential batches.

::

    itertools.groupby( enumerate(reader), lambda x: x[0]//batch_size )

This expression will break the iterable, reader, into groups each of
which has a size of batch_size records. The last group will have
total%batch_size records.

The with statement allows us to make each individual group into a
separate context. This assures that each file is properly opened and
closed no matter what kinds of exceptions are raised.

Here's a typical script.

::

   import itertools
   import stringray.cobol
   import collections
   import pprint

   batch_size= 1000
   counts= collections.defaultdict(int)
   with open( "some_file.schema", "rb" ) as source:
       reader= stringray.cobol.RECFM_VB( source ).bdw_iter()
       batches= itertools.groupby(enumerate(reader), lambda x: x[0]//batch_size):
       for group, group_iter in batches:
           with open( "some_file_{0}.schema".format(group), "wb" ) as target:
           for id, row in group_iter:
               target.write( row )
               counts['rows'] += 1
               counts[str(group)] += 1
   pprint.pprint( dict(counts) )


There are several possible variations on the construction of the
reader object.

-  cobol.RECFM_F( source ).record_iter() -- result is RECFM_F.

-  cobol.RECFM_F( source ).rdw_iter() -- result is RECFM_V; RDW's have been added.

-  cobol.RECFM_V( source ).rdw_iter() -- result is RECFM_V; RDW's have been preserved.

-  cobol.RECFM_VB( source ).rdw_iter() -- result is RECFM_V; RDW's have been preserved; BDW's have been discarded.

-  cobol.RECFM_VB( source ).bdw_iter() -- result is RECFM_VB; BDW's and RDW's have been preserved. The batch size is the number of blocks, not the number of records.

This should allow slicing up a massive mainframe file into pieces for
parallel processing.





