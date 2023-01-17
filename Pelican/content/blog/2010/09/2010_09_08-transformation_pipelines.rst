Transformation Pipelines
========================

:date: 2010-09-08 22:20
:tags: #python,functional programming
:slug: 2010_09_08-transformation_pipelines
:category: Technologies
:status: published

My laptop chartplotter software (`GPSNavX <http://www.gpsnavx.com/>`__)
is marvelous for visualizing a route. But, there are elements to route
planning that it doesn't handle gracefully.

Specifically, it doesn't provide useful elapsed time calculation at
all. While the TTG and ETA (Time to Go and Estimated Time of Arrival)
for the next waypoint are essential, they aren't enough. On a
sailboat, you need to know the complete sequence of planned arrival
times so that you can gauge the overall impact of wind and tide
vagaries on the trip.

As the trip progresses, the schedule variance allows informed
decision-making. Tack? Hole up for the night? Motor?

GPSNavX has a number of marvelous export capabilities -- as GPX, KML
or CSV data. These contain a list of waypoints and little more. We
need to enrich this data to produce an overall schedule.

Enriching The Data
------------------

Fundamentally, we have a number of enrichment stages. The functional
programming features of Python make this complex sequence of
enrichment stages into a very tidy, and adaptable application.

::

    if variance is None: variance= chesapeake
    with open(route_file,'rb') as source:
        rte= csv.reader(source)
        with open(schedule_file,'wb') as target:
            rte_rhumb= csv.writer( target )
            rte_rhumb.writerow(
                ["Name", "Lat", "Lon", "Desc",
                "Distance (nm)", "True Bearing", "Magnetic Bearing",
                "Distance Run", "Elapsed HH:MM", ]
                )
            for sched in gen_schedule( gen_mag_bearing( gen_rhumb( gen_route_points( rte ) ), variance), speed ):
                rte_rhumb.writerow(
                    [sched.point.name, sched.point.lat, sched.point.lon, sched.point.desc,
                    sched.distance,
                    int(sched.true_bearing.deg) if sched.true_bearing is not None else None,
                    int(sched.magnetic.deg) if sched.magnetic is not None else None,
                    sched.running, sched.elapsed_hm, ]
                    )

Essentially, the core of this is a simple composition of generator
functions.

::

    for sched in gen_schedule( gen_mag_bearing( gen_rhumb( gen_route_points( rte ) ), variance), speed ):

We have a number of individual transformations to look at. Each of
those follows a common pattern. The transformations are:

-  gen_route_points( rte )
-  gen_rhumb( route_points_iter )
-  gen_mag_bearing( rhumb_iter, declination )
-  gen_schedule( rhumb_mag_iter, speed= 5.0 )

There's a bunch of fancy math involved in the rhumb line and distance
between two points on the surface of the earth. For my purposes,
plane sailing is fine. I don't need great circle routes because I'm
not going far.

See `Calculate distance, bearing and more between Latitude/Longitude
points <http://www.movable-type.co.uk/scripts/latlong.html>`__ for a
clear and useful treatment of the math. Bowditch's American Practical
Navigator, `chapter
24 <http://www.irbs.com/bowditch/pdf/chapt24.pdf>`__, provides
alternate methods using table lookup and interpolation.

Seeding the Pipeline
--------------------

Here, for example, is the first step of the pipeline. Creating a
RoutePoint from the four values found in the CSV or GPX route file.

::

    RoutePoint= namedtuple( 'RoutePoint', 'name,lat,lon,desc,point' )

    def gen_route_points( rte ):
    for name,lat,lon,desc in rte:
        point= navigation.LatLon( lat, lon )
        yield RoutePoint( name, lat, lon, desc, point )

Since this is a generator function, it can use an iterator and be
used by an iterator. The source iterator can be a csv.reader. Or it
can be the result of XML parsing -- just so long as it matches the
interface specification of being an iterator over a 4-tuple.

Rhumb-Line Calculation
----------------------

We'll enrich the data. But we won't update an object. We'll stick
closely to the philosophy of immutable objects (i.e., named tuples)
which are modified by a generator function.

::

    RoutePoint_Rhumb= namedtuple( 'RoutePoint', 'point,distance,bearing' )

    def gen_rhumb( route_points_iter ):
        p1= route_points_iter.next()
        for p2 in route_points_iter:
            r, theta= navigation.range_bearing( p1.point, p2.point )
            yield RoutePoint_Rhumb( p1, r, theta )
            p1= p2
        yield RoutePoint_Rhumb( p2, None, None )

The essential calculations are in a separate module, navigation. What
we've done, however, is merge information from adjacent values so
that we can transform a simple list of points into a list of pairs of
points: the from and to for each leg of the trip. Between the two
points, we compute the simple rhumb line, the distance and bearing.

True to Magnetic Conversion
---------------------------

We need to enrich our waypoint rhumb-line information with magnetic
compass information. The true course needs a declination or variance
value added to it. Again, we're just creating new objects from
existing objects, using immutable named tuples.

::

    RoutePoint_Rhumb_Magnetic= namedtuple( 'RoutePoint', 'point,distance,true_bearing,magnetic' )

    def gen_mag_bearing( rhumb_iter, declination ): # A/k/a Variation
        for rp_rhumb in rhumb_iter:
            if rp_rhumb.bearing is None:
                yield RoutePoint_Rhumb_Magnetic(rp_rhumb.point, None, None, None)
            else:
                magnetic= rp_rhumb.bearing+declination(rp_rhumb.point)
                yield RoutePoint_Rhumb_Magnetic(rp_rhumb.point, rp_rhumb.distance, rp_rhumb.bearing, magnetic )

In this case, we're simply including a declination calculation. While
the model is available from
`IUGG <http://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>`__, we can often
use averages or approximations. And -- in the Chesapeake -- the
approximation is simply to add 11 degrees.

Spot-on accuracy doesn't matter, since we're driving a sailboat. The
compass isn't very accurate; the boat motion makes it hard to read
precisely; and current as well as leeway have profound effects. It is
helpful to have magnetic courses in the schedule instead of true
courses. Further, the chartplotter will be computing the final CTS
(Course to Steer).

So this stage in the pipeline might be optional.

Distance Run and Elapsed Time
-----------------------------

The final distance run and elapsed time is pretty simple. We're
creating a new tuple from existing tuples.

::

    SchedulePoint = namedtuple( 'RoutePoint', 'point,distance,true_bearing,magnetic,running,elapsed_min,elapsed_hm' )

    def gen_schedule( rhumb_mag_iter, speed= 5.0 ):
        distance = 0.0
        for rp in rhumb_mag_iter:
            if rp.true_bearing is None:
                yield SchedulePoint( rp.point, rp.distance, rp.true_bearing, rp.magnetic, None, None, None )
            else:
                distance += rp.distance
                elapsed_min= 60.*distance/speed
                h, m = divmod( int(elapsed_min), 60 )
                elapsed_hm = "{0:02d}h {1:02d}m".format( h, m )
                yield SchedulePoint( rp.point, rp.distance, rp.true_bearing, rp.magnetic, distance, elapsed_min, elapsed_hm )

This gives us a tuple that includes the original way point, the next
waypoint, the distance, true bearing, magnetic bearing, total
distance run, and elapsed time.

The amount of programming is minimal. The overall design seems
reasonably flexible and built from small, easy-to-validate pieces.

Python's functional programming features -- particularly generator
functions and named tuples -- seem to make it pleasant to write this
kind of transformation pipeline.





