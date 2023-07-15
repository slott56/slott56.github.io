Parallelism Fetishes. #1: Equal-Sized Partitions
================================================

:date: 2008-05-12 12:10
:tags: architecture,database design,data structure,algorithm,concurrency
:slug: 2008_05_12-parallelism_fetishes_1_equal_sized_partitions
:category: Architecture & Design
:status: published







Let's talk about parallel processing, something I prefer to call concurrent processing.  It shows up in many places.  Most OS's have concurrent processes.  Applications like Apache have concurrent threads within a process for handling web requests.  Oracle not only handles concurrent queries from multiple users, but you can define a table to use parallel physical structures, further promoting concurrency.



I got an email asking about Oracle's Partitioned Table structure.  The email used unbound terms like "Good", "Better" and "Advantageous".  This kind of question is unanswerable, making it difficult to be helpful.  Indeed, these questions have a mysticism about them that I can't cope with.



First (and foremost) architecture solves problems.  Without a specific, tangible problem, there is no architecture and there is no architectural recommendation.  That's absolute and final.  You can't ask about parallelism in a vacuum with no specific application.  In general, technology -- by itself -- is boring.  If you aren't applying it to a problem, it's just ideas.  The idea of 13 being a non-prime number, for example, is just an idea.  A partitioned table, similarly, is just an idea.  So what?  The question is "What are you trying to accomplish?"



Second, "Better" doesn't have a generic binding.  "Better" is only meaningful in the specific context of a quality dimension to optimize.  Most of the time, "Better" means "Less": "Less Cost", "Less Time", "Less Memory", "Less I/O".  Sometimes "Better" means "More": "More Adaptable", "More Maintainable", "More Auditable", "More Secure", etc.  Lacking any specific optimization criteria, the idea of a partitioned table is fine.  Or too much work.  Or essential to success.  I can't tell from words like "Better".



Answers
--------



To focus the conversation, I asked, specifically, which "Less" they were interested in.  "Less Time", "Less Memory", or "Less I/O".  I specifically said "Pick One".  Here's the answer I got: "Thanks for explicitly listing them.".  Seriously.  No answer of any kind.  Sigh.



Failing that, I tried to lift up the ideas of "empiricism" and the "scientific method":  do some research, form a conjecture, make a prediction, run some experiments.  This is covered nicely in Wikipedia's entry on `Scientific Method <http://en.wikipedia.org/wiki/Scientific_method>`_ , and this article on `Epistemology <http://webspace.ship.edu/cgboer/epist.html>`_ .  Here's the answer I got: "So, I picked an approach. I will take finger to keyboard and see what I get.".  Seriously.  No theory, no prediction, no comparison, just coding one partitioning approach.  Sigh.



It appears that this was someone for whom "Science" doesn't apply; someone for whom mysticism is better than empiricism.  It appears that I can't really help much there.  I don't have a strong enough background in mysticism.



Concurrency Modeling
--------------------



Let's try empiricism and see if that works.  Here's the simplest possible model -- no communication among the processes.  We'll have *n*  concurrent processes.  Let's keep it simple, and say *n* = 4.  Let's call the processes a, b, c and d.



There are two ways to run these four processes.  Trivially expressed by the following two shell scripts, called Serial and Parallel.



Serial.  
    ``a; b; c; d``



Parallel.  
    ``a & b & c & d``



Let's examine the possible run-times.



Serial:
    a.time + b.time + c.time + d.time



Parallel:
    max( a.time, b.time, c.time, d.time )



Which is less?  By definition, parallel must run in less time than serial.  Conclusion?  Parallel always results in less run time.  Unless of course, 3 of the 4 processes are degenerate cases and run in zero time.  Then serial == parallel.



And that's pretty much all you need to know.



Want details?  Write four shell scripts which consist of "sleep *n*" for different values of *n*.  Run the two versions.  Measure the time.  Write a loop to run each version 128 times and average the results.



What did we do?  Theory, Prediction, Experiment.



Context Switching Fetish
-------------------------



The **True Student of OS** will cry foul at the above analysis.  The Student will claim that Parallel programs somehow involve more overhead than Serial programs because the OS must interleave the executions of multiple processes.



This may have been true -- 20 years ago.  When I was a kid, serial meant the OS was otherwise doing NOTHING.  Parallel meant interleaved concurrent execution -- and concurrency was some kind of special case.  Today, all OS's are doing hundreds of things concurrently even when they're just idling.  The context-switch overheads are essentially fixed.  The only way you can even notice the overheads is to introduce boat-loads of new processes.  Right now, I've got 60 processes running, and I'm just writing.  Running one more process or four more processes is not a measurable change in the number of context switches being managed.



Equal-Sized Workloads
----------------------



Let's look Oracle's table partitioning.  This is the same as having different workloads for our *n* = 4 concurrent processes.  To make it easy on the brain, get a deck of playing cards (or Tarot cards, since we're looking at mysticism of parallelism).



Cut the deck into four piles.  Make no effort at equality.  Just cut and allocate into four piles: a, b, c and d.



Now, to simulate Oracle's physical I/O operations, deal batches of 3 cards into the middle of the table.  Pick 3 cards off a, 3 cards off b, 3 cards of c, 3 cards off d.  That's one quantum of time.  Repeat, counting one quanta of time for each 3-card deal.



When you're nearly done, some pile will run out of cards.  This parallel partition finished early.  When you're completely done, all piles will be out of cards.  How many quanta of time did it take?  There's a theoretical maximum and minimum.  Work this out before reading further.





-----------





Hint: For Tarot cards the minimum is 20 quanta.  The maximum is 78 quanta.



Want more details?  Do this a few dozen times, creating a spreadsheet with your results.  From your randomization experiments, get the average, standard deviation, best and worst cases.  These will be clustered around the middle of the theoretical extremes.



So, the best case is about 1/4 of the worst case.  *n* = 4.  Hmmm.   Pattern?



Unequal Workloads
------------------



Here's were the fetish kicks into high gear.  If equal workloads leads to minimal time, what's the impact of unequal workloads?  How much fetishizing can we do to keep the workloads equal?



Here's a great version of that question: "Oracle partitions are balanced when they have approximately the same number of rows. For the sake of argument lets quantify "approximately" as plus/minus 3 percent.".



*Three*  percent.  Question: Where did this number come from?  Answer: fetishizing.



Let's think.  Time depends on physical I/O's.  So, we really care about blocks, not rows.  How may rows per block determines how close "approximately" means.  If the rows are small (e.g., 0.5K bytes) and the blocks big (e.g., 32K bytes), then ±64 rows is still precisely the same-sized partition.  As a percentage, 64 rows could be 100% or nearly 0%.  



Blocks are harder to count than rows.  Indeed, Oracle's use of blocks is quite confusing, so their documentation suggests using number of rows; for large tables it's as misleading as anything else.  For small tables, why are we bothering?



How Unequal Before We Notice?
------------------------------



Well, we're back to the business problem, at this point.  We need to know "how fast is fast enough?"  If one partition is too slow, then four partitions, even if radically different in size will be faster.  It will be as fast as the largest partition.  



Do they have to be equal-sized?  **No**.  The only requirement is that the largest partition's processing time fit within our time box.



Do we need "optimal" run time?  **No**.  We need to meet the requirements.  If we can partition equally, that's nice, but hardly worth any brain calories.



There's no "Best"
-----------------





"Yes, but," some folks say; they want a "best" answer.



Equal-sized partitions will minimize run time.  At the cost of figuring out which combination of keys splits rows equally.  You will add complexity elsewhere to determine how to precisely equalize the partitions.  Ask yourself if the cost-benefits are there.



BTW, you can explore your data without doing too much work.  SELECT COUNT(*), x FROM t GROUP BY x; is all you need to do to locate combinations of keys and their relative partition sizes.



You *never*  need "minimal", you only need "good enough to make people happy."  You can fetishize over endless partitioning keys.  Have fun.



If you don't have a required query run time, you're just wasting time and money playing Oracle.  You can "put finger to keyboard" if it makes you happy.  Hopefully, you're just doing a few COUNT(*) GROUP BY's to get some answers.  If your employer enjoys it enough, you can squander a lot of time on hand-wringing followed by pointless POC's that show one approach with no theoretical framework to act as a basis for comparison.



If you have a required query run time, and you are looking for a partition that meets it, you're solving problems.



Hold The Phone
---------------



The wise reader will say "This isn't that hard; I can just assign a surrogate partition number to each row, and guarantee equality."



Yep.  It's that simple.  A basic ``count % n`` will assign a number, *k*, :math:`0 \leq k < n` , that can be the partition number.  That is the bottom line: searching among natural keys and other attributes is a waste of time and money.  Just compute a partition number at load time and be done with it.  Or you can fetishize about it.




