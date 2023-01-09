"Hard Coding" Business Rules
============================

:date: 2011-10-05 06:42
:tags: #python,business rules
:slug: 2011_10_05-hard_coding_business_rules
:category: Technologies
:status: published

See this: "`Stop hard-coding business
rules <http://www.sdtimes.com/STOP_HARD_CODING_BUSINESS_RULES/By_David_Rubinstein/About_BUSINESSDEVELOPERS_and_BUSINESSRULES/35919>`__"
in SD Times.
Here's what's exasperating: "Memo to developers: Stop hard-coding
business rules into applications. Use business rules engines instead."
Business Rules Engines?  You mean Python?
It appears that they don't mean Python.
"Developers can use [a BPM suite or rules engine] and be more
productive, so long as they don’t use C# or Java as a default for
development".
I'm guessing that by "C# or Java" they mean "a programming language" and
I would bet that Python is included in "bad" languages for development.
Python has all the simplicity and expressive power of a Domain-Specific
Language (DSL) for business rules.
Don't hard-code business rules in Java.  Code them in an interpreted
language like Python.
Also, don't be mislead by any claims that business analysts or (weirdly)
users can somehow "code" business rules.  They can't (and mostly, they
won't).  That's what SD Times wisely says "Developers".  That's how
coding gets done.



-----

The underlying point about reducing the friction o...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2011-10-04 12:01:17.299000-04:00

The underlying point about reducing the friction of change management
and moving towards more of a self-service mentality for business users
is actually a valid one.
Python is Turing complete - to really use it to its full power, you need
to be able to think algorithmically and in terms of data structures.
The key purpose of a business rules engine is to provide a constrained
environment for \*non\* developers to make changes to business logic
directly. Just as the data in an application has traditionally been the
domain of the business users rather than the developers, a rules engine
aims to put some of the \*logic\* in their hands as well (with
appropriate access controls, of course, again, just like data).
It's similar to the reason why JSON or ini-style config files are a
better idea than using Python for the same thing: you \*don't want\*
that level of expressiveness in your configuration settings, you want
things to be explicit rather than algorithmically generated.


So it&#39;s not the language, but the change deplo...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-10-07 15:31:41.731000-04:00

So it's not the language, but the change deployment mechanism? Since
it's interpreted it doesn't need a compiled binary to be shipped? But it
still needs a testing cycle, right? Seems to me, many languages could
work (even compiled ones, since you can compile and load a .NET CLR
assembly at runtime). Obviously some languages might be more suitable
than others in expressiveness and simplicity, but how do you measure
that? How important is the readability of a traditional language like
VB.NET versus something more declarative yet opaque (i.e. requires more
experience) like XSLT, SQL or Scheme? If users can't program business
rules, what level of developers should?


&quot;constrained environment for *non* developers...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2011-10-04 18:59:42.317000-04:00

"constrained environment for \*non\* developers"
The "constrained environment" may or may not work depending on the
client. Personally, I have seen people become infuriated by limitations
and started using Access/Excel.
At a certain Vanguard location, they first generate reports w/
Access/Excel to explore/document the business rules. Once it's stable
(ie they have figured out what they really want), then it gets
incorporated into their infrastructure via a programming language.





