Essay 18 - What Is Your Problem?
================================

:date: 2005-09-23 17:58
:tags: architecture,design
:slug: 2005_09_23-essay_18_what_is_your_problem
:category: Architecture & Design
:status: published





We know something is wrong or can be improved,
but we lack the will to drill into details and write a problem statement.  It
isn't a lack of ability, it is purely a lack of
will.



A common source of serious issues
with software comes from proposing a solution without a full definition of the
problem.  Lacking a crisp definition of the problem, we don't really know when
the problem has been solved.  The most common symptom of this is scope
creep.



Since we can propose solutions,
we can identify problems.  It's not an ability or skill issue.  Generally, it's
a willingness issue.  Often, root cause identification involves some
considerable embarassment to people who put it software that didn't work and
required work-arounds, or software that had to work-around the work-arounds,
compounding an already bad
problem.



There are several
problem-identification techniques.  You might want to look at Gause and Weinberg
*Are Your Lights On?: How to Figure Out What the Problem Really Is*  [`Amazon <http://www.amazon.com/exec/obidos/tg/detail/-/0932633161/102-2076231-0120167?v=glance>`_ ]
for a very thorough treatment.



Here is
an exercise that may help formalize the problem prior to attempting to specify
an incomplete, over-engineered or mis-applied
solution.



1.  What works?

#.  What are the consequences of what is working?

#.  What doesn't work?

#.  What are the consequences of what isn't working?

#.  What does it take to align the not-working with the working?

#. What are the consequences of these changes?

#. What are possible mechanisms for the change?



I'm sure there are many similar
"structured brain-storming" exercises that can be used to ferret out the problem
without discussing candidate solutions too early in the process.  This one seems
to present the core questions in a usable
order.



An alternative is to attempt to
solve the problem.  We learn about the problem by observing failed solutions. 
This has a very rational appeal, but I believe that it can't be managed
successfully.  I think there are several reasons why "discovery prototyping" is
doomed from the outset.

1.  Almost no one who pays the bills is capable of
    attempting a solution.  They work by funding a project.  If you ask them to fund
    discovery prototyping, they will generally consider the deliverable to be code,
    not knowledge.  This expectation implicitly changes the project from discovery
    prototyping to solution prototyping.  Because they'll try to keep the code, the
    failed solutions will look like mistakes, and there will be tremendous pressure
    to create a deliverable solution instead of knowledge.

#.  It is an expensive use of time.  The number of
    false starts to create non-solutions in an effort to uncover the real problem is
    a tremendous amount of time; time that could be invested in more profitable
    question and answer sessions with a facilitator.  A person with a modicum of
    common sense and a good distance from the problem should be able to guide
    others.

#.  It looks too much like creating a solution. 
    Since we have a track record of cruddy, ad-hoc solutions, a cruddy, ad-hoc
    prototype often looks like production software.  Sad, but often true.  It is too
    hard to distinguish exploration from production in most
    environments.



I think that a
"technical" approach to discovery is fraught with peril.  I would suggest almost
any "non-technical" approach is better.  Particularly if you keep it well
separated from premature description of a solution.











