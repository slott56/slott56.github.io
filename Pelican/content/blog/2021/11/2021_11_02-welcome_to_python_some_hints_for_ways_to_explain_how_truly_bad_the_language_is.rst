Welcome to Python: Some hints for ways to explain how truly bad the language is
===============================================================================

:date: 2021-11-02 14:55
:tags: #python,PEP
:slug: 2021_11_02-welcome_to_python_some_hints_for_ways_to_explain_how_truly_bad_the_language_is
:category: Technologies
:status: published

As an author with many books on Python, I'm captivated by people's hot
takes on why Python is so epically bad. Really Bad. Uselessly Bad.
Profoundly Broken. etc.

I'll provide some hints on topics that get repeated a lot. If you really
need to write a blog post about how bad Python is, please try to take a
unique approach on any of these common complaints.  If you have a blog
post half-written, skip to the **tl;dr** section to see if your ideas
are truly unique.

Whitespace
----------

Please don't waste time complaining about having to use whitespace in
your code. I'm sure it's a burden on your soul to configure your editor
to indent in groups of four spaces. I'm sorry it's so painful. But.
Python isn't the only language with whitespace.

The shell scripting language has semantic whitespace. (It's not used for
indentation, but please try ``cat$HOME/.bashrc`` (without any spaces)
and tell me what happens. Spaces matter in a lot of languages.

Even in C, some whitespace is semantic. The rest of the whitespace is
for humans to read your code.

If you're \*sure\* that indentation is a fatal problem, please provide
an example in the language of your choice where the ``{}``'s or the

case/esac

was \*required\* because ordinary, readable indentation didn't --
somehow -- express the nesting.

The example can be the basis for a Python Enhancement Proposal (PEP) to
fix the whitespace problem you've identified.

The ``self`` Instance Variable
------------------------------

Using ``self`` everywhere is simpler than using ``this`` in those
obscure special cases where it's ambiguous. Python developers are sure
that being uniformly explicit is a terrible burden on your soul. If you
really feel that obscure special cases are required, consider writing a
pre-processor to sort out the special cases for us.

I'm sure there's a way to inject another level of name resolution into
the local v. global choices. Maybe local-self-global or
self-local-global could be introduced.

Please include examples. From this a Python Enhancement Proposal can be
drafted to clarify what the improvement is.

No Formal Constants
-------------------

Python doesn't waste too much time on keywords, like ``const``, to alter
the behavior of assignment. Instead, we tend to rely on tools to check
our code.

Other languages have compilers to look for assignment to consts. Python
has tools like flake8, pyflakes, pylint, and others, to look for this
kind of thing. Conventionally, variables at the module level with
ALL_CAPS names are likely to be constants. Multiple assignment
statements would be a problem. Got it.

"Why can't the language check?" you ask. Python doesn't normally have a
separate compile pass to pre-check the code. But. As I said above, you
can use tools to create a pre-checking pass. That's what most of us do.

"But what if someone accidentally overwrites a constant?" you insist.
Many folks would suggest some better documentation to explain the
consequences an clarify how unit tests will fail when this happens.

"Why should I write unit tests to be sure a constant wasn't changed?"
you demand. I'm not really insisting on it. But you said you had
developers who would "accidentally" overwrite a constant in an
assignment statement, and you couldn't use tools like pylint to check
for it. So. I suggested another choice. If you don't like that, use
enums. Or write documentation and explain which global items can be
changed and which can't be changed.

BTW. If you have global variables that are NOT constants, consider this
a code smell.

If you really need a mixture of constants and variables as module
globals, you can use the ``enum`` module to create named attribute
values of a class definition. You get constants and a namespace. It's
pretty sweet.

Lack of Privacy
---------------

It appears to be an article of faith that a ``private`` keyword is
*unconditionally* required.

Looking at the history of OO languages, it looks like ``private`` seems
to have been introduced with C++. Not every OO language has the same
notion of private the C++ has. CLU has no concept of private. Smalltalk
considers instance variables equivalent to C++ ``protected``, not
``private``. Eiffel has a particularly sophisticated feature exportation
that doesn't involve a trivial private/public distinction.

Since many languages that aren't C++ or Java have a variety of
approaches, it appears private isn't required. The next question, then,
is it necessary?

It really helps to have a concrete example of a place where a private
method or attribute was absolutely essential. And it helps to do this in
a way that a leading \_ on the variable name -- every time it's used --
is **more** confusing than a keyword like private somewhere else in the
code.

It also helps when the example does not involve a hypothetical Idiot
Developer who (a) doesn't read the documentation and (b) doesn't
understand the ``_leading_underscore`` variable, and can still manage to
use the class. It's not that this developer doesn't exist; it's
questionable whether or not a complex language feature is better than a
little time spent on a code review.

It helps when the example does not include the mysterious Evil Genius
Developer who (a) reads the documentation, and (b) leverages
the ``_leading_underscore`` variable to format one of the OS disks or
something. This is far-fetched because the Evil Genius Developer had
access to the Python source, and didn't need a sophisticated subclassing
subterfuge. They could simply edit the code to remove the magical
privacy features.

No Declarations
---------------

Python is not the only language where variables don't have type
declarations. In some languages, there are implied types associated with
certain kinds of names. In other languages, there are naming conventions
to help a reader understand what's going on.

It's an article of faith that variable declarations are essential. C
programmers will insist that a ``void *`` pointer is still helpful even
though the thing to which it points is left specifically undeclared.

C (and C++) let you cast a pointer to -- well -- anything. With
resulting spectacular run-time crashes. Java has some limitations on
casting. Python doesn't have casting. An object is a member of a class
and that's the end of that. There's no wiggle-room to push it up or down
the class hierarchy.

Since Python isn't the only language without variable declarations, it
raises the question: are they necessary?

It really helps to have a concrete example of a place where a variable
declaration was absolutely essential for preventing some kind of
behavior that could not be prevented with a pylint check or a unit test.
While I think it's impossible to find a situation that's untestable and
can only be detected by careful scrutiny of the source, I welcome the
counter-example that proves me wrong.

And. Please avoid this example.

::

   for data in some_list_of_int:
       if data == 42:
           print("data is int")
   for data in some_list_of_str:
       if data == "bletch":
           print("data is str")

This requires reusing a variable name. Not really a good look for code.
If you have an example where there's a problem that's not fixed by
better variable names, I'm looking forward to it.

This will change the world of Python type annotations. It will become an
epic PEP.

Murky Call-By-Value Semantics
-----------------------------

Python doesn't have primitive types. There are no call-by-value
semantics. It's not that the semantics are confusing: they don't exist.
Everything is a reference. It seems simpler to avoid the special case of
a few classes of objects that don't have classes.

The complex special cases surrounding unique semantics for bytes or ints
or strings or something requires an example. Since this likely involves
a lot of hand-waving about performance (e.g., primitive types are faster
for certain things) then benchmarking is also required. Sorry to make
you do all that work, but the layer of complexity requires some
justification.

No Compiler (or All Errors are Runtime Errors)
----------------------------------------------

This isn't completely true. Even without a "compiler" there are a lot of
ways to check for errors prior to runtime. Tools like flake8, pyflakes,
pylint, and mypy can check code for a number of common problems. Unit
tests are another common way to look for problems.

Code that passes a unit test suite and crashes at runtime doesn't seem
to be a language problem. It seems to be a unit testing problem.

"I prefer the compiler/IDE/something else find my errors," you say.
Think of pylint as the compiler. Many Python IDE's actually do some
static analysis. If you think unit tests aren't appropriate for finding
and preventing problems, perhaps programming isn't your calling.

tl;dr
-----

You may have some unique insight. If you do, please share that.

If on the other hand, you're writing about these topics, please realize
that Python has been around for over 30 years. These topics are not new.
For the following, please try to provide something unique:

-  Whitespace
-  The self Instance Variable
-  No Formal Constants
-  Lack of Privacy
-  No Declarations
-  Murky Call-By-Value Semantics
-  No Compiler (or All Errors Are Run-Time Errors)

It helps to provide a distinctive spin on these problems. It helps even
more when you provide a concrete example. It really helps to write up a
Python Enhancement Proposal. Otherwise, we can seem dismissive of Yet
Another Repetitive Rant On Whitespace (YARROW).



-----

I used to whine about the lack of case/switch stat...
-----------------------------------------------------

Jim Collins<noreply@blogger.com>

2021-11-17 13:22:29.382000-05:00

I used to whine about the lack of case/switch statements until a) people
showed me how to work around it and b) it got fixed in 3.10.





