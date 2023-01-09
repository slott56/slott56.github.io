The SQL-based relational database isn't perfection? Whoa if true
================================================================

:date: 2018-02-08 19:00
:tags: design,noSQL
:slug: 2018_02_08-the_sql_based_relational_database_isnt_perfection_whoa_if_true
:category: Technologies
:status: published

| Yes, there are people for whom document databases (and the file
  system) are confusing and weird.
| I was sent this: `Relational Algebra Is the Root of SQL
  Problems <https://www.datasciencecentral.com/profiles/blogs/relational-algebra-is-the-root-of-sql-problems>`__
  which is really brilliant and provides some helpful concrete examples
  of stuff SQL is really bad at.
| The accompanying email was filled with nonsense about how important
  and world-changing SQL was.
| I can't disagree. Back when disk was very expensive and very small,
  the SQL-based join strategies where essential for micro-managing every
  bit of data. Literally. Every Bit.
| And then we would denormalize the structure for performance reasons.
  Because we always knew the SQL was terrible at a fairly large number
  of things.
| Those days are behind us. We can now chose to use a document database,
  and make our lives simpler. Storage is relatively inexpensive, and the
  labor to normalize and denormalize data doesn't create significant
  value. The need to write stored procedures to turn a single conceptual
  operation into a bunch of inserts and updates was a symptom that this
  wasn't the best approach.
| I've had many "But what about..." conversations regarding document
  databases.
| "What about ad-hoc queries in SQL?"
| - Do you really do these without writing a Python script or creating a
  Pandas dataframe? I doubt it. But. If you really think you'll do this,
  most document stores either support a modified SQL or Javascript. And
  yes, you hate Javascript, duly noted. I hate SQL, so we're even there.
| "What about joins?"
| - It's a space-saving technique. We don't need the overheads to save
  the space. The "update anomalies" still require careful design, and
  may lead to some decomposition of data into multiple documents. But
  the ruthless normalization shouldn't be seen as a requirement.
| "What about the schema?"
| - It's brittle and schema migration creates a lot of low-value labor.
  We can use Python JSONSchema to validate documents. See `NoSQL
  Database doesn't Mean No
  Schema <https://medium.com/capital-one-developers/nosql-database-doesnt-mean-no-schema-a824d591034e>`__.

Transactional v. Analytical
---------------------------

| It requires some care to understand the distinction between
  "transactional" and "analytical" uses for data. While folks try to
  leverage this distinction, it's a spectrum not a distinction.
| A lot of data collection is a simple sequence of event documents.
  These have no sensible state change, so they're not really
  transactional. They are often created by concurrent processes where
  locking prevents corruption, so transactions \*seem\* helpful. Except,
  of course, the file system writes can be trivially sharded by process
  ID and then unified later. And all document databases serialize
  document writes from multiple client processes, so there's no value to
  writing a relational database.
| Some data operations are properly stateful. By normalizing our tables,
  moving from consistent state to consistent state is made complex.
  Which requires a defined transaction as a work-around. And don't get
  me started on replication and two-phase commit as yet another layer of
  complexity on top of transactions.
| A document database allows us to skip over 1NF. We can think of a
  document as being a row in a table where the data types are complex
  data structures involving mappings, sequences, strings, numbers,
  booleans, and nulls. (See `JSON Schema <http://json-schema.org/>`__.)
  A lot of multi-step SQL transactions are operations on several
  children of a common parent. If the parent was persisted as a single
  document, there wouldn't be multiple operations, an atomic MongoDB
  update operation can make complex rewrites to a complex document.
| We can contrive a design where state changes must be coordinated and
  the data cannot be colocated in a single document. It's not difficult
  to stipulate enough requirements to make single documents difficult.
  The presence of these contrived requirement, however, doesn't suddenly
  invalidate document datastores for transactional data. In the SQL
  world, the idea of long-running and reversible long-running
  transactions has always been a horrible problem. Allowing stacked
  "undo" for the user means either creating a chain of **Memento**
  objects that can recover previous state, or having numerous flags and
  indicators on each record, allowing the state to be reversed. Some
  design problems are really hard. And the SQL model seems to make them
  harder.
| The core ACID concepts of always consistent is -- in practice --
  nonsense. As soon as we have to consider "isolation levels" and "read
  consistency" it becomes clear that there is no consistent state unless
  all transactions and queries are serialized via exclusive "whole
  database" locking. Competent DBA's know that long-running analytic
  queries performed concurrently with transactional updates can't use
  locking, and must tolerate inconsistencies in the database.
| It's common practice to do data extracts so that analytic queries
  aren't working against the (inconsistent) transactional data. In this
  case, the frequency of extracts is the timing of "eventual
  consistency" promised by the BASE concept.
| Bottom Line: Relational ACID rules are almost always broken in
  practice by read consistency rules and extracts to analytic databases.
  Analytical data is always based on eventual consistency expectations.
  The batch extracts means "eventually" is measured in hours. A document
  data store can often create consistency in milliseconds. (MongoDB
  primary failure, voting, and secondary promotion to primary relies on
  a 10-second heartbeat, so it takes time to discover and repair.)

Also
----

| A second email detailed their amazement (Amazing! Wow! Unbelievable!
  You Must Inform The World Of This!) that analytic processing of data
  is actually faster and simpler using the file system. The very idea of
  HDFS was so amazing that they were amazed.
| Somehow, the idea of the raw filesystem as being really, really fast
  was the source of much amazement.
| I'm glad they're making an effort to catch up. I'm glad they're seeing
  the relational model as a bad choice that has a limited number of use
  cases. Mostly, relational databases are useful for an organization
  can't write API's to handle the integrity issues.
| `To SQL or NoSQL? That's the database question \| Ars
  Technica <https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0ahUKEwj_p_Suie7YAhUBUKwKHY_zA3UQFggxMAE&url=https%3A%2F%2Farstechnica.com%2Finformation-technology%2F2016%2F03%2Fto-sql-or-nosql-thats-the-database-question%2F&usg=AOvVaw1ifu0XcvWq5iNhPKb7XZhj>`__





