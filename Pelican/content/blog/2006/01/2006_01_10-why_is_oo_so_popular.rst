Why Is OO So Popular?
=====================

:date: 2006-01-10 03:29
:tags: architecture,object-oriented design,complexity
:slug: 2006_01_10-why_is_oo_so_popular
:category: Architecture & Design
:status: published





"Polymorphism is nice as well, although I can't
grok (yet) why this is necessarily not part of non-OO things. I'm not clear that
it goes with the strong binding of state and method in a
class."



Polymorphism isn't necessarily
part of OO.  Python actually has polymorphic functions outside of class
definitions. 



Further, Python offers an
interface called "callable", which makes an object equivalent to a function,
giving you stateful function-like things with hysteresis (or other odd
not-very-function-like properties).  [It isn't really an interface, it's a
special method name, but that's just
syntax.]



The Java distinctions between
class and method can be teased apart in the Python world.  This causes me to
think that the crispness of some of these Java-world OO definitions -- while
laudable -- isn't essential to good
programming.



AND.  Smalltalk (like
Python) was free of type declarations.  Originally, OO seems to have been
type-less.  Big, complex, subtle and profound simulations were built in
Smalltalk (and some related earlier OO languages like Simula) and LOOPS (Lisp
with Objects) without benefit of formal
type-checking.



What does this
mean?



C++ introduced strong typing and
Java perpetuated that.  C++ suffers from the bizarre mish-mash of types with
class names, but no actual class objects.  Without a root "object" declaration,
C++ collection classes require the very complex template mechanism.  Why is this
better than C?  I don't know.  C++ adds inheritance and encapsulation to C, but
the strong typing also adds templates.  A net loss,
IMO.



Java introduced class objects and
good memory management to C++; it recast everything to stem from object, making
the collection classes almost as simple as Smalltalk.  To banish multiple
inheritance, it introduced interfaces (approximately a wash between what was
lost and what is gained).



But the
recent hot tickets (Perl, PHP, Ruby and Python) don't have formal type
declarations.  I'll set aside Perl and PHP.  Perl's OO material is ungainly and
doesn't seem to be widely used.  PHP has OO machinery.  It looks very nice, but
it, too, seems to be largely ignored in favor of the excellent HTML templating
engine.



Ruby and Python are OO to the
very core of the virtual machine, giving them more complete polymorphism.  Also,
lacking type declarations, you are freed from the complexity of the subtle
interface declarations required to pile not-very-similar things into a useable
collection class.  You can just bunch all kinds of things into a polymorphic
Python collection as long as they have the right method signatures, all other
considerations be damned.



The Real
Benefits of Java.



I think it isn't
objects -- per se -- that are the appeal of OO programming.  I think it is many
things, exemplified by Python.  (Why Python? you ask.  Because Python predates
Java.)  I think the currency of Java, Python and Ruby comes from a 1-2 punch of
coolnesses.



1.   Powerful tools that
make compiling, linking and executing a breeze.  Ada tools in the 80's struggled
to do the simplest compilation dependency checking -- there were elaborate
provisions for libraries and library lookups and reconciliations and junk that
Java does for free without even asking.   Python embeds the compiler and the JVM
into a single entity, making the whole "compile" thing seamless, silent,
odorless and grease-free.



2.  A
rational approach to programming in the large.  Java has packages, (files),
classes and methods.  Python has packages, modules/files, classes and methods. 
Python packages are more than just a path to a file.  C just had files, you were
on your own for any other structure you wanted to impose.  C++, similarly, is
largely just files, it takes craft and skill to manage the
complexity.



I think these two reinforce
each other as part of a feedback loop.   I think the modern, hot-ticket
languages all provide insanely powerful tools and highly structured
programming.



The tougher question is
"what is next?"



The answer, I think, is
"more of the same".  I think that Java's lack of effective DRY mentality is a
problem.  There is too much extra information floating around in JavaDoc's that
repeat parts of the code and XML files that repeat parts of the
Java.



The hard problems (defining the
problem, defining data structures that solve the problem, defining functions to
manage the data structures that solve the problem) won't go away.  However, more
powerful tools make it easier to explore same with lower costs and risks.




Hence my investment in learning
Django.  I think this kind of thing (not this specific thing) is the reason why
Ruby on Rails is welcomed by many web developers as packaging all the standard
best practices in one place.








