Code Review
===========

:date: 2019-01-24 07:55
:tags: unit testing,#python
:slug: 2019_01_24-code_review
:category: Technologies
:status: published


I can't actually share all the code. So this feels incomplete. But I
can share what I said about the code. Then you can look at your code
and decide if you've got similar problems to fix.

My responses were these. I'll expand on them below.

#. This appears to be a single cell in a Jupyter notebook? Why isn’t it
   a script?

#. The code doesn’t look like any effort was made to follow any
   conventions. Use black. Or pylint. Make the code look conventional.

#. There don’t appear to be any docstring comments. That’s really a very
   bad practice.

#. The design appears untestable. That’s a very bad practice.

#. If this is an example of “production” code, I would suggest it needs
   a lot of rework.


Let's review these in a little more detail.



Number 1 was based on the file name being ``something_p36.ipynb.txt``.
The Jupyter notebookiness of the name is a problem. The ``_p36`` is
extra creepy, and indicates either a severe problem understanding
how bash "shebang" comments work, or a blatant refusal to simply
use Python3. It's hard to say what's going on, and I didn't even
try to ask because... well... too many other things weren't clear.
Don't make up complex, weird naming rules. Use something.py.
Simple. Flat. Pythonic.


Number 2 was based on things like this: def PrintParameters(pca): I
hate to get super-pure PEP-8, but this kind of thing is simply hard
to read. There were a LOT of other troubling aspects to the code.
Once this is corrected, some of the other problems will go away, and
we could move forward to more substantial issues.

Follow existing code styles. Find Python code. The standard library
has a LOT of examples already part of your installation. Read it.

Enjoy it. Mimic it.

Use pylint. Always.

Number 3 and Number 4 are consequences of the bulk of the code being
a flat script with few class or function definitions. Actually, there
were one of each. One class. One function. 240 or so lines of code.
There was no separate ``__name__ == "__main__"`` section, so I was
generally unhappy with the overall design.

Also. There's code like this

::

   if True:

Yes.  That's a real line of code. Sigh.

Here's an ancillary problem. If you need to write something like
this, you're doing it wrong.

::

   ##########################
    -- init Stuff
   ##########################

The code that follows one of these "big billboard comment" sections
**must** be part of a function or class. It can't be left
floating around with a billboard for demarcation. It should be
refactored into a function (or method of a class), documented, and
tested.

Did I mention tested?

It's untestable as written. Sigh.

Number 5 may be a misunderstanding on my part. The email had this:
"They have produced production code that mathematically optimizes
stuff for [redacted]. So, they are heads up type of people."

I'm guessing this is relevant because the team has some "production"
code in Python and consider themselves knowledgeable. Otherwise, this
is noise, and I should have ignored it.

I'm hopeful they'll use `black <https://github.com/ambv/black>`__,
make the code minimally readable, and we can move on to substantial
issues regarding design for testability and overall possible
correctness issues.

It wasn't the worst code I've seen. But. It shows a lot of room for
growth and improvement.





