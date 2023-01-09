On Waiting to Write "Serious Code"
==================================

:date: 2015-06-10 07:40
:tags: OO design,design,tools,software process improvement
:slug: 2015_06_10-on_waiting_to_write_serious_code
:category: Technologies
:status: published


Someone told me they weren't yet ready to write "serious code." They
needed to spend more time doing something that's not coding.

I'm unclear on **what** they were doing. It appears they have some
barriers that I can't see.

They had sample data. They had a problem statement. They had an
existing solution that was not very good. I couldn't see any reason
for waiting. Indeed, I can't figure out what "serious" code is. Does
that mean there's frivolous code?

Because there was a previous solution, they had a minimum viable
product already defined: it has to do what the previous version did,
only be better in some way. One could trivially transform the previous
product into unit test cases and an acceptance test case. Few things
could be more amenable to coding than having test cases.

Since everything necessary seemed to be in place, I had a complete
brain cramp when they mentioned they weren't yet ready to write
"serious" code. "Serious?" Seriously?

It appears that this developer suffers from a bad case of Fear of
Code™. I know some common sources of this fear.

#.  Waterfall Project Experience (WPE™.) Old people (like me,) who
    started in Waterfall World, were told that we had to produce
    mountains of design before we produced any code. No one knew why in
    any precise way. Indeed, there's ample evidence that too much design
    is simply a way to introduce noise into the process. In spite of real
    questions, some folks think that you can write a design so detailed
    that a coder can just type in the code from the design. (This level
    of design is isomorphic to code; to avoid ambiguity it must be
    written as code.)

#.  Relational Database Hegemony (RDH™.) Folks (like me,) who were DBA's,
    know that databases require a lot of design and a lot of review
    before they can be created. Writing stored procedures requires even
    more design and review time. You don't just slap an SP out there. It
    might be "bad" or "create problems." Also, when you insist on DBA's
    writing application code, it takes super-detailed, code-level design
    details. In effect, you must write the code for the DBA to write your
    code back to you.

#.  One and Done (OAD™.) Some people like to feel that they can write
    code once and it can be a thing of beauty and a joy forever. The idea
    of a rewrite is anathema to these people. While this is obviously
    silly, people still like the conceit that they can produce some
    prototype code that will be a proper part of every future release
    forever and always. It's not possible to make all of the decisions
    the first time regarding adoption and scaling and user preferences.
    Your prototype code will get replaced eventually: get over it. Write
    the prototype, get funding, move forward. Don't dither trying to make
    a bunch of future-oriented decisions based on a future you cannot
    actually foresee. You can't "future-proof" your code.

#.  Learnings are Expensive (LAE™.) You can find people that think that
    the sequence of (spike, POC, version 0, version 1) is too expensive.
    They are sure that learning is a project drag, since no "tangible"
    results are created by learning. This means that they don't value
    intellectual property or knowledge work, either; an attitude is
    actually destructive to the organization. Knowledge is everything:
    software captures knowledge: a spike followed by a POC followed by
    version zero will arrive on the scene more quickly than any
    alternative strategy. Don't waste time trying to write version 1 from
    a position of ignorance.

#.  Tools are Expensive (TAE™.) Some people feel that -- since tools are
    expensive -- they should be used rarely. Back in the olden days, when
    a compiler took many minutes to produce an error report, you had to
    be sure the code was good. (I'm old enough that I remember when
    compiles took hours. Really.) Those days are gone. Most compilers
    today work at the "speed of light" -- if they were any faster, you
    couldn't tell, because you can't click any faster. For dynamic
    languages, like Python, the speed with which code can be emitted
    makes all tool considerations quaint and silly.

#.  Diagram it to Death (DTD™.) Rather than write code, some folks would
    rather talk about writing code. To them, email, powerpoint, and
    whiteboard are cheaper than coding. This is a false economy. Nothing
    is saved by avoiding code. Time is wasted drawing diagrams of things
    at a level of detail that mirrors the code. Pictures aren't bad in
    general. Detailed pictures are simply a stalling tactic.


I find it frustrating when people search for excuses to avoid simply
creating code. While I see a number of sources, there are many
counter-arguments available.

#.  Waterfall is dead. Make something minimal that works for this
    sprint. Call it a "spike" if that makes you happier. Clean it up
    in the next sprint. Create value early. Expand on the features
    later.

#.  Databases are free now. SQLite and similar products mean that we
    can prototype a database without waiting around for DBA's to give
    us permission to make progress. Build the database now, get
    something that works. Rework the database as your understanding of
    the problem matures. Rework the database as the problem itself
    matures and morphs. Nothing is static; the universe is expanding;
    do something now.

#.  No code lasts forever. Waiting around to create some kind of
    perfect value one time only is perfect silliness. Create value
    early and often. Discarding code means you're making progress. If
    you think it's important, write "draft" on every electronic
    document which might get changed. (Hint: version numbers are
    smarter than putting "draft" everywhere.)

#.  A spike and code happens more quickly than code. It's a matter of
    technical risk: unfinished work is an "exposure" -- an unrealized
    investment. Failing soon is better than researching extensively in
    an effort prevent a failure that could have been found quickly.

#.  Use a dynamic language and avoid all overheads.

#.  Keep the diagrams high-level. Code is the only way to meaningfully
    capture details. Code endures better than some out-of-date Visio
    file that's in Sharepoint completely disconnected from GitHub.

It's imperative to break down the roadblocks. All "pre-coding"
activities are little more than emotional props: knock them down
and start coding.





