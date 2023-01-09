Twisted Trial
=============

:date: 2005-12-15 17:10
:tags: #python,unit testing
:slug: 2005_12_15-twisted_trial
:category: Python
:status: published





Trial is not really a stand-alone unit test
framework.  It is an extension to unittest focused on the testing needs for the
Twisted framework.



The Trial how-to
http://twistedmatrix.com/projects/core/documentation/howto/testing.html has some information.  More valuable,
perhaps are the API documents http://twistedmatrix.com/documents/current/api/twisted.trial.html.




Because of the asynchronous nature of
Twisted, the Fixture pattern has a rather complex relationship with the Twisted
Reactor.  Also, since Twisted is a framework, not a single application,
components are optional, and the TestSuite pattern is implemented with
considerably more flexibility.








