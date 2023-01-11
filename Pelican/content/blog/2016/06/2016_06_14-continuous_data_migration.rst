Continuous Data Migration
=========================

:date: 2016-06-14 08:00
:tags: data conversion,data migration,continuous migration,design,continuous deployment,continuous integration
:slug: 2016_06_14-continuous_data_migration
:category: Technologies
:status: published


See {filename}/blog/2016/06/2016_06_10-database_conversion_or_schema_migration.rst

People talk about CI/CD (Continuous Integration/Continuous
Deployment).

They also need to talk about CM (Continuous Migration).

"Wait, what?" you ask.

When we roll out a new version of the software (CD) there are three
common situations.

#.  The new software uses the existing data model with no changes. This
    is a "minor version change": from v3.2 to v3.3.

#.  The new software requires a tweak to the schema, but it's backward
    compatible. This, too, is a minor version change. In a SQL context,
    we might have used an ALTER TABLE to add a nullable column. If there
    are no SELECT \* statements in the code, this change is essentially
    transparent to legacy code.

#.  The new software involves a new schema that's not backwards
    compatible. This is a major version change. From v3.2 to v4.0. This
    is difficult. Really difficult.


Clearly, the first two can be done with the data in place. New
software is installed, the servers are restarted, and away we go. In a
big environment, there may be a rolling deployment. There may be a
`canary release <http://blog.christianposta.com/deploy/blue-green-deployments-a-b-testing-and-canary-releases/>`__
that will get converted first, then others will be brought online.

A change of the Second Kind does involve the one-time database
transformation script. This may lead to some down-time. Or it may lead
to a feature toggle so that the new software can work with the old
database until the script is run.

In a NoSQL context, a change of the Second Kind doesn't require the
one-time script. The new documents have new fields that old documents
don't have. NoSQL apps -- in general -- must be able to cope with data
model variations.

A change of the Third Kind is trouble.

Big trouble.

We have two schema: the v3 schema and the v4 schema. We have two sets
of software: the v3.2 release and the v4.0 release. We'd like to have
just one valid set of data. How do we deal with this?

How can we do schema migration badly?
-------------------------------------


We can't **easily** have a single software release that includes one
set of data in both schema. It's **technically** possible Anything
that doesn't involve time travel, anti-gravity or perpetual motion is
**technically** possible. But it rapidly becomes so complex that we
have to set this uber-version idea aside.

We have to do more deployment work to have both v3.2 and v4.0
installed in parallel. v3.2 will use data in the v3 schema, v4.0 will
use data in the new schema.

How do we migrate the data from the old schema to the new schema?

This can be tricky. There are proven bad ideas out there. Really
epically bad ideas.

One Very Bad Idea (VBI™) is the one-time-only data migration. Back in
the olden days, we couldn't afford enough storage to have two copies
of the database. Seriously. When a company owned exactly one computer
(before PC's -- a Very Long Time Ago) the conversion had to be done by
making special backups and restoring the backups into the new schema.

This VBI is still with us today.  Lots of places want to do
one-time-only data migrations because it's the traditional approach.
If they can't done a one-time conversion (over a long weekend) they
complain. Loudly.

BTW. This **never** worked well. The one-time-only conversion software
was never tested carefully, and therefore rarely worked the one time
it was needed. Also, data profiling was never done, so edge and corner
cases were found during conversion. These often called the new
software's features into question, leading to larger and larger
problems.

Continuous Migration
--------------------


The ideas behind continuous migration are these.

#.  We're always going to be migrating the data. Always.

#.  Storage is cheaper than labor. When in doubt, buy more storage.

#.  Data outside the database (in CSV files or YAML documents) is smaller
    than data inside the database. Don't be afraid to export.

#.  Data outside the database is inaccessible. Be cautious of the implied
    down-time during exports and imports.

#.  ABP. Always Be Profiling. If you don't have a data profiler in place
    right now, that's the first thing to build. There are schema
    definition tools and schema checking tools. Look at
    `JSON-Schema.org <http://json-schema.org/>`__. Write schema
    definitions and use a data profiler to examine all rows and check all
    rules. **All**. Seriously. All. In a SQL DB, actually check the
    foreign keys to be sure the referenced row exists; you'll be
    surprised.

#.  We're moving forward. We're not milling around; we're not supporting
    the old version except for the purposes of a parallel test or a
    fall-back in the event the next version doesn't work. There's no
    long-term coexistence strategy. Preserve the data; upgrade the
    software.


Here's the central data migration requirement:

    **Be able to migrate to the new schema as many times as needed.**


I'll repeat that. As. Many. Times. As. Needed.


Migration is **not** a one-time thing. You do it all the time.


#. Migrating (and possibly sanitizing or subsetting) production data into the development environment.
#. Migrating production data for QA testing.
#. Migrating production data for integration testing.
#. Migrating production data for performance testing.
#. Migration production data for the production upgrade.


These are all the same activity.


I'll repeat that. The. Same. Activity. Sometimes with mappings.
Sometimes with filters.


Since you'll do many, many migrations, your data migration
programming is as important as your application programming. Perhaps
**more** important than the application code because it's what
preserves the data, and the data is the **only** thing of value.
Applications come and go. Data is forever.


Having real data available permits seamless, silent, and automatic
parallel testing. We can easily do a parallel test with v3.2 and v4.0
release candidates by simply running the migration (or migration with
subset filter) to gather some data for the parallel test. If the
release candidate has problems, we can fix v4.0 to create the next
release candidate, re-migrate the data, and try the parallel test
again.


At some point the v4.0 release is final, and we need to migrate all
of the data. This (usually) involves some feature toggles to put v3.2
into a special "end-of-life" mode where the keys for records which
change are logged separately. After turning off v3.2 and turning on
v4.0, a second phase of migration will process these end-of-life rows
through the migration mill.

Software and Schema Design Consequences
---------------------------------------


This has an important consequence.


    **Your software must be explicitly bound to a specific schema by major version number.**


Explicitly bound. In a SQL context, you can use the "schema"
construct an include the version number in the schema name.
"myapp_v3" vs. "myapp_v4". This becomes a ubiquitous qualifier on all
table names. SELECT col FROM myapp_v4.some_table AS st.


Yes. Do this Everywhere. Do it Now.


If you're using mybatis or SQLAlchemy to get the SQL out of your
application, then this kind of thing is a trivial change. If you have
SQL in your application code, well, you have two problems to solve.
First, get the SQL out of your application. Then make the schema
version explicit.


In a NoSQL context, you can include the schema version as part of a
collection name. "collection_v3" or "collection_v4".


This should be present everywhere.

Then, you'll need data validation apps and data migration apps. The
validation apps will use your favorite schema definition and schema
validation framework. Start running this as soon as you think you
might need to make a major version change.

Finally, you'll need the data migration tool set. This will involve
filter rules and sanitizing rules. These are not sophisticated "rules
engine" kind of things with unbounded complexity. They're usually if
statements and simple computations. But they come and go pretty
freely, so design the software in a way that makes the filter and
sanitizing code obvious.


Now you can -- trivially -- migrate data between schema versions
inside the same database. You can have v3.2 and v4.0 running
side-by-side. You can migrate the data early and often. You can
profile and validate the data. You have a formal schema for the data
validation.



-----

Thank you for the informative post about Software ...
-----------------------------------------------------

yuvaraj<noreply@blogger.com>

2019-03-20 03:04:03.310000-04:00

Thank you for the informative post about Software Architecture on
continuous Data Migration, Found it useful . cloud migration services
have now become secured and with no-risk
`Database Migration
Services <http://liainfraservices.com/database-migration-services>`__
`VMware Cloud Migration
Services <http://liainfraservices.com/vmware-cloud-migration-services>`__
`Azure Cloud Migration
Services <http://liainfraservices.com/azure-cloud-migration-services>`__
`AWS Cloud Migration
Services <http://liainfraservices.com/aws-cloud-migration-services>`__
`Cloud Migration
Services <http://liainfraservices.com/cloud-migration-services>`__


Very clear and detailed guide on <a href="https://...
-----------------------------------------------------

Jim<noreply@blogger.com>

2019-11-14 09:28:53.507000-05:00

Very clear and detailed guide on `migration of data
center <https://www.nakivo.com/industry/data-center-migration/>`__ .
Enjoyed reaing, thanks!





