Mutability Analysis
===================

:date: 2009-12-09 07:29
:tags: OO design
:slug: 2009_12_09-mutability_analysis
:category: Technologies
:status: published

First, there are several tiers of mutability in requirements. These
tiers define typical levels of change context of the problem, the
problem itself and the forces that select a solution to the problem.

#.  **Natural Laws** (i.e., Gravity, Natural Selection). As well as
    metaphysical "laws" (i.e., reality). These don't change much.
    Sometimes we encapsulate this information with static final
    constants so we can use names to identify the constants. PI, E,
    seconds_per_minute, etc.

#.  **Legal Context** (both statutory law and case law), as well as
    standards and procedures with the effect of law (i.e. GAAP). Most
    software products are implicitly constrained, and the constraints
    are so fundamental as to be immutable. They aren't design
    constraints, per se, they are constraints on the context space for
    the basic description of the problem. Like air, these are hard to
    see, and their effects are usually noted indirectly.

#.  **Industry**. That is to say, industry practices and procedures
    which are prevalent, and required before we can be called a
    business in a particular industry. Practices and procedures that
    cannot be ignored without severe, business-limiting consequences.
    These are more flexible than laws, but as pervasive and almost as
    implicit. Some software will call out industry-specific features.
    Health-care packages, banking packages, etc., are explicitly
    tailored to an industry context.

#.  **Company**. Constraints imposed by the organization of the
    company itself. The structure of ownership, subsidiaries,
    stock-holders, directors, trustees, etc. Often, this is reflected
    in the accounting, HR and Finance systems. The chart of accounts
    is the backbone of these constraints. These constraints are often
    canonized in customized software to create unique value based on
    the company's organization, or in spite of it.

#.  **Line of Business**. Line of business changes stem from special
    considerations for subsets of vendors, customers, or products.
    Sometimes it is a combination of company organization and line of
    business considerations, making the relationship even more
    obscure. Often, these are identified as special cases in software.
    In many cases, the fact that these are special, abnormal cases is
    lost, and the "normal" case is hard to isolate from all the
    special cases. Since these are things change, they often become
    opaque mysteries.

#.  **Operational Bugs and Workarounds**. Some procedures or software
    are actually fixes for problems introduced in other software.
    These are the most ephemeral of constraints. The root cause is
    obscure, the need for the fix is hidden, the problem is enigmatic.

Of these, tiers 1 to 3 are modeled in the very nature of the problem,
context and solution. They aren't modeled explicitly as constraints
on problem X, or business rules that apply to problem X, they are
modeled as X itself. These things are so hard to change that they are
embodied in packaged applications from third parties that don't
create unique business value, but permit engaging in business to
begin with.

Layers 4 to 6, however, might involve software constraints,
explicitly packaged to make it clear. Mostly, these are procedural
steps required to either expose or conceal special cases. Once in a
while these become actual limitations on the domain of allowed data
values.

**Considerations.**

After considering changes to the problem in each of these tiers, we
can then consider changes to the solution. The mutation of the
implementation can be decomposed into procedural mutation and data
model mutation. The `Zachman Framework <http://www.zifa.com/>`__
gives us the hint that communication, people and motivation may also
change. Often these changes are manifested through procedural or data
changes.

Procedural mutation means programming changes. This implies that
flexible software is required to respond to business changes,
customer/vendor/product changes, and evolving workarounds for other
IT bugs. Packaged solutions aren't appropriate ways to implement
unique features of these lower tiers: the maintenance costs of
changing a packaged solution are astronomical. Internally developed
solutions that require extensive development, installation and
configuration aren't appropriate either.

As we move to the lower and less constrained tiers, scripted
solutions using tools like Python are most appropriate. These support
flexible adaptation of business processes.

**Data Model.**

Data lasts forever, therefore, the data model mutations fall into two
deeper categories: **structural** and **non-structural**.

When data values are keys (natural, primary, surrogate or foreign)
they generally must satisfy integrity constraints (they must exist,
or must not exist, or are mandatory or occur 0..\ *m* times). These
are structural. The data is uninterpretable, incomplete and broken
without them. When these change, it is a either a profound change to
the business or a long-standing bug in the data model. Either way the
fix is expensive. These have to be considered carefully and
understood fully.

When data values are non-key values, the constraints must be free to
evolve. The semantics of non-key data fields are rarely fixed by any
formalism. Changes to the semantics are rampant, and sometimes
imposed by the users without resorting to software change. In the
face of such change, the constraints must be chosen wisely.

  "Yes, it says its the number of days overdue, but it's really the
  deposit amount in pennies. They're both numbers, after all."

Mutability Analysis, then, seeks to characterize likely changes to
requirements (the problem) as well as the data and processing aspects
of the solution. With some care, this will direct the selection of
solutions.

**Focus.**

It's important to keep mutability analysis in focus. Some folks are
members of the **Hand-Wringers School of Design**, and consider every
mutation scenario as equally likely. This is usually silly and
unproductive, since their design work proceeds at a glacial pace
while they overconsider the effects of fundamental changes to
company, the industry, the legal context and the very nature of
reality itself.

Here's my favorite quote from a member of the **HWSoD**: "We don't
know what we don't know."

This was used to derail a conversation on security in a small web
application. Managers who don't know the technology very well are
panicked by statements like this. My response was that we actually do
know the relevant threat scenarios, just read the `OWASP
vulnerabilities <http://www.owasp.org/index.php/Main_Page>`__. Yes,
some new threat may show up. No, we don't need to derail work to
counter threats that do not yet exist.

**Progress.**

The trick with mutability analysis is to do the following.

1.  Time-box the work. Get something done. Make progress. A working
    design that is less than absolute perfection is better than no design
    at all. Hand-wringing over vanishingly unlikely futures is time
    wasted. Wasted. Create value as quickly as possible.

2.  Work up from the bottom. Consider the tiers most likely to change
    first. Workarounds are likely to change. Features of the line of
    business might change. Company changes only matter if you've been
    specifically told the company is buying or for sale. Beyond that,
    it's irrelevant for the most part. ("But my software will change the
    industry landscape." No it won't. But if it is really novel, then
    delivery soon matters more than flexibility. If the landscape
    changes, you'll have to fundamentally rewrite it anyway.)

3.  Name Names. Vague hand-waving mutation scenarios are useless. You
    must identify specific changes, and who will cause that change. Name
    the manager, customer, owner, stakeholder, executive, standard
    committee member, legislator or diety who will impose the change. If
    you can't name names, you don't really have a change scenario, you
    have hand-wringing. Stop worry. Get something to work.

**But What If I Do Something Wrong?**

What? Is it correct? Is it designed to make optimal use of resources?
Can you prove it's correct, or do you have unit tests to demonstrate
that it's likely to be correct? Can you prove it's optimal? Move on.
Maintainability and Adaptability are nice-to-have, not central.

Getting something to work comes first. When confronted with
alternative competing, correct, optimal designs, adaptability and
maintainability are a way to choose between them.





