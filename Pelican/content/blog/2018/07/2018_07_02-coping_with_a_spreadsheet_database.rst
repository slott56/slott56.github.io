Coping with a Spreadsheet Database
==================================

:date: 2018-07-02 19:18
:tags: #python,spreadsheet,design,stingray reader
:slug: 2018_07_02-coping_with_a_spreadsheet_database
:category: Technologies
:status: published


A common way to save persistent, important data is a spreadsheet. It
provides a handy, potentially normalized store that's readily
accessible with minimal tooling. It has a UI usable by people with a
spectrum of skills.

Sadly.

There's a core conflict:

-  The advantages of spreadsheets-as-database are numerous.

-  The disadvantage is the lack of any strict, formal control over the
   schema.


At the very best, the steward of the data has some discipline and they
include column headers and assure they're used throughout the rows of
data.

It goes downhill rapidly from that ideal.

Let's look at some scenarios. And. How to cope. And. *Python to the Rescue*.

Outliers, Special Cases, Anomalies, and other Irregularities
------------------------------------------------------------


The whole point of a "normalized" view of the data is to identify a
pattern, assign the lofty title of "Schema" to the pattern, and assure
all of the data fits the schema. In rare cases, all of the data fits a
simple schema. These cases are so rare they only exist in examples of
SQL code in tutorials.

A far more common case is to have several subtypes which are so
similar that optional attributes (or "nullable columns" in SQL
parlance) allow one schema description to encompass all of the cases.
If you're a JSON Schema person, this is the "OneOf" or "AnyOf" type
definition.

Some folks will try argue that optional attributes don't always mean
that there are several subtypes. They'll ramble on for a while and
eventually land on "state change" as a reason for optional attributes.
The distinct states **are** distinct subtypes. Read up on the
**State** design pattern for OO programming. Optional attributes is
the definition of subtype.

The hoped-for simple case is a superclass extended by subclasses used
to add new attributes. In this case, they're all polymorphic with
respect to the superclass. In a spreadsheet page, the column names
reflect the union of all of the various attributes. There are two
minor variants in the way people use this:

-  An attribute value is a discriminator among the subtypes. We like
   this in SQL processing because it's fast. It also allows for some
   validation of the discriminator value and the pattern of attributes
   present vs. attributes omitted. Of course, the pattern of empty cells
   may disagree with the discriminator value provided.

-  The pattern of attributes provided versus omitted is used to identify
   the subtype. This is a more reliable way to detect subtypes. There
   can, of course, be problems here with values provided accidentally,
   or omitted accidentally.


The less desirable case is disjoint classes with few common
attributes. Worse, the common attributes are not part of the problem
domain, but are things that feel databasey, like made-up surrogate
keys. There's an "ID" in column A or some other such implementation
detail. Some of the rows use column A and columns B to G. The other
rows use column A and columns H to L. The **only** common attributes
are the surrogate keys, perhaps mixed with foreign key references to
rows in other spreadsheet tables or pages.)


This is a collection of disjoint types, slapped together for no good
reason. SQL folks like to call it "multiple master-detail
relationships". The master record has children of multiple types. In
some cases, the only thing the children have in common is the foreign
key relationship with the parent. If you want a concrete example,
think of customer contact information: multiple email addresses,
multiple phone numbers. The two contacts have nothing in common
except belonging to one customer.


These don't belong in a single spreadsheet table. But. There they
are. Our code must disentangle the subtypes.




Arrays
------


A lot of spreadsheet data is a two-dimensional grid. Budgets, for
example, might have categories down the page and months across the
page.


This is handy for visualization. But. It's not the right way to
process the data at all.


This extends, of course, to higher orders. Each tab of a spreadsheet
may be a dimension of visualization. There may be groups of tabs with
a complex naming convention to include multiple dimensions into tab
names. Rows may have multiple-part names, or use bullets and
indentation to show a hierarchy.


All of these techniques are ways to provide a number of dimensions
around a fact that's crammed into a cell. The budget amount is the
fact. The category and the month information are the two dimensions
of that cell. In many cases, Star-Schema techniques are helpful for
understanding the underlying data, separate from the visualization as
a spreadsheet.


Our code must disentangle the dimensions of the meaningful facts.

Normalization
-------------


There are tiers of normalization. The normalization described above is
part of First Normal Form (1NF): all rows are the same and all data
items are atomic. Pragmatically, it's rare that all spreadsheet rows
are the same, because it's common to bundle multiple subtypes into a
single table.

   Sidebar Rant. Yes, the presence of nullable columns in a SQL table
   \*is\* a normalization error. There, I said it. Error. We can always
   partition the rows of table into a number of separate tables; in each
   of those tables, all columns are required. We can rebuild the
   original table (with optional fields) via a union of the various
   decompositions (none of which have optional fields). The SQL folks
   prefer nullable columns and 1NF violations over unions and 1NF
   absolutism. I'm a fan of 1NF absolutism to understand each and every
   nullable attribute because casual abuse of nulls is a common design
   error.


The other part of 1NF is each value is atomic: there's no internal
structure to the value. In manually-prepared spreadsheet data, this is
difficult to insist on.  Stuff gets combined into a single cell
because -- well -- it seemed helpful to the people entering it. They
put all the lines of an address into a single cell because they like
to see it that way.

Third Normal Form (3NF) forbids derived data (and transitive
dependencies). In a spreadsheet, we might have a row-level
computation. It helps the person confirm the data is correct. It's not
"essential". It breaks the 3NF rule because the computed attribute
depends on other field values; a change to one attribute will also
change the derived attribute.

When we first encounter spreadsheet data, this isn't always obvious.
In some cases, the derived data is computed "off-line" -- i.e.,
manually -- and entered into the spreadsheet. Really. People pull up a
calculator app (or whip out their phone), compute a value, and type it
in. In other cases, they look something up manually and enter it.

These kinds of data entry weirdnesses require code to normalize the
manually-prepared data. We'll have to decompose non-atomic fields. And
we'll have to handle derived data gracefully. (Reject it? Fix it? Warn
them about it? Handle it as an exception?)

Relationships
-------------


Let's talk about Second Normal Form (2NF). We really want to have a
row in a table represent a single thing. The SQL folks require all of
the attributes to be dependent on the row's key. In spreadsheet world,
we may have a jumble of attributes with a jumble of dependencies. We
may have multiple relationships in a single row.  Look at the `Second
Normal Form <https://en.wikipedia.org/wiki/Second_normal_form>`__ page
on Wikipedia for examples of multiple relationships mashed together
into a single row.

When a spreadsheet has 2NF problems, there will be situations were
some collection of attributes is repeated -- verbatim -- in multiple
places. The most common example in US-based data is City-State-ZIP
Code. These three \*always\* form a consistent triple of data, and
should be repeated as part of an address. In SQL terms, City and State
have a functional dependency on the ZIP Code. In an Object-Oriented
database, we might have a separate City-State-Zip class definition. In
a document datastore, we might combine these items into a
sub-document.

In any 2NF problem area, we're forced to write code which normalizes
this internal relationship.

And. When we do that we'll find the kinds of problems we find with
derived data: The ZIP code 22102 might be McLean or Tysons Corner. One
of them is "right" and the other is "wrong", Or perhaps there needs to
be an exception to handle this. Or perhaps a correction applied to
coerce the wrong values to be right.

The "Association" Table
-----------------------


There's a SQL design pattern called an association table. This is
used to handle a many-to-many relationship between two entities.
Consider Boats and Owners. A boat will have multiple owners. An owner
may have multiple boats. In SQL world, this requires a special table
with two foreign keys. In the degenerate case, there are no other
attributes. In the boat-owner relationship case, however, there's
often a range of dates that specifies when an owner was associated
with a boat. The range of dates applies to the relationship itself,
not to boat nor to owner.


In a spreadsheet there are numerous ways to represent this. Numerous.
A list of boat rows after each owner.  A list of owner rows after
each boat. A number of owner columns for each boat.  A block of text
with a list of owner names in a single cell. Creative people will
create many creative solutions to this data representation problem.


Note that the association table is a SQL hack. It's an implementation
detail, not an essential feature of the problem domain. In Python,
for example, we'll need to use weakref objects to handle this
cleanly.


When Owner O1 refers to Vessel V1 it's easy to have a list of vessel
references under the owner. When the Owner O1 object is no longer
needed, it can be removed from memory. This decrements the references
count for Vessel V1 to zero, and it will also be removed from memory,
too.


When we have mutual references, we have a problem, solved by
weakrefs.


If Owner O1 refers to Vessel V1 **and** we also have Vessel V1
referring to Owner O1, we have mutual references. O1 has a list that
includes V1.  V1 also has a list that includes O1. This means there
are two strong references to O1: some variable, owner, and Vessel V1
**also** refers to O1. When the variable owner is no longer needed,
then the reference count to O1 is decremented from two to one. And
the object can't be deleted yet.


If V1 has a *weak* reference to O1, then the strong reference count
-- based on the variable owner -- is only one. The weak reference
from V1 doesn't count for memory management purposes. O1 can be
removed from memory, references to V1 will be decremented, and it,
too, can be removed.


Our code will have to parse and populate the relationships. And we'll
need to use weakref to be sure we can cleanly remove objects.

Coping Strategies
-----------------


As noted above, we have to cope with manually-prepared spreadsheet
data. It looks like this:

#. Figure out what the likely data structure is. This isn't simple.
   We'll look at Pythonic techniques below. When starting, it helps to
   draw UML class diagrams (or ER diagrams) over and over again to try
   and depict the data. I'm a fan of
   using `https://yuml.me <https://yuml.me/>`__ to draw the pictures
   because they have a super-handy text notation for the relationships
   and attributes.

#. Leverage the **Extract-Transform-Load** design pattern.

   -  The "extract" reads the source spreadsheet data. A first version
      will be trivial use of xlrd or csv module. Or any of the modules
      listed
      here: `http://www.python-excel.org <http://www.python-excel.org/>`__.

   -  The "transform" should be implemented as a function to transform
      source to the target model. Pragmatically, this single function
      will leverage a number of other functions to validate, cleanse,
      convert, and normalize the data.

   -  The "load" may not be anything more than creating instances of the
      underlying model classes. In some cases, the instances of the
      model classes may wind up in an in-memory dictionary. In other
      cases, the "load" might be a simple use of pickle or shelve to
      persist the useful data.

#. Separate Model, ETL, and "Real Work" from each other. The model
   should evolve very slowly. It's the essential problem we're solving.
   The ETL may vary with each major revision to the spreadsheet
   database. Users add columns, they change meanings, their
   understanding evolves. The final work is based on the model -- and
   only the model -- ignoring the vagaries of ETL.

#. Plan for change. Each manually-prepared spreadsheet is a unique
   snowflake, precious and distinct. This leads to an important lesson
   based on the `Open/Closed
   Principle <https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle>`__:** Code
   Must Be Closed To Modification and Open To Extension**. Each version
   of the source data means adding new functions or classes to cope with
   each bizarre new spreadsheet issue. When the source data changes,
   don't modify any old code; **Always Be Adding**. This means planning
   for multiple versions of functions: validate_1(), validate_2(),
   validate_3().  It's essential to be able process \*all\* old versions
   of the data and get meaningful, useful results for regression
   testing.

Python To The Rescue
--------------------


Data modeling must be done slowly and reluctantly. Don't overfit the
model to the first spreadsheet.

Here's the place to start

::

   from typing import SimpleNamespace
   class Model(SimpleNamespace ):
       pass

This is \*enough\* modeling to get started. Don't over-engineer the
  model. We can then do things like this.

::

   class Owner(Model):
       pass


This defines the class Owner as an instance of some abstract Model
  class. The SimpleNamespace allows us to have **any** attributes we
  think we need.

::

   owner = Owner(vessel=some_id, name=row['name'])




We can leverage the SimpleNamespace to build useful objects with
minimal code. This can be replaced with a typing.NamedTuple or a
@dataclass class definition when the definition is more mature.

The "extract" code needs to gather row-like objects. Ideally, this is
a generator function. Because normalization and dereferencing may
require multiple passes through the data, a list can be slightly
easier to deal with. We'll come back to normalization and
dereferencing below.

For some background in the classes used here,
see https://sourceforge.net/projects/stingrayreader/. (Yes, this is
old; I'm thinking of moving it to GitHub and updating it to Python
3.7.)

::

   def load_live_rows(workbook, sheet_name):
       sheet1 = sheet.EmbeddedSchemaSheet(workbook, sheet_name, schema.loader.HeadingRowSchemaLoader)
       dict_rows = sheet1.schema.rows_as_dict_iter(sheet1)
       clean_data = filter(lambda row:not row['Hull No.'].is_empty(), dict_rows)
       initial_data = take_until(lambda row:row['Hull No.'].to_str() == 'Definitely WB Owners:', clean_data)
       return list(initial_data)




Step-by-step.

#. We're working with a sheet that has the schema embedded in it. That
   means using the heading rows as column information. The
   HeadingRowSchemaLoader will be grabbing the first few rows from the
   EmbeddedSchemaSheet. Sometimes we need more complex loaders to read
   multiple rows. If the schema is separate from the sheet, then the
   loader doesn't interact with the source of data.

#. Each row is modeled as a simple dictionary in this example code.

#. A filter locates rows that have hull numbers. Other rows are quietly
   discarded.

#. The take_until() function reads rows until the matching row is found,
   then stops. This chops off the bottom of the spreadsheet where manual
   notes were kept.


The resulting list of rows can be validated, cleansed, and normalized
to create the useful instances of the various Model subclasses.


Here's the "transform" portion.


::

      def make_owner_1(row: Dict[str, Cell]) -> Owner:
          return Owner(
              last_name=null_strip(row["Owner's Last Name"].to_str()),
              first_name=null_strip(row["Owner's First Name"].to_str()),
              display_name=null_strip(row["Display Name"].to_str()),
              website=null_strip(row["Website"].to_str()),
              owner_vessel=[],
          )


We've built an instance of the Owner subclass of Model by extracting
a number of attributes from the row. There are other columns not
extracted; they are part of various normalizations and dereferencing.
The owner_vessel attribute is a parent-child relationship that can't
be trivially populated from the row. The SQL folks would include a
foreign key in each child that refers to the parent. The vessel page
of the spreadsheet has this information, and it's used to populate
the owner's details. This is one of the dereferencing activities that
needs to be done as part of "loading".

The to_str() method is feature of the Stingray Reader's cell
definitions. Conversion methods like this are not typical of
idiomatic Python code. If we were only creating built-in str, float,
or int, the bunch of conversion methods would be A Bad Idea. To be
useful, we also need to create Decimal objects, and that leads us to
embracing a grid of conversion methods for each cell source to
desired resulting objects. We could use decimal(str(cell)), but it
seems cleaner to use cell.to_decimal().

Multiple Passes
----------------

We often touch the source more than once.

#.  There's a "validate and load" pass to get rows that are sensible
    to process. A generator might make sense here.

#.  There may be a "cleanse and convert" pass to reformat the source
      data, perhaps parsing complex cells into components or combining
      multiple source rows into a single entity description. This, too,
      might involve a generator to restructure the spreadsheet rows into
      something sensible.

#.  There will be multiple "normalization" passes. Any 2NF
    relationships need to be extracted to create model objects. Any
    restructuring of complex dimensions should be handled via
    restructuring source data from grid to rows, or from multiple
    sheets to a single, long, sequence of rows with the various
    dimensions as explicit attributes of each row.

#.  There may be multiple "load" passes to build final objects from
    the source rows. This will often lead to including the built
    objects as part of the source data.

#.  There will be some final "dereferencing" passes where foreign key
    relationships are turned into proper references among the objects.
    These should be weakref references to permit proper garbage
    collection.


At this point, the application will have tidy collections of
Python objects that can be used for the real work.

What's essential is finding a balance between end-user
visualization of the data in a spreadsheet and schema validation
in Python. It's often helpful to be flexible when trying to
automate processing of complex, irregular, manually gathered data.
Letting candidate users work with spreadsheets lowers the barrier
to automation.

Coping with irregularity gets the process started.

As the work matures, some schema controls will tend to evolve.
People tend to recognize the cost and complexity of irregular
data. They will try to identify the patterns and impose some order
on those patterns. As they uncover patterns in the data, the
"schema" will evolve. This is a good thing, and Python lets this
proceed at a human pace.

We can -- easily-- create flexible tools that let people
understand and organize their data.





