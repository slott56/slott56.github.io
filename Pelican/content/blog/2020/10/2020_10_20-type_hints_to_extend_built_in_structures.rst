Type Hints to extend built-in structures
========================================

:date: 2020-10-20 08:00
:tags: #python,type hints
:slug: 2020_10_20-type_hints_to_extend_built_in_structures
:category: Technologies
:status: published

Working on revisions to a book. Fun stuff.
See https://www.packtpub.com/product/python-3-object-oriented-programming/9781849511261
I may have the privilege of working with Dusty.

I've been using **mypy** for all my 2nd edition changes, but not in
--strict mode.

I've decided to ramp things up, and switch to strict type checking for
all of the examples and case studies.

This lead me to stumble over

::

   class MyThing(dict):
       def some_extra_method(self):
           pass

I absolutely could not get this to work for hours and hours.

I more-or-less gave up on it, until I started a similar example for a
later chapter.

::

   class ListWithFeatures(list):
       def feature(self):
           pass

This is almost the same, but, somehow, I understood it better.  As
written, it is rejected by mypy. What I meant was this.

::

   class ListWithFeatures(List[MyThing]):
       @overload
       def __init__(self) -> None: ...
       @overload
       def __init__(self, source: Iterable[MyThing]) -> None: ...
       def __init__(self, source: Optional[Iterable[MyThing]]) -> None:
           if source:
           super().__init__(source)
           else:
               super().__init__()
       def feature(self) -> float:
           return sum(thing.some_extra_method())/len(self)

I don't know why, but this was easier for me to visualize the problem..
It clarified my understanding profoundly.

We don't simply extend list or dict.  We should extend them because list
is an alias for List[Any], and when being strict, we need to avoid Any.
Aha.





