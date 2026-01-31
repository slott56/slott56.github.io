TTRPG Progress Report
###########################

:date: 2026-01-31 10:31
:tags: #python,games,ttrpg,dsl
:slug: 2026-01-31_ttrpg_progress
:category: Python
:status: published

See `The eval() Conundrum <{filename}/blog/2025/09/2025-09-28-the_eval_conundrum.rst>`_ for background.
Also, see https://github.com/slott56/writing-tools.

Permit me a long story about budgeting and a language to describe magic.
The story leaves footprints that reveal the impossibility of making the right design choices up front.

..  important:: TL;DR.

    Almost all software design seems to require making bad choices and fixing them.

The story takes place in the world of Table-Top Role-Playing Games (#TTRPG), a fairly complicated subject because the games are designed by folks who (generally) like action and adventure stories.
(There are those folks like to sniff and say “genre fiction” as if action and adventure and fantasy and sci-fi and all that are somehow less worthy than “literary fiction.” Bah. Humbug.)

The folks who write the TTRPG rules are — in effect — writing meta-fiction.
Game rules are -- in a way -- an analysis of a genre; they summarize the important features of a genre.
The writing is aimed at a broad segment of casual game players, not data analysis or software architecture professionals,
This isn't a sophisticated ontology.

I think of the game designers as comic-book writers distilling their experience of writing comic books to create a tidy set rules we can use to play around with the tropes of our favorite genre.

My goal is to extend published **OpenD6** rules with some rules of my own.
I have some world-building and campaign ideas I'd like to capture.
I like the **OpenD6** system because it has an Open Game License (OGL), see https://opengamingfoundation.org/licenses.html.
While I spent a lot of time on the Hero V4 game system, it's not easy for new, casual players.
The **OpenD6** has some of the sophistication of Hero with an easier on-ramp.

One feature I really like about the Hero system and the **OpenD6** system is
the presence of budgeting rules to constrain characters or powers or devices or effects.
These are a necessary part of story-telling.
For example, Aladdin’s djinni suffered from a constraint of being imprisoned in a lamp.
Clearly, the djinni has some profound weakness that can be exploited by an enemy.

Game Mechanics
--------------

Budgets are hard, but necessary.
The **OpenD6** rules have an elegantly simple budget mechanic for creating characters.
I’ll spare you the details.

Additionally, **OpenD6** assigns an elegantly simple difficulty level to activities.
Things like falling down the stairs or spilling coffee into your keyboard have very low difficulties.
Other things, like debugging software, have a much higher difficulty.
During game play, the Game Master may introduce other confounding factors or conditions: tired, confused, shivering in the cold of a Western North Carolina winter.
These can all increase the difficulty to a level where the character may need to ...
(I’ll spare you the game details of game play, also.)

The **OpenD6** rules for determining the difficulty of a magical spell are very complicated. Very.

The complications in the magic systems rules make it difficult to extend the published rules with any confidence.
There's no easy test to see if what you’re doing is right.
Careful reading of the rules uncovers small discrepancies: is it my understanding or is there an error in a specific spell's difficulty summary?

Following the Paper Trail
-------------------------

I started out with some PDF's of OpenD6 rules.
In order to really understand the magic system, I created a Domain-Specific Language (DSL.)
This let me transform the text display of a spell into a data structure that preserved the content.
A little bit of text parsing would uncover the essential difficulty numbers for the various aspects of a spell.

(With a tiny bit of processing, I could emit Restructured Text that would reproduce the printed material.)

A few places didn't add up properly, but that's to be expected.
It's a big book with a lot of rules.

I have V1 of the Domain-Specific Language for OpenD6 spells.
The overall syntax is Python.

Looking back, the footprints proceed from book to code pretty directly.
One can feel good about one's progress when it follows such a straight line.

This V1 DSL is not ideal.
It lacks an important feature.
The big gap is the difficulty values are simply stated: they're a literal number.
They are not derived from the details of the spell.
We can't change anything without also having to manually compute a revised difficulty and updating the literal number.

All the V1 DSL does is sum the difficulties for us.

Proper Computations
-------------------

Computing the difficulty of each individual aspect of a spell is -- for the most part -- elegant.
A lot of the **OpenD6** spell aspects are based on ordinary Kilogram-Meter-Second (KMS) measurements.
(Yes, the magic has a thin veneer of physics.)

There's a "measure-to-value" transformation.
Given a measure, :math:`m`, the value, :math:`v`, is this:

..  math::

    v = \begin{cases}
     &\lceil 5 \log_{10}(m) \rceil_{u} \textbf{ if $m < 10$}\\
     &\lceil 5 \log_{10}(m) \rceil \textbf{ if $m \geq 10$}
    \end{cases}

Where :math:`\rceil_{u}` uses ``decimal.ROUND_UP``,
and :math:`\rceil` uses ``decimal.ROUND_HALF_UP``.

The rules provide a handy table for this.
The rules even provide some benchmark values to save you from having to look up the mass of something like a warhorse.
The associated value is 14.
(The number of kilograms is :math:`10^{\frac{14}{5}} = 630.9`, FWIW.)

This isn't always elegant.
From the various rule books, I extracted over 400 spells.
A bunch of text parsing (and manual cleanup) created the V1 spells.

Creating the V2 DSL, on the other hand, required revisiting each of the dozen or so effect types, and thirty or so aspect types.
This -- it turns out -- is not a simple linear path from V1 to V2.
Some wrong turns were made.

Many of the effects and aspects follow the elegant KMS measure to Value rules.
It was easy to separate the difficulty numbers from the base measurements.
The DSL processing could parse the measurement, and compute the difficulty.
The originally published numbers from the V1 DSL became unit test expected results for the V2 DSL.

This effort uncovers a number of things.

-   Ordinary editing errors, where the numbers aren't **exactly** right.
    A common problem looks like the author's rounding was inconsistent.
    Or, perhaps, the author made a change and didn't check all the math carefully.

-   A few gaps where the spell details simply don't add up.
    (Not many of these, the quality of the publication really is quite good.)

-   Places where the text of the rules is impenetrable.
    Assumptions need to be made.
    If the code written around the assumptions reproduces the printed rules, the code is not **wrong**.
    But, since the code doesn't obviously fit the explanatory text, it's not **right**, either.

-   The "based-on" rules.
    There are four kinds of aspects where the difficulty is derived from another aspect.
    (Skipping the details...)
    Only two cases are similar.
    The other two are utterly unique.

Going through 40+ effect and aspect definitions has consequences.
Potentially bad consequences.

The Organic Evolution Path
--------------------------

First, and foremost: since I didn't write the rules, I have no "big picture" overview of **OpenD6**.
I'm building the big picture by starting with individual details.
This is inductive discovery.
Review the parable of the blind men trying to understand the shape of an elephant by touching individual parts of the animal's body.

Everything is the design of V2 DSL is going along swimmingly until I stumble into the first "based-on" aspect.

The overall architecture had been really simple.

    **All aspect difficulties (and the effect difficulty) are based on measure, modifiers, and factors.**

    **A spell's difficulty is the sum of the effect and aspect difficulties.**

(I've omitted some details about the debit-and-credit feature of the aspects.)

We can say:

..  math::

    d(A) = f(p(t))

The difficulty of an Aspect, :math:`d(A)`, is a function of parsing the text of the aspect, :math:`p(t)`.

And,

..  math::

    d(S) = \frac{\sum\limits_{A \in \mathbb{C}}{d(A)} - \sum\limits_{A \in \mathbb{D}}{d(A)}}{2}

The difficulty of the Spell, :math:`d(A)`, is based on the sum of the difficulties of the aspects.
(Some aspects are credits, :math:`\mathbb{C}`, while the others are debits, :math:`\mathbb{D}`.
The rules use the term "negative modifiers" for the debits, all the rest are credits.
We could use :math:`\mathbb{N}` for the debits and :math:`\mathbb{A}-\mathbb{N}` for the universe of attributes, :math:`\mathbb{A}`, without the negative modifiers for the credits. Too much detail. Sorry.
)

The simple rules are broken.
Each aspect is not simply an independent computation.

We need to backtrack and refactor to accommodate a special case.
The overall architecture is now this.

    **There are two classes of Aspects:**

    -   **An Independent Aspect difficulty is based on measure, modifiers, and factors.**

    -   **A Dependent Aspect depends on another aspect.**

    **The Effect difficulty behaves like an Independent Aspect.**

    **A Spell's difficulty is the sum of the effect and aspect difficulties.**

This means we need to do a topological sort of aspects to put them into an order
so the independent ones are computed first, and the dependent ones are computed second.

So?

Here's what we've learned (again.)

..  important::

    The object model evolves, based on the examples found by wandering around a featureless plain, littered with requirements.

We can't foresee the coming complications and special case exceptions.
We're going to break things and refactor each time we learn something.
There are 40+ aspect and effect definitions.
We've got all but two types of aspects working.
Of the 400+ spells, many are working correctly, computing the difficulties from the details.

Back when the waterfull project plans where considered important,
I was always troubled when the team was constrained by a fantasy plan, written long before anyone had a clear idea what was going on.
The more I learn, the more I learn that putting a time box around learning was evil.

That's Not Right
-----------------

The V2 DSL effort includes two surprisingly complicated aspect class definitions.

-   An aspect that doesn't depend on another aspect, but depends on the spell's central effect.
    This isn't all that complicated: the effect is a special case of the other aspects.
    But, it's unique.
    And could not be foreseen, and leads to backtracking and refactoring.

-   An aspect that depends on the effect and a modifier.
    This is, also, unique.
    And requires yet more backtracking and refactoring.

The overall data model isn't **broken** in the sense that it doesn't work.
Indeed, the type hints all work out perfectly.
The test cases all pass.

The organic evolution of the object model has been a wandering path across a nearly trackless plain littered with aspect types.
As we explored the aspects, we found reasons to go back to the beginning and make changes with profound ripple effects.
This created a number of problems.

-   Code that feels like an *ad hoc* solution because we found it later in our wandering through the requirements.

-   Code that's clearly copied-and-pasted because some inheritance v. composition issue was not resolved well.

-   Code that doesn't map to the explanatory text of the rules in any clear way.
    It may produce the right answer, but it doesn't really capture the meaning or the intent in the explanation.

The Far Side of the World
-------------------------

Where are we?

V3.1 of the DSL passes the unit tests.

It seems to be defensible.

The "based-on" complications are minimized and regularized.
A few classes have special methods to handle the three based-on cases.

It feels like all of the class definitions can be partitioned into two families:

-   The code comes from the rules in a direct and obvious way.
    For example, a lot of the **OpenD6** rules include a table of alternatives.
    These map to ``Enum`` subclasses.

-   The code is a purely technical part of the Python DSL and feels almost generic.
    (*Almost* generic. This is a TTRPG DSL, so it's not truly Standard Library generic.)

Time to move on to the type checking.
