Legacy Data Preservation
========================

:date: 2010-09-08 08:00
:tags: data conversion,#python
:slug: 2010_09_08-legacy_data_preservation
:category: Technologies
:status: published

Extracting legacy data can be really, really hard. However, it's of
central importance because data lives forever. Application "logic" and
"business rules" come and go.

Today's case study is a dusty old Dell Inspiron Laptop running
Windows 98 with
`Chartview <http://www.nobeltec.com/support/suppot_notice.asp>`__
software.

**Problem 1.** Chartview. No extract or export capability, except
to a GPS via a serial port. I guess I could solder up a PC serial
connector to a serial-USB interface so my Mac could read the
stream of NMEA 0183 messages that contain routes and waypoints.
But that seems complex for a one-time transfer.

**Problem 2**. Windows 98. Won't mount any USB device I own. No
solid-state disk, no rotating disk. Nothing. I have the original
install CD with all the extra drivers. Didn't help.

**Problem 3**. Dell Laptop. DVD player, floppy disk drive, and a
USB port that Windows 98 doesn't seem to know what to do with. No
ethernet, only a modem connection.

How do we preserve the waypoints and routes on this ancient Dell
so that we can replace it with a nice, new `Standard Horizon CP
300i <http://www.standardhorizon.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=84&encProdID=786FA3B62DC4B9B5DD197438F18995CD&DivisionID=3&isArchived=0>`__
and MacBook Pro running `GPSNavX <http://www.gpsnavx.com>`__?

**Raw Data**

To get the raw data, I pulled the disk drive, mounted it in an
IDE-USB enclosure and pulled the relevant routes and waypoints
files. Now we have something we can work with.

The file formats are undocumented, but the data's not complex,
making it easy to explore. Also, we can look at the old Chartview
GUI to see the data and compare it with the raw bytes on the file.

Modern software is more properly normalized, simplifying the
conversion. The legacy Chartview route data included each waypoint
-- unrelated to the master list of waypoints -- along with bearing
and range information, as well as compass deviation and projected
speed. Really. A modern GPX file as used by
`GPSNavX <http://www.gpsnavx.com/>`__ or
`iNavX <http://www.inavx.com/>`__ only needs the waypoints.
Nothing else. New software will correctly calculate range and
bearing to next waypoint as well as lookup the magnetic deviation
from standard tables. So we don't need to preserve all of the
data.

**Pass 1**

The first pass is to write simple "hex dump" utility in Python to
see what's even in the files.

Something like this seems to allow enough flexibility to get a
good view of the record sizes and field contents in the file.

::

     def hex_print( bytes, offset=0 ):
     for section in xrange(0,len(bytes)+31,32):
         block= bytes[section:section+32]
         print( '    ', ' '.join( '{0:3d}'.format(x+section) for x in xrange(32) ) )
         print( "{0:4d}".format(offset+section), ' '.join( '{0:3d}'.format(ord(x)) for x in block ) )
         print( '    ', ' '.join(  "  {0}".format(x) if 32 <= ord(x) < 128 else '   ' for x in block ) )
         print()

     def hex_dump( file, size=32 ):
     offset= 0
     with open(file,'rb') as data:
         print( '    ', ' '.join( '{0:3d}'.format(x) for x in xrange(size) ) )
         block= data.read(size)
         while block:
             hex_print( block, offset )
             block= data.read(size)
             offset += size

Once we have a sense of what's going on, we can use the Python
`struct <http://docs.python.org/library/struct.html>`__ module to
get the real data.

**Pass 2**

In the case of Chartview marks, we have a complex, but manageable
structure definition. Some of the field sizes are conjectures.
It's possible that all those filler bytes are some kind of word or
x386 paragraph alignment; it's also possible that I've
misinterpreted some of the less relevant numeric fields. The two
double-precision values, however, are rock solid.

::

     mark_structure =   "=b 4x 6s 45x 502s   d   d 10x h h h 10x 8s x 6s x 8s x 6s 31x  f  f 32x"
     Mark= namedtuple( 'Mark',
      "record, name, text, lat, lon, display_name, enable_mark, anchor_mark,"
      "dt1, tm1, dt2, tm2, arrival_radius, max_xte" )

Given this structure and the associated named tuple, we can write
a pleasant (and highly reusable) generator function.

::

     def gen_items( file, structure, record_class ):
      size= struct.calcsize( structure )
      with open(file,'rb') as data:
          block= data.read(size)
          while len(block) == size:
              raw= record_class( *struct.unpack(structure,block) )
              yield raw
              block= data.read(size)

This makes for a simple application to extract the marks. An
application can reformat them into GPX or CSV format.

Something like this is a good starting point.

::

     def print_marks( file ):
       for mark in gen_items( file, mark_structure, Mark ):
           print( strip(mark.name), mark.lat, mark.lon )

We can easily write a version which includes the formatting
required to get the latitudes and longitudes into a format
acceptable by `GPSNavX <http://www.gpsnavx.com/>`__ or
`X-Traverse <http://www.x-traverse.com/>`__.

**Routes**

Routes are more complex than marks because they have a header,
followed by the details as a sequence of individual waypoints.
Since Chartview doesn't normalize these things, each route can
have duplicate waypoints, making it very difficult to get them
loaded into an application that normalizes properly.

How many WP1's can you have? The answer should be "one". Each
additional WP1 is a problem. But it's a small problem. For the WPx
points, we simply disambiguate them a route number. There seemed
to have been a limit of 15 routes, so we can just expand WP\ *x*
to WP\ *x*-*rr*, where *rr* is the route number.

**Bottom Line**

Data is preserved. Legacy PC and GPS can be chucked (or sold on
eBay to a collector).

It's important to note that data outlives application software.
This is a universal truth -- data lasts forever, applications come
and go. Highly optimized data structures (like the legacy
Chartview files) are a bad policy. Highly usable data structures
(like GPX files) are more valuable.

Python does a marvelous job of making a potentially horrifying
data conversion into something like a few evenings trying to find
the key pieces of data in the legacy files. Perhaps the hardest
part was tracking down single and double-precision floating-point
numbers. But once they were found -- matching known latitudes and
longitudes -- it was clear sailing.



-----

Microsoft will not provide USB 2.0 driver support ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-09-08 19:27:27.213000-04:00

Microsoft will not provide USB 2.0 driver support on Windows 9x or
earlier Windows operating systems
http://www.microsoft.com/whdc/archive/usb2support.mspx


Check out

Creating The Social Address Book
Terry ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-11-06 12:28:19.222000-04:00

Check out
Creating The Social Address Book
Terry Jones, 11.03.10, 06:00 AM EDT
http://www.forbes.com/2010/11/02/internet-fluidinfo-software-technology-social-media.html





