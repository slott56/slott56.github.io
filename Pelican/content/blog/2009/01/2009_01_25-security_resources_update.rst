Security Resources [Update]
===========================

:date: 2009-01-25 01:52
:tags: architecture,design,data structure,algorithm
:slug: 2009_01_25-security_resources_update
:category: Architecture & Design
:status: published







Years ago, I was working with a client who was implementing their first web site.



Well, actually, it wasn't their first.  It was their third.  But their first two were haphazard "we hope this works" kind of web sites.  They relied on third-party security and were pretty sure they were using it correctly.



I was involved with their first externally-facing application.   We were going through a "risk-exposure" analysis.



One of their people was so uncomfortable that they balked at the very idea of a fixed list of risks.



"We don't know what we don't know," they pronounced.  Their claim was that security considerations included an unbounded list of vulnerabilities.



:strong:`Vulnerability Lists` 



I make regular use of the `OWASP <http://www.owasp.org/>`_  top 10 vulnerabilities and other resources.



Today I learned about the SANS Institute's `top 25 coding errors <http://www.sans.org/top25errors/>`_ .  They provide three categories of errors.

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

And, there's the `19 Deadly Sins of Software Security <http://blogs.msdn.com/michael_howard/archive/2005/07/11/437875.aspx>`_  list.  [Thanks!]

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

This is very, very handy stuff.  There's nothing better than a concrete checklist of errors to structure architecture, design, and coding.

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

:strong:`What We Don't Know` 

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

Yes, there are unknown, unlisted, yet-unexploited vulnerabilities.  Until those are discovered, we really :strong:`do`  know what to do.

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

1.  Don't waste a lot of time on a complex risk/cost analysis.  These are complex -- often subjective -- and very expensive.  A short list of exposure and cost is all you need.  And often, the short list includes something like "`HIPAA PHI <http://www.noao.edu/cas/hr/faq/faq_hipaa.html#six>`_ " and that's all you need to know.

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

2.  Use a straight-forward checklist of vulnerabilities built from these lists.  Numerous items appear on all three lists, that's the bare minimum of security considerations.  The union of all three lists isn't that big or complex.  Your framework or language may not even have some of these vulnerabilities.

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_

It's probably cheaper to just plug these known holes than it is to decide which -- if any -- holes have "enough" expected value of a loss.

 -   `Category: Insecure Interaction Between Components (9 errors) <http://www.sans.org/top25errors/#cat1>`_  -   `Category: Risky Resource Management (9 errors) <http://www.sans.org/top25errors/#cat2>`_  -   `Category: Porous Defenses (7 errors) <http://www.sans.org/top25errors/#cat3>`_





