The eval() Conundrum
############################

:date: 2025-09-28 09:46
:tags: python,games,ttrpg,dsl
:slug: 2025-09-28-the_eval_conundrum
:category: Python
:status: published

Many people will proclaim that the ``eval()`` function is reprentnatly evil.

Feel free to skip the two rants.

BLUF
----

The ``eval()`` function is relatively easy to work with.

..  important:: Limit the globals to the fewest possible names.

Eval() Rant
-----------

A too-common claim is that we can't use ``eval()`` because an Evil Super Genius (ESG™) will surreptitiously inject malicious code into a configuration file or something.
This claim ignores the fact that all Python code is plain text.
Any idiot can change the code.
An ESG would find they are over-qualified to make a mess of a Python app.

For services (shared by multiple users), ``eval()`` can raise havoc for all concerned.
So can a clumsy, marginally compentent admin.
Indeed, bad admin mistakes are a considerably larger problem than some mysterious ESG's cleverness.

DSL Rant
--------

I'm not a big fan of inventing whole new DSL's.


    Them: "I'll solve this problem by inventing a DSL."

    Me: "Now you have two problems."

Also. We're surrounded by DSL's. There's a baffling variety.
Even within a general-purpose programming language like Python,
there are "mini-languages".
Formatting. Regular Expressions. DSL's should be viewed with suspicion.

A Python-as-DSL Example
--------------------------

(Thanks for your patience with the ranting.)

In many cases, Python object expressions are a perfectly useful DSL.

We don't need to invent any syntax or write a parser.
Instead, we write Python class declarations and define objects.
We rely on the prefectly wonderful Python parser.

For those who play #TTRPG's, there's a mini-language around the description of a handful of polyhedral dice.

Example **3d6+2**.

This means "find 3 6-sided dice, roll them, and add 2".
There are some variants, but none of them are much more complicated than this example.

Let's say, we're writing some TTRPG design tools, and we want to compute the expected range, mean, and (really important) standard deviation of a handful of dice.

The goal is this.

..  code-block:: Python

    >>> from dice import *
    >>> rule = 3 * D6 + 2
    >>> rule.min, rule.max
    (5, 20)
    >>> rule.mean, rule.stdev
    (12.5, 2.9580398915498076)

This ``rule`` object can do more, of course.

The core feature here is replacing the traditional specification string, ``3d6+2`` with a (very) slightly differerent syntax: ``3*D6+2``.
We've made the ``d`` uppercase for no good reason.
We've added a ``*`` so the expression is valid Python.

So?
----

Next step is to wrap the D6 object with a CLI.

..  code-block:: bash

    % python dice.py --expected '3*D6+2'
    3 * D6 +2
    range: 5 - 20
    mean: 12.50
    standard deviation: 2.958

There's a catch to this.
Some will say it's a security nightmare.
We're parsing Python code provided as a command lime argument.

**This opens the application to exploit by an ESG.**

Folks will announce, one should **never** accept Python code from the command-line.
See `Eval() Rant`_, above: an Evil Super Genius (ESG™) will surreptitiously inject malicious code into the command-line parameters.

..  code-block:: bash

    % python dice.py --expected 'import subprocess; subprocess.run("format c:")'

Everyone knows this **will** happen.
Maybe it will be out of malice.
Or, more likely, it will be simple incompetence.

Safe eval()
------------

..  warning:: Control the Globals

Here's my little example of how I like to use ``eval()``.

..  code-block:: python

    try:
        code_obj = compile(expression, "<argument>", mode="eval")
        d = eval(code_obj, globals=namespace, locals=namespace)
    except BaseException as err:
        sys.exit(f"The dice expression {expression!r} does not compute")

I like to break it into two steps.
In this case, they're in a single ``try:`` block.
In some cases, it makes sense to use two, distinct ``try:`` blocks.

1. If there are syntax errors from the ``compile()`` function, these are caught in one block. These errors are often innocent, and some good error displays can be useful.

2. If there are evaluation errors from the ``eval()`` function, these are caught in a separate block. Other than a ``NameError``, exceptions here indicate potential bugs somewhere in the underlying class definitions.

The ``namespace`` parameter is the **short** list of all the global variables and names available at eval time.
For this application, it's the defined set of polyhedral dice.

..  code-block:: python

    namespace = {
        "D4": D4,
        "D6": D6,
        "D8": D8,
        "D10": D10,
        "D12": D12,
        "D20": D20,
        "D100": D100,
        "PCT": D100,
    }

That's all there is.
Any name not in this mapping will raise a ``NameError`` exception and the end of processing.

In Case It Matters
-------------------

Here's a glimpse at the ``Die`` class.

..  code-block:: python

    class Die:
        def __init__(self, faces: int) -> None:
            ...
        def __rmul__(self, n: int) -> "Die":
            ...
        def __add__(self, adj: int) -> "Die":
            ...
        @property
        def min(self) -> int:
            ...
        @property
        def max(self) -> int:
            ...

    D4 = Die(4)
    D6 = Die(6)
    D8 = Die(8)
    etc.

The DSL itself is essentially a class and some global objects.
The syntax is pure Python.

I'm a big fan of avoiding writing parsers.
Using Python as the DSL makes it relatively easy to test the DSL.
After all, simple doctests provide ready confirmation the DSL works as advertised.

Conclusion
----------

Don't fear ``eval()``. Control the globals.
