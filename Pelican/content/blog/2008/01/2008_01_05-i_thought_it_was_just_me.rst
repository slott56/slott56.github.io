I Thought It Was Just Me
========================

:date: 2008-01-05 14:52
:tags: architecture,design,unit testing,tdre
:slug: 2008_01_05-i_thought_it_was_just_me
:category: Architecture & Design
:status: published







See Scott Ambler's article in `Dr. Dobb's Journal <http://ddj.com>`_ , "`Scaling Test-Driven Development <http://ddj.com/architect/205207998>`_ ".



Recently, I'd seen some notes in SD Times on a similar theme, and blogged that in `Not Quite Following the Book <{filename}/blog/2007/12/2007_12_07-not_quite_following_the_book.rst>`_ .



Ambler's point seems to be the same as Coplien's: "High-level architecture sketches created during your Iteration 0 envisioning activities help set your initial technical direction—a little bit of up front design work helps to avoid structural problems cropping up later in the lifecycle."  It isn't very efficient to use the fine-grained approach of "pure" TDD to get to a good architecture.



It's certainly possible to simply work from the ground up, using testing and refactoring to arrive at a good architecture.  Many people have done this on smaller projects.  I think that this exact experience -- refactoring the presence of reasonably complete test cases -- is what sells TDD.



It's clearly smarter to pitch an architecture early on and get everyone to internalize that architecture.  Each piece of functionality is born with a bias toward fitting into some architecture.  It's best to fit into a common architecture.  Devastating change is reduced (not prevented, but reduced.)



Bonus!  People seem to prefer to do it this way.  I'm absolutely sure that they understand the **Agile Theory**:  anything can be accomplished by working from the details up.   I'm also absolutely sure that they've adapted this foundational theory into a process that reflects practical considerations of the composition of the team and the schedule for delivery of working software.



A Reasonably Agile Lifecycle
-----------------------------



Purely Agile TDD is based on a series of practices that will -- eventually -- yield great software.  We can, however, impose some additional practices that will reduce the value of "eventually" to something a little more palatable.  These practices seem to be the following.



**Consolidated Analysis**.
    While disjoint use cases can be knit into a cohesive whole, it's good to review and reconcile the use cases.  I suggest that an analysis model be built to capture the essential nouns and verbs in the use cases.  I need to emphasize "essential": don't model everything; model the recurring themes, central concepts, and essential ingredients.  This model is NOT (emphasize NOT) a "deliverable" in the sense that code and test cases are deliverable.  This isn't a milestone; if it was, we wouldn't be Agile.  This is merely a tool to help us frame up each use case into a context.  This captures the domain knowledge that users assume and we have to gain.  This consolidated analysis model **is**  how we gain domain knowledge.



**Architectural Overview**.
    While we can refactor our way into a decent architecture, this isn't an optimal use of anyone's time.  If the app is web-based, we -- generally -- embrace some framework before we even get started.  We rarely just start coding and hope that a web app appears.  The architecture is NOT a deliverable; it's a context into which each delivery will fit.  Again, this can't be a milestone, since building this becomes a distracting, limited-value project milestone.  The point isn't the architecture, it's the conversation about the architecture, and the impact that conversation has on subsequent work.



**Acceptance Testing**.
    Different from the detailed testing of TDD, we have the end-user's overall acceptance tests.  This is best viewed as a formal, audited, "for the record" rubber-stamping of the application.  It's very formal, since everyone is forced to look at it; we use formality as a way to provide enough background that a diverse audience can get what they're seeing.  An acceptance test isn't a sing-along around the campfire; it's high opera with a libretto and a closed hall and perhaps a brief intermission lecture by a Famous Artist.  It's audited by QA with an official certification that the software is suitable for production use.  It's "for the record" because everyone is notified about the results, even if they didn't actually attend the show.  QA must write the review for the morning papers to describe how the performance went.  And it's just a rubber stamp of testing that was done at a lower level.



Acceptance testing is important because users may not articulate their requirements very well.  Further, developers may not understand the requirements very well.  The Agile approach of a conversation can get bogged down in nuance (or evasion).  A final acceptance test can be a way to manage and focus the conversation.  It doesn't replace the conversation with "a deliverable", it just directs it.



This isn't perfectly Agile.  It involves pre-work that isn't simply a conversation with a user and development of a feature.  It involves elaborate post-work that isn't simply a release into production.  It is somewhat more efficient because time is taken up front to assure everyone agrees and understands the direction.  It is also somewhat more manageable because we have a final performance that belongs more to QA (and the critics) than the users or developers.




