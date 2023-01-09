Python 3.2 CSV Module -- Very, very nice
========================================

:date: 2012-01-17 08:00
:tags: csv,#python
:slug: 2012_01_17-python_32_csv_module_very_very_nice
:category: Technologies
:status: published


A common (and small) task is reformatting a file that's in some
variant of CSV.  It could be a SQL database extract, or an export from
an application that works well with CSV files.

In Python 2.x, a CSV file with Unicode was a bit of a problem.  The
CSV module isn't happy with Unicode.  The documentation is quite clear
that many files need to be opened with a mode of 'rb' to correctly
handle Windows line-endings.

Because of this, a CSV file with Unicode required using an explicit
decoder on the individual columns (not the line as a whole!)

But with Python 3.2, that's all behind us.

Here's something I did recently.  The file has six columns that are
relevant.  One of them (the "NOTE") column has a big block of text
with details buried inside using a kind of RST markup.  The data might
be three lines with a value like this "words words\\n:budget:
1500\\nwords words".

The file is UTF-8, and the words have non-ASCII unicode characters
randomly through it.

::

    def details( source ):
       relevant = ( "TASK", "FOLDER", "CONTEXT", "PRIORITY", "STAR", )
       parse= "NOTE"
       data_pat= re.compile( r"^:(\w+):\s*(.*)\s*$" )
       rdr= csv.DictReader( source )
       for row in rdr:
           txt= row[parse]
           lines= ( data_pat.match(l) for l in txt.splitlines() )
           matches= ( m.groups() for m in lines if m )
           result= dict( (k, row[k]) for k in relevant)
           result.update( dict(matches) )
           yield result



How much do I love Python? Let me count the ways.

#.  The assignment of *lines* on line 8 was fun.  The "NOTE" column, in
    row[parse], contains the extra fields.  They'll be on a separate line
    with the :word:value format as shown in the *data_pat* pattern.  We
    create a generator which will split the text field into lines and
    apply the pattern to each line.

#.  The assignment to  *matches* on line 9 was equally fun.  If the
    ``matches`` generator produced a match object, the *lines* generator
    will gather the two groups form the line.

#.  The assignment to *result* creates a dictionary from the relevant
    columns.

#.  The second assignment to *result* updates this dictionary with data
    parsed out of the "NOTE" column.

That makes it quite pleasant (and fast) to process an extract file,
reformatting a "big blob of text" into individual columns.

The rest of the app boils down to this.

::

    def rewrite( input, target=sys.stdout ):
       with io.open(input, 'r', encoding='UTF-8') as source:
           data= list( details( source ) )
       headers= set( k for row in data for k in row  )
       wtr= csv.DictWriter( target, sorted(headers) )
       wtr.writeheader( )
       wtr.writerows( data )



This gathers the raw data into a big old sequence in memory, and then
writes that big old sequence back out to a file.  If we knew the
headers buried in the "NOTE" field, we could do the entire thing in a
single pass just using generators.

We have to explicitly provide the encoding because the file was
created via a download and the encoding isn't properly set on the
client machine.  The important thing is that we *can* do this when
it's necessary.  And we no longer have to explicitly decode fields.

Since we don't know the headers in the "NOTE" field, we're forced to
create the *headers* set by examining each row dictionary for it's
keys.



-----

csvkit is designed to augment or supercede much of...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-01-17 19:29:33.971000-05:00

csvkit is designed to augment or supercede much of Python’s csv module
url: http://csvkit.readthedocs.org/en/latest/index.html

