I Have Code That Didn't Work. What Now?
=======================================

:date: 2021-08-17 09:00
:tags: #python,debugging
:slug: 2021_08_17-i_have_code_that_didnt_work_what_now
:category: Technologies
:status: published

I don't get many of these "I have code that doesn't work" requests. But
I do see them once in a great while.

It might be something like the following two-part explanation with a
following question.

| 

I have this code

::

   from base64 import b64encode
   def some_func(message):
       msg = b64encode(message)

   msg = some_func(b'hello world')
   print(f"padding = {msg.count(b'=')}")

I'm getting this error.

::

   Traceback (most recent call last):
     File "/Users/slott/miniconda3/envs/CaseStudy39/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3437, in run_code
       exec(code_obj, self.user_global_ns, self.user_ns)
     File "<ipython-input-18-d54347890e97>", line 7, in <module>
       print(f"padding = {msg.count(b'=')}")
   AttributeError: 'NoneType' object has no attribute 'count'

What can I do?

<rant>As a personal note, I'm extremely grumpy when I get this in the
form of a screen picture. I cannot work with images of code. It's really
important to present code as text. Not a picture of text. </rant>

There are two kinds of answers to this question.

1. It's obvious (to me) what's wrong. While I can say what the problem
is likely to be, that doesn't help the questioner.

2. The questioner needs a strategy for getting to working software.
This, of course, can piss off some people because they insist all
questions have simple answers and I'm just being unhelpful by giving
them a bunch of steps they're supposed to follow.

I'm going to stick to answers of the second kind. I don't provide
answers of the first kind.

The Two General Answers
-----------------------

There are two general answers of the second kind.

#. Use the debugger.
#. Add ``print()``.

I'm told the debugger can be fun to use. I'm not skilled in using it, so
I don't generally recommend it. I find it difficult to uncover state
change using the debugger. It's great for exploring a data structure.

Adding ``print()`` is something I find easier and more useful.

Add print()
-----------

Here's what folks can do to uncover a problem. This is all we ever need
to do. There are no weird other cases or complex situations where this
doesn't work.

The procedure for adding ``print()`` works like this:

#. Find the line with the error. In the example, it's the final
   ``print()``.
#. Look at all the variables. In this case, there's only one, ``msg``.
#. Put a ``print()`` in front to show the values of all the variables.
   ``print(f"{msg=}")``.

This will reveal that ``msg is None`` after the assignment statement.

Now we have to look at the function, ``some_func()``, that creates the
value for ``msg``. We'll start from the end of this function and work
forward, following the above three-step procedure faithfully. And
recursively.

Eventually, we'll uncover the problem. It may not be blazingly obvious,
but we will, without fail, find a missing state change or an unexpected
state change. (In this case, it's missing.)

I can't emphasize enough that this is done as simply and directly as
possible. If the code is hellishly complex, perhaps it should be
refactored until this can be done. If the test case involves
hyper-complex conditions before it fails, then perhaps the code needs to
be refactored until this can be done.

This is the only answer I can ever give to "why doesn't my code work?"
question: Add ``print()``.





