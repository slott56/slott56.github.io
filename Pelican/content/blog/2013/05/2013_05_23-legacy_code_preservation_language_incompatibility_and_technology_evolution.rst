Legacy Code Preservation: Language Incompatibility and Technology Evolution  
=============================================================================

:date: 2013-05-23 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_05_23-legacy_code_preservation_language_incompatibility_and_technology_evolution
:category: Technologies
:status: published

It's important to address language or platform incompatibility as
consequences of technology modernization. The reason why we have to do
manual conversions of software is because of the language
incompatibility issue. We must convert manually when no tool can do
the conversion.

There are several layers to this.

-  **Platform Incompatibility**. This means that the supporting
   libraries for the language are incompatible between versions. This is
   relatively rare; language libraries are almost always backward
   compatible. When they aren't, the problem can often be masked with a
   "shim" or little bit software to "wrap" the new libraries to make
   them work like the old libraries. Adding the shim is -- generally --
   a terrible idea. Why preserve the old version's weird features and
   quirks? Why add the complexity (and bugs and quirks) of the shim?

-  **Support or Framework Incompatibility**. A common "Support"
   incompatibility is a database; there are many other examples. SQL,
   for example, has a standardized core, but is not consistently
   implemented and vendor extensions are common. Any large framework
   will have compatibility issues among versions and platforms.

-  **OS Incompatibility**. Most POSIX-compliant OS's (Linux, Mac OS X,
   etc.) are reasonably compatible. Windows throws a monkey-wrench into
   the works. In some cases, a language offers a library to make the
   programs in that language OS-agnostic. An OS-unique feature of an
   application is a disturbing thing to convert. Is the OS-unique
   feature an **essential** feature of the application? In some cases,
   the OS-unique feature stems from specialized drivers for media
   support (sound, images, video, etc.) This media compatibility issue
   leads to complex OS-agnostic support or leads to the use of
   third-party OS-agnostic libraries.

-  **Language Incompatibility**. This is usually an absolute block to
   automated conversion. Languages are designed **not** to be compatible
   at a conceptual or semantic level. Automated translation from one
   programming language to another is difficult and in some cases
   essentially impossible without some kind of supremely sophisticated
   artificial intelligence effort. If languages were compatible at a
   conceptual level, we'd have universal translation among programming
   languages.

When we look at our case studies, we see the following:

-  **What's the Story?** OS conversion; the language remained
   more-or-less the same.

-  **Are There Quirks?** OS and Language conversion: Fortran to PL/1.

-  **What's the Cost?** Language conversion: JOVIAL to Fortran.

-  **Paving the Cowpaths**. Persistence framework conversion: flat files
   to RDBMS.

-  **Data Warehouse and Legacy Operations**. This often involves OS,
   language and persistence conversion.

-  **The Bugs are the Features**. This was a mental problem, not a
   technical one.

-  **Why Preserve An Abomination?** OS, language and persistence
   conversion: Basic to Java.

-  **How Do We Manage This?** OS, language and persistence conversion:
   COBOL to Java.

-  **Why Preserve the DSL?** Language and persistence conversion: C to
   Java.

In the case where there's a language conversion, the effort simply
becomes new development. The "conversion" or "modernization" concept
is there merely to make managers feel that value is being preserved.

In the rare case where the language was **not** converted, deep
questions about user stories vs. technical implementation needed to be
asked and answered clearly and completely. When they were not asked
(or answered) the conversion did not go well.

.. rubric:: Automated Language Translation
   :name: automated-language-translation

The idea of automated language conversion is an "attractive
nuisance".

(http://en.wikipedia.org/wiki/Attractive_nuisance_doctrine). Not only
is it generally impossible, it reduces or eliminates the value of the
captured knowledge.

Assume you have some program P_1 in language L_1. It captures some
knowledge, K, about the problem domain, and encodes that knowledge in
a more-or-less readable and meaningful format.

We want to 'automagically' create a new program P_2 in language L_2.

Since the two languages employ different concepts, different data
structures, different programming paradigms, the conversion doesn't
happen at a "high level". This is not a matter of changing
the print statement to the print() function. This is a matter of
"understanding" the program, P_1 and then creating a new program,
P_2. that performs the "same" functions from the user's point of
view.

Choice #1 is to create a very high-level technical "specification"
that's language-independent. Then, a translator compiles that
high-level specification into the new language. In essence, we've
"decompiled" from P_1 to P_S and then compiled P_S to P_2, using an
intermediate specification language, L_S. The high-level
specification language L_S must contain both languages, L_1 and L_2,
as features.

There are examples of elements of this. C++ is compiled to C. Eiffel
is often compiled to C. We can think of C++ as a specification
language that's translated to C.

Further, we know that "control structure" (IF-THEN-ELSE, WHILE, GOTO)
can all be mapped to each other. There's an elegant graph-theoretic
proof that a program which is a morass of GOTO's can be revised into
IF-THEN-ELSE and WHILE loops. Clearly, then, the converse is
possible.

While we can go from C++ to C, can we go from C to C++? At least
superficially, yes. But that's only true because C++ is defined to be
a superset of C. So that example is really poor. We'll ignore C++ as
a higher-level language.

Let's look at Eiffel. We can go from Eiffel to C. Can we go from C to
Eiffel? Not really. Eiffel lacks the GOTO, which C supports. Also, C
has unconstrained pointer coercion (or casting) which Eiffel lacks.
In order to "decompile" C to Eiffel, we'd need to "understand" the C
programming and essentially rewrite it into a neutral version in
Eiffel which could be then translated to another implementation
language.

Making the problem worse, C has murky semantics for some
constructs. a[i++]= i; for example, is poorly-defined and can do a
wide variety of things.

.. rubric:: Semantic Loss
  :name: semantic-loss

Choice #1--to create a very high-level technical
"specification"--can't be done automatically.

Choice #2 is to create a very low-level implementation of the program
P_1 by compiling it into machine instructions (or JVM instructions or
Python byte codes or Forth words). This low-level language is L_M.
Given a program in L_M, we want to restructure those machine
instructions into a new program, P_2, in the new language, L_2.

It's important to observe that the translation from P_1 to machine
code L_M may involve some loss of semantic information. A
machine-language "AND" instruction might be part of a P_1 logical
"and" operation or part of a P_1 bit mask operation. The context and
semantic background is lost.

Without the semantic information, P_2 may not reflect the original
knowledge captured in P_1.

Note that this difficulty is the same as choice #1--creating a
higher-level specification.

We can't easily "decompile" code into a summary or understanding or
description. Indeed, for some languages, we're pretty sure we don't
want to try to automatically decompile it. Some legacy C code is so
obscure and riddled with potential confusion that it probably should
be rewritten rather than decompiled.

Here's a concrete example from HamCalc.

.. code-block:: basic

      700 A=2:B=1:T=P:X=0
      730 FOR N=A TO T STEP B
      750 IF T/N=INT(T/N)THEN X=X+1:PN(X)=N:T=T/N:GOTO 730
      760 A=3:B=2
      770 NEXT N

The point is to find prime factors of P, building the array PN with
the X factors.

Note that line 750 executes a GOTO back to the FOR statement. What --
precisely -- does this mean? And how can be be automagically
decompiled into a specification suitable for compilation into another
language?

This, it turns out, is also an example of a place where HamCalc is
not a repository of profoundly useful programming.
See http://en.wikipedia.org/wiki/Integer_factorization for more
sophisticated algorithms.

.. rubric:: Knowledge Capture
   :name: knowledge-capture

It appears that knowledge capture requires thinking.
There's no automatic translation among programming languages, data
structures or programming paradigms.
The only viable translation method is manual conversion:

#. Understand the source program.
#. Create unit test cases.
#. Develop a new program that passes the unit test cases.





