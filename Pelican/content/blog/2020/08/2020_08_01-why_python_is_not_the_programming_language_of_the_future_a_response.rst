Why Python is not the programming language of the future -- a response
======================================================================

:date: 2020-08-01 08:22
:tags: #python
:slug: 2020_08_01-why_python_is_not_the_programming_language_of_the_future_a_response
:category: Technologies
:status: published


See https://towardsdatascience.com/why-python-is-not-the-programming-language-of-the-future-30ddc5339b66.

This is an interesting article with some important points. And. It has
some points that I disagree with.

-  Speed. This is a narrow perspective. numpy and pandas are fast, dask
   is fast. A great many Python ecosystem packages are fast. This
   complaint seems to be unsupported by evidence.

-  Dynamic Scoping Rules. This actually isn't the problem. The problem
   is something about not being able to change containing scopes. First,
   I'm not sure changing nesting scopes is of any value at all. Second,
   the complaint ignores the global and nonlocal statements. The vague
   "leads to a lot of confusion" seems unsupported by any evidence.

-  Lambdas. The distinction between expressions and statements isn't
   really a distinction in Python in general, only in  the bodies of
   lambdas. I'm not sure what the real problem is, since a lambda with
   statements seems like a syntactic nightmare better solved with an
   ordinary, named function.

-  Whitespace. Sigh. I've worked with many people who get the whitespace
   right but the {}'s wrong in C++. The code looks great but doesn't
   work. Python gets it right. The code looks great and works.

-  Mobile App Platform.
   See `https://beeware.org <https://beeware.org/>`__.

-  Runtime Errors. "coding error manifests itself at runtime" seems to
   be the problem. I'm not sure what this means, because lots of
   programming languages have run-time problems. Here's the quote: "This
   leads to poor performance, time consumption, and the need for a lot
   of tests. Like, a *lot* of tests." Performance? See above. Use numpy.
   Or Cuda. Time consumption? Not sure what this means. A lot of tests?
   Yes. Software requires tests. I'm not sure that a compiled language
   like Rust, Go, or Julia require fewer tests. Indeed, I think the
   testing is essentially equivalent.


I'm interested in ways Python could be better.



-----

For ways to improve Python, check out the comments...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2020-04-24 00:54:46.523000-04:00

For ways to improve Python, check out the comments by Jerry Howard at
the following YouTube video
Jeremy Howard: fast.ai Deep Learning Courses and Research \
Artificial
Intelligence (AI) Podcast
Aug 27, 2019 - Lex Fridman
https://www.youtube.com/watch?v=J6XcP4JOHmk


Wow, people are still writing articles like that? ...
-----------------------------------------------------

Wingware<noreply@blogger.com>

2020-04-22 11:46:00.243000-04:00

Wow, people are still writing articles like that? It belies a
fundamental lack of understanding what Python is and how it works. For
one, it's not intended for writing CPU intensive code. Instead, it's the
user-friendly glue that puts things together. In most Python code, very
little time is spent actually spinning the interpreter's wheels; the
work is done in the packages written in C or whatever. That's why
numpy/etc are so fast. Also the idea that compilation can find anything
but a tiny subset of runtime errors is absurd. You need just as many
tests if not more with other languages. Oh well... thanks for posting
this link, though!





