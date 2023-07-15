Code Base Fragmentation
=======================

:date: 2010-10-21 08:00
:tags: triggers,database design
:slug: 2010_10_21-code_base_fragmentation
:category: Technologies
:status: published

Here's what I love -- an argument that can only add cost and complexity
to a project.

It sounds like this to me: "We need to fragment the code base into
several different languages. Some of the application programming
simply **must** be written in a language that's poorly-understood,
with tools that are not widely available, and supported by a select
few individuals that have exclusive access to this code. We haven't
benchmarked the technical benefit."

Further, we'll create complex organizational roadblocks in every
single project around this obscure, specialized, hard-to-support
language.

Perhaps I'm wrong, but database triggers always seem to create more
problems than they solve.

They Totally Solve a Problem
----------------------------

The most common argument boils down to application-specific
`cross-cutting
concerns <http://en.wikipedia.org/wiki/Aspect-oriented_programming>`__.
The claim is that these concerns (logging, validation, data model
integrity, whatever) can only be solved with triggers. For some
reason, though, these cross-cutting concerns can't be solved through
ordinary software design. I'm not sure why triggers are the only
solution when simple OO design would be far simpler.

Some folks like to adopt the "multiple application programming
languages" argument. That is, that ordinary OO design won't work
because the code would have to be repeated in each language. This is
largely bunk. It's mostly folks scent-marking territory and refusing
to cooperate.

Step 1. Write a library and share it. It's hard to find a language
that can't be used to write a sharable library. It's easy to find an
organization where the Visual C# programmers are not on speaking
terms with the Java programmers and the isolated Python folks are
pariahs. This isn't technology. Any one of the languages can create
the necessary shared library. A modicum of *cooperation* would be
simpler than creating triggers.

Step 2. Get over it. "Duplicated" business logic is rampant in most
organizations. Now that you know about, you can manage it. You don't
need to add Yet Another Language to the problem. Just *cooperate* to
propagate the changes.

They're Totally Essential To The Database
-----------------------------------------

The silly argument is that some business rules are "closer to" or
"essential to" the database. The reason I can call this silly is
because when the data is converted to another database (or extracted
to the data warehouse) the triggers aren't relevant or even needed.
If the triggers aren't part of "interpreting" or "using" the data,
they aren't essential. They're just convenient.

The data really **is** separate from the processing. And the data is
far, far more valuable than the processing. The processing really
**is** mostly application-specific. Any processing that isn't
specific to the application really **is** a cross-cutting concern
(see above). There is no "essential" processing that's magically part
of the data.

What If...
----------

Life is simpler if all application programming is done in application
programming languages. And all triggers are just methods in classes.
And everyone just uses the class library they're supposed to use.

"But what if someone doesn't use the proper library? A trigger would
magically prevent problems."

If someone refuses to use the application libraries, they need career
coaching. As in "find another job where breaking the rules is
tolerated."



-----

Thanks, Robert.
---------------

Unknown<noreply@blogger.com>

2010-10-25 23:54:32.457000-04:00

Thanks, Robert.


Unrelated, but your book Building Skills in Python...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-10-25 04:36:30.479000-04:00

Unrelated, but your book Building Skills in Python doesn't use Python 3.
Are you going to update it for Python 3 anytime soon? I'd love to learn
Python and I like your approach. I especially like that you are going to
be using 'casino games' problems. IMO, they provide a good mix of
challenge without being too complex.


All I can say is that using triggers is equivalent...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-21 18:35:01.429000-04:00

All I can say is that using triggers is equivalent to relying on side
effects.

If side effects don't turn you off, how about the mutating table issue ?
Would you take medicine that had side effects and caused mutations ?
You say that you have a strong physical constitution and can handle the
medicine. Well, can you mental constitution handle it ?

In Oracle, the manual explicitly states that it does not gurantee the
execution order of certain triggers. So, your program now becomes
non-deterministic. Yah, I know, deterministic software is for wimps.
Also, haven forbid if you ask for documentation about the triggers. If
you really want to blow their mind, generate some UML state charts for
the triggers.

Oh, and before I forget, lets not forget about trying to test and debug
w/ all these triggers firing all over the place. Yah, I know, you like a
good challenge.

Well, enough ranting. In my career, each and everytime that I have had
serious issues at a client site, its always been because of triggers.
One last thing, if you are an advanced Oracle user, you can take a walk
on the wild side and use "instead of triggers".


Try posting the &quot;unrelated&quot; Python post ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-25 21:37:14.514000-04:00

Try posting the "unrelated" Python post in the following Google group
http://groups.google.com/group/building-skills-books?hl=en
Steve uses the above Google group to support his books.


For an interesting discussing on this trigger stuf...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-21 18:39:24.577000-04:00

For an interesting discussing on this trigger stuff, check out "Database
Triggers - Good, Bad, Ugly?" by "Joel on Software"
http://discuss.fogcreek.com/joelonsoftware2/default.asp?cmd=show&ixPost=67962





