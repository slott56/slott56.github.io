Three Unsolvable Problems in Computing
======================================

:date: 2017-09-19 08:07
:tags: #python,flask,architecture,microservices
:slug: 2017_09_19-three_unsolvable_problems_in_computing
:category: Technologies
:status: published


The three unsolvable problems in computing:

-  Naming
-  Distributed Cache Coherence
-  Off-By-One Errors




Let's talk about naming.

The project team decided to call the server component "FlaskAPI".

Seriously.

It serves information about two kinds of resources: images and running
instances of images. (Yes, it's a kind of kubernetes/dockyard lite
that gives us a lot of control over servers with multiple containers.)

The feature set is growing rapidly. The legacy name needs to change.
As we move forward, we'll be adding more microservices. Unless they
have a name that reflects the resource(s) being managed, this is
rapidly going to become utterly untenable.

Indeed, the name chosen may already be untenable: the name doesn't
reflect the resource, it reflects an implementation choice that is
true of all the microservices. (It's a wonder they didn't call it
"PythonFlaskAPI".)

See https://blogs.mulesoft.com/dev/api-dev/best-practices-for-building-apis/
for some general guidelines on API design.

These guidelines don't seem to address naming in any depth. There are
a few blog posts on this, but there seem to be two extremes.

-  Details/details/details. Long paths:
   class-of-service/service/version-of-service/resources/resource-id
   kind of paths. Yes. I get it. The initial portion of the path can
   then route the request for us. But it requires a front-end request
   broker or orchestration layer to farm out the work. I'm not enamored
   of the version information in the path because the path isn't an
   ontology of the entities; it becomes something more and reveals
   implementation details. The orchestration is pushed down the client.
   Yuck.

-  Resources/resource. I kind of like this. The versioning information
   can be in the Content-Type header:
   application/json+vnd.yournamehere.v\ x\ +json.  I like this because
   the paths don't change. Only the v\ *x* in the header. But how does
   the client select the latest version of the service if it doesn't go
   in the path? Ugh. Problem not solved.


I'm not a fan of an orchestration layer. But there's
this: https://medium.com/capital-one-developers/microservices-when-to-react-vs-orchestrate-c6b18308a14c
tl;dr: Orchestration is essentially unavoidable.


There are articles on
choreography. https://specify.io/concepts/microservices the idea is
that an event queue is used to choreograph among microservices. This
flips orchestration around a little bit by having a more peer-to-peer
relationship among services. It replaces complex orchestration with a
message queue, reducing the complexity of the code.


On the one hand, orchestration is simple. The orchestrator uses the
resource class and content-type version information to find the right
server. It's not a lot of code.


On the other hand, orchestration is overhead. Each request passes
through two services to get something done. The pace of change is
slow. HATEOAS suggests that a "configuration" or "service discovery"
service (with etags to support caching and warning of out-of-date
cache) might be a better choice. Clients can make a configuration
request, and if cache is still valid, it can then make the real
working request.


The client-side overhead is a burden that is -- perhaps -- a bad
idea. It has the potential to make  the clients very complex. It can
work if we're going to provide a sophisticated client library. It
can't work if we're expecting developers to make RESTful API requests
to get useful results. Who wants to make the extra meta-request all
the time?





