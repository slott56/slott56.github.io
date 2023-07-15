Behave Tests and Fixtures
#################################

:date: 2023_01_27 08:00
:tags: books,software design,test driven development
:slug: 2023_01_27-behave_tests_and_fixtures
:category: Python
:status: published

BLUF
-----

**Behave** fixtures totally rock for testing
complex applications.

I had been doing them wrong. Doing them right is simpler.

History
--------

I'm a fan of the Gherkin language for specifying
the behavior of software.

::

    Scenario: Works for Me

    Given a configuration
    When a request is made
    Then the response can be evaluated.

I love this.

What I particularly love is the way **Behave's** ``steps`` package
provide implementations for the individual steps of the scenario.

The steps can be organized around technical needs,
where the features are organized around the user's experience
when operating the software.

The Non-Fixture Approach
-------------------------

For a long time, I used the ``Given`` step and an ``after_scenario()``
function in **Behave's** environment module to create and destroy fixtures.

::

    Scenario: Test with Mock API

    Given a server running on http://127.0.0.1:8000
    And the server has the resource requested
    When a client makes some random request or other
    Then the response is a tidy bit of data the user just loves

The ``Given`` step would seed the context with details used
to configure a tiny, specialized service built with
Python's ``http.server`` module. This separate subprocess would provide
an appropriate response for this scenario.

The mock server srequired creating a request handling class hierarchy
with reusable and extensible choices for the
various scenarios and features.
Often only one or two paths would be handled, since that's all
a scenario needed.

The context parameters were turned into command-line options.
The mini server was started by the ``When`` step and stopped
(eventually) after the scenario.

This was workable. But. Ultimately. Dumb.

Fixtures
---------

**Behave** has a much, much better way to configure
and manage fixtures. This is great for tests that
databases or RESTful API servers or other, separate processes
to collaborate with.

Fixtures.

::

    @fixture.the_mock_server
    Scenario: Test with Mock API

    Given a server running on http://127.0.0.1:8000
    And the server has the resource requested
    When a client makes some random request or other
    Then the response is a tidy bit of data the user just loves

There's one change to the scenario -- a tag with ``@fixture.`` to positively identify
a fixture required for this scenario to make sense.

When reviewing the Gherkin with users, the ``@fixture`` tag
is easy to explain. There are often other tags throughout
the scenarios. A ``@slow`` tag, for example, might be used for those
scenarios that involve throttling or timeouts. A ``@future`` tag
for those options that aren't required but can be tested
to observe development progress. For one project I had a ``@core`` tag
that recapitulated the examples in the documentation --- these **had** to work
exactly as shown.

Infrastructure
--------------

The fixture infrastructure has three parts.

1.  Our specific fixture-managing generator function. This will create the fixture, yield something, and then destroy the fixture. This precisely parallels the way **pytest** fixtures work.

2.  A ``before_tag()`` function in the environment to look for the tags and do any setup or logging required.

3.  The fixture itself. This is our specialized test-case server based on ``http.server``. It still uses a configuration file or command-line options -- or both -- to define some behavior required for the scenario.

What happens, then, is this.

1.  The ``before_tag()`` function is evaluated for every tag on every step.
    If a tag starts with ``"fixture."`` then, something special needs to be done.

2.  The ``before_tag()`` function will evaluate the ``behave.use_fixture()`` function to inject
    our specific fixture-managing generator function into the step processing.

3. The fixture will be created (and destroyed) as part of the scenario's execution.

(If you need details, see https://behave.readthedocs.io/en/stable/fixtures.html#fixture-cleanup-points)

The mapping from ``"fixture.this_special_api"`` to
a generator function named ``this_special_api()`` is kind
of trivial. So trivial that the examples in the **Behave**
documentation suggest you look these up in a map in
the simplest possible way.

::

    TAG_IMPLEMENTATIONS = {
        "the_mock_server": server_fixture_generator,
        "the_other_server": another_fixture_generator,
        "the_timeout_server": the_timeout_server
    }

    def before_tag(context, tag):
        if tag.startswith("fixture."):
            _, name = tag.split('.')
            use_fixture(TAG_IMPLEMENTATIONS[name], context)

There's a ``use_fixture_by_tag()`` function that may be considered to be simpler
than my example.

Now, we can add fixtures by writing a generator
function to create (and destroy) the fixture
and adding the new function to the ``TAG_IMPLEMENTATIONS`` mapping.

The fixture names are for users who might want to review
the scenarios. They're subject to the same kind of negotiation
the rest of the Gherkin terminology is. Sometimes, you'll
tweak the wording as the user's understanding (and needs)
evolve.

Cleanup
--------

When you have serious problems in your test implementation,
you'll have tiny cleanup issues.

For example, if your step implementation code is broken,
the test can crash without having executed all
the steps you anticipated.

This can mean a fixture isn't properly torn down.
It's a rare, but annoying thing to happen.

See https://behave.readthedocs.io/en/stable/fixtures.html#ensure-fixture-cleanups-with-fixture-setup-errors for
some solutions.

I'm a fan of leaving information about the fixture in the context,
and using ``after_scenario()`` or ``after_feature()`` functions
to kill long-running process in the rare case that a step failed.

The alternative, using ``add_cleanup()``, is -- perhaps -- nicer,
because it relies on a closure that doesn't clutter the
context with these little, technical overheads. (I find closures
a little awkward to debug, but, debugging is rarely needed
for this.)

Books
-----

Yes, this is for a book.
Stay tuned. Later this year.
