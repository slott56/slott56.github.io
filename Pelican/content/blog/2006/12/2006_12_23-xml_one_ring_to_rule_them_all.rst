XML - One Ring to Rule them All...
==================================

:date: 2006-12-23 17:43
:tags: xml
:slug: 2006_12_23-xml_one_ring_to_rule_them_all
:category: Technologies
:status: published





The XML folks seem to have a number of
points:

-   Ant already works.   Complexity be damned.

-   XML is fine for everything that's not Java.  Except SQL.  And CSS.

-   Ant is "already" part of the technology stack, and it uses XML.  Anything better isn't already there.

-   Everyone already knows XML.  They can't learn anything new.
    Learning something simpler is the same as learning something new: impossible.

-   XML is established.  New technology isn't established.

-   Scripting doesn't add value.  If you need scripts, write them in XML or Java.

-   I already know XML.   Something simpler no longer helps.

-   A bad non-XML solution is worse than any XML solution.
    XML will never become an opaque legacy technology.



I think the above summarizes the value proposition for XML-based Ant as a build tool.
The point against Ant and XML was repeated many times and in many slightly different forms:



    "Wouldn't be nice to have an higher level way to describe an application build, instead of just working at
    the assembler level ?

    Something like
    being able to describe what a module is (for my application), what a deliverable
    is, what a release is, etc etc ?"



The Value of a DSL
------------------



This seems to be the key point: DSL's work because they force us to do two things.

-   Define the objective.

-   Define a language which describes the
    objective succinctly and clearly.



In many cases, the "objective" is a combination of static definitions and dynamic
actions.  That sounds completely congruent with object-oriented programming. 
Since we often need flexibility in our implementation, that sounds like
object-oriented scripting.



I'm completely enamored of tools like `SCons <http://www.scons.org/>`_   where I can use a fairly
natural-like language, not an opaque and artificial language.  `SMK <http://home.gna.org/smk/>`_  is cut from
the same cloth.  Your dependencies, actions, repositories, targets, etc., are
first-class objects.  Your configuration file simply populates those objects in
a handy, clear notation like Python.  Your desired actions emerge from the
interactions of the object's methods.



While XML is a theoretical
equivalent, it's natural opacity makes it a poor choice for anything that will
be touched by people.



Design Goal 6
-------------



The XML standard has the
following goal: "XML documents should be human-legible and reasonably clear."  
There are issues, however.



Documents
fit on a spectrum from sparsely marked up to entirely symbolic.  A sparsely
marked up document is mostly natural language.  This end of the spectrum has
text-heavy HTML pages and most DocBook documents.  In this case, a little XML
goes a long way, and helps clarify the semantics as well as the structure of a
document.



The symbolic documents
include music, mathematical notation and most programming-related text.  Music
is backed by a mountain of convention and required training: it isn't
self-explanatory.  However, many nuances of placement on the page, font, etc.,
have deep meanings.  Music notation is essentially all markup and very few
non-markup natural language elements.



Mathematical formulas,
similarly, are an artificial language.  Notation schemes like `mathml <http://www.w3.org/Math/>`_  reveal
that there's tons of deeply meaningful typography to mathematics.  Capturing
this reveals that XML is rather clumsy.  The natural language elements are
single letters and numbers.  When we compare that with a DSL like `AMS
LaTeX <http://www.ams.org/tex/amslatex.html>`_ , it looks like a DSL captures meaning more succinctly and
clearly.



Programming is somewhere in
the middle of this spectrum.  A program doesn't have to be as densely packed
with meaning as a mathematical formula, although it can be.  In some cases,
mathematical terseness is a virtue.  Often a program is a tool for knowledge
capture, and the natural language explication in comments and names is essential
to the value being
created.



XML's Strong Suit
-----------------



The best place for XML is
it's historical place:  adding semantic and structural content to natural
language documents.  As web transport, it's fine.  Of course, it is usually
nested in **yet another**  markup language.  Most XML winds up
packaged in `MIME <http://www.faqs.org/rfcs/rfc2045.html>`_   markup.  Note that XML markup gets wrapped
in MIME markup: XML isn't a one-size-fits-all markup language.  It's just one of
many tools.



The worst place for XML is
in places where the meaning is complex and deeply symbolic.  When there is
little or no need for natural language, XML is large overhead for limited
value.


















