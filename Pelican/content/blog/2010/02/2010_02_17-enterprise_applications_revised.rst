Enterprise Applications (Revised)
=================================

:date: 2010-02-17 15:59
:tags: #python
:slug: 2010_02_17-enterprise_applications_revised
:category: Technologies
:status: published

Enterprise Applications really make people sweat. Look at this selection
of StackOverflow questions. There are hundreds. People really get worked
into a lather over this.

-  `What makes an application an “enterprise” or “enterprise-level” application? <http://stackoverflow.com/questions/161991/what-makes-an-application-an-enterprise-or-enterprise-level-application>`__

-  `Is the LAMP stack appropriate for Enterprise use? <http://stackoverflow.com/questions/349924/is-the-lamp-stack-appropriate-for-enterprise-use>`__

-  `What is “Enterprise ready”? Can we test for it? <http://stackoverflow.com/questions/464514/what-is-enterprise-ready-can-we-test-for-it>`__

-  `Python in the enterprise: Pros and cons <http://stackoverflow.com/questions/1358084/python-in-the-enterprise-pros-and-cons>`__

There's an important subtext to this. Your favorite tool
(Python, PHP, LAMP) is not Enterprise Ready. My favorite tool
is better *because* it's Enterprise Scale.

Some folks will reject the subtext and try to say that these
are reasonable questions. Until push comes to shove and no one
seems to be able to define "Enterprise Ready". Words like
scalable and reliable crop up in vague hand-waving ways. But
without a clear yardstick for Enterprise Scale, the term has no
useful meaning.

It's import to separate useful considerations from deprecating
something you don't like. In reading the Stack Overflow
questions, I've figured out what the political consideration
behind Enterprise Scale might be.

Mission Critical
----------------

In many cases, Enterprise-Scale is taken to mean that the
software can be trusted to handle Mission-Critical or
Business-Critical computing. Sadly, even this doesn't mean
much. Numerous businesses do bad things and yet remain in
business. For example, `TJ Maxx suffers a huge theft of
information <http://www.informationweek.com/news/security/showArticle.jhtml?articleID=198701100>`__,
and they remain in business. In this case, the software that
was compromised was -- somehow -- not *actually* business
critical. The software failed; they're still in business.

    [Information loss is not a zero sum game; information
    compromise is not like theft of tangible goods. However,
    everyone would say that credit card processing is mission
    critical. Everyone.]

We can use words like "critical", but actual destructive
testing -- live business, live data, live bad-guys -- showed
that is wasn't "critical". It was central, conspicuous and
important. Based on the evidence, we need a new word, other
than "critical".

Working Definition of Enterprise Scale
--------------------------------------

In talking with a sysadmin about installs, it occurred to me
what the politically-motivated definition of Enterprise Scale
is

    **The install is not "next-next-done" wizard**

Desktop and "departmental" applications have easy-to-use
installers with few options and simple configurations.
Therefore, people who don't like them can easily say their not
Enteprise Scale.

Some folks aren't happy with Enterprise applications unless
they have configurations so complex and terrifying that it
takes numerous specialists (Sysadmins, DBA's, programmers,
managers, business analysts and users) to install and configure
the application.

That's how some folks *know* that a LAMP-based application
stack involving Python can't be enterprise-ready. Python and
MySQL install with "next-next-done" wizards. The application
suite installs with a few dozen easy_install steps followed by
a database build script. They will then spend hours talking
around numerous tangential, ill-defined, hard-to-clarify issues
to back up what they *know*.

Anything that's simple can't scale.

This is the subtext of many "your application or tool isn't
enterprise scale" arguments.



-----

good, i drop by here through keyword "sql inj...
-----------------------------------------------------

d3ck4<noreply@blogger.com>

2010-02-16 02:37:35.773000-05:00

good, i drop by here through keyword "sql injection" via a service call
"blogger auto follow" im following u.. hope to see u in my followers
list soon and would love to share anything from internet, network and
information security stuff.

regards,

Hacking Expose! Team


Hello, I started writing a comment to your post, b...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-02-17 06:53:29.379000-05:00

Hello, I started writing a comment to your post, but it grew too much so
I thought of posting it in my blog:
http://geekscrap.com/2010/02/what-enterprise-grade-really-means/
I would really appreciate your opinion on it :-)


Good Post! Very informative, glad that you are goi...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-02-18 08:45:53.389000-05:00

Good Post! Very informative, glad that you are going to continue writing
things like this!
Regards.
http://www.cooperburns.co.uk


The mistake you make in TJ Maxx&#39;s case is assu...
-----------------------------------------------------

Steve<noreply@blogger.com>

2010-02-15 12:01:50.473000-05:00

The mistake you make in TJ Maxx's case is assuming that data theft
deprives the original owner of a copy. Without that data their sales and
marketing operations may well have ground to a halt, but someone else
taking an illicit copy (while it \*should\* have been fatal if there was
any justice in the world) didn't stop them from operating.

As for the rest, that would normally fall under the umbrella of "complex
operating environment". However the Python Software Foundation has a
complex operating environment, but its applications aren't enterprise
applications.

And Apache, which (on Windows at least) can be installed with a
next-next-done wizard, needs complex configuration afterwards before it
can truly be said to be operational, surely? So I am not sure how
helpful this definition will be.





