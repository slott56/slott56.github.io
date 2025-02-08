Database Migration, Part II
###########################

:date: 2025-01-07 13:21
:tags: #python,database,sql
:slug: 2025-01-07_database_migration_part_ii
:category: Python
:status: published

We're talking about extracting data from complex relational databases.
This is -- in a way -- another case study for my *Unlearning SQL* book.

..  sidebar:: *Unlearning SQL*

    KDP https://www.amazon.com/dp/B0DDMFMXNW

    Lulu https://www.lulu.com/shop/steven-lott/unlearning-sql/paperback/product-yvnm8zn.html?page=1&pageSize=4

    Google Play https://play.google.com/store/books/details?id=23WAEAAAQBAJ

    Apple Books https://books.apple.com/us/book/unlearning-sql/id6443164060

In `Part I <{filename}/blog/2024/12/2024-12-31-database_migration.rst>`_, we loaded a database and queried the metadata.
From this we created Python ``Table`` and ``Column`` objects that we used to record what we know about the data.
These class could also emit metadata in other formats.
The other formats include

-   `PlantUML <https://plantuml.com>`_ ERD diagrams.

-   `Pydantic <https://docs.pydantic.dev/latest/>`_ class definitions.

So far, these have given us a sense of what the data is.

We've fiddled with the PUML file(s) to create ERD's that seem to capture our initial understandings.

We've got a ``db_model.py`` file full of class definitions we can use for further work.

Stumble 2, Extract
===================

We can write a database extract (and database reloader) to work with the NDJSON extracts.
Then we can kiss MariaDB goodbye, and stop the service from running on our laptop.

The database metadata includes a lot of tables. We don't want all of them.
It's hard to be sure **exactly** which ones we need, so it pays to be flexible.

What makes sense to me is creating a list of relevant tables in the ``scan_db.py`` application.
Then we can run it as often as we uncover another table that seems relevant.

The extract can use a function like this to find the tables in the ``db_model`` module.

::

    def class_iter(module: ModuleType) -> Iterator[type]:
        other_imported_names = {
            "Decimal",
            "ClassVar",
            "Any",
            "BaseModel",
            "Field",
            "DBModel",
            "__class__",  # SimpleNamespace
        }
        for name in dir(module):
            object = getattr(module, name)
            match object:
                case typing._AnyMeta():  # type: ignore
                    pass
                case type() if name not in other_imported_names:
                    print("DEBUG", name)
                    yield object

This yields the class definitions.
Here's the entire list of classes in the module.

::

    classes = list(class_iter(db_model))

Since each of our classes has a query and a ``from_query()`` method,
getting the data for a given table looks like this:

::

    def get_data(
        connection: mariadb.Connection, cls: type[db_model.DBModel]
    ) -> list[db_model.DBModel]:
        try:
            with connection.cursor() as crsr:
                crsr.execute(cls.query)
                data = [cls.from_query(row) for row in crsr.fetchall()]
                # pprint.pprint(data)
                return data
            print(cls.__name__, len(data))
        except AttributeError:
            print(f"***UNEXPECTED {cls.__name__}")
            # print(cls.query)
            raise

Execute the table's query. Convert the table's rows to the **pydantic** model instances.
Return the list of instances.

Producing an line in an NDJSON file is delightfully simple with Pydantic.

::

        row.model_dump_json(indent=None)

While we can easily make a bunch of NDJSON files, it offends me to have a whole directory full of files that we're only going to read.

Stumble 3, The Working Files
=============================

My first preference was to pickle the data.
It's easy to create a dictionary that maps table name to  a list of row instances.

We have a common base class

::

    class DBModel(BaseModel):
        query: ClassVar[str]

        @classmethod
        def from_query(cls, row: tuple[Any, ...]) -> "DBModel":
            raise NotImplementedError()

This means the database is

::

    type Database = map[str, list[DBModel]]

We can pickle this mapping and recover the entire thing.

It's really quite elegant. And pretty fast, too.

Big Problem
-----------

There's a big problem.

The data is essentially wired to specific class definitions.
Change the class too much, and the data no longer loads from the pickle.

Since this is exploratory, we won't know anything up front.
We need more flexibility.


Course Correction
=================

Pickle didn't work. What's next?

Make a TAR Archive (compressed) with all the NDJSON members.
The extra CPU of compression is more than offset by the reduced time to do physical I/O on a smaller file.

Here's the TAR write::

    def save_data(
        content_path: Path,
        archive: tarfile.TarFile,
        cls: type[db_model.DBModel],
        data: list[db_model.DBModel],
    ) -> None:
        detail = (content_path / cls.__name__).with_suffix(".ndjson")
        with open(detail, "w") as detail_file:
            for row in data:
                print(row.model_dump_json(indent=None), file=detail_file)
        info = archive.gettarinfo(detail, arcname=cls.__name__)
        print(info.name, info.size)
        with open(detail, "rb") as detail_file:
            archive.addfile(info, detail_file)
        detail.unlink()

The idea is to write a table of data to a file at the ``detail`` path, add this to the open TAR archive, and then delete the ``detail`` entry.
This leaves us with a TAR file filled with the extracted database rows.
Further, it's in JSON notation, so we can fiddle with the schema.

The original SQL backup was 167,885,194 bytes.

The useful subset of data, compressed, is 28,815,360 bytes. 17% of the original. About 1/5 the size.

Simply rebuilding the original db_model collections goes quickly.
And I can make small changes without breaking things.

It turns out, I don't want to make **small** changes.

The Raw Database Model
=======================

The real model is derived from the class definitions in the  ``db_model``  module.
I don't need the SQL query.  Or the ``from_query()`` method.
The ``db_model`` module is full of classes that have these features, but doesn't need them.

To move on in the data pipeline, I need to reload data using ``db_model`` class definitions.
Later, we'll start transforming this data as we undo the mischief of normalization.
Loading the data for exploration is done by this function:

::

    def load_db(source_path: Path) -> Database:
        logger = logging.getLogger("load_db")
        database: Database = {}

        with tarfile.open(source_path, "r") as archive:
            for item in archive.getmembers():
                cls = getattr(db_model, item.name)
                raw_file = archive.extractfile(item)
                if raw_file:
                    reader = io.TextIOWrapper(raw_file)
                    rows = DBTable(cls.model_validate_json(line) for line in reader)
                    database[item.name] = rows
                else:
                    logger.error("archive item %r as no content", item)
        return database

I can read and validate the NDJSON documents with the following generator expression.

::

    (cls.model_validate_json(line) for line in reader)

We can use the **Pydantic** ``model_validate_json()`` method to create my target object.
I can now adjust attribute definitions in a limited way, and add new attributes.

First, however, we need to take a look at the ``DBTable`` class.

The DBTable Collection
======================

For the purposes of reading the db tables back in from the TAR archive,
we have these two definitions:

::

    class DBTable(list[db_model.DBModel]):
        pass


    type Database = dict[str, DBTable]

Yes, ``DBTable`` is a ``list``. It could do more. It turns out, nothing more is needed.

Next
=====

Once we've got a dictionary full of lists of data, we need to restructure it into a more useful form.
This means drawing some more lines to distinguish the various parts of our processing.

1. scan_db.py -- extracts the table definitions and PlantUML descriptions from the database.

2. extract_db.py -- extracts the data, writing a TAR file of NDJSON documents with all the database rows.

Reading and "preparing" the data for deeper analysis is a separate application.

It took a few mistakes to learn that the ``db_model`` schema **must** match the database.
We really can't tweak it.
We need to build a model derived from this model.

In the next section we'll define the ``model.AppModel`` class for objects derived from the ``db_table.DBModel`` objects.
These ``AppModel`` classes can have a number of additional fields and distinct annotated types and validation rules.
This makes it easy to build them using a line like the following:

::

                obj = row_cls.model_validate(row, from_attributes=True)

the ``model_validate()`` moves data into the ``row_cls`` model. The ``from_attributes=True`` means attribute name matching is used.
This means our ``AppModel`` classes must have attribute names that match the ``DBModel`` classes.
These have have attribute names that match the original SQL.
We have a reasonably transparent mapping because of this constraint.
