NULL Confusion
==============

:date: 2010-04-29 08:00
:tags: design
:slug: 2010_04_29-null_confusion
:category: Technologies
:status: published

The SQL database offers a domain-independent NULL value. This is a
terrible thing, and should be treated with a depth of respect and fear.

Before using NULL values in a database, read things like "`Null
Values in Fuzzy
Datasets <http://www.springerlink.com/content/m774708n21277205/>`__"
and "`Null Values Revisited in Prospect of Data
Integration <http://www.springerlink.com/content/lmvekd0xj0r54rq6/>`__".

See this
`question <http://stackoverflow.com/questions/1017064/null-value-in-database>`__,
and the answers -- people are very, very confused by NULL. The issue
is that the SQL NULL conflates several separate and unrelated
concepts.

-   **Not Available Now**. We expect that the data will be discovered
    later. That is, this NULL is a work-around for a process issue.

-   **Not Applicable (or Optional)**. This means that disjoint
    subtypes have been unified into a single table with optional or
    not-applicable attributes. This is an optimization choice. This
    also be due to state changes: the attribite is not used in one
    state, but will be used in another state.

With two meanings for a single value, hilarity always ensues.

**Further Confusion**

The NULL value doesn't participate in comparisons or indexes. This is
-- apparently -- shocking to some people. Here's a nice summary in
"`Why NULL never compares false to anything in
SQL <http://www.xaprb.com/blog/2006/05/18/why-null-never-compares-false-to-anything-in-sql/>`__".
Also, some notes for Oracle users in "`Understand Oracle null
values <http://www.dba-oracle.com/oracle_tips_ault_nulls_values.htm>`__"
and "`Oracle conditions and how they handle
NULL <http://www.lifeaftercoffee.com/2005/09/28/oracle-conditions-and-how-they-handle-null/>`__"

Because of this "NULL doesn't compare" problem, people get baffled by
the use of NVL (or IFNULL) functions.

**The Rules of NULL**

**The first rule of NULL is "Don't."** Don't define a data model that
depends on nullability. Define a model where each class is distinct
and all the attributes are *required*. This will lead to a number of
focused, distinct class definitions. A large number. Get over it.
Don't pre-optimize a design to reduce your number of classes or
tables.

Once you have a model that makes sense -- one that you can prove will
work -- one that precisely matches the semantics of your problem --
you can optimize. But don't start out by pre-optimizing or taking
"obvious" short-cuts.

**The second rule of NULL is "Don't conflate Availability with Applicability."** If you have data that is not available, you may
have serious issues in the process you're trying to automate. Often,
this is because you have multiple views of a single entity. If you
have data that's not applicable, you've done your design wrong -- you
put disjoint subtypes into a single class definition. Factor them
(for now) into class definitions where *all attributes are required*.

If you have inapplicable or unavailable data, you must factor things
into pieces where all attributes are required. You will then find
that your "thing with optional attributes" is either "thing that
changes state" or "thing with multiple subsets of attributes that
must be joined together." Later, you can think about optimizing.

"But," you object, "it's a *single* entity, I can't meaningfully
decompose it."

Consider the root causes for missing data before you take this
position too seriously.

Let's take a concrete example. We're doing econometric analysis of
businesses. We have a "Business" entity that has various kinds of
measurements from various sources. Not all sources of information
have data on all businesses. There's a lot of "not available" data.
Also, depending on the type of business, there may be a certain
amount of "not applicable" data. (For example, not-for-profit
corporations, privately held companies and public companies all have
different kinds of reporting requirements.)

What you have is a core "Business Name" entity with the minimal
information. Name; maybe other identifying information. But often,
the name is all you know.

You have a "Business Address" entity with mailing address. Small
businesses may have only one of these. Large businesses will have
more than one.

You have "Econometric Scoring From Source X" which may have a
normalized name, a different address and other scores.

Conceptually, this is a single entity, a business. But from three
different points of view. Initially, this is not a single class
definition. It may be optimized into a single table with NULLs.
That's a lousy design, but very popular. There are multiple
addresses; scores change over time. Implementing this as a
"single-table-with-nulls" seems to be a bad policy.

**The third rule of NULL is "Only as an optimization."** If you can
prove that a particular join is nearly one-to-one, and you can prove
that the cost of the join is too high, then you can consider
pre-joining and using NULLs.

**Common Mistakes**

There are two common NULL-join mistakes: optional joins and date
ranges.

One common mistake is attempting to join on an "optional" attribute.
You wind up with NVL functions in the WHERE clause. RED ALERT.

If you have NVL functions in a WHERE clause then (1) you've defeated
all indexing and (2) you've reinvented the wheel.

An NVL to a where clause is stand-in for a UNION. When you think you
need an NVL, you've got two subsets that you're tying to put
together: the subset with a non-NULL value and the subset with a NULL
value. This is a UNION, and the UNION will probably be faster than
your NVL construct. (If it isn't, good on you for benchmarking.)

Another common mistake is date ranges. Folks insist on having
"open-ended" date ranges where the "end-of-time" is represented as a
NULL. RED ALERT. NULL already means not applicable or not available.
The end of time is both applicable and available. Don't add a new
meaning to NULL.

Coding the end of time as NULL is simply wrong. The end of time (for
now) is 12-21-2112. It's an easy date to remember. It's a cooler date
in Europe than the US.

"But," the deeply argumentative claim, "I can't have my application
dependent on a mystery constant like that". Lighten up. First, your
app won't be running in 2112. Second, your app is full of mystery
constants like that. You've got codes, your users have codes they
think are important. Your localtime offset from GMT is a mystery
constant. The start and end dates for daylight savings time are
mystery constants. Please. You have lots of mystery constants. If you
want to be "transparent", make it a configuration parameter.

Just code the end-of-time as a real date not a NULL and use ordinary
date-range logic with no silly NVL business.



-----

NULL means that a property doesn&#39;t exist for a...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-04-29 09:50:21.438000-04:00

NULL means that a property doesn't exist for a record -- nothing more
nothing less. It is exactly what you want when you have a date range
where some records don't have an end date. Either you have living people
and dead people in separate tables, or you pre-union them and use NULLs
for date of death. That's what NULL is for, and it's good at it. Your
silly special value is a date, so everybody in your table is currently
dead in the future. That makes no sense. Worse, and not a matter of
taste at all, is that using a special date to mean no-date is a bug.
Unlike NULL, the database doesn't know anything special about that
particular date or your convention. It will happily compute wrong
numbers based on it, instead of turning all your erroneous results into
NULLs, as they should be. What's the cumulative life span of everybody
in the system? Well, if you don't explicitly use the current date for
living people, you'll get NULL. There is no cumulative life span when
you don't specify how to deal with living people. NULL is not a special
date. It is no-date. NULL shouldn't be overused, but there are some
specific cases where it is a good optimization, if you understand the
tradeoffs and don't use it for something it is not.


Nullology: The Zen of Database C.J. Dat...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-05-04 18:00:10.878000-04:00

Check out
Nullology: The Zen of Database C.J. Date
http://post.oreilly.com/rd/9z1zquisnote29p5lsq1r7i10h3t9qlf9s89vl7aubo


Your example can be improved: - a table of a...
-----------------------------------------------------

Chris<noreply@blogger.com>

2010-05-18 11:57:30.045000-04:00

@Adam

Your example can be improved:

- a table of all persons with their date of birth (and other required fields)

- a separate table that contains the date a person dies

@Others

At my company, we build our data models without NULLs and have done so,
successfully on many occasions (and yes, they are real world scenarios).
The trick is to understand "why" you don't have that information. Yes,
we have a lot of tables and the queries are complex, but the data
structure is rigid and provable. We know what the meaning of all the
data is at any point. With NULL, there is no "meaning" to that data, so
you cannot reason about it (and if that is the case, you should use a
document store or other non-SQL store).





