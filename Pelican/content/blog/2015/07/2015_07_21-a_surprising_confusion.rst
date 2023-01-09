A Surprising Confusion
======================

:date: 2015-07-21 08:00
:tags: #python,map-reduce,functional python programming,python essentials,hadoop
:slug: 2015_07_21-a_surprising_confusion
:category: Technologies
:status: published

| Well, it was surprising to me.
| And it should not have been a surprise.
| This is something I need to recognize as a standard confusion. And
  rewrite some training material to better address this.
| The question comes up when SQL hackers move beyond simple queries and
  canned desktop tools into "Big Data" analytics. The pure SQL lifestyle
  (using spreadsheets, or Business Objects, or SAS) leads to an
  understanding of data that's biased toward working with collections in
  an autonomous way.
| Outside the SELECT clause, everything's a group or a set or some kind
  of collection. Even in spreadsheet world, a lot of Big Data folks slap
  summary expressions on the top of a column to show a sum or a count
  without too much worry or concern.
| But when they start wrestling with Python **for** loops, and the
  atomic elements which comprise a set (or list or dict), then there's a
  bit of confusion that creeps in.
| An important skill is building a list (or set or dict) from atomic
  elements. We'll often have code that looks like this:

::

   some_list = []
   for source_object in some_source_of_objects:
       if some_filter(source_object):
           useful_object = transform(source_object)
           some_list.append(useful_object)

| 
| This is, of course, simply a list comprehension. In some case, we
  might have a process that breaks one of the rules of using a generator
  and doesn't work out perfectly cleanly as a comprehension. This is
  somewhat more advanced topic.
| The transformation step is what seems to causes confusion. Or -- more
  properly -- it's the disconnect between the transformation
  calculations on atomic items and the group-level processing to
  accumulate a collection from individual items.
| The use of some_list.append() and some_list[index] and some_list is
  something that folks can't -- trivially -- articulate. The course
  material isn't clarifying this for them. And (worse) leaping into list
  comprehensions doesn't seem to help.
| These are particularly difficult to explain if the long version isn't
  clear.

::

   some_list = [transform(source_object) for source_object in some_source_of_objects if some_filter(source_object)]

| 
| and

::

   some_list = list( map(transform, filter(some_filter, some_source_of_objects)) )

| 
| I'm going to have to build some revised course material that zeroes in
  on the atomic vs. collection concepts. What we do with an item
  (singular) and what we do with a list of items (plural).
| I've been working with highly experienced programmers too long. I've
  lost sight of the n00b questions.
| The goal is to get to the small data map-reduce. We have some folks
  who can make big data work, but the big data Hadoop architecture isn't
  ideal for all problems. We have to help people distinguish between big
  data and small data, and switch gears when appropriate. Since Python
  does both very nicely, we think we can build enough education to
  school up business experts to also make a more informed technology
  choice.





