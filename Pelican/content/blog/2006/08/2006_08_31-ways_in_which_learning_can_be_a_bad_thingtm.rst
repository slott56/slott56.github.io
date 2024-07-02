Ways in which learning can be A Bad Thing™
==========================================

:date: 2006-08-31 17:54
:tags: building skills,#python,learning
:slug: 2006_08_31-ways_in_which_learning_can_be_a_bad_thingtm
:category: Books
:status: published





Once I learned C++, all my C programming became
poor-man's OO.  

-   Every "class" became a C structure
    type.

-   Every class structure was implemented as
    a header file that defined the structure and a bunch of method
    functions.

-   Each method function would have a "self"
    argument, which was a pointer to the object's type
    definition.



This code was somewhat
wordy and contrived-looking when compared with more typical C programs.   But
there was no going back to ordinary procedural programming after learning OO
programming.



Similarly, once I learned
how to do solid OO analysis, that was the end of any other style of requirements
discovery and documentation.  Even if the project was explicitly never going to
have an OO implementation, I still had to do OO analysis, no matter what.  It
leads to documents that are shorter and more to the point (when compared with
other analysis documents), but people would still be confused by the business
focus and lack of techno-mumbo-jumbo. 




I'm forced to do all design work in
the following contrived way:

1.  Create the Python class
    definitions

2.  Get the key algorithms to work in
    Python

3.  Write a specification for VB or Java
    programmers, based on the Python.  Or, if I'm doing the implementation, I
    rewrite the Python into Java.



All are
down sides of learning better ways to work.













