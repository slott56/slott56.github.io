Tying your automobile to a hitching post.
=========================================

:date: 2006-12-17 21:04
:tags: building skills,#python,python complaints
:slug: 2006_12_17-tying_your_automobile_to_a_hitching_post
:category: Books
:status: published





The points are serious issues.  However, the best
summary comes from `Karl Guertin <http://gr.ayre.st/>`_:  "My explanation is that Duck Typing is like Ethernet, in
theory it will break, but in practice it works pretty well."



There were three questions which
raised four issues.  The questions included the seemingly incomplete OO
implementation in Python, the lack of clarity regarding references and objects,
and the lack of overloaded functions.  The last point was more of a complaint
about the lack of function signatures, so we'll make it four issues.  The bulk
of the responses all served to clarify the following point for
me.

**Python's implementation isn't incomplete or confusing, it's just different.** 



This takes some getting used to because you
have to relax your previous ideas and accept some new ones.  The "incomplete" OO
implementation had to do with the lack of a C++ or Java-style formal separation
between interface and implementation.  It isn't that the formalized interface is
missing, but that it's moved around a bit. 




OO Design and Privacy
---------------------



In C++, the interface
lived in the .hpp files, separated from the implementations in .cpp files.  In
Java, the interface could be declared separately, but is usually deduced from
the class definition.  The idea is that any implementation which supports the
interface can be checked by the compiler.  The static analysis of compatibility
somehow provides improved quality.



As a practical matter, however, the potential quality of static checking doesn't
really work out  very well.  While C++ detects a wide variety of errors, it only
does this if everything is recompiled.  In the event of dynamically linked
components (.DLL's or .SO's), however, problems can't be detected until there's
a run-time problem.  Similarly, Java class problems may not be detected until
class load time -- leading to run-time errors for compatibility issues.



In Python, the only detection
is run-time.  Therefore, in a very practical sense, Python error detection is
simpler and more regular.  Every design mistake is detected via run-time
exception handling.



References and Objects
----------------------



One new concept that
experienced programmers struggle with is the "everything's a reference" Python
viewpoint.  For C++ programmers, this can be confusing.  For Java programmers,
however, there is less confusion because Java has two very neat buckets:
primitive and reference types.  The primitive types behave enough like reference
types that the distinction can be made largely transparent.



In Python, I haven't seem
much confusion.  I attribute this to working with people who didn't know C++ in
the first place.  Lacking a confusing concept, they were perfectly comfortable
with this "object" vs. "variable" distinction.  A variable is just a reference
to an object, and objects last precisely as long as they have referencing
variables.  It's very neat and very simple.  The idea of other mechanisms isn't
worth discussing.



Overloaded Functions
--------------------



The third point had two
related issues; the first is the lack of overloaded functions.  Overloaded
functions can be valuable, but can also be confusing.  When a function has
overloaded definitions with different semantics, the overloading is just bad,
obscure design.  Nothing prevents this misuse of overloaded functions.




The valuable side of overloaded
functions is to have optional or variant parameters.  Python's has a vast number
of alternate formulations for parameters.  Having optional parameters in Python
gives us the same advantages of overloading function names to provide optional
or alternate parameters.  Having a single function makes it much harder to
create an overloaded function that has the same name but different semantics.




Function Signatures
-------------------



Here's the hidden
fourth point: "I expect to know (in a C++ sense) what is going in and what is
coming out, and if I don't get that right then the program/complier complains." 
This is only partially true.  Indeed, it's only true in a kind of superficial
way.  For example, when I call Java's ``math.sqrt(-1.0)``,
I've provided data that's correct as far as the compiler is concerned, but still
not really correct.  



The compile-time checking of function signatures isn't really terribly effective at preventing errors.

1.  In SOAP implementation, the function signature
    is restated in WSDL.  The Schema or DTD can add or remove constraints, leading
    to ambiguity not resolvable by any amount of compile-time checking.

2.  In .DLL and .SO libraries, the function
    signature of the .DLL (or .SO) may not match the .HPP file against which other
    components are compiled.  This is not resolvable by any amount of compile-time
    checking.

3.  In many cases, the "type" has to be extended
    to include a valid range of values, not just a valid representation.  Java (and
    C++) don't represent this well.  Python doesn't represent it well, either. 
    However, Java and C++ create an unrealistic expectation that simplistic type
    matching is sufficient, and run-time error checking is often done badly or not
    at all.  In Python, run-time checking is the norm, and can't be
    overlooked.



The Legacy Bias
---------------


Our experience colors our perceptions.  How do we get past our bias?



Here's a good version of a
relevant `Koan <http://mornmeet.blogspot.com/2006/11/introduction-to-zen.html>`_ .  You can learn more effectively if you
have a "`Beginner's Mind <http://sfzc.org/Pages/Library/zmbm.html>`_ ".    In this case, the baggage
of problems in C++ became complaints about gaps in Python. 




They aren't gaps or problems in Python.  They are just differences.




Here's what's most important: **Teaching Programming requires Beginner's Mind**.
I don't think you can teach programming
without revisiting the newbie programmer's fundamental confusion of what they
say at compile time and what happens at run time.  I don't think
compare-and-contrast between programming languages is appropriate.   I think
that it's more important to treat each programming language as a fresh exercise,
using the language to implement the desired algorithms and data structures.












