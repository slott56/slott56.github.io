Splitting Meta-Hairs
====================

:date: 2010-01-21 09:01
:tags: #python,interpreted,dynamic,scripted
:slug: 2010_01_21-splitting_meta_hairs
:category: Technologies
:status: published

Recently, I've been involved in some hair-splitting over the nature of
Python.

I've described it as "interpreted", "scripting" and "dynamic", all of
which seem to be true, but yet each seems to lead to a standard --
and pointless -- dispute.

Yes but No
----------

Some folks object to "interpreted". They feel a need to repeat the
fact that Python is compiled to byte code which is then interpreted.
Somehow, compiling to byte code interferes with their notion of
interpreter. Further exploration of the objection reveals their
unwavering conviction that an interpreter must work directly with the
original source. And it must be slow.

Eventually, they'll admit that's Python is interpreted, but not
really. I don't know why it is so important to raise the objection.

So noted. Are we done? Can we move beyond this?

Scripting Means Bad
-------------------

Some folks object to "scripted". They insist that scripting languages
must also include performance problems, limited data representation
or other baggage. Python is a scripting language because it responds
properly to the shell #! processing rules. Period.

I don't know why it's important, but someone feels the need to object
to calling Python a scripting language. Somehow the #! thing doesn't
convey enough complexity; scripting just *has* to be bad. Pages like
Wikipedia's `Scripting
Language <http://en.wikipedia.org/wiki/Scripting_language>`__ don't
seem to help clarify that scripting isn't inherently bad.

Again, objection noted. And overruled. Scripting doesn't have to be
complex or bad. It's just a relationship with the shell.

Further Nuances
---------------

I'm baffled when some folks take this further and object to Scripted
and Interpreted being separate terms. I guess they feel (very
strongly) that it's redundant and the redundancy is somehow
confusing. A shell script language pretty much has to be interpreted,
otherwise the #! line wouldn't mean anything. I guess that this is
why they have to emphasize their point that Scripted is a proper
subset of Interpreted.

But then, of course, Python is technically compiled before being
interpreted, so what then? What's the point of bringing up the detail
yet again?

Dynamic
-------

More rarely, folks will object to using Dynamic and Interpreted as
separate dimensions of the language space.

Hard-core C++ and Java programmers object to Dynamic in the first
place; sometimes claiming that a dynamic language isn't a "robust"
language. Or that it isn't "safe enough" for production use. Or that
it can't scale for "enterprise" use. Or that there are no "real"
applications built with dynamic languages.

Once we get past the "dynamic" argument, they go on to complain that
dynamic languages *must* be interpreted. The byte-code compiling --
and the possibility that the byte code could be translated to native
binary -- doesn't enter into the discussion early enough.

Also, some folks don't like the fact that an IDE can't do code
completion for a dynamic language. To me, it seems like just pure
laziness to object to a language based on the lack of code
completion. But some folks claim that IDE auto-completion makes VB a
good language.

Hair Resplitting
----------------

How about we stop wasting so much bandwidth resplittting these
hairs? It's scripted. It's interpreted. It's dynamic. How does it
help to micro-optimize the words? Even if scripted really is a
proper subset of interpreted, these prominent features solve
different kinds of problems; it seems to help the potential
language user to keep these concepts separate.

Can we slow down the repetition of (irrelevant) fact that Python
is compiled (but not to executable binary) **and** interpreted?
It's not confusing: byte-code compilation really is a
well-established design pattern for interpreted languages. Has
been for decades. Applesoft Basic on the Apple ][+ used
byte-codes. Okay?

Duck Typing is not a "flaw" or "weakness". Binary compilation is
not a "strength". It's trivial to corrupt a binary file and
introduce bugs or viri; binary compilation is not inherently
superior.

Can we move on and actually solve problems rather than split
meta-hairs?



-----

Today I've been teaching some Python issues at...
-----------------------------------------------------

Jaime<noreply@blogger.com>

2010-01-20 15:00:13.914000-05:00

Today I've been teaching some Python issues at a girl at work. She's
learning Python, so these days I give her "homework" to do, basically
some small programs to practice and getting the code more Pythonic and
less "C-istic".

Today's program takes to run 90 seconds at first. After some profiling
and two optimizations on for loops, the code takes about a second to
run. The optimization were nothing very difficult, just changing the
algorithm a little and doing the things properly on Python...
The main point is, what is the greatest factor on performance? It's not
dynamic or static language, or using registers, or duck typing, or
scripting.

It's algorithmics...

And, at least to me, I can concentrate more on algorithmics on Python
than on other languages. If after algorithmic work, you'll still need
performance, you can then think to change your approach...

I've been "suffering" a lot of the same arguments over and over... ;-)


Regarding your Apple comment toward the end, I thi...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-01-21 08:23:40.805000-05:00

Regarding your Apple comment toward the end, I think you mean Applesoft
BASIC (instead of AppleScript), which was the floating-point replacement
for the original Apple BASIC that only supported numeric integers (and
also used a byte-code format for storing programs in memory.)


Java also compiles to bytecode, not directly to ho...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-01-20 19:54:29.002000-05:00

Java also compiles to bytecode, not directly to host code. In that
sense, Python and Java are both compiled, as are a bunch other languages
that include a VM.


As a newbie, I found this posting very helpful. Al...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-01-20 19:15:16.227000-05:00

As a newbie, I found this posting very helpful. All these terms get
thrown around and I don't know whether they require exacting definitions
or whether they are "technical marketing" terms. Please note the use of
"technical" before "marketing".

Now I know that these are "technical marketing" terms and not to spend
time trying to get definitions that are exacting.


It&#39;s clear that what you mean with &quot;inter...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-01-21 02:32:22.531000-05:00

It's clear that what you mean with "interpreted" and "scripting" is
pretty much the same thing. So I object to that \*you\* separate them.
:)

I'd say that it's a byte-code compiled dynamic general purpose
programming language. Yes, it's a scripting language too. Very general
purpose. :)

If compiling to byte code is interpreted, then compiling to
machine code is also interpreted. Because you have to interpret the code
sometimes. :)

And my editor does code completion... OK, not as well as a static
language, obviously.


You may find it helpful to note that Wikipedia doe...
-----------------------------------------------------

Richard Jones<noreply@blogger.com>

2010-01-20 17:01:34.084000-05:00

You may find it helpful to note that Wikipedia does not classify Python
as a "scripting language" but rather as a "general purpose language".
This may help clarify any confusion you have trying to match "scripting
language" against your view of Python.





