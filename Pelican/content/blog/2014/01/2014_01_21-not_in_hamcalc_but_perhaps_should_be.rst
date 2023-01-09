Not in HamCalc -- But perhaps should be
=======================================

:date: 2014-01-21 08:00
:tags: #python,HamCalc
:slug: 2014_01_21-not_in_hamcalc_but_perhaps_should_be
:category: Technologies
:status: published

This is the kind of little program that would be in HamCalc. But doesn't
appear to be.

Looking at the Airfoil web page, specifically, this one:
http://airfoiltools.com/airfoil/details?airfoil=ls013-il.

The measurements are all given in fractions of the depth of the airfoil.
So you have to scale them. I was working with what may turn out to be a
48" rudder for a boat based on this design. I'm waiting for some details
from the engineer who really knows this stuff.

How do we turn these fractions into measurements for folks that work in
feet and inches?

We can use a spreadsheet -- and I suspect many folks would be successful
spreadsheeting this data. For some reason, that's not my first choice. I
worry about accidental copy and paste errors or some other fat-finger
blunder in a spreadsheet. With code, it's easy to reproduce the results
from the source as needed.

Here's the raw data.
http://airfoiltools.com/airfoil/seligdatfile?airfoil=ls013-il


Part 1. Fractions.

::

  from fractions import Fraction
  class Improper(Fraction):
      def __str__( self ):
          whole= int(self)
          fract= self-whole
          if fract == 0: return '{0}'.format(whole)
          if whole == 0: return '{0}'.format(fract)
          return '{0} {1}'.format(whole,fract)

The idea is to be able to produce improper fractions like 47 ½" or
24" or ¾".  My Macintosh magically rewrites fractions into a
better-looking Unicode sequence. I didn't include that feature in the
above version of Improper. Mostly because in Courier, the generic
fractions look kind of icky.


The raw data is readable as a kind of CSV file.

::

  import csv
  def get_data( source ):
      rdr= csv.reader( source, delimiter=' ', skipinitialspace=True)
      heading= next(rdr)
      print( heading )
      for row in rdr:
          yield float(row[0]), float(row[1])


That saves fooling around with parsing -- we get the profile numbers
from the raw data as a pair of floats.


Finally, the report.

::

  def report( seligdatfile, depth, unit ):
      scale=16 #th of an inch
      for d, t in get_data( source ):
          d_in, t_in = d*depth, t*depth
          d_scale = Improper( int(d_in*scale), scale )
          t_scale = Improper( int(t_in*scale), scale )
          print(
            '{0:6.2f} {unit} {1:6.2f} {unit} \| {2:>8s} {unit} {3:>8s} {unit}'.format(
              d_in, t_in, d_scale, t_scale, unit=unit) )

This gives us a pleasant-enough table of the measurements in decimal
places and fractions.


We can use this for any of the variant airfoils available.  Here's
the top-level script.

::

  import urllib.request
  with urllib.request.urlopen(
    "http://airfoiltools.com/airfoil/seligdatfile?airfoil=ls013-il"
    ) as source:
      seligdatfile= source.read().decode("ASCII")

  import io
  with io.StringIO( seligdatfile ) as source:
      report( source, depth=48, unit="in." )


I'm guessing the data files are ASCII encoded, not UTF-8. It doesn't
appear to matter too much, and it's an easy change to make if they
track down an airfoil data file what has a character that's not
ASCII, but UTF-8.





