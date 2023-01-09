Legacy Code Preservation: Are There Quirks?
===========================================

:date: 2013-04-23 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_04_23-legacy_code_preservation_are_there_quirks
:category: Technologies
:status: published

.. container:: section
   :name: are-there-quirks

   Let's visit some other conversion activities in the 1970's. The gig
   was at a company implementing a customized insurance application. The
   actuaries used a `PDP-10 <http://en.wikipedia.org/wiki/PDP-10>`__
   (and Fortran) to compute their various tables and summaries.

   I was roped into rewriting an actuarial Fortran programs into
   `PL/1 <http://en.wikipedia.org/wiki/PL/I>`__ for an `IBM
   370 <http://en.wikipedia.org/wiki/IBM_System/370>`__.

   This program, clearly, encodes deep business knowledge. It must be
   preserved very precisely, since the actuarial calculations are
   directly tied to the financial expectations for the particular line
   of business.

   The good news about Fortran to PL/1 conversion is that PL/1 offers
   features (and syntax) that are similar to Fortran. It's not an exact
   match, but it's close enough to make the conversion relatively
   risk-free.

   There are, of course, issues.

   In particular, Fortran IV was not big on the "structured
   if-then-else" features of Algol-like languages. PL/1, like Pascal,
   followed on the heels of Algol 60. Fortran didn't follow Algol;
   Fortran depended on GOTO statements instead of nested IF-THEN-ELSE
   statements.

   This meant that some logic expressions were rather tangled and
   difficult to fully understand. Patience and and care were required to
   unwind the logic from it's tangled nest of Fortran GOTO's into neater
   PL/1 BEGIN-END blocks.

.. rubric:: Test Case
   :name: test-case

Perhaps the most important gap here was the lack of any kind of
definitive test case.

It was the 70's. Testing was---at best---primitive. The languages
and tools didn't support very much in the way of automated
testing.

Compounding the problem, IT management was so late in getting the
project started that we had to do repeated overnighters to get
things running. The fog of sleep deprivation doesn't facilitate
high quality software.

Further compounding the problem, we don't really have access to
the PDP-10 that the actuaries use. We can't run any controlled
tests.

And. Bonus.

We were doing "test-in-production". As soon as it worked, that was
the official production run. Everything prior to the one that
worked was discard as a test run.

The test strategy was simply to do a side-by-side comparison with
the legacy PDP-10 output. While it's tedious to read hundreds of
pages of mainframe computer print-out, that was the job.

.. rubric:: Results
   :name: results

For the first attempts, there were significant logic issues.
Regions of IF-GOTO that hadn't been properly rewritten into
IF-THEN-ELSE.

At some point, the output would disagree. The PDP-10 Fortran, of
course, was deemed to be "right."

So it was a matter of discovering what was unique about the case
where there was a difference. Lots of deduction and puzzle
solving.

Finally, we got down to one really subtle issue.

The numbers were slightly different. Slightly.

What does this slight discrepancy mean?

Is it a bug? Do we have to chase down some math error? It's
unlikely to be a math error, since the expressions convert
trivially from Fortran to PL/1. And the numbers are close.

Is it a feature? Is there something in Fortran or PL/1 that we
simply failed to understand? Unlikely.

Everything else works.

It's a "quirk". It's not a "bug" because it's not clearly wrong.
It's not a feature, because we're not going to define it as being
clearly right. It's in this middle realm of behavior best
described as quirky.

.. rubric:: Quirks
   :name: quirks

What we've uncovered, it turns out, is the difference between
Fortran floating point calculations and PL/1's fixed-point decimal
calculations. PL/1's compiler reasons out the proper number of
decimal places in the intermediate results and generates
fixed-point decimal code appropriately.

Decimal hardware, BTW, was part of the `IBM
370 <http://en.wikipedia.org/wiki/IBM_System/370>`__ system.
Decimal-mode arithmetic was often faster then floating-point.
The PL/1 rules have some odd features regarding division and
multiplication. A*0.001 and A/1000 have different deduced number
of decimal places. Other than that, the rules are obvious and
mathematically sound.

The PL/1 version provides exact decimal answers. Lots of decimal
places exact.

The Fortran version involved approximations. All floating-point
calculation must be looked at as an approximation. Many numbers
have an exact binary representation. But numbers without an exact
binary representation will have tiny errors. The tiny errors are
magnified through calculations. Generally, subtracting two
nearly-equal floating-point values elevates the erroneous parts of
the approximation to lofty heights of visibility.

.. rubric:: Preservation
   :name: preservation

It was important to preserve the essential actuarial knowledge
encoded in Fortran into PL/1.

It was not as important to preserve the quirks of single-precision
floating-point math.

Clearly, we have to distinguish between three separate
considerations.

#. Valuable Features: encoded business knowledge.
#. Implementation Details: technology knowledge.
#. Quirks. Aspects of the implementation that lead to low-value discrepancies in the output.





