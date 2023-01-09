On One Aspect of Design Patterns -- Flexibility
===============================================

:date: 2016-09-13 08:00
:tags: design,mastering object-oriented python
:slug: 2016_09_13-on_one_aspect_of_design_patterns_flexibility
:category: Technologies
:status: published

Something I forget to think about is the degree of detail or
granularity of design patterns.  I have my own viewpoint and I often
assume that others share it.

Here's a quote from an email describing the PLoP (Pattern Languages of
Programs) patterns as quite distinct from the Gang of Four (*Design
Patterns: Elements of Reusable Object-Oriented Software*) patterns.

    In the main, the PLoP patterns are less granular than the persnickety
    GoF
    "Design Patterns." (Classic GoF, in part, static type binding
    work-arounds. And
    you need to talk about a "facade" pattern? Really? Although see
    Fowler's at it
    again, coining a ™ term - "fluent API" - for Some Not Egregiously
    Stupid
    Practice, to feed to the credulous who have never reflected on what
    they are doing.)

Cutting through the editorializing, the author is describing two
families.

-  GoF patterns that are essentially ways to cope with static type checking in Java and C++.

-  PLoP patterns which are a little more generic and more widely applicable.

More...

    "Plug-in Pattern" is a nice example. Enumerates the stuff you kinda
    know, with
    qualities / attributes of its proposal, plus application samples /
    outcomes of
    applying the pattern. The claims to relevance throughout are
    reminiscent of the
    investigation behind Parnas' "Criteria for Decomposing Systems into
    Modules."


My habit is to assume this is pretty widely known. I assume everyone
has wrestled with design patterns large and small and found that some
of the GoF apply to Python, but the implementation details will
differ. Dramatically.


Look at the **Singleton** design pattern, for example. The concept is
profound. There are times when we want stateful, global,
**Singleton** instances. The Java or C++ technique of a small factory
method which returns the one-and-only instance (or creates the
one-and-only instance in the rare edge case) is extremely strange in
Python. We can implement it. But why?


Module objects in Python are stateful singletons. Rather than invent
a **Singleton** class, we can -- trivially -- just use a module. And
we're done. Problem solved. No Code Written.


The email served as a reminder that sometimes people aren't quite so
flexible in their understanding of design patterns. I need to cut
them some slack and guide them to seeing that there's wiggle room
there. The email reminds me that some people feel compelled to either
follow the GoF prescription or discard the GoF entirely. The reminder
about PLoP and other pattern languages is a helpful reminder to be
more flexible.


The point here is that patterns are a concept. Not a law.




