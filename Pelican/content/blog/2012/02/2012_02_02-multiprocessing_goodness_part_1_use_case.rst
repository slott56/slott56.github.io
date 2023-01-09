Multiprocessing Goodness -- Part 1 -- Use Case
==============================================

:date: 2012-02-02 08:00
:tags: #python,architecture,multiprocessing
:slug: 2012_02_02-multiprocessing_goodness_part_1_use_case
:category: Technologies
:status: published


The advantage of multiprocessing is to have multiple processes working
on a problem.  If we break a big problem into small, concurrent steps,
we can often get results in less elapsed time by making more effective
use of the CPU.  Specifically, we want to make use of non-user time
where our process might be waiting for something on the network or
waiting for physical I/O to finish.

There are limits on the speedup offered by multiprocessing.  Once
utilization gets to 100%×cores, we can't go any faster.  However,
there are numerous processes that do a lot of I/O or a lot of network
access; we can use Python's
`multiprocessing <http://docs.python.org/py3k/library/multiprocessing.html>`__
module to make more effective use of our CPU.

The easiest approach to multiprocessing is to use the shell's pipeline
philosophy.  Break the processing up into small steps, each of which
reads from a source stream and writes to an output stream.  The
long-standing tradition here is to read from \`sys.stdin\` and write
to \`sys.stdout\`.  The multiprocessing module, however, gives us
tools to achieve this with relatively little pain.

Rather than use a simple pipe, however, we need to use a
  `multiprocessing.Queue <http://multiprocessing.Queue/>`__.  In shell
  parlance we might have ``func1 | func2 | func3``.

For multiprocessing purposes, we'd have something a hair more complex
looking.

::

       q1 = Queue()
       q2 = Queue()
       p1 = Process( target=func1, kwargs=dict(output=q1))
       p2 = Process( target=func2, kwargs=dict(input=q1, output=q2))
       p3 = Process( target=func3, kwargs=dict(input=q2))
       p1.start()
       p2.start()
       p3.start()




While wordy, it hints at a more generalized approach to have three
processes passing data.

**Termination**

The issue is one of termination.  Most multiprocessing packages (like
multiprocessing and celery) presume that your processing pipeline has
a fairly long lifetime.  Because of this, it presumes that you can
determine that it's idle and kill it off one process at a time.

This isn't a bad assumption, and probably covers a large number of use
cases.

It doesn't, however, cover the simple shell-like ``func1 | func2 | func3`` use case very well at all.

Why not?

Because we can't easily tell when a queue is shutdown for good and
all.  A producing process can close a queue, but that's not a piece of
information that shows up at the consumer end of the queue.

Queues are designed to be durable and have multiple produces.  There's
no easy way to know a Queue is no longer needed.  Each producer would
have to attempt to close the Queue **and** the Queue would have to
know the intended number of producers.  If processes are dynamic, then
the number of producers may not have a fixed, known-in-advance limit.

The approach, therefore, is to put a sentinel object in the queue.
This way, a consumer knows that production has finished.  It can
release resources and exit politely.

**Fan-Out and Fan-In**

The problem with a sentinel on a multi-producer queue is that there
will be multiple sentinels, one from each producer.  And, of course,
with a multi-consumer queue, there must be one sentinels for each
consumer.

If producers adhere to a sentinel-per-consumer rule, and consumers
know to expect a sentinel-per-producer, then we can easily create
dynamic multi-processing networks that startup and shutdown quickly
and cleanly.

**Use Case**

Here's a use case.  We want to do **whois** analysis on IP addresses
in a log.

If we have a simple loop to parse the log and do a **whois** request
on each host IP address, the processing will be slow.  It uses
approximately no CPU, since it spends almost all of it's time waiting
for input from the log, waiting for whois, or waiting for buffers to
be written in the output file.

If we make a simple three-step pipeline ``(parse | whois | report)``
then we get some improvement in elapsed time, but -- really -- the
**whois** step is killing the throughput.

What we need is a way to run a dozen **whois** requests concurrently.
This leads us to multiprocessing, fan-out and fan-in.

Here's what we want.

::

   def analyze_ip( logs ):
       user_queue = Queue()
       report_queue= Queue()
       
       user_from_log= ProducerProcess( name='book_users', target=book_users, args=(logs,), output_queue=user_queue, consumers=12 )
       user_from_log.start()
       
       workers= []
       for worker in range(12):
           get_details= ConsumerProducerProcess( name='user_whois', target=user_whois, kwargs=dict(LIVE=False),
           input_queue=user_queue, output_queue=report_queue, producers=1, consumers=1 )
           get_details.start()
           workers.append(get_details)
       
       report= ConsumerProcess( name='final_report', target=final_report, 
           input_queue=report_queue, producers=12 )
       report.start()
                   
       user_from_log.join()
       for w in workers:
           w.join()
       report.join()


This will do a number of concurrent **whois** requests, tying up lots
and lots of resources and (hopefully) saturating the CPU with real
work.

This shows a fan-out from one **ProducerProcess** to a dozen
**ConsumerProducerProcess** instances.  It shows a fan-in from
the **ConsumerProducerProcess** to a single **ConsumerProcess** that
writes the final report.

This is trivially scaled up (or done) by changing the number of
processes in the middle.

What's important is that the actual functions involved (book_users,
user_whois and final_report) are relatively trivial generator
functions that consume source data (log files or queue entries) and
produce results (queue entries or a report file.)

Also important is the fact that it closes down cleanly.  When the
input reaches end-of-file, sentinel values are put into the queues to
trickle through and lead to orderly process shutdown.



-----

This statement is nonsense for any definition of &...
-----------------------------------------------------

Adam<noreply@blogger.com>

2012-02-02 18:54:15.044000-05:00

This statement is nonsense for any definition of "user" that I can think
of: "Specifically, we want to make use of non-user time where our
process might be waiting for something on the network or waiting for
physical I/O to finish." Time spent sleeping isn't considered "non-user"
time in the wall clock sense nor the accounting sense. Just saying
something like, "Multiprocessing allows for lengthy computations to be
performed simultaneously, or for an application to wait on multiple I/O
resources simultaneously. Simultaneous processing can reduce the total
real-world time it takes to complete a program. Accomplishing this
requires structuring your program so that each lengthy computation or
I/O access proceeds independently of the other tasks in the
application," is considerably more clearer and more accurate.

Your statements about multiprocessing and Celery are also problematic.
multiprocessing makes no assumptions about your tasks because it's a
general purpose module. Celery is based around durable queues, so the
lack of producers doesn't mean anything to a consumer--there may never
be a finish point.

It'd be far more accurate to say, "We need to terminate, or join, our
child processes when we are done with all processing tasks. A simple
queue does not provide any mechanism to indicate when all producers have
finished putting data into the queue. One way to solve this problem is
to put in a special data record, called a sentinel, that indicates the
end of input."

Your example function leaks resources. All of them, in fact, under the
right conditions.


Also, one hopes you&#39;ve carefully considered ho...
-----------------------------------------------------

Adam<noreply@blogger.com>

2012-02-02 19:24:00.144000-05:00

Also, one hopes you've carefully considered how to handle the case where
a producer or consumer exits prematurely...





