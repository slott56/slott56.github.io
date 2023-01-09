The Royal Road
==============

:date: 2016-12-20 08:00
:tags: pandas,learning,#python
:slug: 2016_12_20-the_royal_road
:category: Technologies
:status: published

Warning: Long Boring Anecdote: Conclusions will be drawn from a single example.

First, this quote:

   "All your suggestions were great if I had wanted to do a systematic
   study and truly understand. The goal is to understand and learn as
   little as possible to be able to undertake the code challenge for [a
   specific job opportunity]."

The subject of systematic study is Python. The focus of learn as
little as possible is Pandas.

The goal is more-or-less impossible. Focus on a specific code
challenge will devolve into other aspects of the language. Or. It will
lead nowhere.

Also. I'm not **sure** what a "systematic study" is. From the omitted
back-story, I'm seems clear to me that the advice to "read a tutorial"
is restated here as "systematic study." And is unacceptable. I guess
because of time constraints.

It gets better.

There's this:

   "For now, I am just going to follow the pattern and get stuff to
   work."


This is the ideal way to be defeated by technology. The "pattern" is
defined to a large degree by the programming language. The two are
inextricably linked. Trying to identify a pattern in programming
that's magically not part of the implementation language seems
deranged.

Learning Pandas isn't simple. There's no royal road.

The real crux are several questions that are difficult to reproduce,
so I'm forced to summarize.

-  What does name.name().name().name() mean? How can you call multiple
   methods "simultaneously"?

-  What is the range of values for some parameter?


And the capper.

-  I understand object.method().method().  I cannot understand
   object.name -- how can a method have no ()'s?


I'm sorry, but, the advice still stands. These are not questions that
can be answered in a vacuum. This is serious -- and foundational --
object-oriented programming. Each of these small things was a total
show-stopper, leading to four emails merely to clarify the question.
Then more when the answer was rejected as not consistent with
something, or astonishing, or


For the name.name().name(), the answer "Google Fluent Interface" was
too complex. Code examples were requested to show how it was possible
for an object to return another object that had methods.


Advice to use Python's >>> prompt and the dir() function were
apparently part of "systematic study" and not part of "learn as
little as possible."


For the range of values of a parameter, the answer "read the source"
was a non-starter. Reading the source was flat-out rejected as not
making any sense. I finally had to actually provide the link to the
source repo for Pandas before it became clear what "open source" even
meant. This was found to be nothing short of astonishing. The
side-bar conversation on "how is this even possible?" was confusing
to me because -- sadly -- I assumed people knew that the words "open"
and "source" together meant that the source was open for inspection.
My assumption was wrong. At least one person did not know this. That
means there are others.


Finally. For the "capper" question. The exchange really did include
this: "The dot notation I thought was Object.Method.Method."


A great deal of the back-and-forth amounted to "I reject anything
other than fluent methods because that's the only thing I've decided
to understand." Words like "property" and "attribute" were ignored as
noise, AFAIK.


I say "amounted to" because a lot of the back-and-forth was restating
the question. Other parts were exchanging links to the Pandas
documentation in an effort to follow the "learn as little as
possible" strategy. Any link to a tutorial would be "systematic
study". Any link to Pandas, however, was acceptable. But (of course)
confusing because the Pandas documentation assumes a modicum of
language knowledge.


Here's what appears to be the problem: it's impossible to learn a
complex tool like Pandas without starting with a basic understanding
of Python.


I don't think I've ever seen it suggested that one can leap into a
package without knowing the language. I'm not sure how one can
develop the idea of learning as little as possible in the first
place. But, there it is.


There's at least one person who thinks they can learn as little as
possible and still get Pandas code to work. That likely means there
are others.


It appears there's a market for books like


-   *Learn as little Python as possible to be able to use Pandas*

-   *Learn the least Java necessary to make Spark work*

-   *The Royal Road to Data Science*


I'm not sure I'm capable of writing books like these, but for someone
who does, it might be a really lucrative line of books.





