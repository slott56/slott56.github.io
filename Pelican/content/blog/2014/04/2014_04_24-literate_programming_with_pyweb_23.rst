Literate Programming with pyWeb 2.3
===================================

:date: 2014-04-24 08:00
:tags: #python,pyWeb,literate programming
:slug: 2014_04_24-literate_programming_with_pyweb_23
:category: Technologies
:status: published

Updates completed.
See https://sourceforge.net/projects/pywebtool/ and `http://pywebtool.sourceforge.net <http://pywebtool.sourceforge.net/>`__.

The list of changes is extensive.

However, the essential API and the markup language for creating
literate programs hasn't (significantly) changed. A few experimental
features were replaced with a first-class implementation.

The interesting (to me) bit is this sequence of events.

I started out using `Leo <https://wiki.python.org/moin/LeoEditor>`__
and `Interscript <http://interscript.sourceforge.net/>`__ as a
literate programming tools. They worked. But they were larger and
clunky and I wasn't happy.

I wrote my own too, not **really** getting the use cases.

I found `pyLit <https://github.com/slott56/PyLit-3>`__ and liked it a
lot. For a long time, I liked it better than my own
`pyWeb <https://sourceforge.net/projects/pywebtool/>`__ tool.

Then I ran across some problem domains for which pyLit didn't work out
well. It's not that I've abandoned pyLit, but I believe I'll focus
more on pyWeb.

**The Awkward Problem Domains**

Here are the two awkward problem domains.

-   **Historical Story Lines**. In some cases, we want to describe a
    module or package based on the path of exploration. Rather than
    simply drop the design, we want to show the path followed which lead
    to the design. This can be helpful for certain kinds of pedagogical
    exercises where we're steering the reader through a process.

-   **Complex Packages that Don't Follow Python's Presentation Order**.
    In some cases, we need to present things out of order. Python
    constrains us to have docstring and imports first. Our class
    definitions must proceed in "dependency" order. But this may not be
    the best order for explanation. Sometimes, we want to start with the
    "def main():" function first to explain **why** a class looks the way
    it does.


PyWeb handles these nicely.  One of the handiest things is this for
out-of-order presentation.

::

    @d Some Class... @{

    class TheClass:
        etc.
    @}

    This class uses the following imports

    @d Imports...@{
    import this
    import that
    @}

We can then scatter imports through the documentation in the relevant
places. And they **follow** the more interesting material.


When it comes to final assembly, we have this.


::

      @o some_module.py @{
          @<Imports for this module@>
          @<Some Class that does the real work of this module@>
      @}


This builds the module, tangling the imports into one cluster up
front, and putting the class definition later.





