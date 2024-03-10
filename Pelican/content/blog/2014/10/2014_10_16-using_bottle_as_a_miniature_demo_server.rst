Using Bottle as a miniature demo server
=======================================

:date: 2014-10-16 08:00
:tags: #python,bottle,jinja,java
:slug: 2014_10_16-using_bottle_as_a_miniature_demo_server
:category: Technologies
:status: published

Let's talk small.
When writing API's, it sometimes helps to have a small demo web site to
show the API in a context that's easy to visualize. API's are sometimes
abstract, and without an application to provide some context, it can be
unclear why the path looks like that or why the JSON document has those
fields.

I want to emphasize the "small" part of the small demo. A small page or
two with some HTML forms and a submit button. Really small.
The **actual** customer-facing apps (mobile, mobile web, and full web
site) are being built by lots of other people. Not us. They're big. We
build the API's (there are a lot) that support the data structures that
support the processing that supports the user experience.

Building fake mobile apps is right out. We're not going to lard on
`Android SDK <https://developer.android.com/sdk/index.html?hl=i>`__ or
`Xcode <https://developer.apple.com/xcode/>`__ development environments
to our already overburdened laptops. We build backend API's.

Building a fake mobile web or full web site is appealing. What makes it
complex is the UX folks are building everything in
`Angular.js <https://angularjs.org/>`__. If we want to properly
implement a form, we would have to master Angular just to do a demo for
the product owner.

No thanks. Still too far afield for API developers. We're focused on
mongo and JSON and performance and scalability. Not Angular.js and the
UX.

What we want to do is build a small web server which runs just a few
pages plucked out of the UX demo code so that we can show how
interactions with a web page put stuff in a database. And vice-versa:
stuff in the database will show up on a web page.

"Really?" we get asked. Some folks look askance at us for wanting to put
a small demo site together.

"Yes," we answer. "Our product owner has a big vision and we're breaking
that into a bunch of little API's. It's not perfectly clear how we're
building up to that vision."

It's not **perfectly** clear how some of this work. Folks outside the
scrum team have distracting questions. We want to have a page or two
where we can fill in a form and click submit and stuff happens. This is
far easier to explain than showing
them `Postman <http://www.getpostman.com/>`__ or `SoapUI <http://www.soapui.org/>`__ and
**claiming** that this will support some user stories.

And as we grow toward the epic, the workflow aspects of this will grow.
The stuff that admin "A" does after user "U" has made an initial
request. Or the stuff that internal user "I" does after external user
"X" has done something. But really, it's just a few small web pages.

Small.

Imagine the demo. On laptop #1, we'll show user "X". On laptop #2, we're
running a Mongo shell to query what's in the db. On laptop #3 we're
showing user "I". The focus is really the API's. And how the API's add
up to an epic collection of stories.

Serving some HTML pages
-----------------------

Just to make it painful, we can't simply grab the demo web pages out of
the UX team's SVN repository. Why not? First, it's an Angular app. We
can't just grab some HTML and go. The demo pages are served via
`node.js <http://nodejs.org/>`__ with `Bower <http://bower.io/>`__, so
it's not even clear (to us) what the **complete** deployment looks like.

So. We cheated. We took a screen shot. We trimmed the edges of the page
as .PNG files. We wrote our own form and cobbled in enough CSS to make
it look close. We're not here to fake out the UX. We just want to enter
some data and have it tickle our API. (Indeed, we have a "Not The Real
Experience" on some pages.)

Initially, some of the team members tried serving these small pages with
`WebLogic <http://www.oracle.com/technetwork/middleware/weblogic/overview/index.html>`__.
Then `Jetty <http://www.eclipse.org/jetty/>`__. It's not bad. But it's
Java. It takes forever to build and deploy something after a trivial
change. There are a lot of moving parts even with Jetty, and not all of
them are obvious.

Since we're building "enterprise" API's, we're deeply enmeshed with
every feature of the `Spring
Framework <http://projects.spring.io/spring-framework/>`__. Our
STS/Eclipse environments are fat with add-ons and features.

While the Spring Framework ideal is to allow a developer to focus on
relevant details and have the irrelevant details handled automagically,
the magic almost gets in the way. These are small applications that are
little more than a few static pages with forms and a submit button.

Spring can do it, of course. But we're often testing our the actual
API's in a Jetty server (or two). If the demo site requires yet another
instance of Jetty with yet another configuration, our ability to cope
diminishes.

How can we get back to small?

Python and Bottle
-----------------

Python has several web servers built-in. We can use
`http.server <https://docs.python.org/3/library/http.server.html>`__. We
can use `wsgiref <https://docs.python.org/3/library/wsgiref.html>`__.
Both of these are almost OK for what we want to do.

We can do better with two small downloads:
`Bottle <http://bottlepy.org/docs/dev/index.html>`__ and
`Jinja2 <http://jinja.pocoo.org/>`__. With these, we can build simple
HTML pages that show some data. We can build simple servers that collect
form data, use
`http.client <https://docs.python.org/3/library/http.client.html>`__ to
make API requests, and write copious logging details. We can write
little bottle apps that handle just GETs and POSTs simply.

This is suitably small.

We can share the module with the Bottle object and the HTML mock-up
pages. We can fire up the app in an instant on anyone's laptop, no
matter what else they're running. We can tweak the server to adjust the
logging or the API request or the form.

We actually run the server from within Idle. Make a change and hit F5 to
redeploy after a change. It's small. It's fast. And it doesn't involve
the huge complexities associated with Java.

Bottle doesn't do much. But what little it does do is a pretty tidy fit
with tiny little demonstrations of super-simple HTML interactions.





