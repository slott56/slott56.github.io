Spreadsheet Regrets
===================

:date: 2019-10-08 08:00
:tags: #python,data conversion,beautiful soup,spreadsheet
:slug: 2019_10_08-spreadsheet_regrets
:category: Technologies
:status: published


I can't emphasize this enough.

Some people, when confronted with a problem, think

“I know, I'll use a spreadsheet.”   Now they have two problems.

(This was originally about regular expressions. And AWK.
See http://regex.info/blog/2006-09-15/247)

Fiction writer F. L. Stevens got a list of literary agents from AAR
Online. This became a spreadsheet driving queries for representation.
After a bunch of rejections, another query against AAR Online provided
a second list of agents.

Apple's Numbers product will readily translate the AAR Online HTML
table into a usable spreadsheet table. But after initial success the
spreadsheet as tool of choice collapses into a pile of rubble. The
spreadsheet data model is hopelessly ineffective for the problem
domain.

What is the problem domain?

There are two user stories:

#. Author needs to deduplicate agents and agencies. It's considered poor
   form to badger agents with repeated queries for the same title. It's
   also bad form to query two agents at the same agency. You have to get
   rejected by one before contacting the other.

#. Author needs to track activities at the Agent and Agency level to
   optimize querying. This mostly involves sending queries and tracking
   rejections. Ideally, an agent acceptance should lead to notification
   to other agents that the manuscript is being withdrawn. This is so
   rare as to not require much automation.


Agents come and go. Periodically, an agent will be closed to queries
for some period of time, and then reopen. Their interests vary with
the whims of the marketplace they're trying to serve. Traditional
fiction publishing is quite complex; agents are the gatekeepers.


To an extent, we can decompose the processing like this.


1.  Sourcing. There are several sources: AAR Online and Agent Query
    are two big sources. These sites have usable query engines and the
    HTML can be scraped to get a list of currently active agents with a
    uniform representation. This is elegant Python and Beautiful Soup.


2.  Deduplication. Agency and Agent deduplication is central. Query
    results may involve state changes to an agent (open to queries,
    interested in new genres.) Query results may involve simple
    duplicates, which have to be discarded to avoid repeated queries.
    It's a huge pain when attempted with a spreadsheet. The simplistic
    string equality test for name matching is defeated by whitespace
    variations, for example. This is elegant Python, however.


3.  Agent web site checks. These have to be done manually. Agency web
    pages are often art projects, larded up with javascript that produces
    elegant rolling animations of books, authors, agents, background art,
    and text. These sites aren't really set up to help authors. It's
    impossible to automate a check to confirm the source query results.
    This has to be done manually: F. L. is required to click and update
    status.


4.  State Changes. Queries and Rejections are the important state
    changes. Open and Closed to queries is also part of the state that
    needs to be tracked. Additionally, there's a multiple agent per
    agency check that makes this more complex. The state changes are
    painful to track in a simple spreadsheet-like data structure: a
    rejection by one agent can free up another agent at the same agency.
    This multi-row state change is simply horrible to deal with.
    Bonus confusion! Time-to-Live rules: a query over 60 days old is
    more-or-less a *de facto* rejection. This means that periodic scans
    of the data are required to close a query to one agent in an agency,
    freeing up subsequent agents in the same agency.


Manuscript Wish Lists (MSWLs) are a source for agents actively
searching for manuscripts. This is more-or-less a Twitter query.
Using the various aggregating web sites seems slightly easier than
using Twitter directly. However, additional Twitter lookups are
required to locate agent details, so this is interesting
web-scraping.

Of course F. L. Stevens has a legacy spreadsheet with at least four
"similar" (but not really identical) tabs filled with agencies,
agents, and query status.


I don't have an implementation to share -- yet. I'm working on it
slowly.

I think it will be an interesting tutorial in cleaning up
semi-structured data.


