A get_object_size() Function -- Again
#######################################

:date: 2025-10-17 13:08
:tags: python,oo,oodesign
:slug: 2025-10-17-get_object_size_function_again
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

See `A get_object_size() function <{filename}/blog/2025/10/2025-10-16-get_object_size.rst>`_. This shows a totally non-recursive and not-too-smart approach.

The previous example avoids recursion.
This is not *really* helpful.
While structures can be very large, they are rarely deeply nested.
The ordinary Python stack limit would prevent us from walking a structure with over 1,000 layers of nesting.
Even creating a test case is a pain in the neck.


What I Did
==========

This function computes the total size of just about anything.
This includes all the built-in collections.
It also includes "custom classes", both the ``__slots__`` and the non-``__slots__`` variants.

..  code-block:: python

    from collections.abc import Sequence, Mapping, Set
    import itertools
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
        seen: set[int] = set()

        def component_size(obj: Any) -> int:
            nonlocal seen
            if id(obj) in seen:
                return 0
            seen.add(id(obj))

            if verbose:
                print(f"{id(obj):8x} {type(obj)}, {shorten(repr(obj), 32)}", file=sys.stderr)

            base = [sys.getsizeof(obj, default_size)]
            items = iter([])
            match obj:
                case str():
                    pass
                case Sequence() | Set() as sequence:
                    items = map(component_size, sequence)
                case Mapping() as mapping:
                    items = itertools.chain(
                        map(component_size, mapping.keys()),
                        map(component_size, mapping.values())
                    )
                case object() as obj_dict if hasattr(obj, '__dict__'):
                    base.append(sys.getsizeof(obj_dict.__dict__))
                    items = itertools.chain(
                        map(component_size, obj_dict.__dict__.keys()),
                        map(component_size, obj_dict.__dict__.values())
                    )
                case object() as obj_slot if hasattr(obj, '__slots__'):
                    values = (getattr(obj_slot, name)
                        for name in obj_slot.__slots__
                        if hasattr(obj_slot, name)
                    )
                    items = map(component_size, values)
                case _:
                    print(f"skipping {type(obj)}")
                    pass

            sizes = itertools.chain(base, items)
            return sum(sizes)

        return component_size(some_object)


This variant walks an entire structure recursively.
It creates iterable generators with size details.

You won't often need this.
But. I've posted it here so I won't lose it.

And. Because the first version was based on a few faulty assumptions.
