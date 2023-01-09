Legacy Code Preservation: Some Patterns  
=========================================

:date: 2013-05-21 08:00
:tags: test-driven reverse engineering,HamCalc,knowledge capture
:slug: 2013_05_21-legacy_code_preservation_some_patterns
:category: Technologies
:status: published

.. container:: section
   :name: some-patterns

   After looking at this suite of examples, we can see some patterns
   emerging. There seem to be several operating principles.

   #. **The Data Matters**. In many cases, the data is the only thing
      that actually matters. The legacy application knowledge may be
      obsolete, or so riddled with quirks as to be useless. The legacy
      knowledge may involve so much technical detail---no user
      story---that it's irrelevant when a newer, better technology is
      used.
   #. **User Stories Matter; Legacy Technology Doesn't Matter**. It is
      essential to distinguish the legacy technology from the meaningful
      user stories. Once the two are teased apart, the technology can be
      replaced and the user stories preserved. A cool DSL may be
      helpful, and needs to be preserved, or may be a distraction from
      the real solution to the real problem.
   #. **Understanding the New Technology Is Central**. Misusing the new
      technology simply creates another horrifying legacy.
   #. **Testing is Essential**. Legacy code cannot be preserved without
      test cases. Any effort that doesn't include automated comparisons
      between legacy and converted is just new development.
   #. **Discarding is Acceptable**. Unless the legacy code has a
      seriously brilliant and unique algorithm, most business
      applications are largely disposable. It may be less expensive to
      simply do new development using the legacy code as a kind of
      overly-detailed specification. Calling it "conversion" to make
      managers feel good about "preserving" an "asset" is acceptable.
      The project is the same as new development, only the words change
      to protect the egos of those not really involved.
   #. **Quirks are Painful**. They might be bugs or they might be
      features. It will be difficult to tell.

   How do these principles match against our various case study
   projects?

   -  **What's the Story?** The applications were technical, and could
      be discarded.

   -  **Are There Quirks?** Without a test case, we could not be sure of
      our conversion. So we accepted the quirks.

   -  **What's the Cost?** The application was technical, and could be
      discarded.

   -  **Paving the Cowpaths.** New Technology was misused, the result
      was a disaster.

   -  **Data Warehouse and Legacy Operations.** The legacy software
      encoding knowledge can be split haphazardly into database and
      application software buckets. The user stories matter. The
      technology doesn't matter.

   -  **The Bugs are the Features.** The user stories matter. If you
      can't articulate them, you're going to struggle doing your
      conversion.

   -  **Why Preserve An Abomination?** When the code is shabby and has
      bugs, you have to sort out the quirks that will be carried forward
      and the junk that will be discarded.

   -  **How Do We Manage This?** The user stories matter. The data
      matters. Focus on these two can help prioritize.

   -  **Why Preserve the DSL?** The user stories and test cases lead to
      a successful outcome. While the customer may feel like a
      conversion was being performed, it was really new development
      using legacy code as a specification.

   With modern languages and tools, legacy code conversion is quite
   simple. The impediments are simply managerial in nature. No one wants
   to have a carefully maintained piece of software declared a liability
   and discarded. Everyone wants to think of it as an asset that will be
   carefully preserved.



-----

There is another pattern that I have first hand ex...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2013-05-21 19:03:46.862000-04:00

There is another pattern that I have first hand experience with. Covert
only part of the legacy system and have the legacy and the new system
with new features update each other in real time. Oh and btw, the old
and new system are not fully compatible w/ each other.
Techniques like database views and instead of triggers are used to fake
out the old or new system as needed.
And yes, I used the words "fake out" on purpose.





