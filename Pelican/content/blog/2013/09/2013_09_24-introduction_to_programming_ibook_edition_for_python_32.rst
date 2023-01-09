Introduction to Programming: iBook Edition for Python 3.2
=========================================================

:date: 2013-09-24 08:00
:tags: ebook,#python,ibooks,iTunes bookstore,building skills books
:slug: 2013_09_24-introduction_to_programming_ibook_edition_for_python_32
:category: Technologies
:status: published

That was challenging.

I rewrote almost all of my Introduction to Programming book into an
iBook. Trimmed it down. Refocused it. Changed from Python 2.6 to 3.2.
A complete refactoring from which almost nothing of the original book
survives except the goals.

Look for it October 1st in the iTunes bookstore. `Programming for
Absolute Beginners: Building Skills in
Programming <https://itunes.apple.com/us/book/programming-for-absolute-beginners/id707460405?ls=1>`__.

[My intent is to have several Building Skills titles. We'll see how
far I get.]

The rewrite involved three substantial changes.

#.  I removed all of the duplicative reference material. The Python
    library reference is (now)  utstandingly good. When I started using
    Python over ten years ago, it was not very good, and I started
    writing a Python reference of my own merely to organize the
    documentation. The books grew from there; the reference aspect is now
    useless.

#.  I dropped almost all Python 2 references. There's a little bit of
    Python 2 history, but that's it. It's time to move forward, now that
    most of the major packages seem to have made the switch.

#.  I changed the focus from processing to data.


**Processing vs. Data**


When looking at a multi-faceted language like Python, it's difficult
to know what's the most gentle introduction to software development.


Historically, the procedural, imperative style of programming appears
the most appealing. The roots of Python come from procedural
programming. It reaches back to Pascal (and even Algol 60) by
elegantly restating the core principles of those languages with an
easier-to-read syntax.


Indeed, if you read classic foundational CACM articles where
essential algorithms were first formally described, they used a
neatly typeset variant on Algol that (for the early years of my
career) was the gold standard in how code should look. Python follows
this tradition nicely.


But.


That doesn't mean that procedural programming is really the
absolutely best way to introduce the language.


**Data First**


I think that it may be possible to introduce the language with a
focus on data objects first and the procedural/imperative statements
as a secondary consideration.


When it comes to anything beyond trivial Rate-Time-Distance
calculations, the data structure matters more than almost any other
aspect of the software. The objects, their relationships, their
operations and their attributes are core to the problem. The
presentation, user actions and persistent representation are
secondary considerations after the structure of the data.


It seems like the data structures should "drive" the presentation.
The outline of the book should be introductions of each of the
important and visible builtin data structures. Additionally, the
library extensions that are most often used can be introduced, also.


Definitional features (def, return, yield, class, and the ideas of
module and package) are central, but a step behind the builtin data
structures.


Procedural features (if, for, while, break, continue, with, etc.) are
clearly second-class; they exist only to support access to the data
structures. A for statement, makes a "for all" assertion about a data
structure. A for with a break (or a while) makes a "there exists"
assertion about a data structure. The data is central. The imperative
statements are secondary.


Other features (global, nonlocal, del, raise, try, etc.) are
tertiary, and exist to create more elegant programs that don't annoy
the other developers as much.


This also means that generator expressions and comprehensions are
first-class, front-and-center features of the language. This
parallels the approach in the `NLTK Book <http://nltk.org/book/>`__,
which puts the focus on generator expressions as a way to clearly
state the processing.


**Other Forms**


Currently, I only have the iBook available.


The iBook Author application can (and does) produce a PDF. I think I
may offer that separately through
`www.lulu.com <http://www.lulu.com/>`__.





