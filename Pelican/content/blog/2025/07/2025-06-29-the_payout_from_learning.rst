The Payout From Learning
############################

:date: 2025-07-02 15:46
:tags: uml,plantuml,solid,cel-python,cloud custodian,open source
:slug: 2025-06-29-the_payout_from_learning
:category: Architecture & Design
:status: published

.. role:: danger
   :class: text-danger font-weight-bold

.. role:: warning
   :class: text-warning font-weight-bold

The back-story.
See `Coping With Complexity <{filename}/blog/2025/06/2025-06-29-an_investment_in_learning.rst>`_.
See https://github.com/cloud-custodian/cel-python for the code base.

Back around May 26, I created this branch.
Today -- July 2 -- I've got the tests to pass.

BLUF (TL;DR)
=============

I made mistakes.
I spent a lot of time making a some significant mistakes.
I spent :math:`\frac{3}{37} \approx \frac{1}{12}` of the time cleaning it up.

Details
=======

..  csv-table::
    :header: Date,Day,Event

    May 26,1,Open the branch
    June 21,26,Uncover serious problem with the design
    June 29,34,Post about a better design
    July 2,37,All tests pass.

June I posted a a note about this mess on the June 29, reflecting 34 days of frustrating work.
There are important

It took 4 days to clean up the mess. About :math:`\frac{1}{12}` of the overall time.

YMMV, of course.

But. I think a :math:`12 : 1` ratio for getting into trouble and refactoring to fix it is about right.

Next Steps
==========

Celebrate!

Then update the tracking issue (https://github.com/cloud-custodian/cel-python/issues/100) for the project.

I think there are two outstanding issues; neither of them are devilishly complicated.

Sprint Planning
===============

How many story points was this? (As if story points mean something.)

More importantly, imagine a team with 4-week sprints.

This was **not** done in the first sprint.

Now what?

-   A hand-wringing sprint retrospective to ascertain (again) how difficult the future is to predict.

-   A heart-felt sermon on team commitment nad the importance of meeting commitments.

    - Followed by another round of acknowledgement that the future is remarkably hard to predict.

-   A rambling rumination from an old developer (like me) on the importance of detailed design to establish the **right** number of story points.

    - Followed by a good laugh.
      The didn't work for the waterfall approach.
      We rejected that as part of the Agile approach.
      It still won't work.
