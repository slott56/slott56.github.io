Exacting Definitions
====================

:date: 2010-01-21 11:21
:tags: #python,interpreted,dynamic,scripted
:slug: 2010_01_21-exacting_definitions
:category: Technologies
:status: published

Interesting comments to `Splitting
Meta-Hairs <{filename}/blog/2010/01/2010_01_21-splitting_meta_hairs.rst>`__.

Terms like Scripting, Interpreted and Dynamic are *not* "marketing
terms". New, Improved, All Natural, Visual, Groovy, Lucid, etc., are
marketing terms. I regret giving the impression that one should "not
to spend time trying to get definitions that are exacting". One
absolutely *must* get definitions which are exacting. Clearly, I
failed. **Exact definitions matter.**

Hiding behind the edge and corner cases, however, isn't helpful. Just
because some terms *could* be redundant, or *could* be ambiguous
(when stripped of useful meaning) isn't really a helpful thing.
Harping on the "ambiguity" or "contradiction" or "redundancy" isn't
helpful. Yes, Python has edge cases. Outside the purity of
mathematics, no categorization is ever perfect.

**Scripting**. The Python community steers away from this because
it's limiting. However, it's also true. What's important is that some
folks overlook this and over-engineer solutions. Python modules
require three things (1) an appropriate #! line, (2) a mode that
includes appropriate "x" mode flags and (3) a location on the PATH to
be indistinguishable from binary executables.

I find it necessary to repeat "scripting" to prevent
over-engineering. Clearly, scripting isn't a completely distinct
dimension of language description, but it's still an important
clarification to many of the people I work with.

Python's on this `scripting language
list <http://en.wikipedia.org/wiki/List_of_programming_languages_by_category#Scripting_languages>`__.

[We had a RHEL system with SELinux settings that prevented Python
scripts from running. A sysadmin said -- seriously -- that I just
needed to use \`sudo su -\` to get past this. The admin, it appeared,
couldn't see why Python scripts should behave exactly like all other
scripts. Hence the need to emphasize that Python is a scripting
language. Otherwise people forget.]

**Interpreted**. Python is a byte-code interpreter. Saying things
like "compiling to machine code is also interpreted" eliminates all
meaning from the words, so it can't be true or useful. We need to
distinguish between **compiled** to machine code and **interpreted**;
machine code binary executes directly. And Python doesn't compile to
machine code. Python is interpreted.

    [The fact that some hardware had microprogramming is irrelevant;
    there are programmable ASIC chips in my Macintosh, that doesn't
    matter to my Python interpreter. There's a clear line between the
    binary machine code and the Python or Java interpreter. Yes, there
    are other levels of abstraction. No, they don't matter when
    discussing the nature of Python.]

You can use `cython <http://www.cython.org/>`__ or
`py2exe <http://www.py2exe.org/>`__ or
`py2app <http://www.undefined.org/python/>`__ to create binaries from
Python. But that's not the interpreted Python language. This is the
distinction I'm trying to emphasize.

I find it necessary to repeat "interpreted" so people are not
confused by the presence of visible bytecode cache (.pyc) files.

**Dynamic**. Python is dynamic. Dynamic is clearly distinct from the
other dimensions. There's less confusion over this word, but it still
fails to sink in.

I find that this needs to be repeated frequently so people stop
looking for static type declarations. The number of Stack Overflow
questions that include "python" and "declaration" is always
disappointing.



-----

"Python is interpreted." Then Java is a...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-01-21 11:12:51.026000-05:00

"Python is interpreted."

Then Java is an interpreted language as well, and I'll find that you
have removed the meaning of \*that\* word. Interpreted != Virtual
machine != machine code.

And what about the DEC machines, which had processors you programmed in
micro-code? Was that interpreted too? :-)

Python in itself probably could be an interpreted language, but CPython
is a byte-compiled/VM language, like Java. With a JIT-byte-compiler,
unlike Java, which means it can be used as a scripting language, also
unlike Java.


Re: the scripting argument. Again you seem to be m...
-----------------------------------------------------

Richard Jones<noreply@blogger.com>

2010-01-21 17:54:33.824000-05:00

Re: the scripting argument. Again you seem to be missing the point. It's
not that Python can't used for scripting it's that can be used for much
more. Calling it a "scripting" language leads to pigeon-holing - and yes
I've personally had someone be amazed that I earn a six-figure annual
salary using Python because "it's just a scripting language, isn't it?"
Also Python modules don't require either "#!" lines or the "x" bit.
Python "scripts" on Unix-alike operating systems might. Python programs
certainly don't - double-clicking a ".py" file on Windows and OS X will
execute those programs.


@regebro As per my comment, languages like Java an...
-----------------------------------------------------

Michael Foord<noreply@blogger.com>

2010-01-21 11:14:47.689000-05:00

@regebro

As per my comment, languages like Java and C# are usually described as
compiled because they have JIT compilers. The bytecode is \*not\*
interpreted, but native code is generated and executed. Python has an
interpreter loop that interprets its bytecode.


py2exe and py2app do not compile to binaries - the...
-----------------------------------------------------

Michael Foord<noreply@blogger.com>

2010-01-21 11:13:15.751000-05:00

py2exe and py2app do not compile to binaries - they merely bundle the
Python interpreter with the code (usually as compiled bytecode) with the
application. This doesn't change your point, but the way you write
\*implies\* that these tools compile to binary.

As you say Python is usually described as interpreted because the
bytecode is interpreted, whereas languages like C# and Java are usually
described as compiled because they have JIT compilers that compile
bytecode to native code. Once Unladen Swallow is integrated with Python
3 Python will also have a JIT compiler...


The definition of compiled vs interpreted language...
-----------------------------------------------------

Jaime<noreply@blogger.com>

2010-01-21 14:36:10.090000-05:00

The definition of compiled vs interpreted language it's getting somehow
blurry... I'd say that the difference is the fact that the bytecode of
an interpreted language it's a direct translation of the language, in a
more convenient load format, but it doesn't change any of the
fundamentals.

The variables gets their names declared on the bytecode. Any algorithm
is literally used the same way, any parameters are referenced by their
names or positions, etc...

On a compiled language, it's compiled on a different language. Yes, it
does the same, but the variables are transformed on memory addresses,
there are checks ensuring these transformations can be done correctly
(compilation errors)...

The Java bytecode it's really machine code in the "Java architecture",
in the 90s even there were a few "Java" machines that run natively Java
code. It works like assembler, has registers, address jumps, etc...
That's NOT the case of Python bytecode, which is just changing the more
natural language into a step by step more easily loaded by the
interpreter. You can't make a "Python architecture" machine, you'll
always will need a program running that takes that bytecode and map it
to machine code, sometimes one way, sometimes other. All you can do is
join the bytecode with the interpreter to give the illusion of a true
compiled program.

Anyway, JIT and other techniques are making these distinctions
difficult, and I think it's better to think in terms of static and
dynamic, which is usually what change the way of thinking and using the
language...


But Java wasn&#39;t described as interpreted even ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-01-21 11:22:50.775000-05:00

But Java wasn't described as interpreted even before it had a JIT
compiler by default. With that wording it would have been a compiled
interpreted language in the 90's, which nicely illustrates how wrong it
is to try to push all languages into an interpreted/compiled dichotomy.
Python is not interpreted, because it gets compiled to bytecode. An
interpreted language reads the source code line by line. It's a
byte-compiled VM language. So it Java, even though it's typically run
with JIT-compilers.


@regebro "An interpreted language reads the s...
-----------------------------------------------------

Michael Foord<noreply@blogger.com>

2010-01-21 11:31:53.201000-05:00

@regebro

"An interpreted language reads the source code line by line." - that is
not how the terms are \*generally\* used today, although feel free to
make up your own definitions and use them. ;-) (Marketing history of
Java not-withstanding.)





