The Depths of Degradation or How to Reduce
==========================================

:date: 2017-01-09 11:42
:tags: map-reduce,functional python programming,#python
:slug: 2017_01_09-the_depths_of_degradation_or_how_to_reduce
:category: Technologies
:status: published


Let's talk real-world functional programming. Disclosure: I'm a fan of
functional programming in Python.
(This: https://www.packtpub.com/application-development/functional-python-programming)

The usual culprits for functional programming are map(), filter(),
generator functions, and the various comprehensions. This is very
pleasant and can lead to succinct, expressive code.

The reduce operation, however, is sometimes slippery.  The obvious
reductions are sum() and prod().  Some slightly less obvious
reductions are these three:

::

    sum0 = lambda s: sum(1 for _ in s)

    sum1 = lambda s: sum(s)

    sum2 = lambda s: sum(n**2 for n in s)

The first is essentially len(s), but stated more formally. It shows
how we can add in filter or transformations. If we're working with a
collections.Counter object, we can rewrite these three to work with
the values() of a counter. This allows us to have a statistics library
that works with a sequence of simple items or a Counter of binned
items.

(I've left it as an exercise for the reader to create the summaries of
  Counters.)

The Health Check Question
-------------------------


The context is an RESTful application's /health end-point. When a
client does a GET to /health, we want to provide status of the
components on which the app depends as well as a summary.

The details are created like this:

::

    components = (component() for component in COMPONENT_LIST)

    init_components = [thing.init_app(app) for thing in components]

    details = [component.health() for component in init_components]

We have a list of class definitions for each component. We can create
instances of each class. We can initialize these by providing the
RESTful app. Finally, we can create a list of the various health
end-point status codes.

There's a class definition for other RESTful API's. The health check
does a transitive GET to a /health end-point. These are all
more-or-less identical.

There are also class definitions for the database and the cache and
other non-RESTful components. It's all very pretty and very
functional.

Note that the three statements aren't adjacent. They're scattered
around to fit better with the way Flask works. The component list is
in one place. The initialization happens before the first request. The
details are computed as requested.

Also. We don't really use a simple list for the details. It's actually
a mapping from which we will derive a vector. I've left that detail
out because it's a relatively simple complication.

Representation of Health
------------------------


We represent health with a simple enumeration of values:

::

   from enum import Enum
   class Status(Enum):
       OK = "OK"
       DEGRADED = "DEGRADED"
       DOWN = "DOWN"




This provides the essential definition of health for our purposes. We
don't drag around details of the degradation; that's something that we
have to determine by looking at our consoles and logs and stuff.

Degradation is (a) rare, and (b) nuanced. Some degradations are mere
annoyances: one of the servers is being restarted. Other degradations
are hints that something else might be going on that needs
investigation: database primary server is down and we're running on a
secondary.

Summarizing Health
------------------


A subset of the details vector, then, looks like this: [Status.OK,
Status.OK, Status.DEGRADED].

How can we summarize this?

First, we need some rules.  Like these:

::

   class Status(Enum):
       OK = "OK"
       DEGRADED = "DEGRADED"
       DOWN = "DOWN"

       def depth(self, other):
           if self == self.OK:
               return {self.OK: self.OK,
                       self.DEGRADED: self.DEGRADED,
                       self.DOWN: self.DEGRADED}[other]
           elif self == self.DEGRADED:
               return {self.OK: self.DEGRADED,
                       self.DEGRADED: self.DEGRADED,
                       self.DOWN: self.DEGRADED}[other]
           elif self == self.DOWN:
               return {self.OK: self.DEGRADED,
                       self.DEGRADED: self.DEGRADED,
                       self.DOWN: self.DOWN}[other]




The depth() method implements a comparison operator that defines the
relationships. This can be visualized as a table.

======== ======== ======== ========
depth    OK       DEGRADED DOWN
======== ======== ======== ========
OK       OK       DEGRADED DOWN
DEGRADED DEGRADED DEGRADED DEGRADED
DOWN     DOWN     DEGRADED DOWN
======== ======== ======== ========




This allows us to define a function that uses reduce to summarize the
vector of status values.

::

   from functools import reduce
   def summary(sequence): 
       return reduce(lambda a, b: a.depth(b), sequence)


The reduce() function applies a binary operator between items in a
vector. We've used lambda a, b: a.depth(b) to turn the the depth()
method into a binary operator so it can be used with reduce.

The summary() function is a "depth-reduction" of a vector of status
objects. It's defined independently of the actual status objects. The
relationships among the status levels are embedded in the class
definition where they belong. The actual details of status are
pleasantly opaque.

And.

We have an example of map-reduce outside the sphere of big data.

The Integer Alternative
-----------------------

The health rules as shown above are kind of complex. Could they be
simplified? The answer is no.

Here's an alternative -- which does **not** do what we want.

::

      class Status2(IntEnum):
          OK = 1
          DEGRADED = 2
          DOWN = 3

      summary2 = lambda sequence: max(sequence)

This works in some cases, but it doesn't work in others. Another
alternative is to change the order to be OK=1, DOWN=2, DEGRADED=3.
This doesn't work, either. I'll leave it as an exercise to write out
some of the various combinations of values and see how these differ.

JSON Representation
-------------------

The final detail is JSONification of the status vector and the
summary.

::

      json.dumps({"status": summary(vector).name, "details": [s.name for s in vector]})

This converts the various Status objects to text items that fit the
Swagger specification for our /health end-points. The .name attribute
reference is required to get the string labels from the enum. An
alternative is to customize the JSON encoder to recognize the Enum
objects and extract their names.

Conclusion
----------

Map-Reduce is easy. It surfaces in a number of places. The idea helps
encapsulate summarization rules.





