I hate CSS -- mostly because I don't understand it
==================================================

:date: 2008-10-12 12:27
:tags: architecture,design,UX,UI,GUI,TUI
:slug: 2008_10_12-i_hate_css_mostly_because_i_dont_understand_it
:category: Architecture & Design
:status: published







I found `CSS Systems <http://blog.isotoma.com/2008/10/css_systems.html>`_ , in the Isotoma blog.  Which lead me to `CSS Systems for writing maintainable CSS <http://natbat.net/2008/Sep/28/css-systems/>`_  from Natalie Downe.  That was a "aha!" moment.  The problem is that I've been looking at incomplete, poorly-structured examples.



One problem I have with CSS and XPath is the multiple dimensions of search.  You can be talking about an element, an ID or a CLASS or some combination.   For me, the distinctions aren't obvious enough.  Making therm obvious, however, makes CSS (or XPath) so wordy as to be unusable.  So, I have to get over that.



Another problem that I have with CSS is that the display model for browser pages is really complicated.  The basic HTML markup is delightfully simple, but it has the consequence of making complex structures when rendered on a page.  Worse, of course, is the fact that I started with SGML and also use DocBook XML, which are principally semantic markup with very little display capabilities.  HTML has this mixture of semantic and non-semantic markup.  I try to use semantic markup as much as possible, but it's hard to debug my CSS rules.



I have to teach an HTML/XML class, which will include CSS.  I'd like to include a tool like `CSSEdit <http://macrabbit.com/cssedit/>`_ , but that's Mac-only, and our customer base (with one exception) is firmly anti-Mac.



I will, however, direct them `/* Position Is Everything */ <http://www.positioniseverything.net/>`_ , which was a wonderful resource to discover. Some of the IE stuff has an update date of December 9, 2006, but I don't think any of the bugs have been fixed.  Indeed, the newest IE's preserve the old bugs for "compatibility".



[A bug is an undocumented feature; by preserving the old bugs, they become features.]



Perhaps the style editing in Eclipse will help.  Also, I've found `Amaya <http://www.w3.org/Amaya/>`_ , which might help teach people (like me) how to control the features of CSS.





