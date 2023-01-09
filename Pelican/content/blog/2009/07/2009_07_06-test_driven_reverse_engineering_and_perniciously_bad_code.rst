Test-Driven Reverse Engineering and Perniciously Bad Code
=========================================================

:date: 2009-07-06 15:05
:tags: tdd,reverse engineering
:slug: 2009_07_06-test_driven_reverse_engineering_and_perniciously_bad_code
:category: Technologies
:status: published

I've done a fair amount of reverse engineering over the years.

In the early days, you went from code to specification to new code.
It took forever and the problems you uncovered -- well -- they often
derailed the project.

Recently, I used a TDD-like approach. Each piece of legacy code was
turned into some Java code with some associated unit tests. Further,
the users were able to cough up a canonical set of acceptance tests.
These were turned into unit tests, and it wasn't too difficult to
meet in the middle with plenty of testing for each piece of legacy
conversion.

Given some subsequent experience, it turns out that user acceptance
tests are essential to success in reverse engineering. Without user
acceptance tests being provided up front, reverse engineering is a
nightmare.

**Mystery Code**

Today's issue is legacy code that is -- frankly -- incompetently
done. As a bonus, the user organization is a little vague on what
it's supposed to do. They trust it, but they can't verify it. There
are no official test cases.

The only explanation we can get is a demo. And because of the user's
workload, we're only getting one of these. Limited to an hour. AFAIK,
the only way we can test the conversion is to run it head-to-head
with the legacy and take notes as the users complain about the
differences.

There will be no easy way to get to create up-front acceptance tests
to drive development. We'll have to take careful notes during the
demo and transform the demo script into test results we can use.

**Worse Still**

What's worse is the incompetent coding. How bad can code be? Let me
count the ways:

#.  Globals. Anyone who thinks a global is a legal programming
    construct needs to find a new career. A module that declares all
    the globals just compounds the horror. Everything is scopeless and
    could be used anywhere. There's no "interface" to anything, it's
    just a puddle of grey goo.

    -   Using globals means functions have side-effects. They update
        global variables more-or-less spontaneously.

    -   Using globals also means that all kinds of things may have
        hysteresis. You call it once, it does one thing. You call it
        again, it does something different.

#.  Random SQL. Anyone who thinks that SQL statements can be dropped
    in any random place in the application needs to find a new career.
    MVC is *essential* for segregating the SQL away from the View.
    Views functions can't query stuff that should have been part of
    the model, it means the model is incomplete -- and possibly in the
    wrong state. It also means that view functions are slow and
    possibly not strictly idempotent -- every time you refresh, a
    value in the view could diverge from the value in the "official"
    model.

#.  Copy-and-Paste coding. How hard can it be to put common code into
    a function? Apparently, it's nearly impossible. If you're copying
    and pasting common code, stop now. There's no excuse. It just
    raises the cost of maintenance and conversion through the roof.

#.  No Change Control. Or rather, the change control is to leave all
    previous versions of the code in place as comment blocks. For each
    line of real code, there are two lines of previous versions
    commented out. I don't care what it **was**; I want to know what
    it **is**. If you can't use SVN, or even VSS, you need to find
    another career.

There. I feel better. Back to trying to figure out what this
application really does.





