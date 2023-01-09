Tragedy Averted
===============

:date: 2022-08-09 08:00
:tags: sphinx,#python,literate programming,docutils,plantuml,pyWeb
:slug: 2022_08_09-tragedy_averted
:category: Technologies
:status: published

I almost made a terrible blunder.

See https://github.com/slott56/py-web-tool for some background. This is
a "Literate Programming" tool. I started fooling around with this kind
of thing back in '05 (maybe even earlier.) This is not the blunder. The
whole idea of literate programming is not very popular. I'm a fan of
`Jupyter{Book} <https://jupyterbook.org/en/stable/intro.html>`__ as the
state of the art in sophisticated literate programming, if you're
interested in it.

In my case, I started this project so long ago, I
used `docutils <https://docutils.sourceforge.io>`__. This was
long before `Sphinx <https://github.com/sphinx-doc/sphinx>`__ arrived on
the scene. I never updated my little project to use Sphinx. The point
was to have a kind of pure literate programming tool that could work
with a variety of markup languages, including (but not limited to) RST.

Recently, I learned about `PlantUML <https://plantuml.com>`__. The idea
of a text description of a diagram is appealing. I don't really need to
draw it; I just need to specify what's in it and let
`graphviz <https://graphviz.org>`__ do the rest. This tool is very, very
cool. You can capture ideas quickly. You can refine and expand on ideas
until you reach a point where code makes more sense than a picture of
code.

For some things, you can gather data and draw a picture of things \*as
they are*. This is particularly valuable for cloud-based infrastructure
where a few queries leads to PlantUML source that is depicted very
nicely.

Which leads to the idea of Literate Programming including UML diagrams.

Doesn't sound too difficult. I can create an extension to **docutils**
to introduce a UML directive. The resulting RST would look like this:

::

   ..  uml::

       left to right direction
       skinparam actorStyle awesome

       actor "Developer" as Dev
       rectangle PyWeb {
           usecase "Tangle Source" as UC_Tangle
           usecase "Weave Document" as UC_Weave
       }
       rectangle IDE {
           usecase "Create WEB" as UC_Create
           usecase "Run Tests" as UC_Test
       }
       Dev --> UC_Tangle
       Dev --> UC_Weave
       Dev --> UC_Create
       Dev --> UC_Test

       UC_Test --> UC_Tangle

This could be handy to have the diagrams as part of the documentation
that tangles the working the code. One source for all of it.

I started down the path of researching **docutils** extensions. Got
pretty far. Far enough that I had an empty repository and everything. I
was about ready to start creating spike solutions.

Then.

[*music cue*] \*\ `duh duh
duuuuuuh <https://www.youtube.com/watch?v=9mSVzGnKsXw>`__\ \*

I found that Sphinx already has an extension for PlantUML. I almost
started reading the code to see how it worked.

Then I realized how dumb that was. It already works. Why read the code?
Why not install it?

I had a choice to make.

#. Continue building my own **docutils** plug-in.
#. Switch to Sphinx.

Some complications:

-  My Literate Programming tool produces RST that \*may\* not be
   compatible with Sphinx.
-  It's yet another dependency in a tool that started out with zero
   dependencies. I've added pytest and tox. What next?

What to do?

I have to say that Git is amazing. I can make a branch for the spike. If
it works, pull request. If it doesn't work, delete the branch. This
continues to be game-changing to me. I'm old. I remember when we had to
back up the whole project directory tree before making this kind of
change.

It worked. My tool's RST (with one exception) worked perfectly with
Sphinx. The one exception was an obscure directive, ``.. class:: name``,
used to provide an HTML class name for the following block. This always
should have been the **docutils** ``.. container:: name`` directive.
With this fix, we're good to go.

I'm happy I avoided the trap of reimplementing something. Instead of
that, I upgraded from "bare" **docutils** with my own CSS to Sphinx with
it's sophisticated templates and HTML Themes.





