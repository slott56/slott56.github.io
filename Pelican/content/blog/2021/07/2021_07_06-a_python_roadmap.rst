A Python Roadmap
================

:date: 2021-07-06 08:00
:tags: object-oriented programming,functional python programming,#python
:slug: 2021_07_06-a_python_roadmap
:category: Technologies
:status: published

An interesting tweet. The  roadmap has three sections. I'm not sure this
is actually complete, or even grouped correctly. It is a very good list
of topics.

https://twitter.com/prasoonpratham/status/1408435475426254849?s=11

"Here's a complete roadmap of topics to master Python."

The thread, however, seems no longer to exist.

Foundations
-----------

I want start by quibbling about variables being first. I'm not sold on
this.

I think that operators, expressions, and the built-in immutable types
are foundational. int, float, str, and tuple are hugely important as
core concepts in computing and Python.

I also think that "loops" is a sketchy notion and I kind of wish we
wouldn't describe for and while statements as "loops". I think we should
call them iterations. They implement two kinds of logical quantifiers
"for all" and "there exists." I think we should talk about the final
result of a for statement: all of the values in a range are processed.
Similarly a for-if-break construct establishes a "for exists" that
defines the first value in a range for which a condition is met. And
yes, range objects will be central.

I think that a huge amount of programming can be covered with these
topics. I'm not sure "basic" is the right term; **foundations** might be
a better idea.

The use of variables to manage state is part of this. But. Variables,
assignment, and state change are a bit more advanced and maybe shouldn't
be first.

I also think function definitions are foundational. Mathematics has been
defining functions based on other functions. It's a way of providing a
mental short-hand for complex concepts. I don't need to know all the
details of how to compute a square root to make use of square root as a
concept.

The wide varieties of assignment statements, including assignment to
decompose collections aren't mentioned in the original post. This may be
an important omission, causing me to quibble on "complete."

I agree that files and elements of File IO are part of this foundation.
If we limit ourselves to reading and writing files, then they're
essentially immutable structures. I think we can safely avoid
update-in-place files because this is an application topic more than a
language topic. Python offers the minimal level of support via seek and
tell, but little more. And most modern application relies on a database
for updatable files.

Data Structures
---------------

Moving from basic to intermediate. I prefer the term "data structures"
which are built on the language foundations. I think that the mutable
built-in data structures come next in the roadmap. My preference is to
omit terms like Object-Oriented or Functional, and focus on list, dict,
and set, and how the iteration works. This means comprehensions and
generators are part of this essential data structure section.

No, comprehensions aren't and shouldn't be called "advanced." They're
very much a core concept. Thinking about statements to implement a
map/filter/reduce over a collection is the essence of a great deal of
programming. We don't always learn it that way, but it needs to be
presented in that framework even to beginners. A pile of for and if
statements and a bunch of variables is a programmer's first step toward
a simpler comprehension. In both cases, they're doing a mapping and it
needs to be described as mapping one collection to another collection.

This is where the standard library collections module is introduced.

Yes it's part of the library. I think it's too central to be ignored. I
think dataclasses belong here, too.

Talking about the mutable data structures means revisiting the for
statement and using it on a variety of iterables. The way Python's
concepts apply to a variety of data types is an important feature of the
language. (In the olden days, they used to talk about "orthogonality" of
data and processing; we don't need to dwell on it, but I think it helps
to acknowledge it.)

Functional Programming
----------------------

It appears to me that the functional programming topics can come next.
The idea of functional composition via higher-order functions and
decorators builds on the existing foundation. This is where map() and
filter() belong. Because of the way sorted(), max(), and min() work on
collections with a key= function, these are part of the functional
programming roadmap. The inconsistency between map() and functions like
max() is an important thing to note.

I also think itertools belongs here. We can make the case that it's in
the standard library, but then, so is io. I think itertools and
functools are as central to practical Python as the math module and
collections.

I think typing.NamedTuple and dataclasses belong here, also. A frozen
dataclass is stateless, and can be helpful when creating list
comprehensions to perform a mapping from one collection to another
collection.

Object-Oriented Programming
---------------------------

I think OO programming and related concepts build on the previous
material. Class definitions and state management aren't simple, even
though they're essential parts of Python.

To an extent, OO programming can be decomposed into two layers. While I
hate to overuse "foundation", there seem to be two parts:

OO Foundations -- inheritance, composition, and different kinds of
delegation. This tends to expose a number of common design patterns like
Strategy, Decorator, and Facade.

OO Features -- this includes metaprogramming, decorators, ABC's, mixins,
and the like. These topics are all designed to avoid copy-and-paste in
sophisticated edge cases that cross class boundaries.

Concurrency
-----------

I'm not sure why concurrency and parallelism are separate topics in the
original list. I've had folks try to split this hair a number of ways.
The idea is to find a place where async lives that's "concurrency lite"
or something.

The concepts here become blurry because threads and processes are OS
features, not language features. The async/await language features,
however, are clearly part of Python. It becomes particularly awful when
working on something practical where asyncio doesn't provide the feature
you need. Specifically, blocking file system I/O isn't part of asyncio
and requires an explicit appeal to the underlying thread pool for the
blocking operation.

To an extent, async/await needs to be on the roadmap. It's tricky,
though, to cover this without also digressing into threads as a way to
deal with blocking operations.

Test, Integration, and Deployment
---------------------------------

This is where tools show up. This is where pip, unittest, pytest,
tox/nox, coverage, etc. live. Are these part of the language? Or are the
part of the broader ecosystem?

I submit they're explicitly not part of the language. The roadmap ends
just before this topic. The idea is that we should have a Python roadmap
that uses the language and the standard library.

Once we've talked about the language (and some of the library) we can
move on to pip and packaging. I don't think pip is and "intermediate"
topic. I find that premature introduction of pip is a sign of trying to
create useful interesting examples. Examples that don't use pip wind up
being kind of boring. Everyone wants to play with pygame and pillow and
other kinds of projects, but, those aren't foundational to the language.
They're interesting and appealing and -- frankly -- a lot of fun.

tl;dr
-----

I'm not a fan of the roadmap. I like some of it. I don't like some of
it.

I am a fan of presenting the idea for discussion.

.. |image1| image:: https://pbs.twimg.com/profile_images/1406630977158320129/a_EJlPoK_normal.jpg
   :width: 48px
   :height: 48px
   :target: https://twitter.com/prasoonpratham?s=11

.. |image2| image:: https://ea.twimg.com/email/self_serve/media/spacer.png
   :width: 8px

.. |image3| image:: https://ea.twimg.com/email/self_serve/media/logo_twitter-1497383721365.png
   :width: 24px
   :height: 20px

.. |image4| image:: https://ea.twimg.com/self_serve/media/spacer_464x1-1582829598167.png
   :width: 464px
   :height: 1px





