Legacy Code Preservation: Why Preserve An Abomination?  
========================================================

:date: 2013-05-09 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_05_09-legacy_code_preservation_why_preserve_an_abomination
:category: Technologies
:status: published

.. container:: section
   :name: why-preserve-an-abomination

   By the early aughts (2001-2005) Visual Basic had gone from state of
   the art to a legacy application language. Code written in VB was
   being replaced with something more modern (generally Java.)

   Having worked with COBOL and Fortran legacy programs, it's easy to
   describe this legacy VB code as an abomination. Several customers.
   Several applications. Not a simple size of one. Abomination.

   The VB programming I've been involved in preserving has been
   uniformly shabby. It seems reflect an IT department that threw warm
   bodies at a problem until it appeared solved and did nothing more. No
   code reviews. No cleanup. Just random acts of maintenance.

   I'm sure there's are many good VB programmers. But I haven't seen
   their work product yet.

   And now, a customer is paying consultants like me to clean up their
   shabby VB and replace it with Java. Or a web site. Or both.

.. rubric:: A Code Base
   :name: a-code-base

One particular example of abominable VB was a hodgepodge of
copy-and-paste programming, GOTO's and other poorly-used features.
The application printed insurance-like summaries of benefits. In
order to do this, it extracted a great deal of data from a
database. It relied on a collection of stored procedures and an
intimate connection with a massive "calculation" module that
derived the actual benefits, which the VB application summarized
and reported.

The new application architecture was designed to separate the
database from the calculations. The printing of letters to
summarize benefits would be yet another separate part of a web
site.

Instead of being done on one specific model of dot-matrix printer,
the letter would be generated as a PDF that could be displayed or
downloaded or printed. Pretty conventional stuff by modern
standards. A huge revision considering the legacy programming.
The intimate connections between the database, the calculation
module and the letter-writing module would have to be narrowed
considerably. A formal list of specific pieces of information
would have to replace the no-holds-barred access in the VB modules
and database.

.. rubric:: Preservation
   :name: preservation

Essentially, the VB code that produced the letters encoded some
business knowledge.

Much of knowledge was encoded in the calculation module, also.
This needed to be refactored so that the business knowledge was
focused on the calculation module.

The letter writing had to be stripped down to something that
worked like this.

#. Query some initial stuff from the database.

#. Determine which letter template to use.

#. Query the rest of the stuff from the database based on the specific situation and template letter.

#. Fill in the blanks in the template. Generate the PDF.

The legacy VB code, of course, had to be studied carefully to
locate all of the business process and all of the data sources.
And all of the quirks had to be explained. In this case, there are
unfixed bugs that had to be preserved in order to say the new
output matched the old output. In a few cases, we had to report
that the old application was clearly wrong and actually fix the
bugs. Interestingly, there was no arguing about this. The bugs we
found were all pretty well-known bugs.

An "Interface" module was defined. All of the processing from the
VB letter-writing programs was pushed into the interface. The
letter-writing was refactored down to template fill-ins.

The interface became the subject of some architectural debate. It
was the essential encoded knowledge from the original VB programs.
Is it part of letter-writing? Or is it really part of the core
calculation module?

Eventually, it was pushed into the calculation module and the
"interface" could be removed, leaving a very clean interface
between letter-writing and calculation.

I suspect (but I don't know) that the Java calculation module was
quite the mishmash of stuff extracted from numerous VB programs.
Hopefully, those programmers had proper unit test cases and could
refactor the calculation module to get it into some sensible,
maintainable form.





