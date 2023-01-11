Great Lies: "Design" vs. "Construction"
=======================================

:date: 2010-03-11 11:37
:tags: software process improvement,project management,architecture
:slug: 2010_03_11-great_lies_design_vs_construction
:category: Technologies
:status: published

In reflecting on Architecture, I realized that there are some profound
differences between "real" architecture and software architecture.

One of the biggest differences is design.

In the earliest days, software was built by very small groups of very
bright people. Alan Turing, Brian Kernighan, Dennis Ritchie, Steve
Bourne, Ken Thompson, Guido van Rossum. (Okay, that last one says
that even today, software is sometimes built by small groups of very
bright people.) Overall architecture, both design and construction
where done by the same folks.

At some point (before I started in this business in the '70's)
software development was being pushed "out" to ever larger groups of
developers. The first attempts at this -- it appears -- didn't work
out well. Not everyone who can write in a programming language can
also design software that actually works reliably and predictably.

By the time I got my first job, the great lie had surfaced.

    **There are Designers who are distinct from Programmers.**

The idea was to insert a few smart people into the vast sea of
mediocre people. This is manifestly false. But, it's a handy lie to
allow managers to *attempt* to build large, complex pieces of
software using a a larger but lower-skilled workforce.

**Reasoning By Analogy**

The reasoning probably goes like this. In the building trades there
are architects, engineers and construction crews. In manufacturing,
there are engineers and factory labor.

In these other areas, there's a clear distinction between design and
construction.

Software must be the same. Right?

Wrong.

The analogy is fatally flawed because there is no "construction" in
the creation of software. Software only has design. Writing code is
-- essentially -- design work.

**Architecture and Software Architecture**

Spend time with architects and you realize that a good architect can
(and often does) create a design that includes construction details:
what fastenings to use, how to assemble things. The architect will
build models with CAD tools, but also using foam board to help
visualize the construction process as well as the final product.

In the software realm, you appear to have different degrees of
detail: High Level Design, Detailed Design, Coding Specifications,
Code.

High Level Design (or "Architecture") is the big picture of
components and services; the mixture of purchased plus built;
configuration vs. constructions; adaptation vs. new development. That
kind of thing. Essential for working out a budget and plan for buying
stuff and building other stuff.

Usually, this is too high-level for a lot of people to code from.
It's planning stuff. Analogous to a foam-board overview of a
building.

Detailed Design -- I guess -- is some intermediate level of design
where you provide some guidance to someone so they can write
programming specifications. Some folks want this done in more formal
UML or something to reveal parts of the software design. This is a
murky work product because we don't have really formal standards for
this. We can claim that UML is the equivalent of blueprints. But we
don't know what level of detail we should reveal here.

When I have produced UML-centric designs, they're both "too
technical" and "not detailed enough for coders". A critique I've
never understood.

Program Specifications -- again, I'm guessing -- are for "coders" to
write code from. To write such a thing, I have to visualize some code
and describe that code in English.

Let's consider that slowly. To write programming specifications, I
have to

#. Visualize the code they're supposed to write.

#. Describe that code in English.

Wouldn't it be simpler to just let me code it? It would certainly
take less time.

**Detailed Design Flaws**

First, let me simplify things by mashing "Detailed Design" and
"Specification" together, since they seem to be the same thing. A
designer (me) has to reason out the classes required. Then the
designer has to pick appropriate algorithms and data structures
(HashMap vs. TreeMap). Then the designer has to either draw a UML
picture or write an English narrative (or both) from which someone
else can code the required class, data structure and algorithm.
Since you can call this either name, the names don't seem to mean
much.

I suppose there could be a pipeline from one design document at a
high level to other designs at a low level. But if the low-level
design is made difficult by errors in the high-level design, the
high-level designer has to rework things. Why separate the work? I
don't know.

When handing things to the coders, I've had several problems.

#.  They ignore the design and write stuff using primitive arrays
    because they didn't understand "Map", much less "HashMap" vs.
    "TreeMap". In which case, why write detailed design if they
    only ignore it? Remember, I provided specifications that were
    essentially, line-of-code narrative. I named the classes and
    the API's.

#.  They complain about the design because they don't understand
    it, requiring rework to add explanatory details. I've gone
    beyond line-of-code narrative into remedial CS-101. I don't
    mind teaching (I prefer it) but not when there's a silly
    delivery deadline that can't be met because folks need to
    improve their skills.

#.  They find flaws in the design because I didn't actually write
    some experimental code to confirm each individual English
    sentence. Had I written the code first, then described it in
    English, the description would be completely correct. Since I
    didn't write the code first, the English description of what
    the code *should be* contained some errors (perhaps I failed to
    fully understand some nuance of an API). These are nuances I
    would have found had I actually written the code. So,
    error-free specifications require me to write the code first.

My Point is This.

    **If the design is detailed enough to code from -- and error free -- a designer must actually write the code first.**

Indeed, the designer probably should simply have written the
code.

**Architecture Isn't Like That**

Let's say we have a software design that's detailed enough to
code from, and is completely free from egregious mistakes in
understanding some API. Clearly, the designer verified each
statement against the API. I'd argue that the best way to do
this is to have the compiler check each assumptions. Clearly,
the best way to do this is to simply write the code.

"Wait," you say, "that's going too far."

Okay, you're right. Some parts of the processing do not require
that level of care. However, some parts do. For instance,
time-critical (or storage-critical) sections of algorithms with
many edge cases require that the designer build and benchmark
the alternatives to be sure they've picked the right algorithm
and data structure.

Wait.

In order for the designer has absolute certainty that the
design will work, they have to build a copy that works before
giving it to the coders.

In architecture or manufacturing, the construction part is
expensive.

*In software, the construction part does not exist*. Once you
have a detailed design that's error-free and meets the
performance requirements, you're actually done. You've created
"prototypes" that include all the required features. You've run
them under production-like loads. You've subjected them to unit
tests to be sure they work correctly (why benchmark something
that's incorrect?)

There's nothing left to do except transition to production (or
package for distribution.)

Software Design

There's no "detailed design" or "programming specifications" in
software. That pipeline is crazy.

It's more helpful to think of it this way: there's "easy stuff"
and "hard stuff".

-   **Easy Stuff** has well-understood design patterns, nothing
    tricky, heavy use of established API's. The things where the
    "architectural" design can be given to a programmer to
    complete the design by writing and testing some code.
    Database CRUD processing, reporting and analysis modules,
    bulk file processing, standard web form processing for data
    administration, etc.

-   **Hard Stuff** has stringent performance requirements, novel
    or difficult design patterns, new API's. The things where
    you have to do extensive design and prototyping work to
    resolve complex or interlocking issues. By the time there's
    a proven design, there's also code, and there's no reason
    for the designer to then write "specifications" for someone
    to reproduce the code.

In both cases, there are no "coders". Everyone's a designer.
Some folks have one design strength ("easy stuff",
well-known design patterns and API's) and other folks have a
different design strength.

There is no "construction". **All of software development is
design**. Some design is assembling well-known components
into easily-visualized solutions. Other design is closer to
the edge of the envelope, inventing something new.



-----

Website Design Canada...
-----------------------------------------------------

David<noreply@blogger.com>

2010-03-12 01:31:03.040000-05:00

`Website Design Canada <http://www.aguaesolutions.com/webdesign.html>`__
is very helpful for a web site Designing.Designing of a website plays an
important role in business.Effective design attracts people very
easily..


Check out the book &quot;The Nature of Design&quot...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-03-21 17:29:02.287000-04:00

Check out the book "The Nature of Design" by David Pye





