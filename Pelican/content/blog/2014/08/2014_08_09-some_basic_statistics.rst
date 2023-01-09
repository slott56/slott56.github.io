Some Basic Statistics
=====================

:date: 2014-08-09 11:45
:tags: algorithm,#python
:slug: 2014_08_09-some_basic_statistics
:category: Technologies
:status: published

| I've always been fascinated by the essential statistical algorithms.
  While there are numerous statistical libraries, the simple measures of
  central tendency (mean, media, mode, standard deviation) have some
  interesting features.
| Well.  Interesting to me.
| First, some basics.

::

   def s0( samples ):
       return len(samples) # sum(x**0 for x in samples)

   def s1( samples ):
       return sum(samples) # sum(x**1 for x in samples)

   def s2( samples ):
       return sum( x**2 for x in samples )

| 
| Why define these three nearly useless functions? It's the cool factor
  of how they're so elegantly related.
| Once we have these, though, the definitions of mean and standard
  deviation become simple and kind of cool.

::

   def mean( samples ):
       return s1(samples)/s0(samples)

   def stdev( samples ):
       N= s0(samples)
       return math.sqrt((s2(samples)/N)-(s1(samples)/N)**2)

| 
| It's not much, but it seems quite elegant. Ideally, these functions
  could work from iterables instead of sequence objects, but that's
  impractical in Python. We must work with a materialized sequence even
  if we replace len(X) with sum(1 for \_ in X).
| The next stage of coolness is the following version of Pearson
  correlation. It involves a little helper function to normalize
  samples.

::

   def z( x, μ_x, σ_x ):
       return (x-μ_x)/σ_x

| 
| Yes, we're using Python 3 and Unicode variable names.
| Here's the correlation function.

::

   def corr( sample1, sample2 ):
       μ_1, σ_1 = mean(sample1), stdev(sample1)
       μ_2, σ_2 = mean(sample2), stdev(sample2)
       z_1 = (z(x, μ_1, σ_1) for x in sample1)
       z_2 = (z(x, μ_2, σ_2) for x in sample2)
       r = sum( zx1*zx2 for zx1, zx2 in zip(z_1, z_2) )/len(sample1)
       return r

| 
| I was looking for something else when I stumbled on this "sum of
  products of normalized samples" version of correlation. How cool is
  that? The more text-book versions of this involve lots of sigmas and
  are pretty bulky-looking. This, on the other hand, is really tidy.
| Finally, here's least-squares linear regression.

::

   def linest( x_list, y_list ):
       r_xy= corr( x_list, y_list )
       μ_x, σ_x= mean(x_list), stdev(x_list)
       μ_y, σ_y= mean(y_list), stdev(y_list)
       beta= r_xy * σ_y/σ_x
       alpha= μ_y - beta*μ_x
       return alpha, beta

| 
| This, too, was buried at the end of the Wikipedia article. But it was
  such an elegant formulation for least squares based on correlation.
  And it leads to a tidy piece of programming. Very tidy.
| I haven't taken the time to actually measure the performance of these
  functions and compare them with more commonly used versions.
| But I like the way the Python fits well with the underlying math.
| Not shown: The doctest tests for these functions. You can locate
  sample data and insert your own doctests. It's not difficult.





