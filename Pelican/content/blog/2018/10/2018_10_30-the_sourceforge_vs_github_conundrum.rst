The SourceForge vs. GitHub Conundrum
====================================

:date: 2018-10-30 08:00
:tags: open source,stingray reader,github,source forge
:slug: 2018_10_30-the_sourceforge_vs_github_conundrum
:category: Literate Programming
:status: published

Or "When is it time to move?"


I've got https://sourceforge.net/projects/stingrayreader/ which has
been on SourceForge since forever.


Really since about 2014. Not that long. But. Maybe long enough?


The velocity of change is relatively slow.


However.


(And this is a big however.) SourceForge seems kind of complicated
when compared with Github.


It's not a completely fair comparison. SourceForge has a \*lot\* of
features. I don't use very many of those features.


The troubling issues are these.


1.  Documentation.
    SourceForge -- while it has a Git interface --
    doesn't handle my documentation very well. Instead of a docs
    directory, I do a separate upload of the HTML. It's inelegant.
    SourceForge may handle this more smoothly nowadays. Or maybe I should
    switch to readthedocs?


2.  The Literate Programming Workflow.
    There's an extra step (or two)
    in LP workflows. The PyLit3 synchronization to create the working
    Python from the RST source. This is followed by the ubiquitous steps
    creation of a release, creation of a distribution, and the upload to
    PyPI. I don't have an elegant handle on this because my velocity of
    change is so low. SourceForge imposed a "make your own ZIP file"
    mentality that could be replaced by a nicer "use PyPI" approach.


3.  Clunky Design Issue.
    I've uncovered a clunky, stateful design
    problem in the StingrayReader. I really really really need to fix it.
    And while fixing it, why not move to Github?


4.  Compatibility Testing.
    The StingrayReader seems to work with
    Python 3.5 and up. I don't have a formal Tox suite. I think it works
    with a number of versions of XLRD. And it \*should\* be amenable to
    other tools for Excel processing. Not sure. And (until I start using
    tox) can't tell.


5.  Type Hints.
    See #3. The stateful design problem can be finessed
    into a much more elegant use of NamedTuples. And then mypy can be
    used.


6.  Unit Tests.
    Currently, the testing is all unittest.TestCase. I
    really want to convert to pytest and simplify all of it.


7.  Lack of a proper workflow in the first place.
    See #2. It's a
    more-or-less sitting in the master branch of a git repo that's part
    of SourceForge. That's kind of shabby.


8.  Version Numbering Vagueness.
    When I was building my own Zip
    archives from the code manually (because that's the way SourceForge
    worked.) I wasn't super careful about semantic versioning, and I've
    been release patch-number versions for a while. Which is wrong. A few
    of those versions included new features. Minor, but features.


But. One tiny new feature. So. It will be release 4.5.
See https://sourceforge.net/p/stingrayreader/blog/2018/10/moving-to-github/
for status, also


