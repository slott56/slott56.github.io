Python Package Design, Refactoring and the Stingray Reader Project
==================================================================

:date: 2014-05-22 08:00
:tags: #python,OO design,architecture,stingray reader,refactoring,mastering object-oriented python
:slug: 2014_05_22-python_package_design_refactoring_and_the_stingray_reader_project
:category: Technologies
:status: published

We'll be digging into `Mastering Object-Oriented
Python <http://www.packtpub.com/mastering-object-oriented-python/book>`__.
Chapter 17, specifically.

We'll also be looking at a big refactoring of the `Stingray
Schema-Based File
Reader <https://sourceforge.net/projects/stingrayreader/>`__.

We can identify three species of packages.

One common design is a **Simple Package**. A directory with an empty
``__init__.py`` file. This package name becomes a qualifier for the
internal module names. The package is simply a namespace for modules.
We’ll use the package with something like this:

::

    import package.module



Another common design is the **Module-Package**. This is a package
which appears to be a module.  It will have a larger and more
sophisticated ``__init__.py`` that is a effectively, a  module
definition. There are two variations on this theme. Sometimes we'll
use this during the early stages of development because we don't know
if the package will get really big or stay small. If we start out with
a package and all the code is in the ``__init__.py``, we can refactor
down to a module.

The more common use for a module-package is to have the ``__init__.py``
import objects or other modules from the package directory. Or, it can
stand as a part of a larger design that includes the top-level module
and the qualified sub-modules. We’ll use the package with something
like this:

::

    import package

or perhaps

::

    from package import thing

The third common pattern is a package where the ``__init__.py`` selects
among alternative implementations. The os module is a good example of
this. We’ll use the package with something like this:

::

    import package

Knowing that it did something roughly like the following for us.

::

    import package.implementation as package

**Refactoring Module to Package**


The Stingray angle on this is the need to add iWork '13 numbers to the
collection of spreadsheets which it can parse. The iWork '13 format is
unique.

Previously, all of the spreadsheets fell into three families:

-  CSV or CSV-like. Simple text.

-  XLS. We relied on https://pypi.python.org/pypi/xlrd/0.9.3 to make sense of .XLS files.

-  XML-based. We parsed the XML and located sheets, rows and cells.


iWork '13 uses Snappy compress and Protobuf Serialization. Without
some documentation, the files would be incomprehensible.  Read this:
See https://github.com/obriensp/iWorkFileFormat. Brilliant.


The previous releases of Stingray had a single, large module to
handle a variety of workbook formats. Folding iWork '13 into this
module would have been lunacy. It was already large to the point of
being painful to understand.


The original module will be transparently turned into Module-Package.
The API (import stingray.workbook or from stingray.workbook import
SomeClass) will remain the same.


However.


The implementation will involve a package with each workbook format
as a separate module inside that package. At the top, the
``__init__.py`` will include code like the following.


::

      from stingray.workbook.csv import CSV_Workbook
      from stingray.workbook.xls import XLS_Workbook
      from stingray.workbook.xlsx import XLSX_Workbook
      from stingray.workbook.ods import ODS_Workbook
      from stingray.workbook.numbers_09 import Numbers09_Workbook
      from stingray.workbook.numbers_13 import Numbers13_Workbook
      from stingray.workbook.fixed import Fixed_Workbook


This has the advantage of allowing us to include additional
parsing cruft in each module that's not part of the exposed API in
the workbook package.
The `Mastering Object-Oriented
Python <http://www.packtpub.com/mastering-object-oriented-python/book>`__ book
has more details on this kind of design.


