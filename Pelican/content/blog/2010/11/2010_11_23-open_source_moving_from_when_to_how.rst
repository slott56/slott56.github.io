Open-Source, moving from "when" to "how"
========================================

:date: 2010-11-23 08:00
:tags: open source,#python
:slug: 2010_11_23-open_source_moving_from_when_to_how
:category: Technologies
:status: published

Interesting item in the November 1 eWeek: "`Open-Source Software in the
Enterprise <http://www.eweek.com/c/a/Linux-and-Open-Source/Open-Source-Software-in-the-Enterprise-177312/>`__".

Here's the key quote: "rather than asking if or when, organizations
are increasingly focusing on how".

Interestingly, the article then goes on to talk about licensing and
intellectual property management. I suppose those count, but they're
fringe issues, only relevant to lawyers.

Here's the two real issues:

#. Configuration Management

#. Quality Assurance

Many organizations do things so poorly that open source software is
unusable.

**Configuration Management**

Many organizations have non-existent or very primitive CM. They may
have some source code control and some change management. But the
configuration of the test and production technology stacks are
absolutely mystifying. No one can positively say what versions of
what products are in production or in test.

The funniest conversations center on the interconnectedness of open
source projects. You don't just take a library and plug it in. It's
not like neatly-stacked laundry, all washed and folded and ready to
be used. Open Source software is more like a dryer full of a tangled
collection of stuff that's tied in knots and suffers from major
static cling.

"How do we upgrade [X]"? You don't simply replace a component. You
create a new tech stack with the upgraded [X] and all of the stuff
that's knotted together with [X].

Changing from Python 2.5 to 2.6 changes any binary-compiled libraries
like PIL or MySQL_python, mod_wsgi, etc. These, in turn, may require
OS library upgrades.

A tech stack must be a hallowed thing. Someone must actively manage
change to be sure they're complete and consistent across the
enterprise.

**Quality Assurance**

Many organizations have very weak QA. They have an organization,
but it has no authority and developers are permitted to run
rough-shod over QA any time they use the magic words "the user's
demand it".

The truly funny conversations center on how the organization can
be sure that open source software works, or is free of hidden
malware. I've been asked how a client can vet an open source
package to be sure that it is malware free. As if the client's
Windows PC's are pristine works of art and the Apache POI project
is just a logic bomb.

The idea that you might do acceptance testing on open source software
always seems foreign to everyone involved. You test your in-house
software. Why not test the downloaded software? Indeed, why not test
commercial software for which you pay fees? Why does QA only seem to
apply to in-house software?

**Goals vs. Directions**

I think one other thing that's endlessly confusing is "Architecture
is a Direction not a Goal." I get the feeling that many organizations
strive for a crazy level of stability where everything is fixed,
unchanging and completely static (except for patches.)

The idea that we have systems on a new tech stack and systems on an
old tech stack seems to lead to angry words and stalled projects.
However, there's really no sensible alternative.

We have tech stack [X.1], [X.2] and [X.3] running in production. We
have [X.4] in final quality assurance testing. We have [X.5] in
development. The legacy servers running version 1 won't be upgraded,
they'll be retired. The legacy servers running version 2 may be
upgraded, depending on the value of the new features vs. the cost of
upgrading. The data in the version 3 servers will be migrated to the
version 4, and the old servers retired.

It can be complex. The architecture is a direction in which most (but
not all) servers are heading. The architecture changes, and some
servers catch up to the golden ideal and some servers never catch up.
Sometimes the upgrade doesn't create enough value.

These are "how" questions that are more important than studying the
various licensing provisions.



-----

One question to ask clients is for a road map of t...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-11-30 21:32:37.832000-05:00

One question to ask clients is for a road map of their environments.
Recently, at a client site, I was asked, what is that?





