Enriched Details of Apache Common Log Format
============================================

:date: 2012-01-31 22:25
:tags: #python,functional programming,Apache,analysis
:slug: 2012_01_31-enriched_details_of_apache_common_log_format
:category: Technologies
:status: published

See `Apache Log Parsing <{filename}/blog/2012/01/2012_01_26-apache_log_parsing.rst>`__
for the background.

Here's a generator function which expands a simple Access to be a more
detailed named tuple.

::

   Access_Details= namedtuple( 'Access_Details',
       ['access', 'time', 'method', 'url', 'protocol'] )
               
   def details_iter( iterable ):
       def parse_time_linux( ts ):
           return datetime.datetime.strptime( ts, "%d/%b/%Y:%H:%M:%S %z" )

       def parse_time_macos( ts ):
           dt= datetime.datetime.strptime( ts[:-6], "%d/%b/%Y:%H:%M:%S" )
           tz_text= ts[-6:]
           sign, hh, mm = tz_text[:1], int(tz_text[1:3]), int(tz_text[3:])
           minutes= (hh*60+mm) * (-1 if sign == '-' else +1)
           offset = datetime.timedelta(minutes = minutes)
           tz= datetime.timezone( offset, tz_text )
           return dt.replace(tzinfo=tz)
           return dt

       first, last = None, None
       for access in iterable:
           meth, uri, protocol = access.request.split()
           dt= parse_time_macos( access.time )
           first= min(dt,first) if first else dt
           last= max(dt,last) if last else dt
           yield Access_Details(
               access= access,
               time= dt,
               method= meth,
               url= urllib.parse.urlparse(uri),
               protocol= protocol )

       print( "Log Data from", first, "to", last, 'duration', last-first )


This "wraps" the original Access object with an Access_Details that
includes information that isn't trivially parsed from the access row.

-   The datetime object with the real timestamp.  Not the Mac OS
    subtlety.  Due to platform issues, the %z strptime format doesn't
    seem to work in Python 3.2

-   The three fields from the request: method, URL and protocol.

-   The URL is parsed into its individual fields.


Note that the ``Access_Details`` object is pickle-able.  While seemingly
irrelevant, it turns out that having something which can be pickled
means that we can use multiprocessing to create a multi-staged
concurrent pipeline of log analysis.

What's important here is that we're adding functionality without
redefining the underlying Access class. Indeed, the underlying Access
object is immutable.  The idea of stateless values comes from the
functional programming crowd.  It seems to work out really well
because the functionality seems to accrete in relatively simple
layers.





