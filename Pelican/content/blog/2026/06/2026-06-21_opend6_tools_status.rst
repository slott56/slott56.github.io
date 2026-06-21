OpenD6 Tools Project -- Status
################################################

:date: 2026-06-21 09:31
:tags: OpenD6,#python
:slug: 2026-06-21_opend6_tools_status
:category: TTRPG
:status: published

See the `OpenD6 <{tag}opend6>`_ tag for a bunch of related content.
I have a DSL for OpenD6 spells and OpenD6 characters.
At this moment, the test suite statistics are these:

+------------+--------+----------+
| Statements | Misses | Coverage |
+------------+--------+----------+
|    2701    | 166    | 94%      |
+------------+--------+----------+

Background
===========

The OpenD6 tools ahve two DSL's.
These differ in a profound way:

-   Spell definitions are based on a difficulty budget. This is complicated, because some aspects increase the difficulty, while others decrease the difficulty.

-   Character and Creature definitions are based on a dice allocation for attributes, skills, advantages, special abilities, and disadvantages. This is not as complicated: one can start with a handful of 18 dice and physically push them around the character sheet to make a charactet that fits a simplistic budget.

There are more complications, of course. A lot more.

One response to the complications is to simplify the rules. This is laudable.
Many people have offered simplified D6 systems. I'm not that clever.

Another choice is to create tools to help manage the complexities. This is what I chose to do, instead.
I don't have a really **good** reason for this.
But I can implement a DSL for very complicated TTRPG rules.

An Example
==========

From the unit test suite...

..  code-block:: python

    amulet_protection = Item(
        name="Amulet of Protection",
        notes="An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura",
        effect=SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, "non-enchanted weapons",
            modifications=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
        ),
        area_effect=AreaEffectAspect("2m radius sphere"),
        other_aspects={
            'fragile': GenericAspect(0, "Fragile")
        },
        other_conditions=[
            GenericAspect(0, "-1 under a new moon")
        ],
        type="Jewelry",
        price="H (200 G)"
    )

Clearly, it's wordy with a level of redundancy that some might find needless.

While annoying to some, the redundancy is helpful for validation.
If the ``effect`` isn't some kind of ``Effect`` class, then there's a fundamental problem with the definition.
If, as another example, the ``effect`` is omitted, the definition is incomplete.

The ``name=...`` syntax is pure Python; it makes it easy to have a mixture several categories of aspects.
Some aspects have a formal definition (like a ``SpecialAbilityEffect``) while other categories of aspects are best left as descriptive text.
While the text is important for role-playing, the more formal pieces (like the ``AreaEffect``) are required by the game rules to help the GM and players can agree on what happens when someone is wearing this amulet and is whacked over the head with a folding chair.

Objectives
==========

This is **not** a VTT like https://roll20.net or https://www.fantasygrounds.com.
It doesn't play a TTRPG.

"What," you may ask, "is the point?"

As someone who's got a unique world, and a campaign in that world, I really need to be **sure** my non-player characters, creatures, items, spells, etc., and yet more etc., have a reasonable budget when compared with the player characters.

For OpenD6 Fantasy the player characters often start with 18D of attributes, 7D of skills, and a net zero of advantages, disadvantages, and special abilities.
I can't go creating a pool of NPC's with budgets outlandishly larger than this.
I also can't expect players to have any fun when the NPC's are all based on 12D of attributes and 1D of skills.

This may also be useful a GM to help a first-time player get their character's budget correct.
It is kind of technical-looking, and I've made no effort to create a GUI usable by people who don't happen to be technically tool-savvy.
Jupyter Lab is usable by a wide spectrum of folks; in my experience, anyone who can make MS-Word work should be able to use this. (I can't make MS-Word work, my level of technical tool-use is relatively low.)

How do I use it?
================

I use these tools with `Jupyter La <https://jupyter-notebook.readthedocs.io/en/stable/index.html>`_.
I can put the details for a thing in a cell, then compute the resulting budget by clicking the little green triangle.

Doing this supports a Change-Compute-Consider cycle of thinking abouts items, characters, monsters, etc.
Make a change; compute the impact; consider the overall scenario, campaign, and world.

..  figure:: {static}/media/lab_3.png
    :alt: Jupyter Lab, showing a Spell example

    Here's a Jupyter Lab notebook, showing the "Add Chapter" spell and the difficulty computation.

What's Next?
============

Clearly, 100% code coverage is the next step.

My world book and campaign book are reasonably complete, which means I have all
the features I need in the ``opend6_tools`` project.
I can then put the tools out to GitHub.

Next, I need to publish my world book and campaign, also.
Stand by.
