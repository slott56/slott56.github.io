A smoothly operating, well-oiled engine for failure
===================================================

:date: 2011-10-11 08:00
:tags: complexity,software process improvement
:slug: 2011_10_11-a_smoothly_operating_well_oiled_engine_for_failure
:category: Technologies
:status: published

It occurs to me that much of "Big IT" creates a well-oiled organization
that makes broken software seem acceptable. The breakage is wrapped in
layers of finely-tuned process.
Consider a typical Enterprise Application.  There's a help desk, ticket
tracking, a user support organization that does "ad-hoc" processing, and
a development organization to handle bug fixes and enhancement
requests.  All those people doing all that work.
Why?
If people need all that support, then the application is -- from a
simplistic view -- broken.
The organization, however, has coped with the broken application by
wrapping it in layers of people, process, tools, technology, management
and funding.  The end users have a problem, they call the help desk, and
the machine kicks in to resolve their problem.
It is a given -- a going-in assumption -- a normal, standard expectation
that any enterprise software is so broken that a huge organization will
be essential for pressing forward.  It is expected that good software
cannot be built.
We're asked to help a client create a sophisticated plan for the New
Enterprise App support organization.  Planning this organization feels
like planning for various kinds of known, predicted, expected failures.
Failure is the expectation.  Broken is the standard operating mode.
Consider a typical non-Enterprise Application.  Let's say, the GNU C
compiler.  Or Python.  Or Linux.  An almost entirely volunteer
organization, no help desk, no trouble tickets, no elaborate support
organization plan.  Yet.  These products actually work flawlessly.
They're not wrapped in a giant organization.
Why is the bar for acceptability so low for "Enterprise" applications?
Why is this tolerated?



-----

It is because of two substantial reasons: 1. it is...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-10-21 21:59:09.965000-04:00

It is because of two substantial reasons: 1. it is cheaper to ship and
maintain at 90% bug free than it is to ship at 100% bug free -- in a
large enough project, as the number of bugs approaches 0, the cost per
bug fix climbs exponentially. 2. There is no 100% intuitive UI and what
might seem intuitive and well designed through early tests can fail in
the real world.


I wouldn&#39;t call it broken but alive.

Can real...
-----------------------------------------------------

vemv<noreply@blogger.com>

2011-10-11 10:16:42.513000-04:00

I wouldn't call it broken but alive.
Can really software be perfectly designed before implementation?
Feature requests and bug reports seem the most normal thing to me -
requirements constantly change.
Let me blindly bet that most massive open source projects use ticketing
to some extent. And that not all enterprises enjoy using giantic systems
- what blocks them from using just a handful of tools instead?


First of all, I am sorry you are working on Enterp...
-----------------------------------------------------

AConsul<noreply@blogger.com>

2011-10-11 11:18:56.533000-04:00

First of all, I am sorry you are working on Enterprise software.
Secondly, extremely bad comparison.
You might as well be complaining about how teaching remedial english at
an urban public school is nothing like (but should be like! ) a
graduate-level English literature seminar.
Enterprise apps are by giant organizations for giant organizations,
filled with people with low levels of technical interest and ability.
The ecosystem for developers using GCC, Python, or Sys Admins using
Linux, is composed of a very different set of people working on a very
different set of goals from Enterprise/Business.
For GNU C you have a self-selecting set of technically competent people
who don't balk, experiment, persist, and actually read the
documentation, specifications, etc., as well as not balk at the first
compiler error. Do you honestly think you can compare the average GNU C
compiler user to the average Enterprise User? Do you really think the
average Enterprise user would spend more than 5 minutes looking at GCC
documentation before running away screaming?
Enterprise IT is another country, another culture. Consider this like a
trip to a foreign land. Learn the local customs, expectations. You may
not like it there but that's what it will take you to survive.





