iBlog Buggy... Since Leopard's release... No fixes in sight.
============================================================

:date: 2008-03-19 15:59
:tags: technologies,web
:slug: 2008_03_19-iblog_buggy_since_leopards_release_no_fixes_in_sight
:category: Technologies
:status: published







This is a kind of "case study" post.  It happens -- frequently -- that I wind up in a situation similar to this one.  Usually it involves large, complex pieces of software and lots of people with strongly-held opinions.  I'm usually brought in toward the end, and have to discover the parts I missed.



What I'm sometimes asked is to help plan the product/tool selection.  This is a bad policy, since the previous parts of the conversation either never happened or never got documented.  Either way, they aren't provided as input to the stuff I'm supposed to do.  When things go well, I get to participate from the beginning.



This is a detailed, specific case study showing how to structure the "what tool do we use?" decision-making process.  It's something everyone does.  Indeed, carefully logging the information, and creating a structured narrative is a good way to apply discipline to the process and make the political considerations visible and explicit.



[Yes, explicit politics will be painful.  Projects are often cancelled when the management trump cards start coming out.  That's a good thing.  A cancelled project means people learned something and didn't waste money following some manager's whim to it's logical, horrifying conclusion.]



:strong:`Strategy`



iBlog isn't working well, and doesn't look like it will be fixed.  What do I use for Blogging?



There are several "strategic" considerations.  



On the one hand, I'd like to continue to publish via my homepage.mac.com account, since I'm already paying for this.  And I'll continue to pay for the offsite backup as well as hosting.  [Yes, I'm also using Time Machine, that's on-site.]



On the other hand ... well ... there doesn't seem to be any good reason to change hosting for my blog.  Specifically, a move to free hosting (i.e., Google's blogger) leads to the possibility of two sets of ads (theirs plus mine).  Blogger :emphasis:`may`  be smart enough to handle this properly.  



[Ads may bug some readers.  Two ad channels might bug people even more.  Also -- ha ha -- it would dilute my potential revenue stream.  Currently, AdSense owes me about $3.80.  I am well aware that it will be 4 years before I get my first check at this rate.]



On the one hand, my existing RSS feed must continue to work.  



On the other hand, moving to a new site should be a matter of migrating existing readers to the new URL's for content and RSS.  I don't anticipate a lot of breakage from this change, since I only knew of a few places where my RSS feed is used.



:strong:`Approach`



1.  Open a new Blog?  I can track readership by creating a new AdSense channel.   It may help if I mirror new site RSS information onto my legacy site in order to keep it fresh.



1a.   Leave the old blog as simple legacy?  Just add top-of-blog story to the old blog linking to the new blog.  



1b.  Migrate the old Blog content into the new Blog?  I can then replace the old Blog pages with redirects to the new blog.  Hard to see how many people use the redirects.  I'd still need to consider cloning the RSS file from new to old.



1c.  Migrate the old Blog content, as well as leave it as legacy.  



2.  Migrate the old Blog content into new tools, leaving almost everything in place?  The permalink structure of the old Blog makes this harder to do than it appears.



:strong:`Use Cases`



Blog use cases depend on well-designed, permanent URL's and RSS feeds.  There are at least a dozen use cases that provide a benchmark for tool comparison.



There are three actors: Authors, Readers and Syndicators (unofficial planet python, technorati being the two I actually use).  



Readers have (1) the bookmark use case, (2) the permalink reference use case and (3) a search use case.  (4) Comments are most easily handled by Haloscan. There is (5) the social networking ("micro blogging") sites (del.icio.us, digg, furl, reddit, yahoo, twitter, technorati, slash dot, stumble) which rely on an active link from the blog to the networking site to reference content.  Finally, Readers and Syndicators have (6) the RSS notification use case.  



We could, additionally, define a whole flock of HTML use cases for the Readers: browse, search, scroll, follow link, etc.  We don't define those fully, since they're more-or-less implied by the web part of web logging.



Authors have the (1) write draft, (2) search, (3) publish, (4) maintain sidebar links, (5) a whole flock of AdSense use cases, and (6) a whole flock of comment-management (Haloscan) use cases. 



[Currently, iBlog fails at use case 2, search, completely.  It behaves badly in use case 3, publish, by crashing before it updates it's internal "what's been published" state.]



Tools - Overview



See `http://www.weblogmatrix.org/ <http://www.weblogmatrix.org/>`_  for some alternative tools.



1.  Web-based blogging: `http://www.blogger.com <http://www.blogger.com>`_ , for example.  To a lesser extent LiveJournal, TypePad and WordPress.



Blogger doesn't directly support my `http://www.itmaybeahack.com/homepage <http://www.itmaybeahack.com/homepage/iblog/architecture/>`_  account, which requires WebDAV.  Neither does LiveJournal or WordPress.



2.  Desktop Mac OS X blogging.



In all cases, I'd need to rework the site to preserve the legacy permalinks, and create the new blog as a parallel structure.  I could migrate the legacy content, or merely divide the content into old and new.  The problem is the RSS feeds for my old content would go old and dead.  I'd need to post several reminders to assure that all potential readers were properly forwarded.



-    `Blog.Mac <http://www.versiontracker.com/dyn/moreinfo/macosx/27678>`_  - Updated 3/10/08 - Publishes directly to .Mac (yay!) - 1.2 is early in the life cycle.



-    `MarsEdit <http://www.versiontracker.com/dyn/moreinfo/macosx/24670>`_  - Updated 2/13/08 - Publishes using a number of standard protocols - 2.1 somewhat more mature.  Requires an account with another web service, separate from my homepage.mac.com web page.



-    `MacJournal <http://www.versiontracker.com/dyn/moreinfo/macosx/11374>`_  - Updated 2/28/08 - Publishes directly to .Mac - 5.0 means mature.



-    Apple's `iWeb <http://www.apple.com/ilife/iweb/>`_  - I have this; it's part of iLife.  It is actively evolving in the right direction.  However, it also lacks a number of features.



-    `Blogo <http://www.versiontracker.com/dyn/moreinfo/macosx/33532>`_  - Updated 1/27/08 - Not clear if it handles .Mac - 1.0 is early in the life cycle.



-    `myBlog <http://www.versiontracker.com/dyn/moreinfo/macosx/31004>`_  - Updated 12/1/07 - Not clear if it handles .Mac (it might write to iDisk directly) - Version 1.1 is early in the life cycle



-    `BlogThing <http://www.versiontracker.com/dyn/moreinfo/macosx/29098>`_  - Updated 4/4/06 - version 1.0 - too simplistic.



-    `BlogWaveStudio <http://www.versiontracker.com/dyn/moreinfo/macosx/22682>`_  -Updated in 2005, version 1.1, no developer site.



-    `XBlog <http://www.versiontracker.com/dyn/moreinfo/macosx/19116>`_  - 2003, version 1.1, no developer site.



-    `Blosxom <http://www.versiontracker.com/dyn/moreinfo/macosx/14080>`_  - 2003, version 2.0 - Open Source - however, no changes since '03



-    `ecto <http://www.versiontracker.com/dyn/moreinfo/macosx/15723>`_  (mis-categorized in version tracker) - Updated 1/10/07 - version 2.4. Looks good, but no on-line doco to speak of.





The version 1 products leave me a little cold.  iBlog was version 1 and never got far into version 2 before support faded away.




:strong:`The Short List`




The short list is MacJournal, MarsEdit and and iWeb.  Blog.Mac has some appeal, since it is narrowly focused on me, the .Mac blogger.




:strong:`MacJournal`.  Does a lot of things.  Blogging feels like an add-on.  The HTML Templates aren't described well.  It isn't clear how hard it would be to extract elements of my iBlog pages and turn them into a MacJournal template and have some consistency.  The list of MacJournal template tags are undocumented, making this template conversion a dicy proposition.




:strong:`MarsEdit`.  Focused.  However, it's not clear what template capabilities it has for putting entries into a blog page context.  Must have something, but the documentation available on-line is just advertising copy.  Not clear how AdSense or Haloscan would work, either.  No on-line doco is the end of my interest.




:strong:`iWeb`.  Does many things.  Part of iLife.  New release is aware of AdSense ads.  Missing obvious Haloscan integration; an add-on is required (http://web.mac.com/cbrantly/iWeb/Software/iComment.html).  Has some ability to reconstruct templates similar to iBlog templates (minus the calendar, specifically).  No obvious social networking support.




:strong:`Blog.Mac`.  Focused.  Has AdSense and Haloscan comments already available.  Template editing and multiple templates available.  New blog would trivially go to a directory parallel to my existing iblog directory tree.




Detailed Comparison




..  csv-table::

    "Product","Reader/ Syndicator","Author"
    " ","Bookmark, Permalink","Comments","Social Networking","RSS","Write, Search, Publish","Sidebar","AdSense","Comment"
    ":strong:`MacJournal` ","Good","Not Clear","Not Clear","Not Clear","Good","Not Clear","Not Clear","Not Clear"
    ":strong:`iWeb` ","Good","Haloscan is an Add-on","Missing","Good","Good but No Search","Template","New Feature",".Mac"
    ":strong:`Blog.Mac` ","Good","Good","Missing","Good","Good","Template","Good","Haloscan",












:strong:`Solution`



:strong:`MarsEdit`  might be good, but it's too hard to penetrate the fog on what it does.



While :strong:`iWeb`  has some incumbency, it doesn't have idiot-simple social networking capabilities.  It doesn't have an easy-to-use blog search.



This leads me to look closely at :strong:`Blog.Mac`  for a trial.



:strong:`Consequences`



Here's the potential course of events.



First, I need to pilot :strong:`Blog.Mac`: create a new Blog, parallel to my existing iBlog material.  This involves creating (or finding) a template that matches the legacy blog.  It also involves trying to resolve the Social Networking capabilities of Blog.Mac.



If the tool looks workable, then option 1c (migrate legacy content into Blog.Mac) needs to be explored.  If this can't be made to work, then 1a (ignore the legacy) is the next best alternative.



If the tool is not workable, then I might try Mars Edit.



Notify `Unofficial Planet Python <http://www.planetpython.org/>`_  of the new URL.  At this point, I may also look at hooking up with `Planet Python <http://planet.python.org/>`_ .




