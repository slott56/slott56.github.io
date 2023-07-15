Code Base Fragmentation -- Again
================================

:date: 2010-12-14 08:00
:tags: #python,Django,architecture,text-template,jinja,mako
:slug: 2010_12_14-code_base_fragmentation_again
:category: Technologies
:status: published

Check this out: "`Stupid Template
Languages <http://pydanny.blogspot.com/2010/12/stupid-template-languages.html>`__".

Love this:

    "The biggest annoyance I have with smart template
    languages (Mako, Genshi, Jinja2, PHP, Perl, ColdFusion, etc) is that
    you have the capability to mix core business logic with your end
    views, hence violating the rules of Model-View-Controller
    architecture."

Yes, too much power in the template leads to code base fragmentation:
critical information is not in the applications, but is pushed into
the presentation. This also happens with stored procedures and
triggers.

I love the questions on Stack Overflow (like
`this <http://stackoverflow.com/questions/2115869/calling-python-function-in-django-template>`__
one) asking how to do something super-sophisticated in the Django
Template language. And the answer is often "Don't. That's what view
functions are for."



-----

Actually it can&#39;t violate the rules of Model-V...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-12-15 14:31:59.687000-05:00

Actually it can't violate the rules of Model-View-Controller, because
Django doesn't implement MVC in the first place. It's some variation of
PMVC or MVP at best.

http://stackoverflow.com/questions/1549857/simple-php-mvc-framework
And since you are already stretching the definition, I fail to see how
adding real presentation logic is bad. (And said example is not nearly
as bad, btw, as some PHP code \*cough\* osCommerce \*cough*.)





