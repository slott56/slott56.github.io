State Change and NoSQL Databases
================================

:date: 2019-10-22 08:00
:tags: #python,noSQL
:slug: 2019_10_22-state_change_and_nosql_databases
:category: Technologies
:status: published

| Let's take another look at F. L. Stevens spreadsheet with agencies and
  agents. It's -- of course -- an unholy mess. Why? It's difficult to
  handle state change and deduplication.
| Let's look at state changes.
| The author needs URL's and names and a list of genres the agent is
  interested in. This is more-or-less static data. It changes rarely.
  What changes more often is an agent being closed or open to queries.
| Another state change is the query itself. Once the email has been
  sent, the agent (and their agency) should not be bothered again for at
  least sixty days. After an explicit rejection, there's little point in
  making any contact with the agent; they're effectively out of the
  market for a given manuscript.
| There are some other stateful rules, we don't need all the details to
  see the potential complexities here.
| A spreadsheet presents a particularly odious non-solution to the
  problem of state and state change. There's a good and a bad. Mostly
  bad.

-  On the good side, you can edit a single cell, changing the state. You
   can define a drop-down list of states, or radio buttons with
   alternative states.
-  The be bad side, you're often limited to editing a single cell when
   you want to change the state. You want to have dates filled in
   automatically on state change. You want history of state changes.
   Excel hackers try to write macros to automate filling in the date.
   History, however... History is a problem.

| We can try to spread history across the row. This rapidly becomes
  horrifying -- the rows are uneven in length, breaking a First Normal
  Form rule for spreadsheets.
| We can try to spread history down the rows of a column. Wow this is
  bad. We can try to use the hierarchy features to make history a bunch
  of folded-up details underneath a heading row. This is microscopically
  better, but still difficult to manage with all the unfolding and
  folding required to change state after a rejection.
| We can blow up a single cell to have non-atomic data -- all of the
  history with events and dates in a long, ";" delimited list.
| There's no good way to represent this in a spreadsheet.

What to do?
-----------

| The relational database people love the master-detail relationship.
  Agency has Agent. Agent has History. The history is a bunch of rows in
  the history table, with a foreign key relationship with the agent.
| The rigidity of the SQL schema is a barrier here. We're dealing with
  some sloppy data handling practices in the legacy spreadsheet. We
  don't want to have to tweak the SQL each time we find some new
  subtlety that's poorly represented in the spreadsheet data.
| We're also handling a number of data sources, each with a unique
  schema. We need a way to unify these flexibly, so we can fold in
  additional data sources, once the broken spreadsheet is behind us.
| (There are a yet more problems with the relational model in general,
  those are material for a separate blog post. For now, the rigidity and
  complexity are a big enough pair of problems.)

SQL is Out. What Else?
----------------------

| A document store is pretty nice for this.  The rest of this section is
  an indictment of SQL. Feel free to skip it. It's widely known, and
  well supported elsewhere.
| We have an Agency as the primary document., Within an Agency, there
  are a number of individual Agents. Within each agent is a series of
  Events. Some Agents aren't even interested in the genre F. L. Stevens
  writes, so they're closed. Some Agents are temporarily closed. The
  rest are open.
| The author can get a list of open agents, following a number of rules,
  including waiting after the last contact, and avoiding working with
  multiple agents within a single agency. After sending query letters,
  the event history gets an entry, and those agents are in another
  state, query pending.
| One common complaint I hear about a document store is the "cost" of
  updating a large-ish document. The implicit assumption seems to be
  that an update operation can't locate the relevant sub-document, and
  can't make incremental changes. Having worked with both SQL and NoSQL,
  this "cost of document update" seems to be unmeasurably small.
| Another cluster command question hovers around locking and
  concurrency. Most of them nonsensical because they come from the world
  of fragmented data in a SQL database. When the relevant object (i.e.
  Agency) is spread over a lot of rows of several tables, locking is
  essential. When the relevant object is a single document, locks aren't
  as important. If two people are updating the same document at the same
  time, that's a document design issue, or a control issue in the
  application.
| Finally, there are questions about "update anomalies." This is a
  sensible question. In the relational world, we often have shared
  "lookup" data. A single change to a lookup row will have a ripple
  effect to all rows using the lookup row's foreign key.
| Think of changing zip code 12345 from Schenectady, NY to Scotia, NY.
  Everyone sharing the foreign key reference via the zip code has been
  moved with a single update. Except, of course, nothing is visible
  until a query reconstructs the desired document from the fragmented
  pieces.
| We've traded a rare sweeping updated across many documents for a
  sweeping, complex join operating to build the relevant document from
  the normalized pieces. Queries are expensive, complex, and often
  wrong. They're so painful, we use ORM's to mask the queries and give
  us the documents we wanted all along.

What's It Look Like?
--------------------

| This:

::

   @dataclass
   class Agency:
       """A collection of individual agents."""
       name : str
       url : Optional[str] = field(default=None)
       agents : Dict[str, 'Agent'] = field(init=False, default_factory=dict)

   @dataclass
   class Agent:
       """An Agent with a sequence of events: actions and state changes."""
       name : str
       url : str
       email : str
       fiction_genres : List[str]
       query_details : str = field(default_factory=str)
       events : List['Event'] = field(init=False, default_factory=list)

   @dataclass
   class Event:
       """An action or state change.
       status = 'open', 'closed', 'query sent', 'query outcome', 'closed until', etc.

       Depending on the status, there may be additional details.
       For 'query sent', there's 'date'.
       For 'query outcome', there's 'outcome' and an optional 'date'.
       for 'closed until', there's 'reason' and an optional 'date'.
       """
       status : str
       date : Optional[datetime.date] = field(default=None)
       outcome : Optional[str] = field(default=None)
       reason : Optional[str] = field(default=None)

       def __repr__(self):
           return f"{self.status} {self.date} {self.outcome} {self.reason}"

| 
| We have three classes here. Agency is the parent document. Each Agency
  contains one or more Agent instances. Each Agent contains one or more
  Events.
| When we fetch an agent's data, we fetch the entire agency, since the
  "business" rules preclude querying more than one agent in an agency.
  The queries involve a nuanced state change: a rejection by one agent,
  opens another in the same agency.  Rather than do some additional SQL
  queries to locate the parent and other children of the parent, just
  read the whole thing at once.
| In later posts, we'll look at deduplication and some other processing.
  But this seems to be all the schema we'll ever need.  The type hints
  provided **mypy** some evidence of what we intend to do with these
  documents.





