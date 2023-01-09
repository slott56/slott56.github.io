Applet Not Inited; the "Red X" problem
======================================

:date: 2009-05-21 07:21
:tags: HTML,applet,java
:slug: 2009_05_21-applet_not_inited_the_red_x_problem
:category: Technologies
:status: published

I haven't done Applet stuff in years.

I do -- intensely -- like embedding functionality in web pages.
RIA/Ajax and what-not are something I have trouble with because I'm
not a graphic designer.  Javascript and Applets fall into three clear
categories:

#.  Basic usability.  Javascript offers lots of little enhancements to
    HTML presentation that make sense.  Emphasis on "little".

#.  Client-side features.  Many things are simple calculators or other
    processing that makes sense on the client side -- the relevant
    factors can be downloaded and used by an applet or javascript
    script.

#.  Junk.  There are lots of graphical effects that vary from
    gratuitous to irritating.  Too many folks in marketing see some
    "pop-up" technique and think it's cool.  Worse, they'll take an
    application that lacks solid use cases and try to add flashing to
    scrolling to emphasize something instead of reducing clutter and
    distraction.  Sigh.

The Common Problems
-------------------

In all web-based software development, the number one problem is
always permissions.  Always.  In the case of applet development,
this is always hurdle number one.  The file isn't owned by the
right person or doesn't have the right permissions.  You see the
"applet not inited" and "red X icon" as symptoms of the applet not
being downloaded at all.

The number two problem is access to resources.  Usually this is a
CLASSPATH issue, but it can also be an HTML page with a wrong URI
for the applet's code.  You see the "applet not inited" and "red X
icon" as symptoms of the applet not being referenced correctly, or
not being able to locate all of its parts.

  [Technically, the basic access comes before permissions, but you
  usually don't get access wrong first.  Usually, you get
  permissions wrong; later, you discover you have a subtle access
  issue.]

One of the more subtle manifestations are the case-matching
issues.  Your Java class definitions are usually UpperCase.  The
source file and resulting class file will have this same UpperCase
format.  But if you get the case wrong in your HTML, you just get
an applet not inited error.  Arrgh.

When you don't work with applets all that often, the "applet not
inited" is baffling.

Misdirection
------------

I wasted hours on Google and Stack Overflow looking up "applet not
inited" and "Red X icon" and similar stuff.

Then I looked at the HTML I was testing.

Surprise.  No one had moved the .jar file into the proper
directory.

There's a lot of stuff on the applet not inited error.  Most of it
misses the usual culprits: permissions and access to the
resources.



-----

Hi Friend,! Congratulations for this nice looking ...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-06-08 04:43:59.548000-04:00

Hi Friend,! Congratulations for this nice looking blog. In this post
everything about Web Development. I am also interested in latest news,
Great idea you know about company background. Increasing your web
traffic and page views
`Add <http://directory.itsolusenz.com/submit-link.php>`__, add your
website in www.directory.itsolusenz.com/





