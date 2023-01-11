How to Make Technology Choices
==============================

:date: 2013-06-26 16:58
:tags: complexity,architecture
:slug: 2013_06_26-how_to_make_technology_choices
:category: Technologies
:status: published


I get emails looking for help with technology choice. Essentially:
"I've got this idea for game-changing software idea, what technology
should I use?" These questions have disturbing expectations. There's a
Gordian Knot of dependencies that's sometimes baffling.

Sometimes the questions are about choosing a "tech stack" or an
"architecture". Sometimes it's the "framework" or the "platform".

All the questions, however, are very similar. They amount to either
this

    **"What's the one, perfect and final technology choice we need to make?"**


or this


    **"We're considering [X, Y and Z] can you validate this choice?"**


Notice that the emphasis is on making **One** **Perfect** **Final** **Decision**.

An incidental part of this question is the context: this varies
widely:

-   There might be a pretty good software idea.

-   Sometimes there's a list of user stories or use cases. Other times,
    there's a blatant refusal to consider human users, and a bizarre
    focus on technologies.

-   Less often, there's some sense of the business model; i.e., who will
    pay for this. Simply saying "advertisers" is a hint that there's no
    business model. Lack of a business model is a hint that technology
    choices are premature.


I'm not asked handle questions on business models; I'm not a venture
capitalist; I'm just a tech consultant. But I expect that a business
model is in place. Technology choices support a business; not the
other way around. If there's no income, then there's no point in
making technology choices, is there?


**Unreasonable Expectations**


What's disturbing are the expectations. We'll start with one
expectation that is disturbing and then look at another.


The expectation of **finality** is the most disturbing: the
expectation that someone can
make **One** **Perfect** **Final** **Decision**.


No technology choice is ever final. Today's greatest ever
state-of-the-art, kick-ass-and-take-names SDK may evaporate in a
cloud of lawsuits tomorrow. Today's tech giant may collapse. Today's
platform of choice may be tomorrows weird anachronism.
Worse, a super-popular framework or platform may—after deeper
examination—be totally brain-dead regarding some specific API or
standard. Details matter, and details emerge slowly. A vendor (or
open source community) may claim that it's (for example) RESTful, but
you won't know until you try it.


**Principle 0**.
Software Development is Knowledge Capture. You do
not already know **everything** about the business, the technology or
problem being solved. If you already know everything, it means you
learned everything based on already having working software.


**Principle 1**.
Change happens. A fixed technology stack is a
mistake. A fixed set of interface specifications is less of a mistake
than a fixed set of technology choices. Software development involves
learning, and while the learning is going on, the marketplace is
changing. Note that learning is a two-way street, also. You learn
about the users, the users learn about your technology. The problem
you're trying to solve can morph as the users learn.


**Principle 2**.
Change happens quickly.  As you learn about the
marketplace, the problem, the technology and the business model,
you'll be changing your software. Agility matters more than
perfection. The most adaptable solution wins.


This next rule is harsh. But it's important.


**Principle 3**.
If you have nothing to demonstrate, you have
nothing. A good idea without a demo is difficult, almost impossible
to work with. Without a demo, it's all just hand-waving. You must
encode your knowledge in working software **before** you can make a
technology choice.

Yes. It's circular. Sorry. You can't make a software technology
choice until you have demo software that shows the problem areas. You
can't create the demo without making a (potentially inappropriate)
technology choice.


**Demo To Product**


When I ask about the existence of any demo software, I get into
trouble because some folks don't want to even start building a demo
until they have the **One** **Perfect** **Final** **Decision** firmly
in hand.


This leads to a second unreasonable expectation.



The expectation of **continuous evolution** from demo to product
is also disturbing: the expectation that even one line of code
from the initial demo will become part of the final product.


Getting from idea to product will involve many changes. The user
stories, the technology choices, the business model, every aspect
is a candidate for a disruptive change. Success comes from making
these changes. The first developer to abandon a bad idea is the
furthest ahead. The most adaptable solution wins.


**Cutting the Gordian Knot: Making Choices**


Making a final, perfect technology choice for building the initial
demo is not even helpful.
So don't.
Cut the Gordian Knot by building something. Build early. Build
often.


What's essential is to build something which (a) works, (b) has
automated tests, and (c) can be evolved as the user stories evolve
and improve. As you learn, you'll encode your evolving knowledge
into evolving software. This is what software development really
is: learning and encoding.


The initial demo may have to be discarded because better technology
is located. Usually, however, the initial demo must be discarded
based on experience in the marketplace, experience with the users, or
experience solving the user's problems. It's more often these "other"
non-technology lessons learned that trash the initial demo.


It's impossible to make a "future proof" technology choice. The
future technology alternatives are difficult to know in advance. We
distinguish between future and past by the lack of certainty in the
future. As experience is gained, the initial round of user stories
will get rewritten or possibly even discarded. A technology choice
based on obsolete user stories is a liability, not an asset.


Some folks beg for something that will be "scalable" or "responsive"
or "efficient" without having any actual scaling or performance
problem that needs to be solved.


Using appropriate data structures and algorithms leads to inherently
high-performance software. Beyond this vague platitude nothing much
can be said.


Until.


Until there's a demo that has a specific scalability issue or
performance bottleneck. Once a problem has been uncovered, then
there's something to solve, and technology choices begin to matter.
Most of the time, this will be a data structure or algorithm choice.
Less often, this will be a larger architectural choice regarding
parallelism or persistence.

**Hand Wringing**

"But what if," the professional hand-wringer asks, "What if my user
stories are perfect, my demo is perfect, but I've made some
sub-optimal technology choice and I'm forced to rework **everything**
for purely technical reasons that—in hindsight—I could have
foreseen?"

The answers are (A) Are you an absolute genius of flawless user story
creation? (B) Is your code so bad that the rewrite is more than just
a refactoring? (C) When did you plan to fix you code so it could be
refactored? (D) Did you really think you were never going to be
forced to make a core technology change?

"But what if," the hand-wringer asks, "What if I can't afford to
write the whole thing twice."

The answers are (A) Is your business plan so fragile that a rewrite
invalidates everything? (B) What do you think "user support" entails?
(C) What will you do when users ask for new features?

If this is about "time-to-market" and you have to rush to be early or
first or something, then technology choice doesn't matter, does it?
Time to market matters. So build something that works and get it to
the market first.

"But what if," the hand-wringer asks, "I choose a lousy platform
initially?"

The answers are (A) Nothing is really wrong, it's just somewhat more
costly or somewhat more complex. (B) So do others. (C) They rewrite,
also.

"But what if I don't have skills in the best technology choice? What
if I master a lousy technology to build the demo and release 1 and
now I have to learn a whole new technology for release 2?"

The answers are (A) Did you really think that any technology would
last forever? (B) Why can't you learn something new?


**Basic Rules**


The essential rules are these.


  **Build Early. Build Often.**


The first step in making technology choices, then, is to pick a
technology that you can actually make work, and build a demo.


Once you have a demo, recruit some potential or actual users.


Learn your lessons from these users: solve their problems: be sure
your software is testable: troubleshoot your software as it is
applied by **real** users to their **real** problems.
Plan to rebuild your demo to satisfy your user's demands. You will be
learning from your users.


In order to maximize the learning, you're going to need to log
carefully. The default logging in something like Apache is useless;
log scraping is useless. You'll need detailed, carefully planned,
application-specific logging to capture enough information that you
really know what's really going on.


Once you have working software with real users, you're going to
switch into support mode. You'll be using your application-specific
logging to figure out what they're doing.


  [War Story. For testability purposes, I added a special logger for
  a particularly gnarly and visible calculation of actuarial risk.
  The logger dumped **everything** in a giant JSON document. To
  simplify debugging, I wrote a little app that loaded the JSON
  document and produced a ReStructured Text document so that I could
  read it and understand it. When requested, I could trivially pump
  the RST through docutils to create PDF's and send them to customer
  actuaries who questioned a result. This PDF-of-the-details became
  a user story for a link that would show supporting details to an
  actuarial user.]


Once you have working software, and a base of users, you can consider
more refined technology choices. Now the question of PHP vs. Python
vs. Java might become material.

    [Hint. The right answer was RESTful web services with Python and
    mod_wsgi all along. Now you know.]


When the product is evolving from release 1 to release 2, you may
have to reconsider your choice of database, web server, protocols,
API's, etc. It turns out you're always going to be making technology
choices. There will never be a final decision. Until no one wants
your software.


If you are really, really lucky, you may get big enough to have
scalability issues. Having a scalability issue is something we all
dream about. Until you actually have a specific scalability issue,
don't try to "pre-solve" a potential problem you don't yet have. If
your software is even moderately well design, adding architectural
layers to increase parallelism is not as painful as supporting
obscure edge cases in user stories.

When you're still circulating your ideas prior to writing a demo, all
technology choices are equally good. And equally bad. It's more
important to get started than it is to make some
impossibly **Perfect** **Final** **Decision.** Hence the advice to
build early and build often.



-----

I would suggest 2 questions

1) What is your produ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2013-06-26 19:25:38.324000-04:00

I would suggest 2 questions

1) What is your product/market fit and how do you plan on verifying it?
I borrowed the above from the lean startup literature.

2) Are you really building a business or is this a hobby?
There is nothing wrong w/ a hobby but be honest about it.


Both of which are answered by building something.
-------------------------------------------------

S.Lott<noreply@blogger.com>

2013-06-26 19:39:19.561000-04:00

Both of which are answered by building something.





