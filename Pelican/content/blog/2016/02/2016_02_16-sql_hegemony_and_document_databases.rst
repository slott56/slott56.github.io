SQL Hegemony and Document Databases
===================================

:date: 2016-02-16 08:00
:tags: #python,noSQL,SQL,mongodb
:slug: 2016_02_16-sql_hegemony_and_document_databases
:category: Technologies
:status: published

| A surpassingly strange question is this: "How do I get the data out of
  MongoDB into a spreadsheet?"
| The variation is "How can we load the MongoDB data into a relational
  database?"
| I'm always perplexed by this question. It has a subtext that I find
  baffling. The subtext is this "all databases are relational, right?"
| In order to ask the question, one has to be laboring under the
  assumption that the only difference between MongoDB and a relational
  database is the clever sticker on your laptop. Mongo folks have a
  little green Mango leaf. Postgres has a blue/gray elephant.
| This assumption is remarkably hard to overcome.
| THEM: "How can we move this mongo data into a spreadsheet?"
| ME: "What?"
| THEM: "You know. Get a bulk CSV extract."
| ME: "Of complex, nested documents?"
| THEM: "Nested documents?"
| ME: "Mongo database documents include arrays and -- well --
  subdocuments. They're not in first normal form. They don't fit the
  spreadsheet data model."
| THEM: "Whatever. Every database has a bulk unload into CSV. How do you
  do that in Mongo?"
| ME: "You can't represent a mongo document in rows and columns."
| THEM: (*Thumping desk for emphasis*.) "Relational Theory is explicit.
  ALL DATA CAN BE REDUCED TO ROWS AND COLUMNS!"
| ME: "Right. Through a process of normalization. The Mongo data you're
  looking at isn't normalized. You'd have to normalize it into a
  relational table model. Then you could write a customized extract
  focused on that relational model."
| THEM: "That's absurd."
| At this point, all we can do is give them the minimal pymongo
  MongoClient code block. Hands-on queries seem to be the only way to
  make progress.

::

   from pymongo import MongoClient
   from pprint import pprint
   with MongoClient("mongodb://somehost:27017") as mongo:
       collection = mongo.database.collection
       for document in collection.find():
            pprint(document)

| 
| Explanations seem to wind up in a weird circular pattern where they
  keep repeating their relational assumptions. Not much seems to work:
  diagrams, hand-waving, links to tutorials are all implicitly rejected
  because they don't confirm SQL bias.
| A few days later they call asking how they are supposed to work with a
  document that has complex nested fields inside it.
| This could be the beginning of wisdom. Or it could be the beginning of
  a lengthy reiteration of SQL Hegemony talking points and desk
  thumping.
| THEM: "The document has an array of values."
| ME: "Correct."
| THEM: "What's that mean?"
| ME: "It means there are multiple occurrences of the child object
  within each parent object."
| THEM: "I can see that. What does it mean?"
| ME: (*Rising inflection*.) "The parent is associated with multiple
  instances of the child."
| THEM: "Don't patronize me! Stop using mongo mumbo-jumbo. Just a simple
  explanation is all I want."
| ME: "One Parent. Many Children."
| THEM: "That's stupid. One-to-many absolutely requires a foreign key.
  The children don't even have keys. Mongo must have hidden keys
  somewhere. How can I see the keys on the children in this so-called
  'array' structure? How can expose the underlying implementation?"
| The best I can do is show them an approach to normalizing some of the
  data in their collection.

::

   from pymongo import MongoClient
   from pprint import pprint
   with MongoClient("mongodb://your_host:27017") as mongo:
       collection = mongo.your_database.your_collection
       for document in collection.find():
            for child in parent['child_array']:
                 print( document['parent_field'], child['child_field'] )

| 
| This leads to endless confusion when some documents lack a particular
  field. The Python document.get('field') is an elegant way to handle
  optional fields. I like to warn them that they should not rely on
  this. Sometimes document['field'] is appropriate because the field
  really is mandatory. If it's missing, there are serious problems. Of
  course, the simple get() method doesn't work for optional nested
  documents. For this, we need document.get('field', {}). And for
  optional arrays, we can use document.get('field', []).
| Interestingly we sometimes have confusion over {} for document and []
  for array. I chalk that up to folks who are too used to very wordy SQL
  and Java. I save the questions for my next book on Python.
| At some point, the "optional" items may be more significant than this.
  Perhaps an **if** statement is required to handle business rules that
  are reflected as different document structures in a single collection.
| This leads to yet more desk-thumping. It's accompanied with the
  laughable claim that a "real" database doesn't rely on **if**
  statements to distinguish variant subentities that are persisted in a
  single table. The presence of SQL **ifnull()** functions, **case**
  expressions, and application code with **if** statements apparently
  doesn't exist. Or -- when it is pointed out -- isn't the same thing as
  writing an **if** statement to handle variant document subentities in
  a Mongo database.
| It appears to take about two weeks to successfully challenge
  entrenched relational assumptions. Even then, we have to go over some
  of the basics of optional fields and arrays more than once.





