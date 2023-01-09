Modern Python Cookbook Journey
##############################

:date: 2020-07-30 08:00
:tags: #python,modern python cookbook,@PacktAuthors,marketing promotion
:slug: 2020_07_30-modern_python_cookbook_journey
:category: Books
:status: published

For the author, a book is a journey.


Writing something new, the author describes a path the reader can
follow to get from -- well -- anywhere the reader might be to the
author's suggested destination. Not everyone makes the whole trip.
And not everyone arrives at the hoped-for destination.


Second editions? The idea is to update the directions to reflect the
new terrain.


I'm a sailor. Here's a view of the boat.



.. image:: {static}/media/RedRangerSailing.jpg
   :width: 320px
   :target: {static}/media/RedRangerSailing.jpg
   :alt: Red Ranger sailboat



What's important to me is the way the authorities produce revised
nautical charts on a stable, regular cadence. There's no "final"
chart, there's only the "current" chart. Kept up-to-date by the
patient hard work of armies of cartographers.


Is updating a book like updating the nautical charts? I don't think
so. Charts have a variety of update cadences.  For sailors in the US,
we start
here: https://nauticalcharts.noaa.gov/charts/chart-updates.html. The
changes can be frequent.
See https://distribution.charts.noaa.gov/weekly_updates/ for the
weekly chart updates. This is supplemented by the Notices to
Mariners, here, too: https://msi.nga.mil/NTM. So, I think charts are
much, much more complex than books.


Sailors have to integrate a lot of data.  This is no different from
software developers having to keep abreast of language, library, and
platform changes.


The author's journey is different from the reader's journey. A
technical book isn't a memoir.


The author may have crashed into all kinds of rocks and shoals. The
author's panic, fear, and despair are not things the reader needs to
know about. The reader needs to know the course to set, the
waypoints, and hazards. The estimated distances and the places to
anchor that provide shelter.


For me, creating a revision is possibly as difficult as the initial
writing. I don't know how other authors approach subsequent editions,
but the addition of type hints meant every example had to be
re-examined.  And this meant discovering problems in code that I
\*thought\* was exemplary.


While many code examples can simply have type hints pasted in, some
Python programming practices have type hints that can't be trivially
introduced to the code. Instead some thinking is required.

Generics
--------


Python code is always generic with respect to type. Expressions
like ``a + b`` will work for a surprisingly wide variety of object
classes. Of course, we expect any of the numbers to work. But lists,
tuples, and strings all respond to the "+" operator. This is
implemented by a sophisticated check of a's ``__add__()`` and b's
``__radd__()`` methods.


When we write hints, it's often intended to **narrow** the domain of
potential types. Here's some starting code.

::

   def fact(a):
      if a == 0:
          return 1
      return a*fact(a-1)


The implied type hint is Any. This means, any class of objects that
defines \__eq__(), \__mul__() and \__sub__() will work. There are a
fair number of these classes.


When we write type hints, we narrow the domain. In this case, it
should be integers. Like this:

::

   def fact(a: int) -> int:
       if a == 0:
           return 1
       return a*fact(a-1)


This tells mypy (or other, similar analytic tools) to confirm that
every place the fact() function is used, the arguments will be
integers. Also, the result will be an integer.


What's important is there's no run-time consequence to this. Python
runs the same whether we evaluate fact(2) or fact(3.0).  The
integer-based computation clearly matches the intent stated in the
code. The floating-point computation is clearly at odds with the
stated intent.


And this brings us to the author's journey.

Shoal Water
------------


Sometimes we have code that works. And will always work. But. The
type hints are hard to express.


The most common examples?


Decorators.


Decorators can be utterly and amazingly generic. And this can make it
very, very difficult to express the domain of types involved.

::

   def make_a_log(some_function: Callable) -> Callable:
       @wraps(some_function)
       def concrete_function(*args, \**kwargs):
           print(some_function, args, kwargs)
           result = some_function((*args, \**kwargs)
           print(result)
       return concrete_function


This is legal, but very shady Python. The use of the Callable type
hint is almost intentionally misleading. It could be anything.
Indeed, because of the way Python works, it can truly be any kind of
function or method. Even a lambda object can be decorated with this.


The internal concrete_function doesn't have any type hints. This
forces mypy to assume Any, and that will lead to a possibly valid
application of this decorator when -- perhaps -- it wasn't really
appropriate.


In the long run, this kind of misleading hinting is a bad policy.


In the short run, this code will pass every unit test you can throw
at it.


What does the author do?


#.  Avoid the topic? Get something published and move on? It is
    simpler and quicker to ignore decorators when talking about type
    hints. Dropping the section from the outline would have been easy.

#.  Dig deeply into how we can create Protocols to express a narrower
    domain of candidates for this decorator? This is work. And it's
    new work, since the previous edition never touched on the subject.
    But. Is it part of this cookbook? Or do these deeper examples
    belong in a separate book?

#.  Find a better example?


Spoiler Alert: It's all three.


I start by wishing I hadn't broached the topic in the first edition.
Maybe I should pretend it wasn't there and leave it out of the second
edition.


Then I dig deeply into the topic, overwriting the topic until I'm no
longer sure I can write about it. There's enough, and there's too
much. A journey requires incremental exposition, and the side-trip
into Protocols may not be the appropriate path for any but a very few
readers.


After this, I may decide to throw the example out and look for
something better.  What's important is having an idea of what is
appropriate for the reader's journey, and what is clutter.


The final result can be better because it can be:


-   Focused on something useful.

-   Any edge cases can be corrected to work with the latest language,
     library, and mypy release.

-   Where necessary, replaced by an alternative example that's clearer
    and simpler.


Unfortunately (for me) I examine everything. Every word. Every
example.


Packt seems to be tolerant of my slow pace of delivery. For me, it
simply takes a long time to rewrite -- essentially -- everything. I
think the result is worth all the work.



