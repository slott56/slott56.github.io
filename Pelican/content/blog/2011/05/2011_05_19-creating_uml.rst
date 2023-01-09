Creating UML
============

:date: 2011-05-19 08:00
:tags: RST,markup,UML
:slug: 2011_05_19-creating_uml
:category: Technologies
:status: published

I'm a big fan of plain-text tools. Source Code. ReStructuredText. LaTeX.

I'm not a big fan of proprietary file formats and document formats
that are difficult or impossible to decode. JSON and XML rock. .XLS
files are painful and difficult to work with.

UML Diagrams are a particularly odious problem. To see a diagram it
has to be PNG or PDF or some other graphic format that's optimized
for storage and display, but not really optimized for editing. SVG
has a text vector markup language, but it's painful because it's so
generalized.

Recently, I found two text to UML tools that are exciting prospects.

First, there's `YUML.me <http://yuml.me/>`__. This draws pretty nice,
if simple, diagrams that you can work with with relatively little
pain. It's slow and limited. But it works for simple diagrams.

|image1|

The best part is that the image is rendered from the URL as plain
text.

http://yuml.me/diagram/scruffy/usecase/[Author]-(write text), (render
image)-[YUML], [Author]-(share link).

YUML supports simple use case diagrams, simple class diagrams and
really simple activity diagrams. It covers a few bases with a
pleasant level of flexibility.

The other tool is `Plant UML <http://plantuml.sourceforge.net/>`__.
"PlantUML is used to draw UML diagram, using a simple and human
readable text description."

The online `Plant UML Server <http://www.plantuml.com/plantuml/>`__
allows a flexible no-software-on-the-desktop way to play with their
markup language. The text of the image is not in the URL here, since
the text is so much more complex.

|image2|

The best part of this is that the pictures come from plain text.

-   The plain text is trivial to put under configuration control.

-   Plain text system descriptions are easy to write with simple
    markup.

-   Plain text documentation of existing software can be derived from
    simple source analysis.

-   Plain text design documents can generate some elements of the
    source code

.. |image1| image:: http://yuml.me/diagram/scruffy;scale:75/usecase/%5BAuthor%5D-(write%20text),%20(render%20image)-%5BYUML%5D,%20%5BAuthor%5D-(share%20link).

.. |image2| image:: http://www.plantuml.com:80/plantuml/img/it8iBSd8Bx9IqDMrKz08paWiIbNmoSpBrkJbiaAH2Y_AB4bL24cjA05A0IL3ylDpe591gNafgKKAdhc9wQcQ0000



-----

Also check out a number of Sphinx extensions whic ...
-----------------------------------------------------

Kevin H<noreply@blogger.com>

2011-05-19 16:02:17.133000-04:00

Also check out a number of Sphinx extensions whic do things like this at
https://bitbucket.org/birkenfeld/sphinx-contrib/
All based on external tools (aafig, blockdiag, sdedit, etc.) but I find
that the sphinx-contrib repo acts as sort of a hub for these tools.


Hi, A full list of text-to-UML tools can be found ...
-----------------------------------------------------

Jordi Cabot<noreply@blogger.com>

2011-05-21 11:00:13.109000-04:00

Hi, A full list of text-to-UML tools can be found here:
http://modeling-languages.com/content/uml-tools#textual (around 15 and
counting!)


See also http://www.graphviz.org/ which is a gener...
-----------------------------------------------------

zacharyh<noreply@blogger.com>

2011-05-29 17:52:40.757000-04:00

See also http://www.graphviz.org/ which is a general purpose grapher
that can be extended for UML.
See here for an example:
http://www.ffnn.nl/pages/articles/media/uml-diagrams-using-graphviz-dot.php
Also, it appears UML Graph is such an extension of graphviz.





