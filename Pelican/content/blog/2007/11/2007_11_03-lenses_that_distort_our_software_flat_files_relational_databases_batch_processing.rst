Lenses that Distort our Software: Flat Files, Relational Databases, Batch Processing
====================================================================================

:date: 2007-11-03 12:49
:tags: architecture,design,unit testing,tdre
:slug: 2007_11_03-lenses_that_distort_our_software_flat_files_relational_databases_batch_processing
:category: Architecture & Design
:status: published







When approaching reverse-engineering, we have to partition the big puddle of code into some useful pieces that we can manage intellectually, and will likely become parts of the resulting application.  In some cases, this is either impossible or valueless.  It may be that the application is so hopelessly bad that we can't partition it.  Often, the batch processing lens distorts the business processes.  In order to  understand the legacy processing, we need to account for this lens.



More commonly, the data model is so out of date from current business practice, that there's little real value in attempting to preserve it.  We need to find the underlying model first, and then determine how the program imposes the application processing on this model.  To develop a model from the legacy code, we have to `Find the Objects <{filename}/blog/2007/09/2007_09_21-deconstructing_programs_from_c_or_finding_the_objectstm.rst>`_ .  In some cases, the actual objects are so distorted by the implementation lens that this can be challenging.



When dealing with legacy batch programs, there are a number of typical design patterns.  If we understand these design patterns, we can also see how they distort the data model as well as the processing.



The Relational Lens
-------------------



The simplest data model, when viewed through the relational lens, is distorted in terrible ways.  I've had DBA's try to tell me that data manipulation (Create, Retrieve, Update and Delete) does not have any underlying business "meaning".  They're just operations on data.  The "meaning" is that there are transactions and persistence.



What we often find is that the structure imposed by relational tables has distorted the underlying business entity.  In particular, a relational databases don't have proper containers, so collective structures are often flattened out through a join operation, making the resulting objects appear to be peer-like.  In fact, some attributes of the result rows belong to the container and other attributes define a child contained within a parent.



A certain amount of processing follows a "group-by" (also known as a "Control Break") design pattern to reconstruct the original parent-child relationships.



The Flat File Lens
------------------



The flat file data model is not as obsolete as one would hope.  Much data is taken out of a reasonable structure, transformed into a series of rows, and reconstructed by another application.  Even a translation to XML can lose some of the relationships in the original structure.  Yes, ID= and IDREF= attributes can preserve all of the original object structure, but these are not always used well.



In the rare case of truly ancient software (e.g., IBM Z/OS VSAM files or similar structures) we often have files with the following icky properties.



Variant Record Types (i.e., not in first normal form).  COBOL folks call this a "redefined" record because some part of the record definition has a "REDEFINES" clause.  C folks call this a "union" because the union definition is required.  



Complex Joins and Repeated Data (i.e., not in second normal form).  We may find that we have several different files that repeat some common pieces of data; effectively restating a relationship.  In each file, we may find a slightly different mix of attributes.  These must be combined to reconstruct a complete entity.  However, we'll also find that the data rows from the various files involve contradictions that must be resolved manually.  Plan on it.



Derived Data (i.e., not in third normal form).  Derived data in legacy applications -- almost universally -- cannot be understood from the available data.  In some cases, there are hidden constants or configuration values.  In other cases, data from some other source is folded in via a cryptic join-like lookup.



Ultimately, these problems are part of the flat-file implementation of the business entities.  Each resulting entity will be considerably more sophisticated than the original file layout.



Some Batch Design Patterns
--------------------------



In the most recent example, it wasn't clear what constituted the business entity, and what operations where a merely temporary state change, and what operations where the enduring state change for the object.



A few tests to confirm that the functions had been migrated to methods seemed sufficient.  However, as things progressed, it became clear that simplistic refactoring to encapsulate all fields with getters and setters was a mistake.



Not All Updates Are Created Equal
---------------------------------



After converting most of a 10,000 line program, and starting to get some performance data from the profiler, a few methods showed up as very heavily used.  These were string conversions from the underlying model object.  Clearly, we should be able to cache results and save some conversion.



Most attributes are static, but, a few attributes are changing, so we don't have an easily cacheable value.  





