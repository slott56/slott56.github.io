Keeping the Customer Satisfied
==============================

:date: 2008-05-14 22:53
:tags: management
:slug: 2008_05_14-keeping_the_customer_satisfied
:category: Management
:status: published







Here's some reference information on the "Cone of Uncertainty".  JB says that Steve McConnell popularized it.  There's an orphaned `wikipedia article <http://en.wikipedia.org/wiki/Cone_of_Uncertainty>`_ , a `note <http://www.construx.com/Page.aspx?hid=1648>`_  on Construx.com's site, an `article <http://csdl2.computer.org/persagen/DLAbsToc.jsp?resourcePath=/dl/mags/so/&toc=comp/mags/so/2006/03/s3toc.xml&DOI=10.1109/MS.2006.82>`_  in the IEEE Digital Library, and an `image <http://www.microsoft.com/china/technet/images/itsolutions/techguide/innsol/images/msfpmd07.gif>`_  on Microsoft's china site.



It's crap.  Why do we use it?  Because it makes our customers happy.



How Wrong Is It?
-----------------



It's crap for a number of reasons.  First, it's gloriously uncalibrated.  The horizontal axis appears like linear time, but it's just a bunch of project phases.  It isn't linear; indeed, it isn't smooth.  Estimates don't change smoothy, they change in jumps -- mostly when a manager asks you to jump.



The vertical axis starts at .25x and 4x.  Random numbers, imbued with deep mystic significance, but no practical value at all.



If I said it would cost anywhere from $25K to $400K I wouldn't finish the presentation.  That level of variability is unacceptable to all rational people.  The next phase ("Vision Approval") suggests that I should have somehow reduced the "uncertainty", and be pitching a plan that could cost anywhere from $50K to $200K.



One, no one would sit still for that range.  As consultants, we're only allowed something in the neighborhood of ±33%.  From $66K to $133K.  Anything larger scares the client (and us).  "Too Risky", everyone says.



Two, who measured projects to determine these numbers?  Where's the raw data?



Non-Linearity
---------------



There is no smooth progression of growing "certainty".  There are scope changes, and lots of them.  To reduce the cost, things are removed or replaced.  With a new scope, there's a new deliverable.  It isn't even sensible to call it the same project when the scope changes.



Example.  I ask you to build a garage for my Bentley, you ask for $12.5 to $200K.  I don't say, "get to work and during the next phase of planning, reduce the range."  I say "what runs the price up so high?"  You think about it and say that the heater and insulation run the price up.  I say "Build a car port, not a garage."



When I changed the scope, it didn't move you down the "cone of uncertainty".  It started a new project, with new deliverables.  Yes, the client and the overall goal ("protect the Bentley") remained the same.  But you can't compare the $200K for an insulated garage with $50K for a carport.  They're unrelated.



Retrospective
--------------



The final issue is that the cone of uncertainty is entirely retrospective.  At no point in the life of the project do you **ever**  say "the remaining costs will be 1.0 *x*."  Instead, you wrap the prediction in the "barring further scope changes" qualifier.



As a practical matter, almost all software projects proceed until cancelled.  I don't think it's possible for there to be (a) a definite scope that is (b) totally achieved and (c) no one can think of a single enhancement.  Since most projects involve negotiation over scope, the project ends when "enough" software has been installed to solve "enough" (sometimes all) of the business problem, and the enhancements don't seem to create "enough" value.



The 1.0x business happens **after**  the end.  After the project is over, and you've added up every line item, you know the final cost.  You'll be hard-pressed to find a definition of the final scope.  And no scope definition ever matches any of the initial scope statement(s).



What Becomes More Certain?
--------------------------



What becomes "more certain" as the project progresses?  Almost nothing.  The staff skills improve, and our understanding gets better.  But scope changes are always a toss of the dice.  Every end-user brain fart randomizes the scope, which causes complete discontinuities in the basis of our estimation.



The essential variability doesn't reduce at all.  Random errors, mistakes, confusion is a permanent feature of human behavior.  Measure everything you want, you'll find that each variable has a gigantic standard deviation.  Productivity, quality, everything varies widely. 



What can change is the number of degrees of freedom.  For the short periods in which the scope is absolutely fixed, each design decision removes some potential variability.



The Decision-Tree of Uncertainty
---------------------------------



What we really have isn't a misleading linear-like "cone" of uncertainty.  What we really have is a big decision-tree of uncertainty.



Let's work backwards.  Ideally, the final decisions will have little overall impact.  These will be deployment decisions that are trivially handled by the software's configuration files: port numbers, host names, authorized users, etc.



Before these decisions are "simple" programming decisions to make speed/memory tradeoff decisions; LinkedList vs. ArrayList, for example.  These decisions are largely independent of the final deployment decisions, by the way, leading to a complex parallel set of trees.



In front of the "simple" programming decisions are design decisions for how to approach loops and decisions.  In front of that are responsibility allocation decisions for how to determine class attributes and operations.  



Before we can make the class design decisions, we have a number of deeply intertwingled architectural decisions.  At this point, a single architectural decision (e.g., REST vs. SOAP) has a profound impact on cost, schedule, and the ensuing tree of decisions.



None of these involve "uncertainty".  What they involve is an inability to work through all alternative moves in the game.  As with chess, we have openings and gambits, but we can't create a complete decision tree from beginning to end of a game.



It May Be A Hack, But Customers Like It
---------------------------------------



Here's the scenario we run into.  The customer has a very poorly-defined problem.  It's hard to determine what the essential business problem really is because everyone's talking about a "project" and "systems" and "applications" and "data mapping" and "conversion" and "loading".  Everyone's thrashing through the technical details, so our estimate is based on the technical unknowns.



We provide a range.  The customer doesn't like the high end.  The presence of a low end focused them on the low end.  If you say $25K to $400K, everyone wants the $400K feature set at the $25K price.  



So we start negotiating.  The customer takes stuff off the table, we reduce the price.  Then, when there's no longer any business value left in the project, they start putting things back on, and complain every time we try to raise the price.



At some point, they either fail to see what's going on and throw us out, or we pull out the Cone of Uncertainty picture.  This makes it look like there's a way to get $400K of features for $25K.  They're both within the "cone of uncertainty".



This is bad, but **everyone**  wants a Bentley at Hyundai prices.



Agility
--------



The solution is to take an Agile approach.  Rather than define a mystical cone, define a spend rate.  The team of 6 costs $500K per year.  They produce something 4 to 6 times each year -- about $100K per "something".  Rather than plan it to death, do the following.



Pick the one thing that will create some value.  Build and deploy that one thing.  Iterate.  It will cost an average of $100K per iteration.  At the end of the year, you'll have spend $500K.  Since each sprint is a stand-alone work effort, feel free to cancel the project at any time.  



Since the first thing delivered will be of value, you'll always be ahead of the game.



"But what's the total cost?" some folks ask.  The question is stupid.  Look at legacy software.  It's been in production for decades.  A team of 2 or 3 has been supporting it for all those years.  What's the total cost of all that maintenance?  The same analysis holds true for new software -- after the first big spending sprints, you'll spend less, but never zero.



There is no "total" cost until you retire the software from service.  And there's uncertainty involved in every change; the variability of human efforts never goes away.




