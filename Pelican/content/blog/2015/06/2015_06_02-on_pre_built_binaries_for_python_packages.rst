On Pre-built Binaries for Python Packages
=========================================

:date: 2015-06-02 08:00
:tags: mac os x,#python,windows,linux
:slug: 2015_06_02-on_pre_built_binaries_for_python_packages
:category: Technologies
:status: published

Or.
Why I Hate Windows.
For Mac OS X, you download XCode (for free) and you can build anything.
For Linux, you use some kind of yum or rpm installer for the developer
tools, and you can build anything.
For Windows...
Pre-built binaries. 😂
And a hope that the version numbers all match up properly. 😖
In many cases, you can use
`http://www.mingw.org <http://www.mingw.org/>`__ or
`http://www.cygwin.com <http://www.cygwin.com/>`__. Many projects can
work well with one or both of these compilers.
In some cases, however, you have for fork over $$$ for Microsoft Visual
Studio to download and build a Python module with a C extension.
The problem is a show-stopper for many n00bz. They are lead to believe
that pip does everything. And it does -- for Mac OS X and Linux; for
Windows, however, it does **almost** everything. And it's not obvious to
the n00bz what the problem is when pip barfs because there's no suitable
C compiler.
"Replace that junk Windows PC" is not an appropriate response. Although
I often suggest it as the first solution when things won't install. 😡
Often `Anaconda <http://docs.continuum.io/anaconda/pkg-docs.html>`__ is
the solution. It includes MinGW and you can (for a fee) buy their bundle
of database drivers. The install for Anaconda is breathtakingly simple,
removing a great deal of the potential complexity of assembling a tech
stack for Python.
In other cases, we have to do some hand-holding to show how to find a
pre-built binary for Windows.





