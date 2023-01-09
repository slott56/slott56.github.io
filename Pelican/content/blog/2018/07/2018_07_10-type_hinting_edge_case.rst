Type Hinting Edge Case
======================

:date: 2018-07-10 08:22
:tags: #python,type hints
:slug: 2018_07_10-type_hinting_edge_case
:category: Technologies
:status: published


Warning. I'm new to this. Yes, my book Functional Python Programming
-- 2nd ed -- is full of type hints. But my examples are all
(intentionally) *relatively* simple. There are edge cases that I do
not pretend to understand.

Here's a fun one. Start here
   
    Lazy PyTwitter: Is there some way with typing/mypy to express that
    a type must be a 3-element numpy array of reals?

    — David Beazley (@dabeaz) `June 21,
    2018 <https://twitter.com/dabeaz/status/1009772982741266432?ref_src=twsrc%5Etfw>`__


This is a cool question.

Here's an essential clarification on what this structure is.


    Sorry, but I'm not letting go of this. Suppose I write a function:
    def vec3(x:float, y:float, z:float):
    return numpy.array((x,y,z))
    I now use this to make "instances" of 3D vectors, which get passed
    around and used throughout my code.
    How would I type hint all of that?

    — David Beazley (@dabeaz) `June 22,
    2018 <https://twitter.com/dabeaz/status/1010112644819439616?ref_src=twsrc%5Etfw>`__



This is tricky and I think there are two reasons why it's hard.

1.  We want to specify some details internal to instances of the
    np.array class.

2.  We want to provide a size constraint, something that I don't think
    typing can do.

The size constraint may be handled by using Tuple, but it doesn't
really fit in a general way. This three-tuple is Tuple[float, float,
float]. You can see how that rapidly gets hideous for higher-dimension
objects. You'd want Tuple[float*3], right?

The internal constraint, similarly, is challenging. However. An
np.array() -- for the most part -- is a Sequence with extra features.

I have a suggestion.

1.  A stubs/numpy.py file with this. I think this characterizes the
    array structure.

    ::

       from typing import TypeVar, Sequence

       _Base = TypeVar("_Base")

       def array(*args: Sequence[_Base]) -> Sequence[_Base]: ...




2.  Here's the target function.

    ::

       import numpy as np
       from typing import Sequence

       Vector3 = Sequence[float]

       def vec3(x: float, y: float, z: float) -> Vector3:
           return np.array((x, y, z))




This seems to capture part of the type definition. It doesn't capture
the 3-ness of the vector.





