Breaking into Agile
===================

:date: 2009-10-22 21:44
:tags: scrum,agile
:slug: 2009_10_22-breaking_into_agile
:category: Technologies
:status: published

I had a recent conversation with some folks who were desperate to
"processize" everything. They were asking about Scrum Master
certification and what standards organizations define the "official"
Scrum method.

Interestingly, I also saw a cool column in Better Software magazine,
called
"`Scrumdamentalism <http://stickyminds.com/BetterSoftware/magazine.asp?fn=citoc>`__"
on the same basic question.

In my conversation, I referred them to the `Agile
Manifesto <http://agilemanifesto.org/>`__. My first point was that
process often gets in the way of actual progress. Too much process
focus lifts up "activity" in place of "accomplishment".

My second point, however, was that the Agile Manifesto and the
Scrum method are responses to a larger problem. Looking for a
process isn't an appropriate response to the problem.

The One True Scrum Quest
------------------------

Claiming that there's one true Scrum method and everything else is
"not scrum" is an easy mental habit. The question gets asked on
Stack Overflow all the time. The questions are usually one of two
kinds.

-   What's the "official" or "best practice" Scrum method and how
    do I define a process that rigidly enforces this for my entire
    team of 20?

-   We are doing our design/code/test/integration/release in a way
    that diverges from the "official" form in the Ken Schwaber and
    Mike Beedle
    `book <http://www.amazon.com/Agile-Software-Development-Scrum/dp/0130676349>`__.
    Or it diverges from the
    `Eclipse <http://epf.eclipse.org/wikis/scrum/Scrum/guidances/supportingmaterials/scrum_overview_610E45C2.html>`__
    version. Or it diverges from the `Control
    Chaos <http://www.controlchaos.com/about/>`__ overview. Or the
    `Mountain Goat <http://www.mountaingoatsoftware.com/scrum>`__
    version. Or the `C2
    Wiki <http://c2.com/cgi/wiki?ScrumOverview>`__ version. Or
    `this <http://codebetter.com/blogs/darrell.norton/articles/50339.aspx>`__
    version. Is it okay to diverge from the "standard"?

Sigh. The point of Agile is that we should value "Individuals
and interactions over processes and tools". The quest for "One
True Scrum" specifically elevates the process above the people.

In The Real World
-----------------

The biggest issue is that the Agile Manifesto is really a
response to some fundamental truths about software development.

In management fantasy world, a "project" as a fixed, definite,
limited, clearly articulated scope. From this fixed scope, we
can then document "all" the requirements (business and
technical). This requirements document is (a) testable against
the scope, (b) necessary for all further work and (c)
sufficient for design, code, test and transition to production.
That's not all. And -- in order to make a point later on --
I'll continue to enumerate the fantasies. The fantasy continues
that someone can create a "high-level design" or
"specification" that is (a) testable against the requirements,
(b) necessary for all further work and (c) sufficient to code,
test and transition to production. We can then throw this
specification over the transom into another room where a
"coder" will "cut code" that matches the specification. The
code production happens at a fixed, knowable rate with only
small random variation based on risk of illness. The testing,
similarly, can be meticulously scheduled and will happen
precisely as planned. Most "real-world" (management fantasy)
projects do not leave any time for rework after testing --
because rework won't happen. If it won't happen, why test?
Finally, there will be no technology transfer issues because
putting a freshly-written program into production is the same
as installing a game from a DVD.

Managers like to preface things with "In The Real World". As in
"In The Real World we need to know how long it will take you to
write this."

The "in the real world" speech always means "In My Management
Fantasy Land." The reason it's always a fantastic speech is
because software development involves the unknowable. I'm not
talking about some variable in a formula with a value that's
currently unknown. I'm talking about predicting the
*unknowable* future.

The Agile Response to Reality
-----------------------------

In the Real real world, software development is extraordinarily
hard.

Consider this: the computer clock runs in 100-nanosecond
increments (1.0E-7). We expect an application to run 24x7x0.999
= 6.04E5 seconds. That's from 100-nano to half-million: about
12 orders of magnitude to keep in one's head.

Consider this: storage in a largish application may span almost
a terabyte, (1.0E12). From bytes to terabytes: about 12 orders
of magnitude to keep in one's head.

Consider this: a web application written in a powerful
framework (Django) requires one to know the following languages
and frameworks. Shell script, Apache Config, Python, Django
Templates, SQL, HTML, CSS, Javascript, HTTP (the protocol is
it's own language), plus the terminology of the problem domain.
That's 9 distinct languages. We also have the OS, TCP/IP
Apache, mod_wsgi, Django, Python, browser and our application
as distinct frameworks. That's 8 distinct framework API's to
keep in one's head.

Consider this: the users can't easily articulate their problem.
The business analyst is trying to capture enough information to
characterize the problem. The users, the analyst, the project
manager (and others outside the team) all have recommendations
for a solution, polluting the problem description with
"solution speak" that's only adds confusion.

In the Management Fantasy "Real World", this is all knowable
and simple. In the Real Real World, this is rather hard.

Adapting to Reality
-------------------

Once we've recognized that software development is hard, we
have several responses.

#. **Deny**. Claim that software developers are either lazy or
stupid (or both). Give them pep-talks that begin "in the
real world" and hope that they cough up the required
estimates because they're motivated by being told that
software development "in the real world" isn't all that
hard.

#. **Processize**\ (tm). Claim that software development is a
process that can be specified to a level where even lazy,
stupid programmers can step through the process and create
consistent results.

#. **Adapt**. Adapting to the complexity of software
development requires asking, "what -- if anything --
expedites software development?"

What Do We Need to Succeed?
---------------------------

There are essentially two domains of knowledge required to
create software: the problem domain and the solution domain.

-   Problem Domain. This is the "business rules", the
    "scope", the "requirements", the "purpose", etc. We have
    the features and functions. What the software does. The
    value it creates. The "what", "who", "where", "when" and
    "why".

-   Solution Domain. This is the technology that makes it go.
    The time and space dimensions (all 12 orders of magnitude
    in each dimension), all the languages and all the
    frameworks. The "how".

The issue is this:

    **We don't start out with complete knowledge of problem and solution.**

At the start of the project -- when we're asked to
predict the future -- we can *never* know the whole
problem, nor can we *ever* know the whole solution we're
about to try and build.

What we need is this:

    **Put Problem Domain and Solution Domain knowledge into one person's head.**

The question then becomes "Who's head?"

We have two choices:

-   **Non-Programmers**. We can try to teach the various
    non-programmers all the solution domain stuff. We can
    make the project manager, business analyst, end-users,
    executive sponsor -- everyone -- into programmers so
    that they have problem domain and solution domain
    knowledge.

-   **Programmers**. We can try to impart the problem
    domain knowledge on the programmers. If we're
    seriously going to do this, we need to remove the
    space between programmer and problem.

That's the core of the Agile Response: Close the gap
between Problem Domain and Solution Domain by letting
programmers understand the problem.

The Bowl of Bananas Solution(tm)
--------------------------------

"But wait", managers like to say, "in the real world, we
can't just let you play around until you claim you're
done. We have to monitor your activity to make sure that
you're making 'progress' toward a 'solution'."

In the Real real world, you can't define the "problem",
much less test whether anything is -- or is not -- a
solution. I could hand most managers a bowl of bananas
and they would not be able to point to any test procedure
that would determine if the bowl of bananas solves or
fails to solve the user's problems.

Most project scope documents, requirements documents,
specifications, designs, etc., require extensive tacit
problem domain knowledge to interpret them. Given a bowl
of bananas, the best that we can do is say "we still have
the problem, so this isn't a solution." Our scope
statements and requirements and test procedures all make
so many assumptions about the problem and the solution
that we can't even figure out how evaluate an
out-of-the-box response -- like a bowl of bananas.

In the Real real world, management in organization A
demands that information be kept in a one database.
Management organization B has a separate database for
reasons mired in historical animosity and territorial
scent-marking. Management in yet another organization
wants them "unified" or "reconciled" and demands that
someone manually put the data into spreadsheets. This
morphs into requirements for a new application "system"
to unify this data, making the results look like
poorly-design spreadsheets. This morphs into a multi-year
project to create a "framework" for data integration that
maintains the poorly-designed spreadsheet as part of the
"solution".

A quick SQL script to move data from A to B (or B to A)
is the bowl-0f-bananas solution. It cannot be evaluated
(or even considered) because it isn't a framework, system
or application as specified in the scope document for the
data integration framework.

This is the problem domain knowledge issue. It's so hard
to define the problem, that we can't trust the executive
sponsor, the program office, the project managers, the
business analysts or anyone to characterize the problem
for the developers.

The problem domain knowledge is so important that we need
to allow programmers to interact with users so that
*both* the problem *and* the solution wind up in the
programmer's head.



-----

"variable in a formula" Warning Pontifi...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2009-10-22 20:05:22.782000-04:00

"variable in a formula"

Warning Pontification

The "real world" usually involves more than one equation with one
variable. However, ...

If you are lucky, your system is time invariant.

If you continue to be lucky, you will have n equations with n unknowns.

If you continue to be lucky, all your equations will be linear.

If you continue to be lucky the inverse matrix of your linear equations
won't be zero.

If you continue to be lucky, your numbers are well behaved and you don't
have to do partial pivoting during your inverse matrix operation.

If you continue to be lucky, just stop working and buy a lottery ticket.

In the "real world", our systems are often time variant and governed by
non-linear equations which may or may not be constrained. To get a quick
feel for how truly difficult these problems are, consider scheming
www.mpri.lsu.edu/textbook/Chapter6.htm.

Software developmnet is at least an order of magnitude harder because in
addition to dealing with the technology, you have to deal with business
constraints intermixed with the human condition.


Looking forward to hearing your thoughts of Lean P...
-----------------------------------------------------

Dean Goodmanson<noreply@blogger.com>

2009-10-22 17:55:55.585000-04:00

Looking forward to hearing your thoughts of Lean Principles applied to
Software Development.


Fantastic post Steven. I agree that as you put it,...
-----------------------------------------------------

Robert Dempsey<noreply@blogger.com>

2009-10-22 14:02:05.121000-04:00

Fantastic post Steven. I agree that as you put it, we need to, "close
the gap between Problem Domain and Solution Domain by letting
programmers understand the problem," and then helping them solve it. On
the other side of the equation, managers need to understand the
challenges involved in solving that problem. I've seen all sorts of
problems arrise due to massive communication issues, typically with
management not understanding what is going on, why things are taking so
long, etc. The onus is on the Team in this case to help management
understand their side of the problem, the issues involved in solving it,
and solutions they are working toward.

As you point out, the Agile Manifesto talks about individuals and
interactions over processes and tools. And to use a cliche,
communication is a two-way street.





