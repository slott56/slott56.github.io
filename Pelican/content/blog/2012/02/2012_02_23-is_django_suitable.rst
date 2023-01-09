Is Django Suitable?
===================

:date: 2012-02-23 08:00
:tags: Django,#python
:slug: 2012_02_23-is_django_suitable
:category: Technologies
:status: published

I got a long list of requirements from a firm that's looking to build a
related family of web sites.  They were down to a Django vs.
Ruby-on-Rails decision.


As you can see, they've done their homework in thinking through their
needs.



I grouped their "high-level requirements" into several
categories.  I summarizes the fit with Django here, and
provided into details separately.


-   **Authentication**.  Django supports flexible logins and
    Python makes it easy to adapt other security API's.  Django
    and Python assure that this is a solid 10.

-   **Shared Code**.  This is handled through Python features
    that are central to the Django framework.  Shared code
    management -- with appropriate overrides and customization
    -- is part of Python and a 10.

-   **Database Access**.  While Django provides the
    necessary access features, database scalability depends on
    the implementation of the database engine itself.  There are
    numerous parallelization features that must all be used to
    maximize database throughput.  Even though the real
    responsibility for performance is outside Django, the Django
    flexibility results in a 10.

-   **AJAX and Javascript**.  Django supports the
    necessary RESTful API's.  However, Django treats JavaScript
    as simple static content, offering little specific support.

    Since JavaScript support is not an *essential* part of
    Django, perhaps this is only a 5.

-   **Applications**.  The various applications described in the
    requirements are more-or-less irrelevant to Django.  They
    can be built easily, but are not first-class features of
    Django.  In the sense of easy-to-develop, this is a solid
    10.  In the sense of already-existing-applications, this may
    be a 5 if the applications are part of a community like
    Pinax.  Because the applications do not already exist,
    this may also be a 0.

-   **API**.  Python allows use of any API.  Django's
    transparent use of Python makes it easy to build API's.
    This is a feature of Python and scores 10 out of 10.

-   **Usability and Developer Skills**.  Django's ease-of-use is
    a direct consequence of the Python programming language. The
    developers of Django make excellent use of the Python
    language,  giving this a 10.

-   **Performance, Access and Scalability**.  For the most part,
    Django performance comes from consideration of the purpose
    of all layers of the architecture.  Principle design
    features include keeping static content separate from
    dynamic content (reducing Django's workload), and optimizing
    the database (to hande concurrent access well).  Django
    provides several internal design features to minimize
    memory.  Django  encourages proper separation of concerns,
    giving a 10.

 
In each of these areas, it's possible to dive into
considerable depth.  It was tempting to offer up
proof-of-concept code for some of the questions.


-----

And coincidentally, mentioned in another Planet Py...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2012-02-24 08:23:05.855000-05:00

And coincidentally, mentioned in another Planet Python post just a few
entries after this one: http://www.dajaxproject.com/
May help address the Django + AJAX question.

I particularly liked this example:
http://www.dajaxproject.com/maps/


On the performance front: you can run a Django sit...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2012-02-24 08:06:44.261000-05:00

On the performance front: you can run a Django site on PyPy to both
optimise execution speed and reduce memory usage at the same time.
For database access: Django can also be set up to use SQLAlchemy, one of
the most powerful and flexible database abstractions available.

(You already scored Django highly for both of those, so these are really
just confirming your assessment)


Indeed this is the Best thing about it is that it ...
-----------------------------------------------------

Admiral Adney<noreply@blogger.com>

2012-05-07 06:51:06.599000-04:00

Indeed this is the Best thing about it is that it is open source but its
really hard to find the appropriate `ruby on rails development
company <http://www.goodcoresoft.com/ruby-on-rails-portal-development/>`__
or to `hire ruby on rails
developer <http://www.goodcoresoft.com/hire-ruby-on-rails-developers/>`__
.





