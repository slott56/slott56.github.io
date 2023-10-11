The Debugger
===============================================

:date: 2023-10-10 18:21
:tags: python,games,tutorial
:slug: 2023-10-10-the_debugger
:category: Python
:status: published

See `Python 3.12: what didn't make the headlines <https://www.bitecode.dev/p/python-312-what-didnt-make-the-headlines>`_. This is **very** helpful.

It is a great list of 7 key features of Python 3.12.

With one tiny point I need to object to.

I don't like debuggers
-------------------------

This is a strongly-held position.

**Debuggers are harmful.**

I say this because I have had the misfortune to help more than one programmer
who could not actually describe the semantics of the code.

They couldn't draw a picture. Write a sentence. Nothing.

They could only point at the interactive debugger session with hapless flailing, and "see, it should work"
kind of noises.

This is emphatically **bad**.

Every time I would ask them to step away from the debugger and describe -- maybe on a whiteboard --
what the heck they thought was going on.

I could go on with horror stories of bad debugging.

I use debuggers
---------------

Back when C++ was my "stock-in-trade", I used the debugger.

Rarely.

And then, mostly, on core dump files to figure out where the program failed.

And to look at a few key variables to confirm the state of the computation.

Then.

I went back to the source, and looked for a logic path that lead to the wrong state.
It wasn't often hard to find.
And it didn't involve using the debugger for much more than finding the
call frame, stack contents, and local variables.

What set me off
---------------

This:

    ...it's also removing a big "WTF" that all beginners will experience using the Python debugger with nobody in sight to explain to them what's going on.

I think there are no circumstances under which beginners should be using the debugger.

I think there are no circumstances under which anyone should use a debugger before they already know
what's supposed to be going on.

The idea of "beginners" being surprised at the structure of stackframes is an oxymoron.

    Beginners don't know about stack frames.

More-or-less, this is one definition of "beginner".

People who know about stack frames aren't beginners and can be trusted to understand the debugger.

The points in the blog posts are sound: better debugging, additional support for evaluating expressions.

The "audience of beginners" is my only quibble.
