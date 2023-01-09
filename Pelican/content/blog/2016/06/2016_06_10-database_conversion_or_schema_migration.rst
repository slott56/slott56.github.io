Database Conversion or Schema Migration
=======================================

:date: 2016-06-10 07:35
:tags: data conversion,database administration,software process improvement,agile,schema migration
:slug: 2016_06_10-database_conversion_or_schema_migration
:category: Technologies
:status: published


I was told a horror story about a bad database schema migration. Let's
call the author of the horror story HPL.

HPL related a tale of woeful conversion problems from a mismanaged
schema migration.

While I could feel HPL's pain, the reasons given for their pain were
wrong. They didn't quite get the lessons they had learned.
Consequently, HPL sounded like someone doomed to repeat the mistake,
or—worse—unlearning their lessons.

Here's HPL's most distressing comment.

   "we can't migrate over the weekend and be done w/ it."


Apparently, the horror of a weekend migration was somehow desirable to
HPL. Who wants a lost weekend? And who wants to put all of the eggs in
a single basket?

Anyone who's done more than one "lost weekend migration"—and who's
also honest—knows that they don't go well. There are always subsets of
data that (a) don't get converted properly and (b) have to get swept
under the carpet in order to claim to meet the schedule.

It's a standard situation to have less than 100% of the data
successfully converted and still call the effort a success. If 100%
was not required, why lose a weekend over it?

**Good Plans and Bad Plans**

From far wiser people than me, I learned an important lesson in schema
migration.

These Wiser Heads ran a "conversion" business. They moved data and
applications from platform to platform. They knew a lot about database
schema migrations. A lot.

Their standard plan was to build a schema migration script (usually a
sequence of apps) that could be run to convert the database (or files
or whatever) from old to new schema as often as was necessary.

I'll repeat that.

As **often as was necessary**.

They debugged the script to get to an acceptable level of conversion.
The data conversion (or schema migration) was perfectly repeatable. Of
course, they longed for 100% conversion; but pragmatically, the legacy
software had bad data. So some fraction would not convert. And once
that fraction was found, the schema migration applications could be
modified to treat the non-convertable data in some intelligent way.

Their stated goal was to convert data and run parallel testing with
that converted data as often as necessary to create confidence that
the new data was as perfect a conversion as was possible. At some
point, the confidence became certainty and the parallel testing was
deemed complete. Since they were parallel testing with live data, the
decision amounted to a formalized "commissioning" of the new
application. And by then, the new application was already being used.

There are bad ways to do schema migration, of course. HPL listed many.

**Horrible Mistakes**

The horror story from HPL included this:

   "For the migrated tables, create views in the old system and create
   instead of triggers on those views to ship data to the new system."


It appears that they used views and triggers to create a new system
"facade" over the legacy system. Apparently, they wanted both suites
of application software to coexist. Not a good approach to schema
migration. It appeared that they were trying to share one database
with two application schema.

This seems like it's doomed. Unless they're all geniuses.

Wiser Heads would have strongly suggested that the new system use a
**extract** of the old system's data.

HPL goes on to complain,

   "Sometimes we can take over a column or 2 and sometimes we can only
   take over some of the data in the table".


HPL emphasizes this point with "This is not that far fetched". I'm not
sure why the emphasis was needed.

This is not "far fetched". It doesn't need emphasis. It's not really
much of a problem, either. It's a standard part of schema migration.
Extracting a copy of the data makes this quite easy. Triggers and
views to create some kind of active SQL-based Facade is what created
the complexity. Not the number of columns involved.

HPL summarizes,

   "So you end up w/ [many] tables/views triggers all moving data back
   and forth and faking stuff out"


Back and forth. A fundamental mistake. A copy can be much easier to
manage. One way data movement: Legacy to New.

HPL concludes with a litany of errors of various types: performance,
change management, file system issues, error logging and auditing.
Blah blah blah. Yes, it was a nightmare. I feel their pain.

**What About Coexistence?**

It appears that HPL was involved in a project where the **entire** old
and new applications were supposed to somehow coexist during the
conversion.

It appeared that they failed to do any kind of partitioning.

Coexistence is not a trivial exercise. Nor is it a monolith where the
**entire** legacy application suite must coexist with the **entire**
new schema and the entire new application suite.

Pragmatically, coexistence usually means that some portion of the
legacy must be kept running while some other portion is modernized.
This means the coexistence requires that the application portfolio be
partitioned.

Step 1: Some suite of functionality is migrated. That means data from
the legacy database/file system is copied to new. That also means some
data from new is copied back into the legacy database file/system.
Copied.

Step 2: Some other suite of functionality is migrated. As
functionality is moved, less and less data is copied back to the
legacy.

At some point, this copying back is of no value and can be
discontinued.

**What About Timing?**

This copying clearly requires some coordination. It's not done
haphazardly.

Does it require "real time" data movement? i.e. triggers and views?

Rarely is real time movement required. This is the point behind
partitioning wisely. Partitioning includes timing considerations as
well as data quality and functionality considerations.

It's remotely possible that timing and partitioning are so
pathological that data is required in both legacy and new applications
concurrently. This is no reason to throw the baby out with the
bathwater. This is nothing more than an indication that the data is
being copied back to the legacy application close to real time.

This also means performance must be part of the test plan. As well as
error handling and diagnostic logging. None of this is particularly
difficult. It simply requires care.

**Lessons Learned**

HPL appeared to make the claim that schema migration is super hard. Or
maybe that coexistence is really hard.

Worse, HPL's horror story may be designed to indicate that a
horrifying lost weekend is the only way to do schema migration.

Any or all of these are the wrong lessons to learn.

I think there are several more valuable lessons here.

#. Schema migration can and should be done incrementally. It's ideally
   tackled as an Agile project using Scrum techniques. It's okay to have
   release cycles that are just days apart as each phase of the
   conversion is run in parallel and tested to the user's satisfaction.

#. Coexistence requires partitioning to **copy** any data back to
   unconverted legacy components. Triggers and views and coexistence of
   entire suites of software make a difficult problem harder.

#. The conversion script is just another first-class application. The
   same quality features apply to the conversion as to every other
   component of the app suite.

#. The conversion must be trivially repeatable. It must be the kind of
   thing that can be run as often as necessary to move legacy data to
   the new schema.





