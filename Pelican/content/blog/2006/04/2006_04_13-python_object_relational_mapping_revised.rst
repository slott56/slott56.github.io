Python Object-Relational Mapping (Revised)
==========================================

:date: 2006-04-13 02:37
:tags: #python,database
:slug: 2006_04_13-python_object_relational_mapping_revised
:category: Python
:status: published





Ian Bicking: A Blog http://blog.ianbicking.org/,
provided some info on Py3K and Python Introspection http://blog.ianbicking.org/introspecting-expressions-in-py3k.html.



For
me, the interesting part was his summary of Object-Relational Mapping.  Mr.
Bicking identifies two broad approaches: lambda introspection and operator
overloading.



**Lambda Introspection**

`Dejavu  <http://projects.amor.org/dejavu>`_
It primarily uses a generic `Data Mapper <http://www.martinfowler.com/eaaCatalog/dataMapper.html>`_  architecture.  It is more of an OODB
backed by a relational store.

`SQLComp  <http://subway.python-hosting.com/wiki/SQLComp>`_  The make_query method examines a lambda
containing a list comprehension to create SQL.  This is only queries, and isn't
a complete ORM.



**Operator Overloading** 

`SQLObject  <http://sqlobject.org/>`_  This is
a very complete ORM, cast in the some mold as
Django.

`SQLAlchemy  <http://sqlalchemy.org/>`_ This provides a Pythonic definition
of SQL metadata and a mapping from the SQL metadata to Python class definitions.
This is a very, very rich approach, allowing you to straddle the SQL and Object
worlds explicitly.

`PyORQ <http://pyorq.sourceforge.net/>`_   This
is an older ORM with a few data types but a very "naked" use of overloaded
operators to perform queries.  Unlike the lambda overloading, the class provides
operators that are set operations for
queries.



**Non-Introspective Approaches** 


`Django <http://www.djangoproject.com/>`_ , for example, encodes attributes and
operators as keyword parameters to methods.  It doesn't look inside the Python
code, but parses the keywords.

`PyDO2 <http://skunkweb.sourceforge.net/>`_
encodes the query explicitly, using functions that mirror SQL operators or
tuples that contain string names for the
functions.

`QLime <http://www.qlime.org/>`_   is an ORM with functional notation,
similar to PyDO2.

`ORM <http://www.tux4web.de/computer/software/orm/>`_  (the Object-Relational Membrane) mostly
captures SQL metadata in Python.

`DBClass <http://projects.almad.net/dbclass>`_
is focused on an easy way to hack around with SQL queries (to get data from
procedures and so on).

`Axiom <http://divmod.org/trac/wiki/DivmodAxiom>`_  is an object database, or alternatively,
an object-relational mapper.  It depends on `Epsilon <http://divmod.org/trac/wiki/DivmodEpsilon>`_ .



The
Python wiki page on `Higher Level Database Programming <http://wiki.python.org/moin/HigherLevelDatabaseProgramming>`_   has
additional notes and products that are high
level.



**Garden-Variety Relational Access** 

All of these modules
provide the standard `DB-API <http://www.python.org/dev/peps/pep-0249/>`_  (PEP 249) interface to a SQL database.




The most visible access layer product
is `mx.ODBC <http://www.egenix.com/files/python/eGenix-mx-Extensions.html>`_  for bare ODBC connectivity.  This has
the advantage of wide portability, and the disadvantage of the narrow ODBC
interface.



`PDO <http://pdo.neurokode.com/>`_  wraps a
variety of other access methods into a single, combined package.  I'm not
precisely sure why it adds another interface layer, but it appears to simply do
away with Cursor objects.  However, it does provide a nice list of DB-API 2.0
modules for direct SQL access.



`MySQLdb <http://sourceforge.net/projects/mysql-python>`_  for
MySQL

`PySQLite <http://initd.org/tracker/pysqlite>`_  and `APSW <http://www.rogerbinns.com/apsw.html>`_
are for the ultra-lightweight SQLite
RDBMS.

The `PostgresPy <http://python.projects.postgresql.org/>`_   project will address many PostgreSQL
topics.  `PyGreSql <http://www.pygresql.org/>`_  (aka pgdb), `psycopg <http://www.initd.org/projects/psycopg1>`_ , `PoPy <http://www.zope.org/Members/tm/PoPy>`_ ,
`bpgsql <http://barryp.org/software/bpgsql>`_ .

`kinterbasdb <http://kinterbasdb.sourceforge.net/>`_  Firebird and Borland's
Interbase

`pyDB2 <http://sourceforge.net/projects/pydb2/>`_
DB/2

`cx_Oracle <http://www.cxtools.net/default.aspx?nav=cxorlb%22%20target=%22NewWindow>`_
Oracle

`adodbapi <http://adodbapi.sourceforge.net/>`_
Python access to the MS Windows ADO
interface



The Python wiki page on `Database Interfaces <http://wiki.python.org/moin/DatabaseInterfaces>`_  also has a list of these
product-specific access
modules.



**Recommendations** 

Rule
1.  Do development with SQLite.  Why? Eschew Features.  Focus on RDBMS for
relational store, focus on Python for processing.  Stored Procedures and
Triggers are a product-specific mine-field.  Once the model passes unit tests,
move to another RDBMS that supports concurrent
users.



Rule 2.  For OLTP, use an
OR-Mapping and stay away from naked SQL.  However (and this is a big however)
you will likely be supporting ad-hoc reporting through SQL-based report writers.
There are two extemes.  At one end is Deja-Vu, which may be too far from the
underlying SQL.   The other end begins with SQLAlchemy, which may expose too
much SQL; ORM and DBClass may be too light on object
features.



Rule 3.  For OLAP, you have
two kinds of applications.  Some parts (like dimension conformance) can use an
OR-Mapping because they are OLAP-like.  For some loading, aggregation and
extraction, use direct SQL drivers for the chosen product.  For the large-volume
fact-oriented loads, use the vendor-supplied bulk loader.  Portability is not
your concern.








