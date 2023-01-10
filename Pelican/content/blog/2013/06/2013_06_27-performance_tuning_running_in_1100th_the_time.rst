Performance "Tuning": running in 1/100th the time
=================================================

:date: 2013-06-27 10:04
:tags: performance,algorithm,test-driven reverse engineering,complexity
:slug: 2013_06_27-performance_tuning_running_in_1100th_the_time
:category: Architecture & Design
:status: published

For the `757 Python Meetup <http://www.meetup.com/757-Python-Users-Group/>`__ group,
someone proposed looking at some Python code they had which was slow.
The code implemented a variation on the `Elo chess rating
system <http://en.wikipedia.org/wiki/Elo_rating_system>`__.  It
applied the ratings to other sports, and used the points scored as
well as basic win/lose/tie to work out a ranking for sports teams.
Very clever stuff.

But.

It was described as horribly slow. Since it was only 400 lines of
code, it was a great subject for review in a Python meetup.  I would
be able to show some tweaks and performance tips.

**Hypothetical Step 1:  Profile**

My first thought was to run the profiler and see what popped up as a
possible root cause of slowness.

Generally, there are three kinds of performance problems.

-  **Wrong data structure**.
    Or wrong algorithm.  (They're simply
    opposite sides of the same coin.)  This generally leads to dramatic,
    earth-shattering improvements.

-  **Piss-Poor Programming Practices**.
    This kind of fine-tuning yields
    minuscule improvements.  In some cases, no measurable change at all.

-  **Bugs**.
    Every time I've been asked to improve "working" code, I
    find that it has bugs.  Every time.  These can exacerbate performance
    problems.  Interestingly, most of these are readily apparent during
    an initial survey:  i.e., while simply reading the code to see how it
    works.  Trying to create unit tests for the purposes of refactoring
    often reveals additional bugs.


I didn't know what I was going to see in this 400-line program.


Hypothetically, profiling will help show what kind of problems we
have.


Prior to profiling, of course, we need to run the darn thing.
Thankfully, they provided some typical input files.  For example,
1979 High School Football season results.  159 lines of patiently
gathered teams and scores.


**It Didn't Run**


When we tried to run it with the profiler, we found that we had a
bug.  Tracking down the bug, revealed the essential performance
problem, also.


The *core* problem was a failure to make use of Python data
structures.


This manifested itself in a number of really bad design errors.
Plus, it presented as the actual, show-stopping, serious bug.


In order to work out team rankings, the program kept a list of teams.


I'll repeat that for folks who are skimming.


  **In order to work out team rankings, the program kept a list of teams.**


Not a dict mapping from team name to team details.  But a simple
list.  Locating a team in the list meant iterating through the list,
looking for the matching team.  Really.

::

    for t in team_list:
       if t['name'] == target_name:
           process( t )


This kind of thing was repeated in more than one place.


And one of those repeats had the bug in it.


What we have here is "wrong data structure".  Replacing a list with a
dict will have earth-shattering impact on performance.


**The Bug**


The bug, BTW, was a lookup loop which had the additional requirement
of adding missing teams.  It tried to use the **for-else** structure.
This was the intended code (not the actual code).

::

    for t in team_list:
       if t['name'] == target_name:
    else:
       t['name']= init_new_team(target_name)


This is a first-class bit of Python.  An **else** clause on a **for**
statement is a real feature of the language.  However, it's obscure
enough that it's easy to get wrong.


However, it's also unique to Python, and the kind of thing that can
lead to confusion.  I discourage it's use.


**Test-Driven Reverse Engineering**


We're doing TDRE on a little piece of recreational programming.  This
means that we need to fabricate unit tests for code that is purported
to work.  Some folks like to call this "exploratory testing" (a
phrase which is contradictory, and consequently meaningless.)  We're
"exploring".  We're not "testing".


Once the core bug is fixed, we can run sample data through the
application to get "big picture" results.  We can extract bits from
the sample data and exercise various functions in isolation to
determine what they actually do now, bugs included.


Since this is so simple--and we're going to review it during a 2-hour
meet up--and there's nothing billable going on--we can get by with a
few really simple unit tests.  We'll run the darn thing once to
create some expected output.  We save the output and use that single
output log as the expected results from each refactoring step.


More complex applications require more unit tests.  For a billable
TDRE effort last year, I had to create 122 unit tests to successfully
refactor a program of over 6,000 lines of code.  It took several
weeks.


**Real Step 1: Fix The Data Structure**


Before profiling (but after running to capture some output) we have
to fix the essential data structure.  Repeated scanning of a list is
never going to perform well.

The whole point of the study of "Data Structures" is to prevent (or
optimize) search.


In this case, we can prevent linear search of a list by using a
dictionary.  That, clearly, is job one.


It was a pervasive rewrite.   Essentially, everything in this little
program included a goofy loop to lookup a team in the list.  The Elo
algorithm itself, which is already :math:`\textbf{O}(n^2)`, is dragged
down by using the linear search for the opposing team four more
times, making it :math:`\textbf{O}(n^3)`.

**Cyclomatic Complexity**

One of the big "issues" is the use of **if** statements throughout
the scoring algorithm.  An **if** statement creates `Cyclomatic
Complexity <http://en.wikipedia.org/wiki/Cyclomatic_complexity>`__
and can lead to performance problems.  Generally, **if** statements
should be avoided.

This algorithm applies some normalization factors to reconcile
scoring with win/loss numbers in different sports.  Basketball,
specifically, involves generally high scores.  Since there are
2-point and 3-point scoring opportunities, a factor is used to
normalize the points into "goals".  Football, similarly, has numerous
scoring opportunities with values of 1, 2, 3 and 6 points; the scores
here are also normalized.

This normalization was done with an **if** statement that was
evaluated deep inside the Elo algorithm.  Repeatedly. Evaluated.
The two functions that handled the normalizations, plus the
normalization factors, are ideal candidates for OO design.  There's a
clear hierarchy of classes here.  A superclass handles most sports,
and two polymorphic subclasses handle football and basketball
normalization.

The **if** statement is now "pushed up" to the very beginning of the
program where an instance of the sports normalization object is
created.  This object's methods are then used by the Elo algorithm to
normalize scores.

**Icing on the Cake**

Once we've fixed the bug and replaced a list with a dict, everything
else is merely icing.

Some other OO changes.

#.  The "Team" information should not be a flat, anonymous dictionary.
    It should be a proper class definition with proper attributes.
    There aren't many methods, so it's easy to create.

#.  The "Game" information is read by csv.DictReader.  However, it
    should not remain a simple, anonymous dict.  As with a Team, a
    simple class can be created to handle Game.

#.  The overall structure of the application needs to be broken into
    two sections.  The command-line interface parses options, opens
    files, and generally gets everything set up.  The actual ranking
    algorithm should be a function that is given an open file-like
    object plus the Sport object for normalization.  This allows the
    ranking algorithm to be reused in other contexts than the
    command-line (i.e. a web service).

A more subtle OO design point is the question of "mutability".  A
Team in this application is little more than a name.   There are
also numerous "stateful" values that are part of the Elo
algorithm.   A Game, similarly, is an immutable pair of teams and
scores.  However, it has some mutable values that are part of the
Elo algorithm.


Really, we have immutable Team and GameHistory objects, plus a few
values that are used as part of the Elo calculation.  I'm a big
fan of disentangling these mutable and immutable objects from each
other.


I suspect that the Elo algorithm doesn't *really* need to update
the "state" of an object.  I suspect that it actually creates (and
discards) a number of immutable candidate ranking objects.  The
iteration that leads to convergence might be a matter of object
creation rather than update.  I didn't make this change, since it
required real work and we were out of time.


**Bottom Line**


The more times I do TDRE to improve performance, the more I
realize that it's all about bugs and data structures.
This recreational application took 45-60 seconds to process one
year's record of games for a given league.  It now takes less than
0.2 seconds to do the same volume of work.  Two test cases
involving a complete run of 159 records runs in 0.411 seconds.
That's 1/100th the time simply from switching data structures.


The idea of "tweaking" a working program to improve performance is
generally misleading.  It might happen, but the impact is
minuscule at best.


Here's the checklist for getting 100:1 improvements.


-  Remove searches.

-  Remove deeply-nested **if** statements.


Generally, reduce Cyclomatic Complexity.



-----

This also falls nicely into the “anti if campaign”...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2012-08-24 19:52:30.407000-04:00

This also falls nicely into the “anti if campaign” genra
http://www.antiifcampaign.com/

`"The Anti-IF Campaign"
<{filename}/blog/2010/12/2010_12_27-the_anti_if_campaign.rst>`_





