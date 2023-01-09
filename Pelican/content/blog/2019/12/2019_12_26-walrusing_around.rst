Walrusing Around
================

:date: 2019-12-26 12:00
:tags: walrus,#python
:slug: 2019_12_26-walrusing_around
:category: Technologies
:status: published

| This is -- well -- it is what it is. I don't have to like it.

::

   >>> t_s = (8063599, 0)
   >>> fields = [(t_s := divmod(t_s[0], b))[1] for b in (60, 60, 24, 7)]
   >>> list(reversed(fields + [t_s[0]]))
   [13, 2, 7, 53, 19]

| 
| It works and shows how the assignment operator works.
| The point here is to convert a timestamp into ISO week, day, hour,
  minute, second. 13th week, 2nd day, 7h, 53m, 19s.
| The divmod() function returns a two-tuple, which the assignment
  operator can't decompose. Instead, we decompose it by wrapping the
  whole thing in ()[1].
| Works.
| Do Not Recommend.



-----

Black fails to format over-length line containing ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-12-27 14:45:40.359000-05:00

Black fails to format over-length line containing walrus operator
https://github.com/psf/black/issues/1194





