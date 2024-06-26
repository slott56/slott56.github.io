Essay 17 - Solution or Workaround?
==================================

:date: 2005-09-22 17:29
:tags: architecture,software design
:slug: 2005_09_22-essay_17_solution_or_workaround
:category: Architecture & Design
:status: published





The challenge in starting a project correctly is
to get a problem statement written down in spite of the lack of clue.  There is
a pervasive unwillingness to tackle problem description because it is so hard. 
It's hard because there is a potentially lengthy search to separate proximate
from root causes.



I think that another
cause of the unwillingness to commit to written descriptions is the conflation
of "solutions" and "work-arounds".  Without recognition of the actual problem
(and actual root causes), it's hard to tell what is being fixed and what is
being adapted.  Often we avoid root cause fixes because they are pervasive;
fixing the real problem would break a number of work-arounds.  This is termed
scope control and is somehow
meritorious.



Compounding the difficulty
of clearly defining a problem is that problems (and their solutions) are often
negotiable.  The solutions to some problems have high value and we're willing to
pay to have them fixed.  Other problems are mere trifles, and we don't invest
any effort in fixing them.  The costs and benefits are subtle and shifty; the
number of alternative solutions make it sometimes difficult to pin down a
crisply defined problem.  Problem identification can be embarassing, and there
is a lot of blame deflection that prevents root cause
analysis.



My theory on how to proceed
is this.  Warning: what follows is an iterative approach to analysis; it
involves rework and incremental delivery.  This is, in many circles, anethma:
analysis can't be that hard, rework can't be necessary, etc.  However, bad
analysis leads to bad everything that follows.  If incremental delivery is good
for the construction phases, it ought to be good for the discovery phases,
also.



**State The Problem** .  No one gets to propose any solution
until the problem statement is reasonably complete, been agreed to by the
stake-holders, and has been edited to be "solution neutral."  This is painful. 
The powerpoint presentation used to justify spending $15M often merely implies a
problem statement, and describes a solution, but fails to nail down the problem.




My preference is to take hostages
until this is done.  Refuse to do my "architect" job until I have a problem
statement.  I try really hard to do that, but at some point I realize that the
battle-front has moved, and I'm left assaulting an empty
bunker.



**Clarify The Problem** .  No one gets to propose any solution
until the problem statement has been rewritten with a reasonably well-defined
list of real business entities, and a reasonably well-defined list of
consistently used verbs.  The lexicon of discourse defines the problem domain
and is the seed for a data
dictionary.



I find it hard to do this. 
I try and try and try, and people say "in the real world we just don't have time
for all that formality and rigor."  To which I respond, "what problem are you
solving?"  To which they rarely have a reply.  They run on anyway, with me left
whining in the background.  I often put it on my weekly status reports until
they ask me to stop saying that, it makes the project look bad.  They wave their
hands at the 25 use cases, and say "if that doesn't define the problem, what
does?"  To which I resopnd "a problem
statement."



**Propose A Solution** .  Now that you have a problem, you
get to propose a solution and write up use cases to describe that proposal. 
Plan to throw the first batch or two away.  Hopefully, you'll get a chance to
trash them before people start writing software that doesn't really solve the
problem.  However, you will often have to wait for a later release to attempt to
address the real problem.  



This is
something new that I've begun to realize: the lack of clue is so profound, and
so hard to recognize that the only real way to understand the problem is to
write it up once, realize how little you know, throw it all away, and write it
up again.



**Understand the Problem** .  You will rewrite the initial problem
statement, write a third (or fourth) draft of the use cases.  At this point, you
will have figured out what the root causes of the problem are, and recognize
when you are "solving" something and when you are "working around" something. 
These are conflated all the time with horrible consequences in cost and
complexity.



**Weigh The Effectiveness Of Solution Alternatives** .  Once
you actually understand the problem, you can make rational judgments about the
solutions, their actual value and their costs.  Only now can you seriously
consider building something.  Since you finally know what you are solving and
what you are working around, you can make intelligent progress with intelligent
trade-offs.  



Until you understood the
problem, you were really in discovery mode.  Once you understood the problem,
you could transition to engineering
mode.



For some additional details on
this, see Essay 9, "`Getting Started <{filename}/blog/2005/09/2005_09_12-essay_9_getting_started.rst>`_ ".








