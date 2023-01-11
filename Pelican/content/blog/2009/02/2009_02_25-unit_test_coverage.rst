Unit Test Coverage
==================

:date: 2009-02-25 20:22
:tags: architecture,design,unit testing,tdre
:slug: 2009_02_25-unit_test_coverage
:category: Architecture & Design
:status: published







Unit test coverage is a politically sensitive issue.



If you don't like (or want) unit testing, you set the threshold really high.  100% code coverage, or worse, 100% logic path coverage.  Since these goals are difficult to achieve, the whole unit testing business can be made to go away.



If you're struggling with quality issues, and you just want things fixed, you can also demand some kind of 100% coverage number as a "stretch goal".  This may not be a bad thing.  Unless, of course, you have no unit testing at all, then it's intimidating.



Pragmatic Testing
------------------



Pragmatically, you really want to test the logic paths you'll encounter during "normal" operations.  That is the 97% coverage of non-exception, non-crazy, non-edge cases.



Yes, it's subjective.



No, it can't be actually measured.  



Think about the metric issue.  If I do 100% logic path coverage -- every single path -- every exception -- everything -- I'm pretty sure my software will be rock solid.  



But if I miss say 3% of the edge cases, what does that mean?  Will my software "not work"?  Will it be "unacceptably buggy?"  Unlikely.  



The 100% coverage doesn't correlate with anything else I can measure.  50% test coverage doesn't mean the system is half buggy, or runs half the time, or looses half the transactions, or processes each transaction only half-way through.  No, 50% test coverage means half the system is rock solid and the other half is probably really good, also.



Gut Check
----------



Here are some "is there enough testing?" gut check questions.



1.  Would you refactor it?  This is the most basic level of test coverage -- enough to refactor.



2.  Would you immediately blame installation, operations, maintenance, support -- anyone else -- or would you dig in to find the problem?  This is a higher-level of coverage.  Enough that you're sure it's an installation issue.



3.  If the customer was a psycho and took you to court, and you had to provide testimony, do you have any hard evidence that things essentially work?  Not absolute 100% proof, but some evidence to back up your claim that you think it works and the customer's a whacko.  This is still a higher-level because you have to explain it to civilians and lawyers.



4.  Would you use it as an example a training class on testing?  This is the highest level -- knowledgeable peers.





