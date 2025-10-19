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

    from collections.abc import Sequence, Mapping, Set, Iterable, Callable
    import itertools
    import sys
    from textwrap import shorten
    from typing import Any


    def get_object_size(
        some_object: Any,
        additional_types: Callable[[Any], int | None] | None = None,
        verbose: bool = False,
    ) -> int:
        """
        Computes the size of the given object.
        This expands on the recipe cited in the documentation for :py:func:`sys.getsizeof`.

        :param some_object: Any Python object.
        :param additional_types: A function that can return the size for an object for a type not handled here.
        :param verbose: True to print object information as the size is computed.
        :return: aggregate size of the object and all the related objects.

        The sizes are **highly** implementation specific.

        The types handled here are the built-in collections
        defined in :py:mod:`collections.abc`:
        ``str``, ``Sequence``, ``Set``, ``Mapping``.
        Additionally, this will look at any instance of class derived from :py:class:`object`,
        handling the default ``__dict__`` as well as ``__slots__``.

        >>> get_object_size("Hello, world!")
        54
        >>> get_object_size("!")
        42
        >>> get_object_size(list(range(10)))
        416
        """
        default_size = sys.getsizeof(0)
        seen: set[int] = set()

        def component_size(obj: Any) -> int:
            nonlocal seen
            if id(obj) in seen:
                return 0
            seen.add(id(obj))

            if verbose:
                print(
                    f"{id(obj):8x} {type(obj)}, {shorten(repr(obj), 32)}", file=sys.stderr
                )

            items: Iterable[int] = iter([])
            match obj:
                case str():
                    pass
                case Sequence() | Set() as sequence:
                    items = map(component_size, sequence)
                case Mapping() as mapping:
                    items = itertools.chain(
                        map(component_size, mapping.keys()),
                        map(component_size, mapping.values()),
                    )
                case object() as obj_dict if hasattr(obj, "__dict__"):
                    items = itertools.chain(
                        map(component_size, obj_dict.__dict__.keys()),
                        map(component_size, obj_dict.__dict__.values()),
                    )
                case object() as obj_slot if hasattr(obj, "__slots__"):
                    values = (
                        getattr(obj_slot, name)
                        for name in obj_slot.__slots__
                        if hasattr(obj_slot, name)
                    )
                    items = map(component_size, values)
                case _:
                    if additional_types and (obj_size := additional_types(obj)) is not None:
                        items = iter([obj_size])

            base = [sys.getsizeof(obj, default_size)]
            sizes = itertools.chain(base, items)
            return sum(sizes)

        return component_size(some_object)


This variant walks an entire structure recursively.
It creates iterable generators with size details.

You won't often need this.
But. I've posted it here so I won't lose it.

And. I like to think through alternative implementations.
One of these is probably faster.
