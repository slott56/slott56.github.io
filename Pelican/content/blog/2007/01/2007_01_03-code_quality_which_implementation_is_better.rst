Code Quality - Which Implementation is "Better"?
================================================

:date: 2007-01-03 11:39
:tags: architecture,design,complexity
:slug: 2007_01_03-code_quality_which_implementation_is_better
:category: Architecture & Design
:status: published





To begin with, we're talking about the
implementation's source code.  Here's the situation: Ann says that Bob's code is
no good, and she's provided an alternative implementation.  How do we
choose?



The first part of any scorecard
is the `SEI Quality Measures Taxonomy <http://www.sei.cmu.edu/str/taxonomies/view_qm.html>`_ .  It's marked
"Legacy", but I haven't seen anything as good or complete to replace
it.



There are five top-level categories
on which you can evaluate any implementation.  Actual numeric scores for these
are hard to come by, since they don't all have units and measurement instruments
defined.  However, you can use subjective scores.  More importantly, these
topics focus the conversation around useful quality
attributes.



Here are the five top-level
categories:

-   Need Satisfaction.  In short, does it
    work?  Does it solve the problem in the first place?

-   Performance.  Here is where the classical
    memory and time considerations are evaluated.

-   Maintenance.  How easy is it to
    fix?

-   Adaptive.  How easy is it to extend or
    port?

-   Organizational.  How expensive is it?  Do
    we have the skills?



The SEI taxonomy
has 16 subcategories, enough to cover all the bases.  For me, this is the final
word on quality, and I haven't seen anything better than
this.



**Understandability.** 



Under
"Maintenance", there's a subcategory of "Understandability", which includes four
lower-level metrics:

-   Complexity

-   Simplicity

-   Structuredness

-   Readability



This "Understanability"
group is so important that we need to pull it out and evaluate it by itself. 
The SEI information directs us to a "`Maintainability Index <http://www.sei.cmu.edu/str/descriptions/mitmpm.html>`_ " technique that combines a
number of metrics.  Detailed values are a pain to gather because they involve
parsing the source code, something that isn't very quick or easy to do. 




On the other hand, an informal survey
of the source can be done using the following techniques.  These aren't the
official numbers, but they're a way to have a useful conversation about which
implementation is "better".  They provide a workable definition of
"understandable" that -- to an extent -- is free from subjective complaints
about someone else's coding style.

-   Halstead Length = total number of
    variable occurrences plus total number of method calls, operators, and (in
    Python) function calls.  How long is the component, not in lines of code, but in
    things the program represents and things the program does?

-   Halstead Volume = number of
    *distinct* 
    variables plus
    *distinct* 
    methods, operators and functions.  Often a much smaller number than the length. 
    This is "volume" in the sense of how many distinct things do you have to keep in
    your head to understand it; it's the brain volume tied up in working on the
    program.

-   McCabe Complexity = number of nested
    **if** ,
    **while** 
    and **for** 
    statements.  In the case of Python
    **elif** 
    constructs, these count, also.  Statements at the "top-level" of a method or
    function don't count, only the nested ones.  Yes, you can finesse this score to
    zero with a lot of small methods, that would be the whole point.

-   Total source lines of code.  If you want,
    you can segregate comments from non-comments.  Python and Java programmers have
    three categories: the Javadoc (or docstring) comments, the "other" comments, and
    the remaining code.  The Javadoc (or docstring) comments have to be taken as
    seriously as the code itself.



These can
be combined into a single score, but that defeats the purpose of looking at the
code and evaluating it based on the textual complexity (the Halstead metrics)
and the structural complexity (the McCabe)
metric.



**The Evils of If-Statements.** 



I find that my own
quick-and-dirty McCabe metric works well in evaluating complex.  I count
**if** -statements.
In my experience, little good comes from
**if** -statements.
Each one needs to be scrutinized carefully and justified as essential. 




Generally, every one of the cool
design patterns in the *Design Patterns: Elements of Reusable Object-Oriented Software* 
book can be replaced with an amazingly poor cluster of rotten, unmanageable
**if** -statements.
In particular,
**State** ,
**Command** 
and
**Strategy** 
are often bollixed up into a horrifying morass of
iffiness.



Here's the
conversation:



**Customer** :
"Make it do 'X', not 'Y', in this
situation."

**Me** :
"What does that mean?  Why is this situation
unique?"

**Customer** :
"That doesn't matter; there's no underlying meaning.  It's just an
**if** -statement."



Everything
has meaning.  There's no such thing as "just an
**if** -statement".
Generally, the things we think of as "conditions" are not last-minute decisions
in the middle of an algorithm.  They are starting conditions that describe what
objects we should be created in the first place.  Most
**if** -statements
belong in some sort of
**Factory** 
or
**Builder** :
they have deep and pervasive meaning.




















