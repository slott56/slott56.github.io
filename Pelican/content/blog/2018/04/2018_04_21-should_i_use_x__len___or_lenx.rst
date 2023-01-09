Should I use x.__len__() or len(x)?
===================================

:date: 2018-04-21 09:37
:tags: #python
:slug: 2018_04_21-should_i_use_x__len___or_lenx
:category: Technologies
:status: published

| In the context of providing type hints, someone had a function like
  this.

::

   def f(x: Sized) -> Whatever: ...

| 
| And, since sized objects have a \__len__() method it seemed sensible
  to use x.__len__(). It was a good question about the use of special
  methods.
| My advice is to avoid using the special methods in general. Use them
  only when defining classes that need to behave like Python objects.
| (I'll make an exception for using x.__dict_\_, to avoid having to
  introduce an explicit dictionary object when there's one built-in to
  most objects.)
| Use len(x) and be happy.  The function wrapper around a special method
  is a common Python feature; it occurs in many places; use it.





