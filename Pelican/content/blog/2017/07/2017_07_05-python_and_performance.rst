Python and Performance
======================

:date: 2017-07-05 09:48
:tags: performance,#python
:slug: 2017_07_05-python_and_performance
:category: Technologies
:status: published

Real Question:


   One of the standard problems that keeps coming up over and over is
   the parsing of url's. A sub-problem is the parsing of domain and
   sub-domains and getting a count.

   For example

   https://www.theatlantic.com/video/index/374880/living-alone-on-a-sailboat/

   It would be nice to parse the received file and get counts like

   .com had 15,323 count

   .google.com had 62 count

   .theatlantic.com had 33 count

   The first code snippet would be in Python and the other code snippet
   would be in C/C++ to optimize for performance.




Yes. They did not even try to look in the standard library for
urllib.parse. The general problem has already been solved; it can be
exploited in a single line of code.

The line can be long-ish, so it can help to use a lambda to make it a
little easier to read. The code is below.

The C/C++ point about "optimize for performance" bothers me to no end.
Python isn't very slow. Optimization isn't **required**.

I made 16,000 URL's. These were not utterly random strings, they were
random URL's using a pool of 100 distinct names. This provides some
lumpiness to the data. Not real lumpiness where there's a long tail of
1-time-only names. But enough to exercise collections.Counter and
urllib.parse.urlparse().

Here's what I found. Time to parse 16,000 URLs and pluck out the last
two levels of the name?

::

    CPU times: user 154 ms, sys: 2.18 ms, total: 156 ms

    Wall time: 157 ms

32,000?

::

    CPU times: user 295 ms, sys: 6.87 ms, total: 302 ms

    Wall time: 318 ms

At that pace, why use C?

I suppose one could demand more speed just to demand more speed.

Here's some code that can be further optimized.

::

   top = lambda netloc: '.'.join(netloc.split('.')[-2:])
   random_counts = Counter(top(urllib.parse.urlparse(x).netloc) for x in random_urls_32k)




The slow part of this is the top() function. Using rsplit('.',
maxsplit=2) might be better than split('.'). A smarter approach might
be find all the "." and slice the substring from the next-to-last one.
Something like this, netloc[findall('.', netloc)[-2]:], assuming a
findall() function that returns the locations of all '.' in a string.

Of course, if there is a problem, using a numpy structure might speed
things up. Or use `dask <http://dask.pydata.org/en/latest/>`__ to farm
the work out to multiple threads.





