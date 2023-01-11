Innovation includes Failure (some organizations call it "Learning", however)
============================================================================

:date: 2008-04-09 13:20
:tags: management
:slug: 2008_04_09-innovation_includes_failure_some_organizations_call_it_learning_however
:category: Management
:status: published








Some reading:



1.  `Flexible Software is Error-Enabling Software <http://www.itworld.com/AppDev/flexible-software-application-design-nlstipsm-080408/index.html>`_ , by Sean McGrath.  If users can make changes, they can make mistakes.  Why would you allow users to make changes?  It's their process, it's their data.  But, everyone in IT is absolutely sure that end users a lying gypsies.  After all, if you give them something like MS-Access, they just go build stuff.  There has to be a middle ground between big, slow, unresponsive corporate IT and end-user hack-arounds.







2.  An excellent book, `To Engineer is Human: The Role of Failure in Successful Design <http://www.amazon.com/Engineer-Human-Failure-Successful-Design/dp/0679734163>`_ , by Henry Petroski.  Yes, it dates from 1992.  However, the basic advice on what happens when you push the envelope is timeless.








3.  ComputerWorld's April 7th edition has two interviews of note. 









First, `The End of the Internet As We Know It <http://www.computerworld.com/action/article.do?command=viewArticleBasic&taxonomyId=17&articleId=314935>`_ , an interview with Jonathan L. Zittrain.  The term "generativity" is used to describe the way in which we use the internet to build new things.  See `The Generative Internet <http://www.harvardlawreview.org/issues/119/may06/zittrain.shtml>`_  in the Harvard Law Review.  The point is that the Internet empowers people to make new things.  It describes an open view of the world, not a closed one.










Second, A Q&amp;A with Bala Iyer, `Google 'stalker' Deconstructs the Secrets to Its Success <http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=315448>`_ .  This emphasizes that some organizations make an effort to learn; they do this in part by not labeling it failure.





Insight
--------


The "Good ideas are Generative", "Generative means creating New Things" and "New things may include Errors" was a new set of connections for me.

All programming languages are generative and allow people to create bad software.  Period.




Let's look at end-user computing.  When I was a kid there was this "Fourth Generation Language" idea: a better programming language would empower end-users.  Of course, they created errors and IT took those tools away from them. Now we have Business Rule engines and BPEL and BPEL editing tools.  Which IT generally keeps locked in the hands of developers and business analysts.  If you let users touch that, they'll create errors.




The users, left to their own devices, invent hellish spread sheets and MS-Access databases.  When someone tackles a business problem with a spreadsheet, they create two problems.

So, all innovation is controlled by big, low IT or it's utterly uncontrollable by IT.  There must be a middle ground.




Generative Tools Manifesto



The middle way -- between stodgy, slow IT and no IT seems to be defined by Agile techniques.  The `Agile Manifesto <http://agilemanifesto.org/>`_  is helpful, but incomplete.  I think that there's another manifesto lurking in this idea of "generativity".



I think this Generative Tools manifesto may capture the innovative strengths in Java, Python, Ruby, PHP and Perl -- as languages.  But it goes beyond mere language, and into tools and the open source ecosystem.





And it goes beyond developer generativity into the "user" realm.  Users are smart and sophisticated.  They will either work with corporate IT or they're work around it.  Corporate IT shouldn't be a barrier to innovation, they should enable it by passing on tools and best practices.

1.  **Transparency**.  For Developers, open source gives us transparency.  So does simplicity, focus, and conceptual integrity.  A good set of tools does one thing well and simply.  For Users, transparency means direct access to data, with minimal interference by "application" software.


2.  **Adaptability**.  For Developers, open standards allow us to build and rebuild in simple, obvious ways.  One big lesson learned is the way that Ant task definitions have a simple interface that permits endless composition without resorting to a shell script or non-Java tool.  Python's `top-level script environment <http://docs.python.org/lib/module-main.html>`_  encourages simple, obvious reuse techniques.  For Users, solutions must be scriptable with an easy-to-use language.

    Python's easy-on-the-eyes syntax makes it the ideal substrate for building a useful Domain-Specific Language.  I've just finished studying `SCONS <http://www.scons.org/>`_ , and see how an elegant DSL can built on **Gold Old Python Syntax** .


3.  **Cost**.  The cost of doing things well should not be higher than stupid hacks.  Stupidity is a tax that is collected after the fact.  We can omit "expensive" configuration control now, but we'll pay for that later when we can't recover the last good release after ill-advised changes.

    Security, testability, configuration management, data management and the like should not involve tools any more complex than what appears to be a shared directory.  


For example, consider testing.  developers often give themselves numerous sandboxes, development, unit test, integration test and quality assurance structures.  But we collect all user-owned data into one bucket: "production".  End users deserve to have data with multiple owners (user QA, user sandbox, training, etc.) similar to the way IT works.




