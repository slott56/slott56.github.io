Get this to "Work"
==================

:date: 2007-08-27 10:16
:tags: architecture,design
:slug: 2007_08_27-get_this_to_work
:category: Architecture & Design
:status: published







What I knew was this: I had a program, and I was supposed to make it work.  I went to a meeting, the responsibility was duly handed off to me.  "Alex has it mostly done, you just need to pitch in and help finish this by Friday."



Okay.  



I listened, patiently, hoping to get some sense of what it was supposed to do.  Eventually, it became clear that it was supposed to read a file, write a file and put stuff into a database.  It imported some fancy classes from elsewhere in the enterprise that created some new fields in the records of the file.



What Is The Result?
--------------------



I consider persistence to be more-or-less sacred.  You have to take it very, very seriously.  This program wrote a record **and**  inserted it into a database.  Was this just dumb belt-and-suspenders stuff?  Did they not trust the database?  Or, did was the file used by some other application, separate from the database?  Both ideas made me crazy.



If it was belt-and-suspenders, they needed to think carefully about their database choices.  If you can't trust a database, why use it for mission-critical data?  



If the data went both to the database and to other applications that couldn't connect to the database, they needed to think carefully about their database choices.  If you can't use a database, why are we putting data into it?



The program produced two outputs, which could -- under fairly ordinary circumstances -- be shown to be different.  All you have to do is a re-run and the database timestamps may not match the filesystem timestamps.  What does "works" mean when you can easily doubt the results?



Some Testing
------------



The program was small, and a few of the classes had tests.  I've learned (in `Tools Aren't the Answer <{filename}/blog/2006/08/2006_08_04-tools_arent_the_answer.rst>`_ ) that even abstract superclasses and interfaces need test cases.  So, I'd have to add those to the test suite to be sure that things really "worked".



Interestingly, most of the program was piled into the class with public static void main in it.  This is typical clumsy design.  It makes a bunch of interesting parts of the program static, and forces them into one method, main, which is famously hard to reuse.  The main method has an interface that's often difficult to live with.  Who wants to make a properties file just to call the method named "main" of some other class.  Why not just call well-defined interface methods?



Of course, this main program is a royal pain to write unit tests for.  Of course, there were none.



Documentation
-------------



The best part about this is the lack of usable documentation. There were no documented requirements, and no overall design.  There was word-of-mouth and code.



I demanded a written specification.  The customer called a meeting.  I said that I didn't work well with oral requirements; I needed something written.  Their leadership called our Account Executive to cuss me out for requiring things in writing.   



The Account Executive told me that I was being even more of a jerk than usual by asking for written specifications.  I reminded the AE that verbal requirements are merely an opening for `plausible deniability <http://en.wikipedia.org/wiki/Plausible_deniability>`_ .  I could already hear the conversation.



Them: "You bums didn't get our software to work on time."



Us:  "What do you mean by 'work'?"



Them:  "Idiots!  You went to the meetings.  You should know."



Us:  "You're right, obviously.  We think it works.  Our recollection of the meetings tells us it works."



Them:  "But it doesn't.  It doesn't do [X]"



Us:  "I don't recall that being discussed."



That doesn't make for a good relationship with a client.



Preventing Disaster
-------------------



I would prefer to prevent the whole debacle.  But how do you ask for reasonably clear specifications when they clearly refuse to write things down?



Me: "I need to know what it does."



Them: "We'll tell you during testing when it doesn't work."



Me: "How about you tell me now?  That would prevent waiting until test time to learn what it was supposed to do."



Them: "We can't."



Me: "Okay.  Imagine that it failed a test.  What is the most important test?  What would be the biggest mistake on my part."



Them:  "Not meeting the deadline date."



Structural Issues
------------------



No specifications.  A structure unsuited for unit testing.  Incomplete unit tests.  Both file and database outputs.



And that's just the beginning.  The first week we were told that there's a central stored procedure call.  The procedure hasn't been written, doesn't have a defined API, but it is central.  We were also told the procedure had existed for a long time.  It either didn't exist or did; either way, no one could provide us an API.



This week we found that the procedure returns a result set of multiple rows.  This is a devastating change to the cardinalities already written into the program.  The program assumed a kind of 1 row in-1 row out process.  



It turns out that it's more like the following:  A cluster of *n*  related rows come in; a common attribute is used to execute a stored procedure which returns a result set of *n*  related pieces of data.  Somehow the *n*  rows in the result set are correlated with the *n*  input rows.  What if the cardinalities differ?  Arrgh.



Can Anything Good Come Of This?
--------------------------------



Let's look at the outcomes.



**We get something to "work" on time.**
    They hate us forever because we weren't up to the task, and only their constant nagging made the thing work.



**We get something to "work" after the deadline.**
    They hate us forever because we didn't make the date.



**We get something that almost "works" by the deadline.**
    They hate us forever because they have to think about what actually matters in this application.



**We give up now.**
    They hate us forever for not even trying.





