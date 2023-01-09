This Seems Irrational... But... HamCalc 
========================================

:date: 2013-04-11 09:54
:tags: #python,knowledge capture,HamCalc,GW-Basic,test-driven reverse engineering
:slug: 2013_04_11-this_seems_irrational_but_hamcalc
:category: Technologies
:status: published

Step 1.  Look at the
original `HamCalc <http://www.cq-amateur-radio.com/cq_ham_calc/cq_ham_calc.html>`__.
Even if you aren't interested in Ham radio, it's an epic, evolving
achievement in a specialized kind of engineering support.  It's a
repository of mountains of mathematical models, some published by the
`ARRL <http://www.arrl.org/>`__, others scattered around the internet.

Step 2.  Look closely at HamCalc.  It's all written in GW basic.
Really.  The more-or-less final update is from 2011 -- `it's no
longer an active
project <http://www.southgatearc.org/news/october2011/development_of_hamcalc_to_cease.htm>`__
-- but it's a clever idea that suffers from a horrible constraint
imposted by the implementation language.

A **long** time ago, I was captivated by the idea of rewriting HamCalc
as Java Applets.  It seemed like a good idea at the time, but that's a
lot of work: 449 programs, 85,000 lines of code.

Recently, I wanted to make some additional use of HamCalc's amazing
collection of formulas.

However.  The distribution kit is rather hard to read.  The .BAS files
are in the tokenized "binary" format.

I found a Python project to interpret the byte codes into a more
useful format.
See http://www.danvk.org/wp/gw-basic-program-decoder/  However, it
wasn't terribly well written, and didn't prove completely useful.

**GW Basic Bytes Codes**

Look at http://www.chebucto.ns.ca/~af380/GW-BASIC-tokens.html for some
basic rules on the file format.

See http://www.antonis.de/qbebooks/gwbasman/index.html for a
reasonably clear definition of the language itself. Quirks are, of
course, studiously ignored, so there's a lot of ambiguity on edge
cases.

For simple bytes-to-text translation, this is pretty simple.  The next
step -- interpreting GW Basic -- is a bit more complex.

**Future**

The irrational thing is that I'm captivated by the idea of preserving
this legacy gift from the authors in another, more useful language.
Indeed, the idea of a community of "HamCalc Ports to Other Languages"
appeals to me. This base of knowledge is best preserved by being made
open so that it can be rewritten into other commonly-used languages.

There's a subset version
here: http://www.softpedia.com/get/Science-CAD/HamCalc.shtml and
here http://www.dxzone.com/dx11432/hamcalc-v1-3.html. This is just a
few of the calculations, carefully rebuilt to include nice versions of
the ASCII-art graphics that are central to the original presentation.

The hard part of preserving HamCalc is the absolute lack of any test
cases of any kind.

I think the project should work like this.

#.  Publish the complete plain text source decoded from the tokenized
    binary format. It will likely be somewhere on
    http://www.itmaybeahack.com/ or perhaps a
    `Dropbox <https://www.dropbox.com/home>`__.

#.  Publish the index of programs and features as a cross-reference to
    the various programs. This should include the various links and
    references and documentation snippets that populate the code and
    output. This forms the backbone of the documentation as well as the
    unit testing.

#.  Do a patient (and relatively lame) translation to Python3.2 to break
    HamCalc into two tiers. The calculation library and a simple UI
    veneer using stdio features of the print() and input() statements.
    The idea is to do a minimalist rewrite of the core feature set so
    that a GUI can be laminated onto a working calculation library.

#.  Work out test cases for the initial suite of 449 legacy programs
    oriented toward the calculation layer, avoiding the UI behavior. The
    idea isn't 100% code coverage. The idea is to pick the relevant logic
    paths based on the more obvious use cases.


A sophisticated GUI is clearly something that was part of the
original vision. But the limitations of GW Basic and tiny computers
of that era assured that the UI and calculation were inextricably
intertwingled.


If we can separate the two, we can provide a useful library that
others can build on.


Maybe I should organize http://www.hamcalc.org/ as the jumping-off
point for this effort?



-----

Why not put the project on Github or BitBucket so ...
-----------------------------------------------------

Chris Nelson<noreply@blogger.com>

2013-04-12 07:16:32.048000-04:00

Why not put the project on Github or BitBucket so the project has source
control and exposure? You could also make a modern Python version that
utilized some of the great third party libraries for graphing and
calculations.
Chris
WA5TT


That wasn´t necessary. You can save a file in ASCI...
-----------------------------------------------------

Rodri<noreply@blogger.com>

2013-04-12 05:48:56.085000-04:00

That wasn´t necessary. You can save a file in ASCII format in GWBASIC.


Interesting project. I&#39;d be willing to help if...
-----------------------------------------------------

Jason Crowe<noreply@blogger.com>

2013-04-11 16:08:54.095000-04:00

Interesting project. I'd be willing to help if needed.


While my GWBASIC knowledge is a little bit rusted,...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-04-12 04:28:04.215000-04:00

While my GWBASIC knowledge is a little bit rusted, i offer my help in
porting stuff to Python. I am not quite sure if i got the point of the
test cases right: You want to compare the calculation results of the
legacy GWBASIC apps with the ported Python apps as test cases?
How can we stay in contact regarding the project?
Greetings,
Stefan DL1ELY


This is a great idea.  I&#39;m ready to get involv...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-04-14 00:09:23.367000-04:00

This is a great idea. I'm ready to get involved. I like the Github idea,
too. So, has anyone started a github, yet? Or shold I do it
Peter
N3DXY


Cool thanks ... I was out of town for a while but ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-05-22 23:49:23.350000-04:00

Cool thanks ... I was out of town for a while but I'm back and still
thinking this is a good idea. Is anyone else working on this?


Steve,

I put together a DOS VM and dug up my old ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-04-17 00:10:59.621000-04:00

Steve,
I put together a DOS VM and dug up my old copies of GWBASIC. Getting the
code to ASCII isn't really a big problem. Although GWBASIC saves in that
tokenized format by default. From inside the interpreter after you load
the BASIC file, you can just save them as ASCII using the command: SAVE
"filename.bas",a
Then it's saved as text. So I've done a bunch already.


Found it! 

gwbascii.exe with source code!

http:/...
-----------------------------------------------------

Chris Nelson<noreply@blogger.com>

2013-04-17 09:00:38.678000-04:00

Found it!
gwbascii.exe with source code!
http://utopia.knoware.nl/users/arne/gwbascii/


Peter,

There&#39;s also conversion program I foun...
-----------------------------------------------------

Chris Nelson<noreply@blogger.com>

2013-04-17 06:12:32.315000-04:00

Peter,
There's also conversion program I found a while back that runs under
Windows, I'll have to scrounge and see where it came from.


For folks who are interested.  http://hamcalc.wiki...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2013-06-01 07:45:16.488000-04:00

For folks who are interested. http://hamcalc.wikispaces.com/home
https://github.com/slott56/HamCalc-2.1





