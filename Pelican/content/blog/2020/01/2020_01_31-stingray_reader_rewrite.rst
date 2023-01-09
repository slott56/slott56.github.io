Stingray Reader Rewrite
=======================

:date: 2020-01-31 10:39
:tags: stingray reader,#python,type hints
:slug: 2020_01_31-stingray_reader_rewrite
:category: Technologies
:status: published

See
https://slott-softwarearchitect.blogspot.com/2020/01/stingrayreader-upgrade.html


This drifted into some serious rethinking of bad design decisions.
(If someone else did this, I'd call it weak, and suggest
improvements. It was me. It was bad. I'm a bad programmer and I feel
bad about it.)


An an example, there's this sketchy construct:


::

      some_data = {name: source[name] for name in the_names}
      the_object = SomeClass(**some_data)


The some_data dictionary could be called Dict[str, Any], but that's
unhelpful for letting **mypy** check the consistency of data
structures. This is what was required:


::

        FullAttr = TypedDict("FullAttr",
            {
                "name": str,
                "offset": int,
                "size": int,
                "type": str,
                "create": Cell,
            },
            total=False
        )


This dictionary changes -- profoundly -- the relationship between
classes. The FullAttr type gives us an intermediary representation.
The SomeClass hierarchy has a flexible collection of attributes. We
can use this to uncouple some parsing operations from object factory
operations, using this minimal subset of definitions as a kind of
bridge between modules, both of which can be fully type-checked, but
still permit Python's duck-type flexibility.

It Got Worse
-------------

Adding type hints to Stingray Reader required navigating some shoal
water created by a poor set of dependency decisions.

The original, vague, concept was to have a Schema and Attribute
definition that could be shared by all the various readers. A schema
contains a number of attributes. Ideally, an attribute can be defined
by a sub-schema. This is how JSONSchema and XSD work.

But.

The Stingray Reader reads Workbooks with an extension to read COBOL.

There are a bunch of extensions required.

-   The schema is loaded by a COBOL parser.

-   The physical file formats require the possibility of EBCDIC -> Unicode conversion.

-   Unlike ordinary workbooks, the record layouts have to be built
    lazily. An ordinary workbook row is complete. Some physical
    formats elide empty cells, but they're easy to replace with an
    explicit empty cell. COBOL has a REDEFINES clause that means we
    can't even attempt to parse the bytes for a row until they're
    required by the app. There's no way -- from the data definition
    alone -- to discern which of the redefines options will have valid
    data. There's more, but you get the idea: COBOL is kind of
    complex.


Versions 1 to 4 had a dumb-as-a-bag-of-hammers problem.

The Schema and Attribute definitions where extended to depend on
COBOL implementation details.

It works nicely because of duck typing and late binding of types.
Python's type hinting exposes the grotesque consequences of this
dependency.

We tried several ways of reordering a bunch of definitions to remove
forward type references. It took almost an hour to realize the
circularity could not be removed trivially because of a circularity.
Two Attribute subclasses depended on COBOL features. And the COBOL
features had weakref references back to their Attributes.

Crushing everything into a single, large module, worked to ease the
complications or circularity. But the essential interdependence needs
to be expunged.

What has to happen next is to invert the relationship between
Attributes and COBOL details. This means two changes:

#.  Extending the Attribute class hierarchy to contain just enough
    information to cover the COBOL complications.

#.  Changing the function that builds an Attribute definition from the
    COBOL source so it copies details into the Attribute. The COBOL
    detail needs to be little more than the description of the
    property.

This isn't easy. But. 187 test cases and a TOX setup makes it a
reasonable effort.

And.

I can finally look seriously at converting between JSON Schema and
COBOL.





