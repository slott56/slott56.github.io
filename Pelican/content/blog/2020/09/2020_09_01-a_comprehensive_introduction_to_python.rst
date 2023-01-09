A Comprehensive Introduction to Python
=======================================

:date: 2020-09-01 08:00
:tags: #python
:slug: 2020_09_01-a_comprehensive_introduction_to_python
:category: Books
:status: published

Python 101, by Michael Driscoll. 545 pages, available from leanpub.com
in a variety of formats. Available soon in hardcover.

The modern Python programming language is a large topic. A book on a
programming language has to be seen as a collection of several large
topics.

At its core, a book on a programming language has to cover the syntax of
the language. What’s for more important is covering the underlying
semantics of the various constructs. Software captures knowledge, and
it’s essential for a book on a programming language to make it clear how
the language expresses knowledge.

For a programming expert, a fifteen page technical report can be enough
to get started with a new language. When I was first learning to
program, that’s all there was. For the vast majority of people who come
in contact with programming, there’s a lot more information required.

This leads to a number of interesting tradeoffs when writing about a
programming language. How much of a book should be devoted to installing
the language tools? How much should it cover the other tools required to
create software? I think Python 101 makes good choices.

In the modern era of open-source software, the volume and sophistication
of the available tools can be daunting. An author must consider how many
words to invest in text editors, debuggers, performance measurement,
testing, and documentation. These are all important parts of producing
software, they’re often tied closely with a language, but these
additional tools aren’t really the language itself.

A language like Python offers a rich collection of built-in data types.
A book’s essential job is to cover the data structures (and algorithms)
that are first-class parts of the Python language. A focus on data puts
the various syntactic elements (like statements) into perspective. The
break statement, for example, can’t really be discussed in isolation.
It’s part of the conversation about for statements and conditional
processing in if statements. Because Python 101 follows this data-first
approach, I think it can help build comprehensive Python skills.

The coverage of built-in data structures in a modern language needs to
include file objects. While Python reads strings and bytes, the standard
library provides ways to read HTML, CSV, JSON, and XML documents.
Additional packages provide access to Excel spreadsheet files. While,
technically, not part of the language, these are essential parts of the
problem domain a programming language like Python is designed to
address. Because these are part of the book, a reader will be empowered
to solve practical problems.

There was a time when a programming “paradigm” was part of a book’s
theme. Functional programming, procedural programming, and
object-oriented programming approaches spawned their own libraries. Some
languages have a strong bias. Other languages, like Python, lack a
strong bias. A developer can work with functions, using material from
the first seventeen chapters of Python 101 and be happy and successful.
Moving into class definitions can be helpful for simplifying certain
kinds of programs, but it’s not required, and a good book on Python
should treat classes as a sensible alternative to functions for handling
more complex object state and bundle operations with the state.

Moving beyond the language itself, a book can only pick a few topics
that can be called “advanced.” This book looks at some of the language
internals, exposed via introspection. It touches on some of the standard
library modules for managing subprocesses and threads. It covers tools
like debuggers and profilers. It expands to cover development
environments like the Jupyter Notebook, also. I’d prefer to reduce
coverage of threading and switch to Jupyter Lab from Jupyter Notebook.
These are small changes at the edges of large pool of important details.

I’m still waffling over one choice of advanced topics. Does unit testing
count as an advanced topic? For software professionals, a testing
framework is as important as the language itself. For amateur hackers,
however, a testing framework may be a more advanced topic. The location
of a chapter on unit testing is a telling indication of who the book’s
audience is.

The Python ecosystem includes the standard library and the vast
collection of packages and applications available through the Python
Package Index. These components can all be added to a Python
environment. This means any book on the language must also cover parts
of the standard library, as well as covering how to install  new
packages from the larger ecosystem. Python 101 doesn’t disappoint. There
are solid chapters in PIP and Virtual Environment management. I can
quibble over their  place in Part II. The presence of chapters on tools
is important; Python is more than a language; Python 101 makes it clear
Python is a collection of tools for building on the work of others to
solve problems collaboratively.

I’m not easily convinced that Part IV has the same focus on helping the
new programmer as the earlier three parts. I think packaging and
distribution considerations take the reader too far outside
problem-solving with a programming language and tools. I’m not sure the
audience who sees testing as an advanced topic is ready to distribute
their code. I think there’s room for a Python 102 book to cover these
more professionally-oriented topics.

The volume of material covered by this comprehensive book on Python
seems to require something more elaborate than a simple, linear sequence
of chapters. The sequence of chapters have jumps that seem a little
awkward. For example, from an introduction run-time introduction
introspection, we move to the PIP and virtual environment tools, then
move back to ways to make best use of Python’s annotations and type
hints. Calling this flow awkward is — admittedly — a highly nuanced
consideration. I suspect few people will read this book sequentially;
when each chapter is used more-or-less independently, the sequence of
chapters becomes a minor side-bar consideration. Each chapter has
generous examples and there are screen shots where necessary.

The scope of this book covers the language and the features through
Python 3.8 in a complete and intelligible way. The depth is appropriate
for a beginning audience and the examples are focused on simple,
concrete, easy-to-understand code. The presence of review questions in
each chapter is a delight, making it easy to leverage the book for
instructor-guided training. I can imagine covering a few chapters each
week and quizzing students with the review questions. Some of the
questions are nicely advanced and can lead to further exploration of the
language.

If you’re new to Python, this should be part of your Python reading
list. If you’ve just started and need more examples and help in using
some of the common tools, this book will be very helpful. If you’re
teaching or helping guide people deeper into Python, this may be a
helpful resource.

Driscoll’s colorful nature photos are a bonus. My Kindle is limited to
black and white, and the pictures would have been disappointing. I’m
glad I got the PDF version.





