Database Design and UML - What was the question again?
======================================================

:date: 2007-12-15 13:08
:tags: management
:slug: 2007_12_15-database_design_and_uml_what_was_the_question_again
:category: Management
:status: published








One issue in creating a database design is working around the limitations inherent in the SQL data model.  I'm going to call it the SQL model because you can make the case that the entity-relationship (ER) model is an abstraction and could have a far more expressive implementation.  I'm going to claim that the SQL implementation introduces some limitations.  Ironically, the issue is getting database designers to recognize this. 


Here's the lead-off question: "What do you think of Scott Ambler's approach to using UML to do ERD's?" 

This is a reference to the 
`Object-Relational Impedance Mismatch  <http://www.agiledata.org/essays/impedanceMismatch.html>`_
article.  The question is a little out-of-phase because the article isn't about UML 
:emphasis:`per se` .  It's about ORM, it just happens to use UML.  But, I guess the question is really "Is Ambler showing a good example of using UML for doing E-R design?" 



My response was pretty rude.  The trivial answer is "Yes".  But there had to be something else going on.  I also asked how you could justify NOT using a standard like UML? 



Regarding context, it's important to note that the query comes from an All-Singing-All-Dancing-All-Oracle kind of person.  So the ERD question is focused on producing relational database SQL.   


See 
`Over-Solving the Problem  <{filename}/blog/2006/06/2006_06_20-over_solving_the_problem_or_when_your_architect_is_a_dba.rst>`_
and 
`Lenses that Distort our Software <{filename}/blog/2007/11/2007_11_03-lenses_that_distort_our_software_flat_files_relational_databases_batch_processing.rst>`_ .  Architecture should be larger than answering the "how do we use the database?" question.  But some DBA's reduce everything to database and SQL.


The question is unlikely to be this silly and trivial.  The answer is "Yes," but the follow up is "What did you really mean?" 

:strong:`Richness of Notation` 


Using UML -- for anything -- presents two problems. 


First, UML is very rich; it can depict things you have a hard time implementing. 


Second, UML is very rich, and it isn't obvious what subset of the notational alternatives are appropriate to what you're trying to depict. 



A UML class diagram can show a lot of things.  Specifically, UML is biased toward showing object-oriented class definitions, with attributes as well as methods.  You can, of course, try and limit yourself to just enough notation to define a SQL database.  However, you're missing a lot of opportunities for clarifying the problem and bracketing alternative solutions. 


In summary, rich notation gives you a way of visualizing the real problem.  The real world is complex and messy.  Rich notation is essential for describing the world as we find it.   

:strong:`The Politics Question` 


In many organizations, UML is unusable.  First, it's not the classic James Martin Crow's Feet Notation.  For some reason, this notation came out in the early days and has stuck.  Permanently.  ERWin, for example, uses this notation and everyone loves it.  Switching to UML requires leaving the crow's feet behind.  What's the ROI on that kind of change?


A second reason that UML can be unusable is that organizations suffer from some fundamental concept problems.  A database separates a "logical view" from a "physical view".  Most people forget what the physical view is, and do some bizarre things.  UML clarifies the views, but can introduce new terminology.  And who wants their terminology changed? 




ERWin creates the confusion by claiming that the "physical" view is the logical model with vendor-specific names.  This is flat-out wrong.  The physical model is the physical on-disk structures.  In Oracle parlance, the physical model includes the tablespaces and underlying files.  ERWin doesn't even depict this.  UML can show this, however, making this level of design visible. 


ERWin's "logical" and "physical" models are really just a Logical View of data: it maps entities to SQL tables and columns.  ERWin's "logical" model is more accurately termed "Platform Independent Model"; their "physical" model is an "Platform Specific Model".  Some UML tools don't show the PIM vs. PSM comparison well because they aren't as handy at flipping back and forth between models. 


ERWin, as an incumbent, gives us one political viewpoint.  The introduction of new notation and terminology will face a struggle.  Standardization doesn't enter into dislodging the incumbent terminology. 



:strong:`Reality, Objects and Relations` 


The biggest problem -- the one that Ambler was addressing -- was the mismatch between object classes and SQL tables.  The object model is very rich with numerous features for depicting the real world.  The SQL relational model, on the other hand, is rather poor.  A great deal of clever things can be done in the relational world.  In the object world, we don't have to be nearly so clever. 



We have a number of mapping steps here, and I think this is the crux of the question. 


1.  We have users and the real entities they deal with.  Documents or Notices or    Claims or Balances or whatever is the subject of the problem domain. 


2.  We can have an object model.  This is rich with features, and generally has a high fidelity match with the real world.  Some object implementations impose some constraints (like single inheritance) but the UML diagram should capture the problem domain's entities precisely.  


3.  We have a SQL-based model.  This is relatively poor in features, being limited to a few data types and foreign key relationships.   



By using UML, we can depict either model of reality with a great deal of useful precision.   The initial question -- "What do you think" -- doesn't have an interesting answer.  Yes, UML works.  It's hard.  You won't like it for dumb political reasons.   



:strong:`The Real Question` 


A little digging lead to this follow-up question statement:  "Goal: Generate DDL (create table, create FK) from the UML model for various target databases."

So the initial question wasn't "what do you think?" but "Can I engineer my SQL using UML?" 


The answer to this, also, is "Sure" and "What do you really mean by that?"  There are any number of UML design tools with DDL creation features.  A quick Google reveals 
`Magic Draw <http://www.magicdraw.com/>`_
UML and ` <http://www.sparxsystems.com.au/products/index.html>`_ `Sparx  <http://www.sparxsystems.com.au/>`_
Enterprise Architect, 
`IBM-Rational  <http://www.ibm.com/developerworks/rational/library/07/1002_vasudevamurthy/index.html>`_
Business Developer, and `Visual Paradigm  <http://www.visual-paradigm.com/>`_
for UML.  Clearly, they do precisely what is needed.  Why ask me? 




Here's the follow up: 

"Bigger goal: Keep the UML, Java code, and DDL all in sync".


:strong:`In Synch with What?` 



While keeping various models "in synch" is a noble aspiration, it's delightfully vague.  Vague enough that problems inevitably ensue. 



A fundamental problem is that a database design is really a kind of knowledge capture.  We do different kinds of knowledge capture for different purposes.  It's difficult to synchronize all of the knowledge that comprises working software. 



First, we have problem domain knowledge, often called "analysis".  There may be any number of views (logical, process, use case, component) of the problem. 


Second we have solution knowledge, often called "design".  There may be any number of views of the solution, also.  If you search for four plus one views, or Philippe Kruchten, you can find excellent coverage like 
http://www.surfscranton.com/Architecture/ApplicationArchitecture.htm
and http://www.ibm.com/developerworks/wireless/library/wi-arch11/


There's a mapping between the two, but they are never isomorphic.  We rarely solve all of the problem.  We may have a solution which is somewhat more general than the original problem, and has bonus features.   



Clearly, to keep all the models in synch, we have to focus on design only or analysis only.  If we pick design only, we have layers of meaning from an abstract solution, a concrete platform independent solution, and a concrete platform-specific solution (i.e., "code"). 


**What Was The Question?**


Can we keep the various design elements in synch?  The answer is almost "Yes".  If it weren't for the shortcomings of the SQL Relational model, it would be easy. 




Sadly, we have this essential problem -- the Object-Relational Impedance Mismatch problem.  The problem stems directly from the limited nature of the SQL relational model.  We have to make intelligent choices in how we are going to work around the limitations of the SQL world.  These choices will clutter up our object model with details that are relevant to the SQL world, but not the Object world. 




Just one example: containment.  In the object world, an object can be a collection and contain other objects.  The container and containees can have mutual references.  The container can have a variety of semantics: list, set or mapping.  (Python people further subdivide list into mutable and immutable variants.)   




The relational world only has a foreign key relationship from containee to the overall container.  The container is -- utterly -- unconscious of the role as container.  The only exception might be the presence of a cascade delete rule. 




I've got a huge conceptual gap between objects and SQL.  To bridge that gap, I have to write code, queries and object-relational maps.  While my Java has one view, my SQL has a considerably restricted view.  My queries might be limited to the SQL view.  Or, depending on the design, they might depend on the more liberal Java view.  In Java, navigation is a simple "." operator or a getter method.  In SQL, navigation is a full-scale SELECT statement or a SELECT statement with JOINS. 




:strong:`The Irony` 


So here's the irony in this long sad story.  The DBA reads Ambler's article about Object-Relational Impedance.  The DBA asks a tangential question about UML.  I press the DBA for details to find that they want some kind of automated maintenance that will eliminate Object-Relational Impedance.  Apparently, they didn't actually read the article that stimulated the question in the first place.  At the end was a reference to 
`O/R Mapping in Detail <http://www.agiledata.org/essays/mappingObjects.html>`_ .


This reference lays out the issues in glorious detail.  It should be clear that there are so many SQL shortcomings that it can't be automated.  The Object and SQL worlds aren't simply two implementations of a model in slightly different syntax.  They're two different designs aimed at solving the same problem; they can't easily be reconciled.  UML has nothing to do with this essential problem.  I'm guessing that my DBA only looked at the pictures. 






