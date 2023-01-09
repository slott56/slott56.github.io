The "Build Script" Idea
=======================

:date: 2017-01-03 08:00
:tags: sphinx,#python,pylint,pytest,tools,mypy
:slug: 2017_01_03-the_build_script_idea
:category: Technologies
:status: published


In compiled languages, the build script or makefile is pretty
important. Java has maven (and gradle and ant) for this job.

Python doesn't really have much for this. Mostly because it's
needless.

However.

Some folks like the idea of a build script. I've been asked for
suggestions.

First and foremost: **Go Slow**. A build script is **not** essential.
It's barely even helpful. Python isn't Java. There's no
maven/gradle/ant nonsense because it isn't necessary. Make is a poor
choice of tools for reasons we'll see below.

For folks new to Python, here's the step that's sometimes important.

python setup.py sdist bdist_wheel upload

This uses the source distribution tools (sdist) to build a "wheel" out
of the source code. That's the only thing that's important, and even
that's optional. The source is all that really exists, and a Git Pull
is the only thing that's truly **required**.

Really. There's no compilation, and there's no reason to do any
processing prior to uploading source.

For folks experienced with Python, this may be obvious. For folks not
so experienced, it's difficult to emphasize enough that Python is just
source. No "class" files. No "jar" files. No "war" files. No "ear"
files. None of that. A wheel is a Zip archive that follows some simple
conventions.

Some Preliminary Steps
----------------------


A modicum of care is a good idea before simply uploading something.
There are a few steps that make some sense.

#. Run pylint to check for obvious code problems. A low pylint score
   indicates that the code needs to be cleaned up. There's no magically
   ideal number, but with a few judicious "disable" comments, it's easy
   to get to 10.00.

#. Run mypy to check the type hints. If mypy complains, you've got
   potentially serious problems.

#. Run py.test and get a coverage report. There's no magically perfect
   test coverage number: more is better. Even 100% line-of-code coverage
   doesn't necessarily mean that all of the potential combinations of
   logic paths have been covered.

#. Run sphinx to create documentation.


Only py.test has a simple pass-fail aspect. If the unit tests don't
pass: that's a clear problem.

The Script
----------




Using **make** doesn't work out terribly well. It can be used, but it
seems to me to be too confusing to set up properly.




Why? Because we don't have the kind of simple file relationships with
which make works out so nicely. If we had simple \*.c -> \*.o ->
\*.ar kinds of relationships, make would be perfect. We don't have
that, and this seems to make **make** more trouble than it's worth.
Both pylint and py.test keep history as well as produce reports.
Sphinx is make-like already, which is why I'm leery of layering on
the complexity.




My preference is something like this:




::

      import pytest
      from pylint import epylint as lint
      import sphinx
      from mypy.api import api

      (pylint_stdout, pylint_stderr) = lint.py_run('*.py', return_std=True)
      print(pylint_stdout.getvalue())

      result = mypy.api.run('*.py')

      pytest.main(["futurize_both/tests"])

      sphinx.main(['source', 'build/html', '-b', 'singlehtml'])




The point here is to simply run the four tools and then look at the
output to see what needs to be fixed. Circumstances will dictate
changes to the parameters being used. New features will need
different reports than bug fixes. Some parts of a project will have
different focus than other parts. Conversion from Python 2 to Python
3 will indicate a shift in focus, also.

The idea of a one-size-fits-all script seems inappropriate. These
tools are sophisticated. Each has a distinctive feature set. Tweaking
the parameters by editing the build script seems like a simple,
flexible solution. I'm not comfortable defining parameter-parsing
options for this, since each project I work on seems to be unique.

**Important**. Right now, mypy-lang in the PyPI repository and mypy
in GitHub differ. The GitHub version includes an **api** module; the
PyPI release does not include this. This script may not work for you,
depending on which mypy release you're using. This will change in the
future, making things nicer. Until then, you may want to run mypy
"the hard way" using **subprocess.check_call()**.

In enterprise software development environments, it can make sense to
set some thresholds for pylint and pytest coverage. It is very
helpful to include type hints everywhere, also. In this context, it
might make sense to parse the output from lint, mypy, and py.test to
stop processing if some quality thresholds are met.

As noted above: **Go Slow**. This kind of tool automation isn't
required and might actually be harmful if done badly. Arguing over
pylint metrics isn't as helpful as writing unit test cases. I worry
about teams developing an inappropriate focus on pylint or coverage
reports -- and the associated numerology -- to the exclusion of
sensible automated testing.

I think tools like https://pypi.python.org/pypi/pytest-bdd might be
of more value than a simplistic "automated" tool chain. Automation
doesn't seem as helpful as clarity in test design. I like the BDD
idea with Gherkin test specifications because the Given-When-Then
story outline seems to be very helpful for test design.





