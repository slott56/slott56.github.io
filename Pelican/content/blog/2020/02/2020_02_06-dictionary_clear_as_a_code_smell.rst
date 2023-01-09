Dictionary clear() as a code smell
==================================

:date: 2020-02-06 16:50
:tags: #python,design
:slug: 2020_02_06-dictionary_clear_as_a_code_smell
:category: Technologies
:status: published

| Using the clear() method of a dict isn't \*wrong*. But. The reasons
  have to be investigated. I got a question about this code not working
  "properly." ("Properly"? Seems too vague to be useful.)
| Here's a summary of the example.

::

   final_list = []
   temp_dict = {}
   for obj in some_source:
       cool_function(obj, temp_dict)
       final_list.append(temp_dict)
       temp_dict.clear()  # Ready for reuse, right?

| 
| This can't work.
| (Bonus points if you suspect that list.append() is a smell, too. There
  may be a list comprehension solution that's tidier than this.)
| It's not always easy to get to a succinct statement of what doesn't
  work "properly," or what's confusing about the Python list structure.
  Getting useful information can be hard. Why?

-  Some programmers are "Assumptions First" kind of people, and their
   complaint is often "doesn't match my assumption" not "doesn't
   actually work."
-  Some people live in "All Details Matter" world. Rather than create
   the smallest example of code that's confusing, they send the
   \*entire\* project. The problem is buried in a log, wrapped with "Why
   is the list of dictionaries not being properly updated?" In an email
   that provides background details. For a Trello story that links to
   background details. Details. None of which point to the problem.

| 
| "Properly?" What does that even mean?
|  Confronted with hundreds of lines of impenetrable code, I asked for a
  definition of "properly" and got these exact seven words: "Properly is
  defined as correctly or satisfactorily."
| 
  So...
| 
  They have no idea what's wrong, can't summarize the code that's
  broken, and it's my fault because I'm the Python guru.

Why Won't My Code Work?
-----------------------

| The short answer is "Because You're Making an Assumption."
| 
  Of course, anyone who puts their assumptions first is as blind to
  their assumptions as we are to the air that surrounds us. Assumptions
  are just there. All around them. They breathe their assumptions in and
  out without seeing them.
| 
  The long answer is Python uses references.
| 
  If you apply the id() function to the items in the resulting
  final_list, you'll see that it's reference after reference of one
  object, temp_dict.  Not copies of individually populated dictionaries,
  but multiple references to the same dictionary. The same dictionary
  which was cleared and reloaded over and over again.
| 
  The very first log, crammed with useless details, had output from
  print() functions. It showed multiple copies of the same dict.
| 
  Because they assumed Python is making copies, there was no explanation
  for why the list of dictionaries was broken. Clearly, it couldn't be
  in their code. They assume their code is correct. The only choice has
  to be an undocumented mystery in Python. And I'm the Python guru, so
  it's my problem.
| 
  The presence of duplicates in the output meant "something" to them.
  They could point it out as somehow wrong. But the idea that their
  assumptions might be wrong? That was a nope.
| 
  They wanted it to be the list object, final_list, which didn't append
  dictionaries the way they assumed it would. They needed it to be a
  Python internals problem. They needed it to be a bad documentation
  problem. (Seriously. These convos have spun out of control in the
  past.)

tl;dr
-----

| Using the clear() method of a dict may indicate the developer is
  hoping Python shares copies, not references. Either add an explicit
  copy() (or deepcopy.copy()) or fix things to create new, fresh
  dictionaries each time. Objects are cheap. Why reuse them?
| 
  (Indeed, an interesting side-bar question I did not ask is "In what
  god-forsaken programming language does this 'clear-and-reuse' a data
  structure even make sense? FORTRAN?)
| 
  The list comprehension solution to this problem will have to wait.
  Stay tuned. I want to disentangle the algorithmic design problem from
  the "why aren't my assumptions correct?" problem..





