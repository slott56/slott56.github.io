Essay 11 - Management Trump Cards
=================================

:date: 2005-09-15 15:13
:tags: architecture,software design,management
:slug: 2005_09_15-essay_11_management_trump_cards
:category: Architecture & Design
:status: published





I've seen two common varieties of management
trump cards.  These are played by managers who don't like the architecture, and
want to make changes.  These are a little bit like the spell cards in Magic:The
Gathering.  These cards can either change the state of the game (different
requirements, context, problem or constraints) or change the rules of the game
itself.



One management trump card is the "**Let's Step Back** " or "**Taking a 50,000 Foot View** ".
This card allows the manager to
reformulate the context, leading to a reinterpretation of the requirements. 
This, of course, changes the forces and constraints, the proposed solution and
the consequences.  This can be countered by the
"**Framework Focus** " or the
"**Appeal to Users** ".



A "**Framework Focus** " response emphasizes the generic
framework the underpins the solution.  Since this is based on non-functional
requirements, it may change only slightly when the problem is reformulated in a
new context.  We emphasize that no matter how the context changes, the solution
is still a web site running over tomcat.  We can, with patience, keep the
project on track in spite of the "Let's Step Back"
card.



An "**Appeal to Users** " response prevents context and problem
changes by making an authority (the users in the case) mediate the conversation.
In many cases, they don't care too mcuh.  You may find that the manager is
overruled by the users, or you are overruled.  Either way, the meddling will
continue.  If you were right, you may be able leverage the user's help.  If you
were wrong, you were wrong, and need to make appropriate adjustments.  Take your
damage.



Another management trump card is the "**I'm Fuzzy** " card.  This is played when the
architecture (or some element of it) is not what was expected.  You try to
answer the question and explain, but it won't work: this was not a question. 
This card is a demand for change that was framed rhetorically as a question. 
Since this card has a more technical focus, it requires a more involved,
technical response, generally "**Proof of Concept** ."



A "**Proof of Concept**" can take one of two forms: "**Demonstration**" and "**Evolution**".
The "**Demonstration**"
response builds a throw-away demo or proof-of-concept.  This is used to reduce
technical risks: a specific risk area has to be identified, and the results are
used to finalize the architecture.

An "**Evolution**" response is not a throw-away.  This is done when there are no real technical
risks, but a manager insists that something undefinable is still unknown.  When
there are no defined risks, nothing much will be learned.  You are, in effect,
building the first release of the software.








