Bottle vs. Flask vs. Django vs. a dozen others
==============================================

:date: 2015-01-29 08:00
:tags: Django,flask,bottle,WebServices
:slug: 2015_01_29-bottle_vs_flask_vs_django_vs_a_dozen_others
:category: Technologies
:status: published

There are times when a "micro framework" is actually useful. I wasn't
easily convinced that this could be true. Big framework or die trying.
Right?
Maybe not so right.
My primary example of a micro framework's value is a quick demo site to
show how some API's are going to be consumed.
I've been avoiding an `Angular.js <https://angularjs.org/>`__ app. We're
going to be supporting the user experience with a sophisticated
Angular.js app. But, as a back-end developer, I don't want to try to
write demo pages in the proper app framework. There's too many ways to
screw this up because I'll miss some key UX feature. Instead, I want to
write fake pages that show a considerably simplified version of
consuming an API. Sort of "suggestion" pages to clarify how the API's
fit together.
To make it even more complex than necessary, I'm not interested in
learning `Angular.js <https://angularjs.org/>`__, and I'm not interested
in figuring out how it works. Running `node.js <http://nodejs.org/>`__,
`bower <http://bower.io/>`__, `npm <https://www.npmjs.com/>`__, etc.,
etc., is too much.
[And Angular.js is just one version of the front-end. There's also
mobile web, mobile native, tablet native, and
God-alone-only-knows-what-all-else, to name a few. Each unique.]
Several sprints back, I slapped together two fake forms
using `bootstrap <http://getbootstrap.com/>`__ for layout and hosted
them with `Bottle <http://bottlepy.org/docs/dev/index.html>`__. The
navigation and framework look were simply copied from a screenshot and
provided as static graphics. Lame, but acceptable. All that matters is
getting the proper logo to show up.
The problem is that the sequence of API requests has grown since then.
The demo grew to where we need a session so that alternative sequences
will provide proper parameters to the APIs. We're beyond "Happy Path"
interactions and into "what-if" demonstrations to show how to get (or
avoid) a 404.
Bottle started with the significant advantage in fitting entirely into a
single .py module. The barrier to entry was very low. But then the forms
got awkwardly complex and `Jinja2 <http://jinja.pocoo.org/>`__ was
required. Now that sessions are required, the single module benefit
isn't as enticing as it once was.
I've been forced to upgrade from Bottle to
`Flask <http://flask.pocoo.org/>`__. This exercise points out that I
should have started with Flask in the first place. Few things are small
enough for Bottle. In some ways, the two are vaguely similar.
The @route() annotation being the biggest similarity. In other ways, of
course, the two are wildly different. There's only a single Flask, but
we can easily combine multiple Bottles into a larger, more comprehensive
site. I like the composability of Bottles, and wish Flask had this.
The Flask Blueprints might be a good stand-in for composing multiple
Bottles. Currently, though, each functional cluster of API's has their
own unique feature set. The bigger issue is updating the configuration
to track the API's through the testing and QA servers as they march
toward completion. Since they don't move in lock-step, the configuration
is complex and dynamic.
The transparent access to session information is a wonderful thing. I
built a quick-and-dirty session management in Bottle. It used
`shelve <https://docs.python.org/3.3/library/shelve.html>`__ and a
"simple" cookie. But it rapidly devolved to a lot of code to check for
the cookie and persist the cookie. Each superficially simple
Bottle @route() needed a bunch of additional functionality.
The whole point was to quickly show how the API's fit together. Not
reinvent Yet Another Web Framework Based On Jinja2 and Werkzeug.
`Django <https://www.djangoproject.com/>`__ seems like too much for this
job. We don't have a model; and that's the exact point. Lacking a
database model doesn't completely break Django, but it makes a **large**
number of Django features moot. We just have some forms that get filled
in for different kinds of events and transactions and searches and
stuff. And we need a simple way to manage stateful sessions.
Omitted from consideration are the other dozen-or-so frameworks listed
here: http://codecondo.com/14-minimal-web-frameworks-for-python/. This
is a great resource for comparing and contrasting the various choices.
Indeed, this was how I found Bottle to begin with.





