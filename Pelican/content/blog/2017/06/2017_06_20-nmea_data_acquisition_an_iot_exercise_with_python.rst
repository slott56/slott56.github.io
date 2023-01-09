NMEA Data Acquisition -- An IoT Exercise with Python
====================================================

:date: 2017-06-20 08:00
:tags: #python,IoT,internet of things,nmea
:slug: 2017_06_20-nmea_data_acquisition_an_iot_exercise_with_python
:category: Technologies
:status: published


Here's the code: https://github.com/slott56/NMEA-Tools. This is Python
code to do some Internet of Things (IoT) stuff. Oddly, even when
things connected by a point-to-point serial interface, it's still
often called IoT. Even though there's no "Internetworking."

Some IoT projects have a common arc: exploration, modeling, filtering,
and persistence. This is followed by the rework to revise the data
models and expand the user stories. And then there's the rework
conundrum. Stick with me to see just how hard rework can be.

What's this about? First some background. Then I'll show some code.

Part of the back story is here:
http://www.itmaybeahack.com/TeamRedCruising/travel-2017-2018/that-leaky-hatch--chartplot.html

In the Internet of Things Boaty (IoT-B) there are devices called
chart-plotters. They include GPS receivers, displays, and controls.
And algorithms. Most important is the merging of GPS coordinates and
an active display. You see where your boat is.

Folks with GPS units in cars and on their phones have an idea core
feature set of a chart plotter. But the value of a chart plotter on a
boat is orders of magnitude above the value in a car.

At sea, the hugeness and importance of the chartplotter is magnified.
The surface of the a large body of water is (almost) trackless. Unless
you're really familiar with it, it's just water, generally opaque. The
depths can vary dramatically. A shoal too shallow for your boat can be
more-or-less invisible and just ahead. Bang. You're aground (or worse,
holed.)

A chart -- and knowledge of your position on that chart -- is a
**very** big deal. Once you sail out of sight of land, the chart
plotter becomes a life-or-death necessity. While I can find the North
American continent using only a compass, I'm not sure I could find the
entrance to Chesapeake Bay without knowing my latitude. (Yes, I have a
sextant. Would I trust my life to my sextant skills?)

Modern equipment uses modern hardware and protocols. `N2K (NMEA
2000) <http://www.boat-project.com/tutorials/nmea2000.htm>`__, for
example, is powered Ethernet connectivity that uses a simplified
backbone with drops for the various devices. Because it's Ethernet,
they're peers, and interconnection is simplified.
See `http://www.digitalboater.com <http://www.digitalboater.com/>`__
for some background.

The Interface Issue
-------------------


The particularly gnarly problem with chart plotters is the lack of an
easy-to-live-with interface.

They're designed to be really super robust, turn-it-on-and-it-works
products. Similar to a toaster, in many respects. Plug and play. No
configuration required.

This is a two-edged sword. No configuration required bleeds into no
configuration possible.

The Standard Horizon CP300i uses `NT
cards <https://en.wikipedia.org/wiki/NT_Card>`__. Here's a reader
`device <http://www.landfallnavigation.com/ee86002.html>`__. Note the
"No Longer Available" admonition. All of my important data is saved to
the NT card. But. The card is useless except for removable media
backup in case the unit dies.

What's left? The NMEA-0183 interface wiring.

NMEA Serial EIA-422
-------------------


The good news is that the NMEA wiring is carefully documented in the
CP300i owner's manual. There are products like this `NMEA-USB
Adaptor <http://www.digitalyachtamerica.com/index.php/en/products/interfacing/nmeausb/product/67-usb-to-nmea-adaptor>`__.
A few wire interconnections and we can -- at least in principle --
listen to this device.

The NMEA standard was defined to allow numerous kinds of devices to
work together. When it was adopted (in 1983), the idea was that a
device would be a "talker" and other devices would be "listeners." The
intent was to have a lot of point-to-point conversations: one talker
many listeners.

A digital depth meter or wind meter, for example, could talk all day,
pushing out message traffic with depth or wind information. A display
would be a listener and display the current depth or wind state.

A centralized multiplexer could collect from multiple listeners and
then stream the interleaved messages as a talker. Here's `an
example <https://www.navstore.com/noland-engineering-am43-nmea-0183-hi-speed-multiplexer-usb.html>`__.
This would allow many sensors to be combined onto a single wire. A
number of display devices could listen to traffic on the wire, pick
out messages that made sense to them, and display the details.

Ideally, if every talker was polite about their time budget, hardly
anything would get lost.

In the concrete case of the CP300i, there are five ports. usable in
various combinations. There are some restrictions that seem to
indicate some hardware sharing among the ports. The product literature
describes a number of use cases for different kinds of
interconnections including a computer connection.

Since NMEA is EIA-422 is RS-232, some old computer serial ports could
be wired up directly. My boat originally had an ancient Garmin GPS and
an ancient windows laptop using an ancient DB-9 serial connector. I
saved the data by copying files off the hard drive and threw the
hardware away.

A modern Macintosh, however, only handles USB. Not direct EAI-422
serial connections. An adaptor is required.

What we will have, then, is a CP300i in talker mode, and a MacBook Pro
(Retina, 13-inch, Late 2013) as listener.

Drivers and Infrastructure
--------------------------


This is not my first foray in the IoT-B world. I have a
`BU-353 <http://usglobalsat.com/s-122-bu-353-support.aspx>`__ GPS
antenna. This can be used directly by the GPSNavX application on the
Macintosh. On the right-ish side of the BU-353 page are **Downloads**.
There's a USB driver listed here. And a GPS Utility to show position
and satellites and the NMEA data stream.

Step 1. Install this USB driver.

Step 2. Install the MAC OS X GPS Utility. I know the USB interface
works because I can see the BU-353 device using this utility.

Step 3. Confirm with GPSNavX. Yes. The chart shows the little boat
triangle about where I expect to be.

Yay! Phase I of the IoT-B is complete. We have a USB interface. And we
can see an NMEA-0183 GPS antenna. It's transmitting in standard 4800
BAUD mode. This is the biggest hurdle in many projects: getting stuff
to talk.

In the project Background section on Git Hub, there's a `wiring
diagram <https://slott56.github.io/NMEA-Tools/background.html#nmea-hardware-interface>`__
for the USB to NMEA interface.

Also, the
`Installation <https://slott56.github.io/NMEA-Tools/installation.html>`__
section says install pyserial. https://pypi.python.org/pypi/pyserial.
This is essential to let Python apps interact with the USB driver.

Data Exploration
----------------


Start here: `NMEA Reference
Manual <https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf>`__.
This covers the bases for the essential message traffic nicely. The
full NMEA standard has lots of message types. We only care about a few
of them. We can safely ignore the others.

As noted in the project
`documentation <https://slott56.github.io/NMEA-Tools/background.html>`__,
there's a relatively simple message structure. The messages arrive
more-or-less constantly. This leads to an elegant Pythonic design: an
Iterator.

We can define a class which implements the iterator protocol
(\__iter__() and \__next__()) that will consume lines from the serial
interface and emit the messages which are complete and have a proper
checksum. Since the fields of a message are comma-delimited, might as
well split into fields, also.

It's handy to combine this with the context manager protocol
(\__enter__() and \__exit__()) to create a class that can be used like
this.

::

       with Scanner(device) as GPS:
           for sentence_fields in GPS:
               print(sentence_fields) 


 

This is handy for watching the messages fly past. The fields are kind
of compressed. It's a light-weight compression, more like a lack of
useful punctuation than proper compression.

Consequently, we'll need to derive fields from the raw sequences of
bytes. This initial exploration leads straight to the next phase of
the project.

Modeling
--------


We can define a data model for these sentences using a Sentence class
hierarchy. We can use a simple Factory function to emit Sentence
objects of the appropriate subclass given a sequence of fields in
bytes. Each subclass can derive data from the message.

The atomic fields seem to be of seven different types.

-  Text. This is a simple decode using ASCII encoding.
-  Latitude. The values are in degrees and float minutes.
-  Longitude. Similar to latitude.
-  UTC date. Year, month, and day as a triple.
-  UTC time. Hour, minute, float seconds as a triple.
-  float.
-  int.


Because fields are optional, we can't naively use the built-in float()
and int() functions to convert bytes to numbers. We'll have to have a
version that works politely with zero-length strings and creates None
objects.

We can define a simple field definition tuple, Field =
namedtuple('Field', ['title', 'name', 'conversion']). This slightly
simplifies definition of a class.

We can define a class with a simple list of field conversion rules.

::

   class GPWPL(Sentence):
       fields = [
           Field('Latitude', 'lat_src', lat),
           Field('N/S Indicator', 'lat_h', text),
           Field('Longitude', 'lon_src', lon),
           Field('E/W Indicator', 'lon_h', text),
           Field("Name", "name", text),        
       ]




The superclass \__init__() uses the sequence of field definitions to
apply conversion functions (lat(), lon(), text()) to the bytes,
populating a bunch of attributes. We can then use s.lat_src to see the
original latitude 2-tuple from the message. A property can deduce the
actual latitude from the s.lat_src and s.lat_h fields.

For each field, apply the function to the value, and set this as an
attribute.

::

           for field, arg in zip(self.fields, args[1:]):
               try:
                   setattr(self, field.name, field.conversion(arg))
               except ValueError as e:
                   self.log.error(f"{e} {field.title} {field.name} {field.conversion} {arg}")




This sets attributes with useful values derived from the bytes
provided in the arguments.

The factory leverages a cool name-to-class mapping built by
introspection.

::

       sentence_class_map = {
           class_.__name__.encode('ascii'): class_ 
           for class_ in Sentence.__subclasses__()
       }
       class_= self.sentence_class_map.get(args[0])




This lets us map a sentence header (b"GPRTE") to a class (GPRTE)
simply. The get() method can use an UnknownSentence subclass as a
default.

Modeling Alternatives
---------------------


As we move forward, we'll want to change this model. We could use a
cooler class definition style, something like this. We could then
iterate of the keys in the class \__dict_\_ to set the attribute
values.

::

   class GPXXX(Sentence):
       lat_src = Latitude(1)
       lat_h = Text(2)
       lon_src = Longitude(3)
       lon_h = Text(4)
       name = Text(5)




The field numbers are provided to be sure the right bunch of bytes are
decoded.

Or maybe even something like this:

::

   class GPXXX(Sentence):
       latitude = Latitude(1, 2)
       longitude = Longitude(3, 4)
       name = Text(5)




This would combine source fields to create the useful value. It would
be pretty slick. But it requires being \*sure\* of what a sentence'
content is. When exploring, this isn't the way to start. The
simplistic list of field definitions comes right off web sites without
too much intermediate translation that can lead to confusion.

The idea is to borrow the format from the `SiRF
reference <https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf>`__ and
start with Name, Example, Unit, and Description in each Field
definition. That can help provide super-clear documentation when
exploring. The http://aprs.gids.nl/nmea/ information has similar
tables with examples. Some of the http://freenmea.net/docs examples
only have names.

The most exhaustive seems to be http://www.catb.org/gpsd/NMEA.html.
This, also, only has field names and position numbers. The conversions
are usually pretty obvious.

Filtering
---------


A talker -- well -- talks. More or less constantly. There are delays
to allow time to listen and time for multiplexers to merge in other
talker streams.

There's a cycle of messages that a device will emit. Once you've
started decoding the sentences, the loop is obvious.

For an application where you're gathering real-time track or
performance data, of course, you'll want to capture the background
loop. It's a lot of data. At about 80 bytes times 8 background
messages on a 2-second cycle, you'll see 320 bytes per second, 19K per
minute, 1.1M per hour, 27.6M per day. You can record **everything**
for 38 days to and be under a Gb.

The upper bound for 4800 BAUD is 480 bytes per second. 41M per day. 25
days to record a Gb of raw data.

For my application, however, I want to capture the data **not** in the
background loop.

It works like this.

#. I start the laptop collecting data.

#. I reach over to the chartplotter and push a bunch of buttons to get
   to a waypoint transfer or a route transfer.

#. The laptop shows the data arriving. The chartplotter claims it's done
   sending.

#. I stop collecting data. In the stream of data are my waypoints or
   routes. Yay!


A reject filter is an easy thing: Essentially it's filter(lambda s:
s._name not in reject_set, source). A simple set of names to reject is
the required configuration for this filter.

Persistence
-----------


How do we save these messages?

We have several choices.

#. Stream of Bytes. The protocol uses \\r\\n as line endings. We could
   (in principle) cat /dev/cu.usbserial-A6009TFG >capture.nmea.
   Pragmatically, that doesn't always work because the 4800 BAUD setting
   is hard to implement. But the core idea of "simply save the bytes"
   works.

#. Stream of Serialized Objects.

   #. We can use YAML to cough out the objects. If the derived
      attributes were all properties, it would have worked out really
      well. If, however, we leverage \__init__() to set attributes, this
      becomes awkward.
   #. We can work around the derived value problems by using JSON with
      our own Encoder to exclude the derived fields. This is a bit more
      complex, than it needs to be. It permits exploration though.

#. GPX, KML, or CSV. Possible, but. These seems to be a separate
   problem.


When transforming data, it's essential to avoid "point-to-point"
transformation among formats. It's crucial to have a canonical
representation and individual converters. In this case, we have NMEA
to canonical, persist the canonical, and canonical to GPX (or KML, or
CSV.)

Rework
------


Yes. There's a problem here.  Actually there are several problems.


#. I got the data I wanted. So, fixing the design flaws isn't
   essential anymore. I may, but... I should have used descriptors.

#. In the long run, I really need a three-way synchronization process
   between computer, new chart plotter and legacy chart plotter.


Let's start with the first design issue: lazy data processing.


The core Field/Sentence design *should* have looked like this:


::

      class Field:
          def __init__(self, position, function, description):
              self.position = position
              self.function = function
              self.description = description
          def __get__(self, object, class_):
              print(f"get {object} {class_}")
              transform = self.function
              return transform(object.args[self.position])

      class Sentence:
          f0 = Field(0, int, "Item Zero")
          f1 = Field(1, float, "Item One")
          def __init__(self, *args):
              self.args = args


This makes all of the properties into lazy computations. It
simplifies persistence because the only real attribute value is the
tuple of arguments captured from the device.

::

      >>> s = Sentence(b'1', b'2.3')
      >>> s.f1
      1
      >>> s.f2
      2.3


 

That would have been a nicer design because serialization would have
been trivial. Repeated access to the fields might have become costly.
We have a tradeoff issue here that depends on the ultimate use case.
For early IoT efforts, flexibility is central, and the computation
costs don't matter. At some point, there may be a focus on
performance, where extra code to save time has merit.

Synchronization is much more difficult. I need to pick a canonical
representation. Everything gets converted to a canonical form.
Differences are identified. Then updates are created: either GPX files
for the devices that handle that, or NMEA traffic for the device which
updated over the wire.

Conclusion
----------


This IoT project followed a common arc: Explore the data, define a
model, figure out how to filter out noise, figure out how to persist
the data. Once we have some data, we realize the errors we made in
our model.

A huge problem is the pressure to ship an MVP (Minimally Viable
Product.) It takes a few days to build this. It's shippable.

Now, we need to rework it. In this case, throw most of the first
release away. Who has the stomach for this? It's essential, but it's
also very difficult.

A lot of good ideas from this blog post are not in the code. And this
is the way a lot of commercial software happens: MVP and move forward
with no time for rework.



-----

Great Article
-----------------------------------------------------

Jackie Co Kad<noreply@blogger.com>

2019-05-28 06:08:55.448000-04:00

Great Article
`Internet of Things Final Year
Project <http://projectcentersinchennai.co.in/Final-Year-Projects-for-CSE/Final-Year-Projects-for-CSE-IOT-Domain>`__
`Final Year Project Centers in
Chennai <http://projectcentersinchennai.co.in>`__





