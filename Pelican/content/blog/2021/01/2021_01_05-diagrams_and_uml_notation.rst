Diagrams and UML notation
=========================

:date: 2021-01-05 08:00
:tags: plantuml,UML
:slug: 2021_01_05-diagrams_and_uml_notation
:category: Technologies
:status: published

When I started in this business I was given a flowcharting template.

See https://americanhistory.si.edu/collections/object-groups/flowcharting-templates.
I'm pretty sure I had one of
these: https://americanhistory.si.edu/collections/search/object/nmah_690078.

Since then, things have changed a little.

I fondly recall using the Rational Rose (and an earlier tool that did
Rumbaugh OMT diagrams) to create object models.

But these were expensive.

After much searching, I found **ArgoUML**. This was my go-to-diagrammer
of choice for many years. It's available
here: https://argouml-tigris-org.github.io.

Then, I wound up using **yuml**
at https://yuml.me/diagram/scruffy/class/draw. This was very nice
because there was a source text version of the diagram. It was a
high-level code-like description that would lead to a handy picture you
could include in documentation.

Heavenly.

Recently, I spent time using **draw.io**. Start here https://draw.io.
You have plain-text source version of the diagram that's Git-friendly. I
liked that. It has a lot of UML features, which is very nice, also.

But now.

I'm using **plantUML**, and I think it's pretty
handy. https://plantuml.com. It's a big-old JAR file that converts text
to a diagram. There's no GUI component to this. You describe the image
in a source-code like way. Run it through the tool, and you get a
picture you can paste into documentation. Like yuml, it has an
easy-to-understand high-level text description. I strongly suspect I
could walk a Python AST and emit plantUML source as an intermediate
language from which pictures can be created.

The Python-Markup tool (https://python-markdown.github.io/extensions/)
has a third-party PlantUML plug-in. PyCharm can leverage this to draw
while you're editing in the markdown window.

The Fiddly Bits
---------------

It's a little fiddly to get all the parts organized properly, but, it
really, really does work. You can write technical documentation, with
pictures.

-  Add the Markdown tool to PyCharm.
-  In the preferences for the PyCharm Markdown tool, install and enable
   PlantUML.
-  You can usually use **conda** to install **graphviz** as well as
   installing the **plantuml-markdown** tools. You can manually run the
   **markdown_py** application to create the HTML copies of the .md
   files.
-  Update your OS environment settings to set the
   **GRAPHVIZ_DOT** environment variable to name the conda virtual
   environment where **graphviz** was installed. For macOS and Linux
   users update the **~/.zshrc** (or **~/.bashrc**) file, depending on
   which shell is in use. Windows users have my heartfelt sympathy;
   maybe set the system environment variables.
-  You may also need to create a **plantuml** shell script that's on
   your **PATH**. I put it in **/usr/local/bin**.

See https://github.com/mikitex70/plantuml-markdown for details on
installation.

After all this fussing around, it worked delightfully. I'm a convert to
PlantUML.

I suggest the following in each diagram.

::

   skinparam monochrome true
   skinparam handwritten false
   skinparam shadowing false
   hide class circle

You may want to set a more global configuration, but I sometimes want to
change the handwritten parameter to true for "draft" diagrams, separate
from final.

tl;dr
-----

You can integrate plantUML with PyCharm to draw pictures while you're
editing in the markdown window.

You do have to trust plantUML to draw more-or-less what you want. There
are limits, and if you don't like what plantUML is doing, switch to
draw.io. If you are flexible, however, it's really, really good.

| 





