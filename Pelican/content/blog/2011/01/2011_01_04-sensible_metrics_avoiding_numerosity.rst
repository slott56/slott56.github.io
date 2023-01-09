Sensible Metrics -- Avoiding Numerosity
=======================================

:date: 2011-01-04 07:22
:tags: software process improvement,numerosity
:slug: 2011_01_04-sensible_metrics_avoiding_numerosity
:category: Technologies
:status: published

In general, Software Engineering Metrics are not without value.

Expecting magic from metrics is what devalues them, reducing metrics
to dumb numerosity.

Once code is in production, plenty of metrics are readily available.
For example, the trouble-ticket history tells you everything you need
to know about code that's in production. You don't need anything more
than this.

Also, an attempt to do more statistical analysis of production code
is largely doomed because it appears (to most managers) as zero-value
work.

Software Engineering Metrics (Cyclomatic Complexity, for example) are
used for their predictive power. There's not point in using them for
post-production analysis.

**Metrics as Leading Indicators**

Metrics are a handy filter as part of an overall QA process. The
point is this: sometimes they're a leading indicator of code smells.

Metrics have to be one part of the overall QA process. For example.

#.  All code is inspected.

#.  Code with more suspicious metrics are inspected more closely. Code
    with less suspicious metrics are not inspected as closely.

Now the questions become much more sensible. Can we quantify
"suspicious" to support decision-making by thinking people?

Imagine this scenario. You establish a Cyclomatic Complexity
threshold; you choose 5 as the upper limit on acceptable complexity.

Now what?

You start measuring code as it goes through development. And
everything is between 5 and 15. What does that mean?

Until you inspect all that code, 5 doesn't mean anything.

**Inspect First, Measure Second**

If, on the other hand, you start inspecting every piece of code,
you'll learn a lot.

#.  Some inspections are boring. The code is good. End the meeting;
    move on quickly. (Few things are more awkward than a manager who
    feels the need to control people by using the entire half-hour.)

#.  Some inspections are hard. The code is confusing. Cut to the
    Rework; reschedule.

#.  Some inspections are contentious. Some folks like one thing and
    other folks find they cannot reconcile themselves to this.

What's important is to use metrics to enhance the good stuff and
expose the bad stuff. People still have to make the decisions.
Metrics only help.

Find a metric that brackets the boring stuff to save you having to
inspect every module that's "similar". Cyclomatic Complexity is
popular for this. It's not the only thing, but it's popular. You can
use feature count or lines of code, also. Short and sweet modules
rarely suffer from code smell. But you still have to check them.

Find a metric that brackets the obviously bad stuff to alert you that
something really bad is going on. Intervene and rework early and
often. Large and complex modules are a leading indicator of a code
smell. How large is too large? Inspect and decide.

Find a way to reduce the contention. Metrics -- because they're so
simple -- are harder to fight over. A Cyclomatic Complexity of 20 is
just too complex. Stop arguing and rework it. Often, bull-headed
nerds can find a way to agree to a metrics program more easily than
they can agree to detailed coding standards.

**Which Metric?**

That's the tough problem. In a vacuum, of course, it's an impossible
question.

Given an inspection process, however, adding metrics to tune and
enhance the existing inspection process can make sense.

There are many Software Science metrics. Here's the list:
http://en.wikipedia.org/wiki/Software_metric.

Pick some at random and see if they correlate in any way with
inspection results. If they do, you can trim down your inspection
time. If they don't, pick other metrics until you find some that do.

But only use metrics to support you're code inspection process.



-----

Integration Watch: Using metrics effectively - By ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-03-09 21:13:40.636000-05:00

Integration Watch: Using metrics effectively - By Andrew Binstock -
March 1, 2010 -
http://www.sdtimes.com/INTEGRATION_WATCH_USING_METRICS_EFFECTIVELY/By_ANDREW_BINSTOCK/About_METRICS/34157


Check out

NIST Special Publication 500-235 Struct...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-04-03 07:38:33.916000-04:00

Check out
NIST Special Publication 500-235
Structured Testing: A Testing Methodology Using the Cyclomatic
Complexity Metric
http://www.mccabe.com/iq_research_nist.htm





