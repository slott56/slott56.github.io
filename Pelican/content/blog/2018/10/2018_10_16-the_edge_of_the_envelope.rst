The Edge of the Envelope
========================

:date: 2018-10-16 08:00
:tags: #python,mypy,mastering object-oriented python
:slug: 2018_10_16-the_edge_of_the_envelope
:category: Technologies
:status: published

I don't -- generally -- think of myself as an edge-of-the-envelope
developer. I'm a tried-and-proven kind of engineer. I want stuff that's
been around for years, with a long history of changes.
Except.
Today.
Currently, I'm revising `Mastering Object-Oriented
Python <https://www.packtpub.com/application-development/mastering-object-oriented-python>`__.
Second Edition.
That means upgrading everything to Python 3.7 with full type hints
throughout almost all of the 18 chapters. (SQLAlchemy presents some
problems, so we're not going deep there.)
The chapter on foundational WSGI applications is \*\ **totally**\ \*
broken. I can't get anything to work with mypy. (The unit tests run, but
mypy complains. Loudly.) Of course, I tried every wrong thing for three
solid days. Then I pulled the stub file from typeshed and realized how
dumb I was.
Okay. I finally got the correct type hints. Yay!
But.
Something in **mypy** is balking at the start_response() function calls.
Too many arguments.
Read the issues. Hm. Stack Overflow. Hm.
Just to be **sure**, I updated to the new 0.630 release in September,
2018.
Problem solved. So. I've arrived at the edge of the envelope. I now
require the absolutely latest and greatest mypy release. By the time I'm
done with the rewrites, this release will be ancient history. But today,
it was wonderful to get past the examples.





