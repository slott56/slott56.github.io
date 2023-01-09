Functional Python Programming 2e -- Type Hints!
===============================================

:date: 2018-05-07 09:28
:tags: #python,@PacktAuthors,functional python programming,type hints
:slug: 2018_05_07-functional_python_programming_2e_type_hints
:category: Technologies
:status: published


You might want to look into this: `Functional Python Programming -
Second
Edition <https://www.packtpub.com/application-development/functional-python-programming-second-edition>`__.

Let's talk about the type hints, shall we?

Most of the examples have had type hints added. This means running
everything through mypy. And it also means running everything through
doctest, as well.

More important than the technical steps, there's a change in viewpoint
that comes with type hints.

If you follow a variety of Pythonistas on Twitter, you can see some
debates on the merits of type-hinting. Some key points:

-  It's hard.

-  It's so hard, only do it if you absolutely need it.

-  It's too verbose

-  It's hard, but it can help.

-  It's really helpful.

-  It represents a "gap" in the language and without run-time type
   checking, the whole thing is worthless.


The last point a weird view. I work in a shop that's heavily
Pythonic. But. You still hear nonsense. Python a very popular
language and it's popularity is growing. The popularity of Python
isn't like the popularity of a movie where you're not planning on
making a living off of it (I know
`someone <https://www.imdb.com/name/nm3399447/?ref_=nmvi_tt>`__ who
makes their living off the popularity of movies.) The popularity of
Python is like the popularity of automobiles or air travel or
electricity.

I hear the "a real language would have prevented that with
type-checking." And I respond, "Then why do you unit test?" And they
don't really have much of an answer. Python has the same workflow as
statically type-checked languages, so the "prevention" thing seems to
be nonsense.


Moving on.


"It's hard." Anything new is hard. The complaint is vague, so it's
\*hard\* to respond. (Heh.)


Anything like "only do it if you absolutely need it" bothers me
because it seems like a passive-aggressive barricade around things.
Also. It's vague.

Verbosity
---------


Verbosity in type hints is a real problem. When creating complex
objects from built-in types, we often forget to give names to the
intermediate object classes.


Consider Dict[Tuple[Tuple[int, int], Tuple[int, int]], float]


It's long. It describes a structure like this {((12, 13), (14, 15)):
2.8284271247461903, ...}


Writing something like the following d_map() function without hints
is easy. Adding hints seems hard.


::

   def d_map(points):
       return {(p1, p2): hypot(p1[0]-p2[0], p1[1]-p2[1]) for p1, p2 in points}


The declaration became L.. O... N... G... because we ignored the
intermediate types.

::

      def d_map(points: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> Dict[Tuple[Tuple[int, int], Tuple[int, int]], float]:
          return {(p1, p2): hypot(p1[0]-p2[0], p1[1]-p2[1]) for p1, p2 in points}

These hints, however, doesn't really describe what's happening. The
hints elide important details. The hints don't reflect the underlying
semantics of the data structure.

One of Python's strengths is the rich collection of first-class data
structures with built-in syntax. We can abbreviate some complex
concepts into succinct, expressive code.

However.

We shouldn't lose sight of what the succinct code represents. And in
this case, it represents some rather complex concepts.

      <rant>

      Let me sit in my lawn chair and shake my fist in helpless fury at
      you kids. When I was your age, we sent half a semester of
      undergraduate work trying to get linked lists, and simple hash
      mapping to work. Months of work. Later on, as a professional --
      years of actual experience -- it took forever to build a binary
      tree-based ``collections.Counter`` definition to gather simple numbers
      from a flat file. Nowadays, you just slap a ``Counter`` down into your
      code like it's a nothing. It's not a nothing. It's serious,
      sophisticated software engineering. It's more than ``Dict[Any, int]``.

      </rant>

What can we do?
---------------

When in doubt, **Expose the Intermediate Types**.

::

      Point = Tuple[int, int]
      Leg = Tuple[Point, Point]
      Distances = Dict[Leg, float]
      def d_map(points: Iterable[Leg]) -> Distances:
          return {(p1, p2): hypot(p1[0]-p2[0], p1[1]-p2[1]) for p1, p2 in points}

This exposes the details. In some cases, it causes us to rethink
using a two-tuple to represent a point. The p1[0] syntax starts to
chafe a little.

Perhaps this should have been

::

      class Point(NamedTuple):
          x: int
          y: int

That leads to tiny (almost-but-not-quite trivial) simplifications.
Instead of building simple tuples for each point, we can now build
named Point tuples and use p1.x and p1.y to make the code more
civilized.

One consequence of this is actually avoiding ``()``, ``[]``, and ``{}`` to build
tuples and lists. Yes. This is heresy. I seriously recommend using
``tuple()``, ``list()``, ``dict()``, and ``set()`` because we can replace them with
equivalent types. And yes, I text my mother with the same fingers
that wrote that.

"But," you object, "It's objectively LONGER! You didn't save me
anything! You're a fraud!"

My first response is, "Correct." It is objectively longer. And
"Correct," I didn't really "save" you anything; I'm not sure what
you're saving. Lines of code do have a cost, but I think clarity has
value. And finally, "Correct," I've often been wrong, and I may be
wrong here, too.

I like this because the type definitions are **reusable**, I think
this can add clarity throughout the application.

When this kind of declaration is part of a reusable module, the
goodness spreads like smiles and hugs throughout the application.
Before long, other functions have been tweaked and everyone is
sending each other little teddy-bear hug gifts with rainbow cupcakes.

(Please don't exchange mylar balloons. They're
`evil <https://www.chesapeakebaymagazine.com/features/2017/9/15/a-ballooning-problem>`__.
Also, see
`this <http://www.itmaybeahack.com/TeamRedCruising/travel-2015-2016/cape-charles.html>`__.)

tl;dr
-----

When your type hints seem ungainly and large, consider **Exposing the
Intermediate Types**. Break down a big structural type hint into the
constituent pieces.

If you had to create a class definition for EVERY variation on list,
dict, set, and tuple, what would your new class be named?

If you had to describe the underlying meaning of a class -- separate
from it's structure -- what name would you give it?

Picking names is one of the two hardest problems in computing. It
isn't easy. (The other hardest problem? Cache invalidation and
off-by-one errors.)



