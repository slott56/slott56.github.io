Python 3.9 Rearranging typing and collections.abc
=================================================

:date: 2020-10-27 08:54
:tags: #python,type hints
:slug: 2020_10_27-python_39_rearranging_typing_and_collectionsabc
:category: Technologies
:status: published

This is glorious.

There was this sort of awkward shoving match between ``typing`` and
``collections.abc``. Both had generic type definitions and it was --
often -- unclear how to use them.

See `PEP 585 <https://www.python.org/dev/peps/pep-0585>`__. Now they are
all unified into a much happier family.

And. We wind up writing things like this.

::

   import collections.abc
   import typing
   import sys

   if sys.version_info >= (3, 9):
       BucketCollection = collections.abc.Collection[Sample]
   else:
       BucketCollection = typing.Collection[Sample]

Now we can have code that passes tests for 3.8 and 3.9. And at some
point we can cut off the 3.8 support and delete the ancient alternative
definition.

I'm delighted to be able to move forward with a much simpler future in
which collections are in the ``collections.abc`` and other, more
foundational stuff is in ``typing``.





