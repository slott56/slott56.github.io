Legacy Code Preservation: What's the Cost?
==========================================

:date: 2013-04-25 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_04_25-legacy_code_preservation_whats_the_cost
:category: Technologies
:status: published

.. container:: section
   :name: what-s-the-cost

   It's 1980-something. We're working on a fairly complex system that
   includes some big machines and three computers. One of the computers
   has a magnetic tape drive into which it writes a log of interesting
   events. In the 80's, this was a pretty big deal.

   An operational run will produce a log; then we can use customized
   applications to analyze and reduce the log to something more useful
   and focused. The first step is to do some data extraction to get the
   relevant log entries off the tape and into a disk file that engineers
   can work with.

   Recall that the spreadsheet has only been around for a few weeks at
   this point in the history of computing. Sums and counts require
   programs. In this case, they are written in Fortran.

   So far, so good. My job is to add yet another feature to the data
   extraction program. It will pull some new different bits of data off
   the logs.

   The log entries are, of course, fairly complex. This is not different
   from log scraping in a web server context. Some log entries have to
   be ignored, others have to be merged. Some have cryptic formats.

.. rubric:: The Code Base
   :name: the-code-base

The extraction application has been in use (and heavily modified)
for a couple of years. Many programmers have touched it. Many.
The data extractor is written in a language called
`JOVIAL <http://en.wikipedia.org/wiki/JOVIAL>`__. This is not a
problem. It's the language of the large system being built. The
engineers are happy to use Fortran for their off-line analysis of
the files.

There's a subtlety that arises in this mixed language environment.
Any engineer with Fortran skills can whip together an analysis
program. But only the favored few programmers know enough JOVIAL
to tweak the data extraction program. And they're all busy writing
the real software, not supporting analysis and trouble-shooting.

This data extractor program suffers from a lot of "copy-and-paste"
programming. Blocks of code are repeated with minor changes.

Standard modules are repeated with differences from the official
copy that the entire rest of the system uses. Block comments don't
nest, so it's hard to remove a large chunk of code which contains
a block comment.

Further, it suffers from "**Don't Delete Diddly**" programming.

Large swaths of code are left in place, relegated to a subroutine
that never gets used. Other blocks of code are circumvented with a
GOTO statement to simply jump over the code.

And, it has a complex history and provenance. In order to debug
anything on the complex target system, the logger had to be the
first thing up and running. Therefore, the logger specifically
predates all other features of the application. It doesn't involve
any rational reuse of any other piece of software.

This is the 80's, so version control and forking a new version
were simply not done.

My job was to make a minor revision and extract just one certain
type of log entry. Effectively a "filter" applied to the log.
After several days of reading this mess, I voted with my feet. I
wrote a brand-new, from-scratch, "de novo" program (in Fortran,
not JOVIAL) which reads the tape and produces the required log
entries.

Why?

It was cheaper than messing with the legacy code base. Less work.
Less risk of breaking something. And less long-term cost from
continuing to maintain the data extractor.

.. rubric:: Grief and Consternation
   :name: grief-and-consternation

Discarding the legacy JOVIAL analysis program was a kind of
heresy. It was a Bad Thing To Do. It "Raised Questions".
Raised Questions? Really? About what?

Did it raise questions about the sanity of managers who preserved
this beast? Or about the sanity of programmers doing
copy-and-paste programming?

I had to endure a lengthy lecture on the history of the data
extraction program. As if the history somehow made a bad program
better.

I had to endure begging. The legacy program should be preserved
precisely because it was a legacy. Really. It should be
"grandfathered in" somehow. Whatever that means.

.. rubric:: Preservation
  :name: preservation

The original Jovial data extractor program still existed. It still
ran. It could still be used. The JOVIAL code base and tools (and
skilled programmers) remained available.

No one had **deleted** anything. There was no actual problem.
We had just started to realize that it was time to move on.

I started with a clean, simple Fortran program that read the logs,
extracted records, and created files that engineers could work
with.

But, but doing that, I guess that I had called somebody's baby
ugly.

This new Fortran program preserved the **essential** knowledge
from the original JOVIAL program. Indeed, I think that one of the
reasons for all the grief was that I had exposed relevant details
of the implementation, stripped clean of the historical cruft.

The tape file format and the detailed information on the log file
records had gone from closed and embedded in just one program to
open and available to more than one program.

The Fortran program exposed the log file details so that anyone
could write a short (and more widely readable) Fortran program.
This allowed them to avoid the cost and complexity of waiting for
someone like me to modify the JOVIAL extraction program.

The file format is merely a technical detail. It's the analyses
that were of real value. And none of that was in the original
JOVIAL program. They remained as separate Fortran programs.





