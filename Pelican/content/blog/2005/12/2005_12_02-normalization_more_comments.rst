Normalization - More Comments
=============================

:date: 2005-12-02 03:02
:tags: architecture,design,data structure,algorithm
:slug: 2005_12_02-normalization_more_comments
:category: Architecture & Design
:status: published





Fragmentation &amp; similar is sometimes a
storage problem in I/O generated, vs. the gross space consumed. This distinction
didn't leap out at me.



Performance
degradation and storage expansion are closely related, but only for certain
kinds of queries.  Full table scans are penalized by sparsely used storage. 
Individual row retrievals, however, aren't as badly penalized.  Oracle's
row-chaining does penalize even a single-row retrieval, but this is a problem
unique to Oracle.



Normalization can
have a performance payoff from row-level locking if your locking scheme in the
DBMS engine is correct. Spread things all over hell's creation and you get more
frequent blocks, deadlocks, and live-locks. Didn't see
this.



Concurrency and concurrent
performance are more sensitive issues, not really amenable to empirical study. 
Yes, this does need to be mentioned.  However, in the cases that will be
examined, normalization has little locking benefit.  Typically, the MESS problem
means that we were not clear on what the entity was to begin with.  Once
normalized, there will likely be transactions that will lock several of the
normalized tables and increase the possibility of deadlock.  Generally, a
standard from-clause ordering will reduce problems.  The decomposition, however,
should include a recognition that that MESS was bad design; there really are
separate entities, and separate transactions with separate business rules.




Related to the locking, update
anomolies are less frequent as you normalize. This is a big winner, and one of
the biggest as the concurrent users'
scales.



Yes, Normalization is
Necessary.  However, the original MESS uni-table was created because update
anomalies weren't possible for other business reasons.  A close study of the
keys might reveal that update anomalies were a theoretical possibility, but no
update in the application would ever create inconsistent data.  Further
normalization wouldn't change that, since the business view is one of a
uni-table.








