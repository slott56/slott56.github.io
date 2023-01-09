Legacy Code Preservation: How Do We Manage This?  
==================================================

:date: 2013-05-14 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_05_14-legacy_code_preservation_how_do_we_manage_this
:category: Technologies
:status: published

.. container:: section
   :name: how-do-we-manage-this

   At an insurance company, I encountered an application that had been
   in place for thirty years.

   Classic flat-file, mainframe COBOL. And decades old.
   It had never been replaced with a packaged solution. It had never
   been converted to a SQL database. It had never been rewritten in VB
   to run on a desktop.

   What had happened is that it had grown and morphed organically.
   Pieces the original application it had been subsumed by other
   applications. Additional functionality had been grafted on.

   After a few decades of staff turnover, no single person could
   summarize what the applications did. There was no executive overview.

   No pithy summary. No elevator pitch.

   The company had, further, spent money to have consultants "reverse
   engineer" the COBOL. This meant that the consultants created
   narrative English-language versions of the COBOL code.

   This reverse engineering replaced detailed, disorganized COBOL with
   detailed, disorganized English. No summaries were produced that could
   serve as an explanation of the actual valuable parts of the program.
   The question of scope and duration was daunting. The conversion would
   take years to complete. the central question become "How to manage
   the conversion?"

.. rubric:: The Goal
   :name: the-goal

The goal was to preserve the valuable features while migrating the
data out of flat files into a proper SQL database. The focus on
the data was important.

The technical obstacle was the hellish complexity of the
applications and their various shell scripts ("JCL" in the Z/OS
mainframe world.)

One approach to overcoming the complexity is to break the overall
collection of applications down into just those applications that
write to any of the central "master" files. Other applications
that read master files or do other processing are less important
than those which update the master files.

The master files themselves are easy to identify. The JCL that
references these files is easy to identify.

The programs run by those JCL scripts give us clusters of related
functionality.

We want to rank the master files by business value. The one with
the most valuable data is something we tackle first. The least
valuable data we leave for last.

In some cases, we'll identify programs that work with relatively
low-value data; programs which are not actually assets. They don't
encode any new, useful knowledge. A wise manager can elect to
remove them from the software inventory rather than convert them.

Since the conversion can't happen overnight, there needs to be a
period of coexistence between the first conversion and the last.
And this coexistence means that database tables will get extracted
back to flat files so that legacy programs can continue to
operate.

Another component of the plan for this conversion was the assembly
of test cases. This is critical when refactoring code.
The idea here is to preserve selected files and run them through
the application software to create repeatable test cases. One of
the existing file-compare utilities can be used to validate the
output.

.. rubric:: Other Barriers
   :name: other-barriers

The human obstacle was triumphant here. People who had worked with
this software for their entire career in IT would rather quit than
help with the conversion.

Experienced mainframe people could not see how a "little" Linux
processor could ever provide the amazing feature set and
performance of their beloved mainframe. They made the case that
CICS was higher performance and more scalable than any web-based
application platform.

And that lead to an impasse where one camp refused to consider any
migration except to COBOL and CICS. The other camp simply wanted
to write a web application and be done with it.

The COBOL/CICS group were either confused on in denial of how
quick and simple to can be to build default web applications
around stable data models. In this case, the relational database
version of the flat files would not be difficult to concoct. Once
built, 80% of the application programming would be default
add-change-delete transactions. The other 20% would be
transactions that included the remnants of useful knowledge
encoded in the legacy COBOL.

More time would be spent "studying the alternatives" than were
required to build working prototypes.

.. rubric:: Preservation
   :name: preservation

The real question is one of what needs to be preserved.
Clearly, the data is central to the business.

The larger question, then, is how much of the COBOL processing was
really essential processing?

How much of the COBOL was technical workaround to implement things
that are one-liners in SQL?

How much of the COBOL is workaround for other bugs in other
applications? How many programs fix broken interface files? How
many programs provide data quality inspections?

How much of the COBOL is actually unique? A substantial fraction
of the legacy code was irrelevant because a package replaced it.
Another substantial fraction implemented a "Customer Relationship
Management" (CRM) application for which a package might have been
a better choice than a software conversion.

How much of the legacy code contain quirks? How much code would we
would have to understand and consider repairing because it
actually contains a long-standing bug?

Perhaps the **only** thing of value was the data.

And perhaps the reason for the human obstacle was an realization
that the cost to convert exceeded the value being preserved. It's
difficult to have your life's work simply discarded.





