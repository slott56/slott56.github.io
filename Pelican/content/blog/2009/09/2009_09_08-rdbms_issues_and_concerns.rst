RDBMS Issues and Concerns
=========================

:date: 2009-09-08 15:10
:tags: RDBMS,SQL,COBOL
:slug: 2009_09_08-rdbms_issues_and_concerns
:category: Technologies
:status: published

Check out this blog post:
http://cacm.acm.org/browse-by-subject/data-storage-and-retrieval/32212-the-end-of-a-dbms-era-might-be-upon-us/fulltext

The first issue is that the RDBMS code base in ancient. The second
issue is that we keep pushing the envelope on the RDBMS model;
examples include OLAP and RDF triple-stores.

Some folks want to say "reports of the death of the RDBMS are
premature."

Like COBOL, the relational model, and words like "DASD", some
technologies will be with us for decades after their useful life.

The decline of COBOL and the Relational Database will be protracted,
painful, inevitable and asymptotic with actual death. The old
one-size-fits-all COBOL is being replaced by many other languages.
Similarly, the one-size-fits-all RDBMS will be fragmented into more
specialized data stores. Further, legacy technology never completely
goes away.



-----

OLAP and RDF are not relational, so it&#39;s no su...
-----------------------------------------------------

Bill Karwin<noreply@blogger.com>

2009-09-08 16:19:48.382000-04:00

OLAP and RDF are not relational, so it's no surprise that implementing
them in an RDBMS is painful. It'd be like designing an OO application in
a non-OO language like C. Is that C's fault? Does that mean C doesn't
still do some things well?

The debate about the death of RDBMS is based on a zero-sum game view of
technology. This view is needless. Instead, let's use different tools
where they give the most benefit.


I&#39;m not sure the relational model can be consi...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-09-09 08:25:06.535000-04:00

I'm not sure the relational model can be considered "legacy technology"
like COBOL et al. Sure, most relational databases are pretty long in the
teeth (and SQL is a huge warty mess), but there's something pretty
timeless about mathematical logic and set theory. I think the relational
model just needs a facelift, personally.





