CI/CD DevOps and Python
=======================

:date: 2017-11-14 08:00
:tags: DevOps,#python,continuous integration,continuous deployment
:slug: 2017_11_14-cicd_devops_and_python
:category: Technologies
:status: published


See https://www.slideshare.net/ITRevolution/does-sfo-2016-topo-pal-devops-at-capital-one for
the 16 gates that separate a good idea from secure, productive use of
software. While a lot of DevOps folks like the idea, when it comes to
implementing it for Python apps, they get confused.

The confusion seems to stem from Python's lack of a proper "build"
step in the CI/CD pipeline. I've had the "everything involves a build"
argument and the "well setup.py is analogous to a build" arguments. I
have to acquiesce to these positions as part of making progress. In
this case, reasoning by analogy can be misleading.

I want to focus on the two gates that are part of the code itself,
separate from the rest of the pipeline.

-  Static Analysis

-  >80% Code Coverage (which implies Unit Tests)




Unit Testing
------------


My preference is to run the unit test suite first and get that out of
the way. If the unit test suite fails, or fails to cover 80% of the
code, any other considerations are moot.

I like Git triggers based on Pull Requests (PR's) and Merge to Master
for checking these two conditions. I like the idea that a PR can't be
discussed until unit tests pass. They can also be part of whatever
other pipeline is going on, but I like them to be done early and
often.

(I worked on a sprint team where the PR unit test wasn't trusted by
one of the devs: he'd carefully check out the branch and rerun the
unit tests. His comments were good, so the extra effort paid off. I
guess.)

After flirting with a lot of frameworks, I'm happiest with
`py.test <https://docs.pytest.org/en/latest/>`__. I like the
`py.test-coverage <http://pytest-cov.readthedocs.io/en/latest/>`__
plug-in and the
`py.test-BDD <https://github.com/pytest-dev/pytest-bdd>`__ plug-in.

Yes. We have acceptance tests for our features written in Gherkin. And
we have pytest fixtures that are used by pytest-bdd to process the
scenarios in the Gherkin feature files. It actually works out nicely
because we have a cucumber.json file that makes everyone happy that
we've run an acceptance test suite along with our unit test suite.

What's important is the coverage report is painless and automatic.

And it's compatible with the Ruby-based cucumber tool without
involving any actual ruby.

For integration testing, we use
`Behave <http://pythonhosted.org/behave/>`__. This is a bit more
cumbersome than pytest-bdd, but it's appropriate for the
bigger-picture testing where we have a docker cluster and have to see
a number of "Then" steps to confirm operations spread across a suite
of microservices.

The goofy question that often leads to endless confusion is the
relationship between unit testing and "build." The setup.py setup
definition includes a \`tests_require\` parameter. This \*should be\*
all that's needed to do \`python setup.py test\`, which \*should be\*
all that's involved in testing.

Is it a "build"? No. But. You can tell the DevOps folks it's a build
if it makes them happy.

Static Analysis
---------------


There are several kinds of static analysis. Folks who work in Java are
used to having Sonar analysis performed. This is above and beyond the
static analysis already performed by the compiler. It seems excessive
to me, but folks deploying Java seem to like it.

For Python, there are two important static analysis tools. And this is
another source of profound confusion for DevOps folks new to Python.

-  pylint (I prefer this over pyflakes and pep8. See `About style guide
   of python and linter
   tool <https://blog.sideci.com/about-style-guide-of-python-and-linter-tool-pep8-pyflakes-flake8-haking-pyling-7fdbe163079d>`__
   for a long list of tools.)

-  mypy


I like to extract the last line of the pylint output and use that
numeric score as the "bottom line" on static analysis part 1. While
the default setting is 9.5, that can be a challenge, and we prefer
9.0 as well as some local pylintrc modifications to modify some
checkers (e.g., set line length to 120.)


For mypy, it's a little bit more complex. We're still fumbling around
here.


Ideally, the type hints are all clean and mypy has nothing to say. We
can, of course, fix any errors by claiming everything uses Any and
returns Any and every assignment statement sets an Any value. But
that's so wrong.


There are (still) modules which require typeshed stub definitions.
Ideally, we'd provide these. This would be better than using Any as a
hack-around. While good, it's a lot of work.


For now, I think it's sensible to have two "pass" rules for mypy:
clean or typeshed error. If mypy is silent, that's perfect. If mypy
can't find stubs in typeshed, we can let this go for now and log an
issue from the CI/CD pipeline to note the presence of technical debt.


In the best of all worlds, we'd fork the package, fix the type hints,
and put in a PR. That's a lot better than using typeshed to work
around the lack of hints.


And, of course, there's the "build" question. For mypy to work, the
dependencies (or their typeshed stubs) must be present. We wind up
doing a ``python setup.py install`` to build out the requirements. Is
this a "build"? Maybe. You can tell the DevOps folks it's a build if
it makes them happy.


If you want idempotent server (or container) builds, you'll need to
be sure that you pin specific versions. It can help to break this
into two parts:


-  a requirements.txt with specific versions

-  a generic version-free high-level list in setup.py


The reason for this separation is to make it easy to do
a ``pip install`` or ``conda create`` from the detailed requirements. Once
that's out of the way, the ``python setup.py`` will run very
quickly. If you're working with Docker containers,
the ``pip install`` (or ``conda create``) can be part of the Dockerfile, and
then tests or static analysis can be run separately, after the
initial wave of installations.






