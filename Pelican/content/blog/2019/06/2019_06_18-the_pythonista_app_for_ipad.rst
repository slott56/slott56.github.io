The Pythonista app for iPad
===========================

:date: 2019-06-18 08:00
:tags: education,#python
:slug: 2019_06_18-the_pythonista_app_for_ipad
:category: Technologies
:status: published

Let me start my review with "wow!"

Python 3.6 on the iPad. Works. Nicely. Easy to use. Reliable.
Rock-Solid.

I'm not switching to iPad as my primary platform any time in the near
future.  But. For certain kinds of small and tightly focused hackery,
this is really nice.

I use a bracket to hold the iPad up and an external keyboard. I can be
used with the on-screen keyboard, but, that's slow-going for me.

Here's the thing that was exquisitely simple in Pythonista:



.. image:: "{static}/media/File May 31, 1 41 24 PM.png"
   :width: 320px
   :height: 240px
   :target: "{static}/media/File May 31, 1 41 24 PM.png"
   :alt: UML diagram



I'm able to draw a hex grid ("Flat Top", "Double Height") in a few
dozen lines of code. This includes a bunch of geometry rules like
adjacency and directional movement.

The Pythonista package includes a super-easy-to-use ``canvas`` module
that's a tiny bit simpler than turtle graphics. It takes a bit of
getting used to, but it has enough graphics primitives to make it
easy to create hexagons and tile the surface.

Given a HexGrid instance, I can then create "cities" and their
surrounding territories in an "empire". I've tried a few organic
growth algorithms, and I like the look of these maps. They provide a
lot of avenues for conflict for writing fiction or playing
role-playing games.

Some of the algorithmic
foundations: https://www.redblobgames.com/grids/hexagons/.

Fun Hackery
-----------

This is fun hackery because I can change the code, click the run
icon, and watch the consequence of the changes. A traceback is
highlighted in the original file. Easy. Fun.

It's pretty slow. No surprise there. It's running on an iPad.

It's pretty easy to work on. Whip out the iPad and start coding.
The super-easy, built-in ``canvas`` module means feedback is instant
and gratifying.

I can see having an intro to programming class where the fee includes
an extra $800 for the iPad you take home along with your new-found
skills in basic coding. (This is still a \*lot\* of money, but it's
less than a full laptop.)

Filling in the Holes
---------------------

Looking at the output, you can see the growth algorithm left some
unfilled holes. A later version examines all unfilled spaces to see
if they're entirely surrounded by one color and fills them. This is a
fun algorithm because it works in a simple way with the adjacency
iterator and the set of locations covered by a city. Locations 12L
and 17K are these "Simply Surrounded Single Holes."

However, there are still some "Edge" cases that are challenging.

Location 12D reflects a hole on a border. These are interesting, and
could be the seed for epic wargaming, role-playing game,
novel-writing drama. A simple algorithm can find these and assign a
random owner... But... They really need a special "On Fire" color
scheme to show the potential for drama.

There's a subtlety in the upper-left corner (5W and 6V) between Blue
and Green. While these seem like simple border holes, each hole as
only five of six required neighbors.

Compare these with 16P in the upper-right corner. This also has five
of six neighbors. However, this space looks like it could be a bay
leading up to a river and the river is a natural border between
nations.

The head of the bay at 16P has 5 neighbors of two colors, similar to
5W and 6V. The difference can be detected by a recursive walk to see
if a hole is connected to other holes and the composite is actually
surrounded. There are lots of \*edge\* cases, but the (5W, 6V) pair
seems to embody the next stage of surround detection.

This more nuanced algorithm design doesn't work out well in the
Pythonista environment. This algorithm design requires careful unit
tests, not the code-and-run cycle of hackery. For this kind of
careful design, we'd need to leverage ``doctest`` (or ``unittest``)
for testing. While I'd like **pytest**, that's a lot to ask for. For
these kinds of apps, doctest is more than adequate, and a simple
``import doctest; doctest.testmod()`` in a scrip can help be sure
things work as expected.

tl;dr
-----

If you're an iPad user, consider adding Pythonista. You can really
write real Python. It's a useful environment. It's fun for teaching.




