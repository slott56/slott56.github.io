What Books Should I Read? In What Order? 
=========================================

:date: 2021-07-13 09:00
:tags: packtpub,#python,building skills books
:slug: 2021_07_13-what_books_should_i_read_in_what_order
:category: Technologies
:status: published

A fascinating question.

   
      ... I'm baffled by the amount of books you've published over the
      course of time. Currently Reddit suggests that I use Building
      Skills in Python under Beginner's section, but it looks quite
      outdated. So back and forth, I found your Building Skills in OO on
      GitHub Page and was quite happy with the read on the first 100
      pages.

      I searched for more info on the books you've published and wanted
      to know if you could sort them in ascending order of difficulty
      for me as I intend to purchase them slowly.

      My main concern to learn Python is just to cross technical
      interviews and building applications that help with my workflow
      (they are in bash with around 200 functions, so I'm hoping to
      migrate them to something which is more robust). 

      Currently the focus I intend to develop is on:

      1) Strong Foundations of the Python Language.

      2) Strong Foundations on the Basic Libraries for Data Structures
      and Algorithms (For example, bisect gives me insort(), calendar
      gives me isleap(), iter_tools gives me permutation(), etc).

      3) Strong Foundations on the Design Patterns.

      So could you please help me out and suggest your books?

This is challenging for a few reasons.

First, the "Building Skills" books have been reduced to only the
*Building Skills in OO Design*. This can be found in GitHub.
https://github.com/slott56/building-skills-oo-design-book.

That book is not really targeted to beginners, though. It presumes some
core OO skills, and provides a (very) long series of exercises to build
on those skills.

Second, I never really conceived of a beginner-to-expert sequence of
books. From your letter, I see that I need to look at filling in some
gaps in my sequence of books. I'll alert my editors at Packt, and we can
consider this in the future.

Specific Needs
--------------

Let's look at your needs.

1. Foundations in the Python language.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This might be something you can learn from my `Python
Essentials <https://bookshop.org/books/python-essentials/9781784390341>`__.
This isn't focused on complete n00bs. All of my books expect some
programming background. Since you're an Android engineer and write code
in C++ and Java, this may be helpful. This title is getting old,
however, and needs a second edition.

For someone with core programming skills, I suspect that `Mastering OO
Python <https://www.oreilly.com/library/view/mastering-object-oriented-python/9781789531367/>`__ will
be suitable. My `Python 3 OO
Programming <https://www.packtpub.com/product/python-object-oriented-programming-fourth-edition/9781801077262>`__ (4th
ed.) is similarly aimed at folks who can program and can learn a new
language quickly.

A book like Martelli's `Python in a
Nutshell <https://www.amazon.com/Python-Nutshell-Second-Alex-Martelli/dp/0596100469>`__ may
provide a better foundation the way the language works than any of mine.
Also Lutz's `Learning
Python <https://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730/ref=pd_lpo_14_t_2/145-5116566-3930956>`__
is extremely popular.

2. Foundations in the Standard Library.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is tricky. I touch on some of these topics in `Functional Python
Programming <https://www.abebooks.com/Functional-Python-Programming-Second-Edition-Lott/30276798601/bd>`__
(2nd ed.) I also touch on some of these topics in the `Modern Python
Cookbook <https://www.ebooks.com/en-us/book/210095364/modern-python-cookbook/steven-f-lott/>`__
(2nd ed.)

I don't, however, cover very much of the library. I touch on a few
really important modules. The library is vast. A book like
Hellmann's `The Python Standard Library by
Example <https://www.amazon.com/Python-Standard-Library-Example/dp/0321767349>`__ might
be more suitable than one of mine.

3. Design Patterns.
~~~~~~~~~~~~~~~~~~~

This is central to `Python 3 OO
Programming <https://www.packtpub.com/product/python-object-oriented-programming-fourth-edition/9781801077262>`__ (4th
ed.) Dusty Phillips and I cover a number of popular design patterns in
detail. 

There are -- of course -- a lot of very, very good books on Python. I'm
honored you reached out to me.

Other Random Advice
-------------------

Because Python is a relatively simple language (with a vast library) I
have always suspected that language foundations don't really require a
ton of explanation. Many languages (i.e., C++) are filled with odd
details and weird features that are really unpleasantly complex. Many
Java programmers get used to the distinction between the primitive
``int`` type and the ``Integer`` class type. While the Java and C++
approach can seem simple (after a while) it really isn't simple at all.

The standard library is vast, and it takes time to get used to how much
is there. I would suggest having a browser tab open
to https://docs.python.org/3/library/ at all times.

Design patterns, similarly, require some care. There are complex details
around implementing the **Singleton** pattern in C++ and Java. Python
class definitions and Python module definitions are Singletons, and
using a class definition as a **Singleton** object is often far simpler
than the commonly-used techniques for C++ and Java.





