The Wrong Abstraction Problem
=============================

:date: 2020-01-14 08:00
:tags: Design Principles,architecture
:slug: 2020_01_14-the_wrong_abstraction_problem
:category: Technologies
:status: published


For the last week I've been working with some legacy code that reveals
a kind of problem I hadn't really seen before.

I'm calling it the **Wrong Abstraction**.

I want to contrast this with the **Leaky Abstraction**, where
implementation details are revealed and raise havoc.

The **Wrong Abstraction** problem seems to arise when a specification
is too technical. A detailed, code-like tangle of if-then-else becomes
its own problem. I'm guessing someone worked to detail **all** the
technical considerations. The chosen format as code-like text was not
a great idea. The cyclomatic complexity of the specification is
through the roof. And the code reflects this failure to actually
capture anyone's underlying intent.

Cue the gif from the office. https://gph.is/1m89uqR Someone with
"people skills" tried to recast the business intent into technical
if-then-else.

Details
-------


The context doesn't matter very much, but it can help people visualize
the problem.

We're talking about validation rules. A document arrives, perhaps it's
source code, or perhaps it's a shopping cart, or perhaps it's a schema
definition. The document is validated according to some fairly
sophisticated rules.

-  There's the obvious syntax check: is it valid JSON or Python or
   whatever the language is.

-  There are isolated validity checks. Individual elements (statements,
   items in the cart, subschemas) have to be valid.

-  There are aggregate validity checks. Groups of items -- the cart
   overall -- must satisfy some additional criteria. In our case, nine
   additional rules.


Some of the rules are complex. I think they original intent was
drafted by a committee. It's visible, and involves large piles of
money and potential lawsuits. Serious rules.

There are at least two separate implementations, mostly in JavaScript.
(I'm not here to curse out JavaScript. The language has a lot of wat
-- https://github.com/denysdovhan/wtfjs -- but that's not the point.)

So, you ask, where's the Wrongness?

It's a vast gap between intent and implementation.

Mind the Gap
------------


The source documents decompose the validation into 9 steps. There's an
explicit "all or nothing" disclaimer. That's nice.

The code looks more-or-less like this:

::

   valid = True
   for item in cart:
       for r in (Rule1, Rule2, Rule3, Rule4, ..., Rule9):
           if applies(r, item):
               valid = valid and r(item)




It turns out, though, we don't really apply all 9 rules like this.
This is **The Gap**.

We actually have three types of items in the cart (or code or schema
or whatever.) One type item has a default, a hidden feature of rule 1.
It breaks down like this.

-  Rule 1 applies to an item of Type A. If the Type A item is omitted,
   the default value will pass the Rule 1 check.

-  Rule 2 applies to all the items of Type B. Only.

-  Rules 3 to 8 apply to the items of Type C. Only. And they work in
   pairs, 3-4, 5-6, 7-8.

-  Rule 9 applies to a subset of items of Type C. The C9 subset.


Code with a nested "for all items" and "for all rules" is -- well --
wrong. It's flat-out lying about the validation rules and the objects
(and collections) being validated. It's lying to a level that seems
unconscionable to me. But. Maybe there's a reason.


The validation is really something more like this.


::

      valid = Rule1(filter(lambda item: item.is_a, cart))
          and Rule2(filter(lambda item: item.is_b, cart))
          and all(
              r(x) 
              for r in (Rule3, Rule4, Rule5, ..., Rule8) 
              for x in filter(lambda item: item.is_c, cart)
          )
          and Rule9(filter(lambda item: item.is_c9, cart))


This reflects the actual structure of item types and rule types
without wrapping them in a wrong abstraction.

(It's actually \*more\* complex than this, but, this is enough to
expose the core issue.)

Why The Gap?
-------------

There are a number of causes. In part, the gap seems to reflect a
disconnect between **intention** and **implementation**. Indeed, this
seems to be an example of `Conway's
Law <http://www.melconway.com/Home/Conways_Law.html>`__.

      "Any organization that designs a system (defined broadly) will
      produce a design whose structure is a copy of the organization's
      communication structure."

I think the for item in cart: for rule in (Rule1, ..., Rule9):
structure reflects some intermediate design work between the
original intent and the developer who implemented the code.

The extra layer of design work was a failed attempt to "simplify"
things for the developer. I can imagine the conversation.

**Designer**:
    "It's simple. There are 12 rules. Each rule applies
    to each item."

**Developer**:
    "Rule one only seems to apply to Type A. So maybe
    it's not simple."

**Designer**:
    "It's simple. Don't make it complex. Write an
    'applicability' test. Evaluate the rule if it applies to the
    item."

**Developer**:
    "So it's not trivially all rules against all items?
    Could we associate subsets of rules with the separate item types?"

**Designer**:
    "No. You're making it complex; It's simply
    evaluating all 12 rules against each item. If the rule applies to
    the item type. Other than that, it's simple."

**Developer**:
    "Instead of the 'applicability test,' could we
    group the rules?"

**Designer**:
    "No. You're making it complex."

I also think the gap also reflects an inability (or a lack of
permission) to hack incrementally.

Incremental Development
-----------------------

One of Python's strong suits is the ability to run code at the >>>
prompt. Confronted with a complex data structure and complex rules,
some of us will try different designs on for size as quickly as we
can. We hack out the essence of the code and see if it would make
sense in a tutorial explanation.

I've darted down any number of dead-ends trying to get a sensible
abstraction that I can understand and explain. The idea is to write a
bit of code, mess around, and then decide to backtrack or push
forward. (For a lot of people, `rubber
ducking <https://en.wikipedia.org/wiki/Rubber_duck_debugging>`__ or
`pair programming <https://en.wikipedia.org/wiki/Pair_programming>`__
helps with this.)

When you're only a few lines of code into the problem, it's easy and
fun to delete it all and start again. Or. It \*should\* be easy and
fun. Some folks worry about deleting bad code and starting over.

I think the overall context didn't facilitate hacking around. The
documentation talks about creating mock documents (or carts or
collections) of items for testing purposes. I don't think anyone
tried that. I'm not sure they knew the feature was available. I think
they put the validation code into the framework, ran it in the
development environment, looked at the debugging logs, changed the
code, deployed, and ran things again until it worked. A long, painful
slog, where backtracking would be considered a horrible set-back.

The complex "applies()" test has a surprising bunch of if statements
that don't seem to reflect the actual properties of the three types
of items. It seems to reflect an evolving series of guesses about
attributes that were present or absent.

When I was younger, writing COBOL, PL/I, Fortran and the like, that's
how we worked. Run it. Look at logs. Run it again later in the day.
The long, slow development cycle meant that as soon as something
looked like it was working, we called the project 90% complete.

This lead inexorably to the
`ninety-ninety <http://catb.org/jargon/html/N/Ninety-Ninety-Rule.html>`__
rule.

      "The first 90% of the code accounts for the first 90% of the
      development time. The remaining 10% of the code accounts for the
      other 90% of the development time.”

Even if the abstraction is wrong. We've take 90% of the time to get
something that works. There's no fixing it, now. We have to ship
something, so we spend the next 90% of the time working around the
wrongness and filling in gaps that shouldn't have existed.

A horrid development environment tends to prohibit refactoring. You
can't simply run the test suite with refactored code because the test
suite is neither fast nor fully automated. In this case, I don't
think it runs in a handy form on the desktop, but requires a
dedicated server. Without a Docker container for each developer, I
think the project gets paralyzed and stuck with icky code and me
doing a very expensive rewrite.

tl;dr
-----

An utterly wrong abstraction seems have two root causes:

-   Too many designers

-   No ability to delete the garbage abstraction and start over with
    something better

-   No simple unit test environment to support refactoring





