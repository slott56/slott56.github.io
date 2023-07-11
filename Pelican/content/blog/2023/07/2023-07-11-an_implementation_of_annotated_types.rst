An Implementation of Annotated Types
##############################################

:date: 2023-07-11 09:00
:tags: patterns,python,type-hints
:slug: 2023-07-11-an_implementation_of_annotated_types
:category: Technologies
:status: published

The ``typing`` module includes the mysterious-looking ``Annotated`` type hint.
See https://docs.python.org/3/library/typing.html#typing.Annotated for details.

`What does this do?`_

`Why do I need it?`_

`Where can I see examples?`_

What does this do?
==================

The ``Annotated`` type hint lets us append "details" to a type.

It might look like this

::

    x: Annotated[int, MustBePrime()]

The annotated type has one origin type (which must be first) and a sequence of objects. Presumably, they are "annotations" of some kind.
They can be anything. We can do a lot with them; we'll start with using them to narrow the domain of values.

The core ``x: int`` provides a large domain of possible values. Python's ints can be immense numbers, easily filling memory with digits.

The ``MustBePrime`` class is the kind of thing that might be used to narrow the domain of allowed
values to prime numbers.

When does this value checking happen?
-------------------------------------

I'm glad you asked.

Use of annotated types is **not** part of the Python run-time. Annotated type arguments are essentially ignored.
The origin type is used by tools like **mypy**.

Any further use of annotations is a thing your application or tool-chain will need to do.

An application can see the annotations for an object using the ``__annotations__`` special attribute number,
or use the ``typing.get_type_hints()`` function.

::

    >>> from typing import Annotated, get_type_hints
    >>> class MustBePrime:
    ...     pass
    ...

    >>> class SomeApp:
    ...     x: Annotated[int, MustBePrime()]
    ...

    >>> get_type_hints(SomeApp)
    {'x': <class 'int'>}
    >>> get_type_hints(SomeApp, include_extras=True)
    {'x': typing.Annotated[int, <__main__.MustBePrime object at 0x7fde259a7be0>]}
    >>> get_type_hints(SomeApp, include_extras=True)['x']
    typing.Annotated[int, <__main__.MustBePrime object at 0x7fde259a7be0>]

We can see the annotated type hint for ``x``.

This means, our application is free to "apply" the annotation in some way.

"**Whoa!  That's vague**," you say. "There are no specific rules for annotated types?"

I agree.

The details are up to your app.  Seriously.  Define them in a way that makes sense.

Maybe you want your app looks like this:

::

    >>> class SomeApp:
    ....    x: Annotated[int, MustBePrime()]
    ...     def __init__(self, arg_value: int) -> None:
    ...         self.x = arg_value
    ...

And you've got a use case in mind...

::

    >>> sa = SomeApp(42)
    Traceback (most recent call last):
       ...
    ValueError: value 42 is not prime

The idea is that this specific app has an associated collection of annotations that are used
during ``__init__()`` processing to further validate the supplied values.

The code to this is *clearly* part of ``SomeApp`` -- maybe a metaclass, maybe a superclass -- but
clearly part of the app.

And the app will use the annotation as a kind of "plug-in" or "extension" or **Strategy** design pattern to do some additional processing at some point.

Our use case was part of ``__init__()`` processing.  What does this look like?

An example app
---------------

We'll avoid metaclasses, and pretend that Annotated types are checked by an
explict call to a method of the class.
Let's say a superclass, named ``RuleCheck`` has a method that must be
called at the end of ``__init__()`` to check compliance with annotations.

::

    class SomeApp(RuleCheck):
        x: Annotated[int, MustBePrime()]

        def __init__(self, arg_value: int) -> None:
            self.x = arg_value
            self.check()

The idea here is that the class-level hints are carefully defined.

The ``__init__()`` merely slaps any old value in there.

And the ``self.check()`` then assures that all hints are actually true for the supplied
values.

This means it will "apply" the annotation to the given value. In this case,
it will either allow the value silently or raise an exception if there's a problem.

Here's the ``RuleCheck`` class.

::

    from typing import Annotated, get_type_hints, get_args

    class RuleCheck:
        def check(self) -> None:
            vars = get_type_hints(self.__class__, include_extras=True)
            for name in vars:
                match vars[name]:
                    case Annotated:
                       base, *rules = get_args(vars[name])
                       for rule in rules:
                           rule(getattr(self, name))

Each annotated variable has the arguments to the annotation
retrieved with ``typing.get_args()``.
Each of these annotations must be a callable object of some kind
that can be applied to the attribute's value.

We leave the implementation of ``MustBePrime`` as an exercise for the reader.

Why do I need it?
==================

You need it in a bunch of cases. Here are some ideas.

1.  Type domain narrowing. We used "prime" as an example. You might want to use positive values, or
    values in a range. Or other properties that you'd like to make part of a type.

2.  Documentation. You can imagine ``x: Annotated[str, title("Some Descriptive Information"), Positive()]``.
    Since the documentation is not a comment or other ephermeral source text, you can use this
    to create a formal Schema for a class. Thing JSONSchema. (Or XSD if you're old.)
    You could use the title to beef up the exception messages, for example.

3.  Other Processing. Let's not get crazy, but the following is possible.

::

    x: Annotated[float, Title("Independent"), Range(0, 10)]
    y: Annotated[float, DerivedFrom("x"), Function(lambda x: 2*x-1)]

The idea is that we might build a class where any change to ``x`` computes a value
for ``y`` based on the annotation; and the value is cached as an attribute
value, not a ``@property`` which is always recompued.

(Yes, ``@cache`` and ``@property`` can do this. This isn't necessarily a **great** idea.
But it's possible.)

Building a type definition
---------------------------

Maybe we want this.

::

    PosInt: TypeAlias = Annotated[int, MustBePositive()]
    PrimePosInt: TypeAlias = Annotated[PosInt, MustBePrime()]

We've built a complicated type on top of another complicated type.

This permits us to -- for example -- improve the performance of ``MustBePositive`` with an attendant speedup of other, related objects.

File Parsing
------------

This is an edge case. But. It applies to the vast number of files processed by COBOL programs.

::

    x: Annotated[str, Start(0), Length(5)]
    y: Annotated[str, Start(5), Length(10)]
    z: Annotated[Decimal, Start(15), Length(10), Scale(2)]

We've provided the metadata for positions of the source data in a text document.
A file with a line like ``"ABCDEZYXWVUTSRQ0000001299"`` could be parsed by a class
that leveraged the annotations to pluck values out of the source string.
It could apply conversion from mainframe encodings ("EBCDIC") and do ``decimal`` conversion.

Where can I see examples?
=========================

I have two examples, right now.

Pydantic v2 Annotated Validators: https://docs.pydantic.dev/latest/usage/validators/#annotated-validators

Wow is this cool.

Also.

TigerShark. https://github.com/slott56/TigerShark  This is a pretty narrow problem domain.
But, the Annotated type hints were a *perfect* solution to an ages-old problem.
The X12 messages have complex more-or-less hierarchical structure. Messages have Loops (that can repeat), Segments, and individual Data Elements.

The definitions of the messages have complicated meta-data on size, encoding, data types,
optionality, etc., and etc.

What we want is a top-level definition of a message that looks like this:

::

    class MSG270(Message):
        """HIPAA Health Care Eligibility Inquiry X092A1-270"""
        ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
        isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]

The TypeAlias and Annotated type provide all the metadata for this message.

Looking elsewhere in the message module, we find this...

::

    class ISA_LOOP_ISA(Segment):
        """Interchange Control Header"""
        _segment_name = 'ISA'

        isa01: Annotated[I01, Title('Authorization Information Qualifier'), Usage('R'), Position(1), Enumerated(*['00', '03'])]

        isa02: Annotated[I02, Title('Authorization Information'), Usage('R'), Position(2)]

        isa03: Annotated[I03, Title('Security Information Qualifier'), Usage('R'), Position(3), Enumerated(*['00', '01'])]

Again, the elements are defined (entirely) by annotations.

The base type? ``I01``?  A pool of common definitions.

::

    I01: TypeAlias = Annotated[ID, MinLen(2), MaxLen(2)]

But wait! That still depends on a more foundational definition, ``ID``.

::

    ID: TypeAlias = str

The idea of this is to map the type information to type aliases, so anyone
can follow the message definitions completely. The annotations are defined
formally by the X12/EDI standards; the mapping to Python is through these
foundational type aliases for Python types.

Also see https://pypi.org/project/TigerShark3/ if you have the urge to install it.

