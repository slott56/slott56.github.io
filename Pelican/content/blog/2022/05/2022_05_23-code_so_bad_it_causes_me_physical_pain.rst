Code so bad it causes me physical pain
======================================

:date: 2022-05-23 20:38
:tags: data structure,#python
:slug: 2022_05_23-code_so_bad_it_causes_me_physical_pain
:category: Technologies
:status: published

Here's the code.

::

   def get_categories(file):
       """
       Get categories.
       """
       verify_file(file)

       categories = set()

       with open(file, "r") as cat_file:
           while line := cat_file.readline().rstrip():
               categories.add(line)

       return categories

To me this was terrible. truly and deeply horrifying. Let me count the
ways.

#. The docstring repeats the name of the function providing no
   additional information.
#. The ``verify_file()`` function checks are pure, useless LBYL code. It
   seemed designed to map a lot of detailed exceptions to a
   ``RuntimeError``. Which is misleading.
#. The use ``while`` and ``readline()`` to iterate through the lines of
   a file is -- I guess -- reasonable if we're working Pascal or
   Modula-2. But we're not. Use of the walrus operator isn't really
   getting any bonus points because -- well -- this is terrible.
#. While pathlib is used elsewhere in this module, it's not used here.
   This function works with a filename string, assigned to the ``file``
   parameter.

Actually, taking a step back, it's not that the author is being
malicious. They just missed all the features of files and sets. And --
somehow -- were able to learn about the walrus operator while never
figuring out how files work.

This is something like:

::

   source = Path("some_file.txt")
   with source.open() as source_file:
       categories = set(source_file)

And that's it.

It Gets Worse
-------------

This was part of some category mapping application.

They've got a CSV file with some string values. And they want to map
those string values to summary category values.

Most folks think of a dictionary for a mapping from one string to
another string.

The code I was sent -- I kid you not -- used a list of two-tuples. I'll
repeat that for those who are skimming. It use **A LIST OF TWO-TUPLES
INSTEAD OF A DICTIONARY**.  It used a colossally bad search through an
unsorted list of tuples to find matches. (The only search that would
have been worse was random probes instead of iteration.)

It really did.

It can't even show you that code, it's such a horrifyingly bad design.

They had a question. Was the looping over a list of two-tuples
ineffective? That's why they asked for help.

It was like they had never heard of a dictionary. Nor seen a tutorial
with a dictionary. Nor read a book that mentioned dictionaries. They had
managed to learn enough Python to see the walrus operator without
hearing of dictionaries.

A list of two-tuples, when provided to the ``dict()`` function, will
make a dictionary. They were ignorant of this.

A dictionary that does **O**\ (1) lookups and avoids looping over a list
of two-tuples. This was a mystery to them..

When someone doesn't know the Python dictionary exists, what is the
appropriate response?

How can you politely say "Find another tutorial and do the ENTIRE thing
all of it!"

That's Not All
--------------

There's this nugget of "You can't be serious."

::

   category_counts = {element: 0 for element in categories}

And

::

   category_counts[category] += 1

Yes. They used a dictionary to count instances of the categories. They
did not understand ``collections.defaultdict`` or
``collections.Counter``. But they understood a dictionary well enough to
use it here. But not use it elsewhere for the central functionality of
the app.

So. They couldn't use a dictionary, but could use a dictionary.

They couldn't use the csv module, so they wrote their own (bad) CSV
parser.

It's almost impossible to write a polite code review.



-----

Hopefully you have tests on it and can refactor or...
-----------------------------------------------------

McSee<noreply@blogger.com>

2021-10-19 13:03:56.467000-04:00

Hopefully you have tests on it and can refactor or write it again from
scratch





