Real Math (symbolic math, like mathematicians do) and a spreadsheet-like feedback loop
======================================================================================

:date: 2021-06-01 08:00
:tags: #python,jupyter lab,spreadsheet,sympy
:slug: 2021_06_01-real_math_symbolic_math_like_mathematicians_do_and_a_spreadsheet_like_feedback_loop
:category: Technologies
:status: published

See https://slott56.github.io/replacing-a-spreadsheet/. This document is
really exciting (to me).

This is still shaky -- I'm still learning -- but it's a very cool
combination of Python components
`sympy <https://docs.sympy.org/latest/index.html>`__ and `Jupyter
Lab <https://jupyterlab.readthedocs.io/en/stable/>`__. As a bonus,
`Jupyter{Book} <https://jupyterbook.org/intro.html>`__ appeals to me as
a writer. There's an aspect of literate programing in this that is also
very appealing.

The core is this.

-  I have a problem that involves complex math. Well, it's complex to
   me. It involves integrals, so there's a lot of space for confusion.
-  This is applied math, and I want to plug in numbers and get answers.

In effect, I want a spreadsheet.

I don't want rows-and-columns. I do want cells, though, that's a nice
organizing principle.

I don't want the goofy little formulas in a spreadsheet. I want real
Python code.

I want the spreadsheet-like feature of computations that depend on
inputs and are re-run when the inputs change. This has been the core
value proposition for spreadsheets since the days of VisiCalc. It's a
great UX in general. We just need to get past the rows-and-columns.

The problem with most spreadsheet apps is the limited capability for
more serious math.

Which is why the sympy + Jupyter Lab was a blinding revelation to me.





