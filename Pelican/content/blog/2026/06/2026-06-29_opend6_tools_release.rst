OpenD6 Tools Project -- Released
################################################

:date: 2026-06-29 09:31
:tags: OpenD6,#python
:slug: 2026-06-29_opend6_tools_released
:category: TTRPG
:status: published

I have (finally) released a usable DSL for OpenD6 spells and characters.

See the `OpenD6 <{tag}opend6>`_ tag for a bunch of related content.

See https://github.com/slott56/opend6-tools for the final product.

I doubt there will ever be a PyPI package.
For the few who want to use these tools, use **uv** like this to install it.

..  code-block:: bash

    uv add git+https://github.com/slott56/opend6-tools

If you're not a Python programmer, and aren't clear on what **uv** is,
then you'll need to visit the tutorial at https://slott56.github.io/opend6-tools/_build/html/tutorial/index.html.

Or, perhaps, pick up a copy of *Pivot to Python*

- https://www.amazon.com/Pivot-Python-professionals-beginners-started-ebook/dp/B0DFMT15GY

- https://books.apple.com/us/book/pivot-to-python/id1586977675

- https://play.google.com/store/books/details/Pivot_to_Python_A_Guide_for_Professionals_and_skil?id=fQ6IEAAAQBAJ&hl=en&pli=1


Test Coverage
=============

The test suite statistics are these:

+------------+--------+----------+
| Statements | Misses | Coverage |
+------------+--------+----------+
|    2625    | 15     | 99%      |
+------------+--------+----------+

Five lines are part of a ``NormalizedAspectReference`` class that has so few examples in the published rules, I gave up on testing it.
I think this deserves a test case, but, I ran out of patience.

One line is an obscure parsing situation in ``QualifiedLookup`` that I'm not sure I can contrive a test case for.
It may be a redundant ``if`` statement, replaced by a better regular expression.

I think I overlooked these because they're (to me) obvious generalizations.
Since they don't have **any** examples in the published corpus of spells, they require test cases that are convoluted.
Maybe I'll add them as issues.

-   Two ``Aspect`` base class computations that never seem to get exercised.

-   A default case for a ``MeasureEffect`` descriptive text in the rare case that no notes were provided.

-   A special case for the ``SpeedAspect`` descriptive text when additional text is provided.

What's Next?
============

See the application of these DSLs: https://github.com/slott56/opend6-koe-world-campaign

-  Kingdom of the East worldbook: https://slott56.github.io/opend6-koe-world-campaign/world_book

-  The Bandit King campaign: https://slott56.github.io/opend6-koe-world-campaign/campaign_book_1

This, at the end of all the testing, was the real point of the exercise.
