Object Models and Relational Joins -- Endless Confusion
=======================================================

:date: 2009-07-31 07:32
:tags: Django,#python,object-oriented design,SQL,ORM
:slug: 2009_07_31-object_models_and_relational_joins_endless_confusion
:category: Technologies
:status: published

Check out this list of questions from Stack Overflow: `[Django]
join <http://stackoverflow.com/search?q=%5Bdjango%5D+join>`__.

These are all folks trying to do joins or outer joins even though
they have objects fetched through the ORM.

How does this confusion arise? Easy. Folks work with SQL as if the
relational world-view is Important and Universal. It isn't. SQL isn't
even a programming language, *per se*.

Here's the important thing for Django developers to know: **SQL is a
Hack; Leave it Behind**.

The bad news is that all those years spent mastering the ins and outs
of the SELECT statement doesn't have as much enduring value as I'd
hoped it would have. [Yes, I was a DBA in Ingres and Oracle. I know
my SQL.]

The good news is that Object Navigation replaces much of the
hideousness of SQL. To an extent. Let's look at some cases.

Joins in General
----------------

SQL SELECT statements are an algebraic specification of a result set.
The database is free to use any algorithm to build the required set.

SQL imposes the Join hack because SQL is a completely consistent set
algebra system. A simple SELECT returns a row-column set of data. A
join between tables has to construct a fake row-column set so that
everything is consistent.

A Join is nothing more than navigation from an object to associated
objects. In OO world, this is simply object containment; the
navigation is simply the name of a `related
object <http://docs.djangoproject.com/en/dev/topics/db/queries/#related-objects>`__.
Nothing more.

Master-Detail (1:m) Joins
-------------------------

A master-detail join in SQL works with a foreign key reference on the
children.

In Django, this has to be declared in a SQL-friendly way so that the
ORM will work.

::

  class Master( models.Model ):

  class Detail( models.Model ):
     master= models.ForeignKey( Master )

The "Join" query is simply this. The "detail_set" name is deduced by
Django from the class that contains the foreign key.

::

  for m in Master.objects.filter():
     process m
         for d in m.detail_set.all():
             process d

"But wait!" the SQL purist cries, "isn't that inefficient?" The
answer is "rarely". It's possible that the RDBMS, doing a
"merge-join" algorithm to build the entire result set might be
quicker than this.

As practical matter, however, the rest of the web transaction --
including the painfully slow download -- will dominate the timeline.

Association (m:m) Joins
-----------------------

An association in SQL requires an intermediate table to carry the
combinations of foreign keys.

In Django, this has to be declared in a SQL-friendly way so that
the ORM will work.

::

 class This( models.Model ):

 class That( models.Model ):
    these = models.ManyToManyField( This )

The navigation, however, is simply following the relationships.
There's no complicated SQL join required.

::

    for this in This.objects.filter():
        for that in this.that_set.all():
            process this and that

Here's the other side of the navigation.

::

    for that in That.objects.filter():
        for this in that.these:
           process this and that

Outer Joins
------------

An Outer Join is a "Join with Null for Missing Relationships".
It's navigation with an if-statement or an exception clause.

::

    for that in That.objects.filter():
        try:
            this = that.this_set.get()
        except This.DoesNotExist:
            this = None
        process this and that

There isn't any "join" in object-oriented programming. The ORM
layer removes the need.



-----

You might be interested in RQL which is similar to...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-07-31 09:28:02.676000-04:00

You might be interested in RQL which is similar to SPARQL and CubicWeb's
way to get data from the database.
http://www.logilab.org/project/rql
http://www.cubicweb.org/


"But wait!&quot; the SQL purist cries, &...
-----------------------------------------------------

mike bayer<noreply@blogger.com>

2009-07-31 11:30:32.391000-04:00

> "But wait!" the SQL purist cries, "isn't that inefficient?" The answer
is "rarely".

I'll have to disagree with you there. There answer is, "if there are
many parent rows, yes". Fetching a single result set is definitely
faster than executing hundreds of individual SELECT statements.

SQLAlchemy, as you know, abstracts the JOIN in the "first grab each
parent item, then grab each child item" problem into a feature called
"eager loading". So I don't think the problem is JOINs per se but just
being able to use them appropriately in conjunction with an object
model.


fumanchu:  yes, we're doing that on a project ...
-----------------------------------------------------

mike bayer<noreply@blogger.com>

2009-08-01 21:08:35.454000-04:00

fumanchu: yes, we're doing that on a project now (sorta). lucene is
basically a way of providing views. we still use SQL all over the place
though for smaller ad-hoc result sets.

infixum: SQL being obviated by ORMs is not how we all look at it.


Mike's right, and I'd say most systems I&#...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-07-31 12:19:55.293000-04:00

Mike's right, and I'd say most systems I've worked on in the past few
years have been of that size.

There's another way to architect a large system, however. If your system
of record is under heavy load, and you are therefore already caching
most of your child objects, it can be faster to farm your query out to a
replicated repository (like Lucene), fetch a list of ids, and then fetch
objects from the cache.


I attended a Django tutorial and was blown away by...
-----------------------------------------------------

Carl Trachte<noreply@blogger.com>

2009-07-31 13:29:02.016000-04:00

I attended a Django tutorial and was blown away by the idea that SQL
really isn't a factor, even though you're using data from a database.
For 10 years, my whole world was SQL. Hard to believe it's fading into
the background.

Progress and Moore's Law make everything esoteric after a while. I
wouldn't group SQL in with Assembly (for a number of reasons), but it
appears ORM's have become common and efficient enough to make SQL
knowledge obsolete, for web programmers, at least.





