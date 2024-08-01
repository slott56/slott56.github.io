The XML Balancing Act - Part III, JSON (Revised)
================================================

:date: 2007-01-29 15:03
:tags: xml
:slug: 2007_01_29-the_xml_balancing_act_part_iii_json_revised
:category: Technologies
:status: published





We have a spectrum of interesting needs, and a
corresponding spectrum of solutions.  Here's one dimension: the structured-ness view.

1.  Highly structured data.

#.  Semi-structured data, or the "mixed content model".
    We can further subdivide this into content which is "naturally"
    hierarchical, and a good fit for XML, and data which is relational and a poor
    fit.



Another dimension is the "imperative/declarative" dimension, which is orthogonal to the structured
dimension.  We've got, consequently, four easy-to-see kinds of data
representation needs:



..  csv-table::

    "Highly-Structured, Declarative","Highly-Structured, Imperative"
    "Semi-Structured, Declarative","Semi-Structured, Imperative"

    






Each of these is exemplified by different
languages in practice.  However, some people will argue that XML is appropriate
to all of them, practical considerations be d****d.



Highly-Structured, Declarative Data
-----------------------------------



This is the
sweet-spot for the relational model of data.  The representation for relational
data is a series of DDL statements (for the schema) and INSERT statements (for
the data).  JSON does this well; in some cases better. 

Better?



Let's look at an example.  Say
we have an application that needs to get the total of the most recent order for
a given customer.  In XML parlance, we have to locate ``<order>`` elements for
a given ``<customer>``, get the values of the ``<total>`` elements, and sum
them up.  This isn't a simple SELECT
SUM(total) FOR ORDER WHERE customer=?.  It's
complex, and the available XML API's don't support our application very directly
at all.



McGrath's point appears to be
that the API's support XML parsing, but not structured information processing. 
We can't just use something as clear as ``get_total_value()``, or even ``get_value('total')``.




If we have a complete DTD (or XSD),
then each piece of data has a tag, and each tag is reachable by an XPATH query. 
However, our application program API's aren't -- typically -- wordy XPATH
queries.  Our API's are simple object methods.  We can, of course, embed the
XPATH query in an object wrapper, but that seems to be a huge burden.  Couldn't
we match our data representation to our processing needs in the first
place?



Highly-Structured, Imperative Data
-----------------------------------



I thrashed around
in this space in "`Clarifying XML's Strengths <{filename}/blog/2007/01/2007_01_02-clarifying_xmls_strengths.rst>`_ ."
When there's imperative information (i.e., scripts) we're wandering away from XML's sweet
spot and wandering into a place where Python or a Domain-Specific Language (DSL)
might be more helpful.  While some people argue the fine points of Ant vs.
Maven, they seem to miss the point that Ant has imperative elements written in
Java and Maven has imperative elements written in Jelly.  Either way, we can't
do the whole job using highly structured
data.



If we were to try and use SQL or
some other highly-structured representation, we'd find ourselves deeply
compromised because we need some kind of scripting.  We can add stored
procedures to SQL, or we can use a more flexible data representation that
includes a procedural language.  Or, we can add super-flexible BLOB columns to
our database to contain Python code
fragments.



This mixture of structure
plus script is where the Python or JSON data representation seems to make a lot
of sense.  We can supplement this with some additional syntax to create a DSL
that includes Python, JavaScript or Jelly.  Fundamentally, we're matching our
processing with our data
representation.



Semi-Structured, Declarative
----------------------------



Here is the XML sweet-spot.  The data is a "mixed content" model with untagged text in addition
to tagged values.  Here, the XML API's aren't really in the way, because the
data requires some interpretation.  Some processing rules must be applied by an
application program.  



This is -- to some people -- anathema, because it implies that the XML document isn't complete
and stand-alone.  They prefer to think XML is inherently complete, and don't
want to consider the situation where XML lacks information required to interpret
the content.



Some people try to refine
this argument by saying that a DTD is incomplete, but an XSD is complete because
it has extensive rule declarations.  However, I'm saying something stronger than
the XML is incomplete.  I'm saying that essential knowledge is never captured in
the XSD.  I'm saying that processing rules are essential and are only captured
in the application software.  



Because
processing rules are essential, and are outside the XML, an XML document is
always incomplete, and has to be treated with the same respect that a shell
script (which requires a shell) and a SQL document (which requires a database)
are treated.  You must marry data and processing; further, the data
representation ought to be appropriate to the kind of processing which is being
done.



Hierarchies and Relations
-------------------------



We can further fine-tune
our semi-structured considerations.  Some data is naturally hierarchical; we can
create an outline from the information.  If it is perfectly hierarchical, we can
create a directed, acyclic graph, which is precisely what XML offers.




There is a spectrum of
hierarchical-ness.  Some data has a "preferred" hierarchy, but also has
cross-references.  The DocBook structure, for example, puts your content in the
book's hierarchy, but allows complex cross references among the topics.  Some
data, however, has multiple hierarchies -- because it's multi-dimensional -- and
there the XML world starts to fall
apart.



In a business example, it's
common to have project plans for multiple cost centers over multiple time
periods.  We have two complementary hierarchies: the organizational hierarchy of
the cost centers as well as the time periods.  Which is "right"?  Clearly, both
are relevant, and we can find people interested in both views of the same data. 
XML won't help.  Indeed, it can get in the way of processing this kind of
data.



Just to compound the problem,
this example has "project plans" which are often semi-structured.  So we don't
have a good XML fit, and we don't have a good relational fit, either.  At this
point, some kind of special-purpose DSL may help.  Or, we have to merely use the
XML to get the data into a proper object model for processing.  




Semi-Structured, Imperative
---------------------------



Wait, isn't semi-structured, imperative content the very features which characterizes a
programming language?  Yes.  We wouldn't want to switch Python's elegant syntax
for a pure XML rendering of the same application
programming.

::
    
    <name>n</name></arg> <name>m</name><default>0</default></arg> <function><name>round</name>
    
    <suite>
    
    <docstring><block>round(n[,m=0])
    -&gt; round n to m positions.
    </block><block>...</block>...
    </docstring>
    
    <statement name="if"><expression>...</expression><suite>...</suite></statement>
    
    <statement name="return"><expression>...</expression></statement>
    
    </suite>
    
    </function>
    


No thanks.



Bottom Line
------------



We need to select a data
representation that is appropriate for our data processing needs.  We can't
waste time wringing our hands and saying that there's no way to anticipate all
processing needs.  That's just hard-wringing for the sake of hand-wringing.  If
we're solving a specific problem, we should solve that problem, with an eye
toward related problems.  The question "Are there any unforeseen problems?" is a
tautology; it's always true, so there's no point in
asking.



The point is to identify the
problem, pick a solution, and choose appropriate data representation as well as
processing.  Over-generalizing (i.e., force-fitting XML to every problem) leads
to inefficient and ineffective solutions.  McGrath lifts up the specific issue
of finding a meaningful piece of data, rather than the value associated with a
tag obscured by an XPATH query.  



I've got an example of the obscurity created by XML:  "`Spreadsheet as Syntax <{filename}/blog/2007/01/2007_01_25-spreadsheet_as_syntax.rst>`_ " shows a multi-step
transformation, which includes transforming XML into a spreadsheet document
object model (SSDOM) before doing anything useful.  The raw XML is rather quite
complex and obscure.  The SSDOM isn't half as bad.  The SSDOM allows us to use a
simple ``get_style_name()`` notation to examine the content in a meaningful way.



Until I read McGrath's piece, I
didn't know why my solution appeared so clunky.  Now I see that it's a
consequence of the XML API's being focused merely on parsing.  What I did isn't
wrong or even clunky, it's essential.










