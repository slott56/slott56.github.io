Software Rewrites to Add Hints
###############################

:date: 2023-05-04 08:00
:tags: architecture,object-oriented design,patterns,python,games
:slug: 2023_05_04-software_rewrites_to_add_hints
:category: Technologies
:status: published

Let's reach way, way back. 1989 - 1990.
This will let me talk about OO programming and Python Type Hints. (really)
And doing OO design for things that are as pervasive (and transparent) as air.
Things that **need** to be part of a design, but don't appear in
any documentation.

In the early 90's the Hero Game System, 4ed had just come out.
PC's were an expensive luxury item. But the Macintosh was there to help us think different.

My TTRPG group is loving the Hero Game System. Complicated stories. Super heroes. Sophisticated game mechanics.
The Fantasy Hero rules were a delight, and lead to many long, involved campaigns.

There's no overt OO programming to it (yet.) And, of course, Python has barely been invented.

But there's a down-side to the Hero Game System:

Accounting
----------

The game requires a fairly scrupulous accounting of "Character Points".
Some are assigned at the outset. A hero, for example, may have a base budget of 75 points.
Some are purchased by taking on disadvantages. For example Paranoia, or Hunted and Watched by Authorities,
or a Dependence, or a Weakness you'd like to keep secret, can all add to the budget of character points.

All of the powers, skills, talents, perks, and what-not are purchased
with character points.

And it all has to balance.

Too high a skill in Guns means ripping away some strength or intelligence.
Or reducing other skills.

So what can we do to make sure our character's, gadgets, vehicles, and bases
are all designed properly?

Clearly, the answer is tools. Eventually, there will be OO design in here, I promise.
We'll work through the history, though.

Paper and Pencil
================

In the 90's, I played the game using actual paper spreadsheets. 3-column accounting pads to tally up base
points, advantages, and limitations to compute the net points after adjustments.

After all, we're talking about table-top role-playing.
Paper and pencil gaming. Of course we have 3-column ledger pads.
Along with hex mapping paper. And Dice. Lots of dice.

It's the 90's. I've got Macintosh LC (?) I think.
I remember the Mac+. I remember the iMac. In between the two was a slim pizza box with a front-loading CD.

Software tools are ramping up quickly to the point where they can be used casually
for gaming.

Software
========

It didn't take too long to start using spreadsheet software. Appleworks. Then Clarisworks.

It's clunky, but the computations aren't complicated. It's just a lot of typing.

First, you have to be super-careful to type all the stuff from the rule books into the spreadsheet properly.

Second -- it's the early 90's -- laptops are still very expensive. This means I'm going to
design offline, print, and use paper on game night to play.

Remember, it's a spreadsheet: it introduces as many problems as it solves.

Software V2: Hypercard
======================

HyperCard -- if you've never seen it -- isn't easy to understand.

With some work, I created cards for each power/skill/perk/talent/whatever.

I can use those cards to create new cards for a character with abilities, and references to powers, skills, talents, perks, whatever.

I can then sum up the points to be sure the Character Points balance. I can tweak the card and try
again until I make the budget add up properly.

And.

With a little care, I can serialize the output as a CSV file that can be pumped into a spreadsheet and formatted.

This was heavenly.

I built elaborate campaigns, worlds, scenarios, adventures. All the things designed with HyperCard.
The pubishing involved spreadsheet formatting and some word-processing to tie it together.

But. All good things come to an end. 2004 was the end of Hypercard.

Software V3: Python and OOP
===========================

(See, I told you we'd get to OOP, eventually.)

When you consider the problem domain
it's a classic Object-Oriented Programming problem.
(I'd been thinking about it for well over decade at this point in the historial narrative.)

Classic. OOP.

There's tons of Inheritance. Tons of Delegation. Lots of Composition.  Lots of Instances of Classes.

It's all there. And it's pretty simple. There are relatively few exceptions.
And the exceptions are trivially handled by footnotes to the "Game Master" (me).

This means I have to drag all of the work I already did out of Hypercard and rewrite it into Python.

But.

Once that's done, I can now use a block of code like the following::

    normal1 = hero.Character(
        "Normal",
        hero.NORMAL,
        # Characteristics
        hero.STR(13),
        hero.DEX(12),
        hero.CON(10),
        hero.BODY(12),
        hero.INT(10),
        hero.EGO(8),
        hero.PRE(13),
        hero.COM(9),
        # Skills, Talents, Perks, Powers
        hero.skills.WeaponFamiliarity_Category("Common Melee", 1),
        hero.skills.TransportFamiliarity_Single("Horses"),
        hero.skills.Familiarity("Jungle", 1),
        hero.skills.Familiarity("Town", 1),
        hero.skills.AnimalHandling(1),
        # Disadvantages
        hero.disadvantages.Coward(),
    )

If the points don't balance, the class initializer will print a message.

There's a serializer to produce CSV files for incorporation into spreadsheets.
This means the characters can format nicely for game night.

We're back in business. I introduced my kids to TTRPG. Some of my nephews.
But I could balance the books on my laptop to make sure their characters were legit.

Software V4: Python 3 and Type Hints
====================================

So now it's 2023.

I don't play Hero games much anymore.
In spite of not playing regularly,
the TTRPG topic surfaces from time to time. Maybe once every few years, now.

And the OO Design topic is -- in the back of my mind -- evergreen.

As a kind of mental palate cleansing *Amuse Bouche* I decided to clean up the type hints
and unit tests and make sure my hobby stuff still ran in Python 3.11 or 3.12.
I did this in the unlikely event I ever wind up playing this TTRPG again.

The cleanup inovolved a fair amount of work spread over almost a week.

Why?

Getting the type hints right revealed problems.
There are two parts to why this took so much work.

Type Hint Fundamentals
----------------------

One issue is in the way the various columns of a standard
"Full Character Sheet" are formatted.
The publication guidelines are for paper-and-pencil, hard-copy kind of adventure guides and campaing books.

- The "Cost" column isn't -- universally -- numeric. Sometimes there's text.

- Same for the "Endurance" column. It may have text explanations comingled with numbers.

This is not a big deal when serializing the data for a spreadsheet.
Mixtures of numbers and words and what-not are tolerated politely.

Using **mypy** to check the type hints revealed a number of bad mistakes.

Eventually, I could distinguish between the internal cost computations,
and the external presentation. This cleanly isolated the essentially numeric
accounting. (Which, if you roll back to the top of this post, was why we started this
in the first place: accounting.)

Thst's not all, though.

Use Case Issues
----------------

The more fundamental issue was the conflation of ``Character | Gadget | Base | Vehicle``.
This requires some care in writing type hints and doing OO design to make
sure that any differences are essential differences in these classes of objects.

For the most part, everything's a "Framework" that has a collection of features,
advantages, and limitations. A Power is a Feature, so Frameworks can nest.

From a usability perspective there are two distinct kinds of things:

-   Raw Materials. Powers, Skills, Talents, etc., with a cost.
    Ideally, these are all class definitions. They change very slowly, if at all.
    An instance of one these classes has a CP cost and a list of effects.

    The Raw Materials are all ``class SomePower(Power): effects: list[Effect] = [STRBonus(+10)]`` kind of definitions.
    More-or-less right out of the rules, rewritten into Python.

-   Finished Goods. Things like Characters have a budget, which must balance the sum of the costs of the Raw Materials that make up the Character.
    The characters in a game will be instances of some generic class, popuulated by instances raw material classes.
    The ``Character`` class definition has a few features that are distinct from the raw materials classes.

    The Finished goods are built with ``character = hero.Character(THIS(10), THAT(10), ...)``.

This distinction makes for some gnarly OO design decisions to reflect the variety of use cases.

A raw material has a fairly fixed definition, and there's a direct mapping
from the desired effects to the required cost. (The mapping isn't always **simple**
because there are advantages and disadvantages that are figured in.)

A finished good is built "on the fly" as a collection of instances of raw materials.

Right now, the distinction is kind of buried: the classes ``Character``, ``Gadget``, ``Base``, and ``Vehicle``
lack a unifying abstraction or protocol. This needs to be fixed.

OO Design Advice
----------------

It's not at all clear this distinction between raw material and finished good **needs** to be present.
Superficially, it seems like everything's a ``Feature`` and that's all we need to know.

The use cases for design based on raw materials are an unstated element of the rules.
Technicall, we can argue that it's stated because design the essential purpose of
most of the rulebook. But. It's not stated as a simple "Here are things you'll design
based on raw materials we've already designed." And "When you design a Campaign, you'll often
be extending the pool of raw materials." Instead, it's assumed that you -- the reader --
understand the two kinds of design.

This is a chronic problem in software architecture.

There are things that are essential, but are -- like the atmosphere -- so pervasive
and invisble no one things to mention them.

There's more (of course.)

Software V5: Python 3
=====================

Interactivity was part of HyperCard (and the spreadsheets that preceeded it.)

The Python 2 and Python 3 definitions of a Character was something
I implemented as a simple script.
This isn't **too** interactive. You have an edit-run-crash cycle.

The scripts aren't complicated, and a simple ``Makefile`` rule can be used to rebuild
all the CSV's after a software bug fix or after a change to some Power definition.

The work flow is tweak something. execute the script, look for error messages. Not too bad
when compared with paper-and-pencil of thirty years ago.

Yesterday... (Seriously. Yesterday...)

It occurred to me that Jupyter Lab is a way to restore the original HyperCard interactivity.
The Character/Gadget/Vehicle/Base can be a cell.
I can run the notebook to validate the budgets for all the various bad guys in the scenario.

Over-budget? Tweak a definition until the cell stops printing the "over/under budget" error.

And.

I can write the supplemental stuff as Markdown. Right there. In the notebook.

Software V6: Adventure Books
=============================

There's a very small, dedicated markeplace for Hero content.

(See https://www.herogames.com, https://www.patreon.com/hero_games, and https://roll20.net/compendium/HERO/BookIndex#content)

While I'll never be a proper game author,
I can still write up a scenario in a tidy format as if it's still 1995 and I might
get a few bucks for an Adventurer's Club submission.

And this means using Sphinx, ReStructured Text (or maybe Markdown) to create a Scenario book.

I will slowly unearth my old campaign books (written in Pages) and convert them
to Python/Sphinx projects.
While it might be fun to imagine publishing them to HeroGames or Roll20, they're based 4th ed out-of-date rules.
So. It's a hobby project that pleases only me.
