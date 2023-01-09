Finally Planning the Rewrite of Building Skills in Object-Oriented Design
=========================================================================

:date: 2019-09-03 08:00
:tags: building skills books
:slug: 2019_09_03-finally_planning_the_rewrite_of_building_skills_in_object_oriented_design
:category: Technologies
:status: published


See `Building Skills in Object-Oriented
Design <http://www.itmaybeahack.com/buildingskills/oodesign.html#book-oodesign>`__
for the old content, which has a number of features that hold up well
over time.

#. A graduated series of exercises to build up large, complete
   applications is important.

#. It covers a lot of skills essential to building real applications --
   unit testing, integration, code reuse. I want to expand on this to
   include more testing strategies, and final documentation.

#. It's so popular, I've got enough donations to move forward on a
   rewrite.


Previously, it was hosted out of my ancient web site as HTML and PDF
download. That hasn't aged well.


Also, it was originally Python 2, and that ship sailed years ago.


I'm leaning toward hosting the content on GitHub.


One idea is to have a complex project with the following top-level
folders:


-   A ``docs`` folder that has the HTML as well as PDF (and maybe an ebook
    format, too.)

-   A ``src`` folder with seed files for the various packages and modules.

-   A ``tests`` folder with seed tests.


Someone could fork and then build on the framework.


It's possible to put the exposition into the wiki pages associated
with the repo. This has the advantage of keeping the meta-level
documentation and individual project requirements separate from the
project itself.


Before I go too far, I'll need to experiment a bit to see what the
editing process is like. The Github wiki pages are their own git
branch, and are easy to edit off-line and push to the repo. Some of
the fancy Sphinx markup features vanish, replaced with basic RST.
This may not be all bad, since the baseline content is not \*very\*
complex.


Stand by for more.






