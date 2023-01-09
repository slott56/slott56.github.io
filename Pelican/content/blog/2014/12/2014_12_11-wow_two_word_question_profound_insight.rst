Wow. Two-Word Question. Profound Insight.
=========================================

:date: 2014-12-11 08:00
:tags: #python,functional programming
:slug: 2014_12_11-wow_two_word_question_profound_insight
:category: Technologies
:status: published

I'm working on yet another Python book. This one looking at functional
programming in Python. It doesn't really go with with `Mastering
Object-Oriented
Python <http://www.amazon.com/Mastering-Object-oriented-Community-Experience-Distilled/dp/1783280972>`__
and `Python for Secret
Agents <http://www.amazon.com/Python-Secret-Agents-Steven-Lott/dp/1783980427>`__
because the focus isn't on Python's strong suit.

In chapter one, a reviewer had this two-word question:
"yield from?"

What? What does "yield from" mean?

Oh.

Wow.

https://docs.python.org/3/whatsnew/3.3.html#pep-380-syntax-for-delegating-to-a-subgenerator

I had utterly missed this profound, important feature.

I guess I have been too blasé in skimming the release notes.

That's embarrassing.  And it only took two words to reveal my mistake.
I had to then review all 113 **yield** statements in 72 files of
examples that go with the book.  That means most chapters will get
touched to revise an example to show **yield from iter** instead of the
older **for x in iter: yield x** template.

This also changes the Tail Call Optimization material. The explicit for
was actually kind of nice for showing how TCO is implemented in Python.
The yield from makes it a little less clear.

Some reviewers consider TCO so fundamental that it belongs in chapter 1.
The omission of detailed analysis of Python's TCO approach was
considered a significant flaw. Other reviewers seemed happy setting
discussion of TCO aside for later.

**The Functional Python Conundrum**


This book is going to be difficult. The ratings from the reviewers were
low. Really low. It looks like I've got a lot of work to do. Finding the
target audience will be difficult.

One reviewer asked -- in effect -- why would someone who knew functional
LISP ever use Python? I don't think there's a big audience of
disgruntled LISP programmers, so that's not a relevant question.

Viewed from the other direction, it's hugely import. Why would a Python
programmer adopt functional design patterns? That's the question that
needs to be answered clearly.

And from the reviews of chapter 1, it wasn't addressed clearly enough.





