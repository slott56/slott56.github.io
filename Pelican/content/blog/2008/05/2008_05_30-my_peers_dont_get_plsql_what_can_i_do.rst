My Peers Don't Get PL/SQL, What Can I Do?
=========================================

:date: 2008-05-30 00:29
:tags: architecture,design,complexity
:slug: 2008_05_30-my_peers_dont_get_plsql_what_can_i_do
:category: Architecture & Design
:status: published







The email from a developer starts with a complaint and moves on to a plea: "I am constantly having to look at "IF o_status = 0". Code would be a lot more compact and easy to read if exceptions were used.
Request favor: Please consider blogging about using exception handling vs "IF o_status = 0". " 



At this juncture, it's not clear what the developer's goal is.



1.  Fix the if o_status = 0 stuff that they're constantly having to look at.



2.  Fix the organization to improve their programming.



2a.  Help them use exceptions instead of badly nested if-statements.



2b.  Help them ditch PL/SQL for something faster and simpler.  Example: Java.



3.  Vent about the peer group's shoddy programming.



Here's why the goal is confusing.  The email goes on to include a reference to Chapter 7 of the PL/SQL User's Guide and Reference, `Handling PL/SQL Errors <http://download-east.oracle.com/docs/cd/B10501_01/appdev.920/a96624/07_errs.htm#8858>`_ .  Since the information is already in the email, what more can I offer?  Nothing.



Finally, the email ended with the following: "However, it would be nice to have a discussion of "IF status = 0" vs exception handling discussed from an architectural perspective. After all Java has exception handling."  What?  From an architectural perspective, PL/SQL is a fundamental mistake.  It spreads application software around between application servers and the database server.  Yuck.



Let's pretend we're aiming at "fixing" the organization minimally -- just get them to use exceptions.  The "architectural perspective" is ridiculous, since PL/SQL creates more problems than it solves.



:strong:`The Argument`





Unless you make it a condition of employment, programmers have a number of reasons for NOT changing from many if-statements to exceptions.



1.  It's "costly" to change.  The "disruption" adversely impacts quality or productivity or something.  [I put the terms in quotes because -- if you ask -- there's no detail supporting the disruption claim.  Mostly, it's all code for "I don't want to learn something new right now."]



2.  Exceptions are confusing.  They force you to scroll down to read the exception block, which is bad.  Endless if-statements mean that the error handling is adjacent to the relevant statement.  And using nested blocks to wrap each statement with exception handling adjacent is "too much syntax."



3.  Exceptions are slow/memory intensive/bad in some other way.  [This is, of course, anecdotal; there's never any actual benchmark.]



4.  Exceptions don't capture some nuance of the algorithm.  [Clearly, the if-statements aren't working either -- or we wouldn't have this email in the first place!]



What can our developer do in the face of these kinds of stonewalling arguments?





:strong:`Techniques That Don't Work`



Technique one: provide the PL/SQL reference manual pages.  They did that.  Apparently, that just fueled the argument.



Technique two: Appeal to Authority.  For example, referencing a blog posting.  This will lead people to do nothing.  Odds are good that no one will read a blog in the first place.  A blog posting is exactly as valuable as the Oracle PL/SQL User's Guide pages -- pages already provided.  



How does a blog posting change things?  Generally, it makes the argument shift slightly to include the blog author.  



Given a blog posting, the programmers will add point #5 to their argument against exceptions:



5.  That blogger didn't get the nuances of our culture/experience/application domain/technology stack.  



Technique Three: how about a few False Dichotomies?  Make up some all or nothing situation where if-statements after the SQL statement are bad.  How about "You're not using all features of the language.  Therefore, you shouldn't use the language?"  Use all of the PL/SQL features or drop the language and switch to Java.



Good advice.  Wrong "reason".  (If you can call a false dichotomy a reason.)



Providing information (manual pages, blog postings, etc.) doesn't work.  Okay they're informed.  They still have 5 solid reasons for not changing (it's costly, it's confusing, it performs poorly, it misses some nuance, it doesn't fit our culture/tech stack). 



:strong:`Actually Do The Work`



One way to act as an agent of change is to :strong:`Actually Change Something`.  Not talk about change possibilities or inform people of better courses of action, but actually do something.  If you're constantly having to look at some crap code, you must be doing maintenance or enhancement.  



If you're reading the code with intent to change, think about the long-term cost of having the next maintainer (or enhancer) read that code.  Save everyone a lot of money by doing two things.



1.  Reverse Engineer some Unit Tests for this offensive piece of code.



2.  Refactor the Module.



"Oh," people say, "that's too costly." [Really?  Is it also confusing, performs poorly, misses some nuance and doesn't fit your culture?  If so, you're just as much part of the problem as your peers who won't change.]



"Can't," people say, "I'm not authorized to rewrite it."  Got it.  You want change without actual sweaty labor.  Excellent.  Change without any work is about 4lbs of pixie dust at $1,000 per gram.  That'll change everyone without any work on your part.  And it'll buy me a Bentley.



"It's not 'politically correct' around here to make waves like that."  Okay.  I won't make waves.  I won't do anything, either.  Clearly, your job is not to add value by improving the enterprise's software asset.  Since you're not doing something so obviously valuable, you must be doing something more valuable.  Keep doing whatever it is that's more valuable than reducing the cost of the legacy code and quit complaining.   



[BTW, the 'we don't have time to fix legacy problems' is a false economy, but every IT manager I've ever met has said it emphatically.  I've been asked to scope and plan the replacement of 20- and 30-year old COBOL applications that are breaking the back of the organization.  The plans were, of course, shelved because reducing costs "doesn't create enough value for our end-users."  Got it, the customer insists that limping along with 60% of the organization supporting old crap :emphasis:`does`  create value.]



:strong:`Suggestion`



Actually Do Something.  Just fix the code.  "How will I know it works?" you ask.  That's why step one was to create unit tests.  Step two is to refactor the code.



Read Larry O'Brien's `30K + 100K = success or failure? <http://www.sdtimes.com/content/article.aspx?ArticleID=32059>`_  column.  Unit testing works.  And people complain about it.  [Example Complaint: " time spent writing a test function is time that could be used on application code" -- what?  That's insane because you can't distinguish between application and test: test is essential to making the application "work".]



Read `Test-Driven Development and Software Quality <http://www.dzone.com/links/testdriven_development_and_software_quality.html>`_  in DZone (amongst other places.)  The point is that unit testing allows you to simplify.  Applications with unit tests are measurably simpler.  In this case, the exception handling folderol is a punishing kind of cycolmatic complexity that is reduced (but not eliminated) through exception handling.



So:  Develop unit tests.  Refactor.



Then, brag about the success to your peers.  Carping, complaining and nagging don't work.  Leading by example might work.




