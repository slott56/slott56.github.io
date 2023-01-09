Unit Test Naming [Updated]
==========================

:date: 2014-01-01 13:22
:tags: unit testing,tdd
:slug: 2014_01_01-unit_test_naming_updated
:category: Architecture & Design
:status: published

Just stumbled across several blog postings on unit test naming.


Essentially the TestCase will name the fixture. That's pretty easy to
understand.


The cool part is this: each test method is a two-part clause:
``condition_"should"_result`` or ``"when"_condition_"then"_result``.


See https://wiki.openmrs.org/display/docs/Unit+Testing+With+at-should+Annotation,


Or possibly "``method_state_behavior``".


http://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html


What a handy way to organize test cases. Only took me four years to
figure out how important this kind of thing is.

[*Updated to follow moved links.*]



-----

Have you tried the spec plugin for nose? It gives ...
-----------------------------------------------------

boothead<noreply@blogger.com>

2009-10-22 04:35:02.992000-04:00

Have you tried the spec plugin for nose? It gives you a really good
understandable output for nosetests:
http://darcs.idyll.org/~t/projects/pinocchio/doc/#spec-generate-test-description-from-test-class-method-names





