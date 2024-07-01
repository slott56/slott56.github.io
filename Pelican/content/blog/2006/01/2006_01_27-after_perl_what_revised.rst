After Perl, what? (Revised)
===========================

:date: 2006-01-27 00:58
:tags: LAMP,perl,php,java,python,ruby
:slug: 2006_01_27-after_perl_what_revised
:category: Management
:status: published





The Problem
-----------



Perl's old.  And Perl is
without shame about adopting every syntax gimmick on earth.  Consequently, Perl
has accreted enough features that Perl programs are hard to read, making them
impossible to maintain.  More thoughts on this opacity problem in Gadgetopia
http://www.gadgetopia.com/post/1919 and Freshmeat http://freshmeat.net/articles/view/1339/.



Further, Perl 6 is caught up in political wrangling of the first magnitude.  There's the
Larry Wall camp (Apocalypses), Curl, Lua, Monkey, Ponie and Parrot.  And there's
further opinions like Rindolf http://vipe.technion.ac.il/~shlomif/rindolf/%22%20target=%22NewWindow.



Perhaps most limiting, Perl isn't a hotbed of application frameworks [`Thanks <http://www.haloscan.com/comments/slott/E20060126195803/#66236>`_ ].
Products include `Catalyst <http://catalyst.perl.org/>`_  and `Maypole <http://maypole.perl.org/>`_ .
Perl suffers from being one of the first scripting extensions to Apache,
consequently innovation was focused elsewhere.  Java, PHP, Python and Ruby all
have the advantage of many sophisticated frameworks that minimize the
programming and consequently, minimize the obscurity of the programming
language.



Some Choices
-------------



If Perl is too opaque for
ongoing use, and the future of Perl is cloudy, we should probably think about
moving on to another language.  So step one is the following
advice:

Ditch Perl
-----------



When we ditch Perl, we'll need to replace it
with some language.  Which one?  Further, we'll need a plan for retiring working
applications in Perl and upgrading them to something newer and less
opaque.



O'Reilly's LAMP http://www.onlamp.com/ architecture
(Linux-Apache-MySQL-P.*) lifts up three languages: Perl, PHP and Python. 
Recently, Ruby has matured to the point where it deserves some consideration. 
Finally, there's always Java.  



Here's a chart http://www.jvoegele.com/software/langcomp.html that provides some head-to-head comparison
among these languages.  One issue, of course, is that languages express ideas,
and the world of software is big:  too big for a single language.  There is no
one-language "right" answer.  This isn't a trick question.  We're going to look
at tradeoffs and priorities: always messy
work.



The One True Language
---------------------



Let's dispose of the
one-language-to-rule-them-all-and-in-the-darkness-bind-them
myth:

-   We have command languages like the shell
    optimized for a few tasks like running programs

-   We have markup languages (HTML, XML)

-   We have programming languages for
    complex, high-performance processing (C)

-   We have data query languages (SQL)

-   We have specialized template languages
    for assembling HTML results from data queries and lightweight computations (JSP,
    PHP)

-   We have other programming paradigms
    embodied in Haskell, Groovy or
    Prolog



We have the good-old
general-purpose language (Python, Perl, PHP, Java, Ruby) that can do almost
anything.  Doing almost anything translates to doing anything badly and doing
nothing well.  For any of the above specific purposes, general-purpose languages
are just too wordy.



The Domain
----------



If one language won't solve all of
our problems, we'll need to pick a problem, then pick a suitable language. 
Let's focus, then, on web application development.  Further, let's look at
someone with a legacy of applications developed primarily in Perl.  We need to
look at the alternatives to Perl for web application
development.



Compounding the problem is
the rest of the architecture stack.  We can't easily focus narrowly on using
just Apache as the web server.  While "bare" Apache had some appeal in the murky
past, the world has matured.  CGI and mod_Perl are no longer new; a great deal
of useful infrastructure has arisen, which can reduce the volume of programming
necessary to put dynamic, interactive content onto the
web.



When we look at languages, we're
really looking at a programming environment which includes a web application
framework and a programming language.  Our programming language(s), then,
extend, customize and tailor a generic web application for our specific customer
requirements.  This will complicate our analysis because we aren't merely
comparing languages, we're really comparing framework +
language.



Some Quality Factors
----------------------



We can't easily evaluate
all of the tools available.  However, we can provide some essential criteria
that can be used to narrow the field
rapidly.



1.  Model-View-Controller separation.  The data model, the HTML view, and the controls must be
    separated.

2.  Object-Relational Mapping with
    Persistence.  We should be able to bury our SQL in mapping rules.  Ideally, it's
    generated seamlessly and silently.

3.  RDBMS-agnostic.  Any of the MySQL, Postgres, SQLite products (or any of the expensive, commercial products) should be
    supported.

4.  Web best-practices:  session management, POST-redirect-GET, validation and quoting to prevent SQL/Shell
    command injections, etc.



Additionally, the number of skilled people is important.  Here is the TIOBE programming
community index http://www.tiobe.com/tpci.htm for the languages we're looking at.  We'll
discard C and C++ as being unsuitable for web applications:  Python does the
same processing as C (or C++) without the endless (and error-prone) drudgery of
memory management.  While popular in general, they aren't applicable to web
applications.  Additionally, we'll discard VB and C# because they are
proprietary products and have a cost which exceeds their real value.


1.  **Java**

#.  C 

#.  C++ 

#.  **PHP** 

#.  VB 

#.  **Perl**

#.  C#

#.  **Python** 

(off the list): **Ruby** 

Java
----


Java is totally dominated by J2EE (Tomcat, JBoss, etc.) as the application framework.
Apache Struts http://struts.apache.org/ or Spring http://www.springframework.org/ put
an MVC framework on top of J2EE.  Toplink, JDO and Hibernate are choices for the
Object-Relational Mapping http://c2.com/cgi-bin/wiki?ObjectRelationalMapping and Persistence.  Plus, there are
pure-persistence packages http://java-source.net/open-source/persistence.




Struts can be complex (at first)
because it is a very sophisticated environment which finely partitions the work
among the Action classes, the struts-config definitions, validations, and EJB's
(or POJO's).  Struts, however, has the advantage of separating the model, the
view and the control into EJB's, JSP's and Action classes.  The EJB's write
themselves, since they are the enduring business facts.  The JSP's write
themselves because they are the presentations, done with JSP's HTML template
language.  The struts configuration handles the subtlety of transaction flow,
and the most obvious validation rules.  What's left?  The "business rules" --
validations that can't easily be written as simple XML-encoded rules, and the
actual effect of the web transaction (ordering, canceling, inquiring,
etc.)



Sadly, however, the JSP world was
originally a complete stand-alone application development environment, so it has
a bewildering level of feature-itis.  Further, the XML-based JSP's have a number
of extension tag libraries that are a mixed blessing.  Yes, forms are very easy
to create.  No, you'll never understand all of those JSP tag
libraries.



Java is, however, pure
OO-programming:  everything is very clean and precise, and you have the full
power of inheritance and the sophisticated design patterns.  Some of the
mystique of EJB's can be eliminated in favor of Plain-Ol' Java Objects (POJO's).
Generally, the complexities of EJB's aren't all that pleasant to deal with, so
I'm a POJO
programmer.



PHP
-----



PHP has over 40 individual frameworks http://www.phpwact.org/php/mvc_frameworks, http://dmoz.org/Computers/Programming/Languages/PHP/Scripts/Frameworks/.  How to penetrate the clutter?  There is
no quick answer.  Just looking at PHP content management http://dmoz.org/Computers/Programming/Languages/PHP/Scripts/Content_Management/ turns up a huge list.  Some sorting is
available at CMS Matrix http://www.cmsmatrix.org/.  However, LinuxWorld http://linux.sys-con.com/read/86022.htm has selected two that merit serious
consideration: **Mambo** http://www.mamboserver.com/
and **phpWebsite** http://phpwebsite.appstate.edu/.



When I first looked at PHP (five years ago, in 2000), the language looked like a
clutter of features, and a seemingly-endless library of functions.  While it's
nice to have all those functions, I would have appreciated a few packages and
modules to break them into more meaningful chunks.  More important to me would
have been a focus on object-oriented programming as the way to build web
applications.  However, PHP was originally an HTML template language on
steroids, and seems to remain focused on that
niche.



The frameworkes make PHP more
palatable; separating model, view and control is absolutely essential to
success.  Classical PHP (without a framework) is little more than Java JSP, and
has the same basic complexity.



While PHP has class definitions, Mambo doesn't emphasize OO-style examples.  On the
other hand, phpWebsite, does seem to land on the OO feature set.  The list of
object-oriented MVC frameworks http://www.google.com/search?q=php+object-oriented+framework shows how important it is to promote reuse
and simplification using
objects.



Python
-------



Python
has over 30 frameworks http://wiki.python.org/moin/WebProgramming.  The question is, which are production
ready and reasonably complete?  The answer is to look at frameworks which build
complete content-management solutions.  These can then be tailored for on-line
shopping or any other purpose.  This is a shorter list http://wiki.python.org/moin/ContentManagementSystems including the following:

-   **Zope** http://www.zope.org/,

-   **Nevow** http://divmod.org/projects/nevow,

-   **Webware** http://www.webwareforpython.org/,

-   **Django** http://www.djangoproject.com/.



With Python, the object-orientation isn't mandatory, but is almost universal, unlike PHP or Perl.



Zope takes a very interesting approach to creating content as an assembly of elements.  The
interaction between the Zope DB, the various page templating tools, and the
Python programming language works out very nicely.  Zope is not a rehashing of
other technologies, but a clean and unique approach to web presentation.  In
can, consequently, be very uncomfortable to have Zope do so much and you (the
programmer) do so little.



Django is a little more conventional.  It has an explicit Model, View, Controller separation
and leans on Struts (to an extent).  It has an easy-to-live-with templating
language, full Python programming, and a sophisticated set of built-in
capabilities.  It has a model definition capability that takes some getting used
to, but once you work out the details, the default object-relational mapping can
be made to work nicely.



Nevow's approach to mixing Python programming and template insertion makes use of some
slightly extended HTML syntax.  This has the pleasant consequence of allowing
someone to design pages in largely "pure" HTML, then slap a few special purpose
tag attributes into things like ``<span>`` tags, to provide a linkage with
Python programs.  Python has the functions, the stan markup extensions provide
the presentation.



WebWare has a Servlet engine (like J2EE web applications), it also has Kid and PSP's, which are
PHP-like (or JSP-like) template pages with Python code inserted.  Consequently,
you can use the WebKit servlets and KidKit template pages to build a very robust
Struts-like
application.



Ruby
----




Ruby, as the new language, still has
much to prove.  It enjoys considerable popularity because it has numerous
features and the Rails web application framework is very powerful.  Ruby (like
Python) embodies a DRY - Don't Repeat Yourself - philosophy.  There aren't a lot
of external configuration files and additional descriptive material.  The Ruby
language (like Python) includes enough introspection that the code can examine
itself to do the various mappings from HTML Form to Object to Relational row.



However, Ruby has one serious
flaw: it is largely opaque.  Part of that is the novelty of the language.  But
part of it is the very "spare" look, without a lot of punctuation or other
visual cues.  Ruby may have the same problem that Perl has.  Perl and Ruby may
both be examples of write once programming languages.  They may be
unmaintainable.



Action Plan
------------



Look closely at PHP and Python for a Perl replacement.  Each framework has a "style" or "flavor" that is
difficult to summarize.  However, once experienced, it is either compelling or
confusing.  There's a lot of room for researching and there's a fine line
between researching and hang-wringing.  Here's the
plan.



1.  Download PHP.  Take a few
    weeks and write some small demo programs in PHP to see how it works, and how
    well it fits your mind-set.



2.  Download Python.  Take a few weeks and write some small demo programs in
Python.



3.  Make the first (and toughest) decision: PHP or Python.  PHP will probably be more familiar to a
    procedural Perl programming.  Python's object-orientation may be hard to fathom.
    In the long run, OO allows you to create far more sophisticated programs.  But
    it can be a difficult programming style to
    learn.



4.  Once you've chosen a
    language, you can then choose a framework.  Download an appropriate combination
    of Mambo, PHPWebSite, Django, Nevow, WebWare, and Zope.




5.  Do the tutorials for the products
    you've downloaded.  You may, at this time, rethink your language choice, and
    decide to try the other language and the other frameworks.  However, stick to
    the tutorials so that you can minimize your investment in technologies that you
    won't make serious use of.  In some cases, the documentation of the tutorial may
    be enough to provide you a hint that the approach doesn't resonate well with
    your mental model of web
    applications.



6.  Convert something small, safe and reliable to the chosen framework.  You will make mistakes.  It
    won't be easy.



7.  Convert something
    else small, safe and reliable.  Rework your mistakes in the previous
    conversion.



Conclusion
----------



Perl's opacity makes Perl it's own problem.  It's great to write in, but awful to
maintain.  Replacing Perl is hard -- you can stick with procedural programming
and choose PHP, or you can make a decision to exploit the power of objects and
choose Python.  You can leverage large, expensive, commercial products and
choose Java, also.



More important is the choice of web application frameworks.  The idea of a framework is to
structure the application and leverage existing code from other projects as much
as possible.  This is the big win in replacing Perl: exploiting
well-thought-out, next-generation frameworks for web applications.
























