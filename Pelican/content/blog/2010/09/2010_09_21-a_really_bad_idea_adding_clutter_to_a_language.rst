A Really Bad Idea -- Adding Clutter to A Language
=================================================

:date: 2010-09-21 08:00
:tags: configuration management,#python
:slug: 2010_09_21-a_really_bad_idea_adding_clutter_to_a_language
:category: Technologies
:status: published

A DBA suggested that I read up on "Practical API Design: Confessions of
a Java Framework Architect".

Apparently the DBA had read the phrase "direct compiler support of
versioning of APIs" in a review of the book and -- immediately --
become terribly confused.

I can see why a DBA would be confused. From a DBA's point of view all
data, all processing and all management-- all of it -- is intimately
tied to a single tool. The idea behind **Big Relational** is to
conflate configuration management, quality assurance, programming and
the persistent data so that the product is inescapable.

    [The idea is so pervasive that not using the RDBMS has to be called a
    "movement", as in "NoSQL Movement". It's not a new idea -- it's `old
    wine in new
    bottles <{filename}/blog/2010/10/2010_10_18-nosql_old_wine_new_bottle.rst>`__
    -- but Big Relational has become so pervasive that avoiding the
    database makes some folks feel like renegades.]

Adding to the confusion is the reality that DBA's live in a world
where version management is difficult. What is an API version number
when applied to the database? Can a table have a version? Can a
schema have a version?

    [IMO, the answer is yes, database designs -- metadata -- can easily
    be versioned. There's no support in the database product. But it's
    easy to do with simple naming conventions.]

For a DBA -- who's mind-set is often twisted into "one product
hegemony" and "versioning is hard" -- the phrase "direct compiler
support of versioning of APIs" maps to "direct
tool/database/everything support of versioning." Nirvana.

All Things in Moderation
------------------------

A relevant quote from the book is much more sensible than this
fragment of a review. "Some parts of the solution should be in the
compiler, or at least reflected in the sources, and processed by some
annotation processor later."

API versioning is not a good idea for adding to a programming
language. At all. It's entirely a management discipline. There's no
sensible avenue for "language" support of versioning. It can make
sense to carry version information in the source, via annotations or
comments. But to augment a language to support management can't work
out well in the long run.

Why not?

**Rule 1. Programming Languages are Turing Complete. And Nothing More**. Syntactic sugar is okay, if it can be proven to be built on
the Turing complete core language. Extra "features" like version
control are well outside the minimal set of features required to be
Turing complete. So far outside that they make a completeness proof
hard because there's this extra stuff that doesn't matter to the
proof.

Therefore: **Don't Add Features**. The language is the language. Add
features via a toolset or a annotation processor or somewhere else.
Your API revision junk will only make the proof of completeness that
much more complex; and the proof won't touch the "features".

**Rule 2. Today's Management Practice is Only A Fad**. Version
numbering for API's with a string of
*Major*.\ *Minor*.\ *Release*.\ *Patch* is simply a trendy fad. No
one seems to have a consistent understanding of what those numbers
*mean*. Further, some tools (like subversion) simply using
monotonically increasing numbers -- no dots.

Someday, someone will come up with an XML Feature Summary (XFS) for
describing features and aspects of the the API, and numbers will be
dropped as uselessly vague and replaced with a complex namespace of
features and feature enumeration and a URI referencing an RDF that
identifies the feature set. Numbers will be replaced with URI's.

Therefore: **Don't Canonize Today's Management Practice in the Language**. When the current practice has faded from memory, we don't
want to have to retool our programming languages.

What To Do?
-----------

What we do for API version control is -- well -- hard work.
Annotations are good. A tool that scrapes out the annotations to
create a "profile" of the API might be handy.

In Python (and other dynamic languages) it's a much simpler problem
than it is in static languages like Java and C++. Indeed, API version
management may be one of the reasons for the slow shift from static
to dynamic languages.

If we try to fold in complex language features for API version
support, we introduce bugs and problems. Then -- when management
practice drifts to a new way of handling API's -- we're stuck with
bad language features. We can't simply deprecate them, we have to
find a new language that has similar syntax, but lacks the old-bad
API management features.

Distutils
---------

Python `distutils <http://docs.python.org/distutils/setupscript.html>`__ has
a nice "Requires", "Provides" and "Obsoletes" specification that's
part of the installation script. This is a handy level of automation:
the unit of configuration management (the module) is identified at a
high level using simple numbers. More than this is probably
ill-advised.

And -- of course -- this isn't part of the Python language. It's just
a tool.





