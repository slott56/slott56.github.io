Why Python Is Weird For C++ Developers -- Some Thoughts
=======================================================

:date: 2021-08-10 09:00
:tags: #python,C++,Programming Languages
:slug: 2021_08_10-why_python_is_weird_for_c_developers_some_thoughts
:category: Technologies
:status: published

See `9 Reasons Why Python Is Weird For C++
Developers <https://betterprogramming.pub/9-reasons-why-python-is-weird-for-c-developers-b37e650471d6>`__.

I'm often bothered by inter-language comparisons. Mostly because
programming languages -- except in the most abstract way -- aren't
really very comparable. At the Turing Machine level the finite state
automata are comparable, but that reductionist view (intentionally)
eliminates all the expressive power from a given language.

Let's look at the reasons in some detail. A few of them actually are
interesting.

#. **Whitespace**. I'm dismissive of this as an interesting difference.
   When I read code in EVERY other programming language, I'm immediately
   aware that programmers can indent. Indeed, I've seen C and C++ code
   were {}'s were omitted, but the code was indented properly, making it
   devilishly hard to debug. My experience is that folks get the
   indentation right BEFORE the get the {}'s right.

#. **Syntax**. In this article, it's the lack of {}'s. Again, I'm
   dismissive because I've actually helped folks learning C++ who had
   the indentation right and the {}'s wrong. This is ony "weird" if
   you're absolutely and completely convinced that {}'s are somehow a
   divine requirement that transcends all human attempts at
   interpretation. With Unicode, we're in a position to separate set
   membership from block-of-code and start using multiple variants on
   {}'s.  I'd vote for ``if a > b 【m = a】else 【m = b】`` using
   【】for code blocks.

#. **Class Variables**. This points out an inherent ambiguity of C++.
   Most of the time, most things are not "static". They're "automatic"
   that is, associated with the instance. The auto keyword, however, is
   rarely used, and is mostly assumed. Python (outside **dataclasses**)
   is more consistent. All things inside the class statement are
   "static": part of the class. In the case of **dataclasses**, this
   simple rule is broken, which can be confusing. But. This wasn't
   mentioned.

#. **Pointer and Reference Transparency**. This is simple confusion. All
   Python is handled by reference all the time. C++ is an absolute mess
   of "primitive" types that don't use references and objects that do
   use references. Java is just as bad. And I want to emphasize bad.
   Python is perfectly consistent, and -- I would suggest -- the
   opposite of weird. But. The article is describing things from a C++
   perspective, as if C++ were somehow not weird. I suggest this isn't a
   great approach.

#. **Private Class Members**. This is summarized as "better
   encapsulation and control" without a concrete example. It's hard to
   provide a concrete example because the Pythonic approach works so
   well. The only use case for "private" that I've been able to
   understand is when you're concealing the entire implementation from
   all scrutiny. That is, you have a proprietary implementation with an
   encrypted JAR file and you want to avoid revealing it to protect some
   intellectual property. Since Python is source, this can't happen, and
   we say "We're all adults here." Flag it with a leading \_ and we'll
   recognize it as part of an implementation detail that might change.

#. **Self vs. this**. Not sure what this is but the phrase "only major
   programming language" is something that relies on Java and C++ being
   near the top of the TIOBE index. I suspect we can find a lot of
   languages that use neither "self" nor "this". I'm not sure exactly
   how this is weird, but, I get that it's different.

#. **Multiple Return Values**. This seems like an intentional refusal to
   understand how tuples and tuple unpacking work. Again, this seems to
   make C++ the yardstick when C++ is clearly kind of weird here.

#. **No Strong Data Types**. This seems like another refusal to
   understand Python. In this case, it feels like it's a refusal
   understand that objects are strongly typed in Python and variables
   are transient labels attached to objects. The mypy tool will try to
   associate a type with a variable and will warn you about
   ``a = "string"`` followed by ``a = 42``. Perhaps I'm not
   understanding, but the portrayal of C++ rules as "not weird" seems
   like it's being taken too far.

#. **No Constants**. This isn't completely true. Some folks use enums to
   provide enumerated numeric constant values in the rare cases where
   this might matter. Using global variables as constants actually works
   out fine in practice. Most tools will look for ALL_CAPS names on the
   left of an = sign; and if this occurs more than once will raise a
   warning. If you have really stupid fellow programmers who can't
   understand how some variables shouldn't be reused, you can easily
   write a script to walk the AST looking for references to global
   variables and warn your colleagues that there are rules and they're
   not following them. This is part and parcel of the "We're all adults
   here" approach. If folks can't figure out how constants work, you
   need to collaborate more fully with other developers to help them
   understand this.

I'm unhappy with lifting up C++ quirks as if they're somehow really
important. I don't think C++ is a terribly helpful language. The need
for explicit memory management, for example, is a terrible problem. The
explicit distinction between primitives and objects is also terrible.

While compare-and-contrast with Python might be helpful for C++
expatriates, I think this article has it exactly backwards. I think the
following list couuld be more useful.

-  Python frees you from counting {}'s. Just indent. It's easier.

-  Python has simple rules for class/instance variables (except in the
   case of dataclasses and named tuples.) Also: if it starts with
   ``self.`` it's an instance variable.

-  Python is all references without the horrifying complexity of
   primitive types.

-  We're all adults here. Don't stress yourself out over privacy or
   constants. Document your code, instead. Write a unit test case or
   two. Use mypy. Use black.

-  Tuple unpacking and the fact that tuples are often implied works out
   very nicely to create very clean code.

-  Data types are part of the object. There's no magical "cast"
   capability to process a block of bytes as if they're some other
   type.


These are advantages of Python. And disadvantages of C++. I think
it's better to talk about what Python has than what Python lacks when
measured against a terribly complex language like C++.








