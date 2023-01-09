RESTful Web Services Design
===========================

:date: 2018-04-03 08:00
:tags: REST
:slug: 2018_04_03-restful_web_services_design
:category: Technologies
:status: published

| This -- `REST is the new
  SOAP <https://medium.freecodecamp.org/rest-is-the-new-soap-97ff6c09896d>`__
  -- has so many demolished strawman arguments that it feels like
  looking at a van Gogh painting of people harvesting wheat.
| I won't dive into listing all the strawmen. Most of my responses are
  approximately "How is that an actual problem?" or "Yes, it was new to
  you, so?" or "Yes, people disagreed with each other over an
  implementation choice."
| Some of the observations about "proper REST" vs. "bah, that's not
  really RESTful" point out the differences between expedient REST-like
  design and really good REST design. Some of these considerations can
  be helpful.
| The one point worthy of deeper thought is the nature of verb-heavy
  highly-stateful RPC design and RESTful noun-heavy design. The question
  here is the definition of state and the nature of state change. Some
  people appear to be enthralled with many nuanced state changes. I've
  been doing too much data warehouse and functional design where the
  data is essentially stateless and CRUD rules are refined down to CRD
  with a rare U under limited circumstances.
| And, yes, that means using relatively "stateless" OO design where an
  object is wrapped inside a new object that includes derived data or a
  compositions of stateless objects. The following example leverages
  duck typing to create immutable objects where the class reflects the
  state of the object.

::

   class Thing:
       def __init__(self, a, b):
           self.a, self.b = a, b
       def set_c(self, c):
           return DerivedThing(self, c)

   class DerivedThing:
       def __init__(self, thing: Thing, c):
           self.thing, self.c = thing, c
       @property
       def a(self):
           return self.thing.a
       @property
       def b(self):
           return self.thing.b
       @property
       def value(self):
           return self.a * self.c + self.b

| 
| And, yes, I'm not building things which are absolutely stateless
  because Python has stateful lists and mappings, and web services rely
  on stateful persistence. And, yes, I reject functional purism because
  I'm stupid. Can we move on, now?
| Something that seemed essential to me (but appears to be confusing
  from reading complaints about REST) is understanding the notion of
  "state." One view of state is an aggregation of details. The final
  state of an object is a reduction over the changes -- akin to a sum(),
  max(), or min(), or perhaps something more involved like last(). The
  paucity of REST verbs is **not** a problem when you understand
  *current* state as the end product of applying a journal of *previous*
  state change mementos. Each "change", then, isn't a complex Update
  (REST Put or Patch) where there aren't enough verbs to describe each
  nuanced change. It's a Create (REST Post) of the next change memento.
  The RESTful service can eagerly apply the change to compute the
  current state. Or it can lazily apply the changes to compute the
  current state.
| Some of the blog post cited above sounds like "it was new and I didn't
  like it." Therefore, read the article, locate the strawmen, and know
  there will always be someone who will complain. Some of the complaints
  will have merit, some will be whining about the novelty.
| In a RESTful context, I'm a fan of this kind of pattern.
| /things
|     post:
|         summary: Creates a new thing with a and b
|     responses:
|         201:
|             description: thing was created
| /things/{id}/c
|     post:
|         summary: Sets a value of c for an existing thing, previous
  value is discarded.
|     responses:
|         201:
|             description: c property of thing {id} was set
|
| For more useful advice, start here, for example: `RESTful API
  Designing guidelines — The best
  practices <https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9>`__.
  Articles like this are useful, too: `10 Best Practices for Better
  RESTful
  API <https://blog.mwaysolutions.com/2014/06/05/10-best-practices-for-better-restful-api/>`__.





