Legacy Software is a Sticky Mess
================================

:date: 2021-10-12 08:00
:tags: navtools,navigation,design,#python
:slug: 2021_10_12-legacy_software_is_a_sticky_mess
:category: Technologies
:status: published

I'll get to legacy software. First, however, some backstory on
observability.

Sailors will sometimes create "Float Plans". Like aircraft flight plans,
they have an itinerary to make it slightly easier to find us when
something goes wrong. Unlike airspace, which is tightly controlled by
the FAA, the seas are more-or-less chaos.

The practice then, is to create float plan and give it to a trusted
shore-side party, go out sailing, check in periodically, and cancel the
whole thing when you're done sailing. If you miss a check-in, they can
call an appropriate Search-And-Rescue agency like the US Coast Guard or
BASRA or local cops with jurisdiction over a lake or river.

How much detail should be in this plan? For a long or complex trip, it
doesn't seem sensible to say "Going to the Bahamas" as your float plan.
That's a little thin on details. The bare minimum is to provide an
Estimated Time of Arrival (ETA). But. When you summarize 36 hours of
sailing to a single ETA, you invite observability problems. It's a
sailboat, and you could be becalmed. Things are fine, you're just going
to be late.

Late, of course is relative. Simply late means you missed your ETA. If
you're becalmed to the point where you're running low on supplies, then,
this can become a bit of a problem.

The general policy followed by SAR is to allow several hours past the
ETA before activating SAR resources. (The US Coast announces overdue
mariners on the VHF radio so others can keep a lookout for them and
render assistance.)

If you have a one-checkin-plan that summarizes 36 hours of sailing with
a single ETA, you're going to be waiting for many hours after the ETA
for help. So. Total systems failure after the first hour means 35 hours
of drifting before someone will even alert SAR folks. And then the SAR
folks will wait several hours after the ETA in case you're only slow.

What seems better is to have a sequence of waypoints with ETA's at each
waypoint. That way you have incremental evidence of success or failure,
and you're not waiting a LOOOONG time for your one-and-only ETA to pass
without a check-in.

This leads us to software. And legacy software.

Creating the Plan
-----------------

To create a sensible plan, you have waypoints as Latitude, Longitude
pairs. These are angles on a sphere, not distances on a plane, so
computing the length of a leg isn't a simple hypotenuse.

It is a lot like a hypotenuse. For short distances, we can assume the
earth is more-or-less flat. We can then use a relatively simple
conversion (cosine of the latitude) to compress the longitudes toward
the poles. We can convert lat and lon to distances and use a hypotenuse
and get a really close answer.

::

   def range_bearing(p1: LatLon, p2: LatLon, R: float = NM) -> tuple[float, Angle]:
       """Rhumb-line course from :py:data:`p1` to :py:data:`p2`.

       See :ref:`calc.range_bearing`.
       This is the equirectangular approximation.
       Without even the minimal corrections for non-spherical Earth.

       :param p1: a :py:class:`LatLon` starting point
       :param p2: a :py:class:`LatLon` ending point
       :param R: radius of the earth in appropriate units;
           default is nautical miles.
           Values include :py:data:`KM` for kilometers,
           :py:data:`MI` for statute miles and :py:data:`NM` for nautical miles.
       :returns: 2-tuple of range and bearing from p1 to p2.

       """
       d_NS = R * (p2.lat.radians - p1.lat.radians)
       d_EW = (
           R
           * math.cos((p2.lat.radians + p1.lat.radians) / 2)
           * (p2.lon.radians - p1.lon.radians)
       )
       d = math.hypot(d_NS, d_EW)
       tc = math.atan2(d_EW, d_NS) % (2 * math.pi)
       theta = Angle(tc)
       return d, theta

This means we can't trivially write down a list of waypoints. We need to
do some fancy math to compute distances.

For years and years. (Since our first "big" trip in 2007.) I've used
spreadsheets in various forms to work out the waypoints, distances,
estimated time enroute (ETE) and ETA.

The math isn't too far beyond what a spreadsheet can do. But. There's a
complication.

Complications
-------------

File formats are a complication.

There are KML files, GPX files, and CSV files that are used by various
pieces of software. This is only the tip of the iceberg, because some of
Navionics devices have an even more interesting USR file that contains
everything in your chartplotter. It's cool. But complicated.

The file formats are -- clearly -- way outside the box for a
spreadsheet.

**Python to the rescue.**

Since I'm a Python hack (and have been since well before 2007) I've got
all kinds of file conversion tools.
See https://github.com/slott56/navtools.

But.

And here's where legacy enters the picture. (Music Cue.)

   | Fear that rattles in men's ears
   | And rears its hideous head
   | Dread ... Death ... in the wind ...

Spreadsheets.

Up until yesterday, the final planning tool was a spreadsheet with
waypoints and times. Mac OS X Numbers is GREAT for this. I can pile in
boat information, crew information, safety information, the itinerary,
and SAR contact details in one spreadsheet, save it as a PDF, and email
it to my shore-side contacts.

The BEST part of this was tinkering with the departure time while we
waited for weather. We could plug in the day we're leaving, get revised
ETA's for the waypoints, push the document, and take off.

(We use an old `Spot Navigator <https://www.findmespot.com/en-us/>`__ to
provide notifications at midnight to show progress. We're going to
upgrade to a SpotX so we can send messages a little more flexibly.)

The Legacy Spreadsheet
----------------------

The legacy spreadsheet has a lot of good UX features. It's really
adequate for some user stories. Save as PDF rocks.

However.

For the more advanced route planning, it isn't ideal. Specifically,
spreadsheets can be weak on multiple "what-if" scenarios.

The genesis of spreadsheets (I'm old, I was there, I remember VisiCalc)
was "what-if" analysis. Change an assumption and follow the consequences
through the lattice of dependent cells. These are hard to save. You can
"Save As" to make a copy of the spreadsheet. You can save pages within a
single spreadsheet. These are terrible because you can't really make a
more fundamental change very easily. You have to make the same change to
all the copies in your pile of "what-if" alternatives.

To be very specific. I often need to plan for different boat speeds. We
have a sailboat; wind and water matter a lot. Slow is about 5 knots.
Fast is about 6 knots. Our theoretical top speed is 8 knots, but we've
rarely seen that without a river flowing along with us. Sailing at that
speed means a lot of sail wrestling, something we'd rather not do.

Fine. That's 3 scenarios, one for each speed: 5, 5.5, and 6. No big
deal.

Until we add a waypoint. Or move a waypoint. Now we have to reset all
three spreadsheets with a different itinerary. Since it's a different
number of rows, we have the usual copy-and-paste problems in
spreadsheets.

What's Better?
--------------

Jupyter notebooks crush the life out of spreadsheets.

Here's the revised workflow.

#. Create the route. Use tools like OpenCPN so the route can be exported
   as a GPX or CSV file.
#. Use a notebook to parse the route file, creating an internal Route
   object.
#. Manipulate the Route object, providing different ETA's and speed
   assumptions. These assumptions lead to multiple cells in the
   notebook. They can all share details so that one fundamental change
   leads to lots and lots of recomputation of itineraries. We can
   include all kinds of headings and markdown notes and thoughts and
   considerations.
#. Finalize a route that's part of the plan. Still working in the
   confines of a longish notebook.
#. Emit a Markdown file with Vessel Identification, Itinerary, Notes,
   and SAR Contact sections. Run `pandoc <https://pandoc.org>`__ to make
   a PDF. (This is the foundation for the nbconvert utility.)

This workflow creates two categories results:

One result is a Notebook with all of the planning details and thoughts
and contingencies and considerations.

The other result(s) are float plan documents as PDF's that can be shared
widely.

Why did this take so long?
--------------------------

I used spreadsheets from 2007 to 2021. Why switch now? Some reasons.

Legacy solutions are sticky. This has a lot of consequences. I built up
"expertise" in making the legacy work. I had become an "expert" in
working around the hinky little problems with multiple what-if scenarios
and propagating changes from the route into the what-ifs. For example, I
limited the number of what-if scenarios I would consider because more
than two got confusing.

New solutions are sometimes invisible. I only learned about Jupyter
Notebooks about three years ago. I did not realize how powerful they
were. I've since rearranged my thinking.

I've known about RST and Markdown and Pandoc for years. But. Getting
from spreadsheet-like flexibility to a Markdown document was never a
clear step. Without something like Jupyter Lab.

Pulling it all together
-----------------------

Does it require some kind of catalyst to force change?

Is it a slow accretion of evidence that the legacy software isn't
working?

I'm pretty sure I had a long, slow Aha! moment as I realized that the
Numbers spreadsheet was a large pain in the ass and a notebook would be
simpler. It took a few days of fiddling to become really, really sure
Numbers was not working out.

I think one of the biggest issues was a third "what-if" scenario. It was
helpful to visualize arrival times. But. It was a huge pain in the neck
to fiddle with the spreadsheets to get the right waypoints in there and
summarize the alternatives.

I think the lesson here is to avoid automating anything unless you
actually are the user.

If an organization wants software, a developer needs to do the job
manually to \*really\* understand what the pain points are. Users
develop expertise in the wrong things. And they want automation where
the benefits are minor. Automating the spreadsheet-to-PDF is wrong.
Replacing the spreadsheet is right.





