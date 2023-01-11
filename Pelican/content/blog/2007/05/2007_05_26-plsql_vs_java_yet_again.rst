PL/SQL vs. Java - Yet Again
===========================

:date: 2007-05-26 14:43
:tags: architecture,design,data structure,algorithm
:slug: 2007_05_26-plsql_vs_java_yet_again
:category: Architecture & Design
:status: published







There appear to be four responses.  Two were numbered, the third is a rambling thought on scalability, and the fourth
is a thought on management's discomfort with the truth.







Response 1 -- Denial
--------------------







"1) How can using Java/... be faster ? You have to go up and down the architectural stack of JDBC over and over and you have the network in between."







Since the code is nearly identical, and the PL/SQL is slower, the "you have to go up and down the architectural stack" part must be false.  Indeed, that was the point of the posting in the first place.  This argument (PL/SQL has to be faster because it's "closer" to the RDBMS) is false.  







"Suggested response: Well, as in any perf. activity, you have to actually benchmark it in your specific env."  







My result shows that "specific env." doesn't matter.  I'm convinced that in all environments PL/SQL will be slower than Java for the same algorithm.  It's slower because (1) the "closer to the RDBMS" statement is false, and (2) the PL/SQL virtual machine can't do JIT optimization.







The **benchmark**  is the critical issue here.  Dogmatic acceptance of the received truth of PL/SQL's performance is a mistake.  Benchmarking is essential when performance matters.







Response 2 -- Negotiation
--------------------------







"2) You did not properly take advantage of PL/SQL"







That was the point.  Some algorithms are basic, transactional Insert-Update-Delete, where PL/SQL is as good as anything else.  Other algorithms, however, involve IF-statements, and PL/SQL doesn't do this well.  







Further -- and this is hard to grasp at first -- RDBMS indexes are slow compared to in-memory Java collections.  Therefore, a Java program has all the advantages.  The RDBMS is good at persistence, transactional locking, and some kinds of ad-hoc query processing.  Focus on that, and put other kinds of large analytical and ETL processes outside the RDBMS.







Response 3 -- Thoughts on Scalability
-------------------------------------







This wasn't part of my point, but it's interesting none the less.







"DB's don't scale... What about RAC, what about multi-master replication ?... Each DB has one and only 1 area that does sorting. ...  just get a  bigger CPU and more and faster disks. ... "







"If *[you?]*  used Java and properly architected the system, just add another cheap PC or another cheap single board computer and you are done."







I suppose that's true.  If your Java application is too slow, you can throw more popcorn processors at the problem.  Indeed, the whole concurrency issue plays into this.  Modern Linux OS's will distribute processes among the processors and cores in multi-core processors, giving your Java applications wonderful levels of concurrent processing.







Response 4 -- Anger
-------------------







"I don't have Java resources or budget to buy more hardware. However, I already paid for the DB and I have people that [know] PL/SQL."







If IT management says (1) performance matters and (2) don't make use of the benchmark results, then you have a serious problem with schizophrenia.  If, on the other hand, IT management doesn't care about performance, then why were you benchmarking in the first place?







If performance doesn't actually matter, PL/SQL is fine.  It's ugly and hard to maintain, but that's what management is all about.  Managers make the "hard" decisions.  For example, managers can elect to use a slow, complex language which is a maintenance nightmare.  But maintenance is paid for with `Next Year's Dollars <{filename}/blog/2007/02/2007_02_18-its_drive_to_self_destruction.rst>`_ , which don't matter.  It's a `Management Trump Card <{filename}/blog/2005/09/2005_09_15-essay_11_management_trump_cards.rst>`_ , and you can't beat it.





