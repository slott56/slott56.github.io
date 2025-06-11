Comma Comma
############################

:date: 2025-06-11 07:58
:tags: #python,syntax,cel-python,cloud custodian,open source
:slug: 2025-06-11-comma_comma
:category: Python
:status: published

Ugh.

A painful stretch of hours looking for a problem.
Working on this: https://github.com/cloud-custodian/cel-python/wiki/Evaluation-Design.
I need to address a performance problem and upgrade things generally to get them ready for 3.13 and 3.14.

You know how it goes, right?

I touched something "minor" and all kinds of acceptance tests broke beacuse I also broke something central.

The horrible realization was this:

    There Was No Unit Test

When the problem is not found first by a unit test, it means there's a feature that's only tested by the acceptance test suite.

Where do we stand?
==================

Here are the causes for despair.

1. We've got an acceptance test failure.

2. This reveals a gap in the unit tests.

3. This also reveals the stuff doesn't work because I touched *something*.

What to do?
===========

Ideally?  Fix the unit tests.

Pragmatically?  Review the git change history to see what I've touched recently.

Aha. A trailing comma.

There was a ``{key: lambda x: some_expression, ...}`` data structure.
I took the lambda out and replaced it with a proper ``def`` function. With a name.

::

    def some_new_function(x: type) -> type:
        some_exression,

You know how this goes.

Looks good, who can see the ``,``?

Doesn't work. ``tuple()`` shows up in unexpected places.

Big Lesson
===========

Fix the unit tests.
