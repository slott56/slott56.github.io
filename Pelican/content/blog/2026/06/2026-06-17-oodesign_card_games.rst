OO Design and Card Games
################################################

:date: 2026-06-17 07:32
:tags: python,object-oriented
:slug: 2026-06-17_oodesign_card_games
:category: Architecture & Design
:status: published

Lets look at my favorite OO-Design problem domain: card games.

We'll compare the design of two games: Cribbage and Canasta.

Why? Because they have three common abstractions: cards, hands, and a score.

Overall the player's are dealt cards, form hands, and at some point, accumulate a score. Of course, all of the implementation details are completely distinct.
Here's a use case diagram showing hands and the game overall; this can help provide some context.

..  figure:: {static}/media/cards/usecase.png
    :alt: Use Case Diagram

    Use case diagram for card games like Cribbage and Canasta.

The Humble Card
===============

A card has a small object model, but is fraught with obscure meanings.

..  figure:: {static}/media/cards/card.png
    :alt: Class diagram of card

    Essential class diagram of a card.

Like all real-world problem domains, the ``Card`` class has methods and attributes with deeper meanings.
The meanings are scattered throughout the hand, the game, the scoring, everything. Everything.

It can be **very** difficult to isolate and encapsulate the details of a card.

Mostly because, the details of a card are not part of the card itself. They're part of the context in which the card is used.

The point here is to put two contexts under the microscope: Cribbage and Canasta.

Cribbage
===============

Cribbage cards are used to form different scoring combinations:
pairs, runs of three or more, cards that sum of 15, and flushes.

Note that three or four of a kind are not separate combinations.
Three of a kind is called a "pair royal" and is scored as three separate pairs: the exhaustive enumeration of 3 things taken 2 at a time, :math:`\binom{3}{2}`.
(Really.)

Each scoring combination has a distinct point value.
In addition to the four listed above, there are also "his knobs" and "his heels" which are one card **in a specific context**.
The context is essential for this.

Flushes, similarly, have nuanced a context the other combinations lack.
But, we get ahead of ourselves.
The focus is on cards.

We need to distinguish between points scored in the game overall, and the number of "pips" on a card.
(I've sometimes blurred this distinction. Learning more card games has helped me understand the error of my ways.)

..  figure:: {static}/media/cards/card_cribbage.png
    :alt: Class diagram of Cribbage cards

    Class diagram for Cribbage cards.


The number of pips for a card is an abstraction, with two concrete implementations. For face cards (J, Q, K), the number of pips is 10.
For rank cards, the number of pips is the rank (1 to 10).

A Deck of cards, is a collection.
Creating the distinct card subclasses is the work of a ``Factory`` method of the ``Deck`` class.

::

    class Deck(list[Card]):

        @staticmethod
        def _make_card(rank: int, suit: str) -> Iterator[Card]:
            if rank <= 10:
                return RankCard(rank, suit)
            else:
                return FaceCard(rank, suit)

        def __init__(self):
            super().__init__(
                Deck._make_card(r, s)
                for s in ('♣︎', '♢︎', '♡', '♠')
                for r in range(1, 14)
            )

A scoring combination of a 15 means the total of the pips on the cards is 15.
This requires enumerating the powerset of all :math:`2^5 = 32` possible subsets of the four cards in the hand, plus the starter card.

(The ``powerset()`` function on the ``itertools`` page is your friend here.)

Canasta
===============

In Canasta, on the other hand, there are no "sums" of pips.
There is no ordering and there are no flushes.
Canasta melds are based on simple equality of rank.

But.

Of course there's a catch here.
Actually two catches.

There are wild cards. And there are jokers.
And, we'll have to worry about 3's, as yet two more special cases.

-   Jokers have neither suit nor rank.

-   2's are wild. They're essentially Jokers but with a rank and a suit. This will become a gnarly OO design issue.

-   3's are complicated.

    -   Red 3's (3♢, 3♡) are set aside for scoring purposes, and are replaced when they arrive in a hand. (If they come from the discard pile, they're set aside, but not replaced.) This also means they can't start the discard pile, and they're treated specially when they're the last card in the stock. Complicated, right? But most of those exceptions are part of the game, not part of the essential definition of a card.

    -   Black 3's (3︎♣︎, 3♠) cannot be drawn when they're on the top of the discard pile. (This is **also** true of red 3's. It never occurs, however, that they can get discarded, since they're set aside when they arrive in the hand.)

-   4's through 7's are only worth 5 points.

-   8's through K's are worth 10 points.

-   A's are worth 20 points.

Those considerations force us to add a few things to each card.

..  figure:: {static}/media/cards/card_canasta_1.png
    :alt: Class diagram of Canasta cards

    Class diagram for Canasta cards.

This lets us consider the following concrete subclasses of ``Card``.
This should cover all the the needed aspects.
Except, there's a problem.

..  figure:: {static}/media/cards/card_canasta_bad.png
    :alt: Faulty class diagram of Canasta cards

    Class diagram for Canasta cards, with design problems.

The problem is the ``Deuce`` complication.

-   Is it a subclass of the ``Joker`` class? If so, it would lack the rank and suit attributes.
    The alternative is unpleasant: the implementations of these attributes would have to be cloned from the ``Ranked`` class to add to the ``Deuce`` class.

-   Is it a subclass of the ``Ranked`` class? If so, its various methods would have to be cloned from the implementation of the ``Joker`` class.

This is where we can make use of a Mixin definition.
This is a Protocol that's shared by classes without regard to a simple hierarchy.

Mixin Design
===============

Each card has several clusters of aspects:

-   The rank and suit properties. (Except for Jokers.)

-   A ``match()`` method. For ``Wild`` cards, this is simply True. For ``Natural`` cards, it must compare ranks.

-   The weird rules for 3's: red suited 3's get set aside and replaced, while black suited 3's can't be drawn from the discard pile.

We can unbundle these aspects, and assemble classes from reusable components.
We call the overall design pattern a "mixin" design.

..  figure:: {static}/media/cards/card_canasta_base.png
    :alt: Base class diagram of Canasta cards

    Base mixin classes for Canasta cards.

The distinction between ``Ranked`` and ``Natural`` cards is important.
And clearly, to be a ``Natural``, the card needs all the aspects of a ``Ranked`` card.
The 2's are ``Ranked`` and ``Wild``.
All other ranks are ``Natural``.

We can then build individual subclasses from these.
We'll start with the two wildcard classes: ``Joker`` and ``Deuce``.

..  figure:: {static}/media/cards/card_canasta_wild.png
    :alt: Wild card class diagram of Canasta cards

    Joker and Deuce wild card definitions.

The ``Joker`` is ``Wild``. The ``Deuce`` is both ``Wild`` and ``Ranked``.
This is a very tidy capture of the nuances of these two distinct kinds of wild cards.

Of course the 3's include some additional features unique to their rank.
The class definition overrides some definitions from the base ``Card`` class.

..  figure:: {static}/media/cards/card_canasta_trey.png
    :alt: Trey card class diagram of Canasta cards

    Red and Black Trey card definitions.

Threes are -- in a way -- Naturals.  They're not Wild.
The nuance is that other game rules preclude 3's from being melded or used as naturals to draw the discard pile.
There's a special "can only meld as part of going out" rule that we've omitted to save space.
It's yet another method that's True for the ``Trey`` class and False for all others.

Finally, the rest of the deck.

..  figure:: {static}/media/cards/card_canasta_other.png
    :alt: Other card class diagram of Canasta cards

    The LowRank, HighRank, and Ace definitions.

Each of these class has almost no unique code in it.
Mostly the point value used to total up the points melded (and the points unmelded still in the hand.)

All in one diagram, this looks like a terrible tangle.
Separated like this, we can see how the deck of cards is built from instances of
all the concrete subclasses: ``Joker``, ``Ace``, ``Deuce``, ``Trey``, ``LowRank``, ``HighRank``.

Python Code
===============

Here's some code to go with the pictures.

::


    from abc import ABC, abstractmethod

    class Card(ABC):
        @abstractmethod
        def points(self) -> int: ...

        @abstractmethod
        def matches(self, other: "Card") -> bool: ...

        def replace_me(self) -> bool:
            return False

        def safe_discard(self) -> bool:
            return False


    class Ranked:
        rank: int
        suit: str

        def __init__(self, rank: int, suit: str) -> None:
            self.rank = rank
            self.suit = suit

        def __str__(self) -> str:
            ranks = {
                1: 'A',
                10: 'X',
                11: 'J',
                12: 'Q',
                13: 'K'
            } | {r: str(r) for r in range(2, 10)}
            return f"{ranks[self.rank]}{self.suit}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self.rank}, {self.suit})"

    class Natural(Ranked):
        def matches(self, other: Card) -> bool:
            match other:
                case Wild():
                    return other.matches(self)
                case Ranked():
                    return self.rank == other.rank
                case _:
                    return NotImplemented

    class Wild():
        def matches(self, other: Card) -> bool:
            return True

We can build the various card classes. With the mixin design, we can avoid repeating code.

::


    class Joker(Wild, Card):
        def points(self) -> int:
            return 50

        def __str__(self) -> str:
            return "? "

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}()"

    class Deuce(Ranked, Wild, Card):
        def points(self) -> int:
            return 20

    class Trey(Natural, Card):
        def points(self) -> int:
            if self.suit in {'♢︎', '♡'}:
                return 100
            else:
                return 5

        def replace_me(self) -> bool:
            return True

        def safe_discard(self) -> bool:
            return True

    class LowRank(Natural, Card):
        def points(self) -> int:
            return 5

    class HighRank(Natural, Card):
        def points(self) -> int:
            return 10

    class Ace(Natural, Card):
        def points(self) -> int:
            return 20

It's a little tricky imagining how to build the deck as a whole, but a ``Factory`` function is the ticket.

::


    class Deck(list[Card]):

        @staticmethod
        def _make_card(rank: int, suit: str) -> Card:
            if rank == 1:
                class_ = Ace
            elif rank == 2:
                class_ = Deuce
            elif rank == 3:
                class_ = Trey
            elif rank in {4, 5, 6, 7}:
                class_ = LowRank
            else:
                class_ = HighRank
            return class_(rank, suit)

        def __init__(self):
            super().__init__(
                Deck._make_card(r, s)
                for s in ('♣︎', '♢︎', '♡', '♠')
                for r in range(1, 14)
                for _ in range(2)
            )
            self += [Joker()] * 4

What's important is assembling the needed class definitions from a pool of separate aspects.
The combination of aspects achieves reuse of the aspect definitions, and avoids trying to force the definitions into a too-simple class hierarchy.
