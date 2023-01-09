Eager and Lazy Properties
=========================

:date: 2019-01-29 21:30
:tags: #python,OO design
:slug: 2019_01_29-eager_and_lazy_properties
:category: Technologies
:status: published


See this


    Dear Pythonista lazyweb: If I have a property spam and the
    attribute that backs it is \_spam, what do we call that? The
    "backing attribute"? The "original property"? Something else? Is
    there an official term for this?

    — Al Sweigart (@AlSweigart) `January 29,
    2019 <https://twitter.com/AlSweigart/status/1090348010041528321?ref_src=twsrc%5Etfw>`__




My answer was -- frankly -- vague. Twitter being what it is, I should
have written the blog post first and linked to it.

The use case is this.

::

   class X:
       def __init__(self, x):
           self._value = f(x)
       @property
       def value(self):
           return self._value




We've got a property where the returned value is already an instance
variable.




I'm not a fan.

This reflects an eager computation strategy. f(x) was computed eagerly
and the value made available via a property. One can justify the use
of a property to make the value read-only, but... still nope.

There are a lot of alternatives that make more sense to me.

Option 1. We're All Adults Here.
--------------------------------


Here's an approach I think is better.

::

   class X:
       def __init__(self, x):
           self.value = f(x)




It's read-only because -- really -- if you change it, you break the
class. So don't change it.

This is my favorite. Read-onlyness is sometimes described has a way
protect utter idiots from breaking a library they don't seem to
understand. Or. It's described as a way to prevent some Evil Genius
Programmer (EGP) from doing something intentionally malicious and
breaking things.

Bah.

It's Python. They have access to the source. Why mess around breaking
things this way?

Option 2. Lazyiness
-------------------


Here's an approach that hits at the essential feature.

::

   class X:
       def __init__(self, x):
           self.x = x
       @property
       @lru_cache(None)
       def value(self):
           return f(self.x)




This seems to hit at the original intent without an explicit cached
variable. Instead the caching is pushed off into another space. (I'm
writing a chapter on decorators, so this may be a bit much.)

The idea, though, is to make properties lazy. If they're expensive,
then the result should be cached.

There may be other choices, but I think lazy and eager cover the
bases. I don't think eager is wrong, but I don't see the need for a
property to hide the attribute created by an eager computation.




