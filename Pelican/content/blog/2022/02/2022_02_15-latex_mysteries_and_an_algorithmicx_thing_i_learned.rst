LaTeX Mysteries and an algorithmicx thing I learned.
====================================================

:date: 2022-02-15 08:00
:tags:
:slug: 2022_02_15-latex_mysteries_and_an_algorithmicx_thing_i_learned
:category: Technologies
:status: published

I've been an on-and-off user of LaTeX since the very, very beginning.
Back in the dark days when the one laser printer that could render the
images was in a closely-guarded secret location to prevent everyone from
using it and exhausting the (expensive) toner cartridges.

A consequence of this is I think the various algorithm environments are
a ton of fun. Pseudo-code with math embedded in it. It's marvelous. It's
a pain in the neck with this clunky blogging package, so I can't easily
show off the coolness. But. You can go
to https://www.overleaf.com/learn/latex/Algorithms to see some examples.

None of which have try/except blocks. Not a thing.

Why not? I suspect it's because "algorithmic" meant "Algol-60" for
years. The language didn't have exceptions and so, the presentation of
algorithms continues to this day without exceptions.

What can one do?

This.

::

   \algblock{Try}{EndTry}
   \algcblock[Try]{Try}{Except}{EndTry}
   \algcblockdefx{Try}{Except}{EndTry}
      [1][Exception]{\textbf{except} \texttt{#1}}

   \algrenewtext{Try}{\textbf{try}}

This will extend the notation to add ``\Try``, ``\Except``, and
``\EndTry`` commands. I think I've done it all more-or-less correctly.
I'm vague on where the ``\algnotext{EndTry}`` goes, but it seems to be
needed in each ``\Try`` block to silence the ``\EndTry``.

As far as I know, I'm the only person who seems to care. There seems to
be little about this anywhere online. I'm guessing it's because the
basics work perfectly, and no one wants this kind of weird add-on.





