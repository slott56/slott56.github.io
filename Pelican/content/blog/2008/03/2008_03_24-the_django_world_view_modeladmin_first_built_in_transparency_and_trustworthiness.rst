The Django World-View:  Model+Admin First; Built-in Transparency and Trustworthiness
====================================================================================

:date: 2008-03-24 18:24
:tags: #python,database
:slug: 2008_03_24-the_django_world_view_modeladmin_first_built_in_transparency_and_trustworthiness
:category: Python
:status: published







See Michael Hugos "`Think about screens and the data on them to simplify system development <http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=314557>`_ " for some helpful insight on what an "application" really is -- access to data.  Simple transparency is lifted up as a critical value for software.



I liked the "If you don't believe it could be this simple, consider the reasons for your response" insight.  I didn't like Hugos' sample response, "complex code that you can brag about".  I don't think complexity for the sake of complexity is a real problem.  



Complexity can be defined as everything that separates the user from their data.  As Hugos' notes, the data model and the simplest, most direct presentation is the best design.  Everything else is complexity that obscures the real purpose of the software.



Complexity comes from several sources.  I've blogged about complexity `before <{filename}/blog/2005/09/2005_09_03-why_are_things_so_complicated_7_deadly_reasons.rst>`_ , ever since `Mark Grand <http://www.mindspring.com/~mgrand/>`_  gave me the hint that complexity was part of the IT culture.



Here are seven kinds of complexity that get between a user and their data.



1.  :strong:`"The Conflict Is The Problem"`. The inherent conflicts in the relationship between developers and buyers or users make the problem appear complex. Often this is because buyers insist on their solution -- irrespective of the actual problem.  Rather than describe the underlying problem, buyers describe a solution based on their favorite technology.  They insist they have to do this because the job of the business analyst is to translate the business problem to technology terms -- usually oriented around a complex non-solution.  After all, when you try to solve a business problem with a spreadsheet, you've created two business problems.

#.  :strong:`"Fear of Showing Weakness"`. Simplicity isn't valued.  Some aspect of the problem is (or appears) complex, so we need lots of complex software.  Many "business rules" are transient; an orientation around the decisions a person needs to make is more helpful than over-specifying something that handles 1% of the dollar value of an application.  Rather than simply expose the data (and the business process) to the people, we overdesign "automation" that makes the exceptions and special cases a larger and more complex problem than they deserve to be.

#.  :strong:`"Quality vs. Quantity of Ideas"`. It's hard to let go of the first idea, no matter how bad it is.  Someone with deep experience in legacy technology will often be the root cause of complexity.  Just because batch processing was once the vogue doesn't mean it is essential or even necessary.  Many, many things can be handled via an asynchronous message queue rather than an overnight batch process.

#.  :strong:`"Form vs. Function"`. If we fail to define the problem in the first place, we don't know what problem we're solving.  We're left applying technology inappropriately, filling in the form of a solution, manufacturing complexity because we're vague on what the actual function should be.  Rather than simply present data, we feel that application logic is "important" and should be part of the system; simple presentation of data isn't appropriate.

#.  :strong:`"When I Grow Up"`. If we don't have a mature process for solving problems, we're stuck applying inappropriate technology.  Often we're forced into building something prematurely, and the previous problems all surface: we lock onto the first bad idea, we don't back down from that bad idea, it fills the form of software we think we understand.

#.  ":strong:`If I Had A Hammer"`. Tied in with the lack of quality ideas or well-defined problems, we make inappropriate use of tools or solution design patterns; we view all fastener problems as nails because we only understand hammers.  We have very, very sophisticated application software development tools; we don't need to write mountains of code when we have sophisticated technology stacks like Linux/Apache/MySQL/Python and Django.

#.  ":strong:`How Hard Can It Be?"` Failure to assess risks appropriately biases users against a simple solution.  More programming seems -- in some views -- to be less risky.  More automation isn't a solution.  Appropriate controls are more important than volume of software.

Read Thibodeau's "`D.C.'s tax system won plaudits but couldn't stop alleged insider thefts <http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=9066618>`_ ".  Complexity and technology aren't the answer.  Good old-fashioned controls and audits are what matters.  Audits and controls require transparency, not complexity.




