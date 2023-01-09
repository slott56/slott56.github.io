Multiprocessing Goodness -- Part 2 -- Class Defintions
======================================================

:date: 2012-02-14 08:32
:tags: #python,architecture,multiprocessing
:slug: 2012_02_14-multiprocessing_goodness_part_2_class_defintions
:category: Technologies
:status: published


The
`multiprocessing <http://docs.python.org/library/multiprocessing.html>`__
module includes a generic
`Process <http://docs.python.org/library/multiprocessing.html#multiprocessing.Process>`__
class, which can be used to wrap a simple function.

The function must be designed to work with Queues or Pipelines or
other synchronization techniques.

There's an advantage, however, to defining a class which gracefully
handles generator functions.  If we have Generator-Aware
multi-processing, we can (1) write our algorithms as generators and
then (2) trivially connect Processes with Queues to improve
scalability.

We're looking at creating processing "pipelines" using Queues.  That
way we can easily handle multiple-producer and multiple-consumer
(fan-in, fan-out) processing that enhances concurrency.

See `Multiprocessing Goodness -- Part 1 -- Use
Cases <{filename}/blog/2012/02/2012_02_02-multiprocessing_goodness_part_1_use_case.rst>`__
for more information.

We have three use cases:  Producer, Consumer and Consumer-Producer.

**Producer**

A Producer gets data from somewhere and populates a queue with it.
This is the source that feeds data into the pipeline.

::

   class ProducerProcess( Process ):
       """Produces items into a Queue.
       
       The "target" must be a generator function which yields
       pickable items.
       """
       def __init__( self, group=None, target=None, name=None, args=None, kwargs=None, output_queue=None, consumers=0 ):
           super( ProducerProcess, self ).__init__( name=name )
           self.target= target
           self.args= args if args is not None else []
           self.kwargs= kwargs if kwargs is not None else {}
           self.output_queue= output_queue
           self.consumers= consumers
       def run( self ):
           target= self.target
           for item in target(*self.args, **self.kwargs):
               self.output_queue.put( item )
           for x in range(self.consumers):
               self.output_queue.put( None )
           self.output_queue.close()




This class will wrap a "target" function which **must** be a
generator.   Every value yielded is put into the "output_queue".  When
the source data runs out, enough sentinel tokens are put into the
queue to satisfy all consumers.

**Consumer**

A Consumer gets data from a queue and does some final processing.
Perhaps it loads a database, or writes a file.  It is the sink that
consumes data on the pipeline.

::

   class ConsumerProcess( Process ):
       """Consumes items from a Queue.
       
       The "target" must be a function which expects an iterable as it's
       only argument.  Therefore, the args value is not used here.
       """
       def __init__( self, group=None, target=None, name=None, kwargs=None, input_queue=None, producers=0 ):
           super( ConsumerProcess, self ).__init__( name=name )
           self.target= target
           self.kwargs= kwargs if kwargs is not None else {}
           self.input_queue= input_queue
           self.producers= producers
       def items( self ):
           while self.producers != 0:
               for item in iter( self.input_queue.get, None ):
                   yield item
               self.producers -= 1
       def run( self ):
           target= self.target
           target( self.items(), **self.kwargs )




This class will wrap a "target" function which must be ready to work
with any iterable.  Every value from the queue will be provided to the
target function for processing.  When enough sentinel tokens have been
consumed from producers, it terminates processing.

**Consumer-Producer**

The middle of a processing pipeline is consumer-producer processes
which consume from one queue and the produce to another queue.

::

           
   class ConsumerProducerProcess( Process ):
       """Consumes items from a Queue and produces items onto a Queue.
       
       The "target" must be a generator function which yields
       pickable items and which expects an iterable as it's
       only argument.  Therefore, the args value is not used here.
       """
       def __init__( self, group=None, target=None, name=None, kwargs=None, input_queue=None, producers=0, output_queue=None, consumers=0 ):
           super( ConsumerProducerProcess, self ).__init__( name=name )
           self.target= target
           self.kwargs= kwargs if kwargs is not None else {}
           self.input_queue= input_queue
           self.producers= producers
           self.output_queue= output_queue
           self.consumers= consumers
       def items( self ):
           while self.producers != 0:
               for item in iter( self.input_queue.get, None ):
                   yield item
               self.producers -= 1
       def run( self ):
           target= self.target
           for item in target(self.items(), **self.kwargs):
               self.output_queue.put( item )
           for x in range(self.consumers):
               self.output_queue.put( None )
           self.output_queue.close()




This class will wrap a "target" function which must be a generator
function that consumes an iterable.

Every value from the queue is provided to the target generator.  Every
value yielded by the generator is sent to the output queue.  The input
side counts sentinels to know when to stop.  The output side produces
enough sentinels to alert downstream processes.

**Target Functions**

A producer function must be a generator function of this form

::

   def prod( *args ):
       for item in some_function(*args):
          yield item




A consumer function looks like this:

::

   def cons( source ):
       for item in source:
          final_disposition(item)




Finally, a consumer-producer function looks like this.

::

   def cons_prod( source ):
       for item in source:
          next_value= transform(item)
          yield next_value




These functions can be tested and debugged like this.

::

   for final in consumer( cons_prod( producer( *args ) ) ):
       print( final )




That way we're confident that our algorithm is correct before
attempting to scale it with multiprocessing.



-----

I try your the above code but it does run. Would y...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2012-02-08 04:13:55.109000-05:00

I try your the above code but it does run. Would you be able to put
together a complete example? Thanks!


Your code isn&#39;t exception safe, sys.exit safe,...
-----------------------------------------------------

Adam<noreply@blogger.com>

2012-02-08 20:36:05.805000-05:00

Your code isn't exception safe, sys.exit safe, or C extension
abort/assert safe. Using None as a sentinel is a bad idea for hopefully
obvious reasons. It's simply bad code, period.


@Adam: It&#39;s more helpful to post revised and c...
-----------------------------------------------------

S.Lott<noreply@blogger.com>

2012-02-14 08:34:08.212000-05:00

@Adam: It's more helpful to post revised and corrected code in your own
blog rather than hints or suggestions that something might be wrong.
"Simply bad code" doesn't present better code, does it?





