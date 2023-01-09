The Ubiquitous Object
=====================

:date: 2011-05-10 08:00
:tags: procedural programming,OO design
:slug: 2011_05_10-the_ubiquitous_object
:category: Technologies
:status: published

Objects are everywhere.

Weirdly, some people can't see them. I guess they live in a rarified,
HP Lovecraftian world of pure action inhabited by amorphous things
that can't be properly called "beings" but rather "doings" because
they're pure activity with no existence.

Read
"`Hypnos <http://www.hplovecraft.com/writings/texts/fiction/hy.asp>`__".
"They were sensations, yet within them lay unbelievable elements of
time and space—things which at bottom possess no distinct and
definite existence."

Got this comment the other day.

        ... doing procedural code correctly when you don't want to be
        bothered w/ OO is a separate and big enough topic that warrants
        its own book or monograph.

I guess that means that objects, and the reality that they model, are
a "bother"—a pitfall to be avoided—a cost with no benefit. This is
not the first time I've heard this, and—like Lovecraft—it leads me to
wonder how such a rich and weird phantasy world gets constructed.

I had a project manager exclaim "You don't need more than seven or
eight objects to write any application." I didn't press the person on
that point. I assumed that they were talking about classes (not
objects) and, further, had conflated class with "elaborate
module-like library packed with amazing features". Or maybe they
conflated class with package. Or something. It's hard for me to dig
into misapprehensions and false assumptions without being rude.

There are a surprising number of misapprehensions. I'm occasionally
tempted to turn `NTLK <http://www.nltk.org/>`__ loose on all
questions tagged "Python" on Stack Overflow. With some patient
reading, I think I could develop a taxonomy of OO confusion. However,
let's just focus on this comment.

**The Bother Factor**

Why is OO a "bother"?

#.  I've been told that OO programming is *different*. Different from
    what? From procedural programming without objects, I guess.

#.  I'm been told that some problems are a better fit for OO, and some
    problems aren't a good fit for OO. This is hard to parse because
    it makes the more profound claim that some problems weirdly don't
    involve any "objects" just pure actions.

#.  The `Object-Relational Impedance Mismatch <http://en.wikipedia.org/wiki/Object-relational_impedance_mismatch>`__
    problem somehow indicts object-oriented programming as unsuitable
    when there's a relational database involved.

Let's look at some of these in a little depth to see the
underlying fallacies.

**Procedural Is More Fundamental**

This is subtle and pernicious. An OO language contains within it a
procedural language. Because of this, we can use Java, C++ or Python
to write Fortran-like (or VB-like) crapola code. It's possible to
write everything in a single, massive, static class with piles of
random global variables, long lists of disorganized methods, and
"adaptation via block comment" buffoonery.

Some folks object to characterizing procedural programming as random,
disorganized or buffoonery. They tell me that a purely procedural can
be neat and well organized with tidy, focused modules that have
narrowly-defined responsibilities, no global variables and clever
techniques like pointer-to-function to support adaptation.

Wait. The idea of tidy, focused modules with narrowly-defined
responsibilities is exactly what a class is.

This is important. **All good procedural programming is isomorphic to
object-oriented programming minus the class definitions**.

Procedural isn't "fundamental". It's just a "fragmentary". Procedural
programming is a subset of object-oriented programming. Not a
foundation. We can, for example, do functional-style object-oriented
programming by using immutable objects.

**Some Problems Aren't A Good Fit**

Claiming that there are problems which don't fit the object-oriented
paradigm is false. Or such a claim hearkens to a more elaborate
ontology in which existence somehow doesn't matter.

This question is typical: "`What should be OO and what
shouldn't? <http://stackoverflow.com/questions/178262/what-should-be-oo-and-what-shouldnt>`__"

When a program "runs" or "executes" there is state change. In a lazy
functional world, state change is characterized by the creation and
destruction of immutable objects: the new "4" that's created by
"2+2".

In order for there to be state, there must be an object that has a
state of being. Objects are inherent in doing any computing of any
kind.

Some folks like to lift up stored procedures or shell scripts as
"important" examples of non-OO programming. Mostly, these just show
that a non-OO language can persist for a long time because clever
programmers can work around a lot of limitations. (`Turing
Completeness <http://en.wikipedia.org/wiki/Turing_completeness>`__ is
a necessary pre-condition; not a desirable feature set.)

[And yes, I've written multiple-thousand line shell scripts so
customers can avoid paying a license fee for a proper compiler. Just
because it *can* be done doesn't mean it *should* be done.]

This is important. **All Programming Involves Objects**.

There are really just two "paradigm" decisions. Does the problem
involve *new* class definitions or can it be done using built-in
classes? Does the problem involve mutable objects or immutable
objects?

Software that uses only built-in classes is termed "procedural".
Software that uses only immutable objects is termed "functional".
Software that uses mutable objects is mistakenly termed
"object-oriented".

**Object-Relational Mismatch**

This isn't really very interesting, no matter how many times people
like to flog it. Use an ORM. Move on.

Further, it's important to recognize that normalization, foreign
keys, cascading deletes and other malarky are hacks imposed on us by
several relational database limitations. These are not *essential*
parts of any problem.

I don't know how many times I've had to answer the "how do I do
foreign keys in Java/C++/Python?" question. The answer is always the
same: foreign keys are a hack-around because there are no proper
object references in a relational database.

**What's Left?**

In spite of the obvious logic that OO is central, there is always a
residual "It's a bother" sense from folks who's first language was
not an OO language.

As far as I can tell, the "bother" stems from simple ignorance of
what's *really* going on. Many programmers can't articulate any
design principles. Yet, they tend to follow some principles rather
closely. Ask them what they're doing. Read their code. Almost
everyone who codes has some set of fundamental principles. (The few
exceptions are people who seem to write code more-or-less randomly
and still manage to arrive at something that appeared to "work";
these people do exist and are very scary.)

Many programmers don't follow **all** of the `SOLID
Principles <http://en.wikipedia.org/wiki/Solid_(object-oriented_design)>`__.

Many programmers follow the SOLID principles using different
nomenclature. The SOLID initials and acronyms are just one one goofy
terminology. There are more principles than these, and the principles
can have other names.

What's important is that (except for rare exceptions) **all**
programmers follow some of the SOLID principles. Some follow all of
them. Some follow numerous additional principles beyond these. Some
give their principles other names.

The folks who claim OO programming is a "bother" just don't happen to
recognize that they're already following some of the SOLID principles
and actually doing OO programming with built-in classes.

**Doing Procedural Programming Correctly**

Bottom Line: "doing procedural code correctly" is simply OO
programming using only built-in classes.

It's not a "big" topic. It's entirely an exercise in learning how to
apply someone else's nomenclature to one's existing principles.





