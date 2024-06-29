Python Unit Testing Frameworks (v3)
===================================

:date: 2005-11-02 00:12
:tags: unit testing
:slug: 2005_11_02-python_unit_testing_frameworks_v3
:category: Python
:status: published





Ned Batchelder : Blog [http://www.nedbatchelder.com/blog/index.html ] identifies no less than 6 unit testing
frameworks for Python [http://www.nedbatchelder.com/blog/200510.html#e20051025T070731 ] and [http://www.nedbatchelder.com/blog/200411.html#e20041120T185622 ].



TestGears
[http://www.turbogears.com/testgears/ ] is part of the TurboGears web
uber-framework. It provides automatic discovery of test functions, simplifies
suite development, and makes it easy to run tests zero configuration.  Kevin
Dangoor [http://www.blueskyonmars.com/ ] says he will deprecate this in favor of
Nose.  David Warnock [http://42.blogs.warnock.me.uk/2005/10/turbogears_cont.html ] says something
similar.

TestOOB [http://testoob.sourceforge.net/ ]
(Testing Out Of [the] Box) provides for new styles of output (HTML and color
terminal), debugger launching, verbose asserts, parallel execution, and
command-line utility testing

nose [http://somethingaboutorange.com/mrl/projects/nose/ ] provides an alternate test discovery and
execution engine for unittest

unittest [http://docs.python.org/lib/module-unittest.html ], formerly known as PyUnit [http://pyunit.sourceforge.net/ ]
(Thanks for the heads up, Tony [http://www.haloscan.com/comments/slott/E20051105152154/#29209 ])

doctest
[http://docs.python.org/lib/module-doctest.html ]


py.test [http://codespeak.net/py/current/doc/test.html ]



Michal
Watkins [http://mikewatkins.net/ ] adds  Sancho, a unit testing framework
[http://www.mems-exchange.org/software/sancho/ ].

Also,
ZOPE has test.py [http://zopewiki.org/HowToRunZopeUnitTests ].  There is a derivative product, also, the
SchoolTool Test Runner [http://svn.nuxeo.org/trac/pub/file/CalCore/trunk/test.py ].



Jeremy
Hylton's blog has some notes [http://www.python.org/~jeremy/weblog/031014.html ] on unit testing, describing
test.py.

Ian Bicking also has a list of
complaints about the basic unittest interface [http://blog.colorstudy.com/ianb/weblog/2003/10/10.html#P11 ], many of which are answered by the
add-ons.








