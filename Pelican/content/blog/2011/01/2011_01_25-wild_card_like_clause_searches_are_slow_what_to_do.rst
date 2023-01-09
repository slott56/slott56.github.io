Wild-Card (LIKE-clause) searches are slow.  What to do?
=======================================================

:date: 2011-01-25 08:00
:tags: design,SQL,architecture
:slug: 2011_01_25-wild_card_like_clause_searches_are_slow_what_to_do
:category: Technologies
:status: published

Patient: "Doctor, doctor, it hurts when I do this."

Doctor: "Then don't do that."

I got an email with hundreds of words of content. This part made
sense: "...doing wild card searches using Oracle's database engine
and are wondering why is it so slow and how do they make it go
faster."

The rest made very little sense at all. The programmer in question
immediately dove into nuances of indexing, Oracle pattern matching,
Oracle Text Query and other technical questions. The entire focus was
on the technical ins-and-outs.

Not a single word on **why** wildcards were even being used in the
first place. Wildcards appear to solve a business problem; the
business problem was never mentioned.

**Use Case for Wildcards**

After some back-and-forth, the use case emerged. We'll address it
below. Essentially, the invoices have names (really) that have "rich
semantic content". These invoice names have the form "{customer}
{time period} {offering}".

Apparently, the use case is "slice-and-dice" queries. All invoices
for a given customer; all invoices in a given time period; all
invoices for a given offering; various combinations.

Really. Rather than provide discrete dimensions and use a star
schema, they've (a) combined all attributes into a single free-text
field and (b) used wild-card searches and now (c) want to complain
about it.

We'll return to this use case below.

**Basic Rules**

Here's are the two rules.

    **Wild Cards Are The Last Resort For Human-Friendly Search.**

    **Outside Human-Friendly Search, Wild Cards Are Useless.**

Let's look at rule 1: **Wild Cards Are The Last Resort For Human-Friendly Search**.

When a person enters a search string on a web page, we have two
choices.

#.  Trust them to enter the exact field as it appears in the database

#.  Presume that people are fallible and cannot be trusted to enter
    the exact field.

In case #1 (exact match) we might be using an account number,
shipping number, an invoice number or some kind of surrogate key.
In this case, we do simple equality checks. If the user can't get
it right, bummer. In many cases, this is appropriate to prevent
snooping.

In case #2 (partial match), we're forced to use a some kind of SQL
LIKE clause for the human-friendly search. We have several
implementation choices, some in the database, some out of the
database. Some in-the-database solutions benefit from clever
indexing. Many in-the-database solutions are pretty slow.

Yes, an out-of-the-database solution may actually be faster. Until we
benchmark, we can't know. There's no trivial rule that says the
database always does search faster. For real speed, we may have to
resort to a hybrid solution.

**Search Optimization**

We might create a small RESTful server for our searchable text
fields. This is a cache; the server should handle CRUD rules to
assure cache coherence. This search server can uses a Regular
Expression engine, or perhaps compute `Levenshtein
distances <http://en.wikipedia.org/wiki/Levenshtein_distance>`__ or
whatever makes sense to optimize user-oriented search.

If we're searching in larger chunks of text, we might want to use a
commercial full-text search.

What's essential about this plan is that we're looking at
*application-specific optimizations*. People need flexibility for
*specific* reasons. It's important to look at the *actual* use cases
where a person cannot make an exact match lookup. What problems do
they have?

An application may have to deal with customer names. These are often
difficult to spell consistently. (Is it "AT&T" or "ATT"?) For this
kind of thing Levenshtein Distance might make more sense than
wild-card searches.

An application may have to deal with time periods. "2010", "2Q 2010",
"July 2010", etc. This is best handled by decomposing time periods
into discrete fields and doing appropriate exact match on the
specific, relevant fields. The issue is that there are a lot of
formulations and some text parsing can be better than a form with a
million drop-downs.

An application may have to deal with oddly-named offerings. Marketing
calls it one thing. Sales folks call it another. The customer's
invoice may call it a third, and the help desk may not use any of
those phrases. This may benefit from wild-cards.

Note that we're looking at the *business* issues. Not the technology
issues.

**Design Errors**

The proper use for LIKE is only to optimize the human-friendly
search. Nothing else. Which brings us to rule 2, **Outside Human-Friendly Search, Wild Cards are Useless**.

Outside human search, every wild-card in a SQL statement indicates a
serious database design error. Serious? Error? Yes.

LIKE clauses outside human search indicate a failure to create a
design in first normal form (1NF). A field which is used in a LIKE
clause has multiple parts, and should have been decomposed into
pieces.

Decomposing a multi-part attribute isn't always trivial. There are
two cases.

#.  Simple, regular format or punctuation. For example, SSN, US Phones
    or ZIP codes: 123-45-6789 or (123)555-1234 or 12345-1234.

#.  Complex, irregular format or punctuation. In this case, we have
    disjoint subtypes in a single table. Most manufacturing part
    numbers suffer from this.

In case 1, we have two choices: fully decompose or denormalize. In
case 2, we can only denormalize because the rules are irregular.

The decomposition solution does not have to lead to a hideous user
interface. We can have a web page with a single text field for phone
numbers. We can parse that string and decompose the phone number into
area code, exchange and number for purposes of database storage. We
don't have to thoughtlessly force the users to decompose a field that
they don't see as being in three parts.

The denormalization solution means that we have to do some
calculation when we accept the input value. We save the full field,
plus we extract the various sub-fields based on whatever hellish,
complex rules we're faced with.

**Implementation Choices**

Whenever we have a single text field with "rich semantic content"
(i.e., combines multiple disjoint attributes like customer, time
period and offering) what we're seeing is a clever way to push
database design onto the users. The expectation is that IT will (1)
understand the use cases, (2) provide a proper design and (3)
optimize performance around that design.

A big text field and wild-card search (and the attendant email
traffic) indicates an explicit unwillingness to discuss the real use
cases, unwillingness to do design, and a lame hope that somehow
wild-card searches can magically be made faster through magical
indexing or other super-natural techniques.

The "rich semantic content" field can be decomposed one of two ways.

-   In the GUI. Add drop-downs so users pick the customer, time
    period, and product offering information.

-   In the Application. Parse the big text field into smaller text
    fields that don't require wild-card search.

There isn't any magic. If wild-card searches are too slow, they have
to be replaced.

**Benefits?**

The benefit of decomposing (or denormalizing) a complex field is that
we can eliminate LIKE processing and wild-cards. Instead of
"LONG_TEXT_FIELD LIKE '%2Q 2010%'", we can do "DATE.QUARTER=2 AND
DATE.YEAR=2010".

All the technical folderol related to indexing and full-text search
and database regular expression engines goes right out the window.

The cost is that we have to "wrap" the INSERT and UPDATE processing
in a class definition that does the denormalization. That's what a
data model layer is for: these kinds of business rules. The
insert/update cost, BTW, will be microscopic compared to the number
of SELECTs. The extra time spent at INSERT will be handsomely
amortized over all the simplified SELECT operations.



-----

Check out the book

Search Patterns
Design for Dis...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-01-26 05:15:46.122000-05:00

Check out the book
Search Patterns
Design for Discovery
By Peter Morville, Jeffery Callender
http://oreilly.com/catalog/9781449380335
It is slightly off topic because talking about searching in general and
not wild card searching in particular





