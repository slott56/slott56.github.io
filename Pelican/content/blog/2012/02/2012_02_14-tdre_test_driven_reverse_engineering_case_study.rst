TDRE - Test Driven Reverse Engineering Case Study
=================================================

:date: 2012-02-14 08:00
:tags: unit testing,test-driven reverse engineering,#python
:slug: 2012_02_14-tdre_test_driven_reverse_engineering_case_study
:category: Architecture & Design
:status: published



**Background**


Read up on compass variation or declination.  For example, this
`NOAA <http://www.ngdc.noaa.gov/geomag/declination.shtml>`__ site
provides some useful information.


Mariners use the magnetic variation to compute the difference between
True north (i.e., aligned with the grid on the chart) and Magnetic
north (i.e., aligned with the compass.)


The essential use case here is "What's the compass variation at a
given point?"  The information is printed on paper charts, but it's
more useful to simply calculate it.


There are two `magnetic
models <http://www.ngdc.noaa.gov/geomag/models.shtml>`__: the US
Department of Defense World Magnetic Model (WMM) and the International
Association of Geomagnetism and Aeronomy (IAGA) `International
Geomagnetic Reference Field
(IGRF) <http://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>`__.


A packaged solution is geomag7.0.  This includes both the WMM and the
IGRF models.  This is quite complex.  However, it does have "sample
output", which amount to unit test cases.


The essential spherical harmonic model is available separately as a
small Fortran program,
`igrf11.f <http://www.ngdc.noaa.gov/IAGA/vmod/igrf11.f>`__.


Which leads us to reverse engineering this program into Python.


**TDRE Approach**


The TDRE approach requires having some test cases to drive the reverse
engineering process toward some kind of useful results.


The geomag7.0 package includes two "Sample Output" files that have the
relevant unit test cases.  The file has column headings and 16 test
cases.  This leads us to the following outline for the unit test
application.

::

   class Test_Geomag( unittest.TestCase ):
       def __init__( self, row ):
           super( Test_Geomag, self ).__init__()
           self.row= row
       def runTest( self ):
           row= self.row
           if details: 
               print( "Source: {0:10s} {1} {2:7s} {3:10s} {4:10s} {5:5s} {6:5s}".format( row['Date'], row['Coord-System'], row['Altitude'], row['Latitude'], row['Longitude'], row['D_deg'], row['D_min'] ),
               file=details )

           date= self.parse_date( row['Date'] )
           lat= self.parse_lat_lon( row['Latitude'] )
           lon= self.parse_lat_lon( row['Longitude'] )
           alt= self.parse_altitude(row['Altitude'] )

           x, y, z, f = igrf11syn( date, lat*math.pi/180, lon*math.pi/180, alt, coord=row['Coord-System'] )
           D = 180.0/math.pi*math.atan2(y, x) # Declination 

           deg, min = deg2dm( D )

           if details: 
               print( "Result: {0:10.5f} {1} K{2:<6.1f} {3:<10.3f} {4:<10.3f} {5:5s} {6:5s}".format( date, row['Coord-System'], alt, lat, lon, str(deg)+"d", str(min)+"m" ), 
                   file=details )
               print( file=details )

           self.assertEqual( row['D_deg'], "{0}d".format(deg) )
           self.assertEqual( row['D_min'], "{0}m".format(min) )

   def suite():
       s= unittest.TestSuite()
       with open(sample_output,"r") as expected:
           rdr= csv.DictReader( expected, delimiter=' ', skipinitialspace=True )
           for row in rdr:
               case= Test_Geomag( row )
               s.addTest( case )
       return s

   r = unittest.TextTestRunner(sys.stdout)
   result= r.run( suite() )
   sys.exit(not result.wasSuccessful())






The Test_Geomag class does two things.  First, it parses the source
values to create a usable test case.  We've omitted the parsers to
reduce clutter.  Second, it produces details to help with debugging.
This is reverse engineering, and there's **lots** of debugging.  It
depends on a global variable, details, which is either set to
sys.stderr or None.


This suite() function builds a suite of test cases from the input
file.


The unit under test isn't obvious, but there's a call to
the igrf11syn() function where the important work gets done.  We can
start with this.

::

    def  igrf11syn( date, nlat, elong, alt=0.0, coord='D' ):
       return None, None, None, None






This lets us run the tests and find that we have work to do.


**Reverse Engineering**


The IGRF11.F fortran code contains this IGRF11SYN "subroutine" that
does the work we want.  The geomag 7.0 package has a function called
shval3 which is essentially the same thing.


Both are implementations of the same underlying "13th order spherical
harmonic series" or a "truncated series expansion".


The Fortran code contains numerous Fortran "optimizations".  These are
irritating hackarounds because of actual (and perceived) limitations
of Fortran.  They fall into two broad classes.

-   **Hand Optimizations**.  All repeated expressions were manually
    hoisted out of their context.  This is clever but makes the code
    particularly obscure.  It doesn't help when local variables are named
    ONE, TWO and THREE.  Bad is it is, not much needs to be done about
    this.  Python code looks a bit like Fortran code, so very little
    needs to be done except add \`math.\` to the various function calls
    like sort, cos and sin.

-   **Sparse Array Chicanery**.  There are actually two spherical
    harmonic series.  The older 10-order and the new 13-order.   Each
    model has two sets of coefficients: *g* and *h*.  These form two
    half-matrices plus a vector.  The old models have 55 *g* values in
    one matrix, 55 *h* values in second matrix, and a set of 10 more *g*
    values that form some kind of vector; 160 values.  The new models
    have 91 g, 91 *h* and 13 *g* in the extra vector; 195 values.  There
    are 23 sets of these coefficients (for 1900, 1905, ... 2015).  The
    *worst* case is 23×195=4,485 values.  This appears to be too much
    memory, so the two matrices and vectors are optimized into a single
    opaque collection of 3,256 numbers and delightfully complex set of
    index calculations.

**Phase 1.**  Do the smallest "literal" transformation of Fortran to
Python.

This means things like this:

-  Transforming the subroutine into a Python function with multiple return values.

-  Reasoning out the overall "steps".  There's a bunch of setup followed by the essential series calculation followed by some final calculations.

-  Locating and populating the global variables.

-  Reformatting the **if** statements.

-  Removing the GOTO's.  Either make them separate functions or properly nest the code.

-  Reformatting the **do** loop.

-  Handling the 1-based indexing.  In almost all cases, Fortran "arrays" are best handled as Python dictionaries (**not** lists).

Once this is done, there are some remaining special-case
discrepancies.  Most of these are tacit assumptions about the
problem domain that turn out to be untrue.  For example, the
Geodetic, Geocentric features seemed needless.  However, they're
not handled trivially, and need to be left in place.  Also,
conversion of signed values in radians to degrees and minutes
isn't trivial.

This leads to passing all 16 unit tests with the single opaque
collection of 3,256 numbers and delightfully complex set of index
calculations.

**Phase 2.**  Optimize so that it makes some sense in Python.

This involves unwinding the index calculations to simplify the array.
The raw coefficients are available
(`igrf11coeffs.txt <http://www.ngdc.noaa.gov/IAGA/vmod/igrf11coeffs.txt>`__)
and they have a sensible structure that separates the two matrices
very cleanly.  The code uses the combined matrix (called gh) in a
very few places.  The index calculations aren't obvious at all, but a
few calls to print reveal how the matrix is accessed.

Given (1) unit tests that already work and (2) the pattern of access,
it's relatively easy to hypothesize a dictionary by year that
contains a pair of simple dictionaries, g[n,m] and h[n,m], for the
coefficients.

**Cleanup and Packaging**

Once the tests pass, the package -- as a whole -- needs to be made
reasonably Pythonic.   In this case, it means a number of additional
changes.  For example, converting the API from degrees to radians,
supplying appropriate default values for parameters, providing
convenience functions.

Additionally, there are Python ways to populate the coefficients
neatly and eliminate global variables.  In this case, it seemed
sensible to create a Callable class which could load the coefficients
during construction.

Note that there's little point in profiling to apply further
optimizations.  The legacy Fortran code was already meticulously hand
optimized.



-----

I am not sure where you are getting your info, but...
-----------------------------------------------------

Universal Engineering<noreply@blogger.com>

2012-02-23 01:12:54.811000-05:00

I am not sure where you are getting your info, but great topic. I needs
to spend some time learning much more or understanding more. Thanks for
wonderful info I was looking for this.
`Structural Engineering West Palm
Beach <http://www.universalengineering.net/west-palm-beach.html>`__





