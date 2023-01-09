HamCalc Quirk of the Week
=========================

:date: 2013-07-09 08:00
:tags: HamCalc,preservation,GW-Basic,modernization,quirk
:slug: 2013_07_09-hamcalc_quirk_of_the_week
:category: Technologies
:status: published

The HamCalc program binhop is one of those little nuggets of beauty that
might be helpful or might be useless. Or. Perhaps there's some useful
stuff commingled with quirky stuff.

For folks in agriculture or manufacturing, I'm hoping that the
calculation could be helpful. Although it's also likely that folks don't
spend much time designing hoppered bins; they just buy something out of
a catalog.

The binhop program is 151 lines long. Of those lines, 13 lines appear to
be some orphaned code that doesn't belong there. They appear to be part
of a hoppered bin design program that appears to have been split off
into binvol.

It's easy to grep for all 46 instances
of ``(?:GOTO|GOSUB|THEN)\s+\d\d\d0`` to locate references to line
numbers. We're only interested in line numbers from 1050 to 1170. Of
course, there are none.

But.

This is GW-Basic. Maybe there's a language or implementation quirk that
makes this code somehow get executed? It seems highly doubtful. After
all, it's only 151 lines of code. It's relatively easy to read and
understand what's there.

This kind of quirk demonstrates that an "automated" code conversion is
rarely going to be helpful. An automated conversion of orphaned code
means that the good stuff is diluted by the bad stuff.

I spent the most time with this fumbling through the alternative use
cases to see what the program does. It doesn't do much. But it's
important to be sure that this calculation isn't part of the use cases.
It doesn't get a unit test.

More Oddness
------------

This program has another cute quirk that is less brain-scrambling than
orphaned code.

::

    1020 :REM'
    1030 IF C$="SIDE" THEN N=ATN(H/(F-D))*180/PI:RETURN
    1040 IF C$="CENTER" THEN N=ATN(2*H/(F-D))*180/PI:RETURN

What if C$ is neither SIDE nor CENTER? There's no "otherwise" case
expressed or implied. It just "falls through" to the next line of
code.

In this case, the next line of code just happens to be the orphaned
code starting on line 1050. This will do some calculations on
variables which merely have their GW-Basic default values of 0. Since
line 1170 ends with a RETURN, the program will appear to "work". It
won't crash outright. It just executes a bunch of useless statements.


In other programs with similar structure, the following line of code
is a RETURN (or a STOP or even an END in one case.)


Since C$ is only referenced in five lines of code, it's easy to be
certain that it can only have one of the two values. Of the five
references, one is a PRINT statement. Two are the above IF
statements. The other two are assignment statements.


Here are the two assignment statements:


::

  650 Y$=INKEY$:IF Y$=""THEN 650
  660 IF Y$="1"THEN GOSUB 1340:C$="SIDE":R=1:RETURN
  670 IF Y$="2"THEN GOSUB 1340:C$="CENTER":R=0:RETURN
  680 BEEP
  690 GOTO 650


It's clear that C$ is restricted to a domain of just two values. The
lack of a formal "otherwise" case in the 1020-1040 block of code is
just a weird little quirk.


**Implementation**


Here are the relevant calculation
bits: https://github.com/slott56/HamCalc-2.1/blob/master/python/hamcalc/construction/binhop/__init__.py


By adding documentation and test cases, we've bloated the good bits
up to 336 lines of code.


Here are the user interaction
bits: https://github.com/slott56/HamCalc-2.1/blob/master/python/hamcalc/stdio/binhop.py


This reflects two decisions. It seemed sensible to (nearly) duplicate
some similar blocks of code rather than try to use a single block of
code peppered with IF-statements. IF-statements raise the `cyclomatic
complexity <http://en.wikipedia.org/wiki/Cyclomatic_complexity>`__.
Lines of code just make it longer. Also, we've combined all of binvol
into binhop.


In the long run, I know nothing about the subject matter. Nor did I
even do the minimal amount of online research to confirm the formulae
in the program. I'm secretly hoping that someone who actually
understands this subject area will revise and correct the code to
make it more useful and complete.





