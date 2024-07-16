Functional SQL in Pure Python
#############################

:date: 2024-07-16 08:14
:tags: SQL,python,project
:slug: 2024-07-16-functional_sql_in_pure_python
:category: Python
:status: published

I've published a framework for doing SQL-like programming in Pure Python -- no database required.

Here: `https://github.com/slott56/functional-SQL <https://github.com/slott56/functional-SQL>`_.
See the `functional-SQL <https://slott56.github.io/functional-SQL/_build/html/index.html>`_ documentation.

This allows us to transform SQL:

..  code-block:: SQL

    SELECT n.name, v.c2
    FROM names_table n, values_table v
    WHERE n.code = v.c1

To pure Python:

..  code-block:: Python

    Select(name=lambda cr: cr.n.name, value=lambda cr: cr.v.c2)
    .from_(n=names_table, v=values_table)
    .where(lambda cr: cr.n.code == cr.v.c1)

Yes, the Python is longer and cluttered with lambdas.

This produces the same results using a similar algorithm.

Most important, this works with table-like collections of **Any** class of Python objects.

This implements the essential SQL query algorithm:

- having ``filter()``

- group-by ``reduce()``

- where ``filter()``

- select ``map()``

- from ``itertools.product()``

This `From-Select-Where-GroupBy-Having(Tables)` design pattern is very handy.
A lot of people think of processing data following this template.
There's no reason, however, to inject the overhead of schema and database.
