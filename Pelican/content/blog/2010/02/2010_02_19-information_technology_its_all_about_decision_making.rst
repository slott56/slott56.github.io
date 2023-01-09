Information Technology -- It's all about Decision-Making
========================================================

:date: 2010-02-19 08:00
:tags: dimensional data,design
:slug: 2010_02_19-information_technology_its_all_about_decision_making
:category: Technologies
:status: published

Check this SD Times article out: `Future of data analysis lies in tools
for humans, not automatic
systems <http://www.sdtimes.com/link/34139>`__.

    "Andreas Weigend... said that “data is only worth as much as the
    decisions made based on that data."

This is the entire point of IT: **IT Systems Support
Decision-Making**. The job is not to "automate" decision-making with
a bunch of business rules. The job is to create systems to support
decision-making by people. Buying a tool that allows "end-users" to
drag and drop icons to create workflows and business rules misses the
point. Automating everything isn't helpful.

Information should be classified and categorized to *facilitate*
decision-making.

People need to be in the loop.

Management by exception can only happen when people see the data, can
analyze, categorize, summarize and -- by manipulating the data --
discover outliers and unusual special cases.

Too many systems attempt to leave people out of the loop.

**Business Rules**

A canonical example of business rule processing is credit checks or
discounts in an order processing system. This requires integrating a
lot of information, and making a decision based on ordering history,
credit-worthiness, etc., etc.

In some cases, the decision may be routine. But even then, it is
subject to some review to be sure that management goals *are* being
met. Offering credit or discounts is a business strategy decision --
it has a real dollar-valued impact. A person owns this policy and
needs to be sure that it makes business sense.

These decisions are **not** just "if-statements" in BPML or Java or
something. They are larger than this.

One good design is to queue up the requests, sorted into groups by
their relative complexity, so a person can view the queues and either
make (or confirm) the automated decisions. It's a boring job, but
they're doing management by exception. They own the problems, the
corner cases, the potential fraud cases, the suspicious cases. They
should have an incentive payment for every real problem they solve.

You give up "real-time" because there's a person in the loop. For
small value, high-volume consumer purchases, you may not want a
person in the loop. Most of us, however, are not Amazon.com. Most of
us have businesses that are higher value and smaller volume. People
will look at the orders anyway.

All IT Systems must facilitate and simplify manual review. Even if
they can automate, the record of the decisions made should be trivial
to review. Screen shots or log scraping or special-purpose
audit/extract programs mean the application doesn't correctly put
people into the process.

**"Automated" Data Mining**

In most of the data warehousing projects I've worked on, folks have
been interested in the idea of "automated data mining" discovering
something novel in their data. For example, one of the banks I worked
with was hoping for some kind of magical analysis of risk in their
loan portfolio.

Data Mining is highly constrained by the implicit causal models that
people already have. There's a philosophical issue with attempting to
correlate random numbers in a database and then trying to reason out
some theory or model for those correlations. The science of going
from observation to theory requires actual thinking. There's a long
analysis here:
http://theoryandscience.icaap.org/content/vol9.2/Chong.html.

Indeed, the only possible point of data mining is not to discover
something completely unexpected, but to confirm the details of
something suspected but hidden by noise or complexity. People
formulate models, they confirm (or reject) them with tools like a
data warehouse with some data mining analytics.





