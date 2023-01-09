Formatting Strings and the str.format() family of functions -- Python 3.4 Notes
===============================================================================

:date: 2015-11-10 08:00
:tags: #python,python essentials
:slug: 2015_11_10-formatting_strings_and_the_strformat_family_of_functions_python_34_notes
:category: Technologies
:status: published

I have to be clear that I am obsessed with the str.format() family of
functions. I've happily left the string **%** operator behind. I
recently re-discovered the vars() function.

My current go-to technique for providing debugging information is
this:

::

    print( "note: local={local!r}, this={this!r}, that={that!r}".format_map(vars)) )

I find this to be handy and expressive. It can be replaced with
logging.debug() without a second thought. I can readily expand what's
being dumped because **all** locals are provided by vars().

I also like this as a quick and dirty starting point for a class:

::

    def __repr__(self):
       return "{__class__.__name__}(**{state!r})".format(__class__=self.__class__, state=vars(self))

This captures the name and state. But. There are nicer things we can
do. One of the easiest is to use a helper function to reformat the
current state in keyword parameter syntax, like this:

::

    def args(obj):
       return ", ".join( "{k}={v!r}".format(k=k,v=v) for k,v in vars(obj).items())

This allows us to dump an object's state in a slightly nicer format.
We can replace vars(self) with args(self) in our \__repr_\_ method.
We've dumped the state of an object with very little class-specific
code. We can focus on the problem domain without having to wrestle
with Python considerations.

Format Specifications
----------------------

The use of **!r** for formatting is important. I've (frequently)
messed up and used things like **:s** where data might be None. I've
discovered that -- starting in Python 3.4 -- the **:s** format is
unhappy with None objects. Here's the exhaustive enumeration of
cases.


::

    >>> "{0} {1}".format("s",None)
    's None'
    >>> "{0:s} {1:s}".format("s",None)
    Traceback (most recent call last):
     File "", line 1, in
       "{0:s} {1:s}".format("s",None)
    TypeError: non-empty format string passed to object.__format__
    >>> "{0!s} {1!s}".format("s",None)
    's None'
    >>> "{0!r} {1!r}".format("s",None)
    "'s' None"

Many things are implicitly converted to strings. This happens in a lot
of places. Python is riddled with str() function evaluations. But they
aren't **everywhere**. Python 3.3 had one that was removed for Python
3.4 and up.

Bottom Line: be careful where you use **:s** formatting.  It may do
less than you think it should do.





