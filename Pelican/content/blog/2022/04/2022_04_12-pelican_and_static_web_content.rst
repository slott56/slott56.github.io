Pelican and Static Web Content
==============================

:date: 2022-04-12 08:00
:tags: #python,blogging,markdown,static site generator
:slug: 2022_04_12-pelican_and_static_web_content
:category: Technologies
:status: published

In `Static Site
Blues <{filename}/blog/2022/03/2022_03_01-static_site_blues.rst>`__
I was wringing my hands over ways to convert a **ton** of content from a
two different proprietary tools (the very old iWeb, and the merely old
Sandvox) into something I could work with.

After a bit of fiddling around, I'm delighted with
`Pelican <https://blog.getpelican.com>`__.

First, of course, I had to extract all the iWeb and Sandvox content.
This was emphatically not fun. While both used XML, they used it in
subtly different ways. Apple's frameworks serialize internal state as
XML in a way that preserves a lot of semantic details. It also preserves
endless irrelevant details.

I wound up with a Markdown data structure definition, plus a
higher-level "content model" with sites, pages, blogs, blog entries and
images. Plus the iWeb extractor and the Sandvox extractor. It's a lot of
code, much of which lacks solid unit test cases. It worked -- once --
and I was tolerant of the results.

I also wound up writing tools to walk the resulting tree of Markdown
files doing some post-extraction cleanup. There's a lot of cleanup that
should be done.

But.

I can now add to the blog with the state of my voyaging. I've been able
to keep `Team Red
Cruising <https://itmaybeahack.com/TeamRedCruising2/>`__ up to date.

Eventually (i.e., when the boat is laid up for Hurricane Season) I may
make an effort to clean up the older content and make it more
consistent. In particular, I need to add some annotations around
anchorages to make it possible to locate all of the legs of all of the
journeys. Since the HTML is what most people can see, that means a class
identifier for lat-lon pairs.

As it is, the blog entries are \*mostly\* markdown. Getting images and
blockquotes even close to readable requires dropping to HTML to make
direct use of the bootstrap CSS. This also requires some comprehensive
cleanup to properly use the Bootstrap classes. (I think I've may have
introduced some misspelled CSS classes into the HTML that aren't doing
anything.)

For now, however, it works. I'm still tweaking small things that require
republishing \*all\* the HTML.





