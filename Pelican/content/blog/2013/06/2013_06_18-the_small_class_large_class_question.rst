The Small Class Large Class "Question"
======================================

:date: 2013-06-18 08:00
:tags: project management,object-oriented design,software process improvement
:slug: 2013_06_18-the_small_class_large_class_question
:category: Technologies
:status: published

Tweet:

   People criticize for making tons of small classes instead of fewer
   larger classes.How is well-organized code more difficult to
   understand?

   — jim christopher (@beefarino) `May 31,
   2013 <https://twitter.com/beefarino/status/340533020815675392>`__


This isn't really a question. Writing a few "large" omnibus classes is
simply bad design.

There are several variations on the theme of principles of OO
programming. None of them include "a few large omnibus classes with
nebulous responsibilities."

Here's one set of principles: `Class Responsibility
Collaboration <http://leanagilechange.com/leanagilewiki/index.php?title=Class_Responsibility_Collaboration>`__.
Here's one summary of responsibility definition: "Ask yourselves what
each class knows and what each class does".  Here's another: "A
responsibility is anything that a class knows or does." from `Class
Responsibility Collaborator (CRC)
Models <http://www.agilemodeling.com/artifacts/crcModel.htm>`__.

This idea of responsibility defined as "Knows or Does" certainly seems
to value focus over sprawling vagueness.

Here's another set of principles from `Object-Oriented
Design <http://www.oodesign.com/design-principles.html>`__; these echo
the `SOLID
Principles <http://en.wikipedia.org/wiki/SOLID_(object-oriented_design)>`__
without the clever acronym.

Getting down to S: a single reason to change means that the class must
be narrowly-focused. When there are a few large classes, then each
large class has to be touched for more than one reason. By more than
one developer.

Also, getting to O: open to extension, closed to modification requires
extremely narrow focus. When this is done well, new features are added
via adding subclasses and (possibly) changing an initialization to
switch which **Factory** subclass is used.

But Why?
--------

Why do people reject "lots of small classes"?

Reason 1.
    It's hard to trivially inspect a complex solution. I've had
    an argument similar to the one Beefarino alludes to.  In my case, it
    was a manager who simply didn't schedule the time to review the design
    in any depth.

Reason 2.
    Folks unfamiliar with common design patterns often see them
    as "over-engineered". Indeed, I've had programmers (real live Java
    programmers, paid to write Java code) who claimed that the java.util
    data structures (specifically Map, TreeMap and HashMap) were needless,
    since they could write all of that using only primitive arrays. And
    they did, painstakingly write shabby code that had endless loops and
    lookups and indexing garbage instead of simply using a Map.

Reason 3.
    Some folks with a strong background in simple procedural
    programming reject class definitions in a vague, general way. Many
    good programmers work out ways to do encapsulation in languages like
    C, Fortran or COBOL via naming conventions or other extra-linguistic
    tricks.

They deeply understand procedural code and try to map their ideas of
functions (or subroutines) and their notions of "encapsulation via
naming conventions" onto OO design.

At one customer site, I knew there would be friction because the
project manager was very interested in "code conventions" and "naming
conventions". This was a little upsetting at the time. But I grew to
realize that some folks haven't actually seen any open source code.
They don't understand that there are established international,
recognized conventions for most programming languages, and examples
are available on the World Wide Web. Just download a popular package
and read the source.

The "naming conventions" was particularly telling. The idea that Java
packages (or Python packages and modules) provide distinct namespaces
was not something that this manager understood. The idea that a class
defines a scope was not really making much sense to them.

Also Suspicious
---------------

Another suspicious design feature are "utility" packages. It's rare
(not impossible, but rare) for a class to truly be interpackagial in
scope and have no proper home. The "java.util" package, for example,
is a strange amalgamation of the collection data structures, national
and cultural class definitions (calendars, currency, timzones, etc.)
handy pattern abstractions, plus a few algorithms (priority queue,
random).

Yes, these have "utility" in that they're useful. They apply broadly
to many programming problems. But so does java.lang and java.io. The
use of a vague and overly inclusive term like "util" is an abdication
of design responsibility to focus on what's really being offered.

These things do not belong together in a sprawling unfocused package.

Nor does disparate functionality belong in a sprawling, unfocused
class.

Education
---------

The answer is a lot of eduction. It requires time and patience.

One of the best methods for education is code walkthroughs. This
permits reviews of design patterns, and how the SOLID principles are
followed (or not followed) by code under development.





