Today's Milestone: Refactoring and Django Migrations
====================================================

:date: 2015-10-06 08:00
:tags: Django,API Design
:slug: 2015_10_06-todays_milestone_refactoring_and_django_migrations
:category: Technologies
:status: published


Once upon a time, when today's old folks were young, we'd debate the
two project strategies: Hard Part Do Later (HPDL) vs. Hard Part First
(HPF).

The HPDL folks argued that you could pick away at the hard part until
-- eventually -- it wasn't hard any more. This doesn't often work out
well in practice, but a lot of people like it. Sometimes the attempt
to avoid the hard part makes it harder.

The HPF folks, on the other hand, recognized that solving the hard
problem correctly, may make the easy problems even easier. It may not,
but either way, the hard part was done.

The debate would shift to what -- exactly -- constituted the hard
part. Generally, what one person finds hard, another person has
already done several times before. It's the part that no one has done
before that eventually surfaces as being truly hard.

Young kids today (get off my lawn!) often try to make the case that an
Agile approach finesses the "hard part" problem. We define a Minimally
Viable Product (MVP) and we (magically) don't have to worry about
doing the hard part first or last.

They're wrong.

If the MVP happens to include the hard part, we're back a HPF. If the
MVP tries to avoid the hard part, we're looking at HPDL.

The Novelty Factor
------------------


Agile methods don't change things. We still have to **Confront the
Novelty** (CTN™). Either it's new technology or it's a new problem
domain or a new solution to an existing problem domain. Something must
be novel, or we wouldn't be writing software, we'd be downloading it.

I'm a HPF person. If you set the hard part aside to do later, all the
things you do instead become constraints, limiting your choices for
solving the hard part that comes later. In some rare cases, you can
decompose the hard part and solve it in pieces. The decomposition is
simply **Hard Part First through Decomposition** (HPFtD™) followed by
**Prioritize the Pieces** (PtP™) and another round of Hard Part First.

Today, we're at a big milestone in the HPF journey.

The application's data model is simple. However.

The application has a complex pipeline of processing to get from
source data to the useful data model.

A strict (and dumb) MVP approach would skip building the complex
pipeline and assume that it was magically implemented somehow.

A slightly smarter MVP approach uses some kind of technical spike
solution to handle the complex pipeline. We do that manually until we
get past MVP and decide to implement the pipeline in something more
final and complete.

My HPF strategy tackles the complex pipeline because we have to build
it anyway and it's hard. We don't have to build **all** of it. Just
enough to lay out the happy path.

The milestone?

It's time to totally refactor because -- even doing the hard part
first -- we have the wrong things in the wrong places. Django
application boundaries generally follow the "resources". It's a lot
like designing a RESTful API. Define the resources, cluster them
together in some kind of ontology that provides a meaningful
hierarchy.

Until -- of course -- you get past the problem domain novelty and
realize that some portion of the hierarchy is going to become really
lopsided. It needs to be restructured so we have a flat group of
applications.

Wait. What?

Flatten?

Yes.

When we have a Django application model that's got eleventy-kabillion
classes, it's too big. Think the magic number 7±2: there's a limit to
our ability to grasp a complex model.

Originally, we thought we'd have apps "A", "B", and "C". However. "A"
turned out to be more complex than it seemed when we initially
partitioned the apps. Based on the way the classes are named and
clustered in the model file, it's clear that we have an internal
structure is struggling to emerge. There are too many comments and
high-level organizational hints in the docstrings.

It looks like this might be the model that's emerging:

-   Former A

    -  A1

    -  Conceptual A2

       -  A2a
       -  A2b

    -  A3

-   B

-   C


This means that there will be classes in A3 that depend on separate
apps A2a and A2b. Further, A2 is really just a concept that unifies
the design; it doesn't need to be implemented as a proper app. Both
A2a and A2b depend on A1. A3 depends on A2a, A2b, and A1.


Ugh. Refactoring. And the associated migrations.

Django allows us to have nested apps. But. Do we really want to go
there? Is a nested collection of packages really all that helpful?

Or.

Would it be better to flatten the whole thing, and simply annotate
the dependencies among apps?

The *Zen Of Python* suggests that Flat is Better than Nested.

The hidden benefit of Flat is that the `Liskov Substitution
Principle <https://en.wikipedia.org/wiki/Liskov_substitution_principle>`__
is actually a bit easier to exploit. Yes, we have a tangled web of
dependencies, but we're slightly less constrained when all of the
Django apps are peers. Yes, many things will depend on the A1 app,
but that will be less of a problem than the current pile of classes
is.

The important part here is to start again. This means I need to
discard the spike database and discard the history of migrations to
date. I always hate disrupting my development databases, since it has
test cases I know and remember.

That's the disruptive milestone for me: discarding the old database
and starting again.





