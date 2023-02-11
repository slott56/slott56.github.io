Python Confusion
######################

:date: 2023-02-07 08:00
:tags: #python,learning
:slug: 2023_02_07-python_confusion
:category: Technologies
:status: published

For social contact, I'm generally following people on https://fosstodon.org/home.
I'm https://fosstodon.org/@slott56.

Or `@slott56@fosstodon.org <https://fosstodon.org/@slott56>` as they say in the Fediverse.

But I saw some stuff on Twitter that was disheartening.

    I thought Python🐍wasn't strongly typed.🤔
    But this code seems to be casting input into an int?

    ✅guess = int(input("Pick a number: "))

    The ugliness of all the round brackets aside, why
    does this need to be cast into an int?

Oh dear.

1. Python *is* strongly typed.  Variables don't have a type associated with them, so we say that variable types are dynamic. Object types are essentially immutable.

2. It's not a "cast". It's a conversion. You can't cast objects to another type in Python. Types are essentially immutable.

3. The "cast to an int" is really "converted to an int" and that's required because the string value from the ``input()`` is likely useless later.

Without more code, it's hard to know why the conversion is required.
I'm willing to guess there's comparisons against integers elsewhere,
and therefore, this conversion from string to int will make those
later comparisons work.

Some of the responses to the tweet were a bit off. I have
the urge to enumerate the problems, but that's likely to be unhelpful.

(I say types are *essentially* immutable because I have a vague
feeling that it's possible to around some of the dunder attributes
for some kinds of classes and change the association between
object and creating class. I have not investigated this
because the horror of casting in C, C++, Java, etc., is so emotionally
scarring that I can't even.)
