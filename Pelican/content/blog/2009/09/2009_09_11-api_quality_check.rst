API Quality Check
=================

:date: 2009-09-11 20:14
:tags: API Design
:slug: 2009_09_11-api_quality_check
:category: Technologies
:status: published

A recent request for an API quality check sent me into a paroxysm.

The request seemed simple enough. They had two varieties of API
design: varietal **M** had a lot of methods, each with relatively few
parameters. Varietal **P** had a few methods, but each had a
boat-load of parameters.

There had been some "reading" on API design and questions were
raised. They wanted me to weigh in, telling them that style **M** was
"better" than style **P**. [It is, but that's not the point.]

I was shocked speechless.

I find it incredible that anyone could even need coaching in API
design. Much less find Tulach's
`book <http://books.google.com/books?id=DXYZZVlWOAkC&lpg=PA5&ots=A2FZsDiv0f&dq=art%20of%20api%20design&pg=PA5#v=onepage&q=art%20of%20api%20design&f=false>`__
and still be unable to apply the principles.

Here's what bugged me.

If they were coding in any sensible language, they should have
mountains of API examples all around them. Java has a huge standard
library. C# has the entire .Net framework. Python has a vast library.
All of these are tremendous, well-designed, carefully crafted
examples of API's.

**API's Everywhere**

As far as I can see, the world is fat with API examples. Everywhere
you look, every vendor, every product, everything has an API.

It just shouldn't be rocket science to compare your API against the
established standard for the language in which you're working.

Somehow it was possible for several programmers to be completely
unable to find any examples of API design.

I can only assume that they are living in a time-warp; none of them
have ever connected to the Internet or seen any code but their own.
Perhaps the only API they could think of was JDBC. Or perhaps they
were all Visual Basic or PL/SQL programmers and didn't see much
open-source code. Or perhaps they had some really obscure language
where no one posts any open source API's.

**What To Do?**

My direct advice was to read Tulach and create a big spreadsheet
ranking their code against each principle that Tulach provides.

After thinking about it, I realize I should have asked what API's
they were currently using and how their proposed new code stacked up
against the existing language and framework they already had.





