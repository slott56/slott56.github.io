Audio Synth in Python 3.4, Part II
==================================

:date: 2015-09-01 17:59
:tags: #python,pyaudio,pysynth
:slug: 2015_09_01-audio_synth_in_python_34_part_ii
:category: Technologies
:status: published

See `Audio Synth <{filename}/blog/2015/08/2015_08_30-audio_synth_updated.rst>`__.

At first, I imagined the problem was going to be
`PyAudio <https://people.csail.mit.edu/hubert/pyaudio/>`__. This package
has a bunch of installers. But the installers don't recognize Python
3.4, so none of them work for me. The common fallback plan is to install
from source, but, I couldn't find the source. That looks like a problem.

Once I spotted this: "% git clone http://people.csail.mit.edu/hubert/git/pyaudio.git", things were
much better.  I built the PortAudio library. I installed PyAudio for
Python3.4. Things are working. Noises are happening.

Next step is actual synth.

In the past, I have played
with `pysynth <http://mdoege.github.io/PySynth/>`__ because it has some
examples of wave-table additive synth. That's very handy. The examples
are hard to follow because a lot of the synth ideas are conflated into
small functions.

Complication: The pysynth package is Python2. It lacks even the simple
from \__future_\_ import print_function to make it attempt Python3
compatibility.

The pysynth.play_wav module could be a handy wrapper around various
audio playback technologies, include pyaudio. It has to be tweaked,
however, to make it work with Python3.4. I really need to clone the
project, make the changes, and put in a pull request.

The pysynth.pysynth and pysynth.pysynth_beeper modules are helpful for
seeing how wave tables work.  How much rework to make these work with
Python3.4? And how much reverse engineering to understand the math?

I've since found `pyo <https://code.google.com/p/pyo/>`__. Which is also
Python 2. See the `AjaxSoundStudio <http://ajaxsoundstudio.com/software/pyo/>`__ pages for
details. This may be a better example of wave tables. But it's still
Python2. More investigation to follow.

The good news is that there's some forward motion.





