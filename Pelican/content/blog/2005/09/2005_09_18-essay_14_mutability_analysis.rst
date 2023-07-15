Essay 14 - Mutability Analysis
==============================

:date: 2005-09-18 16:24
:tags: architecture,software design
:slug: 2005_09_18-essay_14_mutability_analysis
:category: Architecture & Design
:status: published





First, there are several tiers of mutability in
requirements in general.  These tiers define typical levels of change context,
problem and forces that select a solution.

1.  **Natural Laws**  (i.e., Gravity). As well as metaphysical
    "laws" (i.e., reality). These don't change much. Sometimes we encapsulate this
    information with static final constants so we can use names to identify the
    constants.  Pi, e, seconds_per_minute, etc.

#.  **Legal Context**  (both statutory law and case law), as
    well as standards and procedures with the effect of law (i.e. GAAP). Most
    software products are implicitly constrained, and the constraints are so
    fundamental as to be immutable. They aren't design constraints, per se, they are
    constraints on the context space for the basic description of the problem. Like
    air, these are hard to see, and their effects are usually noted
    indirectly.

#.  **Industry** . That is to say, industry practices
    and procedures which are prevelant, and required to be called a business in a
    particular industry. Practices and procedures that cannot be ignored without
    severe, business-limiting consequences. These are more flexible than laws, but
    as pervasive and almost as implicit. Some software will call out
    industry-specific features. Health-care packages, banking packages, etc., are
    explicitly tailored to an industry context.

#.  **Company** . Constraints imposed by the
    organization of the company itself. The structure of ownership, subsidiaries,
    stock-holders, directors, trustees, etc. Often, this is reflected in the
    accounting, HR and Finance systems. The chart of accounts is the backbone of
    these constraints. These constraints are often canonized in customized software
    to create unique value based on the company's organization, or in spite of
    it.

#.  **Line of Business** .  Line of business changes stem from
    special considerations for subsets of vendors, customers, or products. 
    Sometimes it is a combination of company organization and line of business
    considerations, making the relationship even more obscure.  Often, these are
    identified as special cases in software.  In many cases, the fact that these are
    special, abnormal cases is lost, and the "normal" case is hard to isolate from
    all the special cases. Since these are things change, they often become opaque
    mysteries.

#.  **Operational Bugs and Workarounds** . Some procedures or software are
    actually fixes for problems introduced in other software. These are the most
    ephemeral of constraints. The root cause is obscure, the need for the fix is
    hidden, the problem is enigmatic.



Of these, tiers 1 to 3 are modeled in the very nature of the problem, context and
solution. They aren't modeled explicitly as constraints on X, or business rules
that apply to X, they are modeled as X itself.  These things are so hard to
change that they are embodied in packaged applications, from third parties, that
don't create unique business value, but permit engaging in business to begin
with.



Layers 4 to 6, however, might
involve software constraints, explicitly packaged to make it clear. Mostly,
these are procedural steps required to either expose or conceal special cases.
Once in a while these become actual limitations on the domain of allowed data
values.



After considering changes to
the problem, we also have to consider changes to the solution.  The mutation of
the implementation can be decomposed into procedural mutation and data model
mutation.  The `Zachman
Framework <http://www.zifa.com>`_   gives us the hint the communication, people and motivation
may also change.  Often these changes are manifested through procedural or data
changes.



Procedural mutation means
programming changes.  This implies that flexible software is required to respond
to business changes, customer/vendor/product changes, and evolving workarounds
for other IT bugs.  Packaged solutions aren't appropriate, the maintenance costs
are astronomical.  Internally developed solutions that require extensive
development, installation and configuration aren't appropriate either.  Scripted
solutions using tools like Python and Perl are most appropriate to support
flexible adaptation of business
processes.



Data model mutations fall
into two deeper categories: structural and
non-structural.



When data values are
keys (natural, primary, surrogate or foreign) they generally must satisfy
integrity constraints (they must exist, or must not exist, or are mandatory or
occur 0..m times). These are structural. The data is uninterpretable, incomplete
and broken without them.  When these change, it is a either a profound change to
the business or a long-standing bug in the data model.  Either way the fix is
expensive.  These have to be considered carefully and understood
fully.



When data values are non-key
values, the constraints must be free to evolve. The semantics of non-key data
fields are rarely fixed by any formalism. Changes to the semantics are rampant,
and sometimes imposed by the users without resorting to software change. In the
face of such change, the constraints must be chosen wisely.

"Yes, it says its the number of days
overdue, but it's really the deposit amount in pennies. They're both numbers,
after all."



Mutability Analysis, then,
seeks to characterize expected changes to requirements (the problem) as weel as
the data and processing aspects of the solution.  With some care, this will
direct the selection of solutions.















