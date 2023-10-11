Python Type Hinting -- generally easy until you find your design flaws
======================================================================

:date: 2017-11-07 08:00
:tags: #python
:slug: 2017_11_07-python_type_hinting_generally_easy_until_you_find_your_design_flaws
:category: Technologies
:status: published

Adding type hints is easy and fun. Seriously. It's not a lot of work.

Until.

Until you find a piece of code that does more than what you sort-of
  thought it kind-of did.

::

   def null_aware_func(x):
       if x is None:
            return x
       return 2.2*x**1.05


This is a stab at a none-aware computation.
Let's add type hints, shall we?

::

   def null_aware_func(x: float) -> float:
       if x is None:
           return None
       return 2.2*x**1.05


This won't fool mypy. Sigh. It passes unit tests, but it's flagged as
  a problem.
We have a variety of ways of define this function. And that means we
  need to think carefully about our None-aware design.

Is this really an ``@overload``?

::

   from typing import overload
   @overload
   def null_aware_func(x: None) -> None:
       ...
   def null_aware_func(x: float) -> float:
       if x is None:
           return None
       return 2.2*x**1.05


And yes, the ``...`` is legit Python syntax. (It's a rarely used token
  that forms the body of the function.)

Or is this a more advanced type?

::

   from typing import Optional
   OptFloat = Optional[float]

   def null_aware_func(x: OptFloat) -> OptFloat:
       if x is None:
           return None
       return 2.2*x**1.05


I'd argue that ``OptFloat`` is a more sensible definition. However, if
  this is the only function that's none-aware, perhaps it's an overload.
The deeper question is one of underlying meaning. Why are we doing
  this? What does it mean?
And. Bonus. Will this be working in a SQLAlchemy environment, where
  they have their own wrappers for database objects, meaning that ``is None`` doesn't work and ``== None`` is required?

What's important is that adding type hints forced us to think about
  what we were doing. Unlike Java we did this without stopping progress
  for an extended period of "wrestling with the compiler". We can use
  Any temporarily because the unit tests all pass. Then, we can pay down
  the technical debt by fixing the type declaration.

Total. Victory.





