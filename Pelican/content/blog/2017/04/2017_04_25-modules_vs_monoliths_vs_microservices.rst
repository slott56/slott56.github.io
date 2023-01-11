Modules vs. Monoliths vs. Microservices: 
=========================================

:date: 2017-04-25 08:00
:tags: gherkin,#python,tdd
:slug: 2017_04_25-modules_vs_monoliths_vs_microservices
:category: Technologies
:status: published

Tweet:

    .. image:: https://pbs.twimg.com/profile_images/779041781413507072/TaqJsdzS_normal.jpg
        :alt: Twitter Avater

    **Dan Bader(**\ `@dbader_org <https://twitter.com/dbader_org?refsrc=email&s=11>`__\ **)**

    `4/21/17, 7:35 PM <https://twitter.com/dbader_org/status/855565565485887488?refsrc=email&s=11>`__


Worth a read: "Modules vs. Microservices" (and how to find a middle ground)

`oreilly.com/ideas/modules-… <https://t.co/5qrDhkSl7R>`__

    "don't trick yourself into a microservices-only mindset"

Thanks for sharing.

The referenced post gives you the freedom to have a "big-ish"
microservice. My current example has four very closely-related
resources. There's agony in decomposing these into separate services. So
we have several distinct Python modules bound into a single Flask
container.

Yes. We lack the advertised static type checking for module boundaries.
The kind of static type checking that doesn't actually solve any actual
problems, since the issues are always semantic and can only be found
with unit tests and integration tests and Gherkin-based acceptance
testing (see Python BDD: https://pypi.python.org/pypi/pytest-bdd
and https://pypi.python.org/pypi/behave/1.2.5).

We walk a fine line. How tightly coupled are these resources? Can they
actually be used in isolation? What do the possible future changes look
like? Where is the swagger.json going to change?

It's helpful to have both options on the table.




-----

great
-----

Mary Brown<noreply@blogger.com>

2019-10-09 09:50:54.913000-04:00

great





