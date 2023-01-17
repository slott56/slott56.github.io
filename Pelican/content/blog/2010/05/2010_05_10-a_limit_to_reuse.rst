A Limit to Reuse
================

:date: 2010-05-10 08:00
:tags: #python,dimensional data,design,refactoring
:slug: 2010_05_10-a_limit_to_reuse
:category: Technologies
:status: published

We do a lot of bulk loads. A lot.

So many that we have some standard ETL-like modules for generic
"Validate", "Load", "Load_Dimension", "Load_Fact" and those sorts of
obvious patterns.

Mostly our business processes amount to a "dimensional conformance
and fact load", followed by extracts, followed by a different
"dimensional conformance and fact load". We have multiple fact
tables, with some common dimensions. In short, we're building up
collections of facts about entities in one of the dimensions. [And
no, we're not building up data individual consumers. Really.]

Until, of course, someone has a brain-fart.

Overall Application Design
--------------------------

An overall load application is a simple loop. For each row in the
source document, conform the various dimensions, and then load the
fact. Clearly, we have a bunch of dimension conformance objects and a
fact loading object. Each object gets a crack at the input row and
enriches it with some little tidbit (like a foreign key).

This leads us to pretty generic "Builder" and "Dimension Builder" and
"Fact Builder" class hierarchy. Very tidy.

Each new kind of feed (usually because no two customers are alike) is
really just a small module with builders that are specific to that
customer. And the builders devolve to two methods

-   Transform a row to a new-entity dict, suitable for a Django model.
    Really, just a simple ``dict( field=source['Column'], field=source['Column'], ... )`` block of code.

-   Transform a row to a dimension conformance query, suitable for a
    Django filter. Again, a simple ``dict( some_key__iexact=source['Column'] )``.

The nice thing is that the builders abstract out all the messy
details. Except.

Hard-to-Conform Data
--------------------

We're now getting data that's not -- narrowly -- based on things our
customers tell us. We're getting data that might be useful to our
customer. Essentially, we're processing they're data as well as
offering additional data.

Cool, right?

But... We lack the obvious customer-supplied keys required to do
dimensional conformance. Instead, we have to resort to a multi-step
matching dance.

Limiting Factors
----------------

The multi-step matching dance pushed the "Builder" design one step
beyond. It moved from tidy to obscure. There's a line that seems to
be drawn around "too much" back-and-forth between framework code and
our Builders.

Something as bone-simple as a bulk loader has two candidate design
patterns.

-   Standard loader app with plug-in features for mappings. This is
    what I chose. The mappings have been (until now) simple. The app
    is standard. Plug a short list of classes into the standard
    framework. Done.

-   Standard load support libraries that make a simple load app look
    simple. In this case, each load app really is a top-level app, not
    simply some classes that plug into an existing, standardized app.
    Write the standard outer loop? Please.

What's wrong with plug-ins?

It's hard to say. But it seems that a plug-in passes some limit to OO
understandability. It seems that if we refactor too much up to the
superclass then our plug-ins become hard to understand because they
lose any "conceptual unity".

The limiting factor seems to be a "conceptually complete" operation
or step. Not all code is so costly that a simple repeat is an
accident waiting to happen.

Hints from Map-Reduce
---------------------

It seems like there are two conceptual units. The loop. The function
applied within the loop. And we should write all of the loop or all
of the mapped function.

If we're writing the mapped function, we might call other functions,
but it feels like we should limit how much other functions call back
to the customer-specific piece.

If we're writing the overall loop -- because some bit of logic is
really convoluted -- we should simply write the loop without shame.
It's a **for** statement. It's not obscure or confusing. And there's
no reason to try and factor the **for** statement into the superclass
just because we can.



-----

For shame! Sorry, I just couldn't resist. :)
-------------------------------------------------

Jerry Seutter<noreply@blogger.com>

2010-05-10 14:58:39.093000-04:00

For shame!
Sorry, I just couldn't resist. :)


Code Reuse -- A Myth? by Danny Kalev Au...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-08-22 06:08:46.367000-04:00

Check out
Code Reuse -- A Myth? by Danny Kalev Aug 13, 2010
Code Reuse -- A Myth? Part II by Danny Kalev Aug 13, 2010
http://www.informit.com/guides/content.aspx?g=cplusplus&seqNum=499
http://www.informit.com/guides/content.aspx?g=cplusplus&seqNum=500&ns=19521&WT.mc_id=2010-08-22_NL_InformITContent





