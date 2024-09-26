Better than grep
################

:date: 2024-09-26 09:50
:tags: parsing,ast,SQL,grep
:slug: 2024-09-26-better_than_grep
:category: Python
:status: published

In the process of writing *Unlearning SQL*, I had a need to extract SQL blocks from Python programs.
Of course, I tried ``grep``.
It wasn't ideal.

..  note:: Book is available here:

    -   https://www.amazon.com/dp/B0DDMFMXNW

    -   https://www.lulu.com/shop/steven-lott/unlearning-sql/paperback/product-yvnm8zn.html?page=1&pageSize=4

    -   https://play.google.com/store/books/details?id=23WAEAAAQBAJ

    -   https://books.apple.com/us/book/unlearning-sql/id6443164060

SQL blocks are -- ideally -- triple-quoted strings.
Of course, so are docstrings.
This creates additional problems.

The first pass is to try to use ``grep`` to track down the triple-quoted blocks.
This is a complex regular expression because it spans multiple lines.

The output is a file of text with SQL stateements, docstrings, and quote marks all over the place.
It requires much manual cleanup.

Doing the cleanup of the initial ``grep`` output is right awful.
I need to somehow preserve a multi-line triple-quoted string that starts with a SQL reserved word,
and ignore multi-line triple-quoted strings that don't begin with something obvious SQL.

I give up.

Python RE
=========

Using Python to extract the initial strings and create a data structure is a good second step.
I can use the same regular expression with the Python ``re`` module.
I can use ``Path.glob()`` instead of shell globbing.

I can now apply a second regular expression to the list-of-strings object to look for SQL words.
(There aren't many: CREATE, DROP, INSERT, UPDATE, SELECT, DELETE.)

This is much nicer. But. I can do better.

Python AST
==========

This process is reading valid, tested Python code.
The standard library's ``ast`` module defines the abstract syntax tree for Python code.
This module can identify literal strings in code, and docstrings.

How does this work?

There are three parts.

1.  Define an ``ast.NodeVisitor`` subclass.

2.  Parse the module's source to create an AST.

3.  Use the visitor to collect the strings.

We'll look at each in some detail.

First, a note for those unfamiliar with the **Visitor** design pattern.
A tree structure is recursive.
Examining each node of the tree can be done with a recursive function to visit a node, then visit all descendents of that node.
It's not a complicated function, but, there's  a complication.

The node in an abstract syntax tree tend to be a union of a wide variety of types.
There will be an ``ast.Module``, an ``ast.ClassDef``, ``ast.FunctionDev``, etc., etc.
A "simple" recursive function needs to treat each class distinctly to properly visit all of the children.

The **Visitor** pattern delegates part of the work to a visitor object that is presented each node of the tree.
The visitor object can have methods for each unique type of node, avoiding a complex ``match-case`` statement,
or a complex ``if isinstance(node, Whatever)-elif`` chain.

The Visitor
-----------

We're interested in one feature of the abstract syntax tree of Python: the ``ast.Constant`` objects where the constant's value is a string.
Ideally, this will focus on those strings that start with a SQL keyword.

Here's the starting point:

::

    class StringVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.sql_blocks = []
        def visit_Constant(self, node: ast.AST) -> None:
            match node.value:
                case str() if sql_like(node.value):
                    self.sql_blocks.append(range(node.lineno+1, node.end_lineno))
                case _:  # Ignore all other types
                    pass

The ``visit_Constant()`` method is invoked for each ``ast.Constant`` object in the tree.
This will find nodes that are strings and pass the ``sql_like()`` filter.

This net is a little too fine.
It can will capture docstring comments that happen to look SQL-like.
It's essentially the same as the ``grep`` output with two improvements:

-   No baffling regular expression.

-   The output can be a more useful data structure, not a file of lines of text.

While nicer in some respects, it's incomplete.
The next step is to add the required feature to ignore docstring comments.
There two choices:

1.  Write a better ``sql_like()`` function.

2.  Exclude any string constant that is the first line of the body of a module, class, or function definition.

Option 1 can can involve finding a SQL parser to see if a string really is pure SQL.
Or, it can require writing a better regular expression to locate likely SQL statements.

Here's the unit test case:

::

    >>> src_text = """
    ... def f(c):
    ...     '''
    ...         Select the right answers.
    ...     '''
    ...     r = c.execute('''
    ...         SELECT * FROM DUMMY
    ...     ''')
    ... """

The docstring comment starts with a SQL keyword. Ugh.
It seems kind of daunting to locate a suitable SQL parser.
The regular expression to distinguish casual use of SQL-like keywords seems hopeless complicated.
There's something better: exclude docstring constants.

Exclusion Rules
---------------

The **ast.NodeVisitor** implementation has a handy feature.
This permits an application to choose to visit or skip the subsidiary nodes of an object.
When a class overrides a ``visit_XXX()`` method, the override can call the ``self.generic_visit(node)`` to visit all the children.
If the overriding method does not evaluate ``self.generic_visit(node)``, the children are **not** examined.

This is a bit too strict.

Skipping **all** children of a module, class definition or function definition isn't helpful.
The rest of the children could have SQL code.
It's important to skip only the very first line of code when this is a string constant.
The rest of the code needs to be visited.

I decided to accumulate an "ignore these" set of nodes.
This set of nodes will be the first line of code that's also a string constant.
The ``visit_Constant()`` can then politely decline these nodes.

Here's the visitor class looks:

::

    class StringVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.docstrings = set()  # Docstring nodes at the start of module, class, def
            self.sql_blocks = []
        def exclude_docstring(self, node: ast.AST) -> None:
            if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
                self.docstrings.add(node.body[0].value)
            self.generic_visit(node)
        visit_Module = exclude_docstring
        visit_ClassDef = exclude_docstring
        visit_FunctionDef = exclude_docstring
        def visit_Constant(self, node: ast.AST) -> None:
            match node.value:
            case str() if sql_like(node.value):
                if node not in self.docstrings:
                    self.sql_blocks.append(range(node.lineno+1, node.end_lineno))
                case _:  # Ignore all other types
                    pass

First, I've added a a set of nodes to exclude.
(Nodes are immutable, and have a hash value, that's why a set works well for this.)

Second, there's a generic visit function, ``exclude_docstring()``, that handles ``ast.Module``, ``ast.ClassDef`` and ``ast.FunctionDef`` classes.
I can define the needed ``visti_XXX()`` methods for these classes to all use the generic exclusion method.

Finally, I need to make sure any ``ast.Constant`` node wasn't already excluded because it was the first string in a definition.

With this, I can now parse the source, and apply the visitor.
The ``sql_blocks`` attribute will have a list of ``range()`` objects that point to the SQL statements.

The Parsing and Visiting
------------------------

Here's the final bit.

::

    tree = ast.parse(src_text, "<test>")
    sv = StringVisitor()
    sv.visit(tree)
    print(sv.sql_blocks)

This will parse the code, then visit the ast.

When this is done, it has a list of ``range()`` objects.
These ranges can be used to highlight the proper lines of code from the source file.
Your application may be different, of course, you may want to simply write the literals to a TOML configuration file, for example.

"Why," you might ask, "do you have range() objects instead of the code?"

The Ultimate Goal
==================

In my specific (and unique) use case, I need to be sure the **minted** code highlighter will properly format SQL code.

The goal is a book, written using RST markup, with properly colorized SQL examples.
That part is easy, what's hard is making sure all examples are unit-tested and really, really work.
(I'm fussy like that.)

This means including the source text from a ``.py`` file into the book's content.

But. (Big Sigh.)

Minted can't cope with a mixture of Python and SQL, and can't properly color code a few isolated SQL lines plucked from a Python context.
(This shouldn't have been too surprising; after I ranted and raved about it, I realized minted must colorize the whole file before a few lines can be selected from it.
Context matters when highlighting syntax.)

In my application, I'm creating a parallel file with all **non-SQL** lines prefixed with the "--" SQL comment marker.
This leaves the SQL behind to be seen by minted and properly colored.
The Python lines are hidden from minted.

The book can then use an ``.. literalinclude::`` directive that has properly highlighted SQL.
The Python file is unit tested, which gives me confidence in the SQL file.
