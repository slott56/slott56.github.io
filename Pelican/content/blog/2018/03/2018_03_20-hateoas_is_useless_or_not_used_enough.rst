HATEOAS is useless? Or not used enough?
=======================================

:date: 2018-03-20 08:00
:tags: REST,API Design
:slug: 2018_03_20-hateoas_is_useless_or_not_used_enough
:category: Technologies
:status: published

See `Why HATEOAS is useless and what that means for
REST <https://medium.com/@andreasreiser94/why-hateoas-is-useless-and-what-that-means-for-rest-a65194471bc8>`__.


The article provides a background leading up to these observations:
   
-  There are very few good tools to create a REST API using this style

-  There are no clients widely used to consume these types of APIs


The "useless" in the title is more like "not used enough."


There's a multi-part conclusion that may be more helpful if it's
fleshed out further. For now, however, it appears that the big
problems center around:


-   You still need to write Open Api Specifications (OAS, f/k/a
    Swagger). I don't think this is bad. The blog post makes it sound
    like a problem. I think it's essential.

-   You need to put versioning somewhere. The path is less than idea.
    I'm big on the Accept header containing application-specific MIME
    types. For example,
    application/vnd.com.your-name-here.app.json+v1. This doesn't
    strike me as a problem, either.

-   The whole approach is "closer to RPC than some REST lovers like to
    admit." I think this point revolves around the way JSON-RPC or
    SOAP involves some overheads above basic HTTP that are unhelpful.
    I don't think the "closer to RPC" follows logically from the lack
    of tooling for HATEOS, but it certainly could be true that a
    badly-done API might involve too many of the wrong kinds of
    overheads.


I think there's a hidden strawman here. The "automatic discovery"
idea. I don't think this idea makes a lick of sense. Some people
think it's implied (or required) by REST, and any failure to
provide for fully-automated semantically rich discovery of an API
is some kind of failure.


I don't think full semantic discovery is possible or even desirable.


-   It's not possible because of the problem of assigning names and
    meanings to resources and verbs in an end-point. The necessary
    details can only be exposed with a semantically complete ontology
    and complex SPARQL queries into the ontology to find resources and
    end-points.

-   It's not desirable because we replace a human-focused OAS with a
    complete ontology that has to be rigorously defined, and tested to
    be sure that all kinds of automated discovery algorithms can
    understand the provided details. And none of this addresses the
    actual application, it's all rich, detailed meta-description of
    the application.


I don't see why we're trying to replace people. API discovery is
actually kind of hard. The resources, their relationships, and the
verbs for getting or updating those resources involves an
essentially difficult knowledge capture and dissemination
problem.





