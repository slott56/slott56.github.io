The Visitor Design Pattern and Python
=====================================

:date: 2014-03-13 08:00
:tags: #python,design,OO design
:slug: 2014_03_13-the_visitor_design_pattern_and_python
:category: Technologies
:status: published


Epiphany.

In Python, with iterators, the **Visitor** design pattern is useless.
And a strongly-ingrained habit. Which I'm trying to break.

Here's a common **Visitor** approach:

::

   class Visitor:
       def __init__( self ): ...
       def visit( self, some_target_thing ): ...
       def all_done( self ): ...

   v = Visitor()
   for thing in some_iterator():
       v.visit(thing)
   v.all_done()




If we refactor the for statement into the **Visitor**, then it's just
a **Command** or something.

Here's the refactored **Iterating Visitor**:

::

   class Command:
       def __init__( self ): ...
       def process_all( self, iterable ):
           for thing in iterable:
               self.visit( thing )
       def visit( self, thing ): ...
       def all_done( self ): ...

   c=Command()
   c.process_all( some_iterator() )
   c.all_done()




Possible Objection
------------------

The one possible objection is this: "What if our data structure is
so hellishly complex that we can't reduce it to a simple iterator?"

That's perfectly silly. Any hyper-complex algorithm to walk any
hyper-complex data structure, no matter how hyper complex, can always
be recast into a generator function which uses yield to iterate over
the objects.

Better Design
-------------

Once we start down this road, we can generally simplify processing
into a kind of **Command** that looks something like this.

::

   class Command:
       def __init__( self ): ...
       def run( self ): 
           for thing in self.iterable:
               ....

   c= Command()
   c.iterable= some_iterator()
   c.run()




I find that this interface is somewhat easier to deal with when
composing large commands from individual small commands. It follows a
**Create-Configure-Run** pattern that seems to work out well. I just
wish I would start with this rather than start with a **Visitor**,
refactor, and end up with this.





