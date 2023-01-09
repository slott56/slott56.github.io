COBOL Rework
============

:date: 2012-06-05 08:00
:tags: test-driven reverse engineering,data conversion,COBOL
:slug: 2012_06_05-cobol_rework
:category: Technologies
:status: published

See this article: "`The COBOL Brain
Drain <http://www.computerworld.com/s/article/9227263/The_Cobol_Brain_Drain?taxonomyId=154>`__"
in ComputerWorld.  This article is very, very well written and repeats
a number of common fallacies.

The fallacies lead to expensive, labor-intensive in-house software
development and maintenance.  Either there's a lot of effort poking at
the COBOL code.  Or there's a lot of extra code to "wrap" the COBOL
code so that it's never touched.

"Migrating large-scale systems built in Cobol is costly and risky."  A
popular position.  But the risks are actually quite small; possibly
non-existent.  The risks of not converting are usually higher than the
risk of conversion.

The perception of the COBOL code is that it's filled with decades of
tricky, nuanced legacy details that are hard to fully understand.
This is only partially true.

A great deal of the tricky code is simply redundant.  COBOL is often
written with copy-and-paste programming and blocks of code are simply
repeated.  It's also important to note that some of the code is no
longer exercised in the first place.

**Mythical Risk**

The "risk" comes from the perceived opacity of  the tricky, nuanced
legacy details.  It doesn't appear to be clear what they mean.  How
can a project be started when the requirements aren't fully
understood?

What appears to be the case in reality is is that this tricky code
isn't very interesting.  Most COBOL programs don't do much.  They can
often be summarized in a few sentences and bullet points.

Detailed analysis (641,000 lines of code, 933 programs) reveals that
COBOL programs often contain several commingled feature sets.

-   The actual business rules.  These are often easy to find in the code
    and can also be articulated by key users.  The real work is usually
    quite simple.

-   A bunch of hackarounds.  These are hacks to work around bugs that
    occur elsewhere in the processing.  Sometimes a hackaround introduces
    additional problems which require yet more hackarounds.  All of this
    can be ignored.

-   Solutions to COBOL data representation issues.  Most of these seem to
    be "subtype" issues: a flag or indicator is introduced to distinguish
    between subtypes.  Often, these are extensions.  A field that has a
    defined range of values ("A", "C" or "D") has a few instances of "*"
    to indicated another subclass that was introduced with a non-standard
    code for peculiar historical reasons.


Once we separate the real code from the hackarounds and the
representation issues, we find that most COBOL programs are trivial.
About 46% of the lines of code (74% of the distinct programs)
involves programs that read one to four files to write a report.  In
effect, these programs do a simple "relational join" or query.  These
programs have single-sentence summaries.


The hackaround problem is profound.  When looking at COBOL code,
there may be endless copy-and-paste IF-statements to handle some
issue.  There may be whole suites of programs designed to work around
some issue with a third-party package.  There may be suites of
programs to deal with odd product offerings or special customer
relationships.


The remaining 26% of the non-trivial programs follow a normal
distribution of 1/4 simple, 1/2 moderately complex, and 1/4
regrettably and stupidly complex.  That final 5% of the programs will
also be a whopping 20% of the lines of code.  They are the few big
programs that really matter.


**Risk Mitigation**


The risk mitigation strategy involves several parts.


#.  Data Profiling.  The COBOL data may have considerable value.  The
    processing is what we're trying to rewrite into a modern language.
    A profile of every field of every file will reveal that (a) most
    of the data is usable and (b) the unusable portion of the data
    isn't very valuable.

#.  Triage.  We can summarize 80% of the code in simple sentences.
    46% of the code is single-sentence summaries.  34% of the code
    has multiple sentence summaries.  The remaining 20% requires
    in-depth analysis because the programs are large; they average of
    2400 lines of code each.

#.  Test-Driven Reverse Engineering.  Since a 5% of the programs do
    the real updates, it's important to collect the inputs and outputs
    of these few programs.  This forms a core test suite.

#.  Agile Methods.  Find the user stories which really matter.  Find
    the COBOL programs that implement those user stories.


The most important risk reduction strategy is to take an Agile
approach.  We need to prioritize based on value creation.  All
COBOL programs are not created equal.  Some fraction can simply be
ignored.  Another fraction produces relatively low value, and can
be converted last.


The second most important risk mitigation is to build conversions
from legacy COBOL files to the new, preferred databases.  The data
is preserved.


There's almost no risk in rewriting the 46% of low-complexity
COBOL lines of code.  This code is trivial.  Note that some of
this code actually has no business value.  Simply ignoring the
no-value code also reduces risk.  Since we're using live files to
drive testing, we can easily prove that our new programs work.


It's not risky to focus on the 20% of high-value COBOL lines of code.
This contains most (or all) of the processing that the business
needs to have preserved.  They can articulate the user stories; it's
easy to confirm that the COBOL does what the business needs.  It's
easy to use live data to drive the reverse engineering.


The remaining 34% of the code base may actually involve a small
amount of overlooked complexity.  There may be a nuance here that
really matters.


This overlooked "nuance" is something that the users didn't
articulate, but it showed up in our unit testing.  We couldn't
reproduce an expected output because we didn't correctly locate all
the processing steps.  It wasn't in our summary of the 80% of
moderate-to-low complexity programs.  It wasn't in our detailed
analysis of the 20% subset of hyper-complex, large programs.


We've reduced the risk by reducing the volume of code that needs to
be examined under the microscope. We've reduced the risk by using
live files for parallel testing.  We've reduced the risk by
collecting user stories.


The remaining risks are ordinary project risks, unrelated to COBOL or
legacy data.


**The Other Great Lie**


Another popular fallacy is this:


| "The business wants us to make investments in programming that buys
| them new revenue. Rewriting an application doesn't buy them any
| value-add".

The value-add is to create a nimble business.  Purging the COBOL has a
lot of advantages.

-   It reduces the total number of lines of code.  Reducing costs.
    Improving time-to-market for an IT solution to a business problem.

-   It reduces the number of technologies competing for mind-share.  Less
    thinking about the legacy applications is less time wasted solving
    problems.

-   It reduces the architectural complexity.  If the architecture is a
    spaghetti-bowl of interconnections between Web and Legacy COBOL and
    Desktop, then following the spaghetti-like connections is simply a
    kind of intellectual friction.


The COBOL does not need to be purged all at once through a magical
"big-bang" replacement.  It needs to be phased out.


Agile techniques need to be applied.  A simple backlog of high-value
COBOL-based user stories is the place to start.  The prioritization
of these stories needs to then be clustered around the data files.


Ideally all of the programs which create or update a given file (or
related group of files) can be rewritten in a tidy package.  The old
files can be used for Test-Driven Reverse Engineering.  Once the
programs have been rewritten, the remaining COBOL legacy applications
can continue to operate, using a file created by a non-COBOL
application.


Each file (and related cluster of programs) is replaced from
high-value down to low-value.  Each step creates a more nimble
organization.





