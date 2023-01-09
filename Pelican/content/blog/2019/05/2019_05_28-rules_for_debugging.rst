Rules for Debugging
===================

:date: 2019-05-28 14:34
:tags: passive-aggressive programmer,Programming Languages
:slug: 2019_05_28-rules_for_debugging
:category: Technologies
:status: published

| Here's the situation.
| Someone wrote code. It didn't do what they assumed it would do.
| They come to me for help.
| Here are my rules for debugging. All of them.
| 1. Try something else.

--------------

| 
| I don't have any other or more clever advice. When I look at someone's
  broken code, I'm going to suggest the only thing I know. Try something
  else.
| I can't magically make broken code work. Code's not like that. If it
  doesn't work, it's wrong, usually in a foundational way. Usually, the
  author made an assumption, followed through on that assumption, and
  was astonished it didn't work.
| A consequence of this will be **massive** changes to the broken code.
  Foundational changes.

   When you make an assumption, you make an "ass" out of "u" and
   "mption".

| 
| Debugging is a matter of finding and discarding assumptions. This can
  be hard. Some people think their assumptions are solid gold and write
  long angry blog posts about how a language or platform or library is
  "broken."
| The rest of us try something different.
| My personal technique is to cite evidence for everything I think I'm
  observing. Sometimes, I actually write it down -- on paper -- next to
  the computer. (Sometimes I use the Mac OS Notes app.) Which lines of
  code. Which library links. Sometimes, i'll include in the code as
  references to documentation pages.
| Evidence is required to destroy assumptions. Destroying assumptions is
  the essence of debugging.

Sources of Assumptions
----------------------

| I'm often amazed at how many people don't read the "But on Windows..."
  parts of the Python documentation. Somehow, they're willing to assume
  -- without evidence -- that Windows is POSIX-compliant and behaves
  like Linux. When things don't follow their assumed behavior, and
  they're using Windows, it often seems like they've compounded a bunch
  of personal assumptions. I don't have too much patience at this point:
  the debugging is going to be hard.
| I'm often amazed that someone can try to use
  multiprocessing.apply_async() without reading any of the `example
  code <https://docs.python.org/3.7/library/multiprocessing.html#using-a-pool-of-workers>`__.
  What I'm guessing is that assumptions trump research, making them
  solid gold, and not subject to questioning or locating evidence. In
  the case of multiprocessing, it's important to look at code which
  appears broken and compare it, line-by-line with example code that
  works.
| Comparing broken code with relevant examples is -- in effect -- trying
  something else. The original didn't work. So... Go to something that
  does work and compare the two to identify the differences.



-----

Thanks for sharing for more <a href="https://kazaf...
-----------------------------------------------------

best android cell<noreply@blogger.com>

2019-07-31 07:14:23.474000-04:00

Thanks for sharing for more `Django Python
Tutorial <https://kazafi.com/django-python-tutorial/%22>`__


Thank you for this informative post. 
<a href="htt...
-----------------------------------------------------

Rajani<noreply@blogger.com>

2019-08-21 03:43:14.682000-04:00

Thank you for this informative post.
`AWS
Training <https://www.visualpath.in/amazon-web-services-aws-training.html>`__
`AWS Online
Training <https://www.visualpath.in/amazon-web-services-aws-training.html>`__





