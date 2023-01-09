On the uselessness of Enum -- wait, what?
=========================================

:date: 2019-02-12 08:00
:tags: Design Principles,architecture
:slug: 2019_02_12-on_the_uselessness_of_enum_wait_what
:category: Technologies
:status: published

Had a question about an enumerated set of constant values.
"Where do I put these constants?" they asked. It was clear what they
wanted. This is another variation on their personal quest which can be
called "I want Python to have CONST or Final." It's kind of tedious when
a person asks -- repeatedly -- for a feature that's not present in the
form they want it.
"Use Enum," I said.
"Nah," they replied. "It's Yet Another Abstraction."
Wait, what?
This is what I learned from rest of their nonsensical response: There's
an absolute upper bound on abstractions, and Enum is one abstraction too
many. Go ahead count them. This is too many.
Or.
They simply rejected the entire idea of learning something new. They
wanted CONST or Final or some such. And until I provide it, Python is
garbage because it doesn't have constants. (They're the kind of person
that needs to see CONST minutes_per_hour = 60 in every program. When I
ask why they don't also insist on seeing CONST one = 1 they seem shocked
I would be so flippant.)
YAA. Seriously. Too many layers.
As if all of computing wasn't a stack of abstractions on top of stateful
electronic circuits.



-----

No one can argue w/ all of computing is a stack of...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2019-02-13 10:21:59.471000-05:00

No one can argue w/ all of computing is a stack of abstractions.
The question is, for a particular use case; what is the appropriate
level of abstraction?
People can examine articles like "How much abstraction is too much?" at
StackOverFlow to obtain guidance on the appropriate level of
abstraction.
https://stackoverflow.com/questions/2668355/how-much-abstraction-is-too-much





