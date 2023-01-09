The Python Challenge
====================

:date: 2015-01-08 08:00
:tags: #python,learning
:slug: 2015_01_08-the_python_challenge
:category: Technologies
:status: published


See `http://www.pythonchallenge.com <http://www.pythonchallenge.com/>`__

Addicting. For folks (like me) who like this kind of thing. For
others, perhaps just dumb. Or infuriating.

Years ago -- many, many years ago -- I vaguely remember a similar game
with a name like "insanity" or something like that. Now there's
`http://www.notpron.com <http://www.notpron.com/>`__ and
`http://www.weffriddles.com <http://www.weffriddles.com/>`__. All of
these are "show the page source" HTML games. These games are a kind of
steganography: the page your browser renders isn't what you need to
see.

What's important about the Python Challenge is that it's not
specifically about Python. Any programming language would do. Although
I suspect that folks who don't know Python will have a difficult time
with some of the puzzles. I found that having
`Pillow <https://pypi.python.org/pypi/Pillow/>`__ was essential for
problems 7 and 11. I'm sure there are packages as powerful as
PIL/Pillow for other languages.

Also, one of the hints included dated Python 2.7 code. The rest of the
problems, however, seem to fit perfectly well with Python 3.4.

I wasted a morning getting to challenge 11. It was a ton of fun.

Challenge 12 was the first of the show-stoppers. The hint "evil1.jpg"
is beyond subtle. Let me add this hint: This is the first puzzle where
the pictures have digits. Perhaps there are related pictures.

I spent hours studying and rearranging and filtering and enhancing
evil1.jpg before I finally broke down and searched for a hint. The
hint -- of course -- included the whole solution, so I had to skim the
code to figure out what I'd missed.


Challenges 14, 15, and 16 require additional hints, also. 14, for
example, needs a reminder that the pixels need to be spiraled.
Challenge 15 barely requires minimal programming and a lot of Google
searching for famous people's birthdays. Challenge 16's hint is as
opaque as the picture. It involves restructuring the image. But. I had
to resort to reading more of the
http://intelligentgeek.blogspot.com/2006/03/python-challenge-16-ahh-i-finally.html
than for other problems.

I have chapters to review. I really shouldn't be playing around with
silliness like this.

In spite of that, let me just say, that reading about the
"Look-and-Say" sequence was a bunch of fun.

See http://oeis.org/A005150. Whatever you do, avoid reading
this: http://archive.lib.msu.edu/crcmath/math/math/c/c671.htm; it
won't help you with the Python Challenge at all. But it's interesting.
And a huge time-waster. This particular challenge was more like
`Project Euler <https://projecteuler.net/>`__ problems. [*Project
Euler is back up and running, BTW*.]

Here's my variation on the Conway sequence theme:

::

   def say( digits ):

       def run_lengths(digits):
           d_iter= iter(digits)
           c, d0 = 1, next(d_iter)
           for d in d_iter:
               if d0 == d:
                   c += 1
               else:
                   yield str(c)+d0
                   c, d0= 1, d
           yield str(c)+d0

       return "".join(run_lengths(digits))




I'm a fan of generator functions. A big fan.

The interesting part is that we can do run-length encoding for the
look-and-say function relatively simply using the "buffered generator"
design pattern.

1. Seed the buffer with the head of the sequence, next(d_iter)

2. For each item in the tail of the sequence:

    a. If it matches, count.

    b. If it doesn't match, yield the interim reduction and reset the counter.

3. Yield the tail reduction.

This design pattern seems to occur in a number of contexts outside
games and abstract math.





