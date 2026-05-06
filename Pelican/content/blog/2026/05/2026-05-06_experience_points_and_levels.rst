Experience Points and Levels
################################################

:date: 2026-05-06 07:46
:tags: OpenD6,#python
:slug: 2026-05-06_experience_points_and_levels
:category: TTRPG
:status: published

See `Writing Project -- perhaps a bad idea <{filename}/blog/2026/04/2026-04-23_writing_project.rst>`_.
I'm trying to dig around in my old notes to pull together a "World Book" with a fantasy setting I think has a lot of good gaming opportunities. I have a problem, though.

History
=======

History is my problem.

Some of this world-building and campaign design started when I played with OD&D rules.
In the late 70's and early 80's. (I'm old.)

The design evolved into the Fantasy Wargaming (published in 1982) system.
The FW rules are similar to the OD&D rules, so I could update my notes reflect these rules.

My first computer (an Apple ][+) wasn't up to keeping the notes I needed.
My first truly useful computer was a Macintosh (ca. 1985), so my notes don't reflect my earliest ideas.
Which, actually, is good. My first ideas weren't great.

The design evolved into the Hero system.
The character definitions moved into a Hypercard application that computed Hero character points.

What's the problem?

The problem is notes that still mention "Level 4-5 Cleric".

Levels
=======

Hero (and OpenD6) don't really have "levels".

While I see this as a good thing, I have to figure out a mapping from Level to OpenD6 CP's.

We'll start with a definition of a Fantasy Wargaming (FW) level.
In FW, each level is 1000 pts.

Here's an extract from the book:

    Combat.

    :math:`XP = (\textrm{opponent's combat level}) \times 100`

    or

    :math:`XP = \frac{(\textrm{monster value})}{(\textrm{own combat level})}`

    General adventuring.

    :math:`XP = \frac{100 - (\textrm{likelihood of success})}{2}`


A FW level, therefore is some mixture of 10 opponents defeated or 40 problems solved (assuming 50% chance of success.)

The FW rules state 1,000 XP provides 2 points to boost attribute values.
In OpenD6, the cost to boost attributes varies.
It costs 3 CP's to boost an attribute value within the 3D to 3D+2 range.
From this perspective, using a :math:`\frac{6\textrm{CP}}{1000\textrm{XP}} = \frac{0.6\textrm{CP}}{100\textrm{XP}}` mapping converts FW levels to OpenD6 CP's.

My notes requiring a "Level 4-5 Cleric" suggest the character has 4000-5000 XP's. This maps to 18-40 CP's to purchase extra attribute and skill values above the baseline 18D of attributes plus 7D of skills.
This is 8-10 pips, which is 2D to 3D with a few CP's left over.

To gain a level with FW combat the character must defeat 10 same-level opponents to gain 1,000 XP.
For OpenD6, this would be an award of 10 CP's which buys about 3 points of attribute value boosts for low-level characters. (A player might buy 2 attribute value boosts and save 4 CP's for use during adventuring.)
From this perspective, each combat awarding :math:`\frac{10\textrm{CP}}{1000\textrm{XP}} = \frac{1\textrm{CP}}{100\textrm{XP}}` mapping seems to convert FW XP's for combat to OpenD6 CP's.

Using this interpretation means "Level 4-5 Cleric" has 40-50 CP's of extra attribute and skill values.

For general adventuring, the likelihood of success (from a fair GM) will have an average of 50. This means :math:`\frac{50\textrm{XP}}{2} = 40` obstacles.

In OpenD6 terms, overcoming 40 obstacles would be 40 CP's.
For General Adventuring, OpenD6 clearly takes a distinct approach from FW.
While FW provides 100XP to defeat an opponent, it only offers a maximum 50XP to overcome an essentially impossible general adventuring obstacle.
25XP is the expected average for obstacles.
FW awards are based on the stakes involved: general adventuring obstacles aren't as fatal as combat.
OpenD6 treats obstacles and combat with equivalent rewards. (It ignores the distinct stakes.)

Campaign Design
===============

I'm left with a spectrum of mappings from my historical "Level" notes to more useful OpenD6 Character points and dice.
This quick-and-dirty summary doesn't include the increased costs to move from 4D to 5D.
But it helps me fiddle with some of the bad guys so they're reasonably well-balanced compared with the player characters.

..  code-block:: python

    for level in range(10):
        d_lo, pips_lo = divmod(level*6, 3)
        d_hi, pips_hi = divmod(level*10, 3)
        print(level+1, level*1000, f"{level*6}-{level*10}", f"{d_lo}D+{pips_lo} - {d_hi}D+{pips_hi}")

This helps me design characters that fit the OpenD6 system.

..  csv-table::

    Level, XP, CP, D+PIPs
    1, 0, 0-0, 0D+0 - 0D+0
    2, 1000, 6-10, 2D+0 - 3D+1
    3, 2000, 12-20, 4D+0 - 6D+2
    4, 3000, 18-30, 6D+0 - 10D+0
    5, 4000, 24-40, 8D+0 - 13D+1
    6, 5000, 30-50, 10D+0 - 16D+2
    7, 6000, 36-60, 12D+0 - 20D+0

This helps me move from my sketchy historical notes to a modern game design.
