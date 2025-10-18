A get_object_size() Function [Updated]
#######################################

:date: 2025-10-16 13:08
:tags: python,oo,oodesign
:slug: 2025-10-16-get_object_size_function
:category: Python
:status: published

BLUF
====

You rarely need this.
Python handles memory management for you.
Except in an edge case where you have a **lot** of objects to work with.

How many is a lot?  Enough that your app crashes with ``MemoryError`` exception.
Or, is consuming so much memory other processes have trouble working.
Or, it's slow because of all the garbage collection going on.

Background
==========

One of the significant benefits of using Python is memory management.
Python creates and disposes of objects as needed, without a lot of complicated-looking code.
The reference counting often works flawlessly.

Often.

Sometimes there are circular references, and objects can't (trivially) be collected.
Object A refers to object B and (sadly) object B *also* refers to object A.
They both have non-zero reference counts.

Weak references can sort this out, preventing a core leak that leads to unreliable software.

Use Case
=============

Python has a way to reduce the size of objects.
It alters a few minor details of how an object works, but is generally transparent.

This is an example of a rare case where you are doing memory management in Python.

You can use the ``__slots__`` feature of a class to name the attributes that are present,
and prevent the creation of the usual ``__dict__`` structure to hold the attributes.

When playing with this, it's often easiest to use the ``@dataclass(slots=True)`` decorator apply this to a class.

This will save memory.

How much memory?

It's hard to say, because you need to know the "without ``slots=True``" and "with ``slots=True``" sizes.
Generally, ``slots=True`` will be smaller.
If you've chosen the right class to shrink, you may find improved performance, also.

To determine the savings, we need to know the actual size of the collection of objects that are crushing the life out of our application and leading to ``MemoryError`` exceptions.

The Object Size Problem
=======================

The ``sys`` module has a function, ``sys.getsizeof()``, that will provide the size of an object.

This is the object **in isolation**.

..  important:: ``sys.getsizeof()`` doesn't include contained objects

What does it matter of it doesn't include contained objects?

Consider a ``list[int]``.

::

    >>> import sys
    >>> small_list = list(range(10))
    >>> large_list = list(range(10_000))
    >>> sys.getsizeof(small_list)
    136
    >>> sys.getsizeof(large_list)
    80056

Okay. Superficially, it seems like each integer in the small list takes up about 13 bytes.

Weirdly, each integer in the large list seems to take about 8 bytes.

This can't be right.

Consider an ``int``.

::

    >>> sys.getsizeof(42)
    28

Okay.
That's really, really weird.

The ``list[int]`` size is the size of the ``list`` object.
It doesn't include the 10 (or 10,000) ``int`` objects that are members of the list.

Total memory for the short list, then is :math:`136 + 10 \times 28 = 416`.
Total memory for the large list would be :math:`80,\!056 + 10,\!000 \times 28 = 360,\!056`.

The Documentation Says
======================

Check the documentation for ``sys.getsizeof()``. You'll see this.

    "See `recursive sizeof recipe <https://code.activestate.com/recipes/577504-compute-memory-footprint-of-an-object-and-its-cont/>`_ for an example of using getsizeof() recursively to find the size of containers and all their contents."

The documentation doesn't say "And read all the comments and integrate all those ideas into one function."

What I Did
==========

This function computes the total size of just about anything.
This includes all the built-in collections.
It also includes "custom classes", both the ``__slots__`` and the non-``__slots__`` variants.

..  code-block:: python

    from collections import deque
    from collections.abc import Sequence, Mapping, Set, Iterable
    import sys
    from textwrap import shorten
    from typing import Any


    def get_object_size(some_object: Any, verbose: bool = False) -> int:
        """
        For built-in collections, the size is clear.
        For classes, however, it's a hair more complicated.

        See https://code.activestate.com/recipes/577504-compute-memory-footprint-of-an-object-and-its-cont/
        """
        default_size = sys.getsizeof(0)
        seen = set()
        elements = deque([some_object])
        sizes: list[int] = []
        while elements:
            obj = elements.popleft()
            if id(obj) in seen:
                continue
            seen.add(id(obj))

            if verbose:
                print(f"{id(obj):8x} {type(obj)}, {shorten(repr(obj), 32)}", file=sys.stderr)

            sizes.append(sys.getsizeof(obj, default_size))
            match obj:
                case str():
                    pass
                case Sequence() | Set():
                    elements.extend(iter(obj))
                case Mapping():
                    elements.extend(obj.keys())
                    elements.extend(obj.values())
                case object() if hasattr(obj, '__dict__'):
                    sizes.append(sys.getsizeof(obj.__dict__))
                    elements.extend(obj.__dict__.keys())
                    elements.extend(obj.__dict__.values())
                case object() if hasattr(obj, '__slots__'):
                    elements.extend(
                        getattr(obj, name)
                        for name in obj.__slots__
                        if hasattr(obj, name)
                    )
                case _:
                    pass
        return sum(sizes)


Note that this walks an entire structure without *actually* being recursive.
If you've got a complicated application, and a **very** deeply-nested data structure,
the overhead of a lot of stack frames may be unmanageable.

(There are other optimization approaches to this problem.)

This assumes that a collection **always** contains heterogeneous types.
This means computing the size of each item in the list.

This uses a big ``deque``, which can involve impossible overhead, also.

In some cases, you may need to create a more complicated special-purpose benchmark app that builds your big data structure using your distinct storage alternatives.
Use your special benchmark test-bed to uncover the implementation that meets all the criteria for storage use and CPU time.

The data that is used for the benchmark would need to reflect real-world data with respect to string lengths, and collection sizes.
Creating synthetic data for an object size benchmark can be a challenge.
See `Synthetic Data <{filename}/blog/2024/06/2024-06-29-synthetic_data.rst>`_.
And, also see `Synthetic Data Tools <{filename}/blog/2024/07/2024-07-25-synthetic_data_tool.rst>`_.


You won't often need this.
But. I've posted it here so I won't lose it.

TODO
====

Handle ``numpy`` types, also.
