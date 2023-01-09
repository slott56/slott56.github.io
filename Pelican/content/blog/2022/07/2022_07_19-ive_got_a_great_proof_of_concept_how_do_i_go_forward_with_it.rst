I've got a great Proof-of-Concept. How do I go forward with it?
===============================================================

:date: 2022-07-19 08:00
:tags: enterprise,#python
:slug: 2022_07_19-ive_got_a_great_proof_of_concept_how_do_i_go_forward_with_it
:category: Technologies
:status: published

This is the best part about Python -- you can build something quickly.
And it really works.

But.

What are the next steps?

While there are a \*lot\* of possibilities, I'm focused on an
"enterprise work group" application that involves a clever web
service/RESTful API built in Flask. Maybe with NLP.

Let me catalog a bunch of things you might want to think about to
"productionize" your great idea. Here's a short list to get started.

-  File System Organization
-  Virtual Environments
-  Unit Testing
-  Integration Testing
-  Acceptance Testing
-  Static Analysis
-  Tool Chain
-  Documentation

| Let's dive into each one of these. Then we'll look at Flask
  deployments.

File System Organization
------------------------

When you're gotten something to work, the directory in which it works
is sometimes not organized ideally. There are a lot of ways to do
this, but what seems to work well is a structure like the following.

- Some parent directory. Often in Git

 - ``src`` -- your code is here

 - ``tests`` -- your tests are here

 - ``docs`` -- your documentation will be here

 - ``requirements.txt`` -- the list of packages to install. Exact,

 - ``requirements-dev.txt`` -- the list of packages used for maintenance and development

 -  ``environment.yml`` -- another list of packages in conda format

 - ``pyproject.toml`` -- this has your tox setup in it

 - ``Makefile`` -- sometimes helpful

Note that a lot of packages you see have a ``setup.py``.  This is
**only** needed if you're going open source your code. For
enterprise projects, this is not the first thing you will focus on.
Ignore it, for now.

Virtual Environments
--------------------

When you're developing in Python you may not even worry about virtual
environments. You have Python. It works. You downloaded NLP and Flask.
You put things together and they work.

The trick here is the Python ecosystem is vast, and you have (without
really observing it closely) likely downloaded a lot of projects.
Projects that depend on projects.

You can't trust your current environment to be reliable or repeatable.
You'll need to use a virtual environment manager of some kind.

Python's built-in virtual environment manager ``venv`` is readily
available and works nicely.
See https://docs.python.org/3/library/venv.html  It's my second choice.

My first choice is **conda**. Start with
**miniconda**. https://docs.conda.io/en/latest/miniconda.html. Use this
to assemble your environment and retest your application to be sure
you've got everything.

You'll be creating (and destroying) virtual environments until you get
it right. They're cheap. They don't impact your code in any way. Feel
free to make mistakes.

When it works, build conda's environment.yml file and the
requirements.txt files. This will rebuild the environment.  You'll use
them with **tox** for testing.

If you don't use conda, you'll omit the environment.yml.  Nothing else
will change.

Unit Testing
------------

Of course, you'll need automated unit tests. You'll want 100% code
coverage. You \*really\* want 100% logic path coverage, but that's
aspirational. 100% code coverage is a lot of work and uncovers enough
problems that the extra testing for all logic paths seems unhelpful.

You have two built-in unit testing toolsets: doctest and unittest. I
like doctest. https://docs.python.org/3/library/doctest.html

You'll want to get **pytest** and the **pytest-cov** add-on
package. https://docs.pytest.org/en/6.2.x/contents.html  https://pytest-cov.readthedocs.io/en/latest/.

Your test modules go in the tests directory. You know you've done it
right when you can use the **pytest** command at the command line and it
finds (and runs) all your tests.

This is part of your requirements-dev.txt file.

Integration Testing
-------------------

This is unit testing without so many mocks. I recommend using pytest for
this, also. The difference is that your "fixtures" will be much more
complex. Files. Databases. Flask Clients. Certificates. Maybe starting
multiple services. All kinds of things that have a complex setup and
perhaps a complex teardown, also.

See https://docs.pytest.org/en/6.2.x/fixture.html#yield-fixtures-recommended
for good ways to handle this more complex setup and teardown.

Acceptance Testing
------------------

Depending on the community of users, it may be necessary to provide
automated acceptance tests. For this, I recommend **behave**.
https://behave.readthedocs.io/en/stable/ You're can write the test cases
in the Gherkin language. This language is open-ended, and many
stakeholders can contribute to the test cases. It's not easy to get
consensus sometimes, and a more formal Gherkin test case lets people
debate, come to an agreement, and prioritize the features and scenarios
they need to see.

This is part of your requirements-dev.txt file.

Static Analysis
---------------

This is an extra layer of checking to be sure best practices are being
followed. There are a variety of tools for this. You \*always\* want to
process your code through
**black**. https://black.readthedocs.io/en/stable/

Some folks love **isort** for putting the imports into a canonical
order.  https://pycqa.github.io/isort/

**Flake8** should be used to be sure there's no obviously bad
programming practices. https://flake8.pycqa.org/en/latest/

I'm a huge fan of type hints. I consider **mypy** to be
essential. https://mypy.readthedocs.io/en/stable/  I prefer "--strict"
mode, but that can be a high bar.

Tool Chain
----------

You can try to manage this with **make**. But don't.

Download **tox**, instead.  https://tox.wiki/en/latest/index.html

The point of tox is to combine virtual environment setup with testing in
that virtual environment. You can -- without too much pain -- define
multiple virtual environments. You can then test the various releases of
the various packages your project depends on in various combinations.
This is how to manage a clean upgrade.

1. Figure out the new versions.

2. Setup tox to test existing and new.

3. Run tox.

I often set the tox commands to run black first, then unit testing, then
static analysis, ending with mypy --strict.

When the code is reformatted by black, it's technically a build failure.
(You should have run **black** manually before running **tox**.)
When **tox** works cleanly, you're ready to commit and push and pull
request and merge.

Documentation
-------------

Not an after-thought.

For human documents, use Sphinx. https://www.sphinx-doc.org/en/master/

Put docstrings in every package, every module, every class, every
method, and every function. Summarize \*what\* and \*why*. (Don't
explain \*how*: people can read your code.)

Use the autodoc feature to create the API reference documentation from
the code. Start with this.

Later, you can write a README, and some explanations, and installation
instructions, and all the things other people expect to see.

For a RESTful API, be sure to write an OpenAPI specification and be sure
to test against that spec. https://www.openapis.org. While a lot of the
examples are complicated, you can easily use a small subset to describe
your documents, the validation rules, and the transactions. You can add
the security details later. They're part of your web server, but they
don't need an extensive OpenAPI documentation at the beginning.

Flask Deployments
-----------------

Some folks like to define a flask application that can be installed in
the Python virtual environment. This means the components are on the
default ``sys.path`` without any "extra" effort. (It's a fair amount of
effort to begin with. I'm not sure it's worth it.)

When you run a flask app, you'll be using some kind of engine. NGINX,
uWSGI, GUnicorn, etc. (GUnicorn is very nice. https://gunicorn.org).

See https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/.

In all cases, these engines will "wrap" your Flask application. You'll
want to make your application visible by setting the ``PYTHONPATH``
environment variable, naming your ``src`` directory. Do not run from
your project's directory.

You will have the engine running in some distinct ``/opt/the_app`` or
``/Users/the_app`` or ``/usr/home/the_app`` or some such directory,
unrelated to where the code lives. You'll use GUnicorns command-line
options to locate your app, wherever it lives on the filesystem.
GUnicorn will use ``PYTHONPATH`` to find your app. Since web servers
often run as nobody, you'll need to make sure your code base is
readable. But. Not. Writable.





