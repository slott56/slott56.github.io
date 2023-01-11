SOA, Reuse and The Unmeasurable
===============================

:date: 2007-10-08 17:37
:tags: architecture,design,complexity
:slug: 2007_10_08-soa_reuse_and_the_unmeasurable
:category: Architecture & Design
:status: published







I find the value proposition for a Service Oriented Architecture to be agility and simplicity.



See Linthicum's Real World SOA blog postings, specifically "`Core Value of an SOA... <http://weblog.infoworld.com/realworldsoa/archives/2007/10/core_value_of_a.html>`_ "  Here's the interesting quote: "this does not mean that reuse is not a core value of SOA, but its value is much less than we expected,"



In a recent SD Times piece ("`Orchestration is the Key of SOA <http://www.sdtimes.com/article/column-20070915-02.html>`_ "), Linthicum makes the case that a proper SOA architecture has a number of tiers.  The lowest layer is the services tier; these are enduring features of the business, the industry, the regulatory context.  Higher layers include the orchestration or collaboration tier.  Some vendors (Sun's Java CAPS) split collaboration and orchestration tiers.  I prefer to merge them, since I'm not positioning products to prevent overlap.



Here's the important quote: "orchestration itself is really about creating another layer of services that interact to form solutions, which is what SOA is all about".  



This helped me realize the value of a SOA.  It isn't the services.  It's the collaboration among services at a higher level that reveals the value.



So if it's not about reuse, what do we measure to be sure we're actually delivering something of value?



Customer Conversation
---------------------



A recent customer conversation highlighted the reuse issue.  They were responding my "It's not reuse, it's agility" point.  They countered with the simple "of course it's reuse."  And I had an epiphany at that moment.  I tried to dig in to understand their point and realized that reuse is impossible to measure.



"Of course you can measure reuse," they explained.  "You compare the actual project *vs.* how it could have been without the reuse."



I asked "How do you measure the things you didn't build?  You're talking about measuring the things that aren't there.  Who counts the things *not*  built?  What criteria do they use?"



The Bentley Reuse Model
-----------------------



Here's my reuse model.  I call it the Bentley Reuse Model (**BRM**\ ™).



I'll reuse my Subaru Impreza two-door coupe instead of having you buy me a new `Bentley Continental <http://www.carsdirect.com/2006/bentley/continental_gt>`_  for this project.  That reuse is direct ROI that results from engaging me as an architect.  I'd like 1% of that ROI as a project completion bonus.



If you like that, I have an even better reuse model.  It's the Team Bentley Reuse Model (**TBRM**\ ™). 



Every one of your IT staff (all 100 of 'em) will reuse their existing transportation options (cars, public transportation, car pooling, bicycles, whatever.)  Since you no longer have to buy 100 Bentleys, you will have saved a fortune through the reuse I created.  I want my 1% of that savings, which -- interetingly -- is a new Bentley.  



So, you give me the Bentley because I made everyone else reuse their transportation.  And since they're already using this transportation, there's minimal disruption to the established organization.



Where's the New Functionality?
-------------------------------



The hair-splitting over reuse arrives with the "what new thing are we getting?" question.  It's hair-splitting because it still involves measuring something that didn't happen.  It involves creating a counter-factual argument:  "What if we could have written all this code that we didn't actually write?"  "What if pigs flew?"  "What if flying pigs wrote this smaller set of code instead of the big set of code we planned on writing?"



The fantasy is that some bundle of features stems directly from some volume of code at a ratio of 1:1.  [X] features are based on [Y] lines of code.  Through reuse we are somehow able to reduce the volume of code to [rY] where :math:`r < 1`, giving us some new relationship between code and features.



This is a fantasy because -- of course -- we can't ever estimate the amount of code required to deliver any specific feature.  Some features may be available through training of the users.  A feature may be a consequence of using the right framework or the right persistence/ORM tool.  Some features are emergent consequences of other engineering choices.  Is this "reuse" or is this a simple consequence of good engineering?



Isn't a framework reuse?  Isn't a database reuse?  What about xalan?  If we use XSLT based on Xalan, that's reuse, isn't it?  Isn't an operating system a kind of reuse?  



How should we credit our project managers with the technological insight to use an OS, database, framework, or open source project?  Perhaps reuse is too hard to measure.



Measuring Things
----------------



Reuse is a comparison between a potentially dumb development effort and an actually less dumb development effort.  I reject the very idea that a dumb plan is a valid thing to measure.  We need to measure actual things.



If we can't measure reuse, what can we measure?  Can we measure agility? 



I think we can measure agility by looking at our historical trend of delivering features through time and at the expenditure of dollars.  Forget code and forget reuse.  How long does it take to enable users with a feature?



A SOA architecture can put features into the user's hands quicker than a non-SOA architecture.  Here's Linthicum's take: "Orchestration, in context to a SOA, is strategic, leveraging business rules to determine how systems should interact and better leverage the business value from each system through a common abstract business model."  



If we use our SOA framework and tools to assemble a usable application out of services, then we've built something quickly.  We can be agile since we aren't rewriting fundamental services to implement a business change.



Reuse Did Happen
-----------------



Yes, reuse of the services *did*  happen.  I never said it wouldn't.  But, we can't measure the ROI of that reuse.  Therefore, we're not going to try and leverage that reuse as the central value proposition for SOA.



We can measure the ROI of agility, since we put features into the hands of users.  It's the business value of those features that are the value of SOA.




