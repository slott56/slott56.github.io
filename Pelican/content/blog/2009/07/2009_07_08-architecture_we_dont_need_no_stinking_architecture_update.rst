Architecture?  We don't need no stinking architecture! (Update)
===============================================================

:date: 2009-07-08 15:45
:tags: VB,architecture
:slug: 2009_07_08-architecture_we_dont_need_no_stinking_architecture_update
:category: Technologies
:status: published

Context: We're reverse engineering some bad VB application code.

What I saw. "This problem report pushed this module over the 64k
limit for modules. Therefore all code used for XYZ has been removed
from this module and placed in the new bas module XYZ."

What I learned. Good design -- irrelevant. Abstraction -- irrelevant.
Layered architecture -- irrelevant. Conceptual Integrity of the
design -- irrelevant. What actually mattered was VB's 64k module
limit.

Consequence. Reverse engineering will be hard because I don't know
what code is scattered around the rest of the code base. The number
of global variables is truly awe-inspiring.

--------------

Edit: Two additional gems: "Needed to split out another portion of
this procedure due to "not enough memory" error on compile" and "This
new sub added because of "Procedure too Large" compile error".

Some people should find jobs in a different industry. The module is
6000 lines of code, and apparently, it had no structure at all until
it stopped compiling.




-----

Mr. Lott, There is so much bad VB code out there, ...
-----------------------------------------------------

Carl Trachte<noreply@blogger.com>

2009-06-25 11:01:14.932000-04:00

Mr. Lott,
There is so much bad VB code out there, you'll be in business forever.


It takes a VB coder to know one - this is where I ...
-----------------------------------------------------

Carl Trachte<noreply@blogger.com>

2009-07-09 00:24:29.499000-04:00

It takes a VB coder to know one - this is where I started programm . . .
er . . . munging data as part of my pit geologist duties in a mine.
So many things I've since learned NOT to do are just par for the course
in VB and especially VBA code (inside Excel spreadsheets). Copy and
paste huge blocks of code - no problem. Declare constants instead of
using magic numbers, why bother?

It's not so much the language as the culture (although there are design
decisions even a mother could not love or defend). I remember the first
VB book I bought at the outset of the dot com boom - the author went on
a feel good rant about how VB programmers like to \*GET THINGS DONE\* -
man, what a crock.

Taking a C course online almost killed me, but it broke some of those
awful habits.

Can we just forget this whole VB thing ever happened? (NO, BECAUSE
THERE'S A BAZILLION LINES OF VB CODE OUT THERE running mission critical
systems). Like I said before, Mr. Lott, if you live long enough you'll
own the yacht in the picture on your homepage yet (maybe 2!).

My two (actually, about forty five) cents.

Sorry for the rant. :-(


Or you can get a job cleaning up crude oil spills....
-----------------------------------------------------

Bill Karwin<noreply@blogger.com>

2009-06-25 11:43:59.283000-04:00

Or you can get a job cleaning up crude oil spills. That might be less
toxic.


All design concerns are overshadowed by the lack o...
-----------------------------------------------------

Lennart Regebro<noreply@blogger.com>

2009-06-25 13:02:56.494000-04:00

All design concerns are overshadowed by the lack of programming skills
of the average VB programmer. I did a project many years ago (10+) where
I after a week of fixing bugs declared that it would be quicker to
rewrite the whole program from scratch than fixing up th VB program. It
took three weeks to rewrite it in Delphi, if I remember correctly.





