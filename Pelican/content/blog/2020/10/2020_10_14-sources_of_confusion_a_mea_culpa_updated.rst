Sources of Confusion: a "mea culpa" [Updated]
=============================================

:date: 2020-10-14 08:45
:tags: #python
:slug: 2020_10_14-sources_of_confusion_a_mea_culpa_updated
:category: Technologies
:status: published

I am not patient. I have been dismissed as one who does not suffer
fools gladly.

This is a bad attitude, and I absolutely suffer from it. No denials
here. I'm aware it limits my ability to help the deeply confused.

My personal failing is not being patient enough to discover the root
cause of their confusion.

It's not that I don't care -- I would truly like to help them. It's that
I can't keep my mouth shut while they explain their ridiculous chain of
invalid assumptions as if things they invented have some tangible
reality.

I'm old, and I'm not planning on becoming more empathetic. Instead, I've
become less curious about wrong ideas. I find silence is helpful because
I don't yell at them as much as I could.

Recently someone tried to tell me that a Python tuple wasn't
**really** immutable.

Yes.

That's what they said.

A tuple of lists has lists that **can** be modified. (They did not have
the courtesy to provide examples, I've had to add examples based I what
I **assume** they're talking about.)

::

   >>> t = ([], [], [])
   >>> t[0].append(42)
   >>> t
   ([42]. [], [])

"See," they said. "Mutable."

Implicit follow-up: Python is a web of lies and there's no reason for it
to be better than a spreadsheet.

I did not ask how the immutability of a tuple was magically transferred
to the lists contained within the tuple.

I did not ask about their infections disease theory of protocol
transformation of types. Somehow, when associated with a tuple, the list
became tuple-like, and lost a bunch of methods.

I did not ask if they thought there was some some method-shedding
feature where an immutable structure forces other data structures to
shed methods.

I did not ask what was supposed to happen to a dictionary, where there's
no built-in frozen dictionary.

I did not ask what would happen with a "custom" class (one created in
the app, not a built-in collection.)

I did not ask what fantasy land they come from where a tuple of mutable
objects would lead to immutability of the contained objects.

I did not ask if it worked the other way, too: was a list of tuples also
supposed to freeze up?

I did not ask if it transferred more than one level deep into the lists
inside the tuple.

I should have.

It was an epic failing on my part to not dig into the bizzaro world
where the question could arise.

BTW. They had the same complaint about frozen data classes. (Again. They
did not have the courtesy to provide code. I'm guessing this is what
they meant. My failure for not asking.)

::

   >>> from typing import List
   >>> from dataclasses import dataclass
   >>> @dataclass(frozen=True)
   ... class Kidding_Right:
   ...     one_thing: List[int]
   ...     another_thing: List[int]
   ... 
   >>> kr = Kidding_Right([], [])
   >>> kr.one_thing.append(42)
   >>> kr
   Kidding_Right(one_thing=[42], another_thing=[])

Triumphant Sneer: "See, frozen is little more than a suggestion. The
lists within the data class are \*not\* frozen."

Yes. They appeared to be claiming frozen was supposed to apply
transitively to the objects within the dataclass.  Appeared. My mistake
was failing to ask what they hell they were talking about.

I really couldn't bear to know what caused someone to think this was in
any way "confusing" or required "clarification." I didn't want to hear
about transitivity and how the data class properties were supposed to
infect the underlying objects.

Their notion was essentially wrong, and wickedly so. I could have asked,
but I'm not sure I could have waited patiently through their answer.

**Update**.

"little more than a suggestion".

Ah.

This is an strange confusion.

A dynamic language (like Python) resolves everything at run-time. It
turns out that there are ways to override \__getattr__() and
\__setattr__() to break the frozen setting. Indeed, you can reach into
the internal \__dict_\_ object and do real damage to the object.

I guess the consequences of a dynamic language can be confusing if you
aren't expecting a dynamic language to actually be dynamic.



-----

&quot;I guess the consequences of a dynamic langua...
-----------------------------------------------------

McSee<noreply@blogger.com>

2020-10-20 21:55:24.002000-04:00

"I guess the consequences of a dynamic language can be confusing if you
aren't expecting a dynamic language to actually be dynamic."
Exactly. You were TOO patient


It might help people if they read the following Py...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2020-10-16 16:05:57.573000-04:00

It might help people if they read the following Python documentation
https://docs.python.org/3/reference/executionmodel.html#interaction-with-dynamic-features





