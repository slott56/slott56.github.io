Navigation: Latitude, Longitude, Haversine, and all that
========================================================

:date: 2015-11-24 08:00
:tags: longitude,#python,haversine,latitude,navigation,navtools
:slug: 2015_11_24-navigation_latitude_longitude_haversine_and_all_that
:category: literate programming
:status: published

| For a few years, I was a tech nomad. See `Team Red
  Cruising <http://www.itmaybeahack.com/TeamRedCruising/>`__ for some
  stories of life on a sailboat. Warning: it's pretty dull.
| As a tech nomad, I lived and died (literally) by my ability to
  navigate. Modern GPS devices make the dying part relatively unlikely.
  So, let's not oversell the danger aspect of this.
| The prudent mariner plans a long voyage with a great deal of respect
  for the many things which can go wrong. One aspect of this is to
  create a "Float Plan". Read more about it
  here: `http://floatplancentral.cgaux.org <http://floatplancentral.cgaux.org/>`__.
| The idea is to create a summary of the voyage, provide that summary to
  trusted shore crew, and then check in periodically so that the shore
  crew can confirm that you're making progress safely. Failure to check
  in is an indicator of a problem, and action needs to be taken. We use
  a `SPOT Messenger <http://findmespot.com/en/>`__ to check in at noon
  (and sometimes at waypoints.)
| Creating a float plan involved an extract of the waypoints from our
  navigation software (`GPS NavX <http://www.gpsnavx.com/>`__). I would
  enrich the list of waypoints with estimated travel time between the
  points.  Folding in a departure time would lead to a schedule that
  could be tracked. I also include some navigation hints in the form of
  a bearing between waypoints so we know which way to steer to find the
  next point.
| The travel time is the distance (in  nautical miles) coupled with an
  assumption about speed (5 knots.) It's a really simple thing. But the
  core `haversine <https://en.wikipedia.org/wiki/Haversine_formula>`__
  calculation is not a first-class part of any spreadsheet app. Because
  of the degrees-to-radians conversions required, and the common
  practice of annotating degrees with a lot of internal punctuation
  (38°54ʹ57″ 077°13ʹ36″), it becomes right awkward to simply implement
  this as a spreadsheet.
| Some clever software has a good planning mode. The chartplotter on the
  boat can do a respectable job of estimating time between waypoints.
  But. It's not connected to a computer or the internet. So we can't
  upload that information in the form of a float plan. The idea of
  copying the data from the chart plotter to a spreadsheet is fraught
  with errors.

Navtools
--------

| Enter `navtools <https://github.com/slott56/navtools>`__. This is a
  library that I use to transform a route into a .csv with distances and
  bearings that I can use to create a useful float plan. I can add an
  estimated arrival time calculation so that a change to departure time
  creates the entire check-in schedule.
| This isn't a sophisticated GUI app. It's just enough software to
  transform a GPS NavX extract file into a more useful form. The GUI was
  a spreadsheet (i.e., Numbers.) From this we created a PDF with the
  details.
| Practically, we don't have good connectivity on the boat.  So we would
  create a number of alternative plans ("leave tomorrow", "leave the day
  after", "leave next Monday", etc.) we would go ashore, find a coffee
  shop, and email the various plans to ourselves. They could sit in our
  inbox, waiting for weather and tide to be favorable.
| Then, when the weather and tides were finally aligned, we could
  forward the relevant details to our trusted shore crew. This was a
  quick spurt of cell phone connectivity to forward an email. It worked
  out well. When the scheduled departure time arrived, we'd coax Mr.
  Lehman to life, raise the anchor and away.

Literate Programming
--------------------

| This is an exercise in literate programming. The code that's executed
  and the HTML documentation are both derived from source ReStructured
  Text (RST) documents. The documentation for the `navigation
  module <http://slott56.github.io/navtools/navigation.html>`__ includes
  the math along with the code that implements the math.
| I have to say that I'm enthralled with the intimate connection between
  requirements, design, and implementation that literate programming
  embodies.
| I'm excited to (finally) publish the thing to GitHub.
  See https://github.com/slott56/navtools.  I'm looking at some other
  projects that require the navtools module. What I wind up doing is
  copying and pasting the navigation calculation module into other
  projects. I had something like three separate copies on my laptop. It
  was time to fold all of the features together, delete the clones, and
  focus on one authoritative copy going forward.
| I still have to remove some crufty old code. One step at a time.
  First, get all the tests to pass. Then expunge the old code. Then make
  progress on the other projects that leverage the navtools.navigation
  module.





