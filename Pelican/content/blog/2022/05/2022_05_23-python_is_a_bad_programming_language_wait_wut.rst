Python is a Bad Programming Language. Wait, wut?
##################################################

:date: 2022-05-23 20:35
:tags: #python,click-bait
:slug: 2022_05_23-python_is_a_bad_programming_language_wait_wut
:category: Technologies
:status: published

It may help to read `Python is a Bad Programming
Language <https://medium.com/nerd-for-tech/python-is-a-bad-programming-language-2ab73b0bda5>`__,
but it's not very useful.

I shouldn't be tempted by click-bait headlines. But.  I am drawn in by
bad articles on Python.

In particular, any post claiming Python is deficient causes me to look
for the concrete PEP's that fix the problems.

Interestingly, there never seem to be any PEP's in any article that
bashes Python. This post is yet another example of complaining without
offering any practical solutions.

BLUF
====

The article has a complaining tone, but, I can't figure out some of the
complaints. It lifts up a confusing collection of features from other
languages as if these features are somehow universally desirable. No
justification is provided. The author seems to rely exclusively on Stack
Overflow answers for information about Python. There are no PEP's
proposed to fix Python. There aren't even any examples.

Point-by-Point
==============

I will try to address each point. It's difficult, because some of the
points are hard to discern. There's a lot of "Who thought that was a
good idea?" which isn't really a specific point that can be refuted.
It's a kind of rhetorical flourish that seems to work best with folks
that already agree.

Let's start.

A Fragmented Language
---------------------

This is the result of profound confusion. It's hard to find anyone
recommending Python 2 anywhere. The supplied link is 9 years old, making
this comment extremely misleading.  (I'm being charitable. A nine-year
old link on Stack Overflow requires some curation. This is not a Python
problem.)

Ugly Object-Orientation
-----------------------

The inconsistent use of ``this`` in C++ and Java is lifted up as somehow
good. The consistent use of the ``self`` instance variable in Python is
somehow less good; perhaps because it's consistent.

"See how I have to both declare and initialize them in the constructor?
Another example of Python stupidity." Um. No, I don't actually see you
*declare* them anywhere. I guess you're unaware of what *declare* means
in languages like C++ and why *declare* isn't a thing in Python.

Somehow using the ``private`` keyword is better than ``__`` name
mangling. I'm unclear on why it's better, it's simply stated in a way
that makes it sound like a long keyword used once is better because it's
better. No additional reason or justification is offered. The idea of
using \_\_ to emphasize the privacy is somehow inconceivable.

The ``private`` and ``protected`` keywords are in C++, C#, and Java to
optimize recompilation. To an extent, this also permits distribution of
libraries in the form of "headers" and obfuscated binaries. None of this
makes sense in a Python context.  A single example of how the
``private`` keyword would be helpful in Python is missing from the
original post. There are huge complications of the ``protected``
keyword, also; these make the keywords more trouble than they are worth,
and any example needs to cover these issues, also.

"In general, when you point out any flaws in their language, Python
developers will act hostile and condescending." Sorry, this complaint in
the original post sounds hostile and condescending. I'll try to ignore
the tone and stick to what content I can find.

Whitespace
----------

"...how is using whitespace any better than curly braces?" has an
answer. But. Somehow it can't be chased down and included in the
original post. Whitespace (like name mangling) is described as wrong
because it's wrong, with no further justification provided.

An example where braces seem to be essential for sorting out syntax
would be nice. The entire Python community is waiting for any example
where braces were **necessary** and the indentation wasn't already
clear.

"And only in Python will the difference between tabs and spaces cause
the interpreter to have a heart attack." Um. A syntax error is a heart
attack? I wish I was able to type code without syntax errors. I am
humbled thinking about the idea of seeing syntax errors so rarely. I
have my editor set up to use spaces instead of tabs, and haven't had a
problem in 20 years of using Python.

Dynamic Typing
--------------

The opening quote, "Dynamic typing is bad," is stated as if it's
axiomatic. The rest of the paragraph seems like vitriol rather than
justification. "Some Python programmers have realized that dynamic
typing is bad" requires some justification; a link to some documentation
to support the claim would be helpful. An example would be good.

I can only assume that code like this is important and needs to be
flagged by the compiler or something.

::

   for data in some_list:
       if data == 42:
           print("data is int")
   for data in some_other_list:
       if data == "wait":
           print("see the type of data changed.")
           

This seems like poor programming to begin with. Expecting the compiler
to reject this seems weak. It seems better to not reuse variable names
in the first place.

Constants
---------

Not sure what the point is here. There's no justification for demanding
the inconsistent behavior of a one-time-only assignment statement.
There's no reference how how folks can use enums to define constant-like
names and values.

The concluding paragraph "The Emperor Has Not Clothes" is some kind of
summary. It says "Python will only grow in popularity as more and more
software is written in it," which does seem to be true. I think that
might be the single most useful sentence.

What Have We Learned?
=====================

First, reading a few Stack Overflow posts can be misleading. Python now
is not Python from nine years ago.

#. Everyone says to use Python3. Really. If you have found a Python2
   tutorial, stop now. Don't follow it.
#. The consistent use of the ``self`` variable seems simpler than trying
   to understand the rules for the ``this`` variable.
#. Variables aren't *declared*, they're assigned values. It's as simple
   as it can be and avoids the clutter of variable declarations.
#. We can read the source; the complexities of private (or protected)
   instance variables doesn't really help.
#. Python's use of whitespace is very simple; most people can indent
   their code correctly. Anyone who's tried to debug C++ code that's
   correctly indented but missing a (nearly invisible) } will agree that
   the indentation is easier to get right.
#. AFAICT, the reason dynamic typing might be bad is when a function or
   class reuses the same variable name for multiple different types of
   data. This seems wrong to reuse a variable name for multiple types. A
   small effort at inspecting the code can prevent this.
#. Constants are easily implemented via enum. But. They appear to be
   useless in a dynamic language where the source is trivially available
   to be changed. I'm not sure why they seem important to people. And
   this article provides no help there.

Bottom line: Without concrete PEPs to fix things, or examples of what
better might look like, this is click-bait whining.

Starting from C# or Java to locate deficiencies is just as wrong as
starting from Dartmouth Basic or FORTH as the standard against which
Python is measured.





