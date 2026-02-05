Revised Understanding --> Revised Data Structures --> Revised Type Hints
========================================================================

:date: 2022-07-05 08:00
:tags: #python,pyWeb
:slug: 2022_07_05-revised_understanding_revised_data_structures_revised_type_hints
:category: literate programming
:status: published

My literate programming tool, pyWeb, has moved to version 3.1 --
supporting modern Python.

Next up, version 3.2. This is a massive reworking of the data structures
involved. The rework lets me use Jinja2 for templates. There's a lot of
fiddliness to getting the end-of-line spacing right. Jinja has the
following:

::

   {% for construct in container -%}
   {{construct}}
   {%- endfor %}

The easy-to-overlook hyphens suppress spacing, allowing the construct to
be spread onto multiple lines without introducing extra newlines into
the output. This makes it a little easier to debug the templates.

It now works. But. Until I get past strict type checks, there's no
reason for calling it done.

::

   Found 94 errors in 1 file (checked 3 source files)

The bulk of the remaining problems seem to be new methods where I forgot
to include a type hint. The more pernicious problems are places where I
have inconsistent hints and Liskov substitution problems. The worst a
places where I had a last-minute change change and switched from ``str``
to ``int`` and did not actually follow-through and make required
changes.

The biggest issue?

When building an AST, it's common to have a union of a wide variety of
types. This union often has a discriminator value to separate
``NamedChunk`` from ``OutputChunk``. This is "type narrowing" and there
are a variety of approaches. I think my best choice is a ``TypeGuard``
declaration. This is new to me, so I've got to do some learning before I
can properly define the required type guard function(s).
(See https://mypy.readthedocs.io/en/stable/type_narrowing.html#user-defined-type-guards)

I'm looking forward (eagerly) to finishing the cleanup.

The problem is that I'm -- also -- working on the updates to `Functional
Python
Programming <https://www.google.com/search?client=safari&rls=en&q=packt+functional+python+programming+2e&ie=UTF-8&oe=UTF-8>`__.
The PyWeb project is a way to relax my brain from editing the book.

Which means the pyWeb updates have to wait for Chapter 4 and 5 edits.
(Sigh.)





