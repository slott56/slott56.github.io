Python Tutor
============

:date: 2015-09-22 08:00
:tags: #python,learning
:slug: 2015_09_22-python_tutor
:category: Technologies
:status: published

| Read This:
  http://radar.oreilly.com/2015/08/learning-programming-at-scale.html
| The core visualization tool
  (`pythontutor.com <http://pythontutor.com/>`__) can be helpful for
  many people. The shared environments seem like a cool idea, also, but
  I don't have any specific comments on the other tools.
| While this looks very cool, I'm not a huge fan of this kind of
  step-by-step visualization. This uses very clear graphics, and looks
  very clever, it has some limitations. I think that some aspects of
  "visualization" can be misleading. Following an execution path for a
  specific initial condition can obscure events and conditions that
  aren't on the happy path. It's not clear how a group of statements
  establish a more general condition.
| I'm a fan of formal post-conditions. From these, we can postulate a
  statement, and work out the weakest precondition for the statement. As
  we work through this exercise, we create a formal proof and a program.
  It's very elegant. And it covers the general case, not specific
  examples.
| Most importantly, this effort depends on having formal semantics for
  each statement. To write code, we need to have a concise definition of
  the general state change is made by each statement in a language.
  We're looking at the general case for each statement rather than
  following a specific initial condition through a statement.
| Sidebar.

   In C, what does this do? a[i++] = ++i; There is no formal definition.
   The statement has three state changes stated. But how are they
   ordered? No matter what initial values for a[] and i we provide, this
   is still pretty murky. A debugger only reveals the specific
   implementation being debugged.

| Visualization may help some people understand the state change created
  by a statement. Some people do learn things by watching this kind of
  "debugger" mode. In particular, this may help because it has much
  better graphics than the built-in character-mode debugger.
| This idea works best with programs that already make sense: programs
  that are well designed. Programs that make orderly progress from some
  initial state to the desired final state.
| Programs written by learners may not be all that clean. Realistically,
  they may be inept. They may even reach the far end of the spectrum and
  be downright bad.
| While this tool is graphically gorgeous, it's still a debugger. It
  wallows around in an internal world in which the formal semantics can
  get obscured. The general case can't easily be shown.
| We have a forest and trees problem here. A debugger (or other
  statement-by-statement visualization tool) emphasizes each individual
  tree. The larger structures of glades, thickets, groves, stands,
  brakes, and coppices are lost to view.
| The humble while statement (especially one with an internal if-break)
  can be extremely difficult to understand as a single statement. If we
  break down the statement-by-statement execution, the presence of two
  termination conditions (one on the while clause and one on the if
  clause) can be obscured because a visualization must follow a specific
  initial condition.
| With really well-written tutorials -- and some necessary metadata -- a
  super-visualizer might be able to highlight the non-happy-path logic
  that exists.  This alternate path viewing could be helpful for showing
  how complex logic works (and doesn't work.)
| With programs written by learners -- programs which are inept and
  won't have appropriate metadata -- a super-visualizer would need to
  reason very carefully about the code to determine what happy path and
  non-happy-path kinds of logic are present. It would have to locate and
  highlight

-  contradictory elif clauses,
-  gaps among elif clauses,
-  missing else clauses,
-  hellishly complex else clauses,
-  break conditions,
-  continue conditions, as well as
-  exception handling.

| 
| For truly bad programs, the super-visualizer may be stumped as to what
  is intended. Indeed, it may be impossible to determine how it can be
  displayed meaningfully to show alternatives and show how the specific
  code generalizes into a final outcome.

::

   def this_program_terminates(some_code):
       # details omitted

   def demo():
       while this_program_terminates(demo):
           print("w00t w00t")

| What does this do? How can any visualizer aid the student to show
  problems?
| To take this one step further, I think this kind of thing might also
  be hazardous to learning how the functional programming feature of
  Python work.  I think that exposing the underlying mechanics of a
  generator expression might be more confusing than simply treating it
  as a "lazy list."
| It's very nice. But it isn't perfect. Something that supports
  reasoning about the general post-conditions established by a statement
  would be more useful than a step-by-step debugger with great graphics.





