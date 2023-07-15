Python Enhancement Proposal -- Floating an Idea
===============================================

:date: 2019-02-05 08:00
:tags: #python,object-oriented design,complexity,Design Principles,PEP
:slug: 2019_02_05-python_enhancement_proposal_floating_an_idea
:category: Architecture & Design
:status: published


Consider the following code

::

   def max(m: int, n: int) -> int:
       if m >= n:
           return m
       elif n >= m:
           return n
       else:
           raise Exception(f"Design Error: {vars()}")


There's a question about else: clause and the exception raised there.

-  It's impossible. In this specific case, a little algebra can provide
   that it's impossible. In more complex cases, the algebra can be
   challenging. In some cases, external dependencies may make the
   algebra impossible.

-  It's needless in general. An ``else:`` would have been better than the
   ``elif n >= m:``.  The problem with ``else:`` is that a poor design, or poor
   coordination with the external dependencies, can lead to undetectable
   errors.


Let's look at something a little more complex.

::

   def ackermann(m: int, n: int) -> int:
       if m < 0 or n < 0:
           raise ValueError(f"{m} and {n} must be non-negative")
       if m == 0:
           return n + 1
       elif m > 0 and n == 0:
           return ackermann(m - 1, 1)
       elif m > 0 and n > 0:
           return ackermann(m - 1, ackermann(m, n - 1))
       else:
           raise Exception(f"Design Error: {vars()}")




It's somewhat less clear in this case that the else: is impossible. A
little more algebra is required to create a necessary proof.

The core argument here is **Edge Cases Are Inevitable**. While we can
try very assiduously to prevent them, they seem to be an emergent
feature of complex software. There are two arguments that seem to
indicate the inevitability of edge and corner cases:

-  **Scale**. For simple cases, with not too many branches and not too
   many variables, the algebra is manageable. As the branches and
   variables grow, the analysis becomes more difficult and more subject
   to error.

-  **Dependencies**. For some cases, this kind of branching can be
   refactored into a polymorphic class hierarchy, and the
   decision-making superficially simplified. In other cases, there are
   multiple, disjoint states and multiple conditions related to those
   states, and the reasoning becomes more prone to errors.


The noble path is to use abstraction techniques to eliminate them.
This is aspirational in some cases. While it's always the right thing
to do, we need to check our work. And testing isn't always
sufficient.


The noble path is subject to simple errors. While we can be very,
very, very, very careful in our design, there will still be obscure
cases which are very, very, very, very, **very** subtle. We can omit
a condition from our analysis, and our unit tests, and all of our
colleagues and everyone reviewing the pull request can be equally
snowed by the complexity.


We have two choices.


#.  Presume we are omniscient and act accordingly: use else: clauses
    as if we are incapable of error. Treat all complex if-elif chains
    as if they were trivial.

#. Act more humbly and try to detect our failure to be omniscient.


If we acknowledge the possibility of a design error, what exception
class should we use?


-   **RuntimeError**. In a sense, it's an error which didn't occur
    until we ran the application and some edge case cropped up.
    However. The error was \*always\* present. It was a design error,
    a failure to be truly omniscient and properly prove all of our
    if-elif branches were complete.

-   **DesignError**. We didn't think this would happen. But it did.
    And we need debugging information to see what exact confluence of
    variables caused the problem.


I submit that **DesignError** be added to the pantheon of Python
exceptions. I'm wondering if I should make an attempt to write and
submit a PEP on this. Thoughts?



-----

Personally, I welcome the suggestion because it wo...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-02-05 19:33:41.361000-05:00

Personally, I welcome the suggestion because it would provide me a
formal mechanism for documenting when a client says that x will never
happen.

The downside is that we are adding Yet More Stuff (YMS, pronounced yams)
to Python. This is a judgment call that needs to be made.




