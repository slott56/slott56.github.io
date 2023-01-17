Real Security Models
====================

:date: 2010-10-14 07:46
:tags: Django,#python,security
:slug: 2010_10_14-real_security_models
:category: Technologies
:status: published

Lots of folks like to wring their hands over the Big Vague Concept
(BVC™) labeled "security".

There's a lot of quibbling. Let's move beyond BVC to the interesting
stuff.

I've wasted hours listening to people identify risks and costs of
something that's not very complex. I've been plagued by folks
throwing up the "We don't know what we don't know" objection to a web
services interface. This objection amounts to "We don't know every
possible vulnerability; therefore we don't know how to secure it;
therefore all architectures are bad and we should stop development
right now!" The `OWASP top-ten
list <http://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project>`__,
for some reason, doesn't sway them into thinking that security is
actually manageable.

What's more interesting than quibbling over BVC, is determining the
authorization rules.

Basics
------

Two of the pillars of security are Authentication (who are you?) and
Authorization (what are you allowed to do?)

Authentication is not something to be invented. It's something to be
used. In our case, with an Apache/Django application, the Django
authentication system works nicely for identity management. It
supports a simple model of users, passwords and profiles.

We're moving to `Open SSO <https://opensso.dev.java.net/>`__. This
takes identity management out of Django.

The point is that authentication is -- largely -- a solved problem.
Don't invent. It's solved and it's easy to get wrong. Download or
License an established product for identity management

and use it for all authentication.

Authorization
-------------

The Authorization problem is always more nuanced, and more
interesting, than Authentication. Once we know who the user is, we
still have to determine what they're really allowed to do. This
varies a lot. A small change to the organization, or a business
process, can have a ripple effect through the authorization rules.

In the case of Django, there is a "low-level" set of authorization
tests that can be attached to each view function. Each
`model <http://docs.djangoproject.com/en/dev/ref/models/options/>`__
has an implicit set of three permissions (can_add, can_delete and
can_change). Each view function can test to see if the current user
has the required permission. This is done through a simple
`permission_required <http://docs.djangoproject.com/en/dev/topics/auth/#the-permission-required-decorator>`__
decorator on each view function.

However, that's rarely enough information for practical — and nuanced
— problems.

The `auth profile
module <http://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users>`__
can be used to provide additional authorization information. In our
case, we just figured out that we have some "big picture"
authorizations. For sales and marketing purposes, some clusters of
features are identified as "products" (or "features" or "options" or
something). They aren't smallish things like Django models. They
aren't largish things like whole sites. They're intermediate things
based on what customers like to pay for (and not pay for).

Some of these "features" map to Django applications. That's easy. The
application view functions can all simply refuse to work if the
user's contract doesn't include the option.

Sadly, however, some "features" are part of an application. Drat. We
have two choices here.

-   Assure that there's a "default" option and configure the feature
    or the default at run time. For a simple class (or even a simple
    module) this isn't too hard. Picking a class to instantiate at run
    time is pretty standard OO programming.

-   Rewrite the application to refactor it into two applications: the
    standard version and the optional version. This can be hard when
    the feature shows up as one column in a displayed list of objects
    or one field in a form showing object details. However, it's very
    Django to have applications configured dynamically in the settings
    file.

Our current structure is simple: all customers get all applications.
We have to move away from that to mix-and-match applications on a
per-customer basis. And Django supports this elegantly.

Security In Depth
-----------------

This leads us to the "Defense in Depth" buzzword bingo. We have SSL.
We have SSO. We have high-level "product" authorizations. We have
fine-grained Django model authorizations.

So far, all of this is done via Django group memberships, allowing us
to tweak permissions through the auth module. Very handy. Very nice.
And we didn't invent anything new.

All we invented was our high-level "product" authorization. This is a
simple many-to-many relationship between the Django Profile model and
a table of license terms and conditions with expiration dates.

Django rocks. The nuanced part is fine-tuning the available bits and
pieces to match the marketing and sales pitch and the the legal terms
and conditions in the contracts and statements of work.



-----

What about http://forgerock.com/?

OpenSSO Express...
-----------------------------------------------------

Rudiger Wolf<noreply@blogger.com>

2010-10-14 19:30:45.179000-04:00

What about http://forgerock.com/?
OpenSSO Express has been removed for download from Oracle's website,
leaving users of the community version of what was Sun's single sign-on
platform to either, build their own version from source code, or to go
to a third party. Norwegian company ForgeRock has stepped in and
released OpenAM, based on OpenSSO source code.





