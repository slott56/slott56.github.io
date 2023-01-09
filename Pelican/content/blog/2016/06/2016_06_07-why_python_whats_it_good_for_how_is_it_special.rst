Why Python? What's it good for? How is it special?
==================================================

:date: 2016-06-07 19:00
:tags: #python
:slug: 2016_06_07-why_python_whats_it_good_for_how_is_it_special
:category: Technologies
:status: published

First. The question is moot. It's a programming language. It's good for
programming.
When I push back, folks try to produce languages which exist only in
certain pigeon holes.
"You know. PHP is for web and JavaScript runs in the browser. What's
Python for?"
The PHP and JavaScript examples aren't helpful. That doesn't narrow the
domain of problems for which Python is appropriate. It only shows that
some languages have narrow domains.
"You know. Objective-C and Swift are for iOS. What's the predominant
place Python is used?"
Python also runs on iOS. I don't know if it has suitable bindings for
building apps. If it does, that doesn't change my answer. It's good for
programming.
"Java is used mainly for web apps, right? What about Python?"
Okay. At this point, the question has slipped from moot to ignorant.
Can we just set that aside? Can we move on?
If you want some useful insight, start here:
http://web.eecs.umich.edu/~bchandra/courses/papers/Wirth_Design.pdf
Yes, it's an essay from 1974.  Parts of it are a little old-fashioned,
but a lot of it is still rock-solid. For example, the idea of
strongly-typed pointers is considered more-or-less standard now. It was
debatable then. And Wirth's opinion continues to drive language design.
Page 28 has the key points: features of a programming language.
Enumerated by the inventor of Pascal, Modula, Oberon, and other
languages too numerous to recall.
Some of the list is a little dated. "...different character sets...,"
for example, has been superseded by Unicode.
Also, the list is focused on compiled languages. Python is a dynamic
language. It's interpreted. Yes, there's a compiler, but that's mostly
an optimization of the source code. If you replace "compiler" with
"run-time", the list stands up as a description of good languages.
I like this list because it helps characterize why Python works out so
well. And why many other languages are also pretty good. It points up
the reason why quirky languages like JavaScript (or even Ruby) are
suspicious. Some of the points about efficiency are important topics for
further discussion.
I often have to remind folks who work with Big Data that most of our
processing is I/O bound. Python waits for the database somewhat more
efficiently than Java. Why does Python wait more efficiently? Because it
uses less memory. Sometimes this is a win.
Let's not ask silly questions about a general-purpose language. Instead,
let's benchmark solutions, and compare tangible performance numbers
using real code.



-----

Thank you for sharing your thoughts and knowledge ...
-----------------------------------------------------

Nina Athena<noreply@blogger.com>

2019-05-29 00:23:12.207000-04:00

Thank you for sharing your thoughts and knowledge on this topic. This is
really helpful and informative, as this gave me more insight to create
more ideas and solutions for my plan. I would love to see more updates
from you.
`Web Development
Services <https://yourwebsitefirst.com/features-4-tips-avoid-scope-creep-web-development-project/>`__





