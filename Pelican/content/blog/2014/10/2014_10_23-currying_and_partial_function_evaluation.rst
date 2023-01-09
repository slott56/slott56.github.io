Currying and Partial Function Evaluation
========================================

:date: 2014-10-23 08:00
:tags: #python,functional programming
:slug: 2014_10_23-currying_and_partial_function_evaluation
:category: Technologies
:status: published

Old. But still interesting.
`Partial Function Application is not
Currying <http://www.uncarved.com/index.py/blog/not_currying.mrk>`__
It seems like hair-splitting. However, the distinction between bound
variables and curried functions does have *some* practical implications.
I'm looking closely at
`PyMonad <https://pypi.python.org/pypi/PyMonad/>`__ and the built-in
`functools <https://docs.python.org/3/library/functools.html>`__
library.
I'm finding some benefits in understanding functional programming and
how to apply functional design patterns in Python. I'm also seeing the
important differences between compiled -- and optimized languages -- and
Python's approach. I'm slowly coming to understand how a (simple)
recursive design is flattened into a **for** loop as part of manual
tail-recursion optimization.
The functional programming goodness is giving me first-class headaches
when trying to apply the lessons learned to Java, however. I suppose I
should look closely
at `http://www.functionaljava.org <http://www.functionaljava.org/>`__ and https://code.google.com/p/functionaljava/.
There are claims that it's dangerously inefficient. Also, the customer
who insists on Java has a (very) limited set of allowed libraries; if
this isn't on the list, then the whole concept is a non-starter.





