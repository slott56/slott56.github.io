How do I use all my cores?
==========================

:date: 2010-03-15 08:00
:tags: performance,architecture
:slug: 2010_03_15-how_do_i_use_all_my_cores
:category: Technologies
:status: published

News Flash: Multi-core programming is "hard". EVERYBODY PANIC.

ZOMFG: We either need new tools, new languages or both! Right Now!

Here's one example. You can find others. "`Taming the Multicore
Beast <http://chipdesignmag.com/sld/blog/2009/03/27/taming-the-multicore-beast/>`__":

  The next piece is application software, and most of the code that
  has been written in the past has been written using a serial
  approach. There is no easy way to compile that onto multiple
  cores, although there are tools to help.

What?

That's hooey. Application software is already working in a multicore
environment; it has been waiting for multi-core hardware. And it
requires little or no modification.

Any Linux-based OS (and even Windows) will take a simple shell
pipeline and assure that the processing elements are spread around
among the various cores.

**Pipelines and Concurrency**

A shell pipeline -- viewed as Programming In The Large -- is not
"written using a serial approach". Each stage of a shell pipeline
runs concurrently, and folks have been leveraging that since Unix's
inception in the late 60's.

When I do python p1.py \| python p2.py, both processes run
concurrently. Most OS's will farm them out so that each process is on
its own core. That wasn't hard, was it?

I got this email recently:

     Then today, I saw the book

     `Software Pipelines and SOA: Releasing the Power of Multi-Core
     Processing <http://www.amazon.com/Software-Pipelines-SOA-Multi-Core-Processing/dp/0137137974>`__

     By Cory Isaacson

     At that point, I figured that there are a lot of yahoos out
     there that are barking up the wrong tree.


I agree in general. I don't agree with all of Isaacson's approach.
A big ESB-based SOA architecture may be too much machinery for
something that may turn out to be relatively simple.


**Easy Problems**


Many problems are easily transformed into map-reduce problems. A
"head" will push data down a shell pipeline. Each step on the
pipeline is a "map" step that does one incremental transformation
on the data. A "reduce" step can combine data for further maps.

This can be expressed simply as: head.py \| map1.py \| map2.py \|
reduce1.py \| map3.py. You'll use both cores heavily.

**Optimization**


Some folks like to really focus on "balancing" the workload so
that each core has precisely the same amount of work.


You can do that, but it's not really going to help much. The OS
mostly does this by ordinary demand-based scheduling. Further
fine-tuning is a nice idea, but hardly worth the effort until all
other optimization cards have been played. Even then, you'd simply
be moving the functionality around to refactor map1.py \| map2.py
to be a single process, map12.py.

Easy and well-understood.

**Harder Problems**

The Hard Problems involve "fan-out" and "fan-in". Sometimes we
think we need a thread pool and a queue of processing agents.
Sometimes this isn't actually necessary because a simple
map-reduce pipeline may be all we need.

But just sometimes, there's a fan-out where we need multiple
concurrent map processors to handle some long-running, complex
transformation. In this case, we might want an ESB and other
machinery to handle the fan-out/fan-in problem. Or, we might just
need a JMS message queue that has a one writer and multiple
readers (1WmR).

A pipeline has one writer and one reader (1W1R). The reason why
fan-out is hard is that Linux doesn't offer a trivial (1WmR)
abstraction.

Even fan-in is easier: we have a many writer one reader (mW1R)
abstraction available in the
`select <http://linux.die.net/man/2/select>`__ function.

The simplest way to do fan-out is to have a parent which forks a
number of identical children. The parent then simply round-robins
the requests among the children. It's not optimal, but it's
simple.

**Bottom Line**

Want to make effective use of your fancy, new multi-core
processors?

Use Linux pipelines. Right now. Don't wait for new tools or new
languages.

Don't try to decide which threading library is optimal.

Simply refactor your programs using a simple **Map-Reduce** design
pattern.



-----

Just to mention, <a href="http://pypi.python.org/p...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-03-15 19:26:40.124000-04:00

Just to mention, `iterpipes <http://pypi.python.org/pypi/iterpipes/>`__
is a little Python library for running shell pipelines using shell-like
syntax. It is a thin wrapper around the standard subprocess module.
I wrote it initially for system administration, but it fits nicely in
the context you have described.


I like the post, respect the idea, but I don&#39;t...
-----------------------------------------------------

Bala<noreply@blogger.com>

2010-03-19 20:03:33.838000-04:00

I like the post, respect the idea, but I don't think I can agree with
you totally!

What will happen if the process on the right completes before the
process on the left? Your pipe will throw an error. You can ignore/mask
the error, but the point is that IMHO, pipes were constructed for
communicating between processes and not for running things in parallel
(though the latter, to an extent, occurs as a side-effect).





