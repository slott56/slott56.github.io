Multithreading -- Fear, Uncertainty and Doubt
=============================================

:date: 2011-06-07 14:10
:tags: threads,software design,code-kata,queue
:slug: 2011_06_07-multithreading_fear_uncertainty_and_doubt
:category: Technologies
:status: published

Read this: "`How to explain why multi-threading is
difficult <http://programmers.stackexchange.com/questions/81003/how-to-explain-why-multi-threading-is-difficult/81008#81008>`__".

We need to talk. This is not that difficult.

Multi-threading is only difficult if you do it badly. There are an
almost infinite number of ways to do it badly. Many magazines and
bloggers have decided that the multithreading hurdle is the Next Big
Thing (NBT™). We need new, fancy, expensive language and library
support for this and we need it right now.

`Parallel Computing <http://en.wikipedia.org/wiki/Parallel_computing>`__ is the
secret to following Moore's Law. All those extra cores will go unused
if we can't write multithreaded apps. And we can't write
multi-threaded apps because—well—there are lots of reasons, split
between ignorance and arrogance. All of which can be solved by
throwing money after tools. Right?

Arrogance
---------

One thing that makes multi-threaded applications error-prone is
simple arrogance. There are lots and lots of race conditions that can
arise. And folks aren't trained to think about how simple it is to
have a sequence of instructions interrupted at just the wrong spot.
Any sequence of "read, work, update" operations will have threads
doing reads (in any order), threads doing the work (in any order) and
then doing the updates in the worst possible order.

Compound "read, work, update" sequences need locks. And the locations
of the locks can be obscure because we rarely think twice about
reading a variable. Setting a variable is a little less confusing.
Because we don't think much about reads, we fail to see the
consequences of moving the read of a variable around as part of an
optimization effort.

Ignorance
---------

The best kind of lock is not a mutex or a semaphore. It surely isn't
an RDBMS (but God knows, numerous organizations have used an RDBMS as
a large, slow, complex and expensive message queue.)

The best kind of lock seems to be a message queue. The various
concurrent elements can simply dequeue pieces of data, do their tasks
and enqueue the results. It's really elegant. It has many, simple,
uncoupled pieces. It can be scaled by increasing the number of
threads sharing a queue.

A queue (read with an official "get") means that the reads aren't
casually ignored and moved around during optimization. Further, the
creation of a complex object can be done by one thread which gets
pieces of data from a queue shared by multiple writers. No locking on
the complex object.

Using message queues means that there's no weird race condition when
getting data to start doing useful work; a get is atomic and
*guaranteed* to have that property. Each thread gets an thread-local,
thread-safe object. There's no weird race condition when passing a
result on to the next step in a pipeline. It's dropped into the
queue, where it's available to another thread.

Dining Philosophers
-------------------

The `Dining Philosophers <http://en.wikipedia.org/wiki/Dining_philosophers_problem>`__
Code Kata has a queue-based solution that's pretty cool.

A queue of Forks can be shared by the various Philosopher threads.
Each Philosopher must get two Fork resources from the queue, eat,
philosophize and then enqueue the two Forks again. It's quite short,
easy to write and easy to demonstrate that it *must* work.

Perhaps the hardest thing is designing the Dining Room (also know as
the Waiter, Conductor or Footman) that only allows four of the five
philosophers to dine concurrently. To do this, a departing
Philosopher must enqueue themselves into a "done eating" queue so
that the next waiting Philosopher can be seated.

A queue-based solution is delightfully simple. 200 or so lines of
code including docstrings comments so that the documentation looked
nice, too.

Additional Constraints
----------------------

The simplest solution uses a single queue of anonymous Forks. A
common constraint is to insist that each Philosopher use only the two
adjacent forks. Philosopher *p* can use forks :math:`p+1 \mod 5` and
:math:`p-1 \mod 5`.

This is pleasant to implement. The Philosopher simply dequeues a
fork, checks the position, and re-enqueues it if it's a wrong fork.

FUD Factor
----------

I think that the publicity around parallel programming and
multithreaded applications is designed to create Fear, Uncertainty
and Doubt (FUD™).

#.  Too many questions on StackOverflow seem to indicate that a slow
    program might magically get faster if somehow threads where
    involved. For programs that involve scanning the entire hard drive
    or downloading Wikipedia or doing a giant SQL query, the number of
    threads has little relevance to the real work involved. These
    programs are I/O bound; since threads must share the I/O resources
    of the containing process, multi-threading won't help.

#.  Too many questions on StackOverflow seem to have simple message
    queue solutions. But folks seem to start out using inappropriate
    technology. Just learn how to use a message queue. Move on.

#.  Too many vendors of tools (or languages) are pandering to (or
    creating) the FUD factor. If programmers are made suitably
    fearful, uncertain or doubtful, they'll lobby for spending lots of
    money for a language or package that "solves" the problem.

Sigh. The answer isn't software tools, it's design. Break the
problem down into independent parallel tasks and feed them from
message queues. Collect the results in message queues.

Some Code
---------

::

     class Philosopher( threading.Thread ):
         """A Philosopher.  When invited to dine, they will
         cycle through their standard dining loop.

         -   Acquire two forks from the fork Queue
         -   Eat for a random interval
         -   Release the two forks
         -   Philosophize for a random interval

         When done, they will enqueue themselves with
         the "footman" to indicate that they are leaving.
         """
         def __init__( self, name, cycles=None ):
             """Create this philosopher.

             :param name: the number of this philosopher.  
                 This is used by a subclass to find the correct fork.
             :param cycles: the number of cycles they will eat.
                 If unspecified, it's a random number, u, 4 <= u < 7
             """
             super( Philosopher, self ).__init__()
             self.name= name
             self.cycles= cycles if cycles is not None else random.randrange(4,7)
             self.log= logging.getLogger( "{0}.{1}".format(self.__class__.__name__, name) )
             self.log.info( "cycles={0:d}".format( self.cycles ) )
             self.forks= None
             self.leaving= None
         def enter( self, forks, leaving ):
             """Enter the dining room.  This must be done before the 
             thread can be started.

             :param forks: The queue of available forks
             :param leaving: A queue to notify the footman that they are
                 done.
             """
             self.forks= forks
             self.leaving= leaving
         def dine( self ):
             """The standard dining cycle: 
             acquire forks, eat, release forks, philosophize.
             """
             for cycle in range(self.cycles):
                 f1= self.acquire_fork()
                 f2= self.acquire_fork()
                 self.eat()
                 self.release_fork( f1 )
                 self.release_fork( f2 )
                 self.philosophize()
             self.leaving.put( self )
         def eat( self ):
             """Eating task."""
             self.log.info( "Eating" )
             time.sleep( random.random() )
         def philosophize( self ):
             """Philosophizing task."""
             self.log.info( "Philosophizing" )
             time.sleep( random.random() )
         def acquire_fork( self ):
             """Acquire a fork.

             :returns: The Fork acquired.
             """
             fork= self.forks.get()
             fork.held_by= self.name
             return fork
         def release_fork( self, fork ):
             """Acquire a fork.

             :param fork: The Fork to release.
             """
             fork.held_by= None
             self.forks.put( fork )
         def run( self ):
             """Interface to Thread.  After the Philosopher
             has entered the dining room, they may engage
             in the main dining cycle.
             """
             assert self.forks and self.leaving
             self.dine()

The point is to have the dine method be a direct expression of the
Philosopher's dining experience.  We might want to override
the acquire_fork method to permit different fork acquisition
strategies.
For example, a picky philosopher may only want to use the forks
adjacent to their place at the table, rather than reaching across the
table for the next available Fork.
The Fork, by comparison, is boring.

::

  class Fork( object ):
      """A Fork.  A Philosopher requires two of these to eat."""
      def __init__( self, name ):
          """Create the Fork.

          :param name: The number of this fork.  This may 
              be used by a Philosopher looking for the correct Fork.
          """
          self.name= name
          self.holder= None
          self.log= logging.getLogger( "{0}.{1}".format(self.__class__.__name__, name) )
      @property
      def held_by( self ):
          """The Philosopher currently holding this Fork."""
          return self.holder
      @held_by.setter
      def held_by( self, philosopher ):
          if philosopher:
              self.log.info( "Acquired by {0}".format( philosopher ) )
          else:
              self.log.info( "Released by {0}".format( self.holder ) )
          self.holder= philosopher

The Table, however, is interesting.  It includes the special
"leaving" queue that's not a proper part of the problem domain, but
is a part of this particular solution.

::

  class Table( object ):
      """The dining Table.  This uses a queue of Philosophers
      waiting to dine and a queue of forks.

      This sets Philosophers, allows them to dine and then
      cleans up after each one is finished dining.

      To prevent deadlock, there's a limit on the number
      of concurrent Philosophers allowed to dine.
      """
      def __init__( self, philosophers, forks, limit=4 ):
          """Create the Table.
          :param philosophers: The queue of Philosophers waiting to dine.
          :param forks: The queue of available Forks.
          :param limit: A limit on the number of concurrently dining Philosophers.
          """
          self.philosophers= philosophers
          self.forks= forks
          self.limit= limit
          self.leaving= Queue.Queue()
          self.log= logging.getLogger( "table" )
      def dinner( self ):
          """The essential dinner cycle:
          admit philosophers (to the stated limit);
          as philosophers finish dining, remove them and admit more;
          when the dining queue is empty, simply clean up.
          """
          self.at_table= self.limit
          while not self.philosophers.empty():
              while self.at_table != 0:
                  p= self.philosophers.get()
                  self.seat( p )
              # Must do a Queue.get() to wait for a resource
              p= self.leaving.get()
              self.excuse( p )
          assert self.philosophers.empty()
          while self.at_table != self.limit:
              p= self.leaving.get()
              self.excuse( p )
          assert self.at_table == self.limit
      def seat( self, philosopher ):
          """Seat a philosopher.  This increments the count 
          of currently-eating Philosophers.

          :param philosopher: The Philosopher to be seated.
          """
          self.log.info( "Seating {0}".format(philosopher.name) )
          philosopher.enter( self.forks, self.leaving)
          philosopher.start()
          self.at_table -= 1 # Consume a seat
      def excuse( self, philosopher ):
          """Excuse a philosopher.  This decrements the count 
          of currently-eating Philosophers.

          :param philosopher: The Philosopher to be excused.
          """
          philosopher.join() # Cleanup the thread
          self.log.info( "Excusing {0}".format(philosopher.name) )
          self.at_table += 1 # Release a seat

The dinner method assures that all Philosophers eat until they are
finished.  It also assures that four Philosophers sit at the table
and when one finishes, another takes their place.  Finally, it also
assures that all Philosophers are done eating before the dining room
is closed.



-----

Sometimes, even when its a black box, people get t...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-06-07 19:26:30.802000-04:00

Sometimes, even when its a black box, people get themselves into
trouble. The classic example that I have run into is Oracle parallel
execution. Just to show that "its not just me", check out
Expert Oracle Database Architecture: 9i and 1…
by Thomas Kyte

Chapter 14: Parallel Execution

Section: When to Use Parallel Execution

"Parallel execution is essentially nonscalable solution. It was designed
to
allow an individual user or a particular SQL statement to consume all
resources
of a database. If you have a feature that allows an indiividual to make
use of
everything that is available, and then you allow two individuals to use
that
feature, you'll have obvious contention issues."





