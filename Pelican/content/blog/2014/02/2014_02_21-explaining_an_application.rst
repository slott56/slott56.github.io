Explaining an Application
=========================

:date: 2014-02-21 10:56
:tags: unit testing,test-driven reverse engineering,legacy code
:slug: 2014_02_21-explaining_an_application
:category: Architecture & Design
:status: published

Some years ago--never mind how long precisely--having little or no money
in my purse...  I had a great chance to do some Test-Driven Reverse
Engineering on a rather complex C program. I extracted test cases. I
worked with the users to gather test cases. And I rewrote their legacy
app using Test-Driven Development. The legacy C code was more a hint
than anything else.
I thought it went well. We uncovered some issues in the test cases.
Uncovered a known issue in the legacy program. And added new features.
All very nice. A solid success.
Years later, a developer from the organization had to make some more
changes.
The client calls.
"No problem," I assure them, "I'm happy to answer any questions. With
one provision. Questions have to be about specific code. I can't do
'overview' questions. Email me the code snippet and the question."
I never heard another word.  No question of any kind. Not a general
question (that I find difficult to answer,) nor a specific question.
Why the provision?
I find it very hard to talk with someone who hasn't actually read the
code yet. I have done far too many presentations to people who are
sitting around a conference room table, nodding and looking at
power-point slides.
I know the initial phone call focused on "an overview." But what counts
as an overview? Use cases? Data model? Architectural layers? Test cases?
Rather than waste time explaining something irrelevant, I figured if
they asked anything -- anything at all -- I could focus on what they
really wanted to know.
I know that I have never been able to understand people hand-waving at a
picture of code. I have to actually read the code to see what the
modules, classes and functions are and how they seem to work. I'm
suspicious of graphics and diagrams.  I know that I can't read the code
while someone is talking. If they insist on talking, I need to read the
code in advance.
Perhaps I'm imposing too much on this customer. But. They're going to
maintain the code -- that seems to mean they need to understand it. And
they need to understand it their own way, without my babbling randomly
about the bits that interested me. Maybe the part I found confusing is
obvious to them, and doesn't bear repeating.
Perhaps raising the bar to "specific questions about specific code"
forced them to read enough. Perhaps after some reading, they realized
they didn't need to pay me to explain things. I certainly can't brag
that the code explained itself.
Or. Perhaps they realized how the unit tests worked and realized that
TestCases provide a roadmap of the API.





