Python's Duck Typing Not General Enough; SQL's Minimally Typed Foreign Keys Not General Enough.  Debugging Hilarity Ensues.
===========================================================================================================================

:date: 2008-02-05 02:24
:tags: architecture,design,complexity
:slug: 2008_02_05-pythons_duck_typing_not_general_enough_sqls_minimally_typed_foreign_keys_not_general_enough_debugging_hilarity_ensues
:category: Architecture & Design
:status: published







The money quote was this "It’s not a big leap then for me to consolidate all three of those into one uber relationship table...".



The question was a good one because it involved the classic higher-order database relationship.



The canonical SQL relationships are binary equi-join relationships that can be implemented with simple foreign keys.  An example design is a Group and the Members of the group is the most common example because it is a nice 1 Group to many Members relationship.  All of the Members have foreign keys that refer to the Group to which they belong.



A SQL many-to-many relationship is binary, but doesn't work out as trivially.  In this specific case, we're scheduling events for specific groups.  An event has many groups, a group participates in many events.  Clearly, a single foreign key isn't going to work.



The standard SQL hack is to have a many-to-many association table that links events and groups.  The association is a collection of foreign-key pairs.  Each foreign key, however, participates in a simple binary relationship.



Wrong Way To The Next Level
----------------------------



Once we start talking about groups of people, participating in events, at specific times and places, we have higher-order relationships.



Something that actually appears as a valid schedule entry has at least four independent dimensions.  We have one or more groups, one time, one place, and one "activity" (lecture, lab, workshop, field trip, whatever.)  This isn't a binary relationship, it's a fourth-order relationship.  It will be higher when you also track individual people (like instructors) in addition to groups.



If you start looking at this as a bunch of binary many-to-many relationships, you can easily get yourself into a **Rat-Warren of Design Details**\ ™.



The list of associations in the email included ActivityToGroup, ActivityToPlace, ActivityToTime, GroupToPlace, GroupToTime, etc.  In essence they had enumerated all possible pairs from the underlying 4th order relationship.



Once the architect had identified all of those binary relationships, they wanted to refactor all of them into a single Uber-Meta-Association class.  Django imposes a number of restrictions, which seemed onerous.  Even SQL's foreign keys imposed too many restrictions.  Python's duck typing didn't seem flexible enough.



The Attractive Nuisance
-----------------------



There are many attractive nuisance features of Python and Django.  Duck Typing -- for example -- can burn up a lot of brain calories.  You begin to think of a class to define an association between objects.  A class to define the attributes of objects.  Wait, what?



My suggestion was to rethink all those pair-wise foreign key relationships.  Most of them, in isolation, are meaningless because they aren't unique.  Yes, Group X participates in Activity 101.  in 3 locations at 3 separate schedules.  Almost all the many-to-manys are just a subset of one fourth-order relationship.



Yes, flexibility is possible.  However, Python already provides the Uber-Meta-Association; that's what Duck Typing IS. 



In SQL, you could collapse a lot of binary many-to-many relationships into a generic many-to-many table.  Django wouldn't like this because Django likes more structure in the database.  To make sense of the uber-meta association table, you'd need to know which "base" tables were connected on each side of the relationship.



Wait.  Wouldn't that base table identification be a kind of type declaration?  Can't you just to that in Django directly?



My Advice
----------



Step 1, lay off the coffee.  Too much thinking about creating generic generalizations of abstractions doesn't build useful software.



Step 2, use higher-order associative relationships.  4th or 5th order relationships work beautifully.



Step 3, build something small that works.  Get the test cases right.  Get data loaded.  It's relatively easy (in Django) to spin up a new app that is derived from an old app but adds new features.  You convert that data, switch the urls.py file and you're up and running with new features.  



Here's the model I proposed which eliminated all of the many-to-many relationships, replacing them with a single, higher-order relationship.





..   image:: {static}/media/EventModel.png
    :alt: EventModel.png



Don't over-solve the problem you have.



You've already made your application "future-proof".  Further design effort to make this even more general isn't going to be too helpful.  You've already done the right thing by choosing high-powered tools like Python and Django that make it easy to implement a new architecture.  




