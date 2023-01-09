Legacy Code Preservation: Why Preserve the DSL?  
=================================================

:date: 2013-05-16 08:00
:tags: HamCalc,knowledge capture
:slug: 2013_05_16-legacy_code_preservation_why_preserve_the_dsl
:category: Technologies
:status: published

.. container:: section
   :name: why-preserve-the-dsl

   A Domain-Specific Language (DSL) can provide some intellectual
   leverage. We can always write long and convoluted programs in a
   general-purpose programming language (like Python, Java or C).

   Sometimes it can make more sense to invent a new domain-specific
   language and implement the solution in that language.

   Sometimes, even well-written, highly portable programming becomes a
   legacy. I once converted a large, well-written program from C to
   Java. The organization had no skills in C and didn't want to build
   these skills.

   They wanted their legacy C program rewritten into Java and then
   extended to cover some additional features.

   The timeframe for this exercise is the sometime after 2010. This is
   important because automated unit test and test driven development are
   common knowledge. We're not fighting an uphill battle just to figure
   out how to compare legacy with new.

   In essence, we're going to be doing "Test Driven Reverse
   Engineering." Creating test cases, seeing what the legacy software
   does and then creating new software that does the same thing.

   We're preserving exactly those features which we can encode as unit
   test cases.

.. rubric:: The Code Base

In this case, there was an interesting wrinkle in the code base.
The application included a small Domain-Specific Language (DSL)
that was used to define processing rules.

There were only a dozen or so rules. The idea was the various
combinations of features could be included or excluded via this
little DSL. The application included a simple parser that
validated the DSL and configured the rest of the application to do
the actual work.

The DSL itself is of no value. No one in the user organization
knew it was there. The file hadn't been touched in years. It was
just a configuration that could have been meaningfully built as
source code in C.

The dozen or so rules are extremely important. But the syntax of
the DSL was disposable.

It was relatively simple to create class definitions that -- in a
limited way -- mirrored the DSL. The configuration could then be
translated into first-class Java.

.. code-block:: java

     package com.whatever.app.config;
     import com.whatever.app.defs;
     class Configuration {
         List theRules= new LinkedList();
         Configuration() {
            theRules.add(
              new Simple_Rule( this_condition, SomeOption, AnotherOption );
            theRules.add(
              new Simple_Rule( that_condition, SomeOption );
            theRules.add(
              new Exception_Rule( some_condition, some_exception );
         }
     }

Things that had been keywords in the old DSL became objects or
classes full of static declarations that could be used like
objects.

By making the configuration a separate module, and using a
property file to name that module, alternate configurations could
be created. As Java code in Java Syntax, validated by the Java
compiler.

.. rubric:: The Unit Tests
   :name: the-unit-tests

The bulk of the code was reasonably clear C programming.
Reasonably. Not completely.

However, I still insisted on a pair of examples of each of the
different transactions this program performed. These mostly
paralleled the DSL configuration.

Having this suite of test cases made it easy to confirm that the
essential features really had been preserved.

The user acceptance testing, however, revealed some failures that
were not part of the unit test suite. Since TDD was new to this
customer, there was some fumbling while they created new examples
that I could turn into proper unit test cases.

The next round of acceptance testing revealed another few cases
not covered by the examples they had supplied. By now, the users
were in on the joke, and immediately supplied examples. And they
also revised a existing examples to correct an error in their test
cases.

.. rubric:: What Was Preserved
   :name: what-was-preserved

Of the original C software, very little actually remained. The
broad outline of processing was all.

The tiny details were defined by the DSL. This was entirely
rewritten to be proper Java classes.

The C data structures where entirely replaced by Java classes.
All of the original SQL database access was replaced with an ORM
layer.

Further, all of the testing was done with an entirely fresh set of
unit tests.

The project was -- actually -- new development. There was no
"conversion" going on. The customer felt good about doing a
conversion and "preserving" an "asset". However, nothing much was
actually preserved.



