Unit Testing in C
=================

:date: 2009-10-14 11:42
:tags: unit testing,C,#python,tdd,java,JUnit
:slug: 2009_10_14-unit_testing_in_c
:category: Technologies
:status: published

I haven't written new C code since the turn of the millennium. Since
then it's been almost all Java and Python. Along with Java and Python
come JUnit and Python's unittest module.

I've grown completely dependent on unit testing.

I'm looking at some C code, and I want a unit testing framework. For
pure C, I can find things like
`CuTest <http://cutest.sourceforge.net/>`__ and
`CUnit <http://sourceforge.net/projects/cunit/>`__. The documentation
makes them look kind of shabby. Until I remembered what a simplistic
language C is. Considering what they're working with, they're
actually very cool.

I found a helpful posting on `C++ unit testing
tools <http://gamesfromwithin.com/exploring-the-c-unit-testing-framework-jungle>`__.
It provided some insight into C++. But this application is pure C.

I'm interested in replacing the shell script in CuTest with a Python
application that does the same basic job. That's -- perhaps -- a
low-value add-on. Perhaps I should look at CUnit and stay away from
replacing the CuTest shell script with something a bit easier to
maintain.



-----

Have you considered Cgreen?  A few friends have re...
-----------------------------------------------------

Tony Arkles<noreply@blogger.com>

2009-10-14 13:51:28.160000-04:00

Have you considered Cgreen? A few friends have recommended it for C unit
testing, but I haven't had the chance to try it yet.


I have found it easier to write unit tests in C th...
-----------------------------------------------------

Jerry Seutter<noreply@blogger.com>

2009-10-14 14:49:56.980000-04:00

I have found it easier to write unit tests in C than to use Swig.
I use CUnit. It doesn't do much compared to libraries available in
Python, but it is reliable. It is simple enough to keep everything you
need to know in your head.


http://code.google.com/p/test-dept/ may be of inte...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-10-14 15:54:25.615000-04:00

http://code.google.com/p/test-dept/ may be of interest for you.


If you write itr correctly no need for Cunit...
-----------------------------------------------

Unknown<noreply@blogger.com>

2009-10-18 10:44:07.822000-04:00

If you write itr correctly no need for Cunit...


How about doing it in python using something like ...
-----------------------------------------------------

Amit<noreply@blogger.com>

2009-10-14 13:54:29.965000-04:00

How about doing it in python using something like http://www.swig.org/ ?


I think this is an informative post and it is very...
-----------------------------------------------------

saad<noreply@blogger.com>

2019-04-03 14:41:58.747000-04:00

I think this is an informative post and it is very useful and
knowledgeable. therefore, I would like to thank you for the efforts you
have made in writing this article.
`mytecheytricks.simplesite.com <http://mytecheytricks.simplesite.com/>`__





