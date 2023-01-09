Doctest beyond Python
=====================

:date: 2006-04-17 14:53
:tags: #python,unit testing
:slug: 2006_04_17-doctest_beyond_python
:category: Python
:status: published





This is something that elevates Doctest into the
realm of Pattern.  Perhaps even above
that.



The idea is so elegant: the
document is the test, and the test procedure is the
document.



There's a `DRY <http://en.wikipedia.org/wiki/Don't_repeat_yourself>`_  clarity to the whole thing that is rather
exciting.  It is an elegant application of basic `Literate Programming <http://en.wikipedia.org/wiki/Literate_programming>`_
principles.



The best part is that it is
difficult to do in other languages.  Ruby and Perl have the necessary
interactive execution modes.  But in Java, it would be a nightmare to define all
the required overheads to have a standardized exercise framework that paralleled
the Python interactive execution
mode.



This makes the "Doctest" pattern
a key value proposition for any new language or environment.  If you can
implement the Doctest pattern, you have something that creates value by binding
testing and documentation into one tidy package.  If you can't implement the
Doctest pattern, perhaps you should rethink your implementation because you
can't easily compete against Python.








