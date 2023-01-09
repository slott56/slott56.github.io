Clarifying XML's Strengths.
===========================

:date: 2007-01-02 15:55
:tags: technologies,xml
:slug: 2007_01_02-clarifying_xmls_strengths
:category: Technologies
:status: published





While there are lame reasons for using XML, there
are good reasons also.  The good reasons, however, aren't delightfully clear. 
They seem to be clouded by the lame issues.  I'm trying to sort out the best and
most logical reasons for using
XML.



Here are 8 typically lame reasons
for using XML.  The "`Stamp
on the ants <http://koti.welho.com/jpakaste/blog/stamp_out_the_ants.html%22%20target=%22NewWindow>`_ " posting noted this exchange in The Server Side, "`Raven
1.1: Build Java with Ruby <http://www.theserverside.com/news/thread.tss?thread_id=42923%22%20target=%22NewWindow>`_ " thread.  Note that this is confined to
build tools, where scripted actions are an integral part of the problem.  A lot
of this discussion doesn't apply to other problem domains.

-   Ant already works.   Complexity be
    damned.

-   XML is fine for everything that's not
    Java.  Except SQL.  And CSS.

-   Ant is "already" part of the technology
    stack, and it uses XML.  Anything better isn't already there. 

-   Everyone already knows XML.  They can't
    learning anything new.  Learning something simpler is the same as learning
    something new: impossible.

-   XML is established.  New technology isn't
    established.

-   Scripting doesn't add value.  If you need
    scripts, write them in XML or Java.

-   I already know XML.   Something simpler
    no longer helps.

-   A bad non-XML solution is worse than any
    XML solution.  XML will never become an opaque legacy
    technology.



I found these to be typical
of many technology decisions:
**Incumbency** ,
**False Dichotomies** ,
**Inflated Opportunity Cost** , a flat-out
**Misrepresentation** 
are the essence of these arguments for
XML.



There is, however, a good value
proposition for XML, even in the build-tool domain where scripting is an
essential part of the problem and any solution.  In "`A Good Reason for XML <{filename}/blog/2006/12/2006_12_28-a_good_reason_for_xml.rst>`_ ", I tried to state it as
"Semantic Richness", that is, "how well it describes the problem."  This isn't
really very good, and another comment challenged this glib
simplification.



**Declarative vs. Imperative Knowledge Representation.** 



The big issue in
software-world is knowledge representation.  Ant or SCons have some
sophistication because they have two levels of knowledge representation: a
collection of algorithms plus a control file that is used by those algorithms. 
Generally, we capture knowledge about building a program and represent it in the
control file.  We don't tinker much with the knowledge embodied in the
algorithms.



We have two strategies for
knowledge representation:
*declarative* 
and
*imperative* .
This is sometimes called the "What vs. How" distinction.  We can declare what we
want -- the desired end-state -- and leave it to our collection of algorithms to
reason out how it gets done; the tool derives the imperative steps to get there.
Or, we can just write down how to do the job; we manually develop the imperative
steps.



The first build systems were
purely imperative: we recompiled the world.  This was, often, an ineffective use
of precious computing resources, so we invented more sophisticated tools.  I
implemented one back in the early '80's that ran in Univac's Exec-8, using
really ancient and obscure software tools.  The purpose then -- as it is now --
is to recompile just enough and no
more.



`GNU
Make <http://www.gnu.org/software/make/>`_ , `Ant <http://ant.apache.org/>`_ , `SCons <http://www.scons.org/>`_ , `Raven <http://raven.rubyforge.org/>`_ , `Maven <http://maven.apache.org/>`_ , etc., have two explicit purposes: to
minimize recompilation, and automate the myriad of packaging steps required by
our deployment architectures.  They have grown, however to embrace an additional
requirement: represent metadata about the software being built.  This additional
requirement is captured in "`XML is first class, scripting languages are second
class <http://kontrawize.blogs.com/kontrawize/2006/12/xml_is_first_cl.html>`_ ".  How do we report or analyze the information captured in our
build tools?



**The Preference for Declarative Knowledge.** 



Declarative
knowledge representation is, clearly, preferred.  "Imperative tools (whether
based on XML ala Ant or a "real" scripting language ala Raven) are inevitably
going to be less productive than a declarative tool..."  This is also an
implication in the "`XML is first class <http://kontrawize.blogs.com/kontrawize/2006/12/xml_is_first_cl.html>`_ " response.




The declarative style has a number of
advantages.  Primarily, it allows us to analyze the declarations to create
reports about our application software.  Since the job is information capture,
we have every reason to demand full value from that knowledge.  Also, a
declarative style can allow swapping the toolset without breaking the declared
relationships in the build configuration
file.



This declarative ideal can be met
a number of ways:

-   **Ant or Maven (XML).**   Typically mostly declarative, because
    it isn't much of a scripting language.  When we use a tool like `Jelly <http://jakarta.apache.org/commons/jelly/>`_ , as Maven does, then it isn't
    **purely** 
    declarative.  The existence of Jelly adds imperative knowledge to a declarative
    knowledge.

-   **SQL.**   Purely declarative.  Most RDBMS vendors
    have added imperative components: triggers, stored procedures, etc.  But,
    lacking these extensions, `SQLite <http://www.sqlite.org/>`_  meets the declarative idea.  It isn't
    however, much used for this sort of thing.  Who wants to code their sources,
    targets and processing steps as a bunch of SQL
    INSERT
    statements.

-   **GNU Make (DSL).**   Less declarative than others.  GNU
    Make, specifically, allows extensive shell script programming.  For this reason,
    a makefile can
    become a painful morass of scripts rather than a tidy definition of what should
    be done.  With some work, a more-or-less purely declarative
    makefile can be
    built.  However, this is difficult to analyze and write reports.  GNU Make
    control files tend to be dominated by scripts, however, because it's often
    simpler than writing a complete declarative control file.

-   **SCons (Python).**   Mostly declarative.  In SCons, the
    bulk of the control file is purely declarative.  Scripting, rather than being in
    some additional language like Jelly, we simply use Python for any
    non-declarative features.



**Murky Ant vs. Maven Issue.** 



While
declarative knowledge has all the advantages, here's an interesting quote:
"Imperative tools (whether based on XML ala Ant or a "real" scripting language
ala Raven) are inevitably going to be less productive than a declarative tool,
and this was a large part of the reason I switched from Ant to Maven some years
ago."  This is a bit confusing.



This
quote sounds like Ant is more imperative than Maven, and therefore less
desirable.   However, I'm confused because of the following:

-   Ant and Maven both use XML, which is
    largely declarative.

-   Maven has Jelly, which adds imperative
    features.



If anything, I'd think that
Maven would be
*less* 
declarative.  Clearly, I'm missing something.  Likely, I don't understand enough
of the DTD (or Schema) for Maven to see how it is more declarative in spite of
the inclusion of Jelly.



**Bottom Line.** 



It's clear that purely
declarative knowledge is ideal.  It's also just as clear that imperative
knowledge is essential to success. 




Interestingly, build systems seem to
typify applications that can't be done as purely declarative knowledge.  We're
always adding imperative hooks to control files.  Purely imperative knowledge
(e.g., a shell script) are
undesirable.



Further, the more we look,
the more we see different mixtures of declarative vs. imperative knowledge
representation techniques.  XML is imperative light (even with jelly),
Python/SCons is declarative with easy addition of imperative scripts, the
GNU/Make DSL is imperative heavy.



The
Ant vs. Maven distinction still needs some clarification.  However, the
preference for a declarative knowledge representation makes compelling sense. 
XML's best for representing declarative knowledge.






















