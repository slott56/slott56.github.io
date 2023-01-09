The Users Just Want "Search" -- What's So Hard?
===============================================

:date: 2010-06-09 08:00
:tags: dimensional data,design
:slug: 2010_06_09-the_users_just_want_search_whats_so_hard
:category: Technologies
:status: published

Great article on "Search" from back in '08 in Forbes. "`Why Google Isn't
Enough <http://www.forbes.com/2008/09/19/cio-enterprise-search-tech-cio-cx_dw_0922search.html>`__",
by Dan Woods. He's talking about "Enterprise Search": why in-house
Google-style search is really hard and often unsatisfying.

Here's the cool quote.

    enterprise search systems also index and navigate information that
    may reside in databases, content management systems and other
    structured or semi-structured repositories. The contents may
    include not only text documents, but also spreadsheets,
    presentations, XML documents and so on. Even text documents may
    include some amount of structure, perhaps stored in an XML format.

Everyone thinks (hopes) that the mere presence of data is sufficient.
That fact that it's structured doesn't seem to influence their hopes.

The complication is simple -- and harsh. Many enterprise databases
are really bad. Really, really epically bad. So bad as to be
incomprehensible to a search engine.

**Explanations**

How many spreadsheets or reports "stand alone" as tidy, complete,
usable documents?

Almost none.

You create a budget for a project. It seems clear enough. Then the
project director wants to know if the labor costs are "burdened or
unburdened". So the column labeled "cost" has to be further
qualified. And "burdened" costs need to be detailed as to which --
exact -- overheads are included.

So a search engine might find your spreadsheet. If a person can't
interpret the data, neither can a search engine.

**Star Schema Nuance**

You can build a clever star schema from source data. But what you
find is that your sources have nuanced definitions. Each field isn't
directly mappable because it includes one or more subtleties.

Customer name and address. Seems simple enough. But... is that
mailing address or shipping address or billing address? Phone number.
Seems simple. Fax, Voice, Mobile, Land-line, corporate switch-board,
direct? Sigh. So much detail.

Of course the users "just want search".

Sadly, they've created data so subtle and nuanced that they can't
have search.





