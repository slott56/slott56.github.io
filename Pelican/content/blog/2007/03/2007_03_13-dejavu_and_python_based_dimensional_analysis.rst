Dejavu and Python-based Dimensional Analysis
============================================

:date: 2007-03-13 10:14
:tags: #python,database
:slug: 2007_03_13-dejavu_and_python_based_dimensional_analysis
:category: Python
:status: published





Actually, the code looks like a clever expansion
on my example, in `PyCon 2007
(Revised) <{filename}/blog/2007/02/2007_02_26-pycon_2007_revised.rst>`_ .



"But wait," you
say.  "Creating a pivot table in
Python?"



Of course.  Spreadsheets can
create pivot tables from dimensionally normalized data.  However, getting the
data in this form is often challenging and if there is any manual operation at
all, the data quality is immediately
suspect.



To have perfect transparency
-- with no possibility of manual transformations -- you need a simple
application program which reliably, auditably, and testably produces the correct
data.  Further, you want to reduce the manual operations to formatting and
presentation.  The ideal solution is to produce the data in the required pivot
table so that it can be loaded into a spreadsheet for display
only.



With an object-relational mapper,
you can write a tidy query to fetch raw data, and compute a aggregate along two
dimensions.  You then assemble result columns on one dimension and rows on the
other dimension. 



**Elegant -- But Dirty -- Pool.** 



The Elegant
Thing that makes this work pleasantly and simply in Python is being able to use
a tuple as the key to a mapping.  I can't say enough good things about this
simple, elegant piece of Pythonic programming.  You can easily handle complex,
multi-column keys in each dimension of the pivot table, by simply creating a
tuple of key values, and using a pair of tuples to locate the appropriate cell
in a mapping.



Things like dimensional
conformance often create a gnarly algorithm in Java or -- shudder -- COBOL.  In
Python, it's a tuple that you can use to locate the dimension value in a
dictionary.  It works for everything except the Customer dimension, which in
some applications is too huge to retain in a simple in-memory
mapping.



The graceful elegance of
**Python's Mapping Indexed By A Tuple™**  (MXT) can really prevent a lot of
brain-cramping bugs.








