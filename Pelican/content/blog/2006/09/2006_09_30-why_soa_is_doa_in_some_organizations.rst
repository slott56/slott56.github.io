Why SOA is DOA in some organizations
====================================

:date: 2006-09-30 03:09
:tags: architecture,design,complexity
:slug: 2006_09_30-why_soa_is_doa_in_some_organizations
:category: Architecture & Design
:status: published





"Here are the exact words from the client when I
suggested using the "official calendar": I’m aware of other systems having
tables for Holidays but I don’t know that we can piggy back off any of
them (not aware they are publicly available). Besides, I’d rather we have
better control over our own destiny than relying on someone else. As far as
Month End is concerned, we have unique needs that only system x might operate in
a similar fashion but that too is user
entered"



This came up in a discussion
of how to find the "first business day" of a month.  Clearly, using the RDBMS
calendar functions to find the first day of the month is completely wrong, since
it doesn't account for legal holidays in any form.    So, the approach suggested
was to add tables and programming logic to -- essentially -- approximate the
calendar information already available in the General
Ledger.



The very idea of reuse was a
non-starter.  This response characterizes the impassible barrier to SOA:
"I’d rather we have better control over our own destiny than relying on
someone else".



Worse still is the idea
that the "user-entered" business calendar (the one actually used by the
business) isn't appropriate, and an algorithmic approximation -- in spite of the
inevitable errors -- is somehow better.  It's almost as if the official business
calendar is not trustworthy because it is tweaked by accountants to get the
number of business days and holidays to balance in each
period.



The simple idea of reuse is
lost in the politics of who controls who's fate.  Does anyone else find this
behavior fringing on the criminal?








