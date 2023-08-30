More Python Quirks Debunking
##############################################

:date: 2023-08-15 09:00
:tags: python,community
:slug: 2023-08-15-more_python_quirk_debunking
:category: Python
:status: published

Stuff I found on the internet that I have to disagree with. 

(And no, I didn't ask for clarification.
If the author posts things without supporting details it suggests they might lack the supporting
details. I can be charitable and assume they don't really care about providing useful information,
but are merely trolling for engagement. Yes. That's cruel.
I can't see how you take the time to have an opinion and not provide support for it.)
    
    A few of #Python 3 #quirks and #kludges
    
    1. Global Interpreter Lock
    #. Strong, dynamic typing
    #. Massive ``Any`` hole in the type system
    #. Verbose class definition
    #. Declaration of instance attributes is their definitions in ``__init__()``
    #. Repetitious ``self`` and kludgy ``super().__init__()``
    #. Kludgy string-quotes to reference the class from within its definition
    #. Kludgy ``TypeVar`` definition
    #. Absence of structural typing
    #. Need explicitly to convert iterator to list using ``list()``
    #. Usurping the ``id()`` name
    #. Inner method may mutate referenced objects in the closure but may not mutate primitive values therein
    #. Kludgy ``main()`` invocation
    #. Disconcerting lack of type information in the holdover documentation from the P2 days

Some of these might be good points. Some of these seem to be nonsense.
A bunch can't be interpreted, which I find madding.

1. Global Interpreter Lock
===========================

I'm not sure what this means. It's a solution to a specific problem.
It's -- I suppose -- a candidate "quirk" because it's an unusual solution to
the problem of assuring that data structure updates are atomic.

It saves us from having to use explicit locks all over the place when updating
objects with complex state.

The GIL-less Python proposals will require a bit more care in defining structures
useful in multithreaded environments. Is this a gain? It's disputable.

2. Strong, dynamic typing
=========================

Yep. There it is. Quirk? Kluge? Dunno. It seems like a brilliant solution to a long-standing problem.

3. Massive ``Any`` hole in the type system
==========================================

Does this mean it's bad that **mypy** assumes ``Any`` for missing types?
If you don't like the **mypy** assumptions, write type hints.

Does this mean it's bad that you can use ``Any`` to provide uninformative type hints?
If you don't like ``Any``, consider not using it as a type hint.

4. Verbose class definition
===========================

Quirk?  I guess they've never seen Java.

Kluge?  What would they prefer?

What would they omit is the real question. From the item 6, below, I'm guessing
they don't like to have ``self`` listed explicitly.

5. Declaration of instance attributes is their definitions in ``__init__()``
=============================================================================

First -- and most important -- there aren't any C- or Java- style declarations.
The instances are dynamic in every sense of the word.
The ``__new__()`` method does almost nothing.

I'll buy this as a legit quirk. It's a consequence of the way attributes
work, and logic is compelling and consistent.

It's trivial to include type hints in the class definition, separate
from initialization in the ``__init__()`` method. I find this helpful.

::

    class X:
        a: int
        b: float

        def __init__(self, a: str, b: str) -> None:
            self.a = int(a)
            self.b = float(b)

It's potentially misleading: the ``a`` and ``b`` appear to be class variables.

6. Repetitious ``self`` and kludgy ``super().__init__()``
==========================================================

The use of ``self`` is not repetitious. It's explicit.

Not sure what's klugy about ``super().__init__()``. I guess they don't like writing ``__init__()`` and
prefer having this assumed, also.

This is -- to me -- flat our wrong.

7. Kludgy string-quotes to reference the class from within its definition
===========================================================================

I guess they'd prefer to have an explicitly complicated-looking forward reference
for a name. We could have a lot of ``class XYZ: defined_later()`` constructs
to sort out circular references among classes.

I guess they don't like this.

::

    class X:
        @classmethod
        def makes_X(cls: type["X"], *args, **kwargs) -> "X":
            ...

It seems like a tedious ``X = ForwardRef('X')`` would be required
to define the name ``X`` before the actual class is defined.
See #8, below, they don't like that syntax. Does this mean they want a new statement for
forward references?

Or. It would require **mypy** to gaze more deeply at the parse tree to resolve
circular references. I'm not sure what they think would be better.

8. Kludgy ``TypeVar`` definition
================================

I'm guessing they want a new statement in the language instead of a function
in the ``typing`` module.

Since types are explicitly optional, new statements to handle types seems wrong to me.

9. Absence of structural typing
===============================

This is confusing. The ``NamedTuple`` provides structural types.

I'm guessing they were hoping for some other classes to **also** behave like
types in a structural system. It seems simplest to use ``NamedTuple``
and a functional style of programming.

10. Need explicitly to convert iterator to list using ``list()``
=================================================================

This is nonsense. What if the iterator is a sequence of pairs that
should be converted to a mapping with ``dict()``?


11. Usurping the ``id()`` name
===============================

Don't get this. The ``print()`` name is also usurped by built-ins.
There are a dozen built-in function names that usurp other names one might want to use.
And all those keywords!  The name ``class`` and ``def`` and ``return`` are all usurped
by keywords.

12. Inner method may mutate referenced objects in the closure but may not mutate primitive values therein
===============================================================================================================

Primitives can't be mutated.

Referenced objects can **always** be mutated.

It doesn't require an "inner" method. It's true for every function and method at all levels.

I'm guessing the idea of mutable vs. immutable objects could be a quirk.

13. Kludgy ``main()`` invocation
================================

Kludge? Really?  I guess they've never seen Java.

14. Disconcerting lack of type information in the holdover documentation from the P2 days
==========================================================================================

It's often helpful to provide an example of a documentation gap where
type information is totally missing (or is only present in a stubs file where it's not
automatically included by Sphinx). While I haven't seen any examples of missing type information in
Python or standard library documentation, that doesn't mean much. I only write books
about Python, I don't actually help maintain it.

Summary
=======

There's a good point:

-   Declaration of instance attributes is their definitions in ``__init__()``

The reset is a mixture of

-   too vague to comment on,

-   it's not clear what would be better, and

-   wrong.

Mostly the former. Few of the latter. (#10 seems to be the stand-out for wrong.)

It's important to think about these things when learning a language.
Some discussion of alterantives from other languages would make these points a lot
easier to interpret and understand.

However, it's also important to understand why soem things are present in a language.
It's important to look a little more deeply at the language rules -- perhaps read the
relevant PEP's -- to see what alternatives have been proposed and discarded.

In most cases, decisions aren't arbitrary, but reflect deeper considerations on the underlying
semantics of the language and the implementation details of the compiler and/or run-time.
