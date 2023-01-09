Enterprise Python -- Some initial thoughts 
===========================================

:date: 2022-08-16 08:00
:tags: #python,enterprise
:slug: 2022_08_16-enterprise_python_some_initial_thoughts
:category: Technologies
:status: published

In the long run, I think there's a small book here. See `8 reasons
Python will rule the enterprise — and 8 reasons it won’t \|
InfoWorld <https://www.infoworld.com/article/3604473/8-reasons-python-will-rule-the-enterprise-and-8-reasons-it-wont.html%20>`__.
The conclusion, "Teams need to migrate slowly into the future, and
adopting more Python is a way to do that," seems to be sensible. Some of
the cautionary tales along the way, however, don't make as much sense.

TL;DR. There are no reasons to avoid Python. Indeed, the 8 points
suggest that Python is perhaps a smart decision.

I want to focus on the negatives part of this because some of them are
wrong. I think there's a "technology hegemony" viewpoint where
everything in an enterprise must be exactly the same. This tends to
prevent creative solutions to problems and mires an enterprise into
fighting problems that are inherent in bad technology choices. Also, I
think there's an enterprises are run by idiots subtext.

1. **Popularity**.
    Really this is about having polyglot software
    portfolio. The reasoning appears to be that a polyglot software
    portfolio is impossible to maintain because (1) no one can learn an old
    language, and (2) software will never be rewritten from an obsolete
    language to a modern language. If these are both true, it appears the
    organization is full of idiots. The notion that a polyglot tech stack
    **must** devolve into chaos seems to ignore the endless chain of
    management decisions that are required to create chaos. Leaving obsolete
    tech in place isn't a consequence of the tech, or the tech's lack of
    compatibility, it's a management decision to enshrine bad ideas, frozen
    in amber, forever.

2. **Scripting Languages**.
    Specifically, the spreadsheet is already the
    *de facto* scripting language of choice, and nothing can be done about
    it. Nothing. No one can learn to use Jupyter Lab to do business
    analytics. If this is true, it appears that the organization is full of
    idiots. Python will not replace all spreadsheets. A pandas data frame
    will replace an opaque macro-filled nightmare with code that can be unit
    tested. Imagine unit testing a spreadsheet. Consider the possibilities
    of expanding business analysis work to include a few test cases; not
    100% code coverage, but a few test cases to confirm the analytical
    process was implemented consistently.

3. **Dynamic Languages**.
    Specifically, dynamic languages are useless
    for reliable software because there's no comprehensive type checking
    across some interfaces. Which begs the question of why there are
    software failures in statically typed languages. More importantly,
    complaining about dynamic languages raises important questions about
    integration and acceptance testing procedures in an organization in
    general. All languages require extensive test suites for all developed
    code. All languages benefit from static analysis. Sometimes the compiler
    does this, sometimes external tools do the linting. Sometimes folks use
    both the compiler and linters to check types. If we are sure dynamic
    languages will break, are we equally sure statically typed languages
    cannot break? Or, do we take steps to prevent problems? I think we tend
    to take a lot of steps to make sure software works.

4. **Tooling**.
    I can't figure this point out. But somehow C++ or Java
    have better tools for managing large source code bases. There are no
    details behind this claim, so I'm left to guess. I would suggest that
    the "incremental recompilation" problem of large C++ (and Java) code
    bases is its own nightmare. Folks go to great lengths to architect C++
    so that an implementation change does not require recompilation of
    everything. While this could be seen as "evolved to handle the jobs that
    enterprise coders need done", I submit that there's a deeper problem
    here, and stepping away from the compiler is a better solution than
    complex architectures. See Lakos `Large-Scale C++ Software
    Design <https://www.oreilly.com/library/view/large-scale-c-volume/9780133927573/>`__ for
    some architectural features that don't solve any enterprise problem, but
    solve the scaling problem of big C++ applications. This bumps into the
    micro-services/monolith discussion, and the question of carefully
    testing each interface. None of which has anything to do with Python
    specifically.

5. **Machine Learning and Data Science**.
    These are fads, apparently.
    I'm not sure I can respond to this, since it has little to do with
    Python. Of course, Python has one of the most complete data science
    toolsets, so perhaps avoiding data science makes it easier to avoid
    Python.

6. **Rapid Growth**.
    The growth of Python is rapid, and there's no
    promise of endless backwards compatibility. This is a consequence of
    active development and learning. I think it's better than the endless
    backwards compatibility that leads to JavaScript's list of WATs. Or the
    endless confusion between java.util.date and Joda-Time. The idea that no
    one will ever look at the Enterprise code base for Common
    Vulnerabilities and Exposures seems to indicate a lack of concern for
    reliability or security. Since the entire compiled code base has to be
    checked for vulnerabilities, why not also check the Python code base for
    ongoing upgrades and changes and enhancements? Is code really written
    once and never looked at again? If so, it sounds like an organization
    run by idiots.

7. **Python Shipped With Some OS's**.
    There's a long story of woe that
    stems from relying on the OS-supplied Python. The lesson learned here is
    **Never Rely on the OS Python; Always Install Your Own**. This doesn't
    seem like a reason to avoid Python in the enterprise. It seems like an
    important lesson learned for all software that's not part of the OS:
    always install your own. I've been using
    `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ to spin
    up Python environments and absolutely love it.

8. **Open Source Software**.
    Agreed. Nothing to do with Python
    specifically. Everything to do with tech stack and architecture. The
    question of using Open Source in the first place doesn't seem difficult.
    It's a well-established way to reduce start-up costs for software
    development.

Of the eight points, two seem to be completely generic issues. Yes,
Machine Learning is new, and yes, choices must be made. The two
questions around scripting and dynamic languages seem specious; all
programming requires careful design and testing. The Python shipped with
the OS is a non-concern; the lesson learned is clear.

We have have three remaining points:

#. **Polyglot Portfolio** (From pursuing popularity.) This is already
   the case in most Enterprises, and needs to be managed through
   aggressive retiring of old software. I may have taken decades to
   build that old app, but it often takes months to rewrite it in a new
   language. The legacy app provides acceptance test cases; it's often
   filled with cruft and detritus of old decisions.

#. **Tooling**. Agreed. Tooling is important. Not sure that Java or C++
   have a real edge here, but, tooling is important.

#. **Growth and Change**. Python's rapid evolution requires active
   management. An enterprise must adopt a YBYO (You Build it You Own it)
   attitude so that every level of management is aware of the components
   they're responsible for. CVE's are checked, Python PEP's are checked.
   Tools like `tox <https://tox.wiki/en/latest/>`__ or
   `nox <https://nox.thea.codes/en/stable/>`__ are used to build (and
   rebuild) virtual environments.


If these seem like a high bar, perhaps there are deeper issues in the
enterprise. If adding Yet Another Language is a problem, then it's
time to start retiring some languages. If Adding Another Tool is a
problem, it's worth examining the existing tool chain to see why it's
such a burden. If the idea of change is terrifying, perhaps the
ongoing change is not being watched carefully enough.





