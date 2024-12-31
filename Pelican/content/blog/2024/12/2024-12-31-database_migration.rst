Database Migration, Part I
###########################

:date: 2024-12-31 13:21
:tags: #python,database,sql
:slug: 2024-12-31_database_migration_part_i
:category: Python
:status: published

Let's talk about extracting data from complex relational databases.
This is -- in a way -- another case study for my Unlearning SQL book.

..  sidebar::

    -   KDP
        https://www.amazon.com/dp/B0DDMFMXNW

    -   Lulu
        https://www.lulu.com/shop/steven-lott/unlearning-sql/paperback/product-yvnm8zn.html?page=1&pageSize=4

    -   Google Play
        https://play.google.com/store/books/details?id=23WAEAAAQBAJ

    -   Apple Books
        https://books.apple.com/us/book/unlearning-sql/id6443164060


This case study is about legacy database preservation: we want the data.
We don't want the code.

Let's reach back 20 years, when packages like Joomla! were -- essentially -- the only way to have interactive, peer-maintained content.
Facebook barely existed before 2005.
Yahoo! Groups was what we had been using to share information as a kind of "social media" up until 2008, when the Joomla! site was started.

We have web content reaching back almost two decades, most of it in a Jooma! database.
Some of the Joomla! articles are extracts stretching from the Yahoo! groups.
Currently, the user base interacts through Facebook, rarely touching this complicated web content.

We want to preserve what's in Joomla! and migrate it into a simpler publishing system like Hugo (https://gohugo.io)
We intend to sacrifice some of the Kunena features. However. Since no one is interacting via the Kunena forums, this isn't a real sacrifice.

Let's work through the conversion of data from a relational database to a directory of Markdown files.
One stumbling step at a time.

Stumble 1: What do we have?
===========================

We have a snopshot of the database. It's MariaDB/MySQL, and the snapshot is a big SQL script.
We can install MariaDB on our laptop and run the script.

We have the data.

What do we have?

The Joomla! PHP world has a bunch of admin apps and tools to peek at the database.
We're not interested in these because they run on the server, which we'd like to disconnect from.

First, we have tables
::

        SELECT TABLE_NAME, TABLE_ROWS
        FROM   information_schema.TABLES
        WHERE  TABLE_SCHEMA = "testdb"
        AND    TABLE_TYPE = "BASE TABLE"

We can extract some details and helps us discover the Joomla! naming convention.
There's a prefix in front of each table name. ``j930_`` and ``jos_`` seem to be prefixes used
by previous admins to preserve some data for a test instance (or something.)
While we don't **know** this, the overlapping names and smaller (or zero) row counts suggest these don't matter.
It's the ``j500_`` tables that matter.

It's best to fuss about with this initial peeking in a notebook, just uncover the metadata, and see what's going on.

Plan to abandon the notebook.

Here's how we prefer to deal with the schama

::

    @dataclass
    class Table:
        name: str
        num_rows: int | None = field(default=None)
        columns: dict[str, Column] = field(default_factory=dict)

        query: ClassVar[str] = """
            SELECT TABLE_NAME, TABLE_ROWS
            FROM   information_schema.TABLES
            WHERE  TABLE_SCHEMA = "testdb"
            AND    TABLE_TYPE = "BASE TABLE"
        """

        @classmethod
        def from_query(cls, row: tuple[Any, ...]) -> "Table":
            return Table(name=row[0], num_rows=row[1])

A reusable function can execute the query, and then use the ``from_query()`` method
to build rows of the ``Table`` class.

The column metadata is a separate dataclass::

    @dataclass
    class Column:
        name: str
        type_name: str
        size: int
        python_type: str | None
        optionality_type: OptionalityType
        domain_type: DomainType | None = field(default=None)
        not_used: bool = field(default=False)
        val_min: Any = field(default=None)
        val_max: Any = field(default=None)
        val_common: list[tuple[Any, int]] = field(default_factory=list)
        val_cardinality: int = field(default=0)

        query: ClassVar[str] = """
            SELECT COLUMN_NAME, IS_NULLABLE, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = "testdb"
            AND   TABLE_NAME = ?
        """

        @classmethod
        def from_query(cls, row: tuple[Any, ...]) -> "Column":
            assert row[2].upper() in PYTHON_TYPE, f"unknown type {row[2]}"
            return Column(
                name=row[0],
                type_name=row[2],
                size=row[3],
                python_type=PYTHON_TYPE.get(row[2].upper()),
                optionality_type=(
                    OptionalityType.REQUIRED if row[1] == "NO" else OptionalityType.OPTIONAL
                ),
            )

The various ``val_...`` attributes are populated later.
We need to query the data to get the minimum value, maximum value, the five most common values, and a general sense of the overall cardinality (is each value unique?)

We can see what the columns mean when we see sample data.

We'll do this with methods that are part of the ``Table`` dataclass.


::

        def rows(self, connection: mariadb.Connection) -> Iterator[dict[str, Any]]:
            query = f"""SELECT * FROM {self.name}"""
            with connection.cursor() as c:
                c.execute(query)
                column_names = [col[0] for col in c.description]
                for rt in c.fetchall():
                    row_dict = dict(zip(column_names, rt))
                    yield row_dict

        def set_domain(self, connection: mariadb.Connection) -> None:
            raw_domains = collections.defaultdict(collections.Counter)
            for row in self.rows(connection):
                for name in self.columns.keys():
                    raw_domains[name][row[name]] += 1
            for name, col in self.columns.items():
                col.set_domain(raw_domains[name])

These were not shown above to keep the initial definition of ``Table`` clear.

The ``set_domain()`` method for a ``Table`` gets all of the data, and then -- column by column -- sets the data domain for the column.
For vast tables, these has to be approached in a different.
For this databsae, with under 10,000 rows in any given table, fetching all the rows works out quite nicely.

This relies on a ``set_domain()`` method for the ``Column`` class. Like this:

::

        def set_domain(self, frequencies: collections.Counter[Any]) -> None:
            values = list(filter(None, frequencies.keys()))
            if values:
                self.val_min = min(values)
                self.val_max = max(values)
                self.val_common = frequencies.most_common(5)
                self.val_cardinality = len(frequencies)
                if all(f == 1 for val, f in frequencies.items() if val is not None):
                    self.domain_type = DomainType.UNIQUE
                else:
                    self.domain_type = DomainType.NON_UNIQUE
            else:
                self.not_used = True

There are two enum class definitions that are part of this, also.

::

    class DomainType(StrEnum):
        UNIQUE = "unique"
        NON_UNIQUE = "non-unique"


    class OptionalityType(StrEnum):
        OPTIONAL = "nullable"
        REQUIRED = "non-nullable"

With this, we can build a schema -- a collection of ``Table`` definitions -- from the database.
We can then view the beast as a whole.

Which means what?

How do we Explore?
====================

Step 1 is to build some ERD diagrams.

We can add a method to ``Table`` to expose it as a Plant UML entity:

::

        def as_puml(self) -> str:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                print(f"entity {self.name} {{ /' {self.num_rows} rows '/")
                for col in (c for c in self.columns.values() if not c.not_used):
                    flag = (
                        "* "
                        if col.domain_type == DomainType.UNIQUE
                        and col.optionality_type == OptionalityType.REQUIRED
                        else ""
                    )
                    print(
                        f"  {flag}{col.name} {col.type_name}({col.size}) /' {col.optionality_type}, {col.domain_type}, range {col.value_range}, {col.value_common} '/"
                    )
                print("}")
            return buffer.getvalue()

The output is a block of text like this:

::

    entity j500_assets { /' 1239 rows '/
      * id INT(4) /' non-nullable, unique, range 1..1334, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), ... 1234 more] '/
      parent_id INT(4) <<FK>> /' non-nullable, non-unique, range 1..941, [(895, 361), (699, 51), (478, 49), (1, 42), (35, 38), ... 117 more] '/
      --
      lft INT(4) /' non-nullable, non-unique, range 1..2475, [(1, 2), (3, 1), (9, 1), (11, 1), (13, 1), ... 1233 more] '/
      rgt INT(4) /' non-nullable, unique, range 2..2477, [(2477, 1), (2, 1), (8, 1), (10, 1), (12, 1), ... 1234 more] '/
      level INT(4) /' non-nullable, non-unique, range 1..5, [(4, 766), (3, 254), (2, 90), (5, 85), (1, 43), ... 1 more] '/
      name VARMYSQL(200) /' non-nullable, unique, range 'com_actionlogs'..'root.1', [('root.1', 1), ('com_admin', 1), ('com_banners', 1), ('com_cache', 1), ('com_checkin', 1), ... 1234 more] '/
      title VARMYSQL(400) /' non-nullable, non-unique, range 'Ar n-Inin (Hull #331)'..'vtest1', [('Uncategorised', 7), ('Whitby42 #172 [...]', 5), ('General', 3), ('Introduction', 3), ('2008 Rendezvous', 3), ... 1170 more] '/
      rules VARMYSQL(20480) /' non-nullable, non-unique, range '{"core.admin":[],"core.mana...'..'{}', [('{}', 544), ('None', 348), ('{"core.delete":{"...', 81), ('{"core.delete":[]...', 74), ('{"core.delete":[]...', 65), ... 25 more] '/
    }
    note bottom: 1239 rows

This isn't too pretty, but when the PlantUML tool finishes with it, it's a tidy little box in an ERD.
The long ``/'...'/`` comments are not shown in the diagram.
They're helpful in the file because they show us the domain of values in a column.

Once we have all of the entities in a ``.puml`` file, we can insert relationships.
We can also partition the tables into packages to try and discern which ones have interesting content, and
which ones are operational overheads.

What We Didn't Do
=================

An important part of this is to **not** -- emphatically **not** -- build an ORM layer.
We don't really want to try and get ORM class definitions wrapped around a legacy database.
It's technically possible.
The tables are small, so there may not be profound performance problems.

It's much, much easier to extract that data from the database, and build native Python objects.

What We Will Do
===============

The goal is to have a ``db_model`` module with **Pydantic** ``BaseModel`` definitions for the tables we want to preserve.
As we'll see in the next section, we can query the database and populate the **Pydantic** class definitions.
We can then dump these Python objects into NDJSON files so we can explore without the overheaeds of SQL or MariaDB.

The relational model -- and the requirement to normalize -- has decomposed relatively straight-forward
objects into a table of tables with primary keys, foreign keys, and equijoin operations.
We want to undo the normalization and recreate a more sensible structure in native Python.
We really want to have nested ``for`` statements without have to create cursors and execute queries.

We want to be able to create dictionaries without the overhead of defining an index.

The Database Model
===================

The starting position is some **Pydantic** class definitions for the database tables.
This is another method of the ``Table`` class.

::

        def as_dataclass(self) -> str:
            """Actually, as pydantic DBModel subclass..."""
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                column_subset = [c for c in self.columns.values() if not c.not_used]
                keys = set(
                    col.name
                    for col in column_subset
                    if col.domain_type == DomainType.UNIQUE
                    and col.optionality_type == OptionalityType.REQUIRED
                )
                print(f"class {self.class_name}(DBModel):")
                print('    """')
                print(f"    {self.num_rows} rows")
                print('    """')
                for col in column_subset:
                    annotation = (
                        f"{col.python_type}"
                        if col.optionality_type == OptionalityType.REQUIRED
                        else f"{col.python_type} | None"
                    )
                    key = "<<PK>> " if col.name in keys else ""
                    print(
                        f"    {col.name}: {annotation}  # {key}range {col.value_range}, in {col.value_common}"
                    )
                wrapped_names = [f"`{col.name}`" for col in column_subset]
                print()
                print('    query: ClassVar[str] = """')
                print(f"        SELECT {', '.join(wrapped_names)}")
                print(f"          FROM {self.name}")
                print('    """')
                print()
                print("    @classmethod")
                print(
                    f"    def from_query(cls, row: tuple[Any, ...]) -> '{self.class_name}':"
                )
                print(f"        return {self.class_name}(")
                for position, col in enumerate(column_subset):
                    print(f"            {col.name}=row[{position}],")
                print("        )")
            return buffer.getvalue()

It writes the definition as Python code.
We can assemble a ``db_model`` class from these.
Once we have that we're in a position to extract the data and build NDJSON files.

This first part, then, is an application with a name like ``scan_db.py`` to emit the UML,
and the db_model.

We draw a line under this module because it deals with the available metadata.
It doesn't do the full extract.
Nor does it explore the data prior to migration.
The database metadata analysis is something we'd like to isolate, and run rarely.

Unit Testing
=============

While -- in principle -- this is one-0ff software, test cases are essential.
We don't need 100% code or logical path coverage.
But, we do need enough coverage that we can refactor with confidence.

Documentation
=============

The PUML files document the source database.

We should create a ``docs`` directory and put some notes in there about what this is and how to use it.

Next
====

So far, we have a sense of what the data is.

We've fiddled with the PUML file(s) to create ERD's that seem to capture our initial understandings.

We've goa ``db_model.py`` file full of class definitions we can use for further work.

We can write a database extract (and database reloader) to work with the NDJSON extracts.
Then we can kiss MariaDB goodbye, and stop the service from running on our laptop.
