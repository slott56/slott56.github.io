The Schema Evolution Problem
============================

:date: 2008-08-06 10:21
:tags: #python,database
:slug: 2008_08_06-the_schema_evolution_problem
:category: Python
:status: published







Fundamentally, we need to provide explicit version identification on a schema.   This is technically easy, but organizationally nearly impossible.



Technically, we need to use some kind of version control software for our model and the resulting DDL.  We need some meta-meta-data to track schema names and version numbers.  If we like doing too much work, we can introduce a meta-meta-data table with schema name and version numbers.  If we're lazy, there's an even simpler, more reliable approach.



Organizationally, we need the discipline to track every single schema change and determine the level of compatibility with application software.  Garden-variety ALTER statements (to add columns, or extend the size of a column) won't break software; bumping the minor version number is fine.  Adding new tables or views won't break software.  Renames and drops, however, will break software and require a bump to the major version number.



What is a Schema?
------------------



First, a schema isn't the *entire*  set of metadata in a single database instance.  Even if your data is organized in one massive, flat schema with thousands of tables, you still have many smaller "schema" within that single SQL schema owned by "PROD" or "OPS" or "DBA" or "SYS" or whoever owns your production tables.



We'll distinguish between the practical, conceptual schema and the often-misused SQL schema.  Sometimes they overlap, but this is rare.



Your smaller conceptual schemas are the "application-specific" subsets of your overall SQL schema.  If you're smart, your SQL schemas match your conceptual schemas.  If you're lazy, you have a single massive SQL schema and use table name prefixes to try and separate tables into smaller conceptual schemas.



Here's the bottom-line suggestion. Use SQL schema.  Don't use table prefixes.  



[In a Big IT organization, this can't happen because it would "break everything".  Everyone depends on there being a single, flat anonymous schema.  This isn't true, as new applications and maintenance to existing applications are an opportunity to restructure the SQL schema to match the actual use of the tables.  Sadly, it only reduces future maintenance costs, so it doesn't have any current-year impact, so no one ever does this.]



What About the Applications?
-----------------------------



The applications exist independent of the data.  Stored procedures (`A Configuration Management Nightmare <{filename}/blog/2008/08/2008_08_03-stored_procedures_are_a_configuration_management_nightmare_revised.rst>`_ ) are in the application model, not the data model, and evolve independently from the data schema.  However, this isn't always understood, and stored procedures are often mis-managed.



An application could check the schema meta-meta-data to be sure that the application is compatible with the schemas it uses.  It can be a simple query, and an exception gets thrown to indicate that the application can't start and run with the given mix of database schemas.  We know that production programs shouldn't work with the new, upgraded integration test database.  However, we also see this happen; sometimes they crash and we fix them, other times they don't crash, but don't produce right answers, either.  Sigh.



There's a simpler approach, however, than a query.



Should the application and schema version numbers track?  Should the application go through version 2.1.2 and 2.1.3 to indicate that it requires schema version 2.1?  Not necessarily.  There is not a tidy 1:1 mapping between software components and database schema objects.  Generally, database schema objects are shared -- widely -- by software components.  Version 2.1 of application X and version 4.2 of application Y may both depend on version 3.x of database schema Z.



How To Make This Work
----------------------



Put the version number in the schema name.



First, don't create a bunch of XYZ_table1, XYZ_table2 names in a single, flat schema.  Create table1 and table2 in schema XYZ.  Use lots of schemas.  That's why they're available to you.



[Yes, your historical, legacy applications didn't use schemas.  I'm aware that this is new.  Start now.]



Second, don't simply create a "timeless" XYZ schema, use the major release number as part of the name.  Create an XYZ_2 schema.  This will work for all 2.x versions of the schema.



When you move to version 3.1, create a new XYZ_3 schema.  **New**.  Migrate the data from the XYZ_2 schema.  Then, rename XYZ_2 to XYZ_2_OLD, so that any program that improperly uses the old schema will throw an exception and die.  When you need to recover the space, you can drop the XYZ_2_OLD schema, knowing that no program is expected to use it; any program that does use it, needs a fix.



Wait!  That's potentially a lot of code to touch.  Or, if your a mainframer, that's a lot of programs that need to be rebound to the new SQL.  Yep.  It is.  It's a trivial administrative task.  If you can't recompile or rebind your programs, you have serious quality issues that you **must**  fix.



If you can't make simple SQL changes, you have serious flaws in your application software and your overall IT processes.  You **must**  fix these application design flaws and organizational process flaws.  I'm sorry for pointing this out.



Implementation Steps
---------------------



Name your schema.  Allocate your tables to appropriate schema.  More schemas is a better approach than fewer schemas.  There's no performance penalty.  Design and maintenance are simpler.  When you design software, You don't design a single, massive, does-everything application, you write small, focused application programs.  Your database, similarly, should be structured in small, conceptually simple modules.



For Java programmers, use `iBatis <http://ibatis.apache.org/>`_  to extract your SQL from your programs.  The schema changes will be isolated to the iBatis configuration files, mostly.



For Python programmers, you can use `SQLAlchemy <http://www.sqlalchemy.org/>`_  to isolate most of the SQL from your overall application.  Put each schema definition in a separate "models" file.  Include the SQLAlchemy table definitions as well as the Python classes and the mappings.  You can, without too much difficulty, include a few convenience functions that will create or drop-and-create the schema.



If you're creating Python/Django applications, consider including the schema version number on your Django application name.  Your Django project folder for a given site might include things like someapp_1 and someapp_2.  The older application (someapp_1) has one model, and the newer version (someapp_2) has the expanded, incompatible model.



Change Management
------------------



Rather than mess with an complex, risky in-place conversion, you are *adding*  to the database.  You can write a simple batch application to create the someapp_2 data objects from the someapp_1 objects.  Once the data is migrated, you can switch the settings.py and the urls.py files to use someapp_2 instead of someapp_1.  You can easily dry-run this conversion process in an integration test or staging instance of your web site.  If it works there, you can do it again in production.



The best part about keeping the two schema in parallel for a time is the ability to fall-back to the previous version and try the conversion again after fixing the bugs.  You're never replacing anything; you're simply adding a schema and directing the application programs at the new schema.




