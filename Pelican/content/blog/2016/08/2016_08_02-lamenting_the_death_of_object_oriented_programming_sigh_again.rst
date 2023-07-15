Lamenting the Death of Object-Oriented Programming. (Sigh) Again? 
==================================================================

:date: 2016-08-02 08:00
:tags: functional programming,object-oriented design,object-oriented language
:slug: 2016_08_02-lamenting_the_death_of_object_oriented_programming_sigh_again
:category: Technologies
:status: published

See `Goodbye, Object Oriented
Programming <https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53#.oe5r8bgir>`__.
I don't want to say that the entire article is bunk. It's not. It raises
a few good points. Points which I thought were pretty well known.
What's aggravating is that this lamentation is overly broad.  It treats
all languages as if they're Java or C++. That's not true, and as a
consequence, the article is less useful than it could be.
**Banana Monkey Jungle Problem**. Only true if you are sadly mistaken
about the unit of reuse. The class as unit of reuse -- across projects
-- is false, has been false, and will always be false. The idea of class
inheritance for reuse makes perfect sense. Sharing individual classes
between projects has never (as far as I know) been a promise of OO
programming. Maybe I read the wrong books and missed that promise.
**The Triangle Problem**. Isn't actually a problem. Python has a defined
method resolution order.
**The Fragile Base Class Problem**. This points out the well known issue
with having concrete classes depend on other concrete classes. The SOLID
design principles suggest concrete classes should depend on
abstractions. Abstractions do not suffer (as much) from the fragile base
class problem.
**The Hierarchy Problem**. I guess the idea that the real world is
multi-dimensional can be confusing. If everything has to be force-fit
into single inheritance, this would create the hierarchy problem. If we
allow multiple inheritance, this problem evaporates.
**The Reference Problem**. Even C++ has "smart" pointer packages. Java
has garbage collection. Python does reference counting. This is only a
problem if you go out of your way to deal with pointers in a primitive
way.
The part on Polymorphism didn't make any sense. There didn't seem to be
a tidy problem. Just a confusingly vague statement that "Interfaces will
give you [polymorphism?]. And without all of the baggage of OO". I don't
get how interfaces are necessary without the baggage of OO. So, I can't
really try to refute this.
In the long run, I guess this was a way to introduce some of the
benefits of a functional approach. I'm not sure that this kind of
criticism of object-oriented programming is very helpful. It doesn't
apply to all OO languages, so it's misleading at best. (At worst, it's
simply wrong.)
I think these problems are interesting and can be used to show the
benefits of functional programming. But without the actual functional
programming examples, this isn't very useful.





