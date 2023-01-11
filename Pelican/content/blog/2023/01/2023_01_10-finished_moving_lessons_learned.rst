Finished Moving: Lessons Learned
#################################

:date: 2023_01_10 08:00
:tags: blogging,markup,rst
:slug: 2023_01_10-finished_moving_lessons_learned
:category: Technologies
:status: published

.. role:: text-danger

Moved everything from blogger.com to "here" (https://slott56.github.io).

What did I learn?

BLUF
====

1. Don't use WYSIWYG editors. Always use plain text markup.

2. Think about your categories and tags.

3. Links rot.

4. Have a data model and tooling to process entries.

History
=======

Back in the early '00's (up to 2003 or so) blogging
was **Rocket Science**. Consider that https://boingboing.net started
to be an online blog in January 2000.

Back then, you needed hosting. And blogging software.

Hosting wasn't as easy as signing up with https://www.a2hosting.com.
A2 hosting didn't exist until 2001. Back then it was complicated and expensive.
Not for the faint of heart.

Apple offered iBlog which they would host for you on one of their domains like http://homepage.mac.com or some such.
See `iBlog <{filename}/blog/2003/11/2003_11_15-iblog.rst>`_.

Big. Mistake. (See `Big Mistakes`_, below.)

From about 2004 to 2006 (maybe)
there was  service called "Bloki", which offered blogging and forum capabilities.
That was super-helpful because you could edit on-line.
See `BLOKI.com <{filename}/blog/2004/01/2004_01_20-blokicom.rst>`_.

Big.  Mistake. (See `Big Mistakes`_, below.)

By 2008, iBlog had run its course.
See `iBlog Buggy... Since Leopard's release... No fixes in sight. <{filename}/blog/2008/03/2008_03_19-iblog_buggy_since_leopards_release_no_fixes_in_sight.rst>`_.

By 2009, it appears that I must have consolidated my content onto https://blogspot.com.
Which got merged with https://blogger.com at some point later in life.
(It's hard to tell, but there were blogspot references scattered through
the internal links.)

Why Move?
=========

If https://blogger.com isn't **broken**, why change?

There aren't any **good** reasons. Only a few weak reasons.

1.  I have a personal blog, which is **not** on blogger.
    It, too, had a long, complex history that went from
    Apple's iWeb to Sandvox until Sandvox stopped working,
    forcing me to consolidate into `Pelican <https://getpelican.com>`_. See https://itmaybeahack.com/TeamRedCruising2/index.html.

2.  I had been following some folks who were starting blogs,
    and they didn't like `Pelican <https://getpelican.com>`_.
    They seemed to really like did like `Hugo <https://gohugo.io>`_.

3.  In researching Hugo, I found out about how https://github.io can
    host content, like a blog, with relatively little real work.
    Mostly ``git commit`` and ``git push``.

4.  I'm over on-line editing. I'm retired, living on a boat,
    and I travel a lot. I need to edit off-line.
    Creating and staging blog posts for the future
    is fun, but requires me to save notes, and then create posts
    when I have connectivity, staging them for future release.

These add up to "move to https://slott56.github.io".

Big Mistakes
============

There was one big mistake that manifested itself two ways.

WYSIWYG -- What You See Is What You Get.

Some secondary mistakes involve the way that blogger lacked
categories. It was "simply" a list of posts.

Finally, I needed to address "link rot".

WYSIWYG Is Evil
===============

Any purely visual editor is a burning dumpster fire
of weirdly inconsistent content that happens to look
right, but is actually wrong.

Writing involves three separate issues:

1. The words chosen.

2. The semantics of the words.

3. The presentation to highlight the semantics.

For example, we write ``code`` in a distinct font.
The word ``code`` has distinct semantics, it's in a programming
language, and gets a distinct font to reveal that.

We **emphasize** things with a style change. We might write foreign *words* or *phrases* in a separate style.

In some cases, we're forced to overload styles.
We might use **bold** for an **AOA** (Abbreviation or Acronym).
And we also use it for **emphasis** and for **Chapter Titles**.

HTML has many semantic categories available as markup.
We can use ``<abbr>ABBR</abbr>`` to denote an abbreviation.
The style sheet may render this in bold (or not, maybe in :text-danger:`red`.)

Here's the problem:

    **WYSIWYG editors conceal the semantics, and only reveal the markup.**

While it's not impossible to check semantics, it's hard.

You can **bold** something and it looks fine.

But it should have been a Section Heading, not simply bold.

You can't tell.

Offline editors and proprietary file formats exacerbate
the problem. The content is very difficult to recover.

In Apple's case, the files were all XML and could
be read.

Newer products use Snappy compression and Protobuf,
which is relentlessly evil.

Categories Are Hard
====================

The iBlog posts had categories.

The Blogspot/Blogger posts didn't have categories.

I think categories are useful.

Now what?

I have to categorize about 1,000 blog posts.

This becomes a kind of K-nn problem. Locate the
tags and find the most popular category.

Link Rot
==========

Links vanish.

I'm not going to use the Wayback Machine (https://web.archive.org)
to locate the old content.

Instead I'm going to (eventually) flag broken links.

In some cases, I'll probably delete the whole blog entry
because it's aged to the point of irrelevance.

After a ton of work, I found 19 old blogspot
URL's that I didn't know about. I have a link
converted app that I can update to handle these the
way I handled hundreds of more visible problems.

Tooling
=======

Some old iBlog entries were in XML.
I converted these to RST without exposing
an intermediate data model. Not good.

The blogger posts were exported in ATOM notation,
a distinct XML format.

What's common?

::

    class Feed:
        ...

    class Entry:
        ...

    class Post(Entry):
        ...

    class Page(Entry):
        ...

A model like this lets a feed contain entries.

This unified model can be parsed from RST or XML,
and then small scripts (and Jupyter notebooks)
can tweak the content to make it consistent.

And, no, I doubt I'll publish any of the tools
I used. It was all one-time hackery.
