Static Site Blues
=================

:date: 2022-03-01 08:00
:tags: RST,#python,blogging,markdown,static site generator
:slug: 2022_03_01-static_site_blues
:category: Technologies
:status: published

I have a very large, static site with 10+ years of stuff about my boat.
Most of it is pretty
boring. http://www.itmaybeahack.com/TeamRedCruising/

I started with iWeb. It was very -- well -- 2000-ish look and feel. Too
many pastels and lines and borders.

In 2012, I switched to Sandvox. I lived on a boat back then. I don't
have reliable internet. Using blogger.com, for example, required a
sincere commitment to bandwidth. I moved ashore in 2014 and returned to
the boat in 2020.

Sandvox's creator seems to be out-of-business.

What's next?

Give up on these fancy editors and switch to a static site generator.
Write markdown. Run the tool. Upload when in a coffee shop with Wi-Fi.

What site generator?

See https://www.fullstackpython.com/static-site-generator.html for some
suggestions.

There are three parts to this effort.

#. Extract the goodness from iWeb and Sandvox. I knew this would be real
   work. iWeb's site has too much javascript to be easy-to-parse. I have
   to navigate the underlying XML database. Sandvox is much easier to
   deal with: their published site is clean, static HTML with useful
   classes and ids in their tags.

#. Reformat the source material into Markdown. I've grudgingly grown to
   accept Markdown, even through RST is clearly superior. Some tools
   work with RST and I may pandoc the entire thing over to RST from
   Markdown. For now, though, the content seems to be captured.

#. Fixup internal links and cross references. This is a godawful
   problem. Media links -- in particular -- seem to be a nightmare.
   Since iWeb resolves things via Javascript, the HTML is opaque.

   Fortunately, the database's internal cross-references aren't
   horrible. Maybe this was exacerbated a poor choice of generators.

#. Convert to HTML for a local server. Validate.

#. Convert to HTML for the target server. Upload to a staging server and
   validate again. This requires a coffee shop. Not doing this with my
   phone's data plan.

Steps 1 and 2 aren't too bad. I've extracted serviceable markdown from
the iWeb database and the published Sandvox site. The material parallels
the Site/Blog/Page structure of the originals. The markdown seems to be
mostly error-free. (Some images have the caption in the wrong place,
``![caption](link)`` isn't as memorable as I'd like.)

Step 3, the internal links and cross-references, has been a difficult
problem, it turns out. I can, mostly, associate media with postings. I
can also find all the cross-references among postings and fix those up.
The question that arises is how to reference media from a blog post?

Mynt
----

I started with `mynt <https://mynt.uhnomoli.com>`__. And had to bail.
It's clever and very simple. Too simple for blog posts that have a lot
of associated media assets.

The issue is what to write in the markdown to refer to the images that
go with a specific blog post. I resorted to a master ``_Media``
directory. Which means each posting has
``![caption][../../../../_Media/image.png)`` in it.  This is
semi-manageable. But exasperating in bulk.

What scrambled my brain is the way a mynt posting becomes a directory,
with an index.html. Clearly, the media could be adjacent to the
index.html. But. I can't figure out how to get mynt's generator to put
the media into each post's published directory. It seems like each post
should not be a markdown file.

Also, I can trivially change the base URL when generating, but I can't
change the domain. When I publish, I want to swap domains \*only*,
leaving the base URL alone. I tried. It's too much fooling around.

Pelican
-------

Next up. `Pelican <https://www.fullstackpython.com/pelican.html>`__.
We'll see if I can get my media and blog posts neatly organized.
This http://chdoig.github.io/create-pelican-blog.html seems encouraging.
I think I should have started here first. Lektor is another possibility.

Since my legacy sites have RSS feeds, it may be sensible to turn Pelican
loose on the RSS and (perhaps) skip steps 1, 2, and 3, entirely.

| 





