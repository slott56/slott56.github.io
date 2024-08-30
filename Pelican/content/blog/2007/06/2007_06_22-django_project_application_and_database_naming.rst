Django Project, Application and Database Naming
===============================================

:date: 2007-06-22 19:25
:tags: open-source,Django,Design,Scope
:slug: 2007_06_22-django_project_application_and_database_naming
:category: FOSS
:status: published







When you start fresh (as I sometimes do), you create a `Django <http://www.djangoproject.com/>`_  project into which you create your first application.  You use django-admin.py to spin up a project directory, and from in side there, use manage.py to create an application boilerplate.



The Django folks are very clear on their value proposition:  The admin interface is already there.  Just build the model, start loading data, and work on the presentation as your requirements solidify.  This is really outstandingly agile.  I can build a model, test, populate and clarify the core model issues quickly.



What's important is that I'm old (really old) and we used to spend a long time gathering requirements, designing things, and drafting a complex architecture before we coded anything.  When I started in this business, word processing was rare and expensive, often done in ALL CAPS.



So I have an urge to build really comprehensive sets of requirements and designs and models.  Which tends to break the basic value proposition of Django.



Small is Beautiful
------------------



On consequence of the Django world view is to start small.  The suggestion is to pick a subject area, put the essential data elements together, and call that an "application".  To this, you'd add applications as you add subject areas.



This seems to fit in with the Web Mart design pattern in `CACM <http://www.acm.org/cacm/>`_  Vol 50 Issue 4 ("`Designing data-intensive web applications for content accessibility using web marts <http://portal.acm.org/citation.cfm?id target=>`_ ").  You have a Core Concept, access dimensions and supporting detail dimensions as a single Django application.



Nomenclature
------------



Here's how it seems to work.



The "top level" is the Project.  A Project contains one settings.py file.  This means that (generally) a Project has one database, one puddle of media files, a puddle of common template files, one top-level URL map, and *n*  individual applications.  (Yes, this is not *fixed* ; Django is flexible, to an extent.)



Within a project, each of the applications gets an application-specific data model, templates, views, and a localized URL map.



What's important is that the first application is not the only application.  In many cases, the first application will be the most superficial "index.html" kind of application for the available data.  It will often house the default pages for non-authorized, general public users.  Further, it will present the central-most of the Core Concepts in the data model.  As new applications are added, this may evolve in parallel to show overviews or or links to the data in the newer applications.



The problem that I have is that I often conflate the project with the first application that I'm building under the project.



Bad Names
---------



It's clearly lame to create a project around some subject ("art portfolios") and then create a single application that effectively duplicates the project's name ("portfolio").  The first application is rarely the only application.  Too generic an application name is limiting.



Similarly, vague names like "main", "core" and "default" are kind of silly, since they don't mean very much.  However, in some cases, your first application will be the one that gets the "all other" URLs.



For example, your top-level URL's may map '/admin' to the admin interface, '/feedback' to the feedback application, '/about' to a static "about" pages, and '/' to the main? core? default? application.  Grrr.  What to call this?



Better Names
------------



It seems that we have to find a way to characterize the first application's data model without having built the rest of the applications and their data models.  Since I'm old (and forgetful) I have the urge to design them all, then cut them up and give them intelligent names.  Since I'm learning to be Agile, I'm trying to avoid designing them all, but rather, sketch in the big picture, then detail one area while keeping a sense of "where this is all going."



I think that there's a hidden feature of Django -- not called out in their documentation -- that helps resolve this.  I think that the Django "application" is really a use case, or a very small set of closely-related use cases.  I think that the Django application names should be aligned with use cases.  This leaves the overall Django project to be the overall system which contains those use cases.



Example
-------



Let's say that the client claims they want just one little customer service thing.  Just a little database that allows a customer to determine their warranty coverage given a couple of pieces of information.  Of course, the template has to match the static content.



So, the project is Warranty Coverage.  What's the application?  Warranty coverage?  Ick.  That's what we're trying to avoid.



What's the use case?  It sounds like the application is "browseCoverageByDate" or something that parallels the use case name.  Another application might include "purchaseAdditionalCoverage" or similar use case name.



It's also possible that the project isn't named broadly enough.  This would happen in the unlikely circumstance that someone picked a verb-noun phrase for the overall project.  



Consequence
------------



For Proof-of-Concept, Django rules.  However, one can't rush headlong into project and application names.  The project needs to be broadly named, and the application focused on use cases.  The problem with Django as Proof-of-Concept, is that can be migrated into production very easily.



The overall project name, as a collection of Core Concepts, is some noun phrase that embodies the content of the (one) database and (one) puddle of media files.  To pick this name, we need a sense of the overall collection of applications.  If we can't nail that down, we should pick a broad enough project name that we won't be embarrassed by the name.  Too broad is easy to justify.  Too narrow requires explaining what the objective used to be when we chose that lame-assed name.



The application names are a little trickier because they are use cases that describe how users access the data in the database.  In some cases, we're writing our own transactions.  In this case use-case style "verb-noun" phrases make sense ("update address", "cancel order", etc.) In other cases, we're presenting data built with the admin interface.  In this case, the verb is always "browse" or "get", so we can consider omitting it.  In this case we name the application around the core concepts.



Projects require thinking broadly.



Applications require use cases.





