Data Modeling Nightmare -- XML, HTML, and Markdown
==================================================

:date: 2018-09-18 08:00
:tags: #python,xml,content management,blogging,HTML,markdown
:slug: 2018_09_18-data_modeling_nightmare_xml_html_and_markdown
:category: Technologies
:status: published


Here's a particularly tangled and difficult problem. It arises because
I have another blog. Specifically this: `Team Red
Cruising <http://www.itmaybeahack.com/TeamRedCruising/>`__. And it's
an unholy mess.

There are two important features of the *Team Red Cruising* blog.

#. It's managed with off-line editor(s) so I can write posts from the
   boat and then upload them when I get connectivity. Welcome to being a
   technomad -- I don't always have a web-based blog editor available.

#. It was actually created with two different off-line editors over a
   period of years: `iWeb <https://support.apple.com/downloads/iweb>`__
   and `Sandvox <http://www.karelia.com/products/sandvox/>`__. iWeb is
   long dead. Sandvox hasn't seen many updates recently, and I think I'd
   like to move on to something newer and "better".


(In this case, "better" means iOS-friendly. e.g.,
`Blogo <https://www.getblogo.com/>`__ or `BlogPad
Pro <https://blogpadpro.com/>`__. **Also**. Blogo's support site seems
to be a right mess. Not a good look. They're working on it.)

The blog isn't the unholy mess. We'll get to the mess below. First,
however some background on the overall strategy. I want to move my
content. What's involved? There are several things in play: the
hosting, the target, and the source. So. Essentially. Everything.

Changing the Hosting Platform
-----------------------------


Both of my legacy tools would export and upload the changes to my
hosting service directly, avoiding the overheads of having any complex
hosting software. The site was static and served simply from the
filesystem via Apache httpd. Publishing was an SFTP transfer to the
server. Nothing more. The "platform" was almost nothing.

(I could switch to using an Amazon S3 bucket and a DNS entry and it
would work nicely.)

Both of these offline editing tools have a tiny bias toward working
with hosting services like WordPress. Blogo claims it can also work
with Medium, and Blogger, as well.

This means running Wordpress on top of my default SFTP/Apache
configuration. I use A2 Hosting, so this is really easy to do.

So. The hosting is more-or-less settled. I'll do very little. (Dealing
with breaking links is a separate hand-wringing exercise.)

In order to move from iWeb and Sandvox to another tool, and start
using WordPress, I have two strategies for converting the content.

#. Ignore my legacy content. Leave it where it is, more-or-less
   uneditable. The tool(s) are gone, all that's left is the static HTML
   output from the tool.

#. Gather the legacy content and migrate it to WordPress and then pick
   an offline tool that works with WordPress.


I've already done strategy #1, when I converted from iWeb to Sandvox.
I left the old iWeb stuff out there, and moved to a new URL path with
new content. While a clever menu structure can make it look like it's
all one multi-year blog, the pages themselves are vastly different in
the way they look. There's no comprehensive search. And, of course, I
can't easily maintain the old iWeb stuff.

Having one #1, I'm now sure that's a bad idea.

An advantage of moving to WordPress is the ability to have all of the
content in one, uniform database. WordPress has export functionality,
so the next tool is a distinct possibility.

Note that SandVox seems to have a distinct problem trying to import
iWeb's published content. They have a cool HTML scraper, but iWeb
relies on JavaScript, and scraper doesn't do well.

Getting to WordPress
--------------------


What we're looking at is a fairly complex data structure. While I'd
like to look at this from a vast and reserved distance (i.e., in the
abstract) I have a very concrete problem. So, we're forced to consider
this from the WordPress POV.

We have a WordPress "Site" with a long series of posts and some pages.


.. image:: http://yuml.me/0eee4623.png
   :width: 186px
   :height: 320px
   :target: http://yuml.me/0eee4623.png
   :alt: UML diagram


The essence here is that the content can -- to an extent -- be
converted to Markdown. The titles and dates are easy to preserve. The
body? Not so much.

We can, as an alternative to Markdown, use some kind of skinny HTML
that WordPress supports. I think WP can handle a structure free of
class names, and using a most of the available HTML tags.

Most of the blog content is relatively flat. The block structure is
generally limited to images, block quotes, paragraphs, ordered and
unordered lists. The inline tags in use seem to be a, img, strong, em,
and a few span tags for font changes.

The complexity, then, is building a useful content model from the
source. There are a few AST's for Markdown.
`commonmark.py <https://github.com/rtfd/CommonMark-py>`__ might have a
useful AST.  It's not complex, so it may be simpler to define my own.

It's hard to understand the inline blocks in mistletoe. The
python-markdown project uses ElementTree objects to build the AST. I'm
not a fan of this because I'm not parsing Markdown.

Starting From -- Well, it's Complicated
---------------------------------------


There are -- as noted above -- two sources:

-  Sandvox.

-  iWeb.


The Sandvox desktop "database" structure is opaque. The media is easy
to find. The content is some kind of binary-encoded data with headers
that tell me a little about the XCode environment, but nothing else.

To read this, I have to scrape the HTML using Beautiful Soup. It
involves processing like this:

::

       content = soup.html.body.find("div", id="main-content")
       article = content.find(class_="article-content").find(class_="RichTextElement").div




Find a nested ``<div>`` with a target ID. Inside that <div> is where the
article can be found.

This seems to work out pretty well. Almost everything I want to
preserve can be -- sort of -- mushed into Markdown.

The iWeb desktop "database" is XML. The published HTML depends on
Javascript and is hard to work with. The XML is -- of course --
densely wordy and convoluted as can be. But the words and markup are
there.  I can use ElementTree to walk down through XML to locate the
right tags.

There's a lot of code like this

::

       main_layer = child_root.find('ns0:site-page/ns0:drawables/ns0:main-layer', ns)




This example digs into site pages, and nested drawables, and main
layers of content.  Eventually, we wind up looking at <p>, <span>,
<attachment-ref>, and <link> tags in the XML to build the relevant
content.

The nuance is style. They're not part of the inline markup. They're
stored separately, and included by reference. Each of the four tags
that seem to be in use have a style attribute that references styles
defined within the posting. Once these references are resolved, I
think Mardown can be generated.

The Unholy Mess
---------------


The hateful part of this is the disconnect between HTML (and XML) and
Markdown. The source data permits indefinite nesting of tags.
Semantically meaningless <p><p>words</p></p> are legal. The
"flattening" from HTML/XML to Markdown is worrisome: what if I trash
an entry by missing something important?

Ideally, it's this:



.. image:: http://yuml.me/41ba6176.png
   :width: 272px
   :height: 320px
   :target: http://yuml.me/41ba6176.png
   :alt: UML diagram



Pragmatically, HTML/XML can be more complex. This diagram assumes we
won't have paragraphs inside list items. HTML permits it. It's
redundant in Markdown.

Worse, of course, are the inline tags. HTML has a kabillion of them.
The software I've been using seems to limit me to <img>, <strong>,
<em>, and <a>. HTML/XML allows nesting. Markdown doesn't.

Ideally, I can reframe the inline tags to create a flat sequence of
styled-text objects within any of the tags.

Right now. Headaches.

Working on the code. It's not a general solution to anyone else's
problem. But. I'm hoping -- as I beat the problem into submission --
to find a way to make some useful tutorial materials on mapping
between complex, and different, data structures.




