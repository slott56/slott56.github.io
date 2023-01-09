Multiprocessing and Shared Objects [Revised]
============================================

:date: 2012-01-18 05:48
:tags: #python,multiprocessing
:slug: 2012_01_18-multiprocessing_and_shared_objects_revised
:category: Technologies
:status: published

Read this: `Shared Counter with Python
Multiprocessing <http://eli.thegreenplace.net/2012/01/04/shared-counter-with-pythons-multiprocessing/>`__.

Brilliant.  Thank you for this.

Too many of the questions on StackOverflow that include multi-threading
are better approached as multi-processing.  In Linux, there are times
when all threads of a single process are stopped while the process (as a
whole) waits for system services to complete.  It's a consequence of the
way select and poll work.  An example of the kind of sophisticated
design required to avoid this can be found
`here <http://www.kircher-schwanninger.de/michael/publications/lf.pdf>`__.

Most I/O-intensive applications should be done via multi processing,
not multi threading.

And.  The kind of shared objects that multi threading allows are often
rare and require locks.

So, simplify your life.  When you hear about "threads", replace the word
with "processes" and move on.  The implementation will be much nicer.

The standard gripe is that process creation is so expensive, and thread
creation is relatively cheap.  All true.  That's why folks use process
pools: to amortize the creation cost over a long period of operation.



-----

According to my tests, forking in python (under li...
-----------------------------------------------------

Nick Craig-Wood<noreply@blogger.com>

2012-01-17 09:52:33.728000-05:00

According to my tests, forking in python (under linux) takes about 3.5
times as long as creating a thread. Forking takes about 600 microseconds
on my machine which is quite quick though ;-)
So use processes - they are cheap!

::

    import sys
    import os
    from time import time
    import threading

    def nop():
        """Do nothing"""
        pass

    def fork_test(n):
        """
        Print time to create and destroy n forks
        """
        start = time()
        for i in xrange(n):
            pid = os.fork()
            if pid == 0: # child
                nop()
            os._exit(0)
            os.waitpid(pid, 0) # join
        elapsed = time() - start
        print "That took %.3f seconds for %d iterations, %.3fms / fork" %
        (elapsed, n, elapsed*1E3/n)

    def threading_test(n):
        """
        Print time to create and destroy n threads
        """
        start = time()
        for i in xrange(n):
            tid = threading.Thread(target=nop)
            tid.start()
            tid.join()
        elapsed = time() - start
        print "That took %.3f seconds for %d iterations, %.3fms / thread" %
        (elapsed, n, elapsed*1E3/n)

    def main():
        if len(sys.argv) != 2:
            print "Syntax: %s " % sys.argv[0]
            raise SystemExit(1)
        iterations = int(sys.argv[1])
        fork_test(iterations)
        threading_test(iterations)

    if __name__ == "__main__":
        main()

(Can't figure out what sort of markup to post that code with - sorry!)


I couldn&#39;t agree more. I moved from multi-thre...
-----------------------------------------------------

SteveO<noreply@blogger.com>

2012-01-12 13:42:36.714000-05:00

I couldn't agree more. I moved from multi-threading to multi-processing
ASAP with 2.6 and life's wonderful. I use it extensively to parallel
process data from hundreds of servers in multiple data centers.


No, threads do not generally block the whole proce...
-----------------------------------------------------

Adam<noreply@blogger.com>

2012-01-12 16:04:15.544000-05:00

No, threads do not generally block the whole process unless they do an
operation that requires the whole process to block (which are
well-known). This simple test program demonstrates this pretty well:
http://pastebin.com/cAhfNB5K
Increase the iterations to a large number and notice in top(1) that it
happily eats up 2 CPUs without any trouble, yet spends almost all of its
execution in kernel space, since it's just making the kernel copy
buffers back and forth. top(1) will likely indicate the process is
sleeping too!

Threads would be much more useless if every syscall blocked the whole
process, even if only when the syscall was actually executing in kernel
space.

Even in Python, where the global interpreter lock prevents threads from
executing Python code concurrently, concurrent I/O is typically possible
since the GIL is usually released before an I/O operation begins and
reacquired after it completes. It is true in Python, that
multiprocessing will probably let you fan out wider than
multi-threading, but that is due the GIL and not the characteristics of
the underlying operating system.

The overhead of creating processes is often quoted as a reason to avoid
them, but it's really a falsehood. Both threads and processes are
generally too expensive to create on-demand, so well written threaded
code will generally use a thread pool[1].

The common reasons for choosing multiple threads over processes are:

\* Memory is shared by default, instead of shared explicitly.

\* The overhead of concurrency constructs is typically lower with threads[1].

\* The memory overhead per thread of execution may be much lower.

\* Some operating systems only support certain concurrency constructs under a threaded model.

\* Some operating systems lack fork(), making it difficult or impossible to spawn a copy of a running program. Portable programs and languages may prefer threads for this reason alone.

[1] In Linux, the difference between the two isn't very large. Thread
and processes really aren't very different at all from the perspective
of the kernel (A clone(2) is a clone(2)). However, not all operating
systems are Linux and things weren't always this way.



Adam<noreply@blogger.com>

2012-01-12 16:03:43.972000-05:00

This comment has been removed by the author.


While I agree with the principle of what you&#39;r...
-----------------------------------------------------

Shane Hathaway<noreply@blogger.com>

2012-01-12 14:37:00.571000-05:00

While I agree with the principle of what you're saying, it is quite
incorrect to say that Linux stops all threads while the process (as a
whole) waits for system services to complete. In reality, Linux is very
good at executing multiple threads concurrently, both application code
and system services.

What gets in the way is Python's GIL, which prevents multiple threads of
an application from accessing Python objects simultaneously.


Cool, thanks for mentioning my post :-) It was act...
-----------------------------------------------------

Eli Bendersky<noreply@blogger.com>

2012-01-18 10:25:08.730000-05:00

Cool, thanks for mentioning my post :-) It was actually born from seeing
this kind of questions on SO too often.

Make sure to read the follow-up post on using multiprocessing instead of
threading for CPU-bound tasks. I also plan additional posts on
multiprocessing in the near future.


Your very minor revision does nothing to correct y...
-----------------------------------------------------

Adam<noreply@blogger.com>

2012-01-13 16:26:55.741000-05:00

Your very minor revision does nothing to correct your post. To be
honest, I'm not even sure I'm entirely correctly that there are any
operations left that require the whole process to block simultaneously.
Regardless, such operations are things like fork(2), exit(2), and
possibly some signal related activities. If your multithreaded
application is doing these things with any regularity, it's broken
anyway.

There's not even a good way to do what you claim happens within the
kernel: there's no singular magic lock you can hold that will suddenly
stop a process and all of its threads from executing in kernel space
(outside of things like the historical BKL that locked the whole kernel
for everything). There isn't even a single lock for the whole
task_struct anymore.

As a result, I believe that the kernel typically iterates through the
list of tasks and locks each one individually when it needs to modify
several in a group, possibly also locking the list itself to prevent
mutation where necessary. However, such locking could also effect code
using multiple processes, since processes are also tasks. Remember, the
Linux kernel doesn't treat threads very differently from processes--it
only does so where POSIX demands it do so.

Tasks shouldn't block other tasks unless they're contending for the same
resource. Avoiding that in a multithreaded application is hardly
difficult.


You revised it again and you&#39;re still totally ...
-----------------------------------------------------

Adam<noreply@blogger.com>

2012-01-26 08:00:28.581000-05:00

You revised it again and you're still totally wrong! Calling select()
nor poll() in one thread does not cause other threads to block, nor does
the paper you cited say that. The only case where multiple threads
calling select() might see additional blocking is when their waitsets
share FDs (i.e., two threads are waiting on the same FD).

All the paper says is that using select() and poll() in multiple threads
with shared waitsets can cause synchronization issues for your
application. Moreover, if I were to attempt the design mentioned in your
paper with multiple processes, the same problems would still occur. The
issue isn't threads, the issue is attempting to access the same socket
from multiple tasks simultaneously without properly synchronizing access
to the socket and the socket's state. All you need to do to test is call
fork(): file descriptors are shared across processes by default!

The problems discussed by the paper are entirely a consequence of their
decision to use select() and/or poll(). Other designs lack these
problems entirely. Blocking I/O with one thread per FD is a perfectly
viable design on Linux and is quite common in Java applications. It can
even lead to superior performance in a lot of cases
(http://www.mailinator.com/tymaPaulMultithreaded.pdf) and is certainly
easier to manage and program in many ways. Even in their design, the
only time that you'll see all threads blocked is when all FDs are idle,
which is something that /you want to happen/.

Though even with their design (which is essentially a variant on the I/O
completion port model provided by Windows), if there's enough work to be
done per I/O request, you won't see all of the threads blocking.

At this point, without actual kernel source code demonstrating your
claims, you really need to issue a full retraction. You really should
issue an apology, too. Your behavior with this issue and refusal to
engage directly is way less than professional and what is expected.





