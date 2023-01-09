Advanced Programming
====================

:date: 2007-03-02 15:43
:tags: books,building skills,#python
:slug: 2007_03_02-advanced_programming
:category: Books
:status: published





First, I'm really pleased to see a focus on
end-user applications of Python.  It seems like most of the Open Source
Community likes to build infrastructure, operating systems, servers, frameworks
and components.  Maybe I'm looking in all the wrong places, but I have a soft
spot in my heart for the final applications of a technology stack, separate from
the technology stack itself.



Second, there's a very pleasing symmetry about the outline:

-   Strategies for Tackling Larger Problems

-   Language Features

-   Library Features

-   Tools and Process

-   Higher-Order Architectures: web and database.



I shouldn't gush too much,
but I like the organizing patterns.  The course is mashed into three days,
however, which leaves two areas that won't be done very well.  Both of these are
skill-related, and they are derived from the central implicit skill of
programming: abstraction.  Not everyone gets abstraction, and I think any
intermediate or advanced programming course has to make abstraction a background
theme that runs through the course.



One area needs to be expanded and the other needs to be
focused.



**Strategies for Tackling Larger Problems.** 



Introductory programming
courses are always about language, library and tools.  More advanced programming
courses are really about the design patterns, how to tackle a larger real-world
problem, what works and what doesn't work.  I think one important skill for
advanced programming is being able to apply the principle of abstraction well
and refactor to manage coupling and
cohesion.



Clearly, two of the topics
(packages and reusability) touch on this larger strategic issue.  However, there
is more that must be covered.  Here's how I think it should be
done.

1.  The Packages and Reusability material is a
    foundation of an "agile" in design.

2.  A good package design is an agile design,
    which means some other things:  a well-defined Model, a carefully-specified
    interface, and some provision for learning as you go.  These topics (data model
    and interface) aren't really called out in the course outline, but they're
    central to answering the question "what makes a good package?"

3.  A good package will get that way after it is
    refactored.  This is the more important thing which is missing: how to factor
    and refactor a package.



Following up on `r0ml <http://r0ml.net/blog/>`_ 's
presentation at `PyCon 07 <http://us.pycon.org/TX2007/Keynotes>`_, a package is really a rhetorical
device to make the overall application make sense.  It's also a component which
can (and will) evolve.  Newbies don't often see clear rationale behind package
boundaries and create odd collections of
components.



The only way to learn good
packaging is to actually do rework.  I think that this section has to include
notes on how to build a package, rebuild a package, expand a package, and then
refactor a package into smarter
sub-packages.



**Larger Architectures are Hard.** 



The example
curriculum has two large architectures jammed into a one day.  I hadn't really
thought about this before, but I know that larger client-server architectures
are hard for some programmers to grasp.  The issue is how to apply the principle
of abstraction to interface design and the separation of
concerns.



What I've found is that
programmers who are first coming to grips with a multi-tiered architecture
struggle with several issues.

1.  They don't "control" the other side of the
    relationship.  Writing a web server means you don't control the browser. 
    Writing a DB client means you don't control the DB server.  The basic "What is
    going on here?" takes considerable classroom time to sort through.  I remember
    teaching an RDBMS class to folks designing a military application, and the idea
    of SQL optimization scared the willies out of them.  They wanted consistent
    performance, and -- for some reason -- the idea that most of the time the
    database would do better than worst-case was very scary.  They'd be happier with
    worst-case all the time instead of generally better with a few spikes of
    worst-case.

2.  There are these "protocols" involved.  Most
    net protocols are pleasant, but irrelevant answers to bar-bet trivia questions. 
    Suddenly ODBC, DB-API, HTTP, WSGI become serious.  Indeed, until you embark on
    client-server programming, you never really understand "protocol" and when you
    do, it's a shocker.  The pragmatic topics of "why doesn't it do that?" have to
    morphed into "here are the design patterns for implementing X with the
    established protocols."  This can be a long, painful conversation, including "I
    don't see why it has to be that way" and "That's way too much overhead, why
    can't I just call a function on another server?"

3.  There are the other, foreign languages
    involved.  HTML, CSS, SQL, etc. muddy up the waters seriously.  It's hard to
    gloss over SQL issues by saying "Here's a 'typical' SELECT statement" and
    leaving it at that.  It leaves the unprepared.  I find that an overview of SQL
    is an all-day affair.



The class is
three hours of instruction.  An hour on SELECT, and hour on RDBMS and related
protocols and an hour on typical Python applications using DB-API is -- well --
the whole day.



Similarly, for the web
class.  An hour in HTML, an hour on HTTP, WSGI and the like, and an hour on
typical Python applications is the whole day. 




**Summary.** 



This outline is very helpful for me, as a technology consultant.  Many thanks.



I find that there are a number
of essential skills which need to be included in this kind of
course.

-   Abstraction, and how it is applied to
    initial design, refactoring, and separation of concerns.  What I find is that
    some people are comfortable switching languages and architectures because they
    work at a higher level of abstraction and then implement in the tools at hand. 
    Much of the rest of the world cuts and pastes example code, and can't be
    bothered to work through the problem using the hard-to-master technique of
    "abstraction". 

-   Organization and Management, and how to
    do incremental work and rework to tackle a large problem in a rational approach.
    The MVC design pattern, for example, should inform the presentation of the
    various libraries to show where the library applies in a larger
    program.

-   Testing.  Writing tests is hard.  It
    requires a grip on what's should happen and what shouldn't happen.  It requires
    really careful logical thinking to work though the domain of possible states to
    prove which state applies to an assertion in a test case.

-   Debugging and diagnostic skills are often
    the ones in shortest supply.  I often find one or two students who are
    "flailers", they can't seem to be able to reason through a diagnosis; we have to
    spend considerable time on "what can you PROVE is true after this statement?"
    and "For this function to do [X], what MUST have been true about the variables?"
    This sometimes requires considerable prodding, particularly in complex
    architectures.



These are themes, not
proper topics.  They are "aspects" that must be present in each module of
instruction.



Large Architectures (Web
or Database) are multi-day affairs in their own right.  I wouldn't attempt both
in a single day.






