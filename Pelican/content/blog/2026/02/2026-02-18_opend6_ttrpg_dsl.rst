OpenD6 TTRPG DSL -- Spell Definitions
#########################################

:date: 2026-02-18 13:28
:tags: DSL,OpenD6
:slug: 2026-02-18_opend6_ttrpg_dsl_spell_definition
:category: TTRPG
:status: published

The OpenD6 Table-Top Role-Playing Game (TTRPG) has a complicated bit of accounting around the definition for magical spells and invocations.
For me, the accounting suggested a need for software tools.
This -- in turn -- forced me to invent a Domain-Specific Language (DSL) to work with OpenD6 spells.

I like the OpenD6 rules because (a) they have a cool mechanic, and (b) the Open Gaming License (OGL) that lets me work on extensions.
While I haven't done must TTRPG in the last few years, I spent a lot of time playing TTRPG's from 1977-ish to 1995-ish.

I throw out an example, then I'll touch a little on why create a DSL.

What It Looks Like
==================

Here's an example spell definition:

..  code-block:: Python

    charm = Spell(
        name="Charm",
        skill="Temperamental Alteration",
        notes=[
            "With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately."
        ],
        effect=SkillEffect("charm skill", "+4D"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Smile and make a gesture of welcome or admiration", "simple"
            ),
            "unreal_effect": UnrealEffectAspect.based_on(("effect",),
                                                         "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="May only be used on humanoids who understand the caster’s language and can hear the caster",
            ),
        ],
    )

This was extracted from the rules through a multi-step process.

1.  Gather the text from the PDF's available at https://ogc.rpglibrary.org/index.php?title=OpenD6.

2.  Write a Minimal DSL that captured the parsed text and supported some tooling
    for difficulty computation and publication.

3.  Refine the DSL to support more complete computations of difficulty.

4.  Refine the DSL even more to make the special cases less special.

Why a DSL? Why not use a spreadsheet?
======================================

Working with TTRPG's means there are two competing needs.

-   Design of the campaign/world/scenario.
    This means making sure monsters and treasures and what-not are commensurate.
    Big monster. Big Risks. Big Skill Use. Big Rewards.
    In OpenD6 terms the difficulties should be reasonably consistent.

-   Publication of notes for GM's and players.

The design needs spreadsheets. These aren't great for publication.

The publication needs a word processor. This is not great for fiddling with the design details and recomputing spell difficulties.

I'm happiest with writing in plain text and using tools like **Sphinx** (or **Hugo**) to convert the text to HTML or PDF or whatever.

I can then use a DSL to define spells and a little toolchain to extract properly-formatted output from the spell DSL.

Using ReStructured Text, I can have a ``..  include:: some_spells.txt`` in the document.
I can then have a ``Makefile`` with recipes to make the ``some_spells.txt`` from the ``some_spells.py`` source.

I can tweak the source and republish the document without having to manually reformat the spreadsheet for publication.
Or, worse, copy and paste from spreadsheet to word-processor.

What's so complicated?
======================

There are several complications in Spell definitions.

1.  Some aspects involve measures (in Kilometer-Meter-Second units) that need to be converted to difficulty values.
    The math is a :math:`v = 5 \log_{10} m`, and the rules provide a big table.
    Who wants to look that up each time?

2.  Some aspects involve dice codes; something like "3D+2". Not difficult to work with.
    But, also, not a KMS measure. Can we keep this straight? Or will we overlook one?

3.  Some aspects depend on other aspects. There aren't too many cases, but speed almost always depends on range.
    Change one, you have to change the other to assure the spell is instantaneous.
    Who wants to manually check this each time?

4.  There's a kind of double-entry debits-and-credits structure to a spell's difficulty computation.
    Some aspects increase difficulty. Some aspects decrease difficulty.
    It's usually clear, but, it's also an annoying bit of accounting.
    When you're trying to design a fun campaign, who wants to be bogged down in details of spell design?

These all add up to a need for a DSL so tools can handle the details cleanly.

What about Items?
=================

Yes. OpenD6 items are spells cooked into a thing (ring, rod, wand, staff, amulet, etc., etc.)

The distinction is that items don't usually have a casting time.
Also, items have a few built-in limitations -- like they can be taken away from the wielder.

The DSL is similar to the spell DSL, with a few distinct constraints.

What about Creatures? or Characters?
====================================

Creatures and Characters also involve some accounting, but it's **much** simpler.
There's a dice budget, and the dice can be spread around among attributes and skils.
The DSL doesn't really involve too much computation.

However, it's not to have things done consistently.

Here's an example monster:

..  code-block:: python

    giant = Creature(
        name='Giant',
        agility=Agility(3*D, {'fighting': 4*D, 'melee combat': 4*D}),
        coordination=Coordination(1*D, {'throwing': 4*D}),
        physique=Physique(5*D, {'lifting': 6*D, 'running': 6*D+2}),
        intellect=Intellect(2*D),
        acumen=Acumen(1*D, {'tracking': 2*D}),
        charisma=Charisma(1*D, {'intimidation': 6*D}),
        move='10',
        strength_damage='3D',
        body=26,
        advantages=[Size(2, 'Large, scale value 6')],
        # disadvantages=[],
        special_abilities=[
            Hypermovement(2, '+4 to Move'),
            IncreasedAttribute(3, 'Physique, +3 to all Physique totals'),
        ],
        equipment='Large club (damage +2D)',
    )

The point of the DSL is to make it easy to tweak something like ``body`` and ``advantages`` to create a spectrum of giants of various sizes.
Additionally, we could also tweak skills and attributes to make sure the clever ones weren't as tough and the tough ones suffered from an abysmal lack of other skills.

What's helpful is having a ``budget()`` method, so ``giant.budget`` can be compared with player characters, other monsters, and the rewards available.

Next Steps
==========

One glaring issue in the code base is the way the ``DieCode`` processing works.
The **Charm** spell has this: ``SkillEffect("charm skill", "+4D")``, which uses a string version of a DieCode.
The **Giant** uses this: ``Intellect(2*D)`` where ``D`` is a constant used to construct Die Codes.
(Even within **Giant**, the ``strength_damage`` -- which is computed from *physique* -- is shown as a string.)
This DieCode business needs to be reified into a single definition that characters and spells can share.

Also, the various skills are provided as strings.
The rules enumerate all of the skills.
The DSL should also work with enumerated skill types.

Since spells can confer skills (and improve attributes) there are some additional overlaps between spells and characters.
We don't want to write tools to support **play**. We're only interested in design.
(And, to a limited extent, preservation of the source documents in a more useful form.)

Eventually, this will wind up on GitHub.

And, sometime after that, an **OpenD6** world-book may also show up somewhere.
