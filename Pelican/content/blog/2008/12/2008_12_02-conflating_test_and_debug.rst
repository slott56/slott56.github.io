Conflating Test and Debug
=========================

:date: 2008-12-02 18:06
:tags: architecture,design,unit testing,tdre
:slug: 2008_12_02-conflating_test_and_debug
:category: Architecture & Design
:status: published







Check out this StackOverflow "question": `Does anyone have metrics on the utility of formal Unit Testing? <http://stackoverflow.com/questions/333922/does-anyone-have-metrics-on-the-utility-of-formal-unit-testing>`_ . While -- technically -- it does have a question, it's more of a rant against formal unit testing than a proper question.



Here's the conflation comment.  "I've worked with developers who never caught any errors in their unit tests."



Apparently, a test which passes initially has no value. 



I think that they're complaining that it has no :emphasis:`debugging`  value.  If it passes, it absolutely has testing value.



:strong:`Debugging and Testing`



A test which fails give us a chance to debug.  It tells us something is broken.



A test which passes could mean anything.



It could means that we wrote the code correctly first, then wrote some tests, and the tests passed because -- well -- we're really good at coding.  



It could also mean that our tests weren't complete enough to find a problem.



Either way, when a test passes, we don't get a chance to debug.



And -- it appears from the conversation on StackOverflow -- no debugging is a bad thing.



:strong:`Good Test, Bad Test`



Note that tests have only two conditions: pass and fail.



Tests aren't benchmarks.  If you want to know how many concurrent transactions before the app fails or becomes too slow to use, that's a benchmark.  Not a test.  



If, on the other hand, you have to handle 40,000 transactions per hour, you have something testable; a test boils down to pass or fail.



I've worked with consultants who claim that benchmarking is part of testing.  I agree that benchmarking might be part of a test :emphasis:`phase`  or test :emphasis:`activity`.  Unless it can fail (and you know the threshold that counts as failure) it isn't a test.  Running it until it breaks isn't "testing".  It's exploring or analyzing or learning or something.  But until there's a way to fail, it isn't testing.



:strong:`Testing and Debugging`



What I've learned recently is that debugging can be done using testing tools.  



Let's say you have an integration test that fails.  The logs and results aren't clear enough to pinpoint a problem.  And -- worse -- no unit test reflects this problem.  That's evidence that you're missing some unit tests.  



Rather than add logging statements or learn to use the debugger, here's what works well.



1.  Hypothesize some error that would pass unit tests and fail integration tests.



2.  Write a new test to plug that gap.



Cycle around those two steps for a while and you both find the problem and build up the test portfolio.




