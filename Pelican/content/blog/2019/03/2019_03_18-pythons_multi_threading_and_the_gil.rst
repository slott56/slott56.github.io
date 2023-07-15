Python's multi-threading and the GIL
====================================

:date: 2019-03-18 07:36
:tags: dask,#python,multiprocessing,threads
:slug: 2019_03_18-pythons_multi_threading_and_the_gil
:category: Technologies
:status: published


Got this in an email.

   "Python's multi-threading module seems not efficient because of the
   global interpreter lock?"


Yep.
         
    Is the trick is to use "`Thread-Local
    Data <https://docs.python.org/3/library/threading.html#thread-local-data>`__"?


Nope.

It Gets Worse
-------------


Interestingly, there was no further ask. The questioner had decided on
thread-local data because the questioner had decided to focus on
threads. And they were done making choices at that point.

Sigh.

No question on "What was recommended?" or "What's a common solution?"
or "What is `Dask <http://docs.dask.org/en/latest/why.html>`__?"
Nothing other than "confirm my assumptions."

This is swirling around a bunch of emails on trying to determine the
**maximum** number of concurrent threads or processes based on the
number of cores or CPU's or something.

**Maximum**.

I'll repeat that for those who skim.

They think there's a **maximum** number of concurrent threads or
processes.

If you have some computation which (1) makes zero OS requests and (2)
is never interrupted, I can imagine you'd like to have all of the
cores fully committed to executing that theoretical stream of
instructions. You might even be able to split that theoretical
workload up based on the number of cores.

Practically, however, that stream of **uninterrupted** computing
rarely exists.

Maybe. Maybe you've got some basin-hopping or gradient-following or
random forest ML algorithm which is going to do a burst of computation
on an in-memory data structure. In that (rare) case,
`Dask <http://docs.dask.org/en/latest/why.html>`__ is still ideal for
exploiting all of the cores on your processor.

The upper-bound idea bugs me a lot.

-  Any OS request leads to a context switch. Any context switch leads to
   waiting. Any waiting means you can have more threads than you have
   cores.

-  AFAIK, any memory write outside the local cache will lead to a stall
   in the pipeline. Another thread can (and should) leap in to the
   core's processing stream. The only way you can create the
   "all-computing" sequence of instructions bounded by the number of
   cores is to \*also\* be sure the entire thing fits in cache.
   Hahahaha.




What's the maximum number of threads or processes? It depends on the
wait times. It depends on memory writes. It depends on the size of the
data structure, the size of cache, and the size of the instruction
stream.

Because it depends on a lot of things, it's rather difficult to
predict. And that makes it rather difficult to determine a maximum.

Replying about the uselessness of trying to establish a **maximum**,
of course, does nothing. AFAIK, they're still assiduously trying to
use os.cpu_count() and os.sched_getaffinity() to put an upper bound on
the size of a thread pool.

Acting as if `Dask <https://docs.dask.org/en/latest/>`__ doesn't
exist.

Solution
--------

Use `Dask <https://docs.dask.org/en/latest/>`__.

Or

Use a `multiprocessing
pool <https://docs.python.org/2/library/multiprocessing.html#using-a-pool-of-workers>`__.

These are simple things. They don't require a lot of hand-wringing
over the GIL and Thread Local Data. They're built. They work. They're
simple and effective solutions.

Side-bar Nonsense
-----------------

   From "a really smart guy. He got his PhD in quantum mechanics and he
   got major money to actually go build … . He initially worked for ...
   and now he is working for .... So, when he says something or asks a
   question, I listen very carefully."


The laudatory blah-blah-blah doesn't really change the argument. It
can be omitted. It is an "Appeal to Authority" fallacy, and the
Highest Paid Person's Opinion (HIPPO) organizational pattern. Spare
me.

Indeed. Asking for my confirmation of using Thread-Local Data to avoid
the GIL is -- effectively -- yet another Appeal to Authority. Don't
ask me if you have a good idea. An appeal to me as an authority is
exactly as bad as appeal to some other authority to convince me you've
found a corner case that no one has ever seen before.

Worse is to ask me and then blah-blah-blah Steve Lott says
blah-blah-blah. Please don't.

I can be (and often am) wrong.

Write your code. Measure your code's performance. Tell me your
results. Explore \*all\* the alternatives while you're at it.



-----

Perhaps the individual was struggling to formulate...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-03-13 08:34:39.085000-04:00

Perhaps the individual was struggling to formulate and clearly
articulate his problem?

Perhaps the individual was trying to figure out how to throttle an
application so computations are available for other things?

Something like use x cores for batch processing and use the other y for
interactive day to day activities.


The link provided for "Using a pool of worker...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-03-13 08:21:44.461000-04:00

The link provided for "Using a pool of workers" refers to Python 2.
The link for Python 3 is below
https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers





