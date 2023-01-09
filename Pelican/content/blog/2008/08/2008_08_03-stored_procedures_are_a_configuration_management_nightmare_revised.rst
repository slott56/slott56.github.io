Stored Procedures Are A Configuration Management Nightmare (revised)
====================================================================

:date: 2008-08-03 16:44
:tags: #python,database
:slug: 2008_08_03-stored_procedures_are_a_configuration_management_nightmare_revised
:category: Python
:status: published







I've been asked about the proper location of Stored Procedures more than once.  I've come down very strongly in opposition to triggers and stored procedures.



First, `PL/SQL is slow <{filename}/blog/2007/05/2007_05_27-plsql_and_java_the_benchmark_challenge_revised.rst>`_ .  Anecdotally, people claim that introducing PL/SQL made an app faster.  I submit that they restructured the application significantly to create small, focused transactions, and that's what created the improvement.  As a practical matter, you need to write focused, PL/SQL-like transaction methods in your Java programs.  While technically possible, you can't casually execute SQL statements willy-nilly.



Second, it's hard to do configuration management on stored procedures.  Not impossible, but very hard.  The reasons are entirely organizational.



Recently I received an email that was nearly opaque, but seemed to indicate that the organization couldn't clone production to create another test, and couldn't rationalize the versions of their various stored procedures.   I think they wanted a puff of :strong:`Faerie Dust`\ ™ that would allow stored procedure X to determine if it was being used by package Y or package Z and behave differently in the different contexts.  The request makes no sense -- this is just a version control issue.  Clearly, there are two versions of X, but the emailer claimed there was one version of X and it had to determine it's behavior dynamically.



:strong:`Conflation - The Organizational Root Cause`



A stored procedure lives in the database.  Consequently, it's conflated with persistent data and schema definitions and assigned -- for no good reason -- to the DBA's.  These three things -- data, schema and processing -- have little to do with each other.  They emphatically do not belong together.   However, they're almost always conflated into a murky puddle of SQL.



Let's break these things apart.



:strong:`Data`  is the organization's actual data.  Some (but not all) of the business records lives in managed databases.  Some live in desktop application documents (word processing, spreadsheets, unmanaged desktop databases, etc.)  Data is precious, perhaps the most precious thing in the organization.



:strong:`Schema`  (or metadata) is table, column, view and index definitions.  It's also physical stuff like tablespaces, files, instances, etc.  Some of this is important, some of it is subject to change without notice.  Tablespace configuration parameters rarely matter except as an implementation detail.



:strong:`Processing`  is triggers, stored procedures and all of the application programs that live outside the database.  Note that there is no crisp distinction between "low-level" and "high-level" processing.  Many DBA's have tried to explain to me that CRUD rules are "low-level", but then they add some foreign-key relationships, after that they also need to add some many-to-many relationships and the intermediate bridge tables, then they start adding other things that are part of larger and more complex relationships.  Stop!  If you can't find a boundary easily, it doesn't really exist. 



:strong:`Version Control`



Data -- typically -- has fairly loose version control.  The RDBMS often has secret sequence numbers (SCN's) that are used internally to manage cache and synchronize physical files.  These transaction sequence numbers are, effectively, a kind of version number for the data.



Often, we'll have a "last changed date" in a database record.  This is a surrogate version number for the record.  It tells us when the data changed.  Most applications don't record a complete change log for the data, we simply update the change date.  A few applications do create detailed change logs.  In some cases, people try to leverage the database logging facilities to back into a formal change log for the data.



Schema is rarely under any kind of version control.  Metadata is often the least disciplined part of the enterprise infrastructure.  It's easy (really easy) to have formal version control over metadata.  It's rarely done, however.  For some reason, DBA's don't seem to use version control software.



Application software, typically, has the best version control.  Many organizations use some formal version control software (CVS, Subversion or some commercial product like MKS, VSS or PVCS.)  This can easily apply version control information to the source code (and even the resulting .class files.)  



[Some organizations can't even put their application software under version control.  This doesn't change the issue of conflating data, schema and application.]



For no good reason stored procedures are the province of the DBA's (who don't use version control software.)  Consequently, the external application software (in Java, Python or whatever) may have version control information, but the stored procedures never have version control.



:strong:`Schema Versions`



The database schema (the tables, columns, indexes, views and sequence generators) has a version number.  The version number for a schema -- like the version number for software -- defines "compatibility".  



Schema version 2.1 and 2.2 are "compatible" in some sense.  Schema versions 3.5 and 4.1 are incompatible.



What defines "compatibility"?  Clearly, "compatible" means "compatible with SQL DML".  If you've done standard database ALTER statements (adding columns, expanding the sizes of columns) or changing indexes or adding views, you haven't broken any SQL DML.  The old SQL still works with the new schema.  This is a 2.2 to 2.3 kind of change.



If you've dropped a column or table or view, or you've shortened a column, or changed the type of a column, then you've made a change which may break existing SQL.  When you've make this kind of change, you'll need to bump the major version number.



You need two things:



:strong:`Discipline`.  This doesn't happen by default.



:strong:`Some meta-meta-data`.  A table that has schema names and version numbers is all you really need.  It's nice to fold in "applicable dates" and "responsible person", etc., but not essential.   In some cases, you can use database comments for this.



When you make database changes, you must create a script that (a) makes the change and (b) updates the database schema version table.  That's about it.



:strong:`What About Stored Procedures?`



Why can't we annotate our stored procedures with version numbers and put them under version control like the rest of the database?



The question is rhetorical.  Of course we can put stored procedures under version control.  It just requires some discipline.  And -- perhaps -- making stored procedures part of application software's responsibility, and not part of the DBA's job.



If we take stored procedures away from the DBA's, we need a formal turnover procedure for putting a particular suite of stored procedures into a database.



Separating the stored procedures from the schema via a formal turnover has some marvelous consequences.



1.  You can reconstruct the stored procedures from your source code repository exactly the same way you extract your Python or Java.  Indeed, you can make a complete software package with all of the various language elements.  You can extract all of the procedure creates as a big script and run it any time you need to.



2.  The database has two distinct parts:  the Data, the Processing.  These two are matched by schema version number.  The DBA's are responsible for the data; the schema versions; the preservation of essential corporate information.  The DBA's are also responsible for running the scripts that upgrade that portion of the application software that happens to live in the database.  The DBA's aren't responsible for stored procedures.



3.  The migration of a database from development to test is a two-part job.  Move the schema and data from the developers to a test environment.  Separately, run all of the scripts to build the proper software version that matches the schema of the data.



4.  You have explicit compatibility checks.  Version 2.x of schema and software are being used in production.  Version 3.x of schema and software is in some kind of parallel test prior to conversion.  Version 3.y of schema and software is in some early test; 3.z is in development.



5.  You can begin to wean yourself away from the nightmare of stored procedure management.  Once you take this out of the DBA's hands, you find that a consistent set of Python (or Java) packages that define the Model layer does everything that stored procedures and triggers do, only more simply and more maintainably.



:strong:`What's So Hard?`



It's very easy to put stored procedures under explicit, clear version control.  With a little care, even a database schema can be put under version control.



What's so hard is actually making the organizational change.  Ask around.  The DBA's will tell you that they are overworked, because they're "forced" to write all the stored procedures and triggers.  Forced?  By whom?  



Generally, the "organization" seems to mandate that everything SQL -- tables, columns, indexes, views, stored procedures and triggers -- pass through the DBA's.  The distinction between data and processing is somehow lost.  Splitting it up will often anger the manager of the DBA's, who'll make the case that no one else can be trusted to create stored procedures.



When testing stops because of version control issues, when production fails, it seems like the problem should be addressed.  It's usually obvious that there are serious version control problems between the schema and stored procedures.



I only know that there's a long-standing, steadfast refusal to split the database into data and processing elements.  The consequence of this is that stored procedures are unmaintainable, testing is nearly impossible, and production problems are rampant.



Consequently, I suggest that stored procedures and triggers never be used.  Ever.




