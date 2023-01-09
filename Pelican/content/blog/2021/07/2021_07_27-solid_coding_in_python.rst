SOLID Coding in Python
======================

:date: 2021-07-27 09:00
:tags: Design Principles,OO design,SOLID
:slug: 2021_07_27-solid_coding_in_python
:category: Architecture & Design
:status: published


Check this out.

   `SOLID Coding in Python <https://link.medium.com/rFDC7sSxBhb>`__ by
   Mattia Cinelli.

   Download Medium on the `App
   Store <https://itunes.apple.com/app/medium-everyones-stories/id828256236?pt=698524&mt=8&ct=app_email_share>`__
   or `Play
   Store <https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3Dios_app%26utm_medium%3Demail%26utm_campaign%3Dios_app_email_share>`__



This was fun to read. It has some nice examples.

I submit that the order of presentation (S, O, L, I, D) is misleading.
The acronym is fun, but awkward.

My `LinkedIn Learning
course <https://www.linkedin.com/learning/learning-s-o-l-i-d-programming-principles/welcome>`__
covers these in (what I think is) a more useful order.

#. **Interface Segregation**. I think this is the place to start: make
   your interfaces as small as possible.

#. **Liskov Substitution**. Where necessary, leverage inheritance.

#. **Open/Closed**. This is a good quality check to be sure you've
   followed the first two principles well.

#. **Dependency Injection**. This is often about test design and future
   expansion. In Python, where everything really happens at run time, we
   often fail to parameterize a type properly. We often figure that out
   a test time, and need to revisit the Open/Closed principle to get
   things right.

#. **Single Responsibility** is more of a summary of the previous
   principles than a distinct, new principle. I think it comes last and
   should be treated as a collection of good ideas, not a single idea.

I think time spent on the first three -- Interface Segregation, Liskov
Substitution, and the Open/Closed principle -- pay off tremendously. The
ILODS acronym, though, isn't as cool as SOLID.

The "Single Responsibility" suffers from an ambiguous context. At one
level of abstraction, all classes have a single responsibility. As we
dive into details, we uncover multiple responsibilities. The further we
descend into implementation details the more responsibilities we
uncover. I prefer to consider this a poetic summary, not the first step
in reviewing a design.





