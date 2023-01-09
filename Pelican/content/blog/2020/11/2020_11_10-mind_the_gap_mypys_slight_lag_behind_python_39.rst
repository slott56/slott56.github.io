Mind the Gap -- mypy's slight lag behind Python 3.9
===================================================

:date: 2020-11-10 08:00
:tags: mypy,PEP,#python,type hints
:slug: 2020_11_10-mind_the_gap_mypys_slight_lag_behind_python_39
:category: Technologies
:status: published

Working on a new book. Fun stuff. It's going to cover Python 3.9.

I'm adding the type hints material. And that means `PEP
585 <https://www.python.org/dev/peps/pep-0585/#forward-compatibility>`__.
Which means type hints for generics can use the generic types. We can
use list[int] instead of List[int] and avoid from typing import List.

It's all fun.

Until...

Wait... What?

When I run **mypy**, it doesn't like the PEP 585 changes.

I make sure I'm running Python 3.9.0 everywhere. I make sure I have mypy
0.790. I'm baffled.

Then. I find this.

https://github.com/python/mypy/issues/7907

Ah. It appears that **mypy** is not completely up-to-speed with Python.

And this makes perfect sense.

What I think it means is that I'll have to tweak all of the examples
when **mypy** also supports PEP 585.

For now, I'm sticking with strict checks and the 0.790 release of
**mypy**.





