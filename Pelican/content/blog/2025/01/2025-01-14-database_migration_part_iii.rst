Database Migration, Part III
############################

:date: 2025-01-14 07:21
:tags: #python,database,sql
:slug: 2025-01-14_database_migration_part_iii
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
In `Part II <{filename}/blog/2025/01/2025-01-07-database_migration_part_ii.rst>`_, we extracted the raw tables and loaded up a TAR Archive with NDJSON documents.

We can now move beyond the raw relational data into something more useful.

Things SQL Does Badly
=====================

One thing SQL does badly is model hierarchies. (This is one aspect of not handling graphs in general.)

In a hierarchy -- a Directed Acyclic Graph -- there are nodes. A node may have a parent.
A mode may have one or more children.
A node with no parent is the "root" of the tree.
A node with no children is a "leaf" of the tree.

..  figure:: {static}/media/tree_model.png
    :alt: Diagram of a tree.

    A tree

The point is that the relationships are transitive -- the root has children that have children dot dot dot that have leaves.
No arbitrary ``<h1>`` to ``<h6>`` limit.
(Pragmatically, you don't *need* very many levels.
Common SQL hacks impose limits to so a simple ``SELECT`` statement and a programming languages like ``COBOL`` will work.
The ``WITH`` clause permits indefinite hierarchies, at the cost of consuming time querying the rows from the database.)

Not Using SQL
=============

In ordinary, in-memory data structures, it makes sense to define tree structures like this:

::

    from pydantic import BaseModel, Field, Json, WrapValidator

    class AppModel(BaseModel, from_attributes=True, arbitrary_types_allowed=True):
        @property
        def pk(self) -> int:
            raise NotImplementedError()

        def __str__(self) -> str:
            base = super().__str__()
            return f"{self.__class__.__name__} {base}"

    class Assets(AppModel):
        """
        1239 rows
        """

        @property
        def pk(self) -> int:
            return self.id

        id: int  # <<PK>> range 1..1334, in [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), ... 1234 more]
        parent_id: int  # range 1..941, in [(895, 361), (699, 51), (478, 49), (1, 42), (35, 38), ... 117 more]
        lft: int  # range 1..2475, in [(1, 2), (3, 1), (9, 1), (11, 1), (13, 1), ... 1233 more]
        rgt: int  # <<unique>> range 2..2477, in [(2477, 1), (2, 1), (8, 1), (10, 1), (12, 1), ... 1234 more]
        level: int  # range 1..5, in [(4, 766), (3, 254), (2, 90), (5, 85), (1, 43), ... 1 more]
        name: str  # <<unique>> range 'com_actionlogs'..'root.1', in [('root.1', 1), ('com_admin', 1), ('com_banners', 1), ('com_cache', 1), ('com_checkin', 1), ... 1234 more]
        title: str  # range 'Ar n-Inin (Hull #331)'..'vtest1', in [('Uncategorised', 7), ('Whitby42 #172 [...]', 5), ('General', 3), ('Introduction', 3), ('2008 Rendezvous', 3), ... 1170 more]
        rules: str  # range '{"core.admin":[],"core.mana...'..'{}', in [('{}', 544), ('None', 348), ('{"core.delete":{"...', 81), ('{"core.delete":[]...', 74), ('{"core.delete":[]...', 65), ... 25 more]

        children: list["Assets"] = Field(default_factory=list, repr=False)
        parent: ref["Assets"] | None = Field(default=None, repr=False)
        gallery_catgs: list["Joomgallery_Catg"] = Field(default_factory=list, repr=False)
        galleries: list["Joomgallery"] = Field(default_factory=list, repr=False)
        categories: list["Categories"] = Field(default_factory=list, repr=False)
        content: list["Content"] = Field(default_factory=list, repr=False)
        modules: list["Modules"] = Field(default_factory=list, repr=False)

An ``Assets`` instance has ``children: list["Assets"]``.
Similarly, an ``Assets`` instance may have a weak reference to a parent, ``ref["Assets"] | None``.

It's a weak reference because two mutual references -- parent -> child and child -> parent -- will create a circularity that defeats reference counting.
Using weak references adds a bit of fussiness, but otherwise leads to objects that play well with others.

Some of these fields are nonsense. The rest describe the asset tree used by Joomla!

Having an explicit ``children`` list attached to each ``Assets`` saves going back to the database to do additional queries to find the children of a given asset.
Further, it makes it very easy to "walk" the transitive closure of all children under an asset.
And, it makes it very easy to locate the transitive closure of all parents of an asset.

How Do We Get There?
====================

Building the the ``model`` objects is a two-step process.

Step, the first
----------------

Most of the attributes are seeded from ``db_model`` objects using a line like the following:

::

                obj = Assets.model_validate(row)

The ``model_validate()`` moves data into a new instance of the  ``Assets`` model.
The ``from_attributes=True`` means attribute name matching is used; this means our ``AppModel`` classes must have attribute names that match the ``DBModel`` classes.
These have have attribute names that match the original SQL.
We have a reasonably transparent mapping because of this constraint.

Step, the second
----------------

The relationships don't resolve themselves.

We need to attach children to parents and parents to children.
For this, we've defined a ``Builder`` class.

::

    class AssetsBuilder(AppModelBuilder):
        """
        @startuml
        hide circle
        skinparam linetype ortho

        entity Assets
        Assets }o-- "parent" Assets
        @enduml
        """

        class AppTable(model.AppTable[model.Assets]):
            pass

        def __call__(self, table: DBTable) -> model.AppTable[model.Assets]:
            items = self.AppTable.build(model.Assets, table)
            for item in items.values():
                if item.parent_id in items:
                    items[item.parent_id].add_child(item)
            return items

In SQL world, every ``Assets`` row has a ``parent_id`` column with a foreign key reference to another ``Assets``.
Or a null of some kind, maybe a database ``NULL``, maybe a zero.

(There is **not** one standard answer to null representation.
Don't ``@`` me with it **should** be ``NULL``.
In this case, it isn't ``NULL``, and it doesn't have to be a ``NULL``.
It's usually zero. Except in one case that seems to be the result of a bug of some kind.)

(We'll look at the ``AppTable.build`` later, for now I want to focus on the hierarchies.)

For each ``Assets`` object in ``items.values()``, we need to see if it has a parent.
If it does have a parent, we need to as the parent to add this child.
This will do two things: add the child to the parent's ``children`` list, and **also** set the parent relationship for each of the children.

::

    def add_child(self, item: "Assets") -> None:
        self.children.append(item)
        item.parent = ref(self)

The ``AppTable`` class
======================

The final step in the ``Builder`` is a the ``AppTable``; a handy structure to manage each collection of objects.

In the long run, this is not required.

In the short run -- where we can't navigate the database -- it's really handy for exploring.

::

    T_AppModel = TypeVar("T_AppModel")


    class AppTable[T_AppModel: AppModel](dict[Any, T_AppModel]):
        """
        A mapping from PK id to AppModel instance.
        """

        logger: ClassVar[logging.Logger]

        @classmethod
        def build(
            cls, row_cls: type[T_AppModel], db_table: Iterable[BaseModel]
        ) -> "AppTable[T_AppModel]":
            cls.logger = logging.getLogger(cls.__name__)
            app_table = AppTable[T_AppModel]()
            for row in db_table:
                obj = row_cls.model_validate(row, from_attributes=True)
                if obj.pk in app_table:
                    cls.logger.error(
                        "Duplicate key %r, replacing %r", row, app_table[obj.pk]
                    )
                app_table[obj.pk] = obj
            return app_table

        def where(
            self, filter_function: Callable[[T_AppModel], bool]
        ) -> Iterator[T_AppModel]:
            """
            A vaguely SQL-like search.
            """
            yield from filter(filter_function, self.values())

This is where we build a ``model.Assets`` object from the database ``db_model.Assets`` object.
Further, we index them by the stated PK so we don't **need** to search.

The ``where()`` method lets us provide a ``lambda`` that searches the rows for matching instances.

::

    featured = list(self.content.Content.where(lambda c: c.featured == 1))

This is equivalent to ``SELECT * FROM content WHERE featured = 1`` in SQL.
Except it's a lot faster.
And a lot more flexible.

This is not **heavily** used.
Most of what we need, we can find with ordinary foreign-key-to-primary-key relationships that use the native Python mappings.
A few things, like specific assets that define Joomla! modules and content categories, must be found by name, and will use the ``where()`` method.

All the Things
==============

Now that we can unravel the parent-child hierarchies, we can prepare the database for real work.

We'll transform the original SQL-like structures to a module-like namespace
that has all the things we want, with their proper relationships.
There are 18 tables that seem to have all the content we care about.
For now, we're avoiding some of the installed Joomla! extensions.

::

    def prepare_content(database: Database) -> SimpleNamespace:
        content = SimpleNamespace()

        content.Phocadownload_Categories = PhocaCategoryBuilder(content)(
            database["Phocadownload_Categories"]
        )
        content.Phocadownload = PhocaDownloadBuilder(content)(database["Phocadownload"])

        content.Kunena_Categories = KCategoryBuilder(content)(database["Kunena_Categories"])
        content.Kunena_Topics = KTopicBuilder(content)(database["Kunena_Topics"])
        content.Kunena_Messages = KMessageBuilder(content)(database["Kunena_Messages"])
        content.Kunena_Messages_Text = KMessageTextBuilder(content)(
            database["Kunena_Messages_Text"]
        )
        content.Kunena_Attachments = KAttachmentBuilder(content)(
            database["Kunena_Attachments"]
        )

        content.Assets = AssetsBuilder(content)(database["Assets"])

        content.Rsgallery2_Galleries = RSGalleryBuilder(content)(
            database["Rsgallery2_Galleries"]
        )
        content.Rsgallery2_Files = RSFileBuilder(content)(database["Rsgallery2_Files"])

        content.Joomgallery_Catg = JGCatgBuilder(content)(database["Joomgallery_Catg"])
        content.Joomgallery = JGalleryBuilder(content)(database["Joomgallery"])

        content.Categories = CategoriesBuilder(content)(database["Categories"])
        content.Content = ContentBuilder(content)(database["Content"])

        content.Modules = ModulesBuilder(content)(database["Modules"])
        content.Menu = MenuBuilder(content)(database["Menu"])
        content.Weblinks = WeblinksBuilder(content)(database["Weblinks"])

        # The following are of dubious value...
        content.Modules_Menu = ModulesMenuAssoc(content)(database["Modules_Menu"])
        content.Content_Frontpage = ContentFPBuilder(content)(database["Content_Frontpage"])

        return content

Each ``Builder`` applies several transformative steps:

1. Build ``model`` objects from ``db_model`` objects for the relevant few ``DBTable`` objects.

2. Make ``AppTable`` dictionaries from ``object.pk`` to ``object``.

3. Make trees for objects with parent-child relationships.

4. Resolve other inter-object references.


Next
=====

Once we've got a proper namespace full of objects, we can start to explore it to find the relevant pieces.

Are are the lines we've drawn to distinguish the various parts of our processing.

1. scan_db.py -- extracts the table definitions and PlantUML descriptions from the database.

2. extract_db.py -- extracts the data, writing a TAR file of NDJSON documents with all the database rows.

3. view_content.py -- ``Builder`` classes and ``prepare_content()`` function to get raw data organized.

The steps in ``view_content`` are free of SQL complications.

In the next section we'll look at the conversion process.

There will be three parts:

1.  Locate the relevant objects

2.  Convert the objects for use by a static site generator like Hugo. This turns out to be pretty complicated. However, since we're done with SQL, the complications don't involve database queries.

3.  Write needed ``_index.md`` files the mimic the legacy site's Joomla! presentation.
