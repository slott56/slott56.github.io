The curse of procedural design
==============================

:date: 2011-05-03 08:00
:tags: #python,procedural programming,OO design
:slug: 2011_05_03-the_curse_of_procedural_design
:category: Technologies
:status: published

After reverse engineering procedural code in C, VB or even Python, I'm
finding that procedural programming inevitably leads to bad, bad
code-rot.

Consider some of the common design patterns.

**Strategy**. Confronted with alternative strategy choices, a purely
procedural code solution is either

-   If-statements everywhere the strategy is involved.

-   Block comments. (Pre-processor #if statements are the logical
    equivalent of block comments plus a tool to move them around just
    prior to compilation.)

These lack flexibility and seem to devolve into a quagmire of
mystery. The if-statements often become tangled and complex. More
importantly, some strategy choices — which are unused — may not be
maintained at all. Of course, the block comments are never
maintained.

**Command**. Often a command design requires a "code" or "label" and
a big-old sequential switch (BOSS™) statement to select among the
procedures which implement the various commands. Once "composite"
commands are introduced, this devolves into nonsense. Ideally, it's a
simple recursion, where a composite command simply invokes the
sub-commands. However, folks get nervous about recursion and try to
write weird loops.

**State**. A state design always seems to involve labels or codes for
the state names and a slightly different big-old-state-switch (BOSS™,
no accident that this is the same acronym) to sort out the variant
behaviors in the distinct states. This shouldn't become too
confusing. After all, Turing machines and other mathematical
abstractions give us a strong hint on how we should proceed.

The problem with stateful procedural programming is that the state
changes can be hidden everywhere. In the Really Bad Languages,
variables can change values without an assignment statement! In the
Not Bad Languages, we can track down the various assignment
statements and try to reason out the state changes. Procedural
code—without a lot of adult supervision—never seems to encapsulate
state change with the the same in-your-face clarity that OO programs
do.

I Could Go On
-------------

The point is this. While procedural programming *could* be done well,
there appear to be a lot of obstacles inherent in the paradigm.

The best procedural programming I've seen has always been very
object-oriented. Each procedure or function had a distinct data
structure it worked with; they were all closely related by virtue of
naming or file structure; much like a class definition.

I'm starting to wonder if my Building Skills books are taking the
right approach. I start with the procedural aspects of Python. I'm
beginning to feel that this may be a disservice to the n00bz.

Perhaps it's better to swap the order of the sections and start with
the various Pythonic data structures and introduce the various
statements sort of "casually" as part of demonstrating how a data
structure is supposed to be used.



-----

I think the procedural approach still is the best ...
-----------------------------------------------------

Patchwork<noreply@blogger.com>

2011-05-04 16:55:11.543000-04:00

I think the procedural approach still is the best way to start teaching
how to program. Although, it is not the best abstraction when the
application gets some non-trivial complexity. Then, some encapsulation
is necessary.

In other words, encapsulation is an abstraction that helps to handle
complexity, but it is not the first concept n00bz must learn.

I don't agree that starting with a data centric view is better than a
procedural one. Any structured data is also an arrangement to solve some
kind of problem and it is not necessary to solve initial programming
concepts.


&quot;Perhaps it&#39;s better to swap the order of...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-05-03 21:27:49.097000-04:00

"Perhaps it's better to swap the order of the sections and start with
the various Pythonic data structures and introduce the various
statements sort of "casually" as part of demonstrating how a data
structure is supposed to be used."

Lets step back and explicitly state what the goals are.

Lets step back and remember the clue absorption rate of the student.
Lets step back and not try to do too much and end up loosing focus.
How about a 3rd book entitled something like doing procedural code
correctly when you don't want to be bothered w/ OO?

I am currently working my way through your book "Building Skills in
Python" and loving it. It follows the "expected" standard procedural
language progression. Heck even Oracle's PL/SQL manual does it.
http://download.oracle.com/docs/cd/B19306_01/appdev.102/b14261/toc.htm


The intro to Java programming class I took many mo...
-----------------------------------------------------

eryksun<noreply@blogger.com>

2011-05-03 14:24:00.410000-04:00

The intro to Java programming class I took many moons ago emphasized
object oriented design and tail recursive algorithms. Java for/while
loops weren't introduced until near the end of the class.


I also think starting with procedural design is st...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2011-05-05 07:36:58.093000-04:00

I also think starting with procedural design is still the right thing to
do. However, part of the point of OO is to make it clear that procedural
programming \*doesn't scale well*.

At the small scale, OO is overkill (even functions are overkill at a
sufficiently small scale).

So Python starts with scripts: Top to bottom evaluation of the main
script.

Then we add conditional execution and repetition (if statements and
loops), but still no distinction between "definition time" and
"execution time"
Then we start to modularise blocks of execution as functions and
introduce the idea that algorithms can be stored for use in multiple
places so that "definition time" and "execution time" may be separated.
Then we start to modularise data and operations on that data as classes.
Then we start to modularise collections of classes (and potentially data
and standalone functions) as separate modules (and now we can optionally
introduce the idea of "compilation time" as separate from both
"definition time" and "execution time").

Then modules may be bundled into packages, and packages into frameworks
and applications (introducing "build time" and "installation time" as
two new potentially important phases in program execution).

Part of the art of software design is learning how to choose an
appropriate level of complexity for the problem at hand.

In my opinion, the \*reason\* "scripting" languages are easier to learn
for many people is that they permit you to start immediately with a main
module that "does things", allowing the introduction of the "function"
and "class" abstractions to be deferred until later.

Starting with C and Java, on the other hand, always requires instructors
to say "Oh, don't worry about that boilerplate, you'll learn what it
means later" before starting in with the explanation of what can go
inside a main() function or method. The "compilation time" vs "execution
time" distinction also has to be introduced immediately, rather than
being deferred until the introduction of file level modularisation.


For a related blog also posted by Steve Lott, chec...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-05-03 21:33:20.399000-04:00

For a related blog also posted by Steve Lott, check out
`"The Anti-IF Campaign"
<{filename}/blog/2010/12/2010_12_27-the_anti_if_campaign.rst>`_





