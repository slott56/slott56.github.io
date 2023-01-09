Functional Python Programming
=============================

:date: 2015-02-24 08:00
:tags: packtpub,#python,functional programming
:slug: 2015_02_24-functional_python_programming
:category: Technologies
:status: published

New from Packt Publishing: `Functional Python
Programming <https://www.packtpub.com/application-development/functional-python-programming>`__.
Also here on
`Amazon <http://www.amazon.com/Functional-Python-Programming-Steven-Lott/Functional+Python+Programming>`__.
The fun part is covering generator functions, iterators, and
higher-order functions in some real depth. There's a lot of powerful
programming techniques available.
What's challenging is reconciling Python's approach to FP with languages
that are **purely** functional like Haskell and OCaml and others. Years
ago, I saw some discussion in Stack Overflow that Python simply wasn't a
proper functional programming language because it lacked some features.
I'm vague on specifics (perhaps there weren't any) but the gaps between
Python and FP are narrow.
As far as I can tell, the single biggest features missing are non-strict
evaluation coupled with an optimizer that can rearrange expressions to
optimize performance. This feature pair also tends to also produce nice
tail-call optimization of recursions.
Languages which are totally non-strict (or fully lazy) need to introduce
*monads* so that some ordering can be enforced in the cases where
ordering really does matter.
Since Python is strict (with only minor exceptions) monads aren't
needed. But we also sacrifice some optimization capability because we
can't reorder Python's strict expressions. I'm not sure this is a gap
which is so huge that we can indict Python as being non-functional or
not suitable for a functional approach. I think the lack of an
optimizing compiler is a little more than an interesting factoid.
An interesting problem that compiled functional languages have is
resolving data types properly. It's a problem that all statically-typed
languages share. In order to write a really generic algorithm, we either
have to rely on a huge type hierarchy or sophisticated type
pattern-matching rules. Python eschews this problem by making all code
generic with respect to type. If we've applied a function to an
inappropriate object, we find out through unit testing that we have
TypeError exceptions.
I think we can (and should) borrow functional programming design
patterns and reimplement them in Python. This is quite easy and doesn't
involve too much work or overhead. For example, the yield from statement
allows us to do manual tail-call optimization rather than trusting that
the compiler will recognize the code pattern.



-----

Thanks for sharing, very informative. Top <a href=...
-----------------------------------------------------

Learn Hacking<noreply@blogger.com>

2019-11-22 12:20:44.141000-05:00

Thanks for sharing, very informative. Top `Programming
Languages <https://youtu.be/LCc6kv4H0Dw>`__ in 2020.





