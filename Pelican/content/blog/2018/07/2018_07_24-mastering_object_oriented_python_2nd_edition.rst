Mastering Object-Oriented Python -- 2nd Edition
===============================================

:date: 2018-07-24 08:00
:tags: #python,@PacktAuthors,packtpub,mastering object-oriented python
:slug: 2018_07_24-mastering_object_oriented_python_2nd_edition
:category: Books
:status: published

It's time to revise `Mastering Object-Oriented
Python <https://www.packtpub.com/application-development/mastering-object-oriented-python>`__.
While the previous edition is solidly focused on Python3, it lacks
some important features:

-  F-Strings
-  Type Hints
-  types.NamedTuple
-  Data Classes


So. There's some stuff to add. I don't think there's too much to take
away. I plan to make some things a little more tidy. I will remove
all references to Python2 and all references to how things used to be
and why they're better now.

It will be several months before this is available. Stand by for
updates.


The earliest drafts of this book date back to 2002. Seriously. I've
been over this material a lot in the past 1.5 decades.


The nascent form of this book took me years (maybe 10 years) to
accumulate. It covered **everything**: data structures, statements,
built-in functions, classes, and a bunch of libraries. It was beyond
merely ambitious and off into some void of "cover all the things."


I was motivated by my undergrad CS text books on the foundations of
computer science. The idea of putting the language features into a
parallel structure with boolean algebra, set theory, and number
theory was too cool for words. And -- lacking the necessary formal
background -- it was something I'm not able to present very well.


While I wanted to cover **all** of Computer Science, acquisition
editors were pointed out how crazy that idea was. A focus on the
object-oriented features of Python was sufficient to sell a
distinctive book. And they were absolutely right.


As I rework the outline for the 2nd edition, there are some other
topics that crop up. These are not going to wind up in the book, but
they're an implicit feature of the topics being covered.

CS Foundations and Python
-------------------------


One of the best of the introductory books (which came out after I
graduated) was `Structured Concurrent Programming With Operating
Systems
Applications <https://books.google.com/books/about/Structured_Concurrent_Programming_With_O.html?id=GPsmAAAAMAAJ>`__.
They presented a nested collection of sub-languages: SP/k. The
organization of the nested subsets can be helpful for exposing
programming incrementally. There are issues, and we'll look at them
in detail below. Here's the collection of subsets from the original
book (and related articles.)


-   SP/1 expressions and output. The print() function.

-   SP/2 variables, assignment, and the input() function.

-   SP/3 selection and repetition. The Python if and while constructs
    are the logical minimum, but the for statement makes more sense
    because it's so widely used.

-   SP/4 character strings.

-   SP/5 arrays. Python lists, really.

-   SP/6 procedures. Python function definition.

-   SP/7 formatted input-output. f-strings for output, and regular expressions for parsing.

-   SP/8 records and files.


There are a lot of gaps between this list of subsets and modern
programming languages. SP/k was explicitly based on subset of PL/I,
saving the complexity of implementing special compilers. It also
reflects the mid-70's state of the art.

What didn't age well is the implicit understanding that numbers are
the **only** built-in data types. Strings are so magical they're
isolated into two separate subsets: SP/4 and SP/7. Arrays are called
out, but sets and dictionaries didn't exist in PL/I and aren't part
of this nested sequence.

Also. And even more fundamental.

There's a bias toward "procedural" programming. The SP/k subsets
expose the **statements** of the language. There are few data
structures, and it seems the data structures require some statements
before they're useful.

This leads to my restructuring of this. It doesn't apply to the
Mastering OO Python book. It's something I use for Python bootcamp
training.

-   py/1 expressions and output: int, float, numeric built-in
    functions, and the print() function.

-   py/2 variables, assignment, and the input() function.

-   py/3 strings, formatting, and various built-in string parsing
    methods.

-   py/4 tuples and multiple assignment. (Since tuples are immutable,
    they're more like strings than they are like lists.) And yes, this
    is kind of short.

-   py/5 if statements and try/except statements. These are the two
    fundamental "selection" statements. The raise statement is
    deferred until the functions section.

-   py/6 sets and the for statement.

-   py/7 lists.

-   py/8 dictionaries.

-   py/9 functions (avoiding higher-order functions, decorators, and
    generator functions.)

-   py/10 contexts, with, and file I/O.

-   py/11 classes and objects.

-   py/12 modules and packages.

   
The point here is to expose the data structures as the central
theme of Python. Statements follow as needed to work with the data
structures.


Note that some topics -- like break, continue, and while -- are
advanced parts of working with data structures.


The standard library? Not included. Perhaps should be. But. It's
**technically** separate from the language and all of this can be
done without any imports. We would then cover a bunch of standard
library modules. The order includes math, random, re, collections,
typing, and pathlib.





