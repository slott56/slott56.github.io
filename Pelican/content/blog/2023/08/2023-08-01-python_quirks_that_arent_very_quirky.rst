Python Quirks that aren't very quirky
##############################################

:date: 2023-08-01 09:00
:tags: python,community
:slug: 2023-08-01-python_quirks_that_arent_very_quirky.rst
:category: Python
:status: published

See https://writing.peercy.net/p/python-quirks

Superficially, most of these are true.

Looking a little more deeply, most of them are also presented in a somewhat misleading way.
A few set up a good punch-line. The **Inheritance** one, for example, is funny.

If the point is to force a deeper investigation, I think the piece might not be helpful.
I know too many people who would look at this list and say "See, Python is as bad as JavaScript."
Or "That's why I only use perl."
These are the sort of folks won't actually refer to the Python language reference manual to see what's going on.

One of these **is** a legitimate quirk.
The rest involve a little bit of "don't look at the man behind the curtain" mixed with "don't read the documentation."

To ease my own mental anguish, I'll include a slightly deeper dive into these language feaures.

1.  Generators.

    ``sorted()`` creates a new list from the argument value. It's not a generator.
    Comparing the resulting list to the argument is unsurprising.

    ``reversed()`` doesn't create a list. It is a generator. Since it can only
    be used once, one use of the generator ``y`` has a sequence of values.
    The other use of the generator ``y`` has no values.

    I suppose the single-use-of-a-generator featrure could be called a quirk.
    Except it's well-documented, so, I'd argue that this simply exposes a language feature.

2.  References.

    The example fails to show how ``a`` was created. It's not obvious
    how the reused reference to a sublist was propogated throughout
    the list.

    Missing:

    ::

        a = [[0]] * 5

3.  Assignment.

    Not sure what the point of this is.
    It doesn't even seem quirky.

    I guess they're astonished they can use something other than a trivial
    variable in a ``for`` statement.

4.  Closures.

    My guess on this is they were hoping the ``i`` variable would not be a single variable;
    instead, a fresh, new variable would be created by the generator expression.
    Perhaps other languages do this, and manufacture fresh, new variable bindings.

    Python has a (relatively) simple rule for variables: Local, Enclosing, Global, and Built-in.
    There's no closure rule to create new variables. There are many good tutorials on the LEGB rule.

5.  Inheritance.  This one is kind of funny.

    It's also, on reflection, unsurprising.
    The ``type`` type -- like all types -- is an ``object``. Mostly because almost everything is an object.
    The ``object`` type -- like all types -- is a ``type``.

6.  Operator Chaining.

    This isn't a quirk at all.
    This seems to be an exploration of precedence rules among operators.
    It seems to be a matter of definition among ``==``, ``and``, and ``in`` operators.

    Also, it's not clear what "chaining" means here.
    If ``1 + 2 + 3`` is what they mean by "operator chaining", then I think that may be the root
    cause of the confusion. These are all binary operators with intermediate results.
    Perhaps it can help to think of implicit ()'s around each binary operation.

7.  Identity.

    This is an optimization in the CPython interpreter to pre-allocate some integers.
    This is a proper quirk. I'm glad it's on this list.

8.  NFKC Normalization.

    See https://unicode.org/reports/tr15/.

    This isn't Python. This is Unicode.

9.  Default Arguments.

    This is pretty well-known. Some newbies discover it, and then
    re-read the documentation that describes why this happens, and say "makes sense."
    Here's the rule: **The mutable object is only created once; it's shared.**

    Most linters warn that this feature may not be doing what folks think it's doing.

    This appears in many other places. For example, default values for fields of
    dataclasses cannot be mutable objects, because they'd be shared.

10. Whatever This Is.

    This isn't a quirk, it's a bug. It was fixed in Python 3.11, though. So it's much less interesting.
    It remains a known bug until Python 3.10 end-of-life, 04 Oct 2026.


11. Python 2.

    Python 2 has been at end-of-life since 01 Jan 2020.
    These kinds of things ceased to be interesting on that date.

In summary, and in conclusion, the identity of small integers is a legitimate quirk.
I like it. The inheritance is funny. I like that, too.
