Testing with PySpark
#####################

:date: 2022-11-22 11:00
:tags: unit testing,pySpark,gherkin,#python
:slug: 2022_11_22-testing_with_pyspark
:category: Technologies
:status: published

This isn't about details of pySpark. This is about the philosophy of
testing when working with a large, complex framework, like pySpark,
pandas, numpy, or whatever.

BLUF
====

Use data subsets.

Write unit tests for the functions that process the data.

Don't test pyspark itself. Test the code you write.

Some History
============

I've worked with folks -- data scientists specifically -- without a deep
background in software engineering.

When we said their model-building applications needed a **test case**,
they supplied the test case they used to validate the model.

Essentially, their test script ran the entire training set. Built the
model. Did extensive statistical testing on the resulting decisions made
by the model. The test case asserted that the stats were "good." In
fact, they recapitulated the entire model review process that had gone
on in the data science community to get the model from "someone's idea"
to a "central piece of the business."

The test case ran for hours and required a huge server loaded up with
GPUs. It cost a fortune to run. And. It tended to timeout the deployment
pipeline.

This isn't what we mean by "test." Our mistake.

We had to explain that **a unit test demonstrates the code works**. That
was all. It shouldn't involve the full training set of data and the full
training process with all the hyperparameter tuning and hours of compute
time. We don't need to revalidate your model. We want to know the code
won't crash. We'd like 100% code coverage. But the objective is little
more than show it won't crash when we deploy it.

It was difficult to talk them down from full training sets. They
couldn't see the value in testing code in isolation. A phrase like "just
enough data to prove the thing could plausibly work with real data"
seemed to resonate.

A few folks complained that a numpy array with a few rows didn't really
show very much. We had to explain (more than once) that we didn't really
want to know all the algorithmic and performance nuances. We mostly
wanted to know it wouldn't crash when we applied it to production data.
We agreed with them the test case didn't show much. We weren't qualified
to revalidate the model; we were only qualified to run their training
process for them. If they had done enough work to be sure we \*could\*
run it.

(It was a bank. Software deployments have rules. An AI model-building
app is still an app. It still goes through the same CI/CD pipeline as
demand deposit account software changes. It's a batch job, really, just
a bit more internally sophisticated than the thing that clears checks.)

Some Structure
==============

I lean toward the following tiers of testing:

#. Unit tests of every class and function. 100% code coverage here. I
   suggest using ``pytest`` and ``pytest-cov`` packages to tracking
   testing and make sure every line of code has some test case. For a
   few particularly tricky things, every logic path is better than
   simply testing lines of code. In some cases, every line of code will
   tend to touch every logic path, but seems less burdensome.
#. Use ``hypothesis`` for the more sensitive numeric functions. In “data
   wrangling” applications there may not be too many of these. In the
   machine learning and model application software, there may be more
   sophisticated math that benefits from hypothesis testing.
#. Write larger integration tests that mimic ``pyspark`` processing,
   using multiple functions or classes to be sure they work together
   correctly, but without the added complication of actually using
   pySpark. This means creating mocks for some of the libraries using
   ``unittest.mock`` objects. This is a fair bit of work, but it pays
   handsome dividends when debugging. For well-understood ``pyspark``
   APIs, it should be easy to provide mocked results for the app
   components under test to use. For the less well-understood parts, the
   time spent building a mock will often provide useful insight into how
   (and why) it works the way it does. In rare cases, building the mock
   suggests a better design that's easier to test.
#. Finally. Write a few overall acceptance tests that use your modules
   and also start and run a small ``pyspark`` instance from the command
   line. For this, I really like using ``behave``, and writing the
   acceptance testing cases using the Gherkin language. This enforces a
   very formal “Given-When-Then” structure on the test scenarios, and
   allows you to write in English. You can share the Gherkin with users
   and other stakeholders to be sure they agree on what the application
   should do.

Why?

Each tier of testing builds up a larger, and more complete picture of
the overall application.

More important, we don't emphasize running pySpark and testing it. It
already works. It has it's own tests. We need to test the stuff we
wrote, not the framework.

We need to test our code in isolation.

We need to test integrated code with mocked pySpark.

Once we're sure our code is likely to work, the next step is
confirmation that the important parts do work with pySpark. For
life-critical applications, the integration tests will need to touch
100% of the logic paths. For data analytics, extensive integration
testing is a lot of cost for relatively little benefit.

Even for data analytics, testing is a lot of work. The alternative is
hope and prayer. I suggest starting with small unit tests, and expanding
from there.





