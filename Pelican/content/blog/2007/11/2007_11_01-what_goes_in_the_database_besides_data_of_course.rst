What Goes In the Database?  Besides Data, of Course.
====================================================

:date: 2007-11-01 10:23
:tags: architecture,software design,database design
:slug: 2007_11_01-what_goes_in_the_database_besides_data_of_course
:category: Architecture & Design
:status: published







In order to talk about what goes in the database, we need to put the question into some kind of useful context.  Weirdly, the question came to me in a context so twisted and bizarre that it's a little hard to sort out what -- precisely -- was going on.  First, what goes in a database, then, things that muddy the waters.



Before talking about databases, we need to look closely at our objective: knowledge capture and modeling.



Modeling
--------



Software captures knowledge about data and processing.  Generally, our software knowledge capture involves building a model of the real world inside our computer systems.  Sometimes it's just a paper model (e. g., a UML depiction of something.)  Mostly, however, software is a kind of model of some interesting, valuable aspect of the real world.



An object-oriented model of the world lets us capture that information in the form of objects and their interactions.  We define classes of objects, which include the object's attributes and behaviors.



Another common model is a data-only model; for example, the SQL implementation of the relational model.  A third common model is a procedure-only model; for example PL/SQL code, or C programs.  Yes, I'm deprecating these models as incomplete.



Clearly, when we're doing software development we need to get to an object-oriented model.  We can get there directly, via Python or Java.  Or we can get there indirectly by attempting to integrate a data-only model and a procedure-only model.



The RDBMS Bias
--------------



Many well-meaning folks get all tangled up with the data-only model.  For some reason, the database appears as the central arterial essence of modeling and everything else is just a kind of tributary or organ feed by the lifeblood information flowing through that database.



Data *is*  more important than process; that much is clear.  We preserve data when converting among various kinds of application software.  We change processes frequently and freely.  Data, however, we preserve as the foundation for new processes.



However, we have to avoid conflating data with database.  And we further have to avoid conflating database with a particular vendor's implementation.  Oracle is not the same as database; database is not the same as data.  But you hear people talk about Oracle as if it **is**  the enterprise information.



What Goes In The Database?
--------------------------



Since our goal is a model with reasonably fidelity to the real world, and that model must involve both data and processing, our model is object-oriented.



Clearly, our desire is to put objects into the database.  We have three fundamental choices: an object data store, blobs in a relational data store, or an object-relational mapping.



Object data stores suffer from a taint.  "It ain't SQL".  Even some of the fancy, extended Object SQL variants don't appeal enough to people who have money and are terribly afraid of the downside consequences of appearing to fail.  I've learned that failure (or the appearance of failure) hurts more than a success of equal magnitude.  People will work harder to avoid losing $100 than they will to gain $100.



Blobs in a relational store have a narrow band where they make sense.  Generally, a blobby attribute makes the most sense.  We have a blob surrounded by ordinary relational database attributes.  While SQL can handle most attributes, it can't handle the blob; that has to be taken outside the SQL environment for processing.  It's opaque to SQL.  



An approach where everything is a blob, and the relational database is just storage for blobs is creepy.  Why not use an object database?  Oh, right, the taint.  Consequently, I've had customers suggest that we make everything a blob and force it into Oracle, bypassing all other SQL features.  



The ORM-Friendly Model
-----------------------



If we focus on Object-Relational Mapping, we have numerous small victories.  First, we analyze our problem in terms of real-world entities, their attributes and behaviors.  We develop a software design, mapping real-world things to objects which are constrained by the need to implement them in Python (or Java or Ruby.)  



We can then develop a relational database design which carries the objects as "cleanly" as possible.  This SQL model will (often) look peculiar or even unorthodox to fat, old DBA's of my vintage.  [Kentucky Hills, late 1950's, good years.]



What's in an Object-Relational Model?
-------------------------------------



The fundamental entities usually map (more-or-less) to tables in a pretty direct way.  However, the real world has innumerable kinds of relationships.  The OO world tries to match this by applying a little bit of rigor.  The relational world, however, has only one kind of relationship: the foreign key.



If we have a good object-relational mapping layer, we can provide pleasant object-friendly definitions which can be mapped to Data Definition Language (DDL) and Data Manipulation Language (DML) without burning too many brain calories.  If, on the other hand, we lack a good ORM mapping, we have to think through each kind of relationship and how we'll implement it.



My ORM experience is split four ways among `SQLAlchemy <http://www.sqlalchemy.org/>`_ , `Django <http://www.djangoproject.com/documentation/model-api/>`_ , totally home-brewed designs, and the kind of ORM that `iBatis <http://ibatis.apache.org/>`_  handles.  SQLAlchemy and Django handle everything, including DDL.  iBatis requires that you do a competent database design, but it will build your Java objects neatly for you.



All of these (even my own home brew) have to cope with transforming rich object semantics into limited relational implementation.



We have tables and columns, of course.  Each table has a unique, system-generated surrogate primary key (PK) and whatever is required to assure that the PKs are unique.  A unique primary key index, or a suitable PK column declaration.



The relational implementation always has foreign keys (FK).  The foreign keys can always be constrained with declared, formal FK constraint clauses.  The FK's are always based on the surrogate keys.



For performance reasons, you might want to add indexes on non-key fields.  More power to you.  That's just performance tuning, not the essential model structure.



What's Missing?
----------------



There are a number of things which are explicitly not present.



1.  **Triggers**.  While some argue for triggers, I haven't had a good experience with a mature application.  Maintenance of triggers seems to get exponentially more expensive.  Since we have object class definitions, it isn't clear why we need triggers.



2.  **Stored Procedures**.  Please don't put code in the DB.  It is a configuration management nightmare.  Further, I can't figure out what the allure is. ` PL/SQL is slow <{filename}/blog/2007/05/2007_05_27-plsql_and_java_the_benchmark_challenge_revised.rst>`_ .  While some people try to tell me that PL/SQL improves performance, I can't find much tangible evidence; no customer has benchmarks, and I can't see the basis for the claim.



3.  **Cascade Delete Rules**.  These seem cool, but they aren't exercised much, and the few places where people can delete things, the application handles it nicely.  "What about transient data?"  Transient data doesn't belong in a database: use files or queues.



4.  **Other Random Constraints**.  The SQL Check Constraint is one of those things where there's a blurry distinction between "essential" features of the entity and special cases, exceptions and situational policies.  The check constraints are rarely universally true, so why try to embed them in the database?  There are few enduring, essential, universal constraints, outside mandatory foreign key and not-null relationships.  Just about everything else will evolve with the use cases.



What About ...?
----------------



What about composite keys?  What about them?  They're a bunch of columns.  Use a secondary index for fast access.  Oh, they have to be unique?  Use a unique secondary index.  A composite key isn't the unique, never-changing object identifier.  It may not change much, but the mere possibility that it could change means it isn't a permanent row identifier.



What about "natural" keys?  They're columns.  Use a secondary index.  They're rarely updated, but rarely isn't never; rarely isn't the same as "impossible".  The surrogate key can't be changed; and doesn't need to be, since no one can see it except the DBA and developers.



What about "CRUD-Level Stored Procedures?"  Create Retrieve Update Delete (CRUD) rules depends on context.  You can claim that each table should be wrapped by stored procedures to implement the CRUD rules.  By so doing, you might be breaking up the relational mapping.  For example, you may have a subclass associated with it's superclass via a 1:1 join.  The CRUD for the subclass now covers two tables.



"Okay, How about CRUD rules for the entities?" is the response.  But isn't that what our object class definitions are for?  Are we now going to duplicate code in "CRUD-level" stored procedures plus class definitions in Java?  Nope.  No CRUD-level stored procedures.



It's Already Here™ and We're Holding A Hammer™ Arguments
---------------------------------------------------------



The **It's Already Here**\ ™ argument goes like this.  Since the RDBMS is already here, we may as well use it.  We paid for all these features.



The **We're Holding A Hammer**\ ™ argument is the traditional view that holding a hammer means we treat each problem like a nail.  



Neither are very compelling.  Just because it's here, doesn't mean it solves our problem.  Just because we're comfortable using it, doesn't mean it is particularly helpful.



My Peers are Jerks
-------------------



This one took the cake.  Here's the email subject line: "What belong in data model and what belong in OO model ?"  After several more emails, there surfaced a horror story about three separate problems.



1.  The programming was so bad that the programmers refused to use the data model.  They insisted that RI constraints either be turned off deferred.



2.  The data modeling was so bad that the programmers couldn't understand it.  The DBA's were forced to turn the RI constraints off or defer the checks.  Nothing quite so much fun as DB2 tables in Check Pending state for a day or two.



3.  The organization was so bad that the programmers and the DBA couldn't coexist except by strange passive-aggressive attacks.  "My code is optimal and involves the least effort on my part; your constraints must permit this application design" -- "My data model is optimal and involves the least effort on my part; your code must conform to this model".



Babies and Bathwater
---------------------



Up front I alluded to a context so twisted and bizarre that it's a little hard to sort out what was going on.  Here's the context.



The DBA who either was a jerk or was enduring the ineptitude of programmers who were jerks, claimed that the important lesson learned was the following:



"Since then, I always delay my RI checking until the commit is issued."



So a bad organization leads to a strange, purely technological work-around to bad software, bad database design or both.  Later, our constraint-relaxing DBA tried to make this point to a DB2 user.  In DB2, they don't seem to have Oracle's flavor of constraint deferral.  Indeed, our DBA is told by the DB2 user that the organization doesn't make heavy use of RI.



So, now our DBA is feeling half-way down the slippery slope of damnation.  Clearly, RI is essential.  Yet, this DBA was punished into turning it off, and then met someone who (gasp!) says that RI isn't even essential.



I Was Told To Do The Wrong Thing
--------------------------------



Everyone's pressured to do something technically dumb.  Here's my response:  I recognize that there's correct design, and then there's things that you do even though the people paying the bills are wrong.  The most important thing about being pressured to do something wrong is the following.



1.  Everyone makes mistakes.  In this case, you happen to know in advance that this is a mistake.  Most people don't find out for years that they did something wrong.



2.  Every implementation has significant flaws.  In this case, it isn't a product of ignorance and you have a better alternative.  Most implementations won't be examined critically for years.  And even then, they will be examined by outside consultants and everyone deprecate their assessment as being a blatant attempt to win the conversion/rewrite/renovation business.



3.  Every manager who is out of touch with the users (and their use cases) as well as the technology still has one thing left that they understand: the schedule.  Using the schedule as a `management trump card <{filename}/blog/2005/09/2005_09_15-essay_11_management_trump_cards.rst>`_  is generally bad.  In this case, you happen to foresee the consequences of bad decision-making.  Most times it's only in hindsight that you see the mistake.



Imagine what this situation will look like in a few years.  Pretend you just walked in to find this mess in production.  Pretend you're that someone who will be asked to find a better approach.  Someone who will be asked to document the potential improvements.  Someone who will be asked to make the business case that the mistakes are more costly to preserve than they are to fix.



Faced with blindly stupid organization or managerial pressure, just do the following:  Start writing down the situation that someone else will discover in the future.  Document what the response should be to straighten it out.  Be factual, precise, and provide plenty of examples.  Don't play the blame game; it isn't helpful.  Don't fall into the trap of providing cost, schedule, ROI or other information that management uses to stall or deny a project.  Just document the mistake and the fix.



Provide it to your replacement when you leave.




