Modern Python Cookbook and Type Hints
#####################################

:date: 2024-09-18 16:03
:tags: book,packt,cookbook
:slug: 2024-09-18-cookbook_and_mypy
:category: Python
:status: published

Modern Python Cookbook — with lots and lots of recipes — is something you might need. Find the results of checking all these recipes here:
https://www.amazon.com/Modern-Python-Cookbook-updated-techniques/dp/1835466389

I (reluctantly) switched from using **mypy** to using **pyright** to check all of these recipes carefully. The type alias (:PEP:`695`) syntax wasn’t fully supported.

I didn’t find any new problems with **pyright**, but I did tweak my workflow a little bit to use more of **pyright**\ ’s linting features.

Follow this for status on mypy https://github.com/python/mypy/issues/15238.

What gets checked?
==================

Using a vague phrase like "everything" is -- obviously -- not quite as helpful as some details.

There are three broad categories of examples:

1.  REPL examples.

2.  Code examples.

3.  Jupyter Lab examples.

Clearly, the REPL examples can't be checked. However. Many REPL examples depend on code definitions that can include checkable hints. The idea is to provide code outside the REPL and then use REPL doctest test cases to demonstrate how the code works. Which means many REPL examples have type hints that aren't shown in detail in the recipe.

All of the ordinary code examples are checked.

The Jupyter Lab examples in Chapter 12 are a mixed bag. Some examples involve an importable module, which can be checked. The notebook itself, though, is difficult to check. One **could** convert the notebook to a script and the type check the script. This only works when the notebook is careful about not reusing variables.

So that means all the example code in almost all of the chapters is put through **pyright** to be **sure** there's nothing obviously sketchy.

I'd like to switch back to **mypy**. I don't have a great reason, it just seems like it's vaguely "better", measured on some axis I can't articulate.
