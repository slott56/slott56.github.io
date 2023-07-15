Shiny New MacBook Pro
=====================

:date: 2014-03-20 08:00
:tags: #python,macosx
:slug: 2014_03_20-shiny_new_macbook_pro
:category: Technologies
:status: published

| Wow. Just Wow. An almost seamless technology change. Almost.
| The old MacBook Pro (dual core 4Gb RAM) was struggling to keep up.
  Struggling. It had been dropped once, so there was a ding in the
  corner. The trackpad "click" wasn't reliably clicking. It was shaky.
| Nothing that couldn't be cured by a new Bluetooth keyboard and/or
  mouse. Awkward, but cheap.
| Instead, I opted for a new quad-core 8Gb MacBook Pro.
| Hence the Wow.
| Here's how the upgrade worked.
| I logged in once in the Apple Store to create an "Administrator"
  account. That's **Not Me**, but it allowed me to configure and
  register the machine.
| Go Home.
| 1. Finish the last Time Machine backup of the old machine.
| 2. Move the Time Machine device to the new machine.
| 3. Use the Migration Assistant to recover everything from the old
  machine. There was 300+ Gb of stuff, so it took a few hours.
  Completely hands-off. Completely successful the first time.
| Turn on WiFi (it's not always on for me, the story is
  `complicated <http://www.itmaybeahack.com/TeamRedCruising/travel-2013-2014/>`__;
  it involves going to a coffee shop.)
| **Almost** everything is perfectly normal and usable on the new
  machine.
| `1Password <https://agilebits.com/onepassword>`__ wanted me to login
  to the App Store to be sure the licenses were all up-to-snuff.
| `DropBox <http://www.dropbox.com/>`__ wanted me to login again to
  their server.
| `GPSNavX <http://www.gpsnavx.com/>`__ needs a license key. Their keys
  are delightfully short, but apparently encode a date or something and
  can't be reused easily.
| `Python3.3 <http://www.python.org/>`__ was -- of course -- a
  non-starter. Not surprising, really, since it's not an "app" that can
  be moved neatly by Mac OS X Migration Assistant.
| The Python download and install was painless. The `ActiveState
  ActiveTcl <http://www.activestate.com/activetcl>`__ is also important
  because I do use tinter and IDLE. The Python page is very explicit
  about the `correct release of ActiveTcl for Mac OS
  X <http://www.python.org/download/mac/tcltk/>`__. And I still did it
  wrong the first time.

   *while the ActiveState web site refers to 8.5.15.0, the installer dmg
   link has been updated to download ActiveTcl 8.5.15.1.*

| Today's job, then, is to put
  `setuptools <https://pypi.python.org/pypi/setuptools>`__
  (easy_install) and pip onto this Mac and begin the process of figuring
  out what's missing that I really use. I install a fair amount of stuff
  experimentally; stuff I don't really want or need.  And I always
  install it "for real" in Python's site-packages because I'm too lazy
  to simply download the Git repository and update the PYTHONPATH
  manually.
| We're talking about
  `docutils <https://pypi.python.org/pypi/docutils/0.11>`__,
  `Sphinx <https://pypi.python.org/pypi/Sphinx/1.2.2>`__,
  `Django <https://pypi.python.org/pypi/Django/1.6.2>`__,
  `Jinja2 <https://pypi.python.org/pypi/Jinja2>`__, and
  `SQLAlchemy <https://pypi.python.org/pypi/SQLAlchemy/0.9.3>`__. To get
  started. PyYAML and PIL are probably required, but I'll wait until I
  need them.





