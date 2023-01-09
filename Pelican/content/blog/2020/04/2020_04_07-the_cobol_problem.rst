The COBOL Problem
=================

:date: 2020-04-07 08:00
:tags: COBOL,#python,data migration
:slug: 2020_04_07-the_cobol_problem
:category: Technologies
:status: published

https://twitter.com/audreywatters/status/1246609613203505152

The tweet has since been deleted. Here's the old text

| Pet peeve: technologists who sneer at the longevity of programming languages like COBOL. Ain't nobody made it to the moon on react.js. And nobody is willing to replace critical aging software with your new tangled, untested, VC funded framework




It's a tweet, so I know there's no room for depth here.

As it is, it's absolutely correct. Allow me to add to it.

First. Replacing COBOL with something shiny and new is more-or-less
impossible. Replacing COBOL is a two-step job.

1. Replace the COBOL with something that's nearly identical but
   written in a new language. Python. Java. Scala. Whatevs. Language
   doesn't matter. What matters is the hugeness of this leap.

2. Once the COBOL is gone and the mainframe powered off, then you can
   rebuild things yet again to create RESTful API's and put many shiny
   things around it.

Second. Replacing COBOL is essential. Software is a form of knowledge
capture. If the language (and tools) have become opaque, then the job
of knowledge capture has failed. Languages drift. **The audience is in
a constant state of flux**. New translations are required.

Let's talk about the "Nearly Identical But In A New Language."

Nearly Identical
----------------

COBOL code has two large issues in general

-  Data. The file layouts are very hard to work with. I know a lot
   about this.

-  Processing. The code has crap implementations of common data
   structures. I know. I wrote some. There's more, we'll get to it.

We have -- for the most part -- two kinds of COBOL code in common
use.

-  Batch processing. Once upon a time, we called it "Programming in
   the Large." The Z/OS Job Control Language (JCL) was a kind of
   shell script or AWS Step Function state transition map among
   applications. This isn't easy to deal with because the overall
   data flow is not a simple Directed Acyclic Graph (DAG.) It has
   cycles and state changes.

-  Interactive (once called "on-line") processing. We called it OLTP:
   On-Line Transaction Processing. There are two common frameworks,
   CICS and IMS, and both are complicated.

Okay. Big Breath. What do we \*DO*?

Here's the free consulting part.

You have to run the new and old side-by-side until you're sick of the
errors and poor performance of the old machine.

You have to migrate incrementally, one app at a time.

It's hellishly expensive to positively determine what the COBOL
really did. You can't easily do a "clean-room" conversion by writing
intermediate specifications. You must read the COBOL and rewrite it
into Python (or Java or Scala or whatever.)

You cannot unit test your way to success here, because you never
really knew what the COBOL does/did. All you can do is extract
example records and use those to build Gherkin-language acceptance
tests using a template like this. GIVEN a source document WHEN the
app runs THEN the output document matches the example.

In effect, you're going to do TDD on the COBOL, replacing COBOL with
Python essentially 1-for-1 until you have a test suite that passes.

Don't do this alphabetically, BTW.

The processing graph for COBOL will include three essential design
patterns for programs. "Edit" programs validate and possibly merge
input files. "Update" programs will apply changes to master files or
databases. "Report" programs will produce useful reports and feeds
for reporting systems that involve yet more data derivation and
merging.

#. Find the updates. Convert them first. They will involve the most
   knowledge capture, A/K/A "Business Logic."  There will be a lot of
   special cases and exceptions. You will find latent bugs that have
   always been there.

#. Convert the programs that produce files for the updates, working
   forward in the graph.

#. The "reporting" is generally a proper DAG, and should be easier to
   deal with than the updates and edits. You never know, but the
   reporting apps are filled with redundancy. Tons of reporting
   programs are minor variations on each other, often built as
   copy-pasta from some original text and then patched haphazardly.
   Most of them can be replaced with a tool to emit CSV files as an
   interim step.

Each converted application requires two new steps injected into the
COBOL batch jobs.


-  Before an update runs, the files are pushed to some place where
   they can be downloaded.

-  The app runs as it always had. For now.

-  After the update, the results are pushed, also.

This changes merely slow things down with file transfers. It provides
fodder for parallel testing.

Then.

Two changes are made so the job now looks like this.

-  Before an update runs, the files are pushed to some place where
   they can be downloaded. (No change here.)

-  Kill time polling the file location, waiting for the file to be
   created externally. (The old app is still around. We could run it
   if we wanted to.)

-  After the update, download the results from the external location.

This file-copy-and-parallel-run dance can, of course, be optimized if
you take whole streams of edit-update processing and convert them as
a whole.

Yes, But, The COBOL Is Complicated
----------------------------------

No. It's not.

It's a lot of code working around language limitations. There aren't
many design patterns, and they're easy to find.

#. Read, Validate, Write. The validation is quirky, but generally
   pretty easy to understand. In the long run, the whole thing is a
   JSONSchema document. But for now, there may be some data cleansing
   or transformation steps buried in here.

#. Merged Reading. Execute the Transaction. Write. The transaction
   execution updates are super important. These are the state changes
   in object classes. They're often entangled among bad
   representations of data.

#. Cached Data. A common performance tweak is to read reference data
   ("Lookups") into an array. This was often hellishly complex
   because... well... COBOL. It was a Python dict, for the love of
   God, there's nothing to it. Now. Then. Well. It was tricky.

#. Accumulators. Running totals and counts were essential for audit
   purposes. The updates could be hidden anywhere. Anywhere. Not part
   of the overall purpose, but necessary anyway.

#. Parameter Processing. This can be quirky. Some applications had a
   standard dataset with parameters like the as-of-date for the
   processing. Some applications prompted an operator. Some had other
   quirky ways of handling the parameters.

The bulk of the code isn't very complex. It's quirky. But not
complicated.

The absolute worst applications were summary reports with a
hierarchy. We called these "control break" reports. I don't know why.
Each level of the hierarchy had its own accumulators. The data had to
be properly sorted. It was complicated.

Do Not Convert these. Find any data cleansing or transformation and
simply pour the data into a CSV file and let the users put it into a
spreadsheet.

Right now. We have to keep the lights on. COBOL apps have to be kept
operational to manage unemployment benefits through the pandemic.

But once we're out of this. We need to get rid of the COBOL.

And we need to recognize that all code expires and we need to plan
for expiration.


-----

[Good response](https://slott-softwarearchitect.bl...
-----------------------------------------------------

Tom Roche<noreply@blogger.com>

2020-04-07 23:13:45.372000-04:00

[Good
response](https://slott-softwarearchitect.blogspot.com/2020/04/why-isnt-cobol-dead-or-why-didnt-it.html),
thanks.


Great post ... or great-sounding anyway, as I'...
-----------------------------------------------------

Tom Roche<noreply@blogger.com>

2020-04-07 15:36:42.299000-04:00

Great post ... or great-sounding anyway, as I'll admit to having minimal
exposure to COBOL. But since you seem to have had lots, perhaps you can
answer this question: Why didn't COBOL evolve more successfully?
I'm asking because I have had significant exposure to FORTRAN, the other
surviving-at-scale 1st-generation language. By which I mean, there is
still a lot of it "in production" in engineering and science, as opposed
to

\* Lisp: while it continues to be popular in some non-academic niches
(e.g., Emacs), there is (IIRC, ICBW) no economically-significant
long-lived software coded in any Lisp dialect.

\* Algol: which is all-the-way dead.
FORTRAN, OTOH, has survived precisely because it--and more importantly,
related tools, esp compilers--has evolved to solve/overcome many
(certainly not all!) of the sorts of pain-points you describe, while
retaining the significant performance edge that (IMHO, ICBW) prevents
challengers (e.g., Python) from dislodging it for tasks like (e.g.)
running dynamical models (esp weather forecasting).


(Context: I spent several years early in my career...
-----------------------------------------------------

Justin du Coeur<noreply@blogger.com>

2020-04-12 18:03:13.064000-04:00

(Context: I spent several years early in my career building a system in
COBOL. I've since been through about forty languages, and am now a Scala
geek.)

Huh. The interesting corollary of this approach (which, I agree, is
likely the only practical way to go in many cases) is that step one can
probably be done \*automatically*. That is, I would do this as:

1. Write a COBOL-to-X translator, where X is a more-modern programming
language that -- very important -- provides good refactoring tools. (I
would of course use Scala; given that Scala is actually fairly popular
in the finance world, that might actually be right in some cases.) Along
with this, you'd need to write the necessary libraries and adapters for
the data and environment.

2. Test the hell out of it, the way you describe.

3. Start refactoring the resulting monstrosity.

The heart of the current problem isn't just that COBOL is obsolete, it's
that it predates the notion that refactoring \*matters*; the result is
that making incremental improvements is unreasonably hard. If you did a
literal translation to a better language, the resulting code would still
be horrible, but you would have a path forward.

And yes, I would bet that writing an automatic translator isn't all that
hard, in the grand scheme of things. Trying to \*analyze\* COBOL code
properly is likely impossible, but simply translating it, warts and all,
is simply a routine cross-compiler -- a substantial project, but not a
huge one.





