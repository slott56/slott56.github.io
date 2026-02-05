Literate Programming and PyLit
==============================

:date: 2013-10-03 08:00
:tags: #python,PyLit,pyWeb
:slug: 2013_10_03-literate_programming_and_pylit
:category: literate programming
:status: published

Even though I wrote a literate programming tool
(`PyWeb <http://pywebtool.sourceforge.net/>`__) I slowly came to
realize that it's not very good.

Mostly, I followed the Web/Weave world view and cribbed their markup
syntax. It's not bad, but, the PyWeb markup is based on some
presumptions about literate programming that were, perhaps, true with
some languages, but are not true at all when working with Python.

#.  The source presentation order incomprehensible. To fix this, we
    create a literate programming document, and from that tangle the
    source into an order that's acceptable to the compiler, but perhaps
    hard to understand for people. We weave a document that's easy for
    people to understand.

#.  The source syntax may be incomprehensible. To fix this, we have fine
    grained substitution. The target source can be built at any level of
    syntax (token, line, or higher-level language construct.) We can
    assure that the woven document for people is written using elegant
    symbols even if the tangled source code uses technical gibberish.

#.  The woven documentation needs a lot of additional output markup. The
    original web/weave toolset create extensive TeX markup. Later tools
    reduced the markup to allow HTML or XML, minimizing the added markup
    in a woven document.


In Python, there's very little "boilerplate" or overhead in a module
file. Also, because of very late binding, the presentation order of
the source can better match reader expectations. For definitions,
inter-class references mandate an order for the class statements in
an inheritance hierarchy, but almost everything else is remarkably
flexible.


Python syntax doesn't benefit from fine-grained web/weave techniques.
It's pretty clear as written in it's normal form.


Finally, the presence of `RST
markup <http://docutils.sourceforge.net/rst.html>`__ language means
that a whole new meta-markup for literate programming isn't
**necessary**.


`PyLit <https://pypi.python.org/pypi/pylit>`__ demonstrates that an
additional markup language is not helpful. RST is sufficient. PyLit
is an elegant parser of RST and Python. It can reshape RST into
Python as well as reshape Python into RST. Do your literate
programming in either language and produce the other easily.


Enter Python 3
--------------

The problem with PyLit is that it's oriented to Python 2.4 through
2.7. How can we use PyLit for Python 3?


-  Use six.py to make a single version that covers both Python2 and Python3.

-  Rewrite PyLit it for Python3 and move forward.


My preference is to move forward. The backward compatibility is
helpful when there's a vast user base, lots of ongoing
development, and the very real possibility of bug fixes that apply
to Python2 as well as Python3.


PyLit has a small user base, no real development to speak of, and a
very remote possibility of backward compatible bug fixes.


The rewrites are small. Here's the summary.


-  Remove print statement and exec statements.

-  Replace string formatting % with .format().

-  Replace raise statements and except statements with Python3 (and Python2.7) syntax.

-  Upgrade for dict method changes in Python3.

-  Replace DefaultDict with collections.defaultdict.

-  Replace optparse with argparse.


I've done this in my Python3.2 installation.


This doesn't address the Sphinx documentation, however, which should
probably be tweaked to be the latest and greatest Sphinx version,
also. Not much will change, there, however, since the RST remains
compatible.

Also, it doesn't address the files with names that differ only in
case. There are two graphics files in the /trunk/rstdocs/logo/ path
that differ only in **case** of letters. Bad, but acceptable for
Linux. Fatal for Mac OS X with the default filesystem.


The question is, what's the polite way to proceed?


-  Fork the PyLit 0.7.5 to create PyLit3 release 1.0? A whole, new project.

-  Try to use six.py to create a 2-3 compatible source file and call this PyLit 0.8?


Adding six.py to a package that was a single module file seems
like a bit of overkill. One of the elegant features of PyLit was
that it was so simple, it didn't even have a setup.py. However,
there may be a community of staunchly Python2 literate programming
advocates.





