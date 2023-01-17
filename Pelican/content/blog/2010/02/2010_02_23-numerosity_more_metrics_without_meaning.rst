Numerosity -- More Metrics without Meaning
==========================================

:date: 2010-02-23 08:00
:tags: software process improvement,numerosity,project management
:slug: 2010_02_23-numerosity_more_metrics_without_meaning
:category: Technologies
:status: published

Common Complaint: "*This was the nth time that someone was up in arms
that [X] was broken ... PL/SQL that ... has one function that is over
1,500 lines of [code].*"

Not a good solution: "*Find someway to measure "yucky code".*"

Continuing down a path of relatively low value, the question
included this reference: "`Using Metrics to Find Out if Your Code
Base Will Stand the Test of
Time <http://www.informit.com/articles/article.aspx?p=1561879>`__,"
Aaron Erickson, Feb 18, 2010. The article is quite nice, but the
question abuses it terribly.

For example: "*It mentions cyclomatic complexity, efferent and
afferent coupling. The article mentions some tools.*" Mentions? I
believe the article defines cyclomatic complexity and gives
examples of it's use.

Red Alert. There's no easy way to "measure" code smell. Stop
trying.

How is this a path of low value? How can I say that proven metrics
like cyclomatic complexity are of low value? How dare I?

Excessive Measurment
--------------------

Here's why the question devolves into numerosity.

The initial problem is that a piece of code is actually breaking.
Code that breaks repeatedly is costly: disrupted production, time
to repair, etc.

What further metric do you need? It breaks. It costs. That's all
you need to know. You can judge the cost in dollars. Everything
else is numerosity.

A good quote from the article: "By providing visibility into the
maintainability of your code base—and being proactive about
reducing these risks—companies can significantly reduce spend on
maintenance". The article is trying to help identify *possible*
future maintenance.

The code in question is *already known to be bad*. What more
information is needed?

What level of Cyclomatic Complexity is too high? Clearly, that
piece of code was already too much. Do you need a Cyclomatic
Complexity number to know it's broken? No, you have simple, direct
labor cost that tells you it's broken. Everyone already agrees
it's broken. What more is required?

**First things first: It's already broken**. Stop trying to
measure. When the brakes have already failed, you don't need to
measure hydraulic pressure in the brake lines. They've failed. Fix
them.

The Magical Number
------------------

The best part is this. Here's a question that provides much
insight in to the practical use of Cyclomatic Complexity.
http://stackoverflow.com/questions/20702/whats-your-a-good-limit-for-cyclomatic-complexity.

Some say 5, some say 10.

What does that mean? Clearly code with a cyclomatic complexity of
10 is twice as bad as a cyclomatic complexity of 5. Right? Or is
the cost function relatively flat, and 10 is only 5% worse than 5?
Or is the cost function exponential and 10 is 10 times worse than
5? Who knows? How do we interpret these numbers? What does each
point of Cyclomatic complexity map to? (Other than if-statements.)

Somehow both 5 and 10 are "acceptable" thresholds.

When folks ask how to use this to measure code smell, it means
they're trying to replace thinking with counting. Always a bad
policy.

**Second Principle: If you want to find code smells, you have to read the code.** When the brakes are mushy and ineffective, you
don't need to start measuring hydraulic pressure in every car in
the parking lot. You need to fix the brakes on the car that's
already obviously in need of maintenance.

Management Initiative
---------------------

Imagine this scenario. Someone decides that the CC threshold is
10. That means they now have to run some metrics tool and gather
the CC for every piece of code. Now what?

Seriously. What will happen?

Some code will have a CC score of 11. Clearly unacceptable. Some
will have a CC score of 300. Also unacceptable. You can't just
randomly start reworking everything with :math:`CC > 10`.

What will happen?

You prioritize. The modules with CC scores of 300 will be reworked
first.

Guess what? You *already knew* they stank. You don't need a CC
score to find the truly egregious modules. You already know. Ask
anyone which modules are the worst. Everyone who reads the code on
a regular basis knows exactly where actual problems are.

Indeed, ask a manager. They know which modules are trouble. "Don't
touch module [Y], it's a nightmare to get working again."

**Third Principle: You already know everything you need to know**.
The hard part is taking action. Rework of existing code is
something that managers are punished for. Rework is a failure
mode. Ask any manager about fixing something that's rotten to the
core but not actually failing in production. What do they say?
Everyone -- absolutely everyone -- will say "if it ain't broke,
don't fix it."

Failure to find and fix code smells is entirely a management
problem. Metrics don't help.

Dream World
-----------

The numerosity dream is that there's some function that maps
cyclomatic complexity to maintenance cost. In dollars. Does that
mean this formula magically includes organization overheads, time
lost in meetings, and process dumbness?

Okay. The sensible numerosity dream is that there's some function
between cyclomatic complexity and effort to maintain in applied
labor hours. That means the formula magically includes personal
learning time, skill level of the developer, etc.

Okay. A more sensible numerosity dream is that there's some
function between cyclomatic complexity and effort to maintain in
standardized labor hours. Book hours. These have to be adjusted
for the person and the organization. That means the formula
magically includes factors for technology choices like language
and IDE.

Why is it so hard to find any sensible prediction from specific
cyclomatic complexity?

Look at previous attempts to measure software development. For
example, `COCOMO <http://en.wikipedia.org/wiki/COCOMO>`__. Basic
COCOMO has a nice :math:`R \times T=D` kind of formula. Actually it's
:math:`a \times K^b = E`, but the idea is that you have a simple function
with one independent variable (likes of code, *K*), and one
dependent variable (effort, *E*) and some constants (*a*, *b*). A
nice Newtonian and Einsteinian model.

Move on to intermediate COCOMO and `COCOMO II <http://sunset.usc.edu/csse/research/COCOMOII/cocomo_main.html>`__.
At least 15 additional independent variables have shown up. And in
COCOMO II, the number of independent variables is yet larger with
yet more complex relationships.

**Fourth Principle: Software development is a human endeavor**.
We're talking about human behavior. Measuring hydraulic pressure
in the brake lines will *never* find the the idiot mechanic who
forgot to fill the reservoir.

Boehm called his book *Software Engineering Economics*. Note the
parallel. Software engineering -- like economics -- is a dismal
science. It has lots of things you *can* measure. Sadly, the human
behavior factors create an unlimited number of independent
variables.

Relative Values
---------------

Here's a sensible approach: "`Code Review and Complexity <http://blogs.msdn.com/mswanson/articles/154460.aspx>`__".
They used a relative jump in Cyclomatic Complexity to trigger an
in-depth review.

Note that this happens at *development* time.

Once it's in *production*, no matter how smelly, it's unfixable.
After all, if it got to production, "it ain't broke".

Bottom Lines
------------

#.  You already know it's broken. The brakes failed. Stop measuring
    what you already know.

#.  You can only find smell by reading the code. Don't measure
    hydraulic pressure in every car: find cars with mushy brakes.
    Any measurement will be debated down to a subjective judgement.
    A CC threshold of 10 will have exceptions. Don't waste time
    creating a rule and then creating a lot of exceptions. Stop
    trying to use metrics as a way to avoid thinking about the
    code.

#.  You already know what else smells. The hard part is taking
    action. You don't need more metrics to tell you where the costs
    and risks already are. It's in production -- you have all the
    history you need. A review of trouble tickets is enough.

#.  It's a human enterprise. There are too many independent
    variables, stop trying to measure things you can't actually
    control. You need to find the idiot who didn't fill the brake
    fluid reservoir.





