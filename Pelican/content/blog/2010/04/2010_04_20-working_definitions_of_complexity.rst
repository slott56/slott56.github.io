Working Definitions of Complexity
=================================

:date: 2010-04-20 08:00
:tags: complexity,software process improvement
:slug: 2010_04_20-working_definitions_of_complexity
:category: Technologies
:status: published

Software developers get so used to their Culture of Complexity, they
hardly notice it.

See `Asshole-Driven Development <http://www.scottberkun.com/blog/2007/asshole-driven-development>`__
for more thoughts on this. The comments add lots and lots of examples
of dysfunctional development. Many of these are additional examples
of complexity run amok.

My personal addition is Next Year's Dollars are Cheaper (NYDC): next
year's dollars are less valuable than this year's dollars. So
technical debt can be accrued without any long-term consequences.
Dumb, bad design can be forced into production because maintenance is
cheaper than getting something done by a fantasy-based deadline date.
Never mind the fact that maintenance goes on -- effectively --
forever, and technical debt accrues real cost at an exponential rate.
Complexity is free? Apparently so.

Recently I heard of the "DIMY" development. DIMY is Do It My Way. The
specific war story was a PL/SQL stored procedure that was somehow
"too complex" because all it did was call 7 other stored procedures.
The business process had 7 steps; the parallelism between procedure
and use case was an important part of the design. Yet, since some
folks would prefer a Monolithic Stored Procedure (MSP), they saw fit
to complain.

Asserting that a MSP is "less complex" is a mirror image our normal
understanding of complexity creating cost. It's a mirror-image
because the debits and credits are reversed. In the DIMY world,
measurable complexity is valued as an asset and real simplicity is
viewed as a cost.

**Working Definitions**

Based in the war story, we can identify several aspects of this
working definition of complexity.

First, it appears that a monolithic piece of software (no matter how
poorly it matches the use case) is "less complex" than a relatively
simple piece of software that better matches the use case. So
software that actually matches the use case is "complex".

It also appears that a simple count of stored procedure names is a
measure of complexity. So any effort at doing any meaningful,
"high-level"
`chunking <http://en.wikipedia.org/wiki/Chunking_(psychology)>`__ of
meaning is accused of creating complexity. So chunking is "complex".

    [I am forced to agree that "more names" is a larger number; I can't
    agree that more names is more complex, because I find that chunking
    works. Note that refusing to engage in mental chunking is absurd.
    Claiming that multiple named stored procedures "obscures the details"
    is silly. Why stop at named procedures? Why not claim that PL/SQL --
    by it's very nature -- obscures the details? Why not claim that an
    RDBMS obscures the details? Why not claim that the OS API's obscure
    details? Why not claim that compiled languages obscure the details?
    Chunking is essential.]

Finally, it appears that real measure of complexity, like `Cyclomatic
Complexity <http://en.wikipedia.org/wiki/Cyclomatic_complexity>`__
are irrelevant. So a monolith, with lots of loops and ifs is somehow
less "complex" and more desirable.

**Perfect Code**

Clearly, then, for some folks, high quality code involves (1) no
match against the use case, (2) a single name, and (3) no limit on
the loops and if-statements. In order to achieve this, we need a very
simple use case (real simplicity -- low cyclomatic complexity -- a
sequence of decision-free steps) for which we can write an immense,
possibly irrelevant pile of code.

What's wrong with the MSP?

Given a monolithic piece of code that doesn't match the use case
sequence of steps, how could we construct unit tests? I don't see
how. Since we can't decompose the problem into meaningful chunks, we
can't test the thing in pieces. All we can do is write overall
end-to-end functional tests. And hope.

Given this MSP, how would we debug problems? I don't see how. We'd be
confronted with "it's broken" almost every time something went wrong.
Pin-pointing the root cause seems like it would be impossible.

DIMY development -- and the associated complexity -- does mean one
thing. It means job security: no one will ever be able to
understand, maintain or adapt this software. Write once, maintain
forever. If you're patient, you have a job for life. At some
point, managers will realize it's too expensive to maintain and --
because you're the only expert -- you can rewrite it, continuing
the cycle of complexity.





