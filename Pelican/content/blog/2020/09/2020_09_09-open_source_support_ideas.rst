Open Source Support Ideas
=========================

:date: 2020-09-09 19:02
:tags: open source,conda
:slug: 2020_09_09-open_source_support_ideas
:category: Technologies
:status: published

"... [I] am thinking of building an in house conda forge, or buying a
solution, or paying someone to set something up."

The build v. Buy decision. This is always hard. Really hard.

We used to ask "What's your business? Is it building software or making
widgets?"

And (for some) the business is making widgets.

This is short-sighted.

But. A lot of folks in senior positions were given this as a model back
in the olden days. So, you need to address the "how much non-widget
stuff are we going to take on?" question.

The "Our Business is Widgets" is short-sighted because it fails to
recognize where the money is made. It's the ancillary things \*around\*
the widgets. Things only software can do. Customer satisfaction.
Supply-chain management.

So. Business development == Software development. They're inextricably
bound.

With that background, lets' look at what you want to do.

Open Source software is not actually "free" in any sense. Someone has to
support it. If you embrace open source, then, you have to support it
in-house. Somehow. And that in-house work isn't small.

The in-house open-source support comes in degrees, starting with a
distant "throw money at a maintainer" kind of action. You know. Support
NumFocus and Anaconda and hope it trickles down appropriately (it
sometimes does) to the real maintainers.

The next step is to build the tooling (and expertise) in-house. Conda
forge (or maybe JFrog or something else) and have someone on staff who
can grow to really understand how it fits together. They may not be up
to external contributions, but they can do the installs, make sure
things are running, handle updates, manage certificates, rotate keys,
all the things that lead to smooth experience for users.

The top step is to hire one of the principles and let them do their open
source thing but give them office space and a salary.

I'm big on the middle step. Do it in-house. It's \*not\* your core
business (in a very narrow, legal and finance sense) but it \*is\* the
backbone fo the information-centric value-add where the real money is
made.

Folks in management (usually accouting) get frustrated with this
approach. It seems like it should take a month or two and you're up and
running. (The GAAP requires we plan like this. Make up a random date.
Make up a random budget.)

But. Then. 13 weeks into the 8-week project, you still don't have a
reliable, high-performance server.  Accounting gets grumpy because the
plan you have them months ago turns out to have been riddled with
invalid assumptions and half-truths. (They get revenge by cancelling the
project at the worst moment to be sure it's a huge loss in everyone's
eyes.)

I think the mistake is failing to enumerate the lessons learned. A lot
will be learned. A real lot. And some of it is small, but it still takes
all day to figure it out. Other things are big and take failed roll-outs
and screwed up backup-restore activities. It's essential to make a
strong parallel between open source and open learning.

You don't know everything. (Indeed, you can't, much to the consternation
of the accountants.) But. You are learning at a steady rate. The money
is creating significant value.

And after 26 weeks, when things \*really\* seem to be working, there
needs to be a very splashy list of "things we can do now that we
couldn't do before."  A demo of starting a new project. \`conda create
demo python=3.8.6 --file demo_env.yml\` and watch it run, baby. A little
dask. Maybe analyze some taxicab data.





