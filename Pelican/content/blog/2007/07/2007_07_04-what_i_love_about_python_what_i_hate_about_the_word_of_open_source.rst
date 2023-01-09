What I love about Python == what I hate about the word of open source
=====================================================================

:date: 2007-07-04 14:37
:tags: FOSS,open-source
:slug: 2007_07_04-what_i_love_about_python_what_i_hate_about_the_word_of_open_source
:category: FOSS
:status: published







The problem with Python is the vastness of the Open Source community.  You may think you have something cool for `HTML parsing <../C1597055042/E20070702200105/index.html>`_ , but then someone tells you about `Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`_  which already does it.



In my defense, I actually did a version of this HTML parsing back in '02.  Indeed, I even debugged part of Python's original SGML parser because I was trying to unwind MS-Word HTML documents which had odd declarations that stumped the parser.  I even put a patch kit together.  I didn't follow-through very aggressively, since everyone else in Python development actually knows what they're doing, and I'm just a hack.



Recently, I had to resurrect the idea because I needed information encoded in inconsistent HTML.  I knew that my object model wasn't as cool as the xml.dom model.  So I pressed ahead with a rewrite to my original design, using xml.dom, without looking around at the available off-the-shelf, free-or-open-source solutions.



What's worse is that I'm constantly telling my clients that they have to get comfortable with searching for open source solutions rather than wasting their precious in-house programming talent reinventing the wheel.  The requirements for the wheel are well known, design specifications abound, and you have sample implementations available all over the place.  But some of my clients still ask me to help with the requirements gathering for a "device which reduces friction when moving heavy loads."  



:strong:`Beautiful Soup.`



The ``findAll`` method is almost a proper :strong:`Visitor`.  It can apply a function to each node of a subtree.  The function's return value causes accumulation of values; so a function which returns None simply visits every node.



The only significant problem with findAll is that I really need it to use a stateful object, not a stateless function.  Yes, I could make a class which implements ``__call__`` to be my :strong:`Visitor`.  However, the mixture of tags and text all coming into a single anonymous method is a pain in the ass for some applications. 



Also, the implementation of findAll uses the Tag.recursiveChildGenerator, which has explicit stack instead of simple recursion, but that's a personal preference of mine.  Recursion is often considerably faster.  Since there are some variations on how the Soup methods work, the lack of simple recursion may be essential.



:strong:`Next Steps.`



I can do a number of things.  Each of these is based on specific experiences I've had with customers.  These are lessons I've learned about big IT that I'm trying to apply to the open source community.



-   I could dogmatically insist that my crap is better/faster/cheaper.  

-   I could claim that my crap is an "investment" and must be preserved.

-   I could wring my hands about "strategy" in HTML scraping and meticulously investigate the other packages that have sprung up over the 5 years between when I first did this, and now, when it seems like everyone's doing it.  Of course, the yardstick I would use is not something more-or-less objective like my requirements, since almost any package would meet those.  My yardstick must be political, and involve comparison against my solution, which isn't very complete, but does have the :strong:`Visitor`  design pattern.

-   I could ask the vague and misleading question "Where's the ROI for HTML scraping?"  As if the error-prone and non-repeatable process makes more sense than having an HTML scraper that actually gets the actual data off the actual web site.  Further, ROI requires an upper bound on the investment part, which is stupid because software is the lynchpin of an endless business improvement cycle.



Conventional wisdom -- in the open source community -- suggests that I post a patch to Beautiful Soup to add the desired :strong:`Visitor`.  That requires me to dig deeply enough into findAll to see how it really works.  I would have to learn something, and that will take a few weeks.



I prefer to take my cue from in-house IT departments where doing nothing is the preferred course of action.  Open source is too much work.




