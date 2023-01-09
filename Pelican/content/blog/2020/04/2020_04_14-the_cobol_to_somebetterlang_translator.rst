The COBOL-to-SomeBetterLang Translator
======================================

:date: 2020-04-14 08:00
:tags: #python,COBOL
:slug: 2020_04_14-the_cobol_to_somebetterlang_translator
:category: Technologies
:status: published


Here's a popular idea.

   ... a COBOL-to-X translator, where X is a more-modern programming
   language ...


This is a noble aspiration.

In principle -- down deep -- all programming can be reduced to an
idealized Turing Machine.

This means that we \*should\* be able to locate all the state changes
in a given spaghetti-bowl of COBOL. Given the abstract state
transitions, we can emit a version of that machine in any language.

Emphasis on the \*should*.

There are road-blocks.

The first two are rarities. But. When confronted with these, we'll
have significant problems.

-  The ``ALTER`` statement means the code can be changed at run-time. There
   are constraints, but still... When the code is not static, the
   possible domain of state changes moves outside working storage and
   into the procedure division itself.

-  A data structure with a ``RENAMES`` clause. This adds a layer of
   alternative naming, making the data states quite a bit more complex.


The next one is a huge complication: the ``GOTO`` statement. This makes
state transitions extremely difficult to analyze. It's possible to
untangle any GOTO of arbitrary complexity into properly tested IF and
WHILE statements.


However. The tangle of GOTO's may have been actually meaningful. It
may have carried some suggestion of a business owner's intent. A
COBOL elimination algorithm may turn tangled code into opaque code.
(It's also possible that it clarifies age-old bad programming.)


The ordinary ``REDEFINES`` clause. This was heavily used as a storage
optimization for the tiny, slow file systems we had back in the olden
days. It's a union of distinct types. And. It's a "free" union. We do
not know how to distinguish the various types that are being
redefined. It's intimately tied to processing logic in the procedure
division.


Just to make it even more horrifying...


File layouts evolve over time. It's entirely possible for a
\*working*, \*valid*, \*in-production\* file to have content that
does not match any working program's DDE. The data has flags or
indicators or something that lets the app glide past the bad data.
But the data is bad. It used to be good. Then something changed, and
now it's almost uninterpretable. But the apps work because there are
enough paths through the logic to make the row "work" without it
matching any file layout in any obvious way.


I'm not sure an automated translation from COBOL is of any value.


I think it's far better to start with file layouts, review the code,
and then write new code from scratch in a modern language. This
manual rewrite leads directly to small programs that -- in a modern
language -- are little more than class definitions. In some cases,
each legacy COBOL app would like becomes a Python module.


Given snapshots of legacy files, the Python can be tested to be sure
it does the same things. The processing is not nuanced, or tricky, or
even particularly opaque.


The biggest problem is the knowledge captured in COBOL code tends to
be disorganized. The real work is disentangling it. A language that
supports ruthless refactoring will be helpful.





