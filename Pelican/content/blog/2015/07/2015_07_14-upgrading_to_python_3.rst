Upgrading to Python 3
=====================

:date: 2015-07-14 08:00
:tags: #python
:slug: 2015_07_14-upgrading_to_python_3
:category: Technologies
:status: published


Folks who don't use Python regularly -- the folks in TechOps, for
example -- are acutely aware that the Python 3 language is
"different," and the upgrade should be done carefully. They've done
their homework, but, they're not *experts* in everything.

They feel the need to introduce Python 3 slowly and cautiously to
avoid the remote possibility of breakage. Currently, the Python 3
installers are really careful about avoiding any possible conflicts
between Python 2 and 3; tiptoeing isn't really necessary at all.

I was stopped cold from having Python 3 installed on a shared server
by someone who insisted that I enumerate which "features" of Python 3
I required. By enumerating the features, they could magically decide
if I had a real need for Python 3 or could muddle along with Python 2.

The question made precious little sense for many reasons: (1) many
things are backported from 3 to 2, so there's almost nothing that's
exclusive to Python 3; (2) both languages are Turing-Complete, so any
feature in language could (eventually) be built in the other; (3) I
didn't even know languages has "features." The reason they wanted a
feature list was to provide a detailed "no" instead of a generic "no."

Either way, the answer was "no." And there's no reason for that.

In all cases, we can install Python 3 now. We can start using it now.
Right now.

Folks who actually use Python regularly -- me, for example -- are well
aware that there's a path to the upgrade. A path that doesn't involve
waiting around and slowly adopting Python 3 eventually (where
eventually ≈ never.)

#.  Go to your enterprise GitHub (and the older enterprise SVN and
    wherever else you keep code) and check out every single Python
    module. Add this line: ``from __future__ import print_function``,
    division, unicode_literals. Fix the print statements. Just that.
    Touch all the code once. If there's stuff you don't want to touch,
    perhaps you should delete it from the enterprise GitHub at this time.

#.  Rerun all the unit tests. This isn't as easy as it sounds. Some
    scripts aren't properly testable and need to be refactored so that
    the top-level script is made into a function and a separate doctest
    function (or module) is added. Or use **nose**. Once you have an
    essentially testable module, you can add doctests as needed to be
    sure that any Python 2 division or byte-fiddling work correctly with
    Python 3 semantics for the operators and literals.

#.  Use your code in this "compatibility" mode for a while to see if
    anything else breaks. Some math may be wrong. Some use of bytes and
    Unicode may be wrong. Add any needed doctests. Fix things in Python 2
    using the ``from __future__`` as a bridge to Python 3. It's not a
    conversion. It's a step toward a conversion.

This is the kind of thing that can be started with an enterprise hack
day. Make a list of all the projects with Python code. Create a
central "All the Codes" GitHub project. Name each Python project as
an issue in the "All the Codes" project. Everyone at the hack day can
be assigned a project to check out, tweak for compatibility with some
of the Python 3 features and test.

You don't even need to know any Python to participate in this kind of
hack day. You're adding a line, and converting print statements to
``print()`` functions. You'll see a lot of Python code. You can ask
questions of other hackers. At the end of the day, you'll be
reasonably skilled.

Once this is done, the introduction of Python3 will not be a shock to
anyone's system. The ``print()`` functions will be a thing. Exact
division will be well understood. Unicode will be slightly more
common.

And -- bonus -- everything will have unit tests. (Some things will be
rudimentary place-holders, but that's still a considerable
improvement over the prior state.)








