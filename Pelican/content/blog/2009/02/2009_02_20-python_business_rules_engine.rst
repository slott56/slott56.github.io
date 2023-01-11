Python Business Rules Engine
============================

:date: 2009-02-20 11:03
:tags: architecture,design,complexity
:slug: 2009_02_20-python_business_rules_engine
:category: Architecture & Design
:status: published







On Stack Overflow I was captivated by "`What tools would you used to write a modular database in Python? <http://stackoverflow.com/questions/532814/what-tools-would-you-used-to-write-a-modular-database-in-python>`_ " and "`Implementing a 'rules engine' in Python <http://stackoverflow.com/questions/467738/implementing-a-rules-engine-in-python>`_ ".



Both questions are quite amazing because they already have a modular, flexible rules engine (called "python") but it's not good enough: they want to use Python to build something that's -- well -- more Python.



It's weirder than `PyPy <http://codespeak.net/pypy/dist/pypy/doc/>`_ , which makes a certain amount of meta-level sense.



Business Rules
--------------



The rules engine question provides a tidy specification for three central features of Python: Regular expression matching, arithmetic comparisons, and Boolean operators.  Then they go on to provide a sample expression that's almost (but not quite) python code.  I'm not sure their tiny syntax change is worth the effort of writing a parser.



In our application, we have a large number of fairly complex business rules.



Worse, we don't have a tidy specification of what those rules **really**  are.  Instead, we have some kinds of flow charts, and some cultural norms, and folks who know a lot about the problem domain.  We could have spent nine months digging.  Instead, I elected to spend nine months programming in Python.  



When things change, the code is easy to change.  Good OO design principles allow us to capitalize in simple **Strategy**  pattern and **Command**  pattern to "plug in" different modules.  In some cases, we've found that we didn't foresee the need for a Strategy plug in and are forced to refactor some packages to reflect what we learned.



Python is our business rules engine.



Modularity
------------



We have a nebulous offering.  Our business model is simple, and based around some smart people who offer a very clever consulting service.  The software packages some of the consulting results in a form that a customer can subscribe to.



Clearly, each customer could be unique.  And our service offering *should*  expand as we get better and better at this.  So we'll have lots of plug-and-play modules for customer-specific features and expansions of the service.



This is what Python does best.  I've already done significant on-the-fly refactoring as we find new opportunities.  Why use Python to build a super-meta "modular" database?  Python already is modular, and so is SQL.



Django's World View
-------------------



One of the best parts of using Django is the "build-the-model-first" world view.  Confronted with requirements, my approach is this.



1.  Build a model that works.



2.  Write unit tests to show how the use cases are implemented with this model.



3.  Write the admin folderol to build a reasonable admin interface for this model.  This actually takes quite a bit of effort to decide what lists and filters to use and where to put the inline forms.



4.  Write RESTful URI's and view functions for our Web Services and our HTML views.



5.  Piss around with templates until we're tired of responding to random tester/user/owner feedback.



Flexible, Modular, Python.





