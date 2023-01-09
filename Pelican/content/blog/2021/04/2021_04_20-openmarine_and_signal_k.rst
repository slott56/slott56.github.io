OpenMarine and Signal-K
=======================

:date: 2021-04-20 08:00
:tags: arduino,#python,CircuitPlayground,boat,IoT,RaspberryPi
:slug: 2021_04_20-openmarine_and_signal_k
:category: Technologies
:status: published

I heard about these less than a week ago.

-  https://openmarine.net/openplotter
-  https://github.com/openplotter/pypilot
-  https://signalk.org/installation.html

This is very interesting. Very interesting.

I have a partially complete IoT anchor alarm.

The idea of leveraging the boat's other devices through a Signal-K
interface is appealing.

The problem is, I don't want the power draw.

I think I want to continue on the path of a small, thrifty, stand-alone
device that can be used when the rest of the boat's systems are mostly
shut down.

However. Seeing these projects causes me to rethink my use of Arduino
and C++. While the Arduino is the thriftiest possible device -- the
power consumption is negligible -- I think that a small upgrade to a
Python-based device might make the software a tiny bit simpler.

An Arduino Uno, specifically, is just barely capable of the UX I was
hoping to build. The two-line LCD with a "mark" push-button, an "anchor
circle" knob, and a "display page" button is right at the limit; I'm
using analog inputs instead of digital for the buttons.

A Raspberry Pi can support more sophisticated displays, at some cost in
power consumption. An e-ink display might be a better choice than the
two-line LCD because -- well -- anchoring details change slowly.  Once
you've drifted too far (or have a consistent COG away from the marked
point with a steadily growing distance) then the alarm sounds and the
display is more-or-less irrelevant. You're going to get up, and eyeball
the situation to see what's going on. Wether or not the display updates
doesn't matter much.

We haven't drifted very often, so I don't have too much data.

#. Once we slid to a new position. It was a stormy, blowy day. We eased
   out more scope. And we never moved again. We stood on deck, taking
   visual bearings. An e-ink display of the details wasn't what we
   depended on.
#. We used to rely on an iPhone app to monitor our position. (We've
   switched to using SafeAnchor, we used to use an older app, no longer
   available.) We were moving slowly, but steadily. It was during a
   hurricane, we weren't surprised. We started the engine, raised the
   anchor and motored to a new place to reset. Again, we weren't using
   the display on the phone, we were looking at Pungo creek.
#. And once we were not on the boat when she moved. That would have been
   awkward for our neighbors. So. We'd need to have a "reset the anchor
   alarm" switch in the cockpit. This would mark a new position. Fatty
   Goodlander's advice is to leave a big sign with a string showing them
   where it is.

A full 1.0 knot of speed is 1.7 feet per second. We often have 50 feet
of line, meaning any movement under 100' is likely ordinary boat motion.
That means 30 seconds until we're suspicious of a problem, and a full
minute before we must sound the alarm. (In the middle, a constant COG
and increasing distance is a leading indicator of trouble; alarm chirps
might be helpful.)

As intermediate data gathering format, the Signal-K data stream is
appealing. It steps away from the NMEA GPS talker messages. It's
heavy-going for an Arduino Uno. But. Might work out well on something a
little bigger.





