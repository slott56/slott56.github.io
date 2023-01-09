Optimizing complex generator expressions [Updated]
==================================================

:date: 2016-10-20 19:39
:tags: generator expressions,functional python programming,#python
:slug: 2016_10_20-optimizing_complex_generator_expressions_updated
:category: Technologies
:status: published


See this: https://twitter.com/jakevdp/status/786920174595158018

The core expression is similar to this

::

    y = (f(x) for x in L if f(x) is not None)

There are a lot of variations on the filter. The point is that the
function appears twice in the above expression.

We have a number of alternatives.

-  ``y = filter(None, f(x) for x in L)``
-  ``y = filter(None, map(f, L))``
-  ``y = (x for x in map(f, L) if x)``
-  ``y = (x for x in (f(y) for y in L) if x is not None)``
-  ``y = (val for x in L for val in (f(x),) if val is not None)``




My preference is two steps, even though I don't really have a good
reason for this.

::

    y1 = (f(x) for x in L)
    y2 = (f for f in y1 if f)


The thread leads to this
path: https://twitter.com/TomAugspurger/status/786922167522828289  and
the idea of "Let Bindings." We could extend the language slightly to
bind a variable within the confines of the generator expression.


Like this:

::

    y = (f(x) as val for x in L if val is not None)


The **as** clause binds the **f(x)** to **val** so that it can be
used in the **if** clause.


Summary: Interesting.





