Things that start badly
=======================

:date: 2019-01-29 08:00
:tags: mako,#python,jinja
:slug: 2019_01_29-things_that_start_badly
:category: Technologies
:status: published

Today's Example of Starting Badly: Building HTML.


The code has a super-simple email message with
``f"<html><body><p>stuff {data}</p></body></html>"``. It was jammed
into an email object along with the text version. All very nice.
For a moment, I considered suggesting that f-string substitution
wasn't a good long-term solution, since it doesn't cover anything
more than the most trivial case.

Two things stopped me from complaining:

-  The case really was trivial.

-  It's administrative code: it sends naggy reminder emails
   periodically. Why over-engineer it?


What an idiot I was.


Today, the ``{data}`` has been replaced with a complex table
instead of a summary. (Why? The user story evolved. And we needed
to replace the summary with details.)


The engineer was pretty sure they could use ``htmlify(data)`` or
``data.htmlify()`` to transform the data into an HTML structure
without seriously breaking the f-string nature of the app.
I **should have** commented "Don't build HTML that way, it's a bad
way to start" on the previous release.


The f-string solution turns rapidly into complexities layered on
complexities dusted over the top with sprinkles of NOPE.


This is a job for `Jinja2 <http://jinja.pocoo.org/>`__ or
`Mako <https://www.makotemplates.org/>`__ or something similar.


There's a step function change in the app's perceived
"complexity". Instead of a simple f-string, we now have to
populate a template. It goes from one line of code to more than
one (three seems typical.) And. The file-system loader for
templates seems more appropriate rather than hard-coding the
template in the body of the code. So there are now more files in
the app with the HTML templates in them.

However. The Jinja ``{{variable|round(2)}}`` was an immediate
victory. The use of ``{%for%}`` to build the HTML table was the
goal, and that simplification was worth the price of entry. Now
we're arguing over CSS nuances to get the columns to look "right."
Lessons learned.

Don't let the currently superficial trivial case slide past
without at least a warning. Make the suggestion that functions
like "get template" and "populate template" will be necessary even
for trivial f-string or string.Template processing.

HTML isn't a first-class part of anything. It's external
serialization.  Yes, it's for people, but it's only serialization.
Serialization has to be separated from the other aspects of the
data gathering, map-reduce summarization, and email distribution.

There's a pipeline of steps there and the final app should reflect
the complete separation of these concerns. Even if it is admin
overhead.





