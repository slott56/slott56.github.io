Rolling Your Own HashMap
========================

:date: 2005-10-04 10:22
:tags: architecture,design,complexity
:slug: 2005_10_04-rolling_your_own_hashmap
:category: Architecture & Design
:status: published





Reference:

`Minimum Object Count Map, part 2 (Analysis) <http://jroller.com/page/slobodan?entry=minimum_object_count_map_part1>`_


[snip]

`Minimum Object Count Map, part 2 (Analysis) <http://jroller.com/page/slobodan?entry=minimum_object_count_map_part1>`_




Was this really necessary? Yeah, it could be an overkill. [snip]


`Minimum Object Count Map, part 2 (Analysis) <http://jroller.com/page/slobodan?entry=minimum_object_count_map_part1>`_



I think it was overkill in the worst way.  I
don't see the head-to-head comparison with HashTree, which already minimizes
storage.  Since storage was the only problem, HashTree appears to be the
solution.  If performance was
*also* 
a problem, then perhaps this might be worth the
effort.



I'll need to see the results of
actual performance testing before I can agree that this was a worthwhile
exercise.








