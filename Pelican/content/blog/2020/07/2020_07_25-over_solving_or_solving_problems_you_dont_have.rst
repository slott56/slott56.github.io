Over-Solving or Solving Problems You Don't Have
===============================================

:date: 2020-07-25 08:02
:tags: #python,haversine,complexity,OO design,Design Principles,SOLID,navigation
:slug: 2020_07_25-over_solving_or_solving_problems_you_dont_have
:category: Architecture & Design
:status: published

Sometimes we call them "Belt and Braces" solutions. As a former
suspenders person who switched to belts, the idea of wearing both is a
little like over-engineering. In the unlikely event of catastrophic
failure of one system, your pants can still remain properly hoist.
There's a weird, but defensible reason for that. Most over-engineering
lacks a coherent reason.


Sometimes we call them "Bells and Whistles." The solution has both
bells and whistles for signaling. This is usually used in a
derogatory sense of useless noisemakers, there for show only. Again,
there's a really low-value and dumb, but defensible reason for this.


While colorful, none of this is helpful for describing
over-engineered software. Over-engineered software is often
over-engineered for incoherent and indefensible reasons.


Over-engineering generally means trying to solve a problem that no
user actually has. This leads to throwing around irrelevant features.

Concrete Example
---------------------


I lived on a boat. I spent a fair amount of time fretting over
navigation.


There are two big questions:


#. How far apart are two points, really.

#. What's the real bearing from one point to another.


These are -- in some cases -- easy to answer.


If you have a printed, paper chart at the right scale, you can use
dividers to compute a distance. It's actually a very easy task.
Similarly, you can read the bearing off the chart directly. There's a
trick to comparing a course to a nearby compass rose, but it's easy
to learn and very accurate.


Of course, we don't want to painstakingly copy our notes from a paper
chart to a spreadsheet to add them up to get total distance. And then
fold in speed to get time and fuel consumption. These summary
computations are a pain.


What you want is to do all of this with a computer.


#. Plot the points using a piece of software like OpenCPN (https://opencpn.org).

#. Extract the GPX file.

#. Compute distances, bearings, and durations to create a route.

   
"So?" you ask.


So. When I did this, I researched the math and got a grip on the
haversine formula for doing the spherical geometry computation of
distances between points on a sphere.


It's not too bad. The formula are big-ish. But manageable.
See http://www.edwilliams.org/avform.htm#Dist for the great circle
distance formula.

..  math::

    d = 2 \times \arcsin \sqrt {
        \bigg(\sin \frac {\phi_2-\phi_1} {2} \biggr)^2 + \cos \phi_1 \times \cos \phi_2 \times \bigg( \sin \frac {\lambda_1 - \lambda_2} {2} \bigg) ^2
    }



For airplanes and powered freighters crossing oceans, this is
perfect.


For a small sailboat going from Annapolis, Maryland, to the Bahamas,
this level of complexity is craziness. While accurate, it doesn't
really solve the problem I have.


I don't actually need that much accuracy.


I need this much accuracy.

..  math::

    d = \sqrt{
    [R \times (\phi_2 - \phi_1)]^2 + [R \times \cos \phi_1 \times (\lambda_2 - \lambda_1)]^2
    }



And no more. This is the essential hypotenuse distance using an
R-factor to convert the difference between latitudes and the distance
between longitudes into pretty-close distances. For nautical miles, R
is 60×180÷π.


This is simpler and it solves the problem I actually have. Up to
about 232 miles, the answer is within 1 mile of correct. The error
grows quickly. Double the distance and the error seems to jump to 8
miles. A 464 mile sailing journey (at 6 knots) takes 3 days. Wind,
weather, tides and currents will introduce more error than the
simplifying assumptions.


What's important is this can be put into a spreadsheet without pain.
I don't **need** to write sophisticated Python apps to apply
haversine to sequences of way-points. I can do a simpler hypotenuse
computation on waypoints converted to radians.

Is there a lesson learned?
--------------------------


I think there is.


There's the haversine a super-general solution. It handles
great-circle routes elegantly.


But it doesn't solve my actual problem. And that makes it
over-engineering.


My problem is what we call rhumb-line sailing. Over short-enough
distances the world may as well be flat. Over slightly longer
distances, errors in the ship's compass and speedometer make a
hyper-accurate great circle route moot.


(Even with several fancy GPS-based navigation computers, a prudent
mariner has paper backups. The list of waypoints, estimated times and
directions are essential when the boat's GPS reciever fails.)


I don't really need the sophistication (and the potential for bugs)
with haversine. It doesn't solve a problem I actually have.






