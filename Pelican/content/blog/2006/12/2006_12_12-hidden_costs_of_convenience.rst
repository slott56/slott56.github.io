Hidden Costs of "Convenience"
=============================

:date: 2006-12-12 16:19
:tags: architecture,software design,complexity
:slug: 2006_12_12-hidden_costs_of_convenience
:category: Architecture & Design
:status: published





This is an important topic.  I've blogged on the
layers issue before ("`Layers, Interfaces and Mutabilty <{filename}/blog/2006/10/2006_10_20-layers_interfaces_and_mutability.rst>`_ "), and this
AJAX issue is a great additional
point.



With depressing regularity I
also hear the complementary "stored procedure" question.  This question takes a
number of different forms, but they all mean the same thing.  Here are some
alternative formulations:

-   Where should the "business logic" live? 
    Stored procedures or application code?

-   What kinds of "business logic" are best
    to encode in stored procedures?

-   How can we make best use of evolving
    stored procedures?

-   How can we implement a `common code base without a consistent data
    model <{filename}/blog/2006/10/2006_10_11-absurdity_consistent_code_and_inconsistent_data_structures.rst>`_ ?



In essence the question has a hidden assertion: Stored procedures are handy, but we need to justify them.



Bad Business
------------



Stored procedures, like
AJAX, are an accident waiting to happen.  The ideal is that AJAX is pure
presentation and stored procedures are pure persistence.  As a practical matter,
bleed-through is inevitable.  As soon as the line is crossed, that piece of code
becomes a costly stumbling block that prevents change and adaptation.



When we bury business rules
in the front-end, we slow down the pace of change.  Even in a simple STRUTS
application, the biding between JSP and JavaBean makes some kinds of changes
more difficult than others.  If the JSP expands to include any business logic at
all, the changes to the business rules either spread between application and
presentation (doubling the cost), or we stop making changes to the presentation
because it's too complex to change.



When we bury business rules in
stored procedures, we also slow down the pace of change.  We are stopped from
making logical database changes because of the impact on our stored procedures.



The convenience items like
AJAX and stored procedures turn out to be bad business from IT's perspective. 
While AJAX is fun for the users, stored procedures are invisible to the users. 
Stored procedures are short-term fun with long-term costs.




Worst-Case Scenario
-------------------



Think about this kind of
worst-case scenario.  Some non-thinker declares that the each person will have
home phone, work phone, mobile phone, fax and email, and that's the end of it. 
One will be marked "preferred".  This is clearly unsuitable for a lot of CRM
purposes because it ignores people who share email addresses, and the use of
instant messenger as a preferred channel.



The DB designer puts five (5)
fields in the database for communication channels; they write stored procedures
to create a person with five (5) points of contact, assuring that the email
address is the unique "natural key".  The GUI designer lays out five fields and
assembles a bunch of widgets to validate the various data types and assure each
is unique.  The application developer validates each field before passing it to
a stored procedure, and assures that all five form a unique combination.



Clearly, everyone's wrong about some nuance, but it's suddenly very difficult to make changes.
Each has encapsulated a business assumption into code where it doesn't belong.




Unit tests will likely work, since the
most common scenario for use lies at the intersection of the nuanced rules. 
However, as soon as we make a change, we uncover problems.  Worst, of course,
the problems are not in our code, but in someone else's code, and we can't quite
pinpoint the problem.  Things just don't work right.



No one can disentangle this
without forcing a rewrite that eliminates features.  Who wants to eliminate
features?  If we're going eliminate features, we might was well just throw away
the whole GUI or Database (pick one).  Why do we have a rich GUI or Database
(pick one) if we're not going to make full use of every
feature?



A Better Case
-------------



A Better Case is for GUI
designers to make generic, reusable widgets.  The phrases "Application-neutral"
or "application-agnostic" are too weak.  They have to be openly antagonistic to
any particular application.  The power of HTML and SQL is that they are so
neutral as to be irritating.  In a similar way, we need to carefully partition
our application into layers which are loosely coupled and only reflect the truly
immutable features of that layer.



The persistence layer is focused on just making business entities persistent.  Other
features of the entity, like natural keys, are outside the database's realm. 
Similarly, relationships have a low-level representation (as a link or foreign
key), but any other constraint (cardinality, optionality, etc.) isn't part of
persistence, but is a business rule that's bleeding through to the wrong
layer.



The presentation layer makes the
business object visible, and little else.  While rich input validation is fun,
there are limits to what can be done meaningfully, and what is subject to change
without notice.  Data types (i.e., email address, telephone number) don't
change.  Other rules regarding uniqueness, identity, cardinality and even
optionality, aren't enduring features of the presentation.  They're business
relationships that can (and will) change.



AJAX and Stored Procedures both
have the potential to thwart change, making them costly.  The cost of adaptation
to new business requirements must be factored in to the design of every layer.












