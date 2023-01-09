Legacy Code Preservation: Paving the Cowpaths  
===============================================

:date: 2013-04-30 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_04_30-legacy_code_preservation_paving_the_cowpaths
:category: Technologies
:status: published

.. container:: section
   :name: paving-the-cowpaths

   No discussion of legacy preservation is complete without some "Paving
   the Cowpaths" stories.

   The phrase refers to the way cows tend to meander across the
   landscape in a remarkably consistent way. The cows reliably follow a
   consistent path. The paths tend to wander in ways that seem crazy to
   us.

   Rather than do a survey and move some dirt to lay a straight,
   efficient road, paving the cowpaths refers to simply using the legacy
   path without consideration of more efficient alternatives.

   There are two, nearly identical paving the cowpath stories, separated
   by three years. We'll only look at one in detail, since the other is
   simply a copy-and-paste clone.

.. rubric:: The Code Base
   :name: the-code-base

In both cases, the code base was not something I saw in any
detail. In one case, I saw a presentation, and I talked with the
author in depth. In the other case, I had the customer assign a
programmer to work with me.

In one case they had a fabulous application system that was the
backbone of their business. It was lots and lots of VAX Fortran
code that did simply everything they needed, and did it exactly
the right way. It was highly optimized and encoded deep knowledge
about the business.

[The other case wasn't so fabulous, but the outcome is the same.]
Sadly, each gem was entirely written to use flat files. It was
relatively inflexible. A new field or new relationship required
lots of tweaking of lots of programs to accommodate the revised
file layout.

In 1991, the idea of SQL databases was gaining currency. Products
like Oracle, Ingres, Informix and many others battled for market
share. This particular customer had chosen Ingres as their RDBMS
and had decided to convert their essential, foundational
applications from flat file to relational database.

.. rubric:: The Failure
   :name: the-failure

There was a singular, and epic failure to understand relational
database concepts.

A SQL table is **not** a file that's been tarted up with SQL
access methods.

A foreign key, it turns out, is actually rather important. Not
something to be brushed aside as "too much database mumbo-jumbo."
What they did was preserve **all** of their legacy processing.
Including file operations. They replaced OPEN, CLOSE, READ and
WRITE with CONNECT, DISCONNECT, SELECT and UPDATE in a remarkably
unthinking way.

This also means that they preserved their legacy programs that
made file copies. They rewrote a file copy as a table copy, using
SELECT and INSERT loops.

Copying data from one file to another file can be a shabby way to
implement a one-to-many relationship. It becomes a one-to-one with
many copies. A file copy can be amazingly fast. A SQL table copy
can never be as fast as a file copy.

They can, of course, easily compare the database results with the
old flat file results. The structures are nearly identical. This,
I think, creates a false sense of security.

.. rubric:: My Condolences
   :name: my-condolences

In both cases, I was called in to help them "tune" the database to
get it to run faster.

I asked about the longest-running parts of the application. I
asked about the most business-critical parts of the application.
"What's the most important thing that's being blocked by
unacceptable slowness?"

It's not possible to get everything to be fast. It is, however,
possible to get important things to be fast. Other, less important
things, can be slow. That's okay.

They talked me though a particularly painful part of the
application that was very important and unbelievably slow. It
cloned a table making a small change to each row.

"Oh," I suggested, "you could have used an UPDATE statement with
no WHERE clause to touch all rows."

That suggestion, it turns out, was wrong. The copying was
essential because the keys were incomplete.

Then it began to dawn on me.

Their legacy application did file copies because they were almost
instant. And the filename (and directory path) become part of the
key structure.

They were shocked that a SQL table copy could be so amazingly
slow. Somehow, the locking and logging that create transactional
integrity wasn't visible enough.

The really hard part was trying
to---gently---determine **why** they thought it necessary to clone
tables.

The answer surfaced slowly. They had simply treated SQL as if it
was a file access method. They had not redesigned their
applications. They did not understand how primary key, foreign key
relationships were supposed to work. They had, essentially, wasted
a fair amount of time and money doing a very, very bad thing.

.. rubric:: Preservation
   :name: preservation

They preserved the relevant business features.

They also preserved irrelevant technical implementation features.
They didn't understand the distinction between business process
and technical implementation details.

In effect, they labored under the assumption that all code was
precious, even code that was purely technical in nature.






