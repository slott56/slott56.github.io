Innovation, Arduino and "Tinkering"
===================================

:date: 2012-07-12 08:00
:tags: arduino,#MADExpo,innovation
:slug: 2012_07_12-innovation_arduino_and_tinkering
:category: Technologies
:status: published

| Many of my customers (mostly super-large IT shops) wouldn't recognize
  innovative behavior.  Large organizations tend to punish defectors
  (folks that don't conform), and innovation is non-conforming.
| I've just had two object lessons in innovation.  The state of the art
  has left many in-house IT development processes in the dust.  The cost
  and complexity of innovation has fallen, but organizations continue to
  lumber along pretending that innovation is risky or complex.
| You can find endless advice on how to foster a `culture of
  innovation <http://scholar.google.com/scholar?q=culture+of+innovation&hl=en&as_sdt=0&as_vis=1&oi=scholart&sa=X&ei=fBf-T-utG6aC2wXrr-GzDw&ved=0CGEQgQMwAA>`__.
   Often, this advice includes a suggestion that innovative projects
  should somehow "`fail
  fast <http://www.google.com/search?client=safari&rls=en&q=innovation+fail+fast&ie=UTF-8&oe=UTF-8>`__".
   I'm deeply suspicious of "fail fast" advice.  I think it misleads IT
  management into thinking there's a super-cheap way to innovate.  It's
  misleading because "fail fast" leaves too many questions unanswered.

-  How soon do you know something's about to be a failure?
-  What's the deadline that applies so that failure can happen quickly?

-  What's the leading indicator of failure?

| 
| If you are gifted enough to predict the future -- and can predict
  failure -- why not apply that gift to predicting success?  Give up on
  the silliness of unstructured "innovation" and simply implement what
  will not fail.
| At MADExpo, I saw an eye-opening presentation on the Arduino.  I
  followed that with viewing `Massimo Banzi's TED
  Talk <http://www.ted.com/talks/massimo_banzi_how_arduino_is_open_sourcing_imagination.html>`__
  on the subject of Arduino, imagination and open source.
| There are two central parts of the Arduino philosophy.

-  Tinkering.
-  Interaction Design.

| 
| **Background**
| Without delving too deeply, I'm trying to build a device that will
  measure the position of a hydraulic piston.  It's the hydraulic
  steering on a boat, and a measurement of the piston position provides
  the rudder position, something that's handy for adjusting sail trim to
  reduce the strain on an autopilot.
| Clearly, such a device needs to be calibrated with the extreme port
  and starboard range of motion.  Barring unusual circumstances, the
  amidships position is simply the center between the two limits.
| Part 1.  Buy an Arduino, a Sharp GP2Y0A02YK0F IR distance measurer
  (for 10-80 cm), plus miscellaneous things like breadboard, jumpers,
  LED's, test leads, etc.  A trip to `Radio
  Shack <http://www.radioshack.com/product/index.jsp?productId=12268262>`__
  covers most of the bases.  The rest comes from
  `Sparkfun <http://www.sparkfun.com/>`__, `Robot
  Shop <http://www.robotshop.com/>`__,
  `Digi-Key <http://www.digikey.com/>`__ and
  `Mouser <http://www.mouser.com/>`__.
| Part 2.  Learn the language (a subset of C.)  Learn core algorithms
  (de-bouncing buttons and the IR sensor).
| **Tinkering**
| At this point, we've tinkered.  Heavily.
| What's important for IT managers is that tinkering doesn't have a
  project plan.  It doesn't have a simple schedule and clear milestones.
   It's a learning process.  It's knowledge acquisition.
| The current replacement for tinkering is training.  Rather than learn
  by attempting (and failing), IT managers hire experts to pass on
  knowledge.  This is, generally, limiting and specifically stifles
  innovation.
| Years ago, I worked on embedded systems: hardware software hybrids.
   We burned ROMs and programmed in assembler.  Back in those days, this
  kind of tinkering was difficult, and consequently frowned upon.  It
  was difficult to specify, locate, source, and assemble the components.
   There was a lot of reading complex product data sheets to try and
  determine what to buy and how few were needed.
| What had once been a very serious (and very difficult) electrical
  engineering exercise (IR sensor, button, LED, power supply, etc.,
  etc.) was a few days of tinkering with commodity parts.  The price was
  low enough and availability ubiquitous enough that frying a few LED's
  is of no real consequence.  Even frying an Arduino or two isn't much
  of a concern.
| **Interaction Design**
| The next step is to work out the user interface.  For the normal
  operating mode, the input comes from the hydraulic piston and the
  output is some LED's to show the displacement left or right of center.
   Pretty simple.
| However.
| There's the issue of calibration.  Clearly, the left and right limits
  (as well as center position) need to be calibrated into the device.
| Just as clearly, this means that the device needs buttons and LED's to
  switch from normal mode to calibration mode.  And it needs some
  careful interaction design.  There are several operating modes
  (uncalibrated, calibrating, normal) with several submodes for
  calibrating (setting left, setting right, setting center.)
| Once upon a time, we wrote long, wordy documents.  We drew complex UML
  state charts.  We drew all kinds of pictures to try and capture the
  important features of the interaction.
| **Enter Arduino**
| The point of Arduino is not to spend too much time up front
  over-specifying something that's probably a bad idea.   The point is
  to experiment quickly with different user interface and interaction
  experiences to see what works and what doesn't work.
| The same is true of many modern development environments.  Web
  development, for example, can be done by using sophisticated
  frameworks, writing little backend code and messing with the jQuery,
  CSS and HTML5 aspects of the interaction.
| The scales fell from my eyes when I started to document the various
  operating modes.
| Arduino doesn't have a great unit testing environment.  It's for
  tinkering, after all.  It's also for building small, focused things.
   Not large, rambling, hyper-complex things.  You can achieve
  complexity through the interaction of small, easy-to-test things.  But
  don't start out with complexity.
| After writing a few paragraphs, I realized that the piston movements
  could easily be self-calibrating.  Simply track the maximum and
  minimum distances ever seen.  That's it.  Nothing more.  In the case
  of a boat, it means swinging the wheel from stop to stop to define the
  operating range.  That's it.
| A button (to clear the accumulated history) is still useful.  But much
  simpler since it's a one-time-only reset button.  Nothing more.
| Moving from idea to working prototype took less time than writing this
  blog post.
| Next steps are to tinker with various display alternatives.  How many
  LED's?  What colors?  LCD Text Display?  There are numerous choices.
| Rather than wasting times on UML, specifications, whiteboard and
  diagrams, it's a simpler matter to write the user stories and tinker
  with display hardware.



-----

I always love these either or conversations.

I am...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-07-14 03:27:21.858000-04:00

I always love these either or conversations.
I am not sure what the answer is, just trust me and give me an infinite
amount of money to tinker and experiment. This ignores the realities of
running a business, cash flow and making payrole.
I need to know down to the exact number of hours of how long it will
take you to implement (some nebulous requirement). This ignores the fact
that requirements discovery is unpredictable whose unknowns are turbo
charged by politics.
How about a different approach. How about saying, I have x dollars w/
which to experiments; what should we try first. As we are trying x, lets
think about what the next step should be. I think that this is called
agile?
How about if we just realize that the client doesn't want to tinker but
wants a package solution. Check out "The chicken and egg of big data
solutions" by Jim Stogdill.
(http://radar.oreilly.com/2012/05/hadoop-applications-package-enterprise-startups.html)


Personally, I like &quot;Do-It-Yourself: An Automa...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-07-23 11:11:37.392000-04:00

Personally, I like "Do-It-Yourself: An Automated Bartender" project.
(https://ieeetv.ieee.org/ieee_spectrum_reports/barbot-mixes-drinks-automatically-)


&quot;just trust me and give me an infinite amount...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2012-09-01 08:10:13.544000-04:00

"just trust me and give me an infinite amount of money" is clearly just
a fanciful straw man argument. It doesn't actually exist. Why propose
it? There is no such thing as an infinite budget. This post has nothing
to do with an infinite budget. You're misrepresenting this in an
egregious way.
"just trust me and give me an ... money" is isomorphic to "I have x
dollars w/ which to experiments". Isomorphic. The same thing. You're
"different approach" is the same thing I'm suggesting here.


Check out the article &quot;Sensors and Arduino: H...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-08-03 22:00:02.354000-04:00

Check out the article "Sensors and Arduino: How to glue them together"
(url: http://radar.oreilly.com/2012/08/sensors-arduino-htm.html)





