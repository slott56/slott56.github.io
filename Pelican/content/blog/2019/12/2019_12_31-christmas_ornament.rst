Christmas Ornament
==================

:date: 2019-12-31 08:00
:tags: #python,CircuitPlayground
:slug: 2019_12_31-christmas_ornament
:category: Technologies
:status: published

See https://github.com/slott56/cpx-xmas-ornament
You'll need a Circuit Playground Express
https://www.adafruit.com/product/3333
Install the code. Enjoy the noise and blinky lights.
The MML translation isn't as complete as you might like. The upper/lower
case for the various commands isn't handled quite as cleanly as it could
be. AFAIK, case shouldn't matter, but I omitted any lower() functions,
making the  MML parser case sensitive. It only mattered for one of the
four songs, and it was easier to edit the song.
The processing leaves a great deal of "clickiness" in the start_tone()
processing. I think I know how to address it.
There are barely 96 or so different tones available in MML compositions.
It might be possible to generate the wave shapes in advance to have a
smoother music experience.
One could image having an off-line translator to transform the MML text
into a sequence of bytes with note number and duration. This would
slightly compress the song, but would speed up processing by eliminating
the overhead of parsing.
Additionally, having 96 wave tables could speed up tone production. The
tiny bit of time to recompute the sine wave at a given frequency would
be eliminated. But. Memory is limited.





