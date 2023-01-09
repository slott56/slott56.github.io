Wrestling with the Python shelve module
=======================================

:date: 2014-03-21 11:53
:tags: design,schema migration
:slug: 2014_03_21-wrestling_with_the_python_shelve_module
:category: Technologies
:status: published

While wrestling with Python's shelve module, I ran across
`ACID <http://acid.readthedocs.org/en/latest/>`__. Interesting thoughts.
Plus what appears to be the related Tumblr blog: `python
sweetness <http://pythonsweetness.tumblr.com/?utm_campaign=SharedPost&utm_medium=Email&utm_source=TumblriOS>`__.
Also interesting.
Not sure I can make heavy use of it right now, but it's helpful to see
the thought process.
I find the subject of shelve (or pickle) and schema change endlessly
fascinating.  I have no good ideas to contribute, but it helps to read
about ways to track schema evolution against data that's as highly
class-specific as shelve data is.
Versioning class definitions and doing data migration to upgrade a
database is -- right now -- a fascinating problem.





