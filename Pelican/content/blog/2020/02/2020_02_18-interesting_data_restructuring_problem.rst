Interesting Data Restructuring Problem
======================================

:date: 2020-02-18 20:35
:tags: algorithm,#python
:slug: 2020_02_18-interesting_data_restructuring_problem
:category: Technologies
:status: published


This seemed like an interesting problem. I hope this isn't someone's
take-home homework or an interview question. It seemed organic enough
when I found out about it.

Given a document like this...

::

      doc = {
          "key": "the key",
          "tag1": ["list", "of", "values"],
          "tag2": ["another", "list", "here"],
          "tag3": ["lorem", "ipsum", "dolor"],
      }

We want a document like this...

::

      doc = {
          "key": "the key",
          "values": [
              {"tag1": "list", "tag2": "another", "tag3": "lorem"},
              {"tag1": "of", "tag2": "list", "tag3": "ipsum"},
              {"tag1": "values", "tag2": "here", "tag3": "dolor"},
          ]
      }

In effect, rotating the structure from ``Dict[str, List[Any]]`` to
``List[Dict[str, Any]]``.

Bonus, we need to limiting the rotation to those keys with a value of
``List[Any]``, ignoring keys with atomic values (int, str, etc.).

Step 1. Key Partitioning
------------------------

We need to distinguish the keys to be rotated from the other keys in
the dict.

We start with ``Dict[str, Union[List[Any], Any]]``. We need to
distinguish the two subtypes in the union.

::

      from itertools import filterfalse
      list_of_values = lambda x: isinstance(doc[x], list)
      lov_keys = list(filter(list_of_values, doc.keys()))
      non_lov_keys = list(filterfalse(list_of_values, doc.keys()))

This gets two disjoint subsets of keys: those which have a list and
all the others. The others, presumably, are strings or integers or
something irrelevant.

List lengths
-------------

There's no requirement for the lists to be the same lengths. We have
three choices here:

-  insist on uniformity,
-  truncate the long ones,
-  pad the short ones.

We'll opt for uniformity in this example. Truncating is what
``zip()`` normally does. Padding is what ``itertools.zip_longest()``
does.

::

      lengths = (len(doc[k]) for k in lov_keys)
      sample = next(lengths)
      assert all(l == sample for l in lengths), "Inconsistent lengths"

Some folks don't like using ``assert`` for this. This can be a more
elaborate ``if-raise ValueError()`` if that's necessary.

Use zip() to merge data values
-------------------------------

We have several ``List[Any]`` instances in the document. The
intermediate goal is a ``List[Tuple[Any, ...]]`` structure where the
items from each tuple are chosen from the source lists. This gets us
a sequence of tuples that have parallel selections of items from each
of the source lists.

The ``zip(list, list)`` function produces pairs from each of the two
lists. In our case, we have n lists in the original document. A
``zip(*lists)`` will produce a sequence of items selected from each
list.

Here's what it looks like:

::

      list(zip(*(doc[k] for k in lov_keys)))

We can also use ``zip(key-list, value-list)`` to make a list of
key-value pairs from a tuple of the keys and a tuple of values.
``zip(Tuple[Any, ...], Typle[Any, ...]])`` gives us a
``List[Tuple[Any, Any]]`` structure. These objects can be turned into
dictionaries with the ``dict()`` function.

It looks like this:

::

      list(dict(zip(lov_keys, row)) for row in zip(*(doc[k] for k in lov_keys)))




Assemble the parts
------------------


The final document, then, is built from untouched keys and touched
keys.

::

   d1 = {
       k: doc[k] for k in non_lov_keys
   }
   d2 = {
       "values": list(dict(zip(lov_keys, row)) for row in zip(*(doc[k] for k in lov_keys)))
   }
   d1.update(d2)




It might be slightly easier to "somehow" build this as s single
dictionary, but the two subsets of keys make it seem more sensible to
build the resulting document in two parts.


The code I was asked to comment on was quite complex. It built a
large number of intermediate structures rather than building a
``List[Dict]`` using a list comprehension.

What's important about this problem is the complexity of the list
comprehension. In particular, the keys are used twice in the
comprehension. One use extracts the source lists from the original
document. The second use attaches the key to each value from the
original list.

It almost seems like the Python 3.8 "Walrus" operator might be a
handy way to shrink this code down from about 14 lines. I'm not sure
it's helpful to make this any shorter. Indeed, I'm not 100% sure this
compact form is really optimal. The fact that I had to expand things
as part of an explanation suggests that separate lines of code are as
important as separate subsections of this blog post.



-----

Minor typo: ziplongest should be zip_longest
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2020-02-14 09:15:44.588000-05:00

Minor typo: ziplongest should be zip_longest
https://docs.python.org/3/library/itertools.html#itertools.zip_longest





