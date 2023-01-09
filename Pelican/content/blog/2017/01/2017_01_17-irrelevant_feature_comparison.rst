Irrelevant Feature Comparison
=============================

:date: 2017-01-17 08:00
:tags: #python,GW-Basic,haskell
:slug: 2017_01_17-irrelevant_feature_comparison
:category: Technologies
:status: published

A Real Email.

   So, please consider creating a blog post w/ a title something like
   "Solving the Fred Flintstone Problem using Monads in Python and
   Haskell"


First. There's this: https://pypi.python.org/pypi/PyMonad/ and
this: http://www.valuedlessons.com/2008/01/monads-in-python-with-nice-syntax.html.
Also, see https://en.wikipedia.org/wiki/Type_class. I think this has
been covered nicely.

I can't improve on what's been presented.

Second. I don't see any problems that are solved *well* by monads in
Python. In a lazy, optimized, functional language, monads can be used
bind operations into ordered sequences. This is why file parsing and
file writing examples of monads abound. They can also be used to bind
a number of types so that operator overloading in the presence of
strict type checking can be implemented. None of this seems helpful
in Python.

Perhaps monads will be helpful with Python type hints. I'll wait and
see if a monad definition shows up in the typing module. There, it
may be a useful tool for handling dynamic type bindings.

Third. This request is perilously close to a "head-to-head"
comparison between languages. The question says "problem", but it is
similar to asking to see the exact same algorithm implemented in two
different languages. It makes as much sense as comparing Python's
built-in complex type with Java's built-in complex type (which Java
doesn't have.)

Here's the issue. I replace *Fred Flintstone* with "Parse JSON
Notation".  This is a cool application of monads to recognize the
various sub-classes of JSON syntax and emit the correctly-structured
document.  See http://fssnip.net/bq/title/JSON-parsing-with-monads.

In Python, this is import json. This isn't informative about the
language. If we look at the Python code, we see some operations that
might be considered as eligible for a rewrite using monads. But
Python isn't compiled and doesn't have the same type-checking issues.
The point is that Python has alternatives to monads.

Fourth. It's just asking about a not-required feature to a language.
In the spirit of showing the not-required-in-Python features, I'll
show the not-required-in-Python GOTO.

Here it is:


::

      def goto(destination):
          global next
          next = destination

      def min_none(sequence):
          try:
              return min(sequence)
          except ValueError:
              return None

      def execute(program, debug=False, stmt=None):
          global next, context
          if stmt is None:
              stmt = min(program.keys())
              context = {'goto': goto}
          while stmt is not None:
              next = min_none(list(filter(lambda x: x>stmt, program.keys())))
              if debug:
                  print(">>>", program[stmt])
              exec(program[stmt], globals(), context)
              stmt = next

      example = {
      100: "a = 10",
      200: "if a == 0: goto(500)",
      250: "print(a)",
      300: "a = a - 1",
      400: "goto(200)",
      500: "print('done'()",
      }

      execute(example)

This shows how we can concoct an additional feature that isn't really
needed in Python.
Given this, we can now compare the GOTO between Python, BASIC, and
Haskell. Or maybe we can look at Monads in BASIC vs. Haskell.





