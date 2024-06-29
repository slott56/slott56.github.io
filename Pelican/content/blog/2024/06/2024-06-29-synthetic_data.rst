Synthetic Data
######################

:date: 2024-06-29 09:22
:tags: synthetic data,python,project
:slug: 2024-06-29-synthetic_data
:category: Python
:status: published

**Book?** Second draft (with tech review comments addressed) off to editors.

**Boat?** Still on the hard during Hurricane Season.

Synthetic Data
==============

I've had a passing interest in data synthesis for decades.

Early on in my career, I figured out how the Z/OS IEDBG utility worked.
See https://www.ibm.com/docs/en/zos/3.1.0?topic=utilities-iebdg-test-data-generator-program.
It synthesized test data according to a number of mainframe-centric rules.

When I started doing DBA work (Ingres, Oracle, DB2, etc.) the need for bulk synthetic data became more profound.
Folks would debate optimization questions without the benefit of **facts**.
They'd suppose the optimizer might use an index or a 2NF demormalization might save some time.

But.

Without data, it's all second-guessing the DBMS algorithms.

..  note::

    This is **not** synthetic data for generative machine learning models.

    That's a possible application, but the focus is on databases, ETL, and data analytics.


New Development
---------------

The real "shoal water without a chart" problem is new development.

You don't have legacy data with which to benchmark anything.

You only have hand-waving ideas of what the data might look like once the application sees some adoption.

And those are often wishful thinking. (Worse, they can be outright lies by folks seeking investment money.)

What To Do?
------------

All design is driven by data. (Remember, when you switch application code, you preserve the data; it's the real value.)

All scalability problems are data-related.

You can use ordinary "Big-O" complexity analysis to design algorithms that are optimal, but you don't know
any actual performance metrics without hardware, software, and -- what's really hard -- data.

The **only** thing you can do is follow this plan:

1. Write your Proof-of-Concept, Spike solution.

2. Synthesize realistic volumes of data with realistic relationships among the values and realistic distributions of values.

3. Benchmark the performance of the POC/Spike with actual data on actual hardware.

4. Continuously monitor performance, establishing new benchmarks with better algorithms or data structures.

Without actual performance benchmarks, you're creating two scalability problems:

- The immediate problem of "can't start using it because it's too slow."

- The subsequent problem of "users are complaining that it's slow."

Okay, How Do I Do It?
---------------------

Which brings us to tools that synthesize data.

This is **not** synthetic data for generative machine learning models.

This is synthetic data for database, bulk ETL, and ordinary statistical analysis performance testing.

I've got a bunch of stuff that I'll be posting to Git with an approach that I think might be useful to others.

It based on stuff I've done before. It includes the results of some lessons learned.

More to come.
