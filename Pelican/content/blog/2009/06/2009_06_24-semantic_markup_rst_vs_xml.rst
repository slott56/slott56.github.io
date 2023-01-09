Semantic Markup -- RST vs. XML
==============================

:date: 2009-06-24 14:08
:tags: RST,sphinx,xml
:slug: 2009_06_24-semantic_markup_rst_vs_xml
:category: Technologies
:status: published

I have very mixed feelings about XML's usability.

An avowed goal of the inventors of XML was "XML documents should be
human-legible and reasonably clear." While I like to think that
"legible" means *usable*, I'm feeling that legibility is really a
minimal standard; I think it's a polite way of saying "viewable with
any text editor."

I've got some content (my `Building
Skills <http://homepage.mac.com/s_lott/books/index.html>`__ books)
that I've edited with a number of tools. As I've changed tools, I've
come to really understand what semantic markup means.

**Once Upon A Time**

When I started -- back in '00 or '01 -- I was taking notes on Python
using BBEdit and other text-editor tools. That doesn't really count.

The first drafts of the Python book were written using AppleWorks;
the predecessor to Apple's iWork
`Pages <http://www.apple.com/iwork/pages/>`__ product. Any Mac text
editor is a joy to use. Except, of course, that AppleWorks semantic
markup wasn't the easiest thing to use. It was little more than the
visual styles with meaningful names.

Then I converted the whole thing to XML.

**DocBook Semantic Markup**

The DocBook XML-based markup seemed to be the best choice for what I
was doing. It was reasonably technically focused, and provided a
degree of structure and formality.

To convert from AppleWorks, I exported the entire thing as text and
then used the `LEO Outlining
Editor <http://webpages.charter.net/edreamleo/front.html>`__ to
painstakingly -- manually -- rework it into XML.

At this point, the XML tags were a visible part of the document, and
editing the document means touching the tags. Not the easiest thing
to do.

I switched to XMLmind's `XXE <http://www.xmlmind.com/xmleditor/>`__.
This was nice -- in a way. I didn't have to see the XML tags, but I
was heavily constrained by the clunky way they handle the XML
document structure. Double-clicking a word can lead to ambiguity on
which level of tag you wanted to talk about.

The XML was "invisble" but the many-layered hierarchical structure
was very much in my face.

**RST Semantic Markup**

After becoming a heavy user of Sphinx, I realized that I might be
able to simplify my life by switching from XML to
`RST <http://docutils.sourceforge.net/rst.html>`__.

There are a number of gains when moving to RST.

#. The document is simpler. It's approximately plain text, with a
   number of simple constraints.

#. Editing is easier because the markup is both explicit and simple.

#. The tooling is simpler. Sphinx pretty much does what I want with
   respect to publication.

There is just one big loss: semantic markup. DocBook documents are
full of ``<acronym>TLA</acronym>`` to provide some meaningful
classification behind the various words. It's relatively easy to
replace these with RST's `Interpreted Text
Roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`__.
The revised markup is ``:acronym:`TLA```.

The smaller, less relevant loss, is the inability to nest inline
markup. I used nested markup to provide detailed
``<function><parameter>a</parameter></function>`` kind of descriptions. I
think ``:code:`function(x)``` is just as meaningful when it comes to
analyzing and manipulating the XML with automated tools.

**The Complete Set of Roles**

I haven't finished the XML -> Sphinx transformation. However, I do
have a list of roles that I'm working with.

Here's the list of literal conversions. Some of these have obvious
Sphinx/RST replacements. Some don't. I haven't defined CSS markup
styles for all of these -- but I could. Instead, I used the existing
roles for presentation.

::

  .. role:: parameter(literal)

  .. role:: replaceable(literal)

  .. role:: function(literal)

  .. role:: exceptionname(literal)

  .. role:: classname(literal)

  .. role:: methodname(literal)

  .. role:: varname(literal)

  .. role:: envar(literal)

  .. role:: filename(literal)

  .. role:: code(literal)

  .. role:: prompt(literal)

  .. role:: userinput(literal)

  .. role:: computeroutput(literal)

  .. role:: guimenu(strong)

  .. role:: guisubmenu(strong)

  .. role:: guimenuitem(strong)

  .. role:: guibutton(strong)

  .. role:: guilabel(strong)

  .. role:: keycap(strong)

  .. role:: application(strong)

  .. role:: command(strong)

  .. role:: productname(strong)

  .. role:: firstterm(emphasis)

  .. role:: foreignphrase(emphasis)

  .. role:: attribution

  .. role:: abbrev

The next big step is to handle roles that are more than a simple
style difference. My benchmark is the :trademark: role.

**Adding A Role**

Here's what you do to add semantic markup role to your document
processing tool stack.

First, write a small module to define the role.

Second, update Sphinx's conf.py to name your module. It goes in
the extensions list.

Here's my module to define the trademark role.

::

    import docutils.nodes
    from docutils.parsers.rst import roles

    def trademark_role(role, rawtext, text, lineno, inliner,
        options={}, content=[]):
        """Build text followed by inline substitution '|trade|'    """
        roles.set_classes(options)
        word= docutils.nodes.Text( text, rawtext )
        symbol= docutils.nodes.substitution_reference( '|trade|', 'trade', refname='trade' )
        return [word,symbol], []

    def setup( app ):
        app.add_role( "trademark", trademark_role )

Here's the tweak I made to my conf.py

::

    import sys, os
    project=os.path.join( "")
    sys.path.append("/Users/slott/Documents/Writing/NonProg2.5/source")extensions = ['sphinx.ext.autodoc', 'sphinx.ext.ifconfig', 'docbook_roles' ]

That's it. Now I have semantic markup that produces additional
text (in this case the TM symbol). I don't think there are too
many more examples like this. I'm still weeks away from finishing
the conversion (and validating all the code samples again.)

But I think I've preserved the semantic content of my document in
a simpler, easier to use set of tools.





