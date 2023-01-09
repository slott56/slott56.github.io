Functional Python Programming 2e -- Now With Type Hints
=======================================================

:date: 2018-03-27 08:00
:tags: @PacktAuthors,#python
:slug: 2018_03_27-functional_python_programming_2e_now_with_type_hints
:category: Technologies
:status: published

| `Functional Python Programming, 2nd
  ed. <https://www.packtpub.com/application-development/functional-python-programming-second-edition>`__
| This has been fun to cleanup some rambling, reset the math to be sure
  it's actually right.
| And.
| **Type Hints**.
| Almost every example has had type hints added.
| (And I raised the pylint scores be rearranging some spacing and
  what-not.)
| Bonus. We will be moving the publication date up from June to possibly
  April. We're still doing technical reviews and what-not, so things
  aren't \*done*.
| **What was hardest?**
| Generics, specifically, decorators can have quite complex type hints.
  Indeed, type hinting raises important questions about trying to write
  super-generic functions that can handle too wide a spectrum of types.

::

   def some_function(arg):
       if isinstance(arg, dict):
           do_something(arg)
       elif isinstance(arg, list):
           do_something({i: v for i, v in enumerate(arg)})
       else: 
           do_something(dict(arg=arg))

| 
| This kind of thing turns out to be ill-advised. It's probably a bad
  design. More importantly, it's difficult to annotate, making it
  difficult to discern if it behaves correctly.
| In this case, the argument is Union[Dict, Sequence, Any]. I've got a
  few examples of Union types, but they're rare because I'm not a fan in
  the first place. And the few places I used them, the complexity of
  getting past **mypy** type checks showed that they add risk and cost
  without a dramatic reduction in complexity.
| In this specific case, the some_function() function is merely a
  type-converting wrapper around the do_something() function. It's
  probably better to refactor the type conversion responsibility into
  the clients of some_function().
| The arguments about "encapsulation" or "the client shouldn't know that
  detail" are generally kind of silly. We're all adults here, we
  generally have to know what's going on with respect to the conversions
  in order to use the function correctly and write unit tests.



-----


emakaren435<noreply@blogger.com>

2020-03-26 17:58:38.174000-04:00

This comment has been removed by a blog administrator.





