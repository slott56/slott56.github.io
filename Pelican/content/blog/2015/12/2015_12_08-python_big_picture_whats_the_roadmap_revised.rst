Python Big Picture -- What's the "roadmap"? [Revised]
=====================================================

:date: 2015-12-08 07:29
:tags: #python,building skills books
:slug: 2015_12_08-python_big_picture_whats_the_roadmap_revised
:category: Technologies
:status: published

Here's an interesting idea: http://www.xmind.net/m/WvfC/
This is associated with the following question: "I've had a hard time
finding the Big Picture re: Python, and it makes it difficult ... to
proceed and prioritize my efforts without one."


An interesting question: what **is** the overview or strategy for
mastering Python?
In this case, the focus is on "Big Data", but I've found that to be
merely a tangential. The application area has a small influence, and
then only around the fringes of the language and libraries.


I'm going to disagree with several particulars on the mind map. I'll
present an alternative, with a point-by-point commentary on the mind
map. (And I'll eschew the graphics, I don't find them helpful.)

Foundation
----------

The language itself is (duh) the foundation. I find it important to
emphasize this because the Python universe is replete with a
seemingly endless supply of packages and libraries that help solve
nearly every problem a programmer might encounter.
This profusion of packages is -- in a way -- it's own problem.
It's obligatory to run the following interaction in Python. (Any
Python 2.7 or 3.2 will work; older Pythons prior to 2.7 need to be
upgraded.)

::

    >>> import antigravity

Yes.

Everything you can imagine is an add-on package. Everything.

But.

That's not the starting point for learning how to solve problems with
Python. That's merely one waypoint along the course. And it's not the
most important waypoint.

Attractive Nuisance
-------------------

We have to set the external libraries aside as an "attractive
nuisance." They're a distraction, in fact. Let's focus on the stuff
that comes with the installation kit: language and library.

When looking at the Language, we actually see two things: Data and
Processing. The "Data" is the built-in data structures: bool, int,
float, complex, exception, context, string, tuple, list, map, set,
lambda, function, class, module and package. The "Processing" is the
imperative programming features: the 21 (or so) statements that
comprise the language.

Both facets are essential, but they're also (approximately)
orthogonal to each other.

For years, I was convinced that the way to learn Python was to come
to grips with most of the imperative statements and then apply these
statements to the various data structures. The tidy orthogonality
between many of the statements and some of the data structures makes
this appealing. I wrote two Python tutorials based on this idea.

My approach was to echo the ancient
`Structured Concurrent Programming with Operating System Applications <http://www.amazon.com/Structured-Concurrent-Programming-Applications-Addison-Wesley/dp/0201029375>`__.
They define a nested series of subsets of a hypothetical PL/I-like
(or Pascal-like) programming language. While the details don't apply
**well** to Python, the approach does make a lot of sense. Start with
constants, expressions and output (i.e., **print**) as the minimal
language. Then add state change via variables, assignment and input.
Then add **if**/**elif**/**else**. Fold in **for** and **while**, and
continue to add features in this careful progression: functions,
exceptions, contexts, generators, etc.

I'm becoming less and less sure that the imperative, procedural
statements should define the roadmap through the language.

It's true that computing is defined by number theory. The original
Turing Machine theorem equates all of number theory to an imperative,
procedural notion of computers and programming. While unconditionally
true, it's not necessarily the most helpful strategy. We could, for
example, start programming by covering Boolean Algebra and Set Theory
first. But it would be a long dull slog before we got to anything
that appeared "useful."

Data Is Central
---------------

I'm starting to see that the data structures are more helpful than
imperative statements. This leads to a different approach to studying
this language. Experienced programmers may feel that a list of
fundamental language topics isn't too helpful.

However. I've noted that many experienced programmers tend to skip
over the unique-to-Python features. This leads them to write clunky
and awkward Python code because they missed something that would lead
to simplicity and clarity.

#.  **int**. Natural numbers are boring but necessary. The first
    explorations of Python can easily be simple expressions, output,
    variables and input using integers.

#.  **bool**. Comparisons and logic allow introduction of the **if**,
    **elif** and **else** statements in a graceful way.

#.  **str**. Strings can be a gentle introduction to objects which are
    collections. Strings have methods, unlike integers and booleans.
    Strings introduce a number of conversion functions (int, float,
    str, hex, oct, etc.) This allows introduction of the
    **for** statement based on this simple collection.

#.  **float** and **complex**. Floating point numbers are an important
    side-bar. They're not central. The notion of "approximation" can't
    be stressed enough, and pathological examples of noise bits at the
    end of floats is absolutely central. The math library is perhaps
    part of this. Also the decimal and rational modules.

#.  **Exception**. For programmers who have a background in languages
    like C (without exceptions) the exception seems complex and
    mysterious. However, for Python they are absolutely central. And
    easy to play with by getting simple Value Errors. This introduces
    the **try**/**except** statements, also. While it's a little
    advanced, the class MyException( Exception ): pass is not a bad
    thing at this point. Yes, it's a bit of a "magical incantation."
    But so is len(string).

#.  **tuple** and **list**. This is an extension to some of the
    discussion of string. It's also a time to introduce mutability and
    show some of the consequences of a mutable list. This introduces
    iterability, also.

#.  **dict** and **defaultdict**. This introduces more loop constructs
    including list comprehensions and various kinds of generator
    expressions.

#.  **set** and **frozenset**. This allows a review of mutability and
    the ways list and tuple differ.

#.  **function** and **lambda**. The **def** and **return**
    statements, plus **global**. Additionally, the sort method of a
    list as well as the sorted iterator function can be looked at in
    some depth.

#.  **file**, **open** and **context**. This includes the
    **with** statement. This is a two-part or three-part exploration.
    It has to include some of numerous library packages for dealing
    with the file system. Plus data representation in CSV and JSON
    files. The way that a file is iterable is essential.

#.  **Iterators**, **generators** and the itertools package. This
    includes techniques for implementing map-reduce algorithms using
    iterators and generators.

#.  **namedtuple**. This is a small thing, but it can help to
    crystalize attribute access and some of the features that are part
    of a class.

#.  **class**. This must include an multi-step excursion into special
    method names.

#.  **module** and **package**.  Note that these are different things.
    Java only offers "package". A Python module is a very, very
    important concept. The module (not the class) is the practical
    unit of reuse. Python is emphatically **not** written in the style
    of Java with one class per file.


Class Definitions
-----------------

The essential goal behind the first 14 topics is to get to the
point where all the language features can be used to create
workable class definitions.

#.  Common object-oriented design patterns. Most of the
    "Gang-of-Four" suite of patterns is relevant to Python. A few
    changes to the textbook examples are required to remove the C++
    and Java biases. Patterns like **State**, **Strategy** and
    **Factory** are central to good OO design. The Python version
    of Singleton has to be treated carefully; the Python Borg
    pattern is rarely useful; on the other hand the concept of
    module global variable is important and underpins some of the
    standard library.

#.  Above and beyond the common design patterns, Python has a
    number of unique design patterns. These are largely exemplified
    by the special method names. **Attribute Access** (properties
    and descriptors). This allows creation of simple collections.

#.  Callable objects allows a review of functions and lambdas,
    also. The Abstract Base Class definitions must be emphasized
    for this to work out well in the long run.

#.  Sequence Types expands simple collections to created ordered
    collections.

#.  Number Types. This allows a complete understanding of decimal
    and rational packages, also.

#.  Some additional design patterns need to be added, also.
    Specifically, things like metaclass and classmethod are
    features of Python that are absent from Java or C++.


Programmers experienced in other languages might object to this
depth in Python OO design techniques and design patterns.



What I find is that programmers who don't really "get" the
Python design patterns (especially the ABC's) overwrite their
programs. They needlessly reinvent methods that are already
first-class features of the language, but weren't well
understood. Properties and descriptors, for example, allow for
a simpler and very clear syntax; it's often better than the
endless parade of explicit getter and setter method calls that
characterize Java Beans programming.



Additionally, bad habits from other languages need to be
unlearned. For example, many Java (and C++) programmers are
taught to overuse the private keyword. When they learn Python,
they think that private is somehow **really important**.  When
the find out about ``__`` (double underscore) name mangling, they
go off the deep end, using ``__`` names everywhere. This is all
bad.



Encapsulation has little to do with private. In Python, the ``_``
(single underscore) prefix on a name is the convention for private. But it's not
like Java's (or C++) compiler-enforced privacy, it's just a
nodding understanding. As the creator of Python says "we're all
adults here." An overused Java private is more of a problem for
proper extension of a Java class than Python's casual
"nudge-nudge-wink-wink-private".


The Standard Library
--------------------

After looking at class definitions, it's important to look at the
default library, subsection by subsection. There is a **lot** to
the installed library.

For most Python programmers, sections 1 to 6 will have been
covered by the previous material. Sections 26 and on to the end,
also, are less important.

Sections 7 to 25 of the library reference contain the centrally
important modules. A familiarity with the list of topics is
essential before tackling "real" projects. This is so important,
we'll use this set of topics as the basis for our point-by-point
commentary on the mind-map linked above.

External Components and Downloads
---------------------------------

One of the reasons why Python is a well-designed language is the
way the principle of orthogonality is applied.


Most statements and data structures play well together. For
example, all the built-in collections are sequences, so that they
are iterable; the **for** statement works directly with
collections.


Also, the external libraries themselves are all independent of the
language, and the language exists without resorting to any of the
external libraries.


Looking at the mind map, there are several interesting topics. And
a few mysteries. And some unhelpful labels. Here's a quick
commentary on the mind map.


-   **Basic Stack**. I supposed these can be called "essential"
    external packages. This seems to be a way to emphasize other
    packages listed elsewhere on the diagram. I'm not sure why this
    topic is here.

-   **Newer Packages**. This is a completely opaque label. Not
    helpful.

-   **Integrated Platforms**. This isn't too helpful, either. I
    suppose one could make a guess based on the list of packages.

-   **Visualization**. Ah. Now we're getting somewhere. These are
    some helpful visualization packages. PIL isn't listed, perhaps
    because it's too primitive.

-   **Data Formats**. YAML isn't listed. The SQL and NoSQL
    categories make precious little sense. Those are all about
    persistence, not data formats. Data format and persistence are
    separate and unrelated. JSON, for example, is a data format.
    CouchDB is persistence.

-   **Packages**. I suppose it's helpful to point out PyPi, but it
    doesn't make sense in this context. This is metadata and
    relatively unhelpful.

-   **Efficiency**. Cython for "efficiency" makes precious little
    sense. Proper data structure and algorithm is the secret to
    efficiency. See my post on a `100:1 speedup in
    Python <{filename}/blog/2013/06/2013_06_27-performance_tuning_running_in_1100th_the_time.rst>`__.
    For efficiency, it's sometimes necessary to drop out of Python
    and write the important 20% of the code in C++.

-   **Parallel**. A non-Windows OS handles parallelism gracefully.
    Process-level parallelism with pipelines is simple and
    efficient. Thread-level parallelism is often more trouble than
    benefit.

-   **GPU**. This is an example of where a little C++ code can go a
    long way to improving the 20% of the code that's the actual
    performance bottleneck.

-   **Glue**. Interfaces to other applications or packages can be
    useful if the other package is actually a first-class part of
    the solution.

-   **MapReduce**. This is essentially persistence, and goes with
    SQL database and noSQL databases. It's also a fundamental
    design pattern that can be exploited trivially in Python.


On this mind-map, there are a few topics that are **really**
important. So important that the topics parallel the Python
library.

-   **Data Persistence**, chapter 11. Databases and Files. This
    includes SQL and noSQL databases as well as pickled data
    structures. Python comes with SQLite, allows SQL development
    without additional downloads. Postgres and MySQL libraries
    often popular because the price is right and the
    functionality is outstanding.

-   **Archive and Compressed Structures**, chapter 12. ZIP, BZ2,
    etc. Compression is sometimes relevant for big data
    projects.

-   **Data Representation and File Formats**, chapters 13, 18
    and 19. CSV, JSON, YAML, XML, HTML, etc. It's important to
    note that JSON is more compact (and almost as expressive) as
    XML. While XML is popular, it's sometimes overused.

-   **OS Features,** chapter 15 and 16. These are tools needed
    to build command-line applications. For Big Data
    applications, logging and command-line parameter parsing are
    essential.

-   **Multiprocessing**. This is it's own design discipline.
    What's important here is that the OS process-level design is
    central. The queue and multiprocess packages are sufficient
    for this. There are some external multiprocessing packages,
    also, like `Zero MQ <http://www.zeromq.org/bindings:python>`__.

-   **Internet Protocols,** chapter 20. This is part of using
    RESTful web services, which is essential for making noSQL
    database (like CouchDB) work. For creating RESTful servers,
    the WSGI approach is essential.

-   **Unit Testing and Documentation**, chapter 25.
    `Sphinx <http://sphinx-doc.org/>`__ is extremely important
    for creating useful documentation with minimal pain.

-   **Visualization**. `matplotlib <http://matplotlib.org/>`__,
    `PIL <http://www.pythonware.com/products/pil/>`__ are
    popular. The built-in turtle package is a bit primitive.
    However, it's also rather sophisticated, and a great deal
    can be done with it.

-   **Numeric Processing**. `numpy <http://www.numpy.org/>`__ or `scipy <http://www.scipy.org/>`__.


Note that the number of external packages on this list is
rather small. Python comes with batteries included.


Admittedly, it's hard to make **general** recommendations
for external packages. But it's misleading to provide a huge
list of external packages when the default suite of packages
will solve a large number of problems gracefully.

Which Python Version?
---------------------

Generally, everything should be done in Python3.2.
In some cases a crucial package hasn't been upgraded to
Python 3.2. In these exceptions, Python 2.7 can be used.

For example, `nltk <http://nltk.org/>`__ is still focused
on Python 2.7.

But.

**Every** Python2.7 program should **always** begin with
``from __future__ import print_function, division``
That's **every** and **always**. All new development should
**always** be focused on Python3.2. There is no rational
exception to this rule.

If there's any need to use the ``input()`` function, then the
following line must be included, also.
``input= raw_input``
This will use the Python 3.2 version of the ``input()``
function.



-----

I don't get the question. What is being "...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2013-06-05 15:54:35.502000-04:00

I don't get the question. What is being "split off" from what? Timelines
mean nothing: making predictions is difficult, especially about the
future. Languages tend to coexist for long, long periods of time.
Witness COBOL. Can you clarify this question?


Thanks. Fixed the scipy reference. I misread their...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2013-06-05 09:46:22.037000-04:00

Thanks. Fixed the scipy reference. I misread their web site. The Cython
version of Python is not a guarantee of efficiency. Preferring Cython
for maintainability or other reasons is fine. But it's not magically
efficient.


Do you think that &quot;big data&quot; and scienti...
-----------------------------------------------------

AppMathDoc<noreply@blogger.com>

2013-06-04 15:23:39.899000-04:00

Do you think that "big data" and scientific computing will split off
from python altogether, perhaps combining with Julia (I've heard
rumblings to that effect)? And if so, what do you foresee as the
timeline for such a split?


Interesting post, thanks for sharing. A few minor ...
-----------------------------------------------------

Ralf Gommers<noreply@blogger.com>

2013-06-04 15:54:27.636000-04:00

Interesting post, thanks for sharing. A few minor comments: scipy
doesn't include visualization (--> matplotlib), and Cython does make an
awful lot of sense if you're trying to build \**maintainable*\*
libraries. Scipy and many other prominent scientific Python libraries
strongly prefer Cython over C, Fortran and C++ for a reason.



arjun<noreply@blogger.com>

2019-08-21 04:57:32.928000-04:00

This comment has been removed by the author.


our very own commitment to getting the message thr...
-----------------------------------------------------

arjun<noreply@blogger.com>

2019-08-21 04:57:17.771000-04:00

our very own commitment to getting the message throughout came to be
rather powerful and have consistently enabled employees just like me to
arrive at their desired goals.
`Surya Informatics <https://twitter.com/surya_infomatic?lang=en>`__


Good Article
------------

Henery<noreply@blogger.com>

2021-03-19 07:30:49.842000-04:00

Good Article


In this case, the emphasis is on “Big Data”, but I...
-----------------------------------------------------

Henery<noreply@blogger.com>

2021-03-19 07:30:34.114000-04:00

In this case, the emphasis is on “Big Data”, but I search that to be
silent surprising. I needed `python django
developer <https://mobilunity.com/blog/hire-django-developer/>`__ for
work. The application area has little effect, and then around the
fringes of language and libraries only. I will agree with many details
on the map in mind. I will bring another option, with a point-by-point
commentary on the map in mind. (And I'll leave out the pictures, I don't
find them useful.) The language itself is (duh) basic. I find it
important to emphasize this because the Python world is filled with a
seemingly endless supply of resources and libraries that help solve
almost every problem a programmer may encounter.





