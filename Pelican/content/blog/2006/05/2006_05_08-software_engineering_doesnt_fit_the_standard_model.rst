Software Engineering doesn't fit the Standard Model
===================================================

:date: 2006-05-08 11:06
:tags: architecture,software design,complexity,numerosity
:slug: 2006_05_08-software_engineering_doesnt_fit_the_standard_model
:category: Architecture & Design
:status: published





Nisley says "Imagine a programming contractor
proposing that increasing the average interrupt latency by 10 μs would
reduce the module size by 5 percent and improve the error rate by 3 percent. 
When was the last time you saw precise numeric relations between various aspects
of a  programming project, before the coding began, that actually worked out as
intended?"



Precise Numeric Relations
-------------------------



First -- and foremost --
we have to recognize that programming is always about creating something
radically new.  If there was existing, measurable, quantifiable, well-known
stuff, we'd just use it.  It's software -- it's adaptable by definition. 
Indeed, when the problem is well-understood, with well-known numeric
relationships, then that means there is an existing body of code, and we're not
really programming.  We're either simply installing or we're
configuring.



I find that this "a software design should be fully quantifiable" approach leads to some common
management mistakes.  Principally, it overlooks that fact that software
engineering isn't like most other forms of engineering because *construction*
is essentially free.

-   The final, complete, detailed design is
    isomorphic to the code.  The additional cost to do the coding from a complete
    design is essentially zero, it's recompiling the design into an executable form.
    What we call the "construction" phase of a development project is really the
    tail end of detailed design, merged into the hand-translation of that complete
    design into an executable form.  No additional design artifact is produced
    separate from the executable form of the design, making this distinction
    blurry.

-   If someone does know everything about a
    given problem, we can often download their solution.

-   Software is cloneable at zero additional
    cost; we are not laying bricks with a fixed cost per brick
    laid.



This conflation of software
engineering and other engineering leads to some strange mismanagement
behaviors.



1.  Mismanagers presume they can (and will) gather complete knowledge of the problem, the solution and the
    technology at design time.
    This complete knowledge can only be gathered if we
    have software in place that we can base our measurements and models on.  But if
    we have this software, and it provides a complete, accurate model, why are we
    programming?  If it works so well that it is the basis for quantified judgement,
    why not just use it?



2.  Mismanagers presume we have repeatable task execution while doing software development.
    In manufacturing and construction, the foremen and general contractors look at
    repeated execution of tasks, which is unlike the one-off world of software
    development.  When we perform tasks repeatedly, we gain a quantitative model.
    In software, we build it once and clone it many times.  If you have a detailed
    model of the tasks involved in construction, you must be *rewriting*
    the same software on which your model is sbased.



Managers have to get comfortable
working in a framework of what is unknown, and look at software construction
projects as an exercise in reducing their ignorance.  Demanding that something
should be fully quantifiable is essentially a self-contradiction -- we can't
know everything until we are done with a design which is isomorphic to the code
itself.  To understand software, one must understand Armour's Five Orders of
Ignorance http://www.computer.org/portal/site/software/menuitem.538c87f5131e26244955a4108bcd45f3/index.jsp?&pName=software_level1&path=software/bookshelf/2005&file=2005s1fre.xml&xsl=article.xsl&.



Before Coding Began
--------------------



My second complaint -- and this is more subtle -- is the question of "before the coding began."
This bothers me because it implies a strict "all-design-before-any-code" world
view.  This kind of world view often looks with suspicion on prototypes and
experiments.  This kind of "analyze the design on paper" management style is
good for many things.  It is particularly good for database design, and I don't
mean to devalue it completely.  However, it does lead to a number of big
mistakes.



Without getting all Agile http://agilemanifesto.org/,
it's important to note that the time before the coding begins is the time before
the project begins.  During the earliest of scope-defining phases, there is room
for prototypes and mock-ups that involve code, and may actually be
production-ready elements of the final
deliverable.



Further, software involves
hellish complexity because of the huge spread in orders of magnitude (from bits
to gigabytes, often 10 orders of magnitude) and from nanoseconds to 168 hours
each week (another dozen orders of magnitude).  Simulation, modeling,
incremental development and testing, and reengineering are part of the software
development process.  All of this involves coding.



The most important reason that
there is not time before the coding began is because the code is actually the
final step in the detailed design.  Since the code is the most detailed level of
the design, all design details are code.  As soon as you look at details in one
area, you're looking at code.



The twin mistakes of "fully quantifiable" and "before coding began" are impediments to
good software development.  They can't be looked at as desirable features of a
software engineering process.  If we aim for fully quantifiable, we have to
ignore the fact that the cost for software is all design cost.  One consequent
mistake is to think that there's some benefit in separating the final phase of
design from coding the design in the executable language.  











