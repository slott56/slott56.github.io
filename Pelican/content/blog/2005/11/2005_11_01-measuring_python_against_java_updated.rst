Measuring Python Against Java (Updated)
=======================================

:date: 2005-11-01 15:56
:tags: books,building skills,#python
:slug: 2005_11_01-measuring_python_against_java_updated
:category: Books
:status: published





**Date** 
[`seven habits <http://jroller.com/page/cpurdy?entry=the_seven_habits_of_highly>`_ ].  Including Calendar and the SQL
variations on the core Date class.  Since it's legacy technology, Date can't be
removed.  And almost everyone gets confused by java.sql.Date and
java.util.Calendar.  There seem to be three problems: mutability of Date
objects, the naming problem with the SQL variations, and the "bolt-on" calendar.




Mutability of fields within a Date
object is rather serious.  Calendar, to an extent, can fix this, but only when
Date objects become truly immutable.  Python used to complicate the issue by
wallowing in the C library, offering multiple representations (numeric seconds
and the time structure).  



Python now
has the date representation problem solved with a clean
datetime module
offering date,
time and
datetime. 
Further, the Python
datetime module
is designed with SQL compatibility in mind.  The objects aren't mutable, a
Date object can
emit a new Date
with modifications applied.



In
/dev/null, the idea is lifted up that the Gregorian calendar is the only
calendar, which is simply wrong.  However, since the Python implementation is
the in Dershowitz and Reingold's implementation from the book
*Calendrical Calculations* , conversion to other calendars is
practical.  Buy the book, it's brilliant computer
science.



**Decimal** 
[`seven habits 1 <http://jroller.com/page/cpurdy?entry=the_seven_habits_of_highly1>`_ ].  Solved.  Python has long decimal
integers as a first-class language construct.  Further, if you need additional
fixed point math features, you can look for the Python
fixedpoint
module http://fixedpoint.sourceforge.net/
].



**Other Interfaces**  [`seven habits 2 <http://jroller.com/page/cpurdy?entry=the_seven_habits_of_highly2>`_ ]:  Cloneable, Serializable and Entry all
raise the unpleasant consequences of attempting to enforce Java's complex
privacy model.  Cloneable, for example, has a convoluted "willing-to" notion. 
Serializable requires private methods for the
implementation.



Since Python has an
much simpler notion of class privacy, there is no convoluted logic to cloning or
serializing an object.  Indeed, Python has almost no privacy at all.  Who is the
beneficiary of the complex interplay between
protected,
private and
public?



**Exceptions** 
[`seven habits 3 <http://jroller.com/page/cpurdy?entry=the_seven_habits_of_highly3>`_ ]:  SQLException and RemoteException are too
widely declared in Java.  Python finesses this by declaring nothing.  Is this an
improvement?  In this case, I submit that it is an improvement.  I think the
Java "full disclosure" of thrown exceptions leads to their egregious
over-declaration.  One consequence is dummy handlers that do little more than
fulfill the syntax requirements of catching the exception so we can stop the
declarations.  



The issue that is
raised in Python-world is that you don't know precisely where you'll
*need* 
try blocks.  On the other hand, as /dev/null observes, a lot of those Java
try-catch blocks aren't always doing something useful.  I prefer the Python view
that a very few exceptions are expected (generator functions raise
StopIteration)
and all others are -- well -- exceptional.  Your program has crashed and an
elaborate and noisy death is appropriate. 




Yes, I'm aware that incorrect
processing still has some value and some programs should limp along in spite of
unhandled exceptions.  Yes, a framework can catch, log and eat those exceptions
so that -- as a whole -- the system continues to stumble forward.  However, the
Java explicit declarations don't help and Python seems to stack up well in this
regard.

 








