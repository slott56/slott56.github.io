Architectural Principles, Spring Framework, and Jersey JAX-RS
=============================================================

:date: 2014-12-04 08:00
:tags: java,spring framework
:slug: 2014_12_04-architectural_principles_spring_framework_and_jersey_jax_rs
:category: Technologies
:status: published

| See this: `http://www.moschetti.org <http://www.moschetti.org/>`__
| Attended a meeting with Buzz. Not stated in his blog (in an obvious
  way) was something he said about not being a fan of big frameworks. I
  didn't write down his punchline, but it was a pretty pithy summary of
  the framework tradeoff.
| IIRC, it was essentially this: you can wrestle with one or both of
  these technical problems.

-  Boilerplate Code
-  A Framework's Conceptual Model

| Either you have to create your own libraries or you have to learn
  someone else's. This is in addition to wrestling with the business
  problem you're supposed to be solving.
| Buzz's point seemed to be that you can often manage your own
  boilerplate more easily than you can come to grips with a framework.
  If one member of your sprint team handles reusable services, you can
  just ask them for a feature. You don't have to spend an hour reading
  other people's struggles.
| After spending three months getting my brain wrapped around Spring
  Framework, I'm inclined toward partial, qualified agreement.
  Frameworks seem to have limited value until you're an expert in using
  them.
| **Layers and Layers**
| When wrestling with a new feature, you are forced to *assume* that
  you've understood its semantics. When you mock a framework element for
  test purposes, you're reduced to hope that your unit tests are
  sufficient. A unit tests of a mocked framework element only tests your
  assumptions. If you're not using the element's API correctly, your
  tests can't show that the framework will break or raise exceptions.
| For new technology, you need to start with a technical spike to
  understand the framework. Then you can write unit tests that test
  against known framework behavior. Then you can write the real code
  that's based on the unit tests that are based on a spike that shows
  how the framework really works.
| Using a technical spike for discovery and debugging can be
  challenging. You don't want to drag around your entire application
  just to create a spike. But you don't want to drop back to a trivial
  "hello world" spike that doesn't really apply to your context. You
  have to balance simplicity against realism.
| For example, making JAX-RS requests to web services is aggravating to
  debug. You can spend many hours looking at boilerplate 401 and 404
  errors wondering what's missing. You can't write the unit tests until
  you finally get *something* to work. Once you have something, you can
  replace real objects with mock objects.
| If you already know JAX-RS features, it's easy. If you already know
  the RESTful service, it's not too bad. If you know neither JAX-RS nor
  the service, you don't have any clue which direction to turn. Did I
  misuse JAX-RS? Is something wrong in the request? Am I missing a
  required header? Did I leave something off the Accept header?
| I finally had to give up creating spikes and debugging RESTful
  requests in Java. It turned out to be simpler to write a version of
  the REST client in Python. I used this to figure out how the real
  service really worked. Given a working Python spike, I could then save
  those interactions for WireMock.
| Once I has a clue how the service worked, I could also write a mock
  server for some more sophisticated experiments.  This was useful for
  debugging problems based on a failure to understand JAX-RS.
| Yes. Rather than struggle with the framework, I wrote the client once
  in Python and then rewrote the client again in Java. It seemed quicker
  than trying to debug it in Java.
| One contributing factor is the 1m 30s build time in Maven. Compare
  that with interactive  Python at the >>> prompt.
| Perhaps a smaller framework would have been better.





