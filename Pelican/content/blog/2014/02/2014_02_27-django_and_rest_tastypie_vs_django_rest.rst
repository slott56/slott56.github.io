Django and REST -- Tastypie vs. Django REST
===========================================

:date: 2014-02-27 08:00
:tags: REST,Django
:slug: 2014_02_27-django_and_rest_tastypie_vs_django_rest
:category: Technologies
:status: published

| Ouch. What a difficult question.

   Lazyweb: Django REST Framework vs. Tastypie. Thoughts?
   `#django <https://twitter.com/search?q=%23django&src=hash>`__
   — Joe Dougherty (@modusjonens) `February 17,
   2014 <https://twitter.com/modusjonens/statuses/435518784036540416>`__

| This isn't easy.
| Comparing http://django-tastypie.readthedocs.org/en/latest/
  with `http://www.django-rest-framework.org <http://www.django-rest-framework.org/>`__
  is hard. They're both outstanding projects with a long history.
| Trivial Follow-up Question 1: What are the requirements?
| I happen to know, however, a bit about the context, so I suspect that
  the requirements center around super-flexible data access and numerous
  serialization formats.
| **History**
| My initial reaction is "Django-REST" of course. Mostly because I
  started with this several years ago and spent some time tweaking and
  adjusting my local copy. Our requirements involved adapting Django
  (and Django-REST) to use Forge Rock Open AM for authentication.
| One feature that we didn't need was a sophisticated set of built-in
  transactions that covered the full REST spectrum of GET, PUT, POST and
  DELETE. 90% of our processing was GET with an occasional POST.
| The other feature we didn't need was a trivial mapping from the Django
  object model. Our GET processing required view functions as mediation
  between our database models and the "published" model available
  through the RESTful API.
| Since we needed so little, we hacked out the essential serialization
  feature set to support our GET operations.
| **Serialization**
| Considering the context of the initial question, I think that
  serialization is the deciding factor. Comparing the serialization
  features seems to indicate that the following summary may be relevant.
| Tastypie serialization is simpler. The support for XML, YAML, JSON,
  etc., is simple.
| Django-REST serialization+render is quite a bit more sophisticated and
  more flexible. The process is explicitly decomposed into serialization
  (for breaking down the model objects) and rendering in some external
  representation like XML, JSON, YAML, etc.
| This two-step breakdown in Django-REST seems to make an open data
  project work out nicely. The developers should find it easier to
  integrate and publish data from a variety of sources.





