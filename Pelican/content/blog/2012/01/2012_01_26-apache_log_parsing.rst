Apache Log Parsing
==================

:date: 2012-01-26 08:00
:tags: #python,functional programming,Apache,analysis
:slug: 2012_01_26-apache_log_parsing
:category: Technologies
:status: published

How much do I love Python?  Consider this little snippet that parses
Apache logs.

::

    import re
    from collections import defaultdict, named tuple

    format_pat= re.compile(
       r"(?P<host>[\d\.]+)\s"
       r"(?P<identity>\S*)\s"
       r"(?P<user>\S*)\s"
       r"\[(?P<time>.*?)\]\s"
       r'"(?P<request>.*?)"\s'
       r"(?P<status>\d+)\s"
       r"(?P<bytes>\S*)\s"
       r'"(?P<referer>.*?)"\s' # [SIC]
       r'"(?P<user_agent>.*?)"\s*'
    )

    Access = namedtuple('Access',
       ['host', 'identity', 'user', 'time', 'request',
       'status', 'bytes', 'referer', 'user_agent'] )

    def access_iter( source_iter ):
       for log in source_iter:
           for line in (l.rstrip() for l in log):
               match= format_pat.match(line)
               if match:
                   yield Access( **match.groupdict() )


That's about it.  The access log rows are now first-class Access-class
objects that can be processed pleasantly by high-level Python
applications.

Cool things.

#.  The adjacent string concatenation means that the regular expression
    can be broken up into bits to make it readable.

#.  When the named tuple attributes match the regular expression names,
    we can trivially turn the match.groupdict() into a named tuple.

#.  By using a generator, the other parts of the application can simply
    loop through the results without tying up memory to create vast
    intermediate structures.

A couple of years back, a sysadmin was trying to justify spending
money on a log analyzer product.  I suggested they (at the very
least) get an open source log analyzer.

I also suggested that they learn Python and save themselves the pain
of working with a (potentially) complex tool.  Given this as a common
library module, log analysis applications are remarkably easy to
write.



-----

Nice code. But what about using `re.VERBOSE` flag ...
-----------------------------------------------------

Roman Haritonov<noreply@blogger.com>

2012-01-28 10:45:17.687000-05:00

Nice code. But what about using \`re.VERBOSE\` flag instead adjacent
string concatenation?


Cool, thanks very much!
-----------------------

Mandar Mitra<noreply@blogger.com>

2019-11-21 12:05:56.600000-05:00

Cool, thanks very much!





