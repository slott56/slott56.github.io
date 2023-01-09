Audio Synth [Updated]
=====================

:date: 2015-08-30 09:32
:tags: mac os x,#python,pyaudio
:slug: 2015_08_30-audio_synth_updated
:category: Technologies
:status: published

| I learned about synthesizers in the '70's using a Moog analog device.
  Epic coolness.
| Nowadays, everything is digital. We use wave tables and (relatively)
  simple additive synth techniques.
| I made the mistake of reading about Arduino wave table synthesis:
| http://learning.codasign.com/index.php?title=Wavetable_Synthesis
| http://makezine.com/projects/make-35/advanced-arduino-sound-synthesis/
| http://playground.arduino.cc/Main/ArduinoSynth
| The idea of an Arduino alarm that uses a chime instead of a harsh buzz
  is exciting. The tough part about this is building the wave tables.
| What a perfect place to use Python: we can build wave tables that can
  be pushed down to the Arduino. And test them in the Python world to
  adjust the frequency spectrum and the complex envelope issues around
  the various partials.
| See http://computermusicresource.com/Simple.bell.tutorial.html
| Except.
| Python3.4 doesn't have
  `PyAudio <https://people.csail.mit.edu/hubert/pyaudio/index.html>`__
  support.
| Yet.
| Sigh. Before I can work with Arduino wave tables, I'll have to start
  by figuring out how to build PyAudio for Python 3.4 on Mac OS X.
| Look here: http://people.csail.mit.edu/hubert/git/pyaudio.git for the
  code.
| Look here for the secret to building this on Mac OS X:
  https://stackoverflow.com/questions/2893193/building-portaudio-and-pyaudio-on-mac-running-snow-leopard-arch-issues/2906040#2906040.
| Summary.

#. Get pyaudio source.
#. Inside pyaudio create a portaudio-v19. Get the portaudio source and
   put it here.
#. Inside pyaudio/pyaudio, do ./config; make and sudo make install
#. Inside pyaudio, do python3.4 setup.py install --static-link





