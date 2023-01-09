TDD -- From SME Spreadsheet to TestCase to Code
===============================================

:date: 2011-02-17 08:00
:tags: unit testing,#python,tdd
:slug: 2011_02_17-tdd_from_sme_spreadsheet_to_testcase_to_code
:category: Architecture & Design
:status: published

In "`Unit Test Case, Subject Matter Experts and
Requirements <{filename}/blog/2011/02/2011_02_08-unit_test_case_subject_matter_experts_and_requirements.rst>`__"
I suggested that it's often pretty easy to get a spreadsheet of
full-worked out examples from subject-matter experts. Indeed, if your
following TDD, that spreadsheet of examples is solid gold.

Let's consider something relatively simple. Let's say we're working
on some fancy calculations. Our users explain until they're blue in
the face. We take careful notes. We *think* we understand. To
confirm, we ask for a simple spreadsheet with inputs and outputs.

We get something like the following. The latitudes and longitudes are
inputs. The ranges and bearings are outputs. [The math can be seen at
"`Calculate distance, bearing and more between Latitude/Longitude
points <http://www.movable-type.co.uk/scripts/latlong.html>`__".]

========== =========== ========== =========== ======= =========
Latitude 1 Longitude 1 Latitude 2 Longitude 2 range   bearing
========== =========== ========== =========== ======= =========
50 21 50N  004 09 25W  42 21 04N  071 02 27W  2805 nm 260 07 38
========== =========== ========== =========== ======= =========

Only it has a a few more rows with different examples. Equator
Crossing. Prime Meridian Crossing. All the usual suspects.

**TDD Means Making Test Cases**

Step one, then, is to parse the spreadsheet full of examples and
create some domain-specific examples. Since it's far, far easier to
work with .CSV files, we'll presume that we can save the
carefully-crafted spreadsheet as a simple .CSV with the columns shown
above.

Step two will be to create working Python code from the
domain-specific examples.

The creation of test cases is a matter of building some intermediate
representation out of the spreadsheet. This is where plenty of
parsing and obscure special-case data handling may be necessary.

::

    from __future__ import division
    import csv
    from collections import namedtuple
    import re

    latlon_pat= re.compile("(\d+)\s+(\d+)\s+(\d+)([NSWE])")
    def latlon( txt ):
        match= latlon_pat.match( txt )
        d, m, s, h = match.groups()
        return float(d)+float(m)/60+float(s)/3600, h

    angle_pat= re.compile("(\d+)\s+(\d+)\s+(\d+)")
    def angle( txt ):
        match= angle_pat.match( txt )
        d, m, s = match.groups()
        return float(d)+float(m)/60+float(s)/3600

    range_pat= re.compile("(\d+)\s*(\D+)")
    def range( txt ):
        match= range_pat.match( txt )
        d, units = match.groups()
        return float(d), units

    RangeBearing= namedtuple("RangeBearing","lat1,lon1,lat2,lon2,rng,brg")

    def test_iter( filename="sample_data.csv" ):
        with open(filename,"r") as source:
            rdr= csv.DictReader( source )
            for row in rdr:
                print row
                tc= RangeBearing(
                    latlon(row['Latitude 1']),  latlon(row['Longitude 1']),
                    latlon(row['Latitude 2']),  latlon(row['Longitude 2']),
                    range(row['range']),
                    angle(row['bearing'])
                    )
                yield tc

    for tc in test_iter():
        print tc

This is long, but, it handles a lot of the formatting vagaries that
users are prone to.

**From Abstract to TestCase**

Once we have a generator to build test cases as abstraction examples,
generating code for Java or Python or anything else is just a little
template-fu.

::

    from string import Template
    testcase= Template("""
        class Test_${name}( unittest.TestCase ):
         def setUp( self ):
             self.p1= LatLon( lat=GlobeAngle(*$lat1), lon=GlobeAngle(*$lon1) )
             self.p2= LatLon( lat=GlobeAngle(*$lat2), lon=GlobeAngle(*$lon2) )
         def test_should_compute( self ):
             d, brg = range_bearing( p1, p2, R=$units )
             self.assertEquals( $dist, int(d) )
             self.assertEquals( $brg, map(int,map(round,brg.deg)))
        """)
    for name, tc in enumerate( test_iter() ):
        units= tc.rng[1].upper()
        dist= tc.rng[0]
        code= testcase.substitute( name=name, dist=dist, units=units, **tc._asdict()  )
        print code

This shows a simple template with values filled in. Often, we have to
generate a hair more than this. A few imports, a "unittest.main()" is
usually sufficient to transform a spreadsheet into unit tests that we
can confidently use for test-driven development.



-----

Pretty cool. Thanks for sharing
-------------------------------

Anonymous<noreply@blogger.com>

2011-02-17 11:50:41.977000-05:00

Pretty cool. Thanks for sharing





