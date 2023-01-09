Is it really test *driven*  reverse engineering?
================================================

:date: 2007-10-21 21:28
:tags: architecture,design,unit testing,tdre
:slug: 2007_10_21-is_it_really_test_driven_reverse_engineering
:category: Architecture & Design
:status: published







When I was a kid, reverse engineering a legacy application was a challenge.  Tools were non-existent, and even a civilized practice like unit testing didn't really exist.  Now that we have test driven development, I think we can apply this to reverse engineering the billions of lines of legacy software that still exist in our application portfolios.



There are a few things to watch out for, however.  Top on the list is trying to recover meaning from code which is intentionally obscure.



:strong:`The Dark Ages`



Back in the dark ages, we had programs written in assembler that did something of value, and the customer wanted a COBOL program.  Sometimes we had RPG applications that needed to be turned into COBOL.  Once, I even looked at some APL code that needed to be turned into COBOL.



In the case of assembler, where there are no real rules imposed by the language, it wasn't possible to consider any kind of syntactic transformation to COBOL.  Assembler programs (like it's bastard child, C) could directly manipulate pointers and do awful things.  Of course, assembler programs could (and did) modify themselves at run-time.



This is a translation from a semantically rich language to a poor language.  You could say :emphasis:`anything`  in assembler.  In COBOL, you only had a limited subset of available language constructs.



The strategy of choice was :strong:`Semantic Transformation`.  Get a grip on the program's purpose and means, describe that in clear English, and then write that in COBOL.



:strong:`RPG and APL`



For languages like RPG or APL, the language itself implies some powerful, but implicit algorithms.  In this case, the language was semantically limited -- you didn't have to say much -- but the meaning of each statement (or expression) was deep.  Writing COBOL programs was translating from a semantically deep language to a semantically shallow language.



In some cases, there were opportunities for :strong:`Syntactic Transformation`.  RPG programs (especially old RPG and RPG II) could be rewritten into a COBOL-like syntax.  A great deal of fixed program structure had to be wired in around this transliterated RPG and it never covered all the cases well, but it got you started. 



In the case of APL, it was purely a :strong:`Semantic Transformation`  exercise.  The APL had to be read (and understood) in order to reason out what the COBOL was supposed to do.  Sadly, APL is a WORN (write-once-read-never) language, so this reverse engineering effort (had we won the bid) would have been epic.



:strong:`From C to Shining Java`



Recent reverse engineering exercises have been from the semantically rich language, C, to the semantically poor, but deep language, Java.  There are many C-isms that don't translate to Java.  While the syntax is similar, that's should be looked at as little more than coincidence.



It isn't sensible to attempt a syntactic transformation, since that obviates any value that Java creates.  Without understanding the semantics and creating some kind of object model, Java isn't really very helpful.



In order to construct proper Java objects, we need to pull out the relevant bits of C, merge them into a candidate object design, and then validate that design.  Clearly, a unit test is just what the doctor ordered.



:strong:`Driven By Testing?`



Unit testing is a wonderful way to get a sense of incremental accomplishment.  As pieces of C program are rewritten into Java, a set of unit tests demonstrate that it "works".  We have to be cautious in this assessment, however, since some C programming is hideously obscure.  A recent example (`Obscure C-isms and How to Find Them <{filename}/blog/2007/10/2007_10_19-obscure_c_isms_and_how_to_find_them.rst>`_ ) was a humbling few hours of pain.



Here's the sequence.  We're writing code first, then fitting unit tests around the extracted code, then refactoring the code.  Is this test driven?



Arguably, it isn't driven by testing.  We didn't fabricate a test scenario and fit code around it.  



However, the process is driven by the need for testing.  Further, test driven development doesn't start with testing.



:strong:`Test Driven isn't Test First`



Test Driven Development starts with a little bit of preliminary design to create an API.  Given the preliminary API design, we start to craft some tests.  Often, I'll realize that the notional API isn't quite the thing, and refactor the tests to describe a slightly different API.  This process rarely goes through more than one iteration; it's a notional API until I start implementing it.



The test did not come first.  It was a close second after the notional API that was going to be tested.



After an initial implementation has been written, I'll often revisit the tests because the notional API is starting to look clumsy.  Generally, a round of early refactoring happens because there are too many objects being created or too many individual steps, or too few discrete objects for comfortable testing.



Reverse engineering is only slightly different from development.  The principle difference is that I rarely start with a notional API, but rewrite the legacy code into the new Java.  Then come test cases, followed by the early round of refactoring to get the API to be sensible.



I claim that reverse engineering can be test driven.  It isn't dramatically different from development.




