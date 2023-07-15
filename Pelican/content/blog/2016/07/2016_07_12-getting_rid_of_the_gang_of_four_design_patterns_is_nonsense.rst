Getting Rid of the Gang-of-Four Design Patterns is Nonsense
===========================================================

:date: 2016-07-12 08:00
:tags: C,#python,functional programming,object-oriented design,java
:slug: 2016_07_12-getting_rid_of_the_gang_of_four_design_patterns_is_nonsense
:category: Technologies
:status: published


Someone found Yet Another Post (YAP™) insisting that the Gang of Four
(GOF™) patterns were on their last legs. The email was misleading,
because this is not precisely what the article said. The bottom-line
was that Design Patterns in general are merely a response to gaps in
the underlying programming language. A position that's nonsense at its
very foundation.

The lexicon of design patterns varies from language to language. GoF
patterns aren't "going away." They're part of the Java/C++ world. They
don't apply quite the same way to Python or functional languages.

There's a more serious issue, though: Language Mapping. First some
background.

Design Patterns
---------------


Design Patterns will always exist. They're an artifact of how we
process the world. We tend to classify individual objects so that we
don't have to deal with each object as a separate wonder of nature.

It's Just Another Brick In The Wall.

We don't have to examine each rectangular solid of ceramic and
understand the wonderfulness of it. We can group and summarize.
Classify. Brick is a design pattern. So is masonry. So is
wall. They're all patterns. It's how we think.

Design Patterns and Language Gaps
---------------------------------


There's a claim that moving toward functional languages will kill
design patterns. This presumes (partly) that non-OO languages
magically don't have design patterns. This is (see above) kind of
insane. Languages have design patterns. We recognize these patterns
all the time.

A functional language has a common technique (or pattern) for visiting
nodes in a hierarchy. We don't dwell on the wonderfulness of the code
as if we'd never seen it before. Instead, we classify it based on the
design pattern, and leverage this higher-level understanding to figure
out why we're walking a hierarchy.

Sounding the death knell for design patterns also presumes (partly)
that functional languages are magically more complete that OO
languages. In this newer better language, we don't need patterns
because there are no gaps. This is pretty much nutso, too. The
Patterns Fill Language Gaps school of thought ignores the fact that
there are many ways to implement these "gaps". We can use GoF design
patterns, or we can use other software designs that don't fit the GoF
design patterns. Both work.

The patterns aren't filling a "gap." They're providing guidance on how
to implement something. That's all. Nothing more. Guidance.

"But wait," you say, "since I needed to write code, that's evidence
that there's a gap."

"What?" I ask, incredulous. "Are you claiming that **any** code is
evidence of a language gap? Does that mean **all** application
software is just a language gap?"

"Let's not be silly," you say. "I can split a hair and create a tiny
distinction between software I shouldn't have to write and software I
should have to write."

I remain incredulous.

Design Patterns as Damage
-------------------------


The idea that somehow the GoF design patterns are a problem is also
goofy. The GoF design patterns are pretty slick. They solve a fairly
broad suite of problems in an elegant and consistent manner.

They're just good design.

Yes, they can be complex. Sorry about that. Software can be complex if
you want really excellent flexibility and extensibility.

AND.

Bonus.

Software can be complex when you have to work around the problems of
"compiler" and "locked libraries" and "no source." That is, the GoF
patterns apply in full force for C++ and Java where you're trying to
protect your intellectual property by disclosing only headers and
obfuscated implementation details. Indeed, there are few alternatives
to the GoF patterns if you're going to distribute a framework that has
no visible source and needs to leave extension points for users.

If you don't have Locked-NoSource-Compiled code as a backdrop, the GoF
patterns can be simplified a little. But some of the patterns are
essential. And remain essential. There are some really great ideas
there.

In Python world, we rely on a modified subset of the GoF patterns.
They work extremely well.

When writing functional-style Python using immutable data structures
(to the extent possible), we use a different set of design patterns.
Not so many GoF patterns when we're trying to avoid stateful objects.
But some patterns (like the Abstract Factory) are really very helpful
even in a largely functional context. It morphs from an abstract
factory **class** to a factory **function**, and it loses the
"abstract" concept that's part of C++ and Java, but the core
**Factory** design pattern remains.

The Serious Issue
-----------------


The serious issue that is surfaced by the email is Language Mapping.
We cannot (and must not) try to map languages to each other. What is
true for Java design is emphatically not true for Python design. And
it doesn't apply to assembly languages, FORTRAN, FORTH, or COBOL.

Languages are different.

There. I said it.

If there was an underlying "universal deep structure" behind all
programming languages, the surface features would be merely syntax,
and we'd have automated translation among languages. The universal
deep structure (the underlying Turing Machine that does computations)
appears to be too abstract to map well among programming languages.
Hence the lack of translators.

When switching among languages, it's important to leave all baggage
behind.

When moving from Java < 8 to Java >= 8<8 java="" to=""> (i.e.,
non-functional Java to more functional Java) we can't **trivially**
map all design patterns among the language features. It's a new
language with new features that happens to be compatible with the old
language.

Attempting to trivially map concepts between non-functional (or
strictly-OO Java) and more functional Java leads to dumb conclusions.
Like the GoF patterns are dying. Or the GoF patterns represent damage
or something else equally goofy.

   **The language changes lead to design pattern changes.**


Language change doesn't deserve an gleeful/anguished blog post
celebrating/lamenting the differences. It's a consequence of learning
a new language, or new features of an existing language.

Please avoid mapping languages to each other.



-----

Great Info!!! Thanks for sharing information with ...
-----------------------------------------------------

Sathya<noreply@blogger.com>

2019-08-30 06:38:50.550000-04:00

Great Info!!! Thanks for sharing information with us. If someone wants
to know about `Safety Software <https://neoehs.com>`__ and `Health and
Safety Software <https://neoehs.com/>`__ I think this is the right place
for you.





