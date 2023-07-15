The world is multidimensional?  Really?
=======================================

:date: 2009-09-15 11:33
:tags: dimensional data,database design,content management
:slug: 2009_09_15-the_world_is_multidimensional_really
:category: Technologies
:status: published

I cannot believe that people still consider top-down, uni-dimensional,
taxonomic hierarchies useful.

This Stack Overflow question (`REST: How to Create a Resource That
Depends on Three or More Resources of Different
Types? <http://stackoverflow.com/questions/1402721/rest-how-to-create-a-resource-that-depends-on-three-or-more-resources-of-differe>`__)
repeats an assumption. Essentially the confusion comes from assuming
that "URI's map directly to a hierarchy".

I think it's over-exposure to the Windows file system where hard
links are a rarity.

Perhaps it's also from over-exposure to hierarchical site-maps that
simply repeat the menu structure without adding information.

Someone who is reading `Everything is
Miscellaneous <http://www.everythingismiscellaneous.com/>`__
suggested I read up on "`faceted
classification <http://en.wikipedia.org/wiki/Faceted_classification>`__"
as if that was something new or different.

What's interesting in Weinberger’s book is (1) recognizing this and
(2) taking some concrete action.

What To Do?
-----------

What's perhaps the most important thing is this

Stop Forcing Things Into Hierarchies
------------------------------------

I sat in a multiple hour meeting where we debated the file-system
structure for artifacts created during a development project. Each
artifact has several dimensions.

-   Phase of the project (Inception, Elaboration, Construction,
    Deployment)

-   Deliverable type (DB Design, Application Programming, Web Site,
    etc.)

-   Status (Work in Progress, Waiting UAT, Completed, Rework, etc.)

-   Calendar (Year, Quarter, Month the work started, as well as ended)

-   Team (DBA's, Batch/Backend, Web/Frontend, ETL, etc.)

Sigh.

Since the data is multidimensional, no single taxonomic hierarchy
can ever "work". Each alternative (and there are 5!=120 ways to
permute five dimensions) appears equally useful.

If you want, you can enumerate all 5! permutations to see which is
more "logical" or "works better for the team". What you'll find is
that they **all** make sense. They all make sense because the
dimensions are all peers -- equally meaningful.

Alternatives
------------

One alternative is to do this.

1. Create a relatively flat structure. Define all your things in
this flat structure. In a Relational Database context, this means
assign surrogate keys to everything, "natural" keys are more
problem than solution. In a content management context, just throw
documents anywhere.

2. Create "alternative" indices via hard links to the flat
structure. Do not limit yourself to a few alternative orderings of
the dimensions. There are *n*! permutations of your dimensions.
Expect to create many of these for different user consituencies.

Remember, Search Exists
-----------------------

Recognize that highly structured metadata fields in a database are
usually a waste of time and money. Search exists. Much data is
unstructured or semi-structured and search functions exist that
handle this nicely.

If you stop force-fitting hierarchies, you find that you have now
have several dimensions. Each dimension has a set of reasonably
well-defined tags. Each document or database fact row is a point
in multi-dimensional space.

A single SQL-style query among these multiple dimensions is a pain
in the neck. Search, however, where the dimensions are implied
instead of stated, is much, much nicer.



-----

sounds like a nice linked data project ;)...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-09-16 01:04:59.094000-04:00

sounds like a nice linked data project ;)
/me is in reading mode of "Programming the Semantic Web" which gives all
examples in Python.


Everything is Miscellaneous by Weinberger, page 12...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2009-09-26 17:19:50.014000-04:00

Everything is Miscellaneous by Weinberger, page 125: "People keep
pretending they cn make things deeply hierarchical, categorizable, and
sequential when they can't. Everything is deeply intertwingled," so said
Ted Nelson.


AKA "labels" or "tags".  They ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-09-15 12:15:25.031000-04:00

AKA "labels" or "tags". They rock. Discuss with your teams first about
which labels they would find useful; make a list of those, standardize
spelling, and go. (For a sufficiently large number of items to
categorize, even standardizing spelling beforehand is unnecessary as the
data will eventually tell you which spelling is important.)


Apple's Flatland Aesthetic by B. Tognazzini...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2009-09-26 20:47:30.958000-04:00

Apple's Flatland Aesthetic by B. Tognazzini
http://www.asktog.com/columns/075AppleFlatlandPart1.html


Quote from page 235 of the book Glut by Alex Wrigh...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2009-09-19 16:09:10.508000-04:00

Quote from page 235 of the book Glut by Alex Wright: In other words,
hierarchies and networks do not ncessarily hve to stand in opposition;
they may not only co-exist but ultimately prove consilient. As Keven
Kelly puts in his 1994 book Out of Control





