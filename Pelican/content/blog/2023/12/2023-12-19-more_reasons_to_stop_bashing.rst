More Reasons to Stop Bash-ing
===================================================

:date: 2023-12-19 08:01
:tags: shell,bash,unit-testing
:slug: 2023_12_19-more_reasons_to_stop_bashing
:category: Python
:status: published

There are many good reasons to use shell scripts.
Mostly, a script can be useful when it's an alias that launches an application.
Beyond that, I have doubts.

BLUF
----

Incumbency is a popular argument for bash.

It's not a good argument, however.

Use `invoke <https://pypi.org/project/invoke/>`_ and you'll be much happier.

Background
----------

See `When You Should Use Bash Over Python <https://dnastacio.medium.com/bash-over-python-39e0eba502f9>`_.

I'll start with the three "expressiveness" points.

-   **Syntax**: Python code is longer. While true, this isn't a reason to use bash. I have to reject this for two reasons.

    -   No one wins at code golf. Shorter code isn't better by any metric other than size. Bash syntax hides important details.

    -   The argument starts from the notion that there's a "better" way to express complicated structures, and the bash reflects better.
        Python, by being more explicit, is less good.

-   **Runtime**: Shell script interpreters are ubiquitous. True. Not a compelling argument, when we consider that bash scripts are untestable.

-   **Semantics**: There is a cognitive cost in converting bash to Python. Correct. Easy to avoid by avoiding the confusing and opaque bash abstractions.

    -   The argument (again) starts from the notion that the bash abstraction is a standard against which other languages -- by virtue of being different -- aren't as good.

The argument **for** bash is incumbency. Bash is installed, and because it's installed, it's better.

"Bash’s longevity is rooted in core strengths that still resonate in the technology industry".
I suggest the longevity is due entirely to it's incumbency.
It's not the **best** choice for anything.
It's a handy default choice because it's already installed.

And.  There's no easy way to unit test.

Let's move on to the other six reasons.

Some reasons for using bash
---------------------------

Here are the the detailed reasons for rejecting Python. Most of this isn't persuasive.
It's mostly about the incumbency of bash.

1.  Mastery Matters. Parts of this argument are true. Bash scripts seem to be uniformly bad because bad is a permitted style.
    They could be better, making use of clever things like functions and their obscure semantics.

    This doesn't make bash better. It only says that a lot of people write bad scripts.
    A lot of bash-bashing stems from seeing so many bad scripts.

2.  Bash is Everywhere. True. Incumbency may be helpful under certain situations.
    It's like learning how to compute logarithms so you can then add them to avoid multiplication.
    Yes. It does work. However. Calculators exist on this timeline; it's no longer 1617.

    -   "Sidestepping the discussions about the Python version to pick"? What discussion? Is this a "Python 2 v. Python 3" question? That's been answered.

    -   "the best way to install Python on a given environment"? Most linux distros have Python ready-to-go. That's best.

    -   "gymnastics to keep dependencies and environments in check"? This isn't hard, actually. Almost anything bash-related is in the standard library plus a few add-ons line `psutil <https://pypi.org/project/psutil/>`_.
        For a very complicated application with a tall stack of poorly-chosen dependencies, there's work involved.
        That application with a complicated set of installs isn't doing bash-like things, though.

    -   "fragmentation of Python runtime versions"? What fragmentation? Python is popular, and evolves quickly. Is evolution to new versions some kind of problem?

    -   "mutually exclusive dependency matrix"? Callback to gymnastics. A tall stack of poorly-chosen dependencies is an edge case. It's not the sweet spot for admin tasks often written as bad, untestable bash scripts.

3.  Secured Production Environments. This is hard. None of these difficulties are Python-related, however. It applies to every single application in the environment.
    Java requires installs for develolpers, too. So go Go and Rust. Air-gapped systems are hard to build.

    -   "whatever Python runtime environment you lock into a production environment"? Um. This is true for *all* applications.
        It has nothing to do with Python. This is configuration management. It's hard.

    -   "Running package managers safely inside a production environment is possible, but everything’s got a price". And the price is actually quite low.
        Further, this means building secured systems for software development. That's quite hard in all languages.
        The only language that wouldn't require extra downloads of new and useful packages would be Pascal, I think.

    -   "You could do [here documents] with a Python script, too, as long as it does not import any package not already installed in the system."
        Right. Most bash-related Python features are part of the standard library. This isn't daunting or even particularly difficult or complicated.
        And. With Python you can unit test.

4.  Container Runtimes. See #3. This is bash incumbency and configuration management from point 3, repeated. It's still challenging.

5.  The Universal Language of Platforms. The bash CLI is ubiquitous, it's ideal for bash. But it's not actually **ideal** in general.
    A Python library that offers access an application's API may be much easier to work with and involve far fewer weird
    leaps to make the CLI amendable to the relatively weak set of abstractions bash has available.

    -   "It would take a couple of days in syntactical and semantical translations to get a result with more lines of code that were less readable than its Bash counterpart".
        Again, the argument presumes the bash language is the gold standard. Starting with bash and enduring translating into Python involves a cost.
        It also had benefits, like the ability to test.
        Why not start with Python?
        "Less readable" is offered without further evidence. Again, this repeats the bash incumbency argument where smaller and older is inherently better.

        Further, the time spent writing Python is often time **well** spent getting the abstractions right,
        and understading use cases.

    -   "All original samples in the docs were written using the command-line interface."  Incumbency. And maybe lazy documentation writers in the vendor organization.
        "All Internet forums reference the command-line interface". Sigh. The "All" is disputable, but the point remains that using Python takes some effort.

6.  The End of the Line Is Not Scripted. (Not sure what this means.)
    There are two obstacles here, both of which seem specious at best.

    -   Mega CLI's. Just because a bash CLI is available does not make it "best."

        -   "every bit of function be wrapped with command-line interfaces."  While true, it ignores the fact
            that some packages are actually written in Python, and the bash interface is -- at best -- a hack
            for those folks who won't learn Python.

        -   Bash is everywhere. Incumbency does not make it better. It only makes it incumbent.

        -   Writing shell scripts is more accessible than writing a new application. A good straw-man.
            It throws Python scripting away as if we can't write a short, pithy, testable, reusable Python script.

        -   "open-source juggernauts..." like ``awk``, ``curl``, ``openssl``, ``jq``, and ``yq`` involves two issues.
            First, some programs like ``openssl`` are better left as stand-alone binaries used by a Python script.
            Second, programs like  ``awk``, ``jq``, and ``yq`` are the primary symptom of how unsuitable bash is for working with anything other
            than a trivial string of characters. Reliance on these add-on programs is one of the reasons why bash is so confusingly horrible.

    -   Operations Frameworks like Ansible, Terraform, and (not mentioned) Puppet. These require some scripting
        for integration. Having done it in Python, I can safely say Python works.

        And I could unit test it.

    Unrelated to the two obstacles is this nugget: "tuned for five decades of minimum resource utilization".
    I don't think this is true at all.

    The original Bourne ``sh`` wasn't very thrifty to begin with. It was constrained by the tiny size of early
    machines. And. The Linux technique of sharing the read-only code pages meant the costs could stay low.
    State management was environment variables and some OS settings (like the current working directory.)
    The bash program is bloatware by comparison to the Bourne shell.
    The use of the OS ``|`` operator forks subprocess after subprocess leading to crazy OS overheads
    for a "simple" ``app | awk | grep | sed > file`` operation.

Conclusion
----------

"In objective terms, regarding task automation for Cloud operations, it is hard to argue against Bash".

No. Actually. It's really easy.

-   The bash scripting language is opaque. Objectively, the syntax rules are quite obscure with complicated line-ending and quoting rules.
    Objectively, it's really difficult to understand the semantics of the operators like ``;``, ``|``, and ``&``.
    Why is ``;`` optional? Why can a line end with ``&``  or ``;`` but not end with ``|``?

-   Error-handling in bash is an unholy mess. Objectively, what does ``set -e`` do?
    Objectively, why are there so many return codes?

-   Unit testing is almost impossible. Objectively, no one should run a shell script without a test case.

-   Bash has almost no useful data structures beyond the string.
    Objectively, we can argue that there's a way to break strings on spaces to treat the string as an array.
    This is essentially Python ``.split()`` as the alternative data structure to the string.

-   Programs like ``expr`` and ``[`` are used widely and very difficult to understand.
    Objectively, the man pages for these programs are quite complicated.
    What looks like an expression isn't really. It's input to a separate binary that produces a result used by the shell's ``if`` construct.
    Objectively, this is confusing and unpleasant.

Programs like ``awk``, ``jq``, ``yq`` are used widely and can be difficult to understand.
They're -- technically -- separate binaries, part of the overall bash ecosystem of internal bash features and external binaries.
They do permit a kind of functional style on bash programming which is nice.
Objectively, this isn't all bad. Python, also, has functional programming features.

The ubiquity of the bash programming is undeniable. It's also terrible. Bash should be used cautiously.

When to use bash?

Use bash you need to launch a Python script. A bash script should be little more than an alias for a program written in a language that offers unit testing.
