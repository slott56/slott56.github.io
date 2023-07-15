Not Quite Following the Book
============================

:date: 2007-12-07 21:23
:tags: architecture,software design,unit testing,test-driven reverse engineering
:slug: 2007_12_07-not_quite_following_the_book
:category: Architecture & Design
:status: published







I can't find all of the **Better Software Magazine** articles on the `Sticky Minds <http://www.stickyminds.com>`_  web site, so I can't provide a permalink.  But look for "A Story About User Stories and Test Driven Development".  It's good stuff, weighing out the good and bad features of "by-the-book" TDD.



`Dr. Dobb's Journal <http://ddj.com/>`_  ran and endless series about Agile, Test-Driven Pair Programming, and Java by Robert C. Martin.  Good stuff; it seemed to bracket the ideal, textbook TDD world-view.



What I tend to do isn't precisely the way TDD is usually described.  As Martin characterizes it, design happens as part of refactoring the code.  With deeply experienced people, I suspect that it looks like this is happening.



But reading the articles in Sticky Minds helped me rethink what was really going on.  



Design Still Happens
--------------------



I designed first and felt guilty about it.  Then I read the article by Gertrud Bjørnvig, James Coplien, and Neil Harrison; now I'm not as plagued by guilt.



One of their points is that a good architecture won't happen.  Indeed, you have to clarify the architecture, and be sure that everyone can articulate the architecture before you're going to get anywhere.  The test cases and code will follow this overall architecture.



Here's the important part.  The code must always be fit into an architecture; architecture leads, code follows.  Either you pick it explicitly, or you back into it by having someone -- haphazardly -- arrive at an architecture and start fitting code into that structure.



I've seen this, but never knew precisely what I was seeing.  In a place dominated by mainframe folks, programs tend to process files and relatively few inputs and a reasonable number of outputs.  In a place dominated by Visual Basic programmers, everything has a GUI, even if the GUI just submits batch jobs. In a place `dominated by DBA's <{filename}/blog/2006/06/2006_06_20-over_solving_the_problem_or_when_your_architect_is_a_dba.rst>`_  everything has to be in the database.



The architecture and design is colored by experience and culture.  Left to their own devices, they work with the architecture they're most comfortable with.  If we turn people loose with a "pure" TDD, they'll pick their favorite architecture and work toward that.



Now I Feel Better
-----------------



One big piece of advice was to design first, then write tests, then write code.  Whew!  I had been doing that.  Now I realize it wasn't just me.  There is a gap in the "formal" definition of TDD.  You need to do some design first.



You need to have an architecture, and everyone on the team has to be able to articulate the architecture.  Then the tests and code will fill in the available spaces correctly and consistently.





