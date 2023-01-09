MongoDB and Schema Validation
=============================

:date: 2014-11-20 08:00
:tags: #python,mongodb,schema migration
:slug: 2014_11_20-mongodb_and_schema_validation
:category: Technologies
:status: published

| One part of the MongoDB value proposition is being freed from the
  constraints of a database schema.
| There's a "baby and bathwater" issue here. While a schema can become a
  low-value constraint, we have to be careful about throwing out the
  baby when we throw out the bathwater. A schema isn't inherently evil.
  A schema that's hard to modify can become more cost than benefit.
| When working with document databases like MongoDB or CouchDB, we're
  freed from the constraints of a schema.
| But.
| Do we really want the kind of freedom that can devolve to anarchy?
| Or.
| Do we want some kind of constraint checking capability to provide some
  additional run-time assurance that the applications are using the
  database properly?
| Read this http://realprogrammer.wordpress.com/tag/json-schema/ and
  this http://www.litixsoft.de/english/mms-json-schema/.
| My thesis is that some schema validation may have some value.
| My plan is this.
| 1. Define the essential collections for the various documents using
  ordinary document design practices.
| 2. For each document class, we'll have two closely associated
  collections:

-  The primary collection, call it it "class" because it matches one of
   the application classes.
-  An additional "class.schema" collection. This collection will contain
   JSON-schema documents.
   See `http://json-schema.org <http://json-schema.org/>`__ for more
   information.
-  For audit, and sequential key generation, we may have some additional
   associated collections.

| Because JSON schema documents have a "$schema" field, we can replace
  the "$" with "\\uFF04" the "FULLWIDTH DOLLAR SIGN" character when
  saving the JSON-schema document into a MongoDB database. We can do the
  inverse operation when finding the schema documents in the database.
| 3. Use a tool like https://github.com/Julian/jsonschema to validate
  the schema. The document-level validation could be embedded in the
  application for each transaction. However, it seems better trust the
  code and the unit testing of the code to enforce schema rules. We'd
  use this validation periodically to check the schema. Significant
  events should include a validation pass. For example, before and after
  any schema changes. This way we can be sure that things are continuing
  to go properly.
| It would be strictly an additional layer of checking.





