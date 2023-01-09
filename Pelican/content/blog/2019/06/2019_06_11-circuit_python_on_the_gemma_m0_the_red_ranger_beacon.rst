Circuit Python on the Gemma M0 -- The Red Ranger Beacon
=======================================================

:date: 2019-06-11 08:00
:tags: Gemma,#python,CircuitPlayground,IoT
:slug: 2019_06_11-circuit_python_on_the_gemma_m0_the_red_ranger_beacon
:category: Technologies
:status: published


PyCon 2018 Swag included a Gemma m0.
(https://www.adafruit.com/product/3501)

PyCon 2019 Swag included a Circuit Playground Express.
See https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart.

Both of these are (to me) amazing. They mount as USB devices; there’s
a code.py file that’s automatically run when the board restarts.

The Gemma has fairly few pins and does some real simple things.  The
CPX has a bunch of pins and ton of hardware on the board. Buttons,
Switches, LED’s, motion sensor, temperature, brightness... I’ve lost
count.

Step 1 -- Get Organized
-----------------------


Create a proper project directory on your local machine. Yes, you can
hack the ``code.py`` file immediately, but you should consider making
a backup before you start making changes.

Few things are more frustrating than making a mistake and being unable
to restore the original functionality as a check to be sure things are
still working.

Also. At some point, you'll want to upgrade the OS on the chip. This
will require you to have a bootable image. The process isn't complex,
but it does require some care.
See https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython#download-the-latest-version-3-4
for downloading a new OS.

So. Step 1a. Create a local folder for your projects. Within that
folder, create a folder for each project. Put the relevant code.py
into the sub-folder. Like this

::

   gemma
    ┣━━ baseline
    ┃   ┗━━ code.py
    ┣━━ my-first-project
    ┃   ┗━━ code.py
    ┣━━ another-project
    ┃   ┗━━ code.py
    ┗━━ os-upgrade
        ┗━━ other files...





See https://learn.adafruit.com/adafruit-gemma-m0/troubleshooting for
additional help if you have a Windows PC.

Step 2 -- Start Small
----------------------

Tweak a few things in the supplied ``code.py`` if you're new to IoT
stuff.

A lot of folks like the Mu editor for
this. `https://codewith.mu <https://codewith.mu/>`__.
I like using BBEdit. https://www.barebones.com/products/bbedit/.  To
make this work I \*also\* need to have

-  a terminal window open so I can use the Mac OS **screen**
   application, and

-  a finder window open to copy the code.py from my PC to the Gemma
   M0.

This is a lot of busy screen real-estate with three separate apps
open. It's not for everyone. I like it because there's little
hand-holding. You may prefer Mu.

It's important to go through the edit/download/play cycle many times
to be sure you're clear on what code's on your PC and what code's on
your board.

It's even more important to see how you're forced to debug syntax
errors using the **screen** app until you invent a suitable mock
library for off-line unit testing.

Step 3 -- Plan Carefully
-------------------------

The version of Python is remarkably complete.
However.

It's also a very small processor, with very few pins, so you can't do
anything super elaborate.  You can, however, do quite a bit.
See `Nina Zakharenko - Keynote - PyCon
2019 <https://www.youtube.com/watch?v=35mXD40SvXM>`__ for some
inspiration

Step 4 -- Check This Out
------------------------

https://github.com/slott56/gemma-boat-beacon
Many thanks to @nnja for showing us some elegant, inspirational
ideas.







