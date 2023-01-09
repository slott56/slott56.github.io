Interesting...
==============

:date: 2012-02-28 08:00
:tags: perl,PHP,#python,ruby
:slug: 2012_02_28-interesting
:category: Technologies
:status: published

Check this out: http://hyperpolyglot.org/scripting.

It's a side-by-side comparison of PHP, Perl, Python, Ruby.
I'm not sure why, but it seems sort of cool.

Things like "offside rule" to describe indentation in Python are
confusing at first.  The "regions which define local scope" section on
Python makes precious little sense.  The "null test" is inaccurate.  The
"Here Document" omits mention of the exec or eval functions.

The "arrays" and "dictionaries" are merely a subset of the built-in
structures in Python.  I guess it's tedious to enumerate all the Python
features which are lacking from other languages.  Passing numbers or
strings by reference in Python is described as "not possible" when
actually it's "the only way"; except strings and numbers are immutable,
so the distinction is important.

The "C-style for" omits for i in range(10) as an equivalent.  The
file-handling section omits mentioning the **with** statement.

More importantly, the very idea of side-by-side comparison is flawed.

Python features like generator functions, list comprehensions and
context managers can't easily be displayed in a chart like this because
they don't have trivial mappings to other languages.

The languages are actually different and no simple compiler can
translate among them.  That means the side-by-side chart must be
misrepresenting each language is small (but important) ways.

Still.  It's very thorough and covers a **lot** of territory.





