Domnain-Specific Language
############################

:date: 2025-03-11 15:52
:tags: #python,domain-specific language,dsl
:slug: 2025-03-11-domain_specific_language
:category: Python
:status: published

Generally, I try to frown on Domain-Specific Languages.
Often, a tidy set of related functions, or a group of class definitions with a few decorators can create something that's every bit as expressive as a DSL in native Python syntax.

There are a few cases where a DSL can be handy.

One of which is when embedding complicated content in Gherkin test cases.

(We'll get the context later. I want to focus on the problem at hand.)

We need to write Gherkin that looks like this:

..  code-block:: cucumber

    GIVEN some configuration
    WHEN we run the Character UI with input of "..."
    THEN we see the right kind of responses in the log and what-not

What's essential here is the input to the Character UI (CUI).
It's a sequence of characters.

In Python, it might be ``"o" + 2*"mu" + "i" + "qy"``.

The idea is to provide a meaningful sequence of commands for the given scenario.

Except, of course, Gherkin isn't Python.

We have two choices:

-   Use ``eval()`` to evaluate a Python expression.

-   Use a DSL.

Since this is a test scenario, the ridiculous arguments about ``eval()`` being "unsafe" are clearly worthy of ridicule.
Any Evil Super Genius capable of writing a Gerkin test case that includes ``import os`` or ``import subprocess`` has access to the source code and doesn't need to subvert the Gherkin language test scenarios.

While ``eval()`` is appealing because it's simple, it's not always ideal.
In particular, some of the scenarios are long, and the sequence of input commands needs some supplemental information to follow through the actions and the responses to work out what the expected intermediate and final states will be.

The Context
===========

I'm working on a Rogue-Like game. The test scenarious involve walking around and collecting treasure,
bashing monsters, and avoiding traps.
The interactions aren't too complicated, but, I'd like these Gherkin-based acceptance tests to involve an absolute minimum of specialized test harness.
A code tweak to seed the random number generator seems to be all that's appropriate.

In the long run, there's a potential to work through some clear definitions of the various features of the game using RDF.
SPARQL queries might provide ways to locate the features of items or behaviors of monsters.

The Complication
================

What we want to have is something like this.

::

    o                          ⍝ acknowledge splash
    room 1≔ ⟨m l⟩×4 ⟨m u⟩×2 i  ⍝ to the room exit
    hall 1≔ ⟨m u⟩×5 i          ⍝ to the next room entrance
    done≔ q y

We've wrapped the essential commands in a bunch of syntax to make the commands a bit more clear.
I can include a label at the left end of the line, and a "comment" on the right end.

Here's what's tricky.

The test case string will contain *almost* any ASCII character found on the keyboard.
We don't want to have a lot of meta-punctuation that's **also** on the keyboard.

This bumps into the same problem the classic Regular Expression language suffers from.
We want to match characters.
And we need the same set of characters to have meta-level meanings.
Sometimes ``.`` means the damn dot.  Sometimes ``.`` means "any" character.
So we have to use ``\.`` vs. ``.``  to express the distinction.

I decided to do this.

Use Unicode
============

I could wrestle with some "meta" characters for grouping and repetition.
Indeed, I could parse the ordinar Regular Expression language.
These are -- technically -- regular expressions that summarize long strings of characters for the test cases.

Or.

I could use a few Unicode characters separate from the ASCII keyboard characters that would be input.

-   ⟨ and ⟩ (MATHEMATICAL LEFT ANGLE BRACKET, and MATHEMATICAL RIGHT ANGLE BRACKET)

-   × (MULTIPLICATION SIGN)

-   ≔ and ⍝ (COLON EQUALS, and APL FUNCTIONAL SYMBOL UP SHOE JOT)

-   ␛, ␠, ␤ for Escape, Space, and Newline.

These eight additional characters are not on the keyboard.
The game will never use these as input.
I don't need to use fancy escape sequences to distinguish these meta-characters from the ASCII characters that are being generated.
These few characters are difficult to type: you have to pluck them off the Unicode character pop-up window that Macos offers you.

The code to handle the Gherkin doesn't have to fuss around with hyper-complex-looking regular expressions to parse this DSL.
The allowed input characters are ``.`` and the meta-characters are simply presented as literal values in the regular expression.
(As noted above, this DSL is a regular expression language. It's highly limited.)
