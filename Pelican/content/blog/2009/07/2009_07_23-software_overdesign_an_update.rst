Software Overdesign -- An Update
================================

:date: 2009-07-23 10:12
:tags: RST,xml,DOM,UML
:slug: 2009_07_23-software_overdesign_an_update
:category: Technologies
:status: published

Saw a horrifying design document recently. One that was at the "gouge
out my eyes" level of badness. That's one step below "drink until I
forget what I saw", but one level above "beat the author with a tire
iron."

They were -- I'm guessing here -- trying to develop their own
Document Object Model. Distinct from any established DOM. The
Wikipedia entry on
`DOM <http://en.wikipedia.org/wiki/Document_Object_Model>`__ provides
several examples of existing DOM's. Why reinvent?

The application is -- ultimately -- going to be in Python. There are
two candidate DOM's that could have been used: the `XML
DOM <http://docs.python.org/library/xml.dom.html>`__ and the RST DOM
as implemented in Docutils
`nodes <http://svn.berlios.de/viewcvs/docutils/trunk/docutils/docutils/nodes.py?view=markup>`__
module. Instead, they were reinventing: they appear to have spent a
great deal of time writing use cases for "editor". I expect there was
a use case for "wheel" and "fire" in there also.

What scared me was the "flatness" of the model. Every buzzword had
it's own class. There was no inheritance or reuse anywhere in the
diagram. Parts of the model where influenced by the
`DocBook <http://www.docbook.org/>`__ schemas. The actual
`DTD <http://www.docbook.org/xml/4.5>`__ could have been turned into
the model, but wasn't.

Further, undefinable terms like "sentence" showed up as class
definitions. XML's DOM treats all text as -- well -- text. Any
language structure is outside the DOM. RST, similarly, treats text as
a container
":literal:`... children are all `Text` or `Inline` subclass nodes.`"

All I could suggest was "locate common superclasses" and "until you
can define 'sentence', omit it". And then run outside and gouge out
my eyes.

It's hard to criticize something like that in a truly helpful manner.
Fixing the model is merely putting lipstick on a pig.

As far as I can tell, the application is -- somehow -- an editor that
imposes a severe set of structural constraints on what the author can
do. It's as if `RST <http://docutils.sourceforge.net/rst.html>`__,
`docutils <http://docutils.sourceforge.net/index.html>`__ and
`Sphinx <http://sphinx.pocoo.org/>`__ don't exist. The real solution
isn't "fix your object model" it's "fix your problem statement and
learn RST."

--------------

Post Script
-----------

Check out this reply:

    The advantage of having an "outliner data model" and a
    "document data model" like DocBook XML is that your outliner
    functionality is not limited by the DocBook XML. The downside
    is that have to create and support a second model as well as
    provide a mapping between the two.

In other words, rather than simplify, we'll (1) insist the
eye-gougingly bad model is "better", (2) justify the complexity
("not limited by DocBook [DOM]") by and (3) plan to add some more
complexity to map an overly complex (and atypical) DOM to a
standard DOM.

Not a very parsimonious approach to design.





