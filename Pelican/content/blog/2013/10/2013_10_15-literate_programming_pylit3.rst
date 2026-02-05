Literate Programming: PyLit3
============================

:date: 2013-10-15 08:00
:tags: #python,PyLit
:slug: 2013_10_15-literate_programming_pylit3
:category: literate programming
:status: published

I've revised PyLit to work with Python3.
See https://github.com/slott56/PyLit-3
The code seems to pass all the unit tests.
The changes include Python3 revisions, plus a small change to handle
trailing spaces in a sightly cleaner fashion. This was necessary because
I have most of my editors set to remove trailing spaces from the files I
create, and PyLit tended to create trailing spaces. This made the
expected output from the unit tests not precisely match the actual
output.





