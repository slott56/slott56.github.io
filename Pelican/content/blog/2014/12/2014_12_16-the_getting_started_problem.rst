The Getting Started Problem
===========================

:date: 2014-12-16 20:03
:tags: building skills books,learning,packtpub
:slug: 2014_12_16-the_getting_started_problem
:category: Technologies
:status: published

How does one get started developing software? What's the first step?

When you come to this craft -- or sullen art -- without a background
except as a user, how do you get started writing code?

It's not easy. Indeed, developing software may be one the hardest
things there is. Really, really hard.

Why? Consider the orders of magnitude involved. From sub-microsecond
clock speeds to software that's supposed to continue running for 8,763
hours a year without interruption. That's 31,547,269 seconds. Isn't
that about 15 orders of magnitude?

Or consider scope of storage. We wrangle over bytes in a dataset that
spans terabytes. That's 12 orders of magnitude.

When engineers build a 13,000' long bridge, are they looking at it
from scales of 10\ :sup:`±5`? Do they even care what's 21 miles away?
They might care about things at the scale of 10\ :sup:`-5`, since
that's about an inch. But 10\ :sup:`-7`? 100\ :sup:`th` of an inch? I
could be wrong, but I have doubts.

I won't go so far as to say bridge building is particularly easy. It's
safety critical work. People die when things go wrong. Consequently,
it's regulated by civil engineering standards. Bridge designs are
limited to proven patterns. You can't spring something new on the
world and expect anyone to pay money for it or trust their life to it.

If you're with me so far, you see my point: software is different. And
that makes it particularly hard. People do learn elements of it. How
does this happen?

Two Paths Diverge
-----------------

I see two separate paths:

-  More formal, and

-  Less formal.

The more formal path includes the kind of curriculum you find at big
CS schools. Formal treatment of algorithms and data structures. Logic
and Computable Functions. The essentials of Turing Completeness.

Books
like http://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs.

The less formal path starts with -- essentially -- random hacking
around, trying to get stuff to work. Some folks argue that a
curriculum of structured exercises isn't "random" hacking around. I
suggest that a curriculum of *structured* exercises can be the formal
path concealed under a patina of hackeriness. On the other hand, a
set of exercises can be successful at training programmers; if it
doesn't follow a formalized structure, it's merely a small step from
random.


[Random doesn't mean "bad;" it means "informal" and "unstructured."]


Some folks learn well in a formal, structured approach. They like
axiomatic definitions of computability, and they can get a grip on
how to map the abstractions of computing to specific languages and
problem domains. They read content
at `http://www.algorist.com <http://www.algorist.com/>`__ and see
applications of principles.


Other folks can be shown the formal background that makes their
random hacking fit into a larger pattern. When shown how some things
fit a larger pattern, they're often happy work in a new context with
an expanded repertoire of data structures and algorithms. They read
content at `http://www.algorist.com <http://www.algorist.com/>`__ and
look for solutions to problems; the formal patterns will emerge
eventually.


Not all folks respond well to having their informal notions
challenged. Some folks have ingrained bad habits and prefer to fight
to the death to avoid change. A sad state of affairs, but remarkably
common. They didn't understand linked lists at some point and
steadfastly refuse to use the java.util.LinkedList class. This is
what software religious wars are about. Some trolls truly and deeply
love an uniformed religious war.

Chickens and Eggs
-----------------


Is this a chicken-and-egg problem?


-   You can't really appreciate the formal foundations until you have
    some hands-on coding experience.

-   You shouldn't dirty your hands with implementation details until
    you have the proper theoretical foundations.

That seems potentially reductionist and uninformative. Or. Perhaps
there is a nugget of truth in this. Perhaps one is actually
foundational.

Eggs, to be specific, show the fresh mutations. The egg comes first
from a chicken-like precursor that's not properly a chicken.

What's that precursor to programming in Python? CS Fundamentals?
Hacking around? I suggest that the way we acquire languages is
important here.

Language Skills
---------------

Software languages are a small step from natural languages. As with
learning natural languages, formal grammar may not be as helpful as
engaging in conversations. Indeed, for natural languages, formal
grammars are an afterthought. They're something we discover about a
corpus. We impose the discovered grammar rules on ourselves (and
others) to be understood in a context of other writing (and
speaking.)

Natural language grammar isn't timeless and immutable. People throw
their hands up in despair at the erosion of grammar and language.
They're -- of course -- just being reactionary. Language evolves. The
loudest complainers are the ones who didn't pay attention for a long
time and suddenly (somehow) realized the don't know what "WTF" means.
LOL.


With an artificial language, the grammar is formalized. It has a
first-class existence in compilers, interpreters and other tools.


However, I think the bits of our brain that assimilate grammar work
best from concrete examples. A formal grammar definition -- while
helpful -- isn't the way to start. I think that a less formal, "try
this" suite of exercises is perhaps the best way to learn to program.


As an author, I'm beholden to my publisher's notions of what sells.
Examples sell. See almost everything from
`Packt <https://www.packtpub.com/>`__. Working examples are solid
gold.


These are not necessarily problems for the reader to tackle and
solve. They're examples to study.

The conundrum with attempting to solve problems is the *attempting*
part. It's hard to set out a list of "solve these problems and master
programming" problems and hope folks get through them. What if they
fail? Clearly, you'd provide answers. In that case, you'd be back at
examples to study. Hmm.

I have intermittent interest in my older `Building Skills in
Python <http://www.itmaybeahack.com/homepage/books/python.html>`__
book. Partly because it's got extensive exercises in each chapter. I
get donations. I get inquiries. The exercises seem to resonate in a
small way.

I've done about 22 levels of the Python Challenge (I'll write about
that separately.) It's not a great way to learn from scratch. You
need to know a lot. And you need a lot of hints.

I've done almost 70 levels of Project Euler. It might be a better way
to learn programming because the easy problems are really easy. No
guesswork. No riddles. No steganography. The answers are totally
cut-and-dried, unambiguous, and absolute. However, there's no easy
guidance for learners. Either you have an answer, and want help on
improving it, or ... well ... you're stuck and frustrated.

Structured Sequence of Exercises
--------------------------------

What strikes me as a possibility here is a structured series of
exercises that lay out the foundations of computer science as
realized in a specific programming language.

Puzzle-style. With extensive hints. Background readings, too. But
with absolutely right answers. And a score-keeping system to show
where you stand.

No tricky riddles. No quizzes to proceed. You could go on to advanced
material without mastering the foundations, if you wanted.

I've got a bunch of exercises and examples in my Building Skills
books. Plus some of the examples in my Packt books can be modified
and repurposed. Plus. Projects like
`HamCalc <https://github.com/slott56/HamCalc-2.1>`__ contain a wealth
of simple applications that can be adjusted to show CS fundamentals.

Perhaps relevant is
this: https://www.google.com/edu/programs/exploring-computational-thinking/.

I'm not sure precisely how it fits, since it seems to be more aimed
at providing a general background, rather than teaching programming
language skills. They decompose the skills into four specific
techniques. Here are specific techniques.

-  Decomposition: Breaking a task or problem into steps or parts.

-  Pattern Recognition: Make predictions and models to test.

-  Pattern Generalization and Abstraction: Discover the laws, or principles that cause these patterns.

-  Algorithm Design: Develop the instructions to solve similar problems and repeat the process.


Perhaps this is
relevant: http://interactivepython.org/courselib/static/pythonds/index.html.
I haven't read this carefully, but it seems to be expository
rather than exploratory.  It's really thorough. It has quizzes and
self-checks.

I think there's a big space for publishing **lots** simple
recreational programming exercises as teaching tools.





