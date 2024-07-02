XML - Scripting - SQL - a DSL: which fits the problem better?
=============================================================

:date: 2006-12-31 04:46
:tags: xml
:slug: 2006_12_31-xml_scripting_sql_a_dsl_which_fits_the_problem_better
:category: Technologies
:status: published





I read "`Stamp on
the ants <http://koti.welho.com/jpakaste/blog/stamp_out_the_ants.html>`_ ", which lead me to write "`XML - One Ring to Rule them All... <{filename}/blog/2006/12/2006_12_23-xml_one_ring_to_rule_them_all.rst>`_ " because I'd
seem some remarkably lame justification for XML.  I saw an interesting response
in "`XML is first class, scripting languages are second
class <http://kontrawize.blogs.com/kontrawize/2006/12/xml_is_first_cl.html>`_ ".



At this point, we
have an interesting tangential problem with well-framed set of requirements and
candidate solutions:

-   We want a build system, like SCons.  This
    is the context for the conversation.  It's important to stick to solving a
    specific problem, not vague hand-waving about "better in general".

-   We want some additional features, not
    often provided by the build tool.  Examples include "... an HTML page showing
    the call sequence that you get for each target in the build", "...statistics,
    documentation, etc."



Note that we've
wandered a bit from the initial subject -- lame justification for XML -- and
moved into a compare-and-contrast between Ant and SCons.  This is probably not
the best consequence of the initial posting because we're on course for shoal
waters.  I'll press on and return to the potential ramifications, below.



What is a good approach for defining a build system that allows us to plug in this kind of extension or add-on?



XML
---



If we have an Ant-style XML database of targets, dependencies and actions, then
it's a matter of using XSLT to transform that database into a nice-looking
report.  XHTML is a fine output medium, and this can work well.  XSLT isn't fun
to write, but tools like `XML Spy <http://www.altova.com/products/xmlspy/xml_editor.html>`_  or `Open XML
Editor <http://www.philo.de/xmledit/>`_  make this at least
feasible.



In the case of XSLT
solutions, we're reforming the representation from one organization of XML tags
to another organization of  XML tags and content.  As long as the transformation
is largely positional, XSLT does a good enough job.  It isn't a pleasant way to
develop really complex algorithms, but most reporting doesn't involve anything
too complex.



If we need to do something
more complex, we have to understand the XML tags as something more than tags. 
We need to build internal objects that represent the targets, sources,
processing scripts and dependencies before any complex analysis can be done.  
We note that this internal representation is exactly the script-language
solution in SCons.



SQL
----



First,
there aren't a lot of database-centric build tools.  Traditionally, SQL
processing involved heavy-weight programming with client programs and database
servers.  With `SQLite <http://www.sqlite.org/>`_ , this heavyweight architecture is no
longer a necessary feature of a solution.  In this case, reporting is a snap: a
``SQL SELECT`` statement will -- generally -- produce the desired report.




Unfortunately, most build rules
involve transitive dependencies, and computing the complete transitive closure
in SQL is a pain in the ass.  Therefore, a more complex report requires a short
piece of programming to extract all of the transitive relationships into a
single "`hierarchy bridge table <http://www.google.com/search?q=hierarchy+bridge+table>`_ ".



An alternative is to
use `SQLAlchemy <http://www.sqlalchemy.org/>`_  or similar to do a pleasant
object-relational mapping.  This makes the SQL relational information into an
object representation of the targets, sources, processing scripts and
dependencies.   We note that this object representation is exactly the
script-language solution in
SCons.



Domain Specific Language (DSL)
------------------------------



The original `GNU Make <http://www.gnu.org/software/make/>`_  syntax is the DSL replaced by Ant's XML.
This isn't terribly difficult to parse, but lacks some of the nuanced expressive power of the newer
XML notation.  Writing a report from this isn't easy, either.  You have to read
it, parse it, analyze it to determine the relationships, and then write the
report.  Fairly icky, and more complex than XSLT or SQL.



Further, this involves creating an "internal" representation of the source information.  The DSL text
representation isn't very usable by itself:  reporting isn't simple XSLT-style
rewriting of the input file.  The DSL must be parsed into objects which
represent targets, sources, processing scripts and dependencies before any
useful analysis or reporting can be done.   We note that this internal
representation is exactly the script-language solution in
SCons.



Scripting Language (e.g. Python)
---------------------------------



At this point, it should be clear where this is headed.



The point of XML, SQL or a DSL is to put a persistent text representation around
objects which represent targets, sources, processing scripts and dependencies. 
SCons allows us to represent these objects in the Python language.  Since the
Python interpreter directly manipulates these objects, we don't have to do very
much additional work for reporting or other
analysis.



We have two choices for producing reports from SCons information.

1.  Extend the SCons framework (most likely the
    Node class) to add reporting methods to the object definitions.  We would then write a new main
    program, which (after loading the SCons control file) invoked the reporting
    methods.  Some of this may already be present in the ``Node.explain()`` method.

#.  Create a subclass of the SCons ``Visitor`` which
    produces the desired report.  We would then write a new main program, which
    (after loading the SCons control file) creates our new ``Visitor`` subclass and executes it.
    


Compare and Contrast
---------------------



For XML, we have XSLT as a query language and Xalan to interpret the XSLT program.



For SQL, we have the ``SELECT`` statement.
We can use our desired database (SQLite, for example) to interpret
the SQL program, producing the output.



For a DSL, we generally don't
have much in the line of query and reporting tools.  We have to write
everything, and this is generally ineffective.



For Python and SCons, the
build control file is -- in effect -- an application program.  Reporting is just
another method or another subclass of Visitor.  The build control file and the
reporting feature of the build system are really just one extended
thing.



Consequences
-------------



Here's where the shoal water lies: there aren't any real consequences.  Many (too many)
people assume that the consequence of a compare-and-contrast is that
**One is Best, All Others Are Bad**\ ™.  This conclusion further implies
that everyone with the Non-Best solution should do an
**Immediate Upgrade**\ ™ to the One Best Solution.




You often hear the following:
"If your solution is so much better why doesn't everyone use it?"
Or, even worse, "If you agree that my solution is better than yours, you should immediately convert
to my solution."



The idea that **Everyone Must Adopt the Best Solution**  is wrong because politics trumps
technology.  A good technical solution is often a political non-starter.  VHS
was a lousy format for video tapes, and Beta was superior in every technical
aspect.  Yet, VHS was preferred by consumers.  The preference was non-technical;
"political" for lack of a better word.  Windows is largely a dreadful operating
system; yet there it is.



There's no reason to abandon Ant.  It's a close second to SCons.  What is important is to
have a *good* reason for using Ant, not one of the *lame* reasons I cataloged
in "`XML - One Ring to Rule them All... <{filename}/blog/2006/12/2006_12_23-xml_one_ring_to_rule_them_all.rst>`_ ".



What then is the value of this kind of compare-and-contrast?  Locating the right reason for using
XML.  If it's political, say so.  Don't make up lame reasons.  Understand the real reasons.












