Threads and I/O
===============

:date: 2011-09-27 18:58
:tags: performance,design,architecture
:slug: 2011_09_27-threads_and_io
:category: Technologies
:status: published

| Threads don't promote concurrent I/O.
| Kernel threads may.  Most of us write user threads.  Here's a great
  summary under `Thread (Computer
  Science) <http://en.wikipedia.org/wiki/Thread_(computer_science)>`__.

   However, the use of blocking system calls in user threads (as opposed
   to kernel threads) or fibers can be problematic. If a user thread or
   a fiber performs a system call that blocks, the other user threads
   and fibers in the process are unable to run until the system call
   returns. A typical example of this problem is when performing I/O:
   most programs are written to perform I/O synchronously. When an I/O
   operation is initiated, a system call is made, and does not return
   until the I/O operation has been completed. In the intervening
   period, the entire process is "blocked" by the kernel and cannot run,
   which starves other user threads and fibers in the same process from
   executing.

| 
| The point is this.
| **If it involves I/O, multi-threading doesn't help.  Processes do.**
| If it involves computation, multi-threading may help.





