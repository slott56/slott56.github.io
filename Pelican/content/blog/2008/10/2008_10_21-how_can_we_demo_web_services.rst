How can we demo web services?
=============================

:date: 2008-10-21 22:47
:tags: architecture,software design,UX,UI,GUI,TUI
:slug: 2008_10_21-how_can_we_demo_web_services
:category: Architecture & Design
:status: published







The obvious answer is that we need a customer-like demo site that shows how the customer's software interacts with our software.



The problem is that it's a totally back-office kind of relationship.  Worse, we don't have solid use cases.  We have working software for some use cases, but every conference call with the sales team leads to -- well -- confusion.



Use Case 1.  Customer sales person sits down at their workstation, decides to sell some product, and in the process of the sales call, gets information from us that adjusts the pricing, terms or conditions of the sales process.  



Use Case 2.  Customer marketing person sits down at their workstation, decides to market some product.  In the process of developing the campaign, gets information from us that adjusts pricing, terms or conditions.  What does the marketing person see?  A long delay while their campaign goes to us and comes back with prices.



Demo Problems
-------------



We can't demo the sales process very well because they don't see much.  Just a "better" price or terms or something.  But there's no before/after kind of thing.



Worse, our mock-up of a sales person's application software won't match anything any of our customers have, we'll spend the whole sales call arguing about the data elements, the format, the color of the background and the labels on the buttons.



We can't demo the marketing process very well because (a) it's overnight and (b) it's still invisible.  If we do it in seconds, it sets a false expectation.



Pilot Instead of Demo
----------------------



What we have to do is to get the sales folks away from demo and into pilot.  And the best way to do this is to refine our extensibility features so that we can spin up a new pilot really quickly.  



We're using Python, so parsing spreadsheets, loading database, and customizing a Django configuration shouldn't take too long.  I'm hoping that we can get a pilot ready in about as much time as it takes to schedule a "Big Demo" with the decision-makers.



Besides, a pilot will show real results for a subset of situations.  It won't show a glossy walk-through of some use cases.  



The problem is that our sales folks are used to Java-scale development where every change takes a month.  At this point, the only thing that will win their hearts and minds is to really deliver on the first few pilots.





