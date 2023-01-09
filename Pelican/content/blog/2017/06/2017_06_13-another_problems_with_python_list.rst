Another "Problems With Python" List
===================================

:date: 2017-06-13 08:00
:tags: #python
:slug: 2017_06_13-another_problems_with_python_list
:category: Technologies
:status: published


This: https://darkf.github.io/posts/problems-i-have-with-python.html

Summary.

#. Slow.
#. Threads.
#. Legacy Python 2 Code.
#. Some Inconsistencies.
#. Functional Programming.
#. Class Definitions Don't Have Enough Features.
#. Switch Statement.


 

Responses.

#. Find the 20% that needs a speedup and write that in C. Most of the
   time that's already available in numpy. The rest of the time you may
   have found something useful.

#. Generally, most folks make a hash of threaded programming. A focus on
   process-level parallelism is simpler and essentially guarantees
   success by avoiding shared data structures.

#. Maybe stop using the legacy projects?

#. Yup.

#. Proper functional programming would requires an optimizer, something
   that doesn't fit well with easy-to-debug Python. It would also
   require adding some features to cope the optimization of functional
   code (e.g., monads.) It seems to be a net loss.
   And `http://coconut-lang.org <http://coconut-lang.org/>`__.

#. Consider a metaclass that provides the missing features?

#. I can't figure out why 'elif' is considered hard to use. The more
   complex matching rules are pretty easy to implement, but I guess this
   falls into the "awful hacks" category.


 

What causes me to write this is the lack of concrete "do this instead"
for most of the points. It sounds too much like empty complaining.

I hope for some follow-on from
`this <https://twitter.com/dbader_org/status/864311190599720960>`__ on
Twitter:

    "Problems I Have With Python" (from a long-time Python user)
    https://t.co/CWYTdsge70

    — Dan Bader (@dbader_org) `May 16,
    2017 <https://twitter.com/dbader_org/status/864311190599720960>`__

But I'm not optimistic. It's too easy to complain and too hard to solve.





