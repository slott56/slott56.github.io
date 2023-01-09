Essay 10.2 - When a Column is Not a Column
==========================================

:date: 2005-09-27 10:41
:tags: architecture,design
:slug: 2005_09_27-essay_102_when_a_column_is_not_a_column
:category: Architecture & Design
:status: published





Sometimes a column is not the atomic piece of
data you thought it was.  See `Essay 10.1 <{filename}/blog/2005/09/2005_09_14-essay_101_when_a_column_is_not_a_column.rst>`_  for the first part of this rant,
which address multi-dimensionality.



A
second example of a column not being an atomic piece of data is when we have to
support navigation through a tree (or graph) of information.  In this case, you
could represent the entire thing as a join table of parent and child
pairs.



 

..  csv-table::

    "parent","child"
    "top","child 1"
    "top","child 2"
    "child 1","child 1.1"
    "chile 1","child 1.2"

    







While correct,  no one can easily navigate that structure in pure SQL.  You either have to resort to proprietary extensions to the SQL, or hope that your visualization tool is up to the job.

You can do a transitive closure on this structure and expand the columns to show multiple generations of parents and children.  You can call this limiting -- it isn't first normal form.  However, it's derived from the proper 1NF view and is merely an aid to navigation



..  csv-table::

    "level 0","level 1","level 2","level 3"
    "top","Child 1","Child 1.1"," "
    "top","Child 1","Child 1.2"," "
    "top","Child 2","Child 2.1","Child 2.1.1"
    "top","Child 2","Child 2.1","Child 2.1.2"

    








This structure is what most people
think of when the think of a hierarchy.  The down side of this presentation is
the hand-wringing that goes with maintenance.  After all, they wouldn't be
considering a data warehouse if they had this hierarchy problem solved.  The
transitive closure algorithm is painful to explain, so an example like this can
help understand the mapping from a small, easily maintained, normalized piece of
data to this, denormalized representation of the same data.








