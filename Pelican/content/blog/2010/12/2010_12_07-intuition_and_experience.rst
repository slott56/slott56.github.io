Intuition and Experience
========================

:date: 2010-12-07 08:00
:tags: #python,building skills books
:slug: 2010_12_07-intuition_and_experience
:category: Technologies
:status: published

First, read
`EWD800 <http://www.cs.utexas.edu/users/EWD/ewd08xx/EWD800.PDF>`__.

It has harsh things to say about relying on *intuition* in
programming.

Stack Overflow is full of questions where someone takes their
experience with one language and applies it incorrectly and
inappropriately to another language.

I get email, periodically, also on this subject. I got one recently
on the question of "cast", "coercion" and "conversion" which I found
incomprehensible for a long time. I had to reread EWD800 to realize
that someone was relying on some sort of vague intuition; it appears
that they were desperate to map Java (or C++) concepts on Python.

**Casting**

In my Python 2.6 book, I use the word "cast" exactly twice. In the
same paragraph. Here they are.

    This also means the "casting" an object to match the declared type
    of a variable isn't meaningful in Python. You don't use C++ or
    Java-style casting.

I though that would be enough information to close the subject. I
guess not. It appears that some folks have some intuition about type
casting that they need to see reflected in other languages, no matter
how inappropriate the concept is.

The email asked for a "a nice summary with a simple specific example
to hit the point home."

It's quite hard to provide an example of something that doesn't
exist. But, I guess, intuition provides a strong incentive to see
things which aren't there. I'm not sure how to word it more strongly
or clearly. I hate to devolve into blow-by-blow comparison between
languages because there are concepts that don't map. I'll work on
being more forceful on casting.

**Coercion**

The words coercion (and coerce) occur more often, since they're
sensible Python concepts. After all, Python 2 has formal type
coercion rules. See "`Coercion
Rules <http://docs.python.org/reference/datamodel.html#coercion-rules>`__".
I guess my summary ("Section 3.4.8 of the Python Language Reference
covers this in more detail; along with the caveat that the Python 2
rules have gotten too complex.") wasn't detailed or explicit enough.

The relevant quote from the Language manual is this: "As the language
has evolved, the coercion rules have become hard to document
precisely; documenting what one version of one particular
implementation does is undesirable. Instead, here are some informal
guidelines regarding coercion. In Python 3.0, coercion will not be
supported."

I guess I could provide examples of coercion. However, the fact that
it is going to be expunged from the language seems to indicate that
it isn't deeply relevant. It appears that some readers have an
intuition about coercion that requires some kind of additional
details. I guess I have to include the entire quote to dissuade
people from relying on their intuition regarding coercion.

Further, the request for "a nice summary with a simple specific
example to hit the point home" doesn't fit well with something that
-- in the long run -- is going to be removed. Maybe I'm wrong, but
omitting examples entirely seemed to hit the point home.

**Conversion**

Conversion gets it's own section, since it's sensible in a Python
context. I kind of thought that a whole section on conversion would
cement the concepts. Indeed, there are (IMO) too many examples of
conversions in the conversion section. But I guess that showing all
of the numeric conversions somehow wasn't enough. I have certainly
failed at least one reader. However, I can't imagine what more could
be helpful, since it is -- essentially -- an exhaustive enumeration
of all conversions for all built-in numeric types.

What I'm guessing is that (a) there's some lurking intuition and (b)
Python doesn't match that intuition. Hence the question -- in spite
of exhaustively enumerating the conversions. I'm not sure what more
can be done to make the concept clear.

It appears that all those examples weren't "nice", "simple" or
"specific" enough. Okay. I'll work on that.



-----


For a simple example, something like the following...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-12-08 07:25:31.723000-05:00

For a simple example, something like the following might be helpful
::

    >>> x = 3
    >>> print x, type(x)
    3
    >>> x = float(x)
    >>> print x, type(x)
    3.0


You could have a section aimed at disentangling th...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-12-07 23:05:24.537000-05:00

You could have a section aimed at disentangling the three technical
terms, as they all refer to very similar concepts of "changing the type"
of something. In C++ and Java casting is a way of changing the *static*
type to make the compiler happy, but (as noted above) this is irrelevant
to dynamically typed languages. Coercion in Python is a process wherein
the types of some values are implicitly changed to match the
requirements of an operator. Conversion is an *explicit* change of type
allowing the programmer to make use of different representations of a
value (string, numeric, boolean) for different purposes.
I bet programmers interchange these three terms when speaking casually,
which adds to the confusion. :P


Well, cast and conversion don&#39;t seem so differ...
-----------------------------------------------------

Michael Foord<noreply@blogger.com>

2010-12-07 11:13:53.397000-05:00

Well, cast and conversion don't seem so different in meaning.
As an example, if you have a class that implements \__contains_\_ and it
returns a non-boolean object then it will be changed to a bool. Is this
a cast or a conversion?

I guess the problem is, as you say, when people take words with a
precise semantic meaning in one language and apply them to another
language where that specific meaning only partly makes sense (or is only
part of the story).


&quot;not sure how to word it more strongly or cle...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-12-07 21:08:25.945000-05:00

"not sure how to word it more strongly or clearly"
Try something like this
"Since the concept of a declared type of a variable does not exist in
Python, "casting" an object to match the variable data type is
non-sensical. You don't use C++ or Java style casting in Python. This is
a long winded way of saying that Python is a dynamnic language but C++
and Java are not. Also, this is one of the areas where experience with
one langauge may be incorrectly and inappropriately applied to another
language."
Another possbility is that perhaps you are dealing with a poor student.





