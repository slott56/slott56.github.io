Semantic Markup with Docutils Interpreted Text Roles
====================================================

:date: 2009-05-27 12:40
:tags: RST,#python,xml
:slug: 2009_05_27-semantic_markup_with_docutils_interpreted_text_roles
:category: Technologies
:status: published

A resume is a slippery thing -- a package of semi-structured data.

It has a kind of database-like feel to it, but there are so many
exceptions and special cases that the database never works out quite
the way you wanted.

For example, I've got -- essentially -- one employer over the past
30+ years.  But I've been on hundreds of projects for almost 100
different clients.  Since projects overlap, there's no tidy timeline.
The database has a token "Employer" table, a "Client" table, a
"Project", which is an association between "Client" and "Employer".
For each "Project" I can have a number of roles or positions.  Most
importantly, each project has a large number of hardware, software,
skill, language and other "features" to it.

Relax
-----

A more relaxed model is some kind of markup so that keywords can be
identified semantically and culled out to create tag clouds or
indices.

The usual culprit for mixed-content models like this is XML.  We
would define a DTD or XSD with our tags in a new namespace.  Sadly,
this also means that I have to rewrite my resume into XML.  Not that
bad, but still...

Can we do similarly detailed semantic markup in
`RST <http://docutils.sourceforge.net/docs/>`__?

What Role Does These Words Play?
---------------------------------

RST offers a flexible mechanism they called `Interpreted Text
Roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`__.
There are two parts to getting started with this.

1.  Name the role in a ``.. role:: name`` directive.

2.  Markup your content with ``:name:`words```.

By default, the role name is the class name that will be put into the
HTML <span> tag when the document is written in HTML.  If you want,
you can supply special formatting in addition to marking the words
with a role.

You can do considerably more with interpreted roles, but we'll look
at creating a tag cloud.

Gathering Data
--------------

The gathering part is easy.  You can snarf out the interpreted text
roles with a simple visitor-based design.

::

    import sys
    from collections import defaultdict
    from docutils.core import publish_doctree
    from docutils.nodes import SparseNodeVisitor

    class RoleVisitor( SparseNodeVisitor ):
        def __init__( self, role="skill", *args, **kw ):
            SparseNodeVisitor.__init__( self, *args, **kw )
            self.role= role
            self.cloud = defaultdict(int)
        def visit_inline( self, aNode ):
            if self.role in aNode['classes']:
                self.cloud[ aNode.astext() ] += 1


This visitor will accumulate a map with tag and frequency for a
given role.

We can parse the RST resume file and accumulate the tag cloud
statistics as follows.

::

    def tagFreq( aFile ):
        source= aFile.read()
        structure= publish_doctree( source )
        skills= RoleVisitor( "skill", structure)
        structure.walkabout(skills)
        return skills.cloud

Once we have the data we can emit a tag cloud.

Frequency to Font Size
----------------------

Converting frequencies to font sizes is a little alignment
exercise.   A clever page designer might have clever style names
based on the tag frequency.  I decided to name the styles after
the font-sizes, since that seems simple.

::

    def sizeMap( cloud ):
        """Many common tags piled into xx-large."""
        size_name = [ 'xx-small', 'x-small', 'small', 'medium', 'large',         'x-large', 'xx-large' ]
        freq=list(set(cloud.values()))
        offset = max( 0, (len(size_name)-len(freq))//2 )
        size_map= {}
        for sz, f in enumerate(sorted(freq)):
            size_map[f]= size_name[sz+offset]
            if sz <> "":
                #print size
        return size_name, size_map

This assigns all the words that occur just once to the smallest
font.  There are usually a large number of tags that occur just
once.  A few tags will have a large number of occurrences; these
will all wind up with 'xx-large' as their class.

Emitting The Cloud
------------------

Writing the tag cloud (in RST) looks this this.

::

    def rst( names, sizes, cloud, destination ):
        sys.stdout= destination
        for s in names:
            print "..  role::", s # The formatting roles that match our CSS.
            print "\n----------\n"
            for k in sorted(cloud):
                print ':%s:`%s`' % ( sizes[cloud[k]], k, )

We can then tack this cloud onto the end of the resume to get a
summary of skills, frameworks, OS's, languages and the like.

Style Points
------------

The docutils section on overriding the style sheet suggests we
include something like the following in the working directory.

resume.css

::

    @import url(html4css1.css);
    span.xx-small { font-size:0.65em; font-family:sans-serif }
    span.x-small { font-size:0.7em; font-family:sans-serif }
    span.small { font-size:0.85em; font-family:sans-serif }
    span.medium { font-size:1em; font-family:sans-serif }
    span.large { font-size:1.3em; font-family:sans-serif }
    span.x-large { font-size:1.6em; font-family:sans-serif }
    span.xx-large { font-size:1.9em; font-family:sans-serif }

We include this with the following command:
::

    rst2html.py --stylesheet-path=resume.css

Workflow
--------

This makes it much more pleasant to edit my resume.

1.  Make the changes.

2.  Run the tag-cloud script.

3.  Run rst2html.

Now I just have to remember to do it more often than once every
five years.





