Automated Code Modernization: Don't Pave the Cowpaths
=====================================================

:date: 2013-06-20 08:00
:tags: unit testing,modern,data conversion,legacy code,use case,software process improvement,user stories,schema migration
:slug: 2013_06_20-automated_code_modernization_dont_pave_the_cowpaths
:category: Architecture & Design
:status: published

After talking about some experience with legacy modernization (or
migration), I received information from `Blue
Phoenix <http://bphx.com/>`__ about their approach to modernization.

Before talking about modernization, it's important to think about the
following issue from two points of view.

   Modernization can amount to nothing more than `Paving the
   Cowpaths <http://www.fastcompany.com/1769710/change-management-paving-cowpaths>`__.


From a user viewpoint, "paving the cowpaths" means that the legacy
usability issues have now been modernized without being fixed. The
issues remain. A dumb business process is now implemented in a modern
programming language. It's still a dumb business process. The
modernization was strictly technical with no user-focused "value-add".

From a technical viewpoint, "paving the cowpaths" means that bad
legacy design, bad legacy implementation and legacy platform quirks
have now been modernized. A poorly-designed application in a legacy
language has been modernized into a poorly-designed application in yet
another language. Because of language differences, it may go from
poorly-designed to really-poorly-designed.

The real underlying issue is how to avoid low-value modernization. How
to avoid merely converting bad design and bad UX from one language to
another.

Consider that it's possible to actually **reduce** the value of a
legacy application through poorly-planned modernization. Converting
quirks and bad design from one language to another will not magically
make a legacy application "better". Converting quirky code to Java
will merely canonize the quirks, obscuring the essential business
value that was also encoded in the quirky legacy code.

Focus on Value
--------------

The fundamental modernization question is "Where's the Value?" Or,
more specifically, "What part of this legacy is worth preserving?"

In some cases, it's not even completely clear what the legacy software
really is. Old COBOL mainframe systems may contain hundreds (or
thousands) of application programs, each of which does some very small
thing.

While "Focus on Value" is essential, it's not clear how one achieves
this. Here's a process I've used.

Step 1. Create a code and data inventory.
-----------------------------------------

This is essential for determine what parts of the legacy system have
value. Blue Phoenix has "Legacy Indexing" for determine the current
state of the application portfolio. Bravo. This is important.

I've done this analysis with Python. It's not difficult. Many
organizations can provide a ZIP file with all of the legacy source and
and all of the legacy JCL (Z/OS shell scripts). A few days of scanning
can produce inventory summaries showing programs, files, inputs and
outputs.

A suite of tools would probably be simpler than writing a JCL parser
in Python

A large commercial operation will have all kinds of source checked
into the repository. Some will be inexplicable. Some will have never
been used. In some cases, there will be executable code that was
**not** actually built from the source in the master source
repository.

A recreational project (like HamCalc) reveals the same patterns of
confusion as large multi-million dollar efforts. There are mystery
programs which are probably never used; the code is available, but
they don't appear in shell scripts or interactive menus. There are
programs which have clear bugs and (apparently) never worked. There
are programs with quirks; programs that work because of an
undocumented "feature" of the language or platform.

Step 2. Capture the Data.
-------------------------

In most cases, the data is central: the legacy files or databases need
to be preserved. The application code is often secondary. In **most**
cases, the application code is almost worthless, and only the data
matters. The application programs serve only as a definition of how to
interpret and decode the data.

Blue Phoenix has Transition Bridge Services. Bravo. You'll be moving
data from legacy to new (and the reverse, also.) We'll return to this
"Build Bridges" below.

Regarding the data vs. application programming distinction, I need to
repeat my observation: Legacy Code Is Largely Worthless. Some folks
are married to legacy application code. The legacy code does stuff to
the legacy files. It **must** be important, right?

"That's simple logic, you idiot," they say to me. "It's only logical
that we need to preserve all the code to process all the data."

That's actually false. It's not simple logic. It's just wishful
thinking.

When you actually read legacy code, you find that a significant
fraction (something like 30%) is trivial recapitulation of SQL's "set"
operations: SQL DML statements have an implied loop that operates on a
set of data. Large amounts of legacy code merely recapitulates the
implied loop. This is trivially true of legacy SQL applications with
embedded SQL; explicit FETCH loops are very wordy. There's no sense in
preserving this overhead if it can be avoided.

Programs which work with flat files always have long stretches of code
that models SQL loops or Map-Reduce loops. There's no value in the
loop management parts of these programs.

Another significant fraction is "utility" code that is not
application-specific in any way. It's an application program that
merely does a "CREATE TABLE XYZ(...) AS SELECT ....": a single line of
SQL. There's no sense in preserving this through an "automated" tool,
since it doesn't really do anything of value.

Also. The legacy code has usability issues. It doesn't precisely fit
the business use cases. (Indeed, it probably hasn't fit the business
use cases for decades.) Some parts of the legacy code base are more
liability than asset and should be discarded in order to simplify,
streamline or improve operations.

What's left?

The high value processing.

Step 3. Extract the Business Rules.
-----------------------------------

Once we've disposed of overheads, utility code, quirks, bad design,
and wrong use cases, what's left are a the real brass tacks. A few
lines of code here and there will decode a one-character flag or
indicator and determine the processing. This code is of value.

Note that this code will be disappointingly small compared to the
total inventory. It will often be widely scattered. Bad copy-and-paste
programming will lead to exact copies as well as near-miss copies. It
may be opaque.

::

    IF FLAG-2 IS "B" THEN MOVE "R" TO FLAG-BC.

Seriously. What does this mean? This may turn out to be the secret
behind paying bonus commissions to highly-valued sales associates. If
this isn't preserved, the good folks will all quit *en masse*.

This is the "Business Rules" layer of a modern application design.
These are the nuggets of high-value coding that we need to preserve.

These are things that must be redesigned when moving from the old
database (or flat files) to the new database. These one character flag
fields should not simply be preserved as a single character. They need
to be **understood**.

The business rules should **never** be subject to automated
translation. These bits of business-specific processing must
**always** be reviewed by the users (or business owners) to be
absolutely sure that it's (a) relevant and (b) has a complete suite of
unit test cases.

The unique processing rules need to have modern, formal documentation.
Minimally, the documentation must be in the form of unit test cases;
English as a backup can be helpful.

Step 4. Build Bridges.
----------------------

A modernization project is not a once-and-done operation.

I've been told that the IT department goal is to pick a long weekend,
preferably a federal Monday holiday weekend (Labor Day is always
popular), and do a massive one-time-only conversion on that weekend.

This is a terrible plan. It is doomed to failure.

A better plan is a phased coexistence. If a vendor (like Blue Phoenix)
offers bridge services, then it's smarter and less risky to convert
back and forth between legacy and new over and over again.

The policy is to convert early and convert often.

A good plan is the following.

#. Modernize some set of features in the legacy quagmire of code. This
   should be a simple rewrite from scratch using the legacy code as a
   specification and the legacy files (or database) as an interface.

#. Run in parallel to be sure the modern version works. Do **frequent**
   data conversions from old to new as part of this parallel test.

#. At some point, simply stop converting from old to new and start using
   the new because it passes all the tests. Often, the new will have
   additional features or remove old bugs, so the users will be
   clamoring for it.

For particularly large and gnarly systems, all features cannot be
modernized at once. There will be features that have not yet been
modernized. This means that some portion of new data will be
converted back to the legacy for processing.

The feature sets are prioritized by value. What's most important to
the users? As each feature set is modernized, the remaining bits
become less and less valuable. As some point, you get to the
situation where you have a portfolio of unconverted code but no
missing features. Since there are no more desirable legacy features
to convert, the remaining code is -- by definition -- worthless.
The unconverted code is a net cost savings.


Automated Translation
---------------------

Note that there is very little emphasis on automated translation of
legacy code. The important work is uncovering the data and the
processing rules that make the data usable. The important tools are
inventory tools and data bridging tools.


Language survey tools will be helpful. Tools to look for file
operations. Tools to look for places where a particular field of a
record is used.
Automated translation will tend to pave **all** the cowpaths: good,
bad and indifferent. Once the good features are located, a manual
rewrite is just as efficient as automated translation.
Automated translation cannot capture meaning, identify use cases or
write unit test cases. Thoughtful manual analysis of meaning,
usability and unit tests is how the value of legacy code and data is
preserved.






-----

You nailed it here, Steven.  It&#39;s not about th...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2013-06-21 10:25:59.162000-04:00

You nailed it here, Steven. It's not about the code, it's about the
business logic, the IP that's been built into these systems over 10-20
years- and the data. Its not easy, but unlocking this stuff has a real
impact on making smarter business decisions. Great summary and points
here, really well done.


Steven, Good Work, Detailing each point to its peak. 
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2013-07-14 23:02:15.594000-04:00

Steven, Good Work, Detailing each point to its peak.





