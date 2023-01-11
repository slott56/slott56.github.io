User Interface Testing
======================

:date: 2007-08-14 10:34
:tags: #python,unit testing
:slug: 2007_08_14-user_interface_testing
:category: Python
:status: published







The question seemed simple, which testing framework is the simplest?  The situation is complex.  There's a web application, there are developers and there are testers.  The developers develop, and the testers test.  So far, not so complex.



Here's the complexity.  The testers are pretty focused on manual point-and-click testing.  They didn't like `HttpUnit <http://httpunit.sourceforge.net/>`_ , declaring it too complex.



What's simpler than HttpUnit?
------------------------------



At first blush, my answer was to look at `Selenium <http://www.openqa.org/selenium/>`_ .  This is a widely-used, easily automated toolset for browser and UI testing.  But further conversation showed that this is the wrong approach.



They aren't deeply interested in the kind of cross-browser testing that Selenium does well.  They're more interested in the essential functionality testing that HttpUnit does.  They need to know that the application works with the given target browser.  Articles like "`Selenium rocks - and you don't need it <http://magpiebrain.com/blog/2007/01/28/selenium-rocks-and-you-dont-need-it/>`_ " help to clarify this distinction between Selenium and HttpUnit



My next answer was to look at `Twill <http://twill.idyll.org/>`_ .  Articles like the Advogato "`Introduction <http://www.advogato.org/article/874.html>`_ " are very compelling.



It turns out, though, the real problem isn't "complexity" *per se* .  The real problem is that the testers aren't interested in writing sophisticated test scripts.  They know the application, they know what they want to see, and they don't feel that programming is the best use of their time.



Unit Testing 101
-----------------



This wasn't my idea, I'm just relaying the insight I got from the conversation.  I was busy shilling shamelessly for Twill when the real solution surfaced.



The smart answer isn't to give the testers more tools.  The testers (as currently managed) don't see a need for tools.  The smart answer is to have the developers made officially responsible for unit tests, in HttpUnit (or Twill).  The developers need to put the unit tests into the source tree along with everything else.  They need to run the unit tests themselves.



The official "testers" are now freed from the "test everything" requirement.  Instead, they can now do "guerilla testing" as well as review the unit test logs.



At some point in time -- and at a higher level in the organization -- the testers need to be encouraged to use powerful scripting and unit testing tools as force multipliers.  They can claim that HttpUnit is too complex, but that's because they're looking at the wrong thing.  



They need to see that they can only point and click so fast.  A tool like Twill or HttpUnit can point and click a whole lost faster.  Until they're rewarded for speed, they don't have any incentive to master a tool.  Until they're given the incentive, every tool will be labeled as "too complex".





