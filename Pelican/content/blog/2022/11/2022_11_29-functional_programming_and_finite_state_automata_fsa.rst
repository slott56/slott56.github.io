Functional Programming and Finite State Automata (FSA)
======================================================

:date: 2022-11-29 11:00
:tags: functional python programming,design,#python
:slug: 2022_11_29-functional_programming_and_finite_state_automata_fsa
:category: Technologies
:status: published

When I talk about functional programming in Python, folks like to look
for place where functional programming isn't appropriate. They latch
onto finite-state automata (FSA) because "state" of an automata doesn't
seem to fit with stateless objects used in functional programming.

This is a false dichotomy.

It's emphatically false in Python, where we don't have a purely
functional language.

(In a purely functional language, monads can help make FSA's behave
properly and avoid optimization. The use of a recursion to consume an
iterable and make state transitions is sometimes hard to visualize. We
don't have these constraints.)

Let's look at a trivial kind of FSA: the parity computation. We want to
know how many 1-bits are in a given value. Step 1 is to expand an
integer into bits.

::

   def bits(n: int) -> Iterable[int]:
       if n < 0:
           raise ValueError(f"{n} must be >= 0")
       while n > 0:
           n, bit = divmod(n, 2)
           yield bit

This will transform a number into a sequence of bits. (They're in order
from LSB to MSB, which is the reverse order of the ``bin()`` function.)

::

   >>> list(bits(42))
   [0, 1, 0, 1, 0, 1]

Given a sequence of bits, is there an odd number or an even number? This
is the parity question. The parity FSA is often depicted like this:



.. image:: {static}/media/FSA_image.png
   :width: 320px
   :height: 188px
   :target: {static}/media/FSA_image.png
   :alt:   two-state finite-state automaton



When the parity is in the **even** state, a 1-bit transitions to the
**odd** state. When the parity is in the **odd**, a 1-bit transitions to
the **even** state.

Clearly, this demands the **State** design pattern, right?

An OO Implementation
--------------------

Here's a detailed OO implementation using the **State** design pattern.

::

    
   class Parity:
       def signal(self, bit: int) -> "Parity":
           ...


   class EvenParity(Parity):
       def signal(self, bit: int) -> Parity:
           if bit % 2 == 1:
               return OddParity()
           else:
               return self


   class OddParity(Parity):
       def signal(self, bit: int) -> Parity:
           if bit % 2 == 1:
               return EvenParity()
           else:
               return self


   class ParityCheck:
       def __init__(self):
           self.parity = EvenParity()

       def check(self, message: Iterable[int]) -> None:
           for bit in message:
               self.parity = self.parity.signal(bit)

       @property
       def even_parity(self) -> bool:
           return isinstance(self.parity, EvenParity)

Each of the ``Parity`` subclasses implements one of the states of the
FSA. The lonely ``signal()`` method implements state-specific behavior.
In this case, it's a transition to another state. In more complex
examples it may involve side-effects like updating a mutable data
structure to log progress.

This mapping from state to diagram to class is pretty pleasant. Folks
really like to implement each state as a distinct class. It somehow
feels really solid.

It's import to note the loneliness of the lonely ``signal()`` method.
It's all by itself in that big, empty class.

Hint. This could be a function.

It's also important to note that this kind of design is subject to odd,
unpleasant design tweaks. Ideally, the transition is \*only\* done by
the lonely ``signal()`` method. Nothing stops the unscrupulous
programmer from putting state transitions in other methods. Sigh.

We'll look at more complex kinds of state transitions later. In the UML
state chart diagrams sates may also have entry actions and exit actions,
a bit more complex behavior than we we're showing in this example.

A Functional Implementation
---------------------------

What's the alternative? Instead of modeling state as an object with
methods for behavior, we can model state as a function. The state is a
function that transitions to the next state.

::

   def even(bit: int) -> ParityF:
       if bit % 2 == 1:
           return odd
       else:
           return even


   def odd(bit: int) -> ParityF:
       if bit % 2 == 1:
           return even
       else:
           return odd


   def parity_check(message: Iterable[int], init: ParityF = None) -> ParityF:
       parity = init or even
       for bit in message:
           parity = parity(bit)
       return parity


   def even_parity(p: ParityF) -> bool:
       return p is even

Each state is modeled by a function.

The ``parity_check()`` function examines each bit, and applies the
current state function (either ``even()`` or ``odd()``) to compute the
next state, and save this as the vakue of the ``parity`` variable.

What's the ParityF type? This:

::

   from typing import Protocol


   class ParityF(Protocol):
       def __call__(self, bit: int) -> "ParityF":
           ...

This uses a Protocol to define a type with a recursive cycle in it. It
would be more fun to use something like
``ParityF = Callable[[int], "ParityF"]``, but that's not (yet)
supported.

Some Extensions
---------------

What if we need each state to have more attributes?

Python functions have attributes. Like this: ``even.some_value = 2``;
``odd.some_value = 1``. We can add all the attributes we require.

What about other functions that happen on entry to a state or exit from
a state? This is trickier. My preference is to use a class as a
namespace that contains a number of related functions.

::

   class Even:
       @staticmethod
       def __call__(bit: int) -> ParityF:
           if bit % 2 == 1:
               odd.enter()
               return odd
           else:
               return even
       @staticmethod
       def enter() -> None:
           print("even")

   even = Even()

This seems to work out well, and keeps each state-specific material in a
single namespace. It uses static methods to follow the same design
principle as the previous example -- these are pure functions, collected
into the class only to provide a namespace so we can use ``odd.enter()``
or ``even.enter()``.

TL;DR
-----

The **State** design pattern isn't *required* to implement a FSA.


