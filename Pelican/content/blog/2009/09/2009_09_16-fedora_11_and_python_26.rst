Fedora 11 and Python 2.6
========================

:date: 2009-09-16 16:13
:tags: #python
:slug: 2009_09_16-fedora_11_and_python_26
:category: Technologies
:status: published

Upgraded a VM to Fedora 11 recently.

This -- it turns out -- comes with Python 2.6 installed.

It is, however, an incomplete build. To do anything, I had to install
a some additional Python packages. Specifically, the "libraries and
header files needed for Python development". Also, IIRC, the tkinter
package isn't present by default.

Once I had the development package installed, I could add
`setuptools <http://pypi.python.org/pypi/setuptools>`__. After that,
it's a sequence of easy_install steps and we were up and running.

I've started running our unit test suite with python -3 to capture
all of the DeprecationWarnings. So far, there aren't many and they
aren't show-stoppers. In one project we have some has_key methods and
a use of urllib that needs to be replaced.

It's very, very nice to have a short, specific list of Python 3
compatibility issues to look out for. We're not going to use Python 3
any time soon, but it's nice to be able to solve the problems in
advance.




-----

Fedora 12 is available to <a href="http://library....
-----------------------------------------------------

elm<noreply@blogger.com>

2009-11-18 03:22:57.748000-05:00

Fedora 12 is available to `download <http://library.jak-stik.ac.id>`__
now!





