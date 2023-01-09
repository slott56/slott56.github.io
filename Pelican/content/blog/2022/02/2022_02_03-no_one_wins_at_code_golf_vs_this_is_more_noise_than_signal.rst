No one wins at Code Golf vs. This is more noise than signal
===========================================================

:date: 2022-02-03 20:14
:tags: code golf,#python
:slug: 2022_02_03-no_one_wins_at_code_golf_vs_this_is_more_noise_than_signal
:category: Technologies
:status: published

Looking at code. Came to a 20-line block of code that did exactly this.

::

   sorted(Path.cwd().glob("some_pattern[1-9]*.*"), reverse=True)

Twenty lines. Seriously.

To be fair, 8 of the 20 lines were comments. 3 were blank. Which leaves
9 lines of code to perform the task of a one-liner.

I often say "no one wins at code golf" as a way to talk people out of
trying to minimize Python code into vanishingly small black holes where
no information about the code's design escapes.

However. Blowing a line of code into 9 lines seems to be just as bad.

I'll spare you the 9 lines. I will say this, though, the author was
blissfully ignorant that ``Path`` objects are comparable. So. There were
needless conversions. And. Even after commenting on this, they seemed to
somehow feel (without evidence of any kind) that ``Path`` objects were
incomparable.

This is not the first time I've seen folks who like assembler-style
code. There is at most one state-change or attribute reference on each
line of code. The code has a very voluble verticality (VVV™).

This seems as wrong as code golf.  Neither style provides meaningful
code.

How can we measure "meaningful"?

Of the 8 lines of comments, the English summary, the "reverse alphabetic
order" phrase is only a few words. Therefore, the matching code can be
an equally terse few symbols. I think code can parallel natural
language.





