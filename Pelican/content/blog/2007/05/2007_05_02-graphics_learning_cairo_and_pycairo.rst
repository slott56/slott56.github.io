Graphics Learning, Cairo and PyCairo
====================================

:date: 2007-05-02 10:26
:tags: architecture,software design,UX,UI,GUI,TUI,pyGTK
:slug: 2007_05_02-graphics_learning_cairo_and_pycairo
:category: Architecture & Design
:status: published





There are three reasons, none of them terribly
good in isolation.

1.  I build business applications, not graphics
    applications, so the "basic" GTK was precisely what I needed. 


2.  `PyCairo <http://cairographics.org/pycairo>`_  is (to me) a fairly recent innovation,
    and my GTK knowledge is a few years old.

3.  Cairo requires a more complex technology
    stack; GTK 2.10 is already complex
    enough.



OLPC's `Sugar <http://www.laptop.org/laptop/software/specs.shtml>`_  specification does include Cairo, so there
isn't a good reason to avoid it.



Your
point about Cairo is interesting, since it provides a more powerful drawing
environment which does very clever things very simply.  Some of the drawing
power, however, is a distraction from my real purpose, which is to teach
programming.



Essentially, programming
is all about data structures.  In modern languages (Python, Java, C, C++) the
"language" part of the education is quick.  The data structure part of the
language, and the add-on modules are the interesting and challenging bits.  This
is were the real learning occurs, since the statements are used to manipulate
the data structures.  For the consequences of this philosophy, see my two
boring, useless `"Building Skills"
books <http://www.itmaybeahack.com/homepage/books/index.html>`_ .



This means that I (as
consultant/educator) have to dig deeply into Cairo to ferret out the data
structure features to show how a Path is similar to a Python list.  It
has the advantage of making the list structure immediately applicable to a Path.




Additionally, there seems to be a
pleasant subset of Cairo features that mirror the basic drawing features of a
more naked GTK.










