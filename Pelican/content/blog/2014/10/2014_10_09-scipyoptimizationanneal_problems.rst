Scipy.optimization.anneal Problems
==================================

:date: 2014-10-09 08:00
:tags: scipy,Data Science
:slug: 2014_10_09-scipyoptimizationanneal_problems
:category: Technologies
:status: published

| Well, not really "problems" *per se*. More of a strange kind of
  whining than a solvable problem.
| Here's the bottom line. Two real quotes. Unedited.
| Me: "> There's a way to avoid the religious nature of the argument. "
| Them: "Please suggest away."
| Really. Confronted with choices between anneal and basin hopping, they
  could only resort to hand-waving and random utterances.
| The tl;dr summary is this:

-  "scipy.optimize.anneal only has three hard-wired schedule
   variants: ‘fast’, ‘cauchy’ or ‘boltzmann’."
-  My initial response was "And..."?
-  "Not being able to specify my own cooling schedule severely limits
   the usability of the code"

| A complaint that causes me deep pain: "severely limits" with no actual
  evidence. And no plan to get evidence beyond a religious wars style
  argument.
| 
  There may have been a technical question on the class definitions
  inside scipy. But that question was overshadowed by the essential
  problems with what they were doing. Or, more properly, what they were
  whining about.
| Did they really have a problem with a state of the art solution to
  optimization problems? More specifically:
| 
  1. Did they read the "Deprecated" part of the scipy documentation?
  This is a hint that there are better solutions available. Perhaps they
  could start there instead of whining.
| 2. Did they actually read the details of the three schedules in the
  "Notes" section? Do they seriously think they've got a new approach
  that does not fit any of the various parameters of the three installed
  algorithms? I don't mean to be too rude, but... Do they really think
  they're that scale of genius?
| 3. Do they have any evidence that their problem is so unlike
  the typical case handled by basin hopping?
| 4. Do they have any evidence that their solution totally crushes
  the already-built code?
| 
  I think the answers to all four question were "no".
| 
  I'm not even certain that I could help them with some of the Python
  technology required to extend scipy. But, I'm sure I cannot actually
  do anything of value under the circumstances that (a) they have not
  really tried the established algorithms and (b) they're already sure
  that the established algorithms can't work based on religious-wars
  arguments.
| It was clear that they never read the "Notes" section on this SciPy
  page: \ http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.anneal.html#scipy.optimize.anneal
| 
  One of the emails in the exchange had a kind of hand-waving
  justification for the problem domain being somehow unique. Lacking any
  actual evidence, I'm inclined to believe they were just hoping that
  their problem domain was unique, allowing them to dismiss the
  available Python solution and do something uniquely bad.
| 
  (Optimization is not my area of expertise. Perhaps I'm way off base;
  perhaps the existing solutions are so problem-domain specific that
  everyone has to invent new technology. Maybe established solutions
  really don't work.)
| More importantly: there was no actual evidence that the existing
  optimization (either annealing or basin hopping) failed to solve their
  problem.
| 
  But the worst part was this:
| 
  "From, a business perspective, I need to know about SA because our
  competitor stole our biggest client using it."
| 
  They don't actually want to innovate. They only want to try and catch
  up by making religious war arguments over the deprecated simulated
  annealing vs. basin hopping.





