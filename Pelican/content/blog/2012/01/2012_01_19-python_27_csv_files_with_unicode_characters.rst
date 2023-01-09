Python 2.7 CSV files with Unicode Characters
============================================

:date: 2012-01-19 08:00
:tags: csv,#python,unicode
:slug: 2012_01_19-python_27_csv_files_with_unicode_characters
:category: Technologies
:status: published

| The csv module in Python 2.7 is more-or-less hard-wired to work with
  ASCII and only ASCII.
| Sadly, we're often confronted with CSV files that include Unicode
  characters.  There are numerous Stack Overflow questions on this
  topic.  http://stackoverflow.com/search?q=python+csv+unicode
| What to do?  Since csv is married to seeing ASCII/bytes, we must
  explicitly decode the column values.
| One solution is to wrap csv.DictReader, something like the following.
   We need to decode each individual column before attempting to do
  anything with value.

::

   class UnicodeDictReader( object ):
       def __init__( self, *args, **kw ):
           self.encoding= kw.pop('encoding', 'mac_roman')
           self.reader= csv.DictReader( *args, **kw )
       def __iter__( self ):
           decode= codecs.getdecoder( self.encoding )
           for row in self.reader:
               t= dict( (k,decode(row[k])[0]) for k in row )
               yield t

| 
| This new object is an iterable which contains a DictReader. We could
  subclass DictReader, also.
| The use case, then, becomes something simple like this.

::

   with open("some.csv","rU") as source:
       rdr= UnicodeDictReader( source )
       for row in rdr:
           # process the row

| 
| We can now get Unicode characters from a CSV file.



-----

It&#39;s one of those things... The files came to ...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2012-01-23 11:27:19.901000-05:00

It's one of those things... The files came to me in that encoding. UTF-8
seems so much more sensible.


I like that you think &#39;mac_roman&#39; is a sen...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2012-01-20 19:56:24.488000-05:00

I like that you think 'mac_roman' is a sensible default encoding.





