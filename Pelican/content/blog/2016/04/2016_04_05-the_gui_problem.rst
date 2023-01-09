The GUI Problem
===============

:date: 2016-04-05 08:00
:tags: #python,API Design,microservices
:slug: 2016_04_05-the_gui_problem
:category: Technologies
:status: published

I write Microservices. And not-so-micro Services. API's.

I got this email recently.

    "Goal: get you to consider adding Gooey to your Python tool set"
    "Gooey
    What it's for: Turn a console-based Python program into one that sports
    a platform-native GUI.
    Why it's great: Presenting people, especially rank-and-file users, with
    a command-line application is among the fastest ways to reduce its use.
    Few beyond the hardcore like figuring out what options to pass, or in
    what order. `Gooey <https://github.com/chriskiehl/Gooey>`__ takes
    arguments expected by the argparse library and presents them users as a
    GUI form, with all options labeled and presented with appropriate
    controls (such as a drop-down for a multi-option argument, and so on).
    Very little additional coding -- a single include and a single decorator
    -- is needed to make it work, assuming you're already using argparse."

The examples and the GitHub documentation make it look delightful.
However.  It's utterly useless for me.  Interesting but useless.
From my perspective, API's and microservices are vastly more important
than desktop GUI's.

I'll repeat that in order to start a food-fight:

   **API's and microservices are more important than desktop GUI's**

I almost forgot the important qualifiers: **When working with Big
Data**. Or **When working with DevOps Automation**.

I realize that some people like to cling to the desktop GUI as a Very
Important Thing™. Which could be why they send me emails touting the
advantages of some kind of GUI tool or framework. The Desktop GUI is
important, but, from my perspective, it's a niche.

Actually two niches.

Niche 1. The word processor and spreadsheet and a few other generic
tools for putting text into a computer. While desktop versions are
better than server-side emacs and vi, they fill a similar purpose. An
IDE is (from this perspective) is little more than a glorified text
editor. In places that use Jenkins and Hudson and uDeploy and all of
those server-based tools, the desktop IDE is a place to stage code for
Jenkins jobs to do the "real" build.

Niche 2. All the other tools that turn a small-ish computer into a
dedicated workstation for specific kinds of media production. Video.
Audio. Image. Typesetting. These are not "generic" applications like
word processors or spreadsheets; they're very specific and
narrowly-focused applications. They rely on effectively transforming the
general-purpose computer into a very special-purpose computer.

Super-fancy desktop-based tools for analytics or Big Data processing are
not actually too useful. Anyone trying to use a desktop as an enterprise
systems of record is asking for trouble.  I work with folks trying to
process terabyte datasets on their laptops and wondering why it takes so
long. My company has servers. We pay for MongoDB and Hadoop. We have
API's to access big databases with big piles of data. I'm automating the
toolsets as fast as I can so they can work with giant datasets.

Gooey looks like fun. But not for me.





