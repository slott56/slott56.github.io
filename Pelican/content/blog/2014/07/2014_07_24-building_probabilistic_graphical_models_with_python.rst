Building Probabilistic Graphical Models with Python
===================================================

:date: 2014-07-24 08:00
:tags: #python,Data Science,numpy,scipy
:slug: 2014_07_24-building_probabilistic_graphical_models_with_python
:category: Technologies
:status: published

A deep dive into probability and
scipy: https://www.packtpub.com/building-probabilistic-graphical-models-with-python/book
I have to admit up front that this book is out of my league.
The Python is sensible to me. The subject matter -- graph models,
learning and inference -- is above my pay grade.

**Asking About a Book**

Let me summarize before diving into details.

Asking someone else if a book is useful is really not going to reveal
much. Their background is not my background. They found it
helpful/confusing/incomplete/boring isn't really going to indicate
anything about how I'll find it.

Asking someone else for a vague, unmeasurable judgement like "useful" or
"appropriate" or "helpful" is silly. Someone else's opinions won't apply
to you.

Asking if a book is technically correct is more measurable. However. Any
competent publisher has a thorough pipeline of editing. It involves at
least three steps: Acceptance, Technical Review, and a Final Review. At
least three. A good publisher will have multiple technical reviewers.
All of this is detailed in the front matter of the book.

Asking someone else if the book was technically correct is like asking
if it was reviewed: a silly question. The details of the review process
are part of the book. Just check the front matter online before you buy.
It doesn't make sense to ask judgement questions. It doesn't make sense
to ask questions answered in the front matter. What can you ask that
might be helpful?

I think you might be able to ask completeness questions. "What's omitted
from the tutorial?" "What advanced math is assumed?" These are things
that can be featured in online reviews.

Sadly, these are not questions I get asked.

**Irrational Questions**

A colleague had some questions about the book named above. Some of
which were irrational. I'll try to tackle the rational questions since
emphasis my point on ways **not** to ask questions about books.


**2.  Is the Python code good at solidifying the mathematical concepts?**

This is a definite maybe situation. The concept of "solidifying" as
expressed here bothers me a lot.

Solid mathematics -- to me -- means solid mathematics. Outside **any**
code considerations. I failed a math course in college because I tried
to convert everything to algorithms and did not get the math part. A
kindly professor explained that "F" very, very clearly. A life lesson.
The math exists outside any implementation.

I don't think code can ever "solidify" the mathematics. It goes the
other way: the code must properly implement the mathematical concepts.
The book depends on scipy, and scipy is a really good implementation of
a great deal of advanced math. The implementation of the math sits
squarely on the rock-solid foundation of scipy. For me, that's a ringing
endorsement of the approach.

If the book reinvented the algorithms available in scipy, that would be
reason for concern. The book doesn't reinvent that wheel: it uses scipy
to solve problems.

**4. Can the code be used to build prototypes?**

Um. What? What does the word prototype mean in that question? If we use
the usual sense of software prototype, the answer is a trivial "Yes."
The examples are prototypes in that sense. That can't be what the
question means.

In this context the word might mean "model". Or it might mean "prototype
of a model". If we reexamine the question with those other senses of
prototype, we might have an answer that's not trivially "yes." Might.
When they ask about prototype, could they mean "model?" The code in the
book **is** a series of models of different kinds of learning. The
models are complete, consistent, and work. That can't be what they're
asking.

Could they mean "prototype of a model?" It's possible that we're talking
about using the book to build a prototype of a model. For example, we
might have a large and complex problem with several more degrees of
freedom than the text book examples. In this case, perhaps we might want
to simplify the complex problem to make it more like one of the text
book problems. Then we could use Python to solve that simplified problem
as a prototype for building a final model which is appropriate for the
larger problem.

In this sense of prototype, the answer remains "What?"  Clearly, the
book solves a number of simplified problems and provides code samples
that can be expanded and modified to solve larger and more complex
problems.

To get past the trivial "yes" for this question, we can try to examine
this in a negative sense. What kind of thing is the book **unsuitable**
for? It's unsuitable as a final implementation of anything but the six
problems it tackles. It can't be that "prototype" means "final
implementation." The book is unsuitable as a tutorial on Python. It's
not possible this is what "prototype" means.

Almost any semantics we assign to "prototype" lead to an answer of
"yes". The book is suitable for helping someone build a lot of things.

**Summary**

Those two were the **rational** questions. The irrational questions made
even less sense.

Including the other irrational questions, it appears that the real
question might have been this.

Q: "Can I learn Python from this book?"

A: No.

It's possible that the real question was this:

Q: "Can I learn advanced probabilistic modeling with this book?"

A: Above my pay grade. I'm not sure I could learn probabilistic modeling
from this book. Maybe I could. But I don't think that I have the depth
required.

It's possible that the real questions was this:

Q: Can I learn both Python and advanced probabilistic modeling with this
book?"

A: Still No.

**Gaps In The Book**

Here's what I could say about the book.

You won't learn much Python from this book. It assumes Python; it
doesn't tutor Python. Indeed, it assumes some working scipy knowledge
and a scipy installation. It doesn't include a quick-start tutorial on
scipy or any of that other hand-holding.

This is not even a quibble with the presentation. It's just an
observation: the examples are all written in Python 2. Small changes are
required for Python 3. Scipy will work with Python 3.

http://www.scipy.org/scipylib/faq.html#do-numpy-and-scipy-support-python-3-x.

Reworking the examples seems to involve only small changes to replace
print statements. In that respect, the presentation is excellent.





