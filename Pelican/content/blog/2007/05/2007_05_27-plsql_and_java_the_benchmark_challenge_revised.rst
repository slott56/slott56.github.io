PL/SQL and Java - The Benchmark Challenge (revised)
===================================================

:date: 2007-05-27 13:07
:tags: architecture,software design,data structure,algorithm,pl/sql,java
:slug: 2007_05_27-plsql_and_java_the_benchmark_challenge_revised
:category: Architecture & Design
:status: published







First, the confusion.  A couple of comments asked for code, offering to "fix" the problems.  Specifically, offering to optimize or improve the PL/SQL.  The code was already posted, but I failed to make that clear.  Here's a recap of the various blog entries on this subject.



1.  `PL/SQL vs. Java - Which is Really Faster? <{filename}/blog/2007/03/2007_03_23-plsql_vs_java_which_is_really_faster.rst>`_



2.  `PL/SQL vs. Java - Additional Information <{filename}/blog/2007/03/2007_03_23-plsql_vs_java_additional_information.rst>`_



3.  `PL/SQL vs. Java - Yet Again <{filename}/blog/2007/05/2007_05_26-plsql_vs_java_yet_again.rst>`_



Sizing
-------



Someone asked how a real-world problem can have so few (only a few thousand) invoices.  The answer is that the customer has a giant table of business records, from which they extract the business records to be processed.  That extraction isn't on the table as part of the overall performance problem.  



It should be.  Indeed, they should have a data warehouse so that they aren't doing extracts of live data from history.  To them, in their real world, that's another problem.



Native Code
-----------



One interesting response lifted up Oracle's PL/SQL Native Compilation technique.  I think they're talking about Oracle® Database PL/SQL User's Guide and Reference, chapter 11, `Tuning PL/SQL Applications for Performance <http://download-east.oracle.com/docs/cd/B19306_01/appdev.102/b14261/tuning.htm>`_ .



While an interesting approach, my customers are unlikely to agree to this as a solution to slowness.  They use PL/SQL precisely because it's flexible.  They like it for the same reasons people like Python -- it's (in effect) a scripting language.  The development overhead of native compilation is daunting.



Java doesn't have the level of complexity (i.e., C compilers, shared libraries, etc.) that this native compilation of PL/SQL has.  That doesn't eliminate the native compilation, it makes it undesirable as a solution.



However, if performance matters, I suppose this needs to to be put on the table.  It is complex -- far more complex than Java -- but it could be considered as a solution.  To run a comparison will take me some time to configure and install this under Fedora Core 6.  I'm not sure I want to go through the agony, when Java is already a solution in hand.



In The Real World
-----------------



[*Digression*\ .  One response included the disturbing magic words "in the real world".  Often I stop reading there, because it's an attempted trump card.  It is a kind of power play; the claim is that the "real world" situation deserves more credence than other situations.  It subverts a useful comparison of constraints and priorities.  Your "real world" is no more real than my "real world"; you have different priorities and different values.  Let's talk about those in detail rather than summarily dismissing my customer's real world as being less real than your real world.]



One response noted that time is lost transferring big chunks of data.  That was specifically what I was trying to avoid in my benchmark.   The client code I was basing this on did not involve big chunks of data.  If the queries did involve big chunks of data, the application might work better in PL/SQL.  The issue centered on queries with small chunks of data; this doesn't work better in PL/SQL.



I didn't make it clear that I'm running a specific benchmark, for which I provided code.  If, in your world, things behave differently, provide the code, post your results.  **Let's see this benchmark**.  



Wrong Algorithm
----------------



One response hinted that I was using entirely the wrong algorithm.  That's an interesting notion.  The claim is that 6 SELECT statements would do the same thing as the two-part business rule I fabricated.  I'm dying to see the 6 SELECT statements.  **Let's see this benchmark**.



What I failed to make clear is that my benchmark is drawn from the situation where the business has a large number of business rules.  Consequently, they a large number of if-statements.  Worse, the if-statements interact with each other, so that you need to (effectively) union all of the rules together and determine the composite predicate for each rule. 



With two rules, it's easy to work out the four conditions that apply.  For *n*  rules, there are 2*n*  predicate combinations that need to be analyzed and optimized.  I'm daunted by the prospect, and don't see how a sizable collection of if-then-else business rules can be optimized into simple SELECTS.



Additional Processing
---------------------



I raised the confusion level by leaving out the updates.  Since I only wanted to illustrate the basic business rules, I took out the update which is an essential operation for each kind of match (and non-match).  This makes the issue more that simple SELECT statements.  



Conclusion
----------



Thanks for the thoughtful comments.  Please post your competing benchmarks so I can see what can be improved in my situation.




