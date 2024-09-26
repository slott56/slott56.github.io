I didn't get the memo -- apparently, I'm not on the distribution list -- in fact, there may be no list
======================================================================================================

:date: 2008-09-09 09:50
:tags: content,discovery,architecture
:slug: 2008_09_09-i_didnt_get_the_memo_apparently_im_not_on_the_distribution_list_in_fact_there_may_be_no_list
:category: Management
:status: published







Recently, I started on an architecture for which `Fast CGI <http://www.fastcgi.com/>`_  seemed like a good idea.  But then, I couldn't find a pre-built `YUM <http://fedoraproject.org/wiki/Tools/yum>`_  distro for `Fedora Core 9 <http://fedoraproject.org/>`_ .  Further, I couldn't really build my own, because I couldn't find the FC9 version of /usr/local/apache2.



Stuff moved.  And no one told me.



Long Anecdote
--------------



Years ago, I worked with someone who had either a knowledge management or a file system issue.  It wasn't clear.  They had a problem organizing information.  They couldn't -- somehow -- make the windows filesystem work and needed a new paradigm, something that would blow the classic hierarchical file system away.



Seriously.  They said that.



I tried to elicit use cases.  Nothing came of that.  Eventually, they sent me the example that had frustrated them.  



They were creating each paragraph as a separate file in a **massive**  hierarchy.  The hierarchy was so deeply nested that they had reached the maximum path length and weren't through putting sub-(sub-)x9-sub levels in.



There is lots of craziness here; and more that I haven't mentioned.  MS-Word has an outlining mode.  They were shocked that such a thing existed.  Shocked.  But it was **Completely Useless**  -- it didn't allow more than 8 levels of indenting.



There are lots of outline editors, Wikipedia calls them `Outliners <http://en.wikipedia.org/wiki/Outliner>`_ .  I used `Leo <http://webpages.charter.net/edreamleo/front.html>`_  for a long time.  I use `XXE <http://www.xmlmind.com/xmleditor/>`_  for really big projects like my `books <http://www.itmaybeahack.com/homepage/books/index.html>`_ .



This person did not know that the "outliner" software category existed and was amazed that no one told them.



It gets worse.  In the process of trying to elicit use cases, we had to spend 100 emails discussing -- essentially -- "hierarchy".  Seriously.  The whole hierarchy == directed acyclic graph == simple node with list of subnodes was beyond their comprehension.  The idea that this trivial data structure could do so much was baffling.  Further, the fact that this data structure is recursive and doesn't map to SQL very well was also baffling.



They were amazed that this was well-understood undergrad computer science.  It didn't require a dozen use cases and two dozen pages of detailed hand-wringing object design.  No one told them.



End Long Anecdote
-----------------



I spent hours researching Apache2 and fastcgi on FC9.  Hours.  I found useful stuff, like `Compile Apache on Fedora <http://hacktux.com/compile/apache/fedora>`_ .  I was getting close to downloading source and beginning from scratch.



Then, the following thought slowly began to trickle into my head.



    **"If it's too hard, you're doing it wrong."** 



So, I went back to the basic FC9 software updater and did the search again.  What I gleaned from the listing this time was that they provide a pre-built `fcgid <http://fastcgi.coremail.cn/>`_  instead of `fastCGI <http://www.fastcgi.com/>`_ .



Do I actually care?  If fcgid is binary-compatible with only a small algorithm change, I don't really care, do I?



For a few minutes, I searched around to see if I could find any "notification" or "change log" for Fedora that indicated that mod_fastcgi was out and mod_fcgid was in.  Then I realized that it was fruitless.  There often aren't Big Announcements.  And even if there are, it may not be sensible to try and be a member of every open source project in my technology stack.



The source is available.  There are always two choices.  (1) Keep all the legacy source and rebuild the legacy technology stack.  (2) Find the path of least resistance and do upgrades on a regular basis.  



It's the "find the path of least resistance" that's hard.  I was so focused on FastCGI that I almost forgot to look around and see what -- if any -- alternatives would meet my objectives.  The point is not a specific technology.  We can't stand around waving the hammer forcing all fasteners to be used like nails.  The point is to solve the problem.





