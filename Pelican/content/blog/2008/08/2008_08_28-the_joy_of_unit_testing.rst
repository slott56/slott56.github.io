The Joy of Unit Testing
=======================

:date: 2008-08-28 09:46
:tags: architecture,software design,unit testing,test-driven reverse engineering
:slug: 2008_08_28-the_joy_of_unit_testing
:category: Architecture & Design
:status: published







The customer sent a screen grab from an accounting desktop application with a couple of rows highlighted. They claim that the application I reverse engineered from C and rewrote in Java didn't work for this one case.



Step 1.  Get clarification on the screen grab information.  The data labels don't match any of the 100's of unit test cases that we put together.



Step 2.  The clarification remains incomplete, but time is passing, so I make some guesses and build a unit test case.  This case is a lot like the cases in spreadsheet X page Y-Z, so I copy the most similar method from that TestCase to create a new TestCase.  Yes, this is copy-and-paste reuse.  Yes it's bad.  



I fold in the new test case from the screen grab as best I can.  



Run it.



Step 3.  Originally, I had planned on step 3 being a day of debugging to either (a) find a super-subtle logic flaw or (b) find that this test case was so different from all others that **We Have To Talk**.  The (b) case is surprisingly common.  Lots of people imagine the scope of the application as being something it isn't.  Often they lift up something that's not a complex edge or corner case; they single out something that is way out in left field.



Many business operations require people to make judgements.  It's common.  It's the thing software doesn't do well, and shouldn't do.  Many people routinely spend a long, boring day making essentially the same judgement call over and over again.  Often, this isn't a good candidate for automation because -- well -- software can't discuss or justify it's judgement.  



Today's step 3, however, was to send back the new test case.  It worked for me.  If it doesn't work for you, then there are two potential issues: (a) you changed something, or (b) I didn't transform the screen grab into a test case properly.



In the case of (b), you could say that this unprofessional of me.  I *should* be able to translate their screen grab into a proper test case.  However, I think that there's an interface between users and developers and creating spreadsheets in a standard form should be their job.  I have hundreds of cases they already created in standard spreadsheets.  They should be able to maintain those spreadsheets, adding new cases.



I have a tool (800 lines of Python) to build Java JUnit TestCase classes from their spreadsheets.  That's my side of the interface.



Bottom Line
------------



Bug -> TestCase rules.  It's the best.




