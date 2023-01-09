How Essential Is Unit Testing?  Or, How Do We Make It Essential?
================================================================

:date: 2007-12-24 11:31
:tags: #python,unit testing
:slug: 2007_12_24-how_essential_is_unit_testing_or_how_do_we_make_it_essential
:category: Python
:status: published







See `Present Perfect <http://thomas.apestaart.org/log/?p=559>`_  for some thoughts on unit testing.   See some other commentary on the discipline required to write Python programs in `Gnome devs too lazy for python <http://panela.blog-city.com/gnome_devs_too_lazy_for_python.htm>`_ .  I think I see the disconnect that makes testing appear to be too costly; I think that some basic "meta-quality attributes" are essential to understanding unit testing.



Here's the original C# vs. Python analysis in `Monotonous <http://joeshaw.org/2007/10/28/496>`_ .



Here's the famous quote: "Writing real applications in Python requires a discipline that unfortunately most people (including myself, at that time) are unwilling to adhere to, and this easily leads to buggy and hard to maintain programs. You have to be very diligent about unit tests and code coverage for every line of code, because you can’t rely on the compiler to catch errors for you."



I didn't take careful notes at a client meeting where this came up, so I don't have good quotes.  The client balked at the very idea of Test Driven Development.  In a larger presentation on testing (technology, environments, process, etc.) I had lifted up TDD as a direction that would benefit the developers.  The response from the director of development was a series of "how would you do that?" questions.  



These weren't practical "how to" questions.  They were rhetorical "that isn't possible" statements, framed as questions.  In order to portray TDD as impossible the questions quickly devolved into how TDD interacts with requirements gathering and business analysis; I couldn't successfully bracket the questions as part of the fringe of TDD.  I think the disconnect was their certain knowledge that test cases come only from requirements and nowhere else.



:strong:`It Hurts When I Do That` 



TDD is -- certainly -- a pain the neck.  I think I see two complaints.  First, it's a lot of "extra" code.  I'm guessing that there's a "non-deliverable" view of test cases that pervades some people's thinking.  I've been measuring the lines of code in both parts of a project, and the total volume of source is about 50% test cases and 50% operational.



Many years ago, we made a distinction between "deliverable" and "non-deliverable" software.  We used to carefully segregate any non-deliverable software so that we could wring our hands over how to estimate the cost for it.  Since it wasn't "deliverable," some managers felt we couldn't charge the customer for it; the logical conclusion was that we should exclude it from our project plans.



I maintained that "non-deliverable" is still "essential", so we must include it in our plans.  The "compromise" was to inflate the estimated size of the deliverable to include a pro-rated version of the non-deliverable code.  The claim was that non-deliverable software was half the cost of deliverable software.  It had less documentation and less testing or some such.



:strong:`I Can't Cope With That` 



The second complaint seems to be that programmers can't be trusted.  Because they can't be trusted, we must have full definitions of all deliverables, complete up-front design, rigorous schedules for code creation, and a fungible, compressible schedule for testing.



We can't engage in an agile test-driven process for a number of reasons.  First, and foremost, programmers are the root cause of scope creep.  We all know that programmers will "gold-plate" the simplest thing; they'll spend years polishing and improving something of limited business value.  [Why did we let them get started on something of limited value?  Why aren't we willing to invest in making it work correctly every time?]



We can't trust programmers to do just enough design because they are lazy slobs and won't ever get anything to work.  If we try to let them fire at half-cock, they'll never get anything useful accomplished. After all, we -- as managers -- have a vision of something trivially simple.  The programmers keep introducing some technology nuance that makes a simple thing horribly complex and difficult.  [Who -- specifically -- told us that introducing new technology will be simpler?  Or did we just make that part up?]



We can't trust programmers to evolve code, design and test hand-in-hand.  If we did, there'd be scope creep and they'd just play with the technology.  Worse, of course, they'd miss the schedule.



We certainly can't trust programmers and end-users to collaborate.  If we did, they would change the focus of the project, and the schedule might be missed.  As managers, we don't fully understand the business value proposition; we don't completely get the technology, but we do understand the schedule.  Since we really, truly, deeply understand the calendar, that is the one thing we can manage to.  [Why is schedule more important than delivered features?]



Above all, we can't trust programmers to create test cases.  Only end-users can create tests, and those tests must be married to the requirements.  There's no reason to elaborate the tests to match the design, or elaborate the tests to match the details embodied in the code.  Tests based on design or programming amount to letting a programmer do their own tests; programmers are untrustworthy; therefore this can't work.



:strong:`The TDD Alternatives` 



I think there's just one disconnect underlying this.  This disconnect manifests itself as two alternatives to TDD.  The static language folks seem to like the idea that compiler type-checking is an alternative to testing.  I suppose -- to a limited extent -- this is true.  Rather than write a unit test to examine proper integration among classes or modules, we can trust the compiler.



Everyone knows -- or should know -- that the compiler is easily fooled.  When using externally developed JAR files, we can easily compile against one version, and try to execute against a different version.  All the compile-time type-checking in the world can't cope with mis-configuration.  Eventually, we need Python-style dynamic testing.



When we can't trust our programmers, we have a number of clever alternatives to TDD.  The primary approach is to define a process that imposes a waterfall approach to developing unit test cases in parallel with the code.  When asked "How does TDD interact with requirements gathering?" no answer I could give was acceptable.  What they wanted me to say was "Oh crap, you're right, I'm such an idiot.  Test cases are only based on requirements, never design or programming."  They wanted me to agree that programmers can't be allowed write their own test cases.



:strong:`The Disconnect` 



I think both viewpoints stem from looking at testing as "final", "end-user" or "acceptance" testing.  If testing is only for acceptance, then we should have other ways to test that the programming is correct and the design really works.  The compiler should -- somehow -- validate our basic programming via static type analysis.  The design, similarly, should be checked via some static analysis.  That leaves testing to focus on the requirements and nothing else.



Additionally, we can't trust one person to interpret the requirements as test cases and as code.  We must apply a second pair of eyeballs to the requirements to create the acceptance-oriented test cases.  



It appears to me that TDD is dismissed as worthless because people don't see a need to test their designs or programming.  Either they hope that static type analysis will do this, or they simply dismiss this testing as worthless.



It's hard to create a value proposition for testing the design and programming.  It requires emphasizing a sense of distrust.  And the level of distrust is already fairly high.  After all, unit testing requires a level of discipline that programmers are unwilling to adhere to.  The idea of adding testing at the design and code level only gets into complex philosophical discussions about "the role of requirements".



It's hard to break testing free from "End-User Acceptance."  However, if we can portray testing as essential, it then becomes deliverable.  Indeed, it becomes essential to establishing confidence in the software.  It also becomes part of the documentation, since each API is demonstrated by at least a test case (in some cases, a whole test suite.)



:strong:`Meta-Quality` 



The logical conclusion is a set of meta-quality attributes.  Software quality attributes can be based on the SEI Quality Measures Taxonomy http://www.sei.cmu.edu/str/taxonomies/view_qm.html.  This taxonomy includes need satisfaction, resource use, maintainability, adaptability and cost factors.



Meta-quality includes the quality attributes of the test cases.  There are probably a number of quality attributes regarding things like 'traceability to requirements", "class coverage" and "method coverage" that determine how useful and complete the test cases are.  Looking at "traceability", we examine how the test cases apply to end-user acceptance. 



I look at "class coverage" as  a way to to look at the design.  This includes classical "class-in-isolation" unit tests, as well as module- (or "component" or "package") -level unit tests that examine a collection of classes to be sure that they interact properly.  This makes limited use of mock objects, since this is looking at integration of classes and modules.



The "method coverage" is how we look at the programming.  This includes appropriate test cases to exercise each method more-or-less in isolation.  This level of testing makes heavy use of mock objects to be sure that the code in each method is actually correct.



I think that these meta-quality attributes of the test case code is as important as the quality attributes of the "operational" code.





