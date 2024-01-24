Dynamic Languages and Corporate IT's Objections
===============================================

:date: 2006-08-29 17:57
:tags: news
:slug: 2006_08_29-dynamic_languages_and_corporate_its_objections
:category: News
:status: published





Since most of these new-fangled dynamic languages
are open-source, we have a a strange artificial barrier to considering the right
solution for our problems.  This barrier is "No Open Source" policy, usually
framed as **We'll Use Open Source Over My Dead Body**\ ™.  It has to be examined
carefully from several points of view:

1.  Most organizations already have considerable
    open source software.  The `Apache server <http://httpd.apache.org/>`_ , for example, is probably the most
    popular (and visible) piece of open-source IT software in use anywhere.  If you
    mention things like `sendmail <http://www.sendmail.org/>`_ , you get back-talk that it's just
    infrastructure and somehow infrastructure doesn't count.  Perhaps it's not
    software, or doesn't support the enterprise.

2.  I've been asked about open source harboring
    viruses or malware.  I responded that the other 9,999 users who downloaded it
    would probably have reported a problem.  After all, we all have access to the
    source.

3.  I've been warned about the "liability issue"
    with open source software.  In short, the legal department doesn't know who to
    sue.  What if our in-house software doesn't work?  Somehow that's different: our
    in-house QA doesn't apply to source we got for
    free?



If we can get past the "dynamic languages are open source", then we can move on to more interesting issues.



Taft gets to the issues, eventually, when he lifts up two objections that have a little more substance.
Taft, however, ran out of words before getting to the real crux of these objections.



1.  **Imperative Programming is Dead**.  "Anders Hejlsberg, a Microsoft software
    architect in Redmond, Wash., and father of C#, said the days are numbered for
    imperative programming".  As with other such pronouncements, this is premature. 
    After all, procedural programming persists in spite of object-oriented
    programming.  Polemics aside, declarative programming has limited value, since
    it depends on automatic optimizers.  Since automated proofs of correctness don't
    exist in general, I'm `suspicious <{filename}/blog/2006/03/2006_03_01-c_microsoft_and_hegemony.rst>`_  that there are pretty severe limits
    on optimizations that can be successfully applied to support declarative
    programming.

2.  **Dynamic Languages Don't Scale**.  "Cedric Beust, an engineer at Google,
    in Mountain View, Calif., said, "Dynamic languages suffer from some inherent
    limitations that make them inadequate for 'large software.'"  There are two
    issues here: performance and error prevention.  Both of these issues lead us to
    some interesting conclusions, and some appropriate uses for dynamic
    languages.



Dynamic Languages Don't Perform Well
------------------------------------



This is a straw-man argument; it misses the point by attacking something irrelevant.
Yes, dynamic languages are not optimized as well by the compiler as dynamic languages.



However, the point is to
leverage this, and partition the architecture into the stable bits, and the
flexible bits.  I can see a spectrum of `mutability <{filename}/blog/2005/09/2005_09_18-essay_14_mutability_analysis.rst>`_  based on the nature of the
requirements.  For relatively immutable requirements, use a static language,
compile the heck out of it, and get it optimized so that it runs really fast. 
For the poorly-defined or inherently flexible requirements, use a dynamic
language.  Expect change, and implement it
appropriately.



Dynamic Languages Don't Prevent Enough Errors
---------------------------------------------



I'm not completely sold on
the value of static type checking in languages like Java, C, C++ (and Ada for
that matter).  Here's what I observe: a programmer who has a vague notion that a
variable has a numeric type, but can't identify the correct numeric subtype; he
spends hours doing an empirical survey of all numeric types to see which one
will compile.



This isn't *design* in the usual sense of the word.  The software will have the first numeric type
which compiled, right, wrong or indifferent.  We don't know if that's the right
type, or merely an acceptable supertype of the right type.  Static type checking
hasn't really prevented the eventual error from occurring.



Another scenario, less common, but more problematic, is the
**Type-Hierarchy-Meta-Framework Most General Declaration**\ ™ where we have created a
hierarchy of interfaces, abstract superclasses, and other declarative malarky to
try and unify two relatively dissimilar things into a common structure.  Perhaps
they should have used a **Façade** design, but instead they aimed for a too-complex static type
declaration.



This is a case of too much
design, rather than too little.  However, static type checking has introduced
problems rather than solved them.



Just to beat this topic to death, our SQL data bindings are always dynamic.  After
all, there's no strong relationship between our statically compiled Java
application and our relational database.  The Java type checking, while
internally consistent, doesn't have to match the database.  Indeed, seemingly
innocuous DB changes can lead to type compatibility problems and run-time
crashes in Java.



Introducing Dynamic Languages
-----------------------------



I think the upshot of Taft's article is the following pieces of advice:

-   Introduce a dynamic language in a way
    that plays to its strength: flexibility.  Handle scalability by partitioning the
    design into static and dynamic elements.

-   Introduce a dynamic language where fussy
    type-checking isn't helping the programmer.  If they need some kind of number, a
    dynamic language will handle this gracefully, without the breakage associated
    with picking the wrong type.  

-   Introduce a dynamic language where
    engineering a very general framework would help, but would be expensive and
    complex.  A simpler, dynamic-language framework can cover all of the bases, and
    glue static programming components together nicely.  After all, we've had the
    shell forever, and it is just rubbish dynamic programming with rotten data
    abstractions and cruddy syntax. 



I think the most important thing we can do is to look at a dynamic language as the
shell on steroids.






