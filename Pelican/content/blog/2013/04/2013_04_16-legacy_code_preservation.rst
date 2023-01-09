Legacy Code Preservation  
==========================

:date: 2013-04-16 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_04_16-legacy_code_preservation
:category: Technologies
:status: published


**Rule One: Writing Software is Capturing Knowledge.**

**Consequence: Converting Software is Preserving Knowledge.**

When software is revised for a new framework or operating system or
database or when an algorithm is converted to a new language, then
we're "converting" (or "migrating") software. We're preserving code,
and preserving the knowledge encoded.

For the next few months, I'm going to post some examples of preserving
legacy code and how this ties to the knowledge capture issue.


Once we've looked at some examples of business software, we can turn
to something a little less concrete:
`HamCalc <http://www.cq-amateur-radio.com/cq_ham_calc/cq_ham_calc.html>`__.

These examples are presented in historical order. Each example raises
questions and outlines elements of a strategy for legacy code
preservation.

-  **What's the Story?** Late 1970's. What user story was encoded in the software?

-  **Are There Quirks?** Late 1970's. Is the encoded knowledge really a
   useful feature? Or is it a bug? What if we can't be sure?

-  **What's the Cost?** Early 1980's. What if the legacy code is complex
   and expensive? How can we be sure it doesn't encode some valuable
   knowledge?

-  **Paving the Cowpaths.** Throughout the 80's. When converting from
   flat-file to database, how can we distinguish between encoded user
   stories and encoded technical details? Isn't all code equally
   valuable? There are several examples; I've combined them into one.

-  **Data Warehouse and Legacy Operations.** This is a digression on how
   data warehouse implementation tends to preserve a great deal of
   legacy functionality. Some of that legacy functionality exists in
   stored procedures, a programming nightmare.

-  **The Bugs are the Features**. Can you do software preservation when
   user doesn't seem to understand their own use cases?

-  **Why Preserve An Abomination?** How do we preserve shabby code? How
   can we separating the user stories from the quirks and bugs? There
   are several instances, I've used one as an example.

-  **How Do We Manage This?** The legacy code base was so old that no
   one could summarize it. It had devolved to a morass of details. With
   no intellectual handles, how can we talk about the process of
   converting and what needs to be preserved?

-  **Why Preserve the DSL?** describes a modern instance of "Test-Driven
   Reverse Engineering" where the unit test cases were created from the
   user stories and the legacy code use merely as supporting details. An
   entirely new application was written which preserved very little of
   the legacy code, but met all the user's requirements.

These nine examples include some duplicates. It's really more like a
dozen individual case studies. Some are simple duplicates; the name of
the customer is changed, but little else.



-----

Check out the internet archive and their preservat...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2013-04-18 05:29:44.870000-04:00

Check out the internet archive and their preservation of software. A
good place to start is
http://ascii.textfiles.com/archives/3947





