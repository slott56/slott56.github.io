Building Skills in OO Design -- Updated
=======================================

:date: 2008-05-31 20:20
:tags: building skills,#python,OO Design
:slug: 2008_05_31-building_skills_in_oo_design_updated
:category: Books
:status: published







The updates to `Building Skills in Object-Oriented Design <http://www.itmaybeahack.com/homepage/books/oodesign.html>`_  cover some notes on testing, Agility and rework, two ongoing themes that can't be emphasized enough.



There were two small updates regarding testability.



First, creating Outcome instances — for testing purposes — does involve an ugly hack of repeating the payout odds.  Since we're developing stand-alone unit tests, this isn't a bad thing.  Later, we'll get Outcomes from the Game, using keys to a mapping of some kind.



Second, our initial version of the Wheel is intentionally naive and untestable.  When we rework it, we really do delete the old code.  And this is an important thing.  Testability isn't always obvious at first, and rework to improve testability is an essential skill.



Agility
----------



There was a small change related to Agility.  This is something that is covered implicitly, and perhaps ought to be brought out more explicitly.



Most things in this simulation live essentially forever.  However, Bets do have to get deleted when they're resolved.  Initially, deleting bets is ignored.  It certainly is possible to add a delete method to the first version of Table.  More fundamentally, there's no compelling reason to add too many features too early in the development cycle.



Frustration
-------------



Some folks noted frustration regarding rework.  This is expected, and I have a few soapboxes and sidebars on the subject of rework.  



The bottom line is that there really is considerable rework in some classes.  For example, the first release of Wheel uses a really poor design, and later rework to make it more testable really does chuck out the initial code.



Rework is essential to the Agile, incremental development approach.  There isn't an easy way to prevent rework.  If I present a "more finalized" design, you don't get to participate fully in the design decisions and their consequences.  



In most cases, the rework involved implementation changes, not interface changes.  This is an essential object-oriented design exercise.  You should always be ready, willing and able to change the implementation of a method.





