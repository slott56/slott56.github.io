Architecture Change: Recognizing Conway's Law
=============================================

:date: 2010-03-22 08:00
:tags: software process improvement,architecture,conway's law
:slug: 2010_03_22-architecture_change_recognizing_conways_law
:category: Technologies
:status: published

I've got lots of examples of places where Conway's Law has turned a
good idea into a poor implementation. A classic is a data warehouse
where there were three project managers, so they broke things up
three ways, leading to a crazy mess of dumb duplication.

Countering that, I've recently look at two gutsy declarations. It
takes real courage to declare an architecture wrong. Our basic human
nature prevents us from acknowledging that an existing architecture
is a liability, not an asset.

Pitching a fix is easy. Locating the root cause of the original
problem is hard. Trying to fix a broken architecture means that you
will run afoul of Conway's Law. In addition to having the guts to
acknowledge that something is broken, figuring a way to work with
Conway's Law is essential to success.

Broken 3-Tier Architecture
--------------------------

The biggest reason for broken architectures is dumb over-engineering.
And most of the dumbosity has Conway's Law as its root cause. Yes,
organizational structures will impose a solution structure that
doesn't match the problem. There are lots of examples.

If you read too much and build too little, you find a ton of articles
on .Net 3-Tier Architectures. Google and you'll get a mountain of
hits, each with a distinctive spin on 3-Tier. For reference, start
with this: `Building an N-Tier Application in
.NET <http://msdn.microsoft.com/en-us/library/ms973279.aspx>`__. It's
the party line on splitting things into tiny buckets consistent with
the MS product offerings.

A "3-Tier" presentation is very seductive because it plays by
Conway's Law.

-   **Manager A**. Lobbies for Web-based solution; takes over
    "presentation" development and builds a team to create flashy
    front-end stuff with cool tools and technologies: HTML, CSS,
    JavaScript, Silverlight, etc. The front-end developers are as much
    graphic designer as programmer; they have distinct skills.
    Conway's Law says that since they're separate from "other"
    programmers, presentation must be a separate tier.

-   **Manager B**. Manages the DBA's. DBA's must be kept separate
    because a database is "infrastructure", like a network and a web
    server. Somehow database development is usually lumped in with
    database administration and development competes with operation
    for resources. Conway's Law says that DBA's are separate so there
    must be a separate data tier.

-   **Manager C**. All of the interfaces and batch loads have to be
    done by someone. There's no sizzle to this; it isn't fun for
    DBA's. It's frankly boring stuff. Another manager is assigned to
    create "back-end" interfaces, and other stuff. Conway's Law says
    that we'll introduce a "middle tier" to give these people
    something to contribute to the web application.

At this point, some people call "shenanigans". They say that this
Conway's Law analysis is crazy talk: I'm just fitting the evidence
to my theory. Here's my question? What's the alternative to the
3-tier architecture? Are they claiming that the three tiers are
*logically* necessary?

Necessary Decomposition
-----------------------

If three tiers were logically necessary, we wouldn't discuss
N-tier architectures.

Clearly, folks have decomposed things into more than three tiers.
So, three tiers isn't *necessary*. It's just convenient. QED:
There's no necessity to three tiers; it's just a handy team size.

Some scalability works out well with a three-tier separation. In
particular, serving a lot of static content (CSS files, PNG's,
static HTML) can be delegated to a front-end tier. Serving the
dynamic content is better handled by a separate process (perhaps
even a separate processor). Database processing -- because it's
I/O bound, is often well-handled by a separate process.

However, if the "middle-tier" has a lot of work or relies on slow
external web services, it might decompose into sub-tiers. No more
three-tier solution. Similarly, one can make a case for splitting
static content services into two sub-tiers: reverse proxy and
proper content server. Again, no more three-tier solution.

Three tiers, five tiers or *N* tiers: the architecture could have
been driven by necessity or it could be driven by Conway's Law.
Clearly, Conway's Law has a profound influence. Indeed, most of
the time, Conway's Law trumps all other considerations.

Otherwise we wouldn't have broken architectures. If the decisions
were technical, we'd have technical spikes and we'd discard broken
ideas. Instead we pursue broken ideas in that weird deadline
driven project death-march.

Apostasy
--------

One consequence of Conway's Law is Stored Procedures. That's the
tier assigned to the DBA's. The idea that stored procedures might
be a bad idea strikes at the very heart of all DBA's (and their
managers) and is therefore unthinkable. Try suggesting that stored
procedures be replaced by middle-tier application logic. Everyone
says that replacing SP's with application code is heresy.

Less than two years ago I sat in a meeting where I was told, very
plainly, that the *only* provably scalable solution was a
`CICS <http://en.wikipedia.org/wiki/CICS>`__ transaction server
and a mainframe DB2 database. The entire room was told that web
architectures were a bad idea. Only CICS could be made to work.
This is just as dumb as claiming that stored procedures are
essential.

This kind of thing leads to a Conway's Law Hybrid solution (CLH™)
where the web front-end used SOAP web services to talk to a CICS
back-end that merely invoked DB2 stored procedures. No other
architecture was discussable. The architecture documentation had
to be rewritten to put the simple web site into an appendix as an
"alternative". The primary pitch was a hell-on-earth hybrid.

Since there was no DBA bandwidth to write all these stored
procedures, the project could only be cancelled. Business rules in
Java were unthinkable, heretical. As a former DBA, my suggestion
to give up on stored procedures makes me apostate. Stored
procedures can be driven by necessity or Conway's Law.

Conway's Law
------------

From http://www.code-muse.com/blog/?p=7

This concept is known as Conway’s Law, named after Mel Conway, who
published a paper called “How Do Committees Invent?”. Fred Brooks
cited Conway’s paper in his classic “The Mythical Man Month”, and
invented the name “Conway’s Law”. Here’s the definition from
Conway’s own website (which also has the original paper in full):

    Any organization that designs a system (defined more broadly here
    than just information systems) will inevitably produce a design
    whose structure is a copy of the organization’s communication
    structure.

http://en.wikipedia.org/wiki/Conway%27s_Law

More Broken Architectures
-------------------------

Another example.

-  **Manager A**. FLEX front-end development.

-  **Manager B**. Ontology development.

Wait, what? Ontology? No database?

Not at first. Clearly, a good ontology engine will handle the
information processing needs. It will be great. The FLEX front-end
can make SPARQL queries, right?

Actually, it doesn't work out well. SPARQL is slow. Hardly
appropriate for a rich user interface.

So here's another pass at this.

-   **Manager A**. FLEX front-end development.

-   **Manager B**. Ontology development.

-   **No One In Particular**. Backend Web Services Development between
    FLEX and the Ontology.

"Aha!" you say. "An example that proves Conway's Law is wrong."

Actually, this is evidence that Conway's Law can't be *patched*. The
initial ontology-based application is entirely Conway's Law in
action. Trying to create the necessary architectural features without
creating a proper organization around the solution ran aground.

Calling It Quits
----------------

A really hard thing to do is call it quits when something isn't
working. A fundamental law of human behavior says that we hold onto
losers. Partly, this is the `Endowment
Effect <http://en.wikipedia.org/wiki/Endowment_effect>`__ -- once the
architecture is in place, it *can* be salvaged. Partly, this is `Loss
Aversion <http://en.wikipedia.org/wiki/Loss_aversion>`__ -- declaring
the old architecture broken realizes that the investment created a
liability, not an asset.

How do you restart the project with a new architecture?

How do you avoid Conway's Law in the next generation of a web
application?

Stay Tuned for part 2 -- **Architecture Change: Breaking Conway's Law**.





