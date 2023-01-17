Getting Started Creating Web Pages
==================================

:date: 2010-04-05 08:00
:tags: RST,PHP,Django,#python,HTML
:slug: 2010_04_05-getting_started_creating_web_pages
:category: Technologies
:status: published

Got this question recently.

    I’m looking for an HTML editor that fits into my price range (free
    of course). I don’t need to do anything fancy, just vanilla HTML
    to run on an Apache server ..., and maybe some PHP down the line.
    Can you recommend any open source or shareware software that would
    run on Windows?

What to do?

First, civilized folks don’t edit HTML any more. That’s so 1999.

You have a spectrum of choices if you want to try and edit HTML.

-   **General-purpose text editors**. Good ones do HTML syntax
    coloring. This is the hardy, forge-through-the-forest way to
    go. Raw text editing. Like when we were kids.
    http://en.wikipedia.org/wiki/List_of_text_editors. In Windows
    world, I use
    `Notepad++ <http://notepad-plus.sourceforge.net/uk/site.htm>`__.

-   **HTML-specific editors**.
     http://en.wikipedia.org/wiki/List_of_HTML_editors. Note that
     WYSIWYG HTML Editing is more trouble than you’d believe
     possible. It’s always fun for the first few months, but then
     you try to do something that confuses the GUI interface and you
     wind up with an entire paragraph in italics and can’t figure
     out why. Or you want to move a punctuation outside a link and
     discover that the editor just can’t figure out where the tag is
     supposed to fall and puts everything inside it. Most of us do
     not try to use WYSIWYG HTML editors because it slowly becomes
     annoying once you get beyond the trivial basics.

-   **IDE’s**. To produce HTML sensibly, you have to also write
    .CSS style sheets, and you often have a number of related
    pages. Essentially, a “project”. An IDE is usually a better
    choice than an editor. All the good IDE’s are free: Eclipse,
    NetBeans and Komodo Edit. I use ActiveState `Komodo
    Edit <http://www.activestate.com/komodo_edit/>`__ heavily.

While NetBeans or Komodo Edit seems like overkill, it will
(eventually) pay out as you move into developing more than static
HTML pages.

Better Than HTML
----------------

Instead of creating HTML, many of us use “Lightweight Markup”
which is much, much easier to cope with and simple tools to
produce HTML from the markup.
http://en.wikipedia.org/wiki/Lightweight_markup_language

I use
`reStructuredText <http://en.wikipedia.org/wiki/ReStructuredText>`__
instead of HTML. I use the
`DocUtils <http://en.wikipedia.org/wiki/ReStructuredText#Docutils>`__
project, which has an rst2html.py tool that converts my RST into
HTML for me. I also use rst2s5.py to create power-point-like
presentations from my reStructuredText. If you want to see the
power of RST, you can look at my `personal
site <http://homepage.mac.com/s_lott/steve/index.html>`__ and my
`books <http://homepage.mac.com/s_lott/books/index.html>`__: and.
100% RST. No manual HTML anywhere. I use
`Sphinx <http://sphinx.pocoo.org/>`__ to create really complex
docments like the books.

For some tasks, I use HTML templates and simple scripts to process
data and create static HTML from the data. You’d be surprised how
effective this is. Few things require up-to-the-second web
applications. Many things can be done as nightly batch programs
that emit static HTML and FTP the HTML up to the web page. No PHP.

Application Development
-----------------------

For web development, PHP is fine. It will – before long – create
holes in your head because it’s so badly thought out. But for
getting started, it’s fun. Real companies (like Google) don’t
waste their time with it because of the numerous problems PHP
causes.

“Problems?” you say. “What problems?”

PHP’s world view (HTML + code in a single package) is a terrible
architecture. It’s horribly slow and leads to very muddled,
inflexible designs. Everyone who tries to make a global change to
their site's “look and feel” finds that PHP is inflexible and a
regrettable platform. Even folks who simply want consistency among
several different pages within their site find that the PHP world
view is more headache than solution.

But it’s fun when you first build a site that works.

Frameworks
----------

Generally, most folks find that a “framework” is absolutely
essential for debugging, consistency and separating Content,
Processing and Presentation. Even a simple Blog or Forum or
Visitor Registration has separate Content, Processing and
Presentation; PHP muddles these. A framework can help unmuddle
them.

I use `Django <http://www.djangoproject.com/>`__ as framework and
Python as programming language. Your hosting site may not support
this, in which case you may be in trouble.

The `Web Frameworks
list <http://en.wikipedia.org/wiki/Comparison_of_web_application_frameworks#PHP>`__
on Wikipedia is good. Zend and CodeIgniter are highly recommended
in places like
`StackOverflow <http://stackoverflow.com/questions/2648/what-php-framework-would-you-choose-for-a-new-application-and-why>`__.
However, here's a good Django vs. PHP comparison: `The Onion Uses
Django, And Why It Matters To
Us <http://www.reddit.com/r/django/comments/bhvhz/the_onion_uses_django_and_why_it_matters_to_us/>`__.

    "Because Cleaner. Much cleaner. Proper unit testing. Real reusable
    components across applications. An ORM rather than a just a series
    of functional query helpers...."

Summary
-------

#.  Get an IDE to edit your pages. **Komodo Edit**.

#.  Consider using RST and tools instead of raw HTML. Installing
    Python + DocUtils and using rst2html.py is easier than learning
    HTML.

#.  Try to avoid PHP’s numerous pitfalls; ideally by avoiding PHP.
    Use Django + Python and create a real application that clearly
    separates the content (data model) from processing (view
    functions) from presentation (HTML templates)



-----

Hi thanks for sharing. you see power pack open sou...
-----------------------------------------------------

patrick<noreply@blogger.com>

2010-04-06 01:32:49.801000-04:00

Hi thanks for sharing. you see power pack open source web sites no
problem see on `Web design and
developments <http://www.itemplatez.com%22>`__


Suggestion: look into CakePHP.  

Most of my exper...
-----------------------------------------------------

Jerry Seutter<noreply@blogger.com>

2010-04-05 12:41:36.170000-04:00

Suggestion: look into CakePHP.
Most of my experience is with Django and Pylons, but I recently looked
into CakePHP and have found it \_very\_ easy to use. It splits up
Views/Models/Controllers just like any other MVC web framework.
Deployment of PHP apps is dead simple on my shared hosting account.
Python apps require more work for me to deploy.


I agree with the author that PHP’s world view (HTM...
-----------------------------------------------------

Marcus_Dane<noreply@blogger.com>

2010-05-18 10:37:34.437000-04:00

I agree with the author that PHP’s world view (HTML + code in a single
package) is a terrible `website
architecture <http://www.webbizdesigns.com/web-architecture>`__. But
using frameworks is the best solution to fix the problem. For `web
application
architecture <http://www.webbizdesigns.com/web-architecture>`__, web
developers need to learn possible ways to use HTML or PHP whichever is
necessary. But then again, the author forewarned web developers to try
avoid PHP’s numerous pitfalls; ideally by avoiding PHP.


Thanks for the information, we will add this story...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-07-21 14:45:33.169000-04:00

Thanks for the information, we will add this story to our blog, as we
have a audience in this sector that loves reading like this” `web
development <http://www.fundootemplates.com>`__


Very interesting and useful post, thank you for sh...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-09-27 07:14:28.361000-04:00

Very interesting and useful post, thank you for sharing this with us.
`web design company <http://www.web-designs-company.com>`__





