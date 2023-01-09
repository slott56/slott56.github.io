All Those TODO's
================

:date: 2009-05-17 15:41
:tags: RST,sphinx,#python,epydoc
:slug: 2009_05_17-all_those_todos
:category: Technologies
:status: published

About a year ago, we started out doing Python development with simple
\ `rst2html <http://docutils.sourceforge.net/docs/user/tools.html>`__\ 
documents for requirements, design, etc.  In the code, we had comments
that used \ `epydoc <http://epydoc.sourceforge.net/>`__\  with the
\ `epytext <http://epydoc.sourceforge.net/manual-epytext.html>`__\ 
markup language.

| 

No, it wasn’t confusing.  Free-text documents (requirements,
architecture, design, test plans, etc.) are easy and fun to write in
RST.  Just write.  Leave the formatting to someone else.  A little
semantic markup doesn’t hurt, but you don’t spend hours with MS-Word
trying to  disentangle your bullets and your numbering.

| 

Adding comments to code in epytext was pretty easy, also.

| 

Then I discovered \ `Sphinx <http://sphinx.pocoo.org/>`__\ .   Sphinx
can add module documentation to a document tree very elegantly.
Further, Sphinx can pull in RST-formatted module comment strings.  Very
nice.

| 

Except, of course, we have hundreds of modules in epytext.  Today, I
started tracking down all of the 150+ modules without proper document
strings in RST notation.  Hopefully, this time tomorrow, I’ll have a
much, much better -- and internally consistent -- set of documentation.





