More On Inheritance vs. Delegation
==================================

:date: 2011-11-17 08:00
:tags: #python,object-oriented design,delegation,inheritance
:slug: 2011_11_17-more_on_inheritance_vs_delegation
:category: Technologies
:status: published

| Emphasis on the "More On" as in "Moron".  This is a standard design
  error story.  The issue is that inheritance happens along an "axis" or
  "dimension" where the subclasses are at different points along that
  axis.  Multi-dimensional inheritance is an EPIC FAIL.
| **Context**
| Data warehouse processing can involve a fair amount of "big batch"
  programs.  Loading 40,000 rows of econometric data in a single swoop,
  updating dimensions and loading facts, for example.
| When you get data from customers and vendors, you have endless
  file-format problems.  To assure that things will work, each of these
  big batch programs has at least two operating modes.

-  Validate.  Go through all the motions.  Except.  Don't commit any
   changes to the database; don't make any filesystem changes.  (i.e.,
   write the new files, but don't do the final renames to make the files
   current.)
-  Load.  Go through all the motions including a complete commit to the
   database and any filesystem changes.

| **Problem**
| What's the difference between the two modes?  Clearly, one is a
  subclass of the other.

-  Load can be the superclass.  The Validate subclass simply replaces
   the save methods stubs that do nothing.
-  Validate can be the superclass.  The Load subclass simply implements
   the save method stubs with methods that do something useful.

| Simple, right?
| Wrong.
| **What Doesn't Work**
| This design has a smell.  The smell is that we can't easily extend the
  overall processing to include an additional feature.
| Why not?
| This design has the persistence feature set as the inheritance axis or
  dimension.  This is kind of limited.  We really want a different
  feature set for inheritance.
| Consider a Validate for two dimensions (Company and Time) that loads
  econometric facts.  It has stub "save" methods.
| We subclass the Validate to create the proper Load for these two
  dimensions and one fact.  We replace the stub save methods with proper
  database commits.
| After the actuaries think for a while, suddenly we have a file which
  includes an additional dimension (i.e., business location) or an
  additional fact (i.e., econometric data at a different level of
  granularity).  What now?  If we subclass Validate to add the dimension
  or fact, we have a problem.  We have to repeat the Load subclass
  methods for the new, extended Load.  Oops.
| If we subclass Load to add the dimension or fact, we have a problem.
  We have to repeat the Validate stubs in the new extended Load to make
  it into a Validate.  Oops.
| **Recognizing Delegation**
| It's difficult to predict inheritance vs. delegation design problems.
| The hand-waving advice is to consider the *essential* features of the
  object.  This isn't too helpful.  Often, we're so focused on the
  database design that persistence seems essential.
| Experience shows, however, that some things are not essential.
  Persistence, for example, is one of those things that should *always*
  be delegated.
| Another thing that should always be delegated is the more general
  problem of representation: JSON, XML, etc., should rely on delegation
  since this is never essential.  There's always another representation
  for data.  Representation is always independent of the object's
  essential internal state changes.
| **Consequence**
| In my case, I've got about a dozen implementations using a clunky
  inheritance that had some copy-and-paste programming.  Oops.
| I'm trying to reduce that technical debt by rewriting each to be a
  proper delegation.  With good unit test coverage, there's no real
  technical risk.  Just tedious fixing the same mistake that I rushed
  into production twelve separate times.
| Really.  Colossally dumb.



-----

Check out &quot;Composition versus inheritance: A ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-11-25 15:15:50.851000-05:00

Check out "Composition versus inheritance: A first attempt at designing
the new cars" in the chapter "Putting Plans into Action with the
Strategy Pattern" in the book Design Patterns for Dummies


You produce the error when you design Validate as ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-11-17 11:57:27.299000-05:00

You produce the error when you design Validate as superclass with save
method stubs, it clearly should do nothing but validation. Mixing
different interfaces, -- that's the real cause. When you separate them,
it becomes indifferent to inherit Validate as a mix-in superclass or
instantiate it as a component.


In general, problems like the above are exactly wh...
-----------------------------------------------------

Adam<noreply@blogger.com>

2011-11-17 12:23:23.506000-05:00

In general, problems like the above are exactly why inheritance,
especially implementation inheritance, is a really bad idea. Composition
avoids this problem entirely even if it requires more work on the part
of the programmer.
Your real problem is that 'Load' and 'Validate' aren't actually
subclasses of one another: they have different side-effects and
therefore different invariants (one modifies the database, the other
does not). The Liskov Substitution Principal tells us that classes with
different invariants cannot be subclasses of one another.
The bigger problem is that 'modifies the database' is an invariant that
not all code cares about. To support code that cares and code that does
not care, one must inject an interface into the inheritance diagram:
ETLProcessor (interface)
\|-OnlyValidate
\|-LoadForReal
with 'ETLProcessor' explicitly noting that it is undefined whether the
database is modified or not. This way, you can't have loads that don't
actually load and validates that do load. ETLProcessor is still subject
to the fragile base-class problem, but that's true of all inheritance
schemes; composition is the only way to avoid this problem.





