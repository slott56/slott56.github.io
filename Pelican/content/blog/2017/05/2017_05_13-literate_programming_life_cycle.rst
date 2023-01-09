Literate Programming Life Cycle
===============================

:date: 2017-05-13 10:11
:tags: #python,F#,literate programming
:slug: 2017_05_13-literate_programming_life_cycle
:category: Technologies
:status: published

The question is a deep one. What is the Literate Programming Life
Cycle? Why is it so difficult? What are the three barriers and how do
we cross them?


Here's most of the original question.


  "Last week I threw together an F# script to parse markdown-style
  text into one or more F# files.

  "The thing is, nearly all the references I can find online talk
  about the finished article, but not the design process. Obviously
  for my first attempt, I necessarily had to start out by writing
  the F#, then writing the document with embedded code afterwards.
  But now I’ve got that working, I have difficulty working out how
  the ongoing development process actually works. Currently only
  having a text editor with no colour coding, then having to
  ‘compile’ my markdown to code, then compile my code to test it,
  all seems like too much hard work, and the temptation is just hack
  the code directly.

  "Given that I imagine the python development process is similar to
  F#, I wondered what your experience is with the hack/test/finalise
  development cycle."


**Some Background**

http://www.tug.org/TUGboat/Articles/tb13-3/childs.pdf


Also, this quote from the discussion on `Lambda the
Ulimate <http://lambda-the-ultimate.org/node/3663#comment-51878>`__.

  
     "The issue of literate programming is an issue of writing a
     program
     that LIVES rather than writing a program that WORKS. In a
     commercial
     setting you pay to train new people on programs but in an open
     source setting there is no training. ..."

  
     "... But if your program needs to live forever then you
     really need literate code."


Recently, I did some major overhauls of two literate programming
exercises. I revised the `pyWeb
tool <http://pywebtool.sourceforge.net/>`__ to better handle LaTeX
output, as well as add unit tests and -- consequently -- fix some
long-standing problems. Also, I revised the `COBOL
DDE <http://cobol-dde.sourceforge.net/>`__ parser to better handle
numeric data, replace the old FixedPoint module with Decimal, add
unit tests and -- of course -- fix other bugs that showed up.


Based on my recent experience, I have some advice on "Full
Life-Cycle Literate Programming".


**A Life Cycle**


In order to identify the barriers, we need to look at the
deliverables and the software development life cycle that produces
those deliverables. Let's break the software development
life-cycle down as follows.


-  New Development
-  Maintenance
-  Adaptation


We'll presume that each of these efforts includes some elaboration
of requirements, some design, and some transition to operational
use. We only care about the coding part of the job, so we're not
going to dwell on all of the other activities that are part of
Application Life Cycle Management.


The question is about that transition from New Development to
Maintenance or Adaptation. Doing new development seems somehow
easier than maintenance or adaptation. How do we work with an
established Literate Program?


**New Development**


New Development of a program is always a delicate subject. We have
an explicit goal of creating some deliverable. We'll look at the
deliverables next. First, we'll look at the conflicting forces
that must be balanced.


#.  It must satisfy the need. There are requirements for the
    program's behavior, interfaces and implementation. Above all it
    must work.

#.  It must use appropriate resources. The data structures and
    algorithms must reflect sensible engineering choices. There's
    no call for "micro-optimization" of each silly piece of syntax.
    However, the algorithm's (and data structures) should be
    minimized.

#.  It must be adaptable.

#.  It must be maintainable.

#.  It must meet other organizational needs like cost,
    time-to-develop, language and toolset, infrastructure
    requirements, etc.


One can maximize one at the expense of others. For instance, one
can reduce development costs to the minimum by creating a mess
that's neither adaptable nor maintainable. Indeed, one can create
software very cheaply if one starts relaxing functional
requirements. Software that doesn't work well can be very cheap to
create.


**Forward vs. Reverse Literate Programming**


As a digression, we'll note that some folks recognize two broad
approaches to literate programming (LP). This isn't the whole
story, however. Ordinary LP encourages the author to create a
document that contains and explains working software. A simple
tool extracts a nice final publication-ready document and working
code from the author's original source document.


`Reverse LP <http://www.ssw.uni-linz.ac.at/Research/Projects/RevLitProg/>`__
is the technique used by tools like JavaDoc, Sphinx, Epydoc,
DOxygen. This usually takes the form of detailed API
documentation, but it can be richer than simply the API's. In this
case, comments in the source code are extracted to create the
final publication-ready document. In Sphinx the author uses a
mixture of source code plus external text to create final
documentation. This isn't as interesting, since the resulting
document can't easily contain the entire source.


We can assign the retronym "Forward Literate Programming" to
ordinary LP to distinguish it from Reverse LP.


**Code-First Literate Programming**


There's an apparent distinction between two variations on the
Forward LP theme: Document-First and Code-First LP. In
Document-First, we aspire to a noble ideal of writing the document
and the code from first principles, from scratch, "*de novo*",
starting with a blank page. The code-first approach, on the other
hand, refactors working code is into a literate programming
document.


One can argue that code-first refactoring is A Bad Thing™ and
subverts the intent of literate programming. The argument is that
one should think the program through carefully, and the resulting
document should be a tidy explanation of the development of the
ideas leading to the working software.


However, Knuth's analysis of "The original Crowther/Woods
Adventure game, Version 1.0, translated into CWEB form" (at
`ADVENT <http://www-cs-faculty.stanford.edu/~uno/programs/advent.w.gz>`__)
shows that even ancient Fortran code can be carefully analyzed and
retro-actively transformed into a piece of literature.


Working forward -- starting with a blank sheet of paper -- isn't
always the best approach. The bad ideas and dead-ends don't belong
in that explanation. All of the erasing and rewriting should be
left out of the LP document. This means that the document should
really focus on the final, working, completed code. Not the
process of arriving at the code. Why start with a blank page? Why
not start with the code?


In short, code-first LP isn't *wrong*. Indeed, it isn't even a
useful distinction. If the resulting document (a) contains the
entire source and (b) stands as piece of well-written description,
then the literate programming mandate has been satisfied.


**Center of Balance**


Literate Programming strikes a balance among the various
development forces. It emphasizes working software with abundant
documentation. It does not emphasize the short-term cost to
develop. It does, however, emphasize the long-term value that's
created.


Interestingly, the idea is to minimize the labor involved in
creating and maintaining this documentation. To some folks, it
seems odd that all that writing would somehow be "minimal".
Consider the alternative, however.


We can try to create software and documentation *separately*,
claiming it's somehow easier. First, we write the software, since
that's the only deliverable that matters. Second, we slap on some
extra documentation, since only the software really matters. While
satisfying in some respects, most folks find -- in the long run --
that this is unworkable. They often diverge.


**When the code and the comments disagree, probably both are
wrong.**


The goal of LP is to prevent this.


Literate Programming seems like a lot of work. But it's work we
have to do anyway. And a non-literate approach is simply *more*
work. Almost any approach that seems to create software "quickly"
doesn't create any enduring value. Why not?


**The Deliverables**


The point of **all** software development is to create a two-part
deliverable.


-  The working software
-  Some supporting justification or reason for trusting the software


The justification can take several forms: test results, formal
proof, API Documentation ("Reverse Literate Programming"), an
explanation (separate from the code) or a Literate Programming
document.


In many cases, our customers want most of the above. Folks
don't expect a formal proof, but they often demand everything
else.


Claiming that the software can exist *without the supporting
justification* is to reduce software development to a hobby.
The worst-run of amateur software development organizations do
tolerate a piece of software without a single test or scrap of
documentation. That only proves the point: if your organization
tolerates junk software without supporting documentation, it's
one of the worst-run of organizations; feel free to quit.


The point of LP is to create the software (and supporting
documents) from a single LP source document. LP seeks to
*minimize* the effort required to create software with
supporting documentation that actually matches the software.


I'll emphasize that.


**Literate Programming seeks to minimize the effort required to
create software with supporting documentation**


If we have to produce software, tests and explanations, clearly
it is simpler to have a single source file which emits all of
that stuff in a coherent, easy-to-follow format. While it's
clearly simpler, there are some barriers to be overcome.


**If It's So Much Easier... ?**


The Jon Bentley issue with LP is that it doesn't feel easier to
write a coherent document because we aren't all good writers.
Bentley notes that there are good writers and good programmers
and that some folks are not members of both sets. I think this
misses the point. We're going to produce documentation, no
matter how good a writer we are.


Most people do not see LP as simpler. They see it as a lot of
work. Weirdly, it's work they already do, but they choose to
keep the program and the explanation separate from each other,
making it *more* work to keep them in synch. I can see why they
claim it's more work.


If it's easier to do this in one document, why doesn't everyone
simply create a literate program?


Generally, we've got three kinds of barriers that make Literate
Programming hard. First, the tools at our disposal don't really
support an LP kind of development effort. We get very used to
intelligent syntax coloring and code folding. We find tools
which lack these features to be harder to use. Second, we're
working in multiple languages in a single document. Finally, it
takes some experience to get settled into an LP mode.


**The Tool Barrier**


The first of the barriers to effective literate programming is
the tool pipeline. The complaint is that "having to ‘compile’
my markdown to code, then compile my code to test it, all seems
like too much hard work".


This is interesting, but specious. The multi-step process is
what `scons <http://www.scons.org/>`__, make,
`ant <http://ant.apache.org/>`__ and
`maven <http://maven.apache.org/>`__ are for. A simple
SConstruct file will handle web, weave, publication,
compilation and unit test in a single smooth motion.


There are a lot of tools involved in literate programming.
We've introduced an additional markup language into the mix,
creating additional steps. This isn't any more complex than
working with any compiled language. We often forget that the C
compiler is really a multi-stage pipeline. Our LP tools --
similarly -- are multi-stage pipelines.


Also, for Python and F# programmers, there's something else
that Seems Very Important™. It isn't. F# and Python have
console interfaces (sometimes called the Read Evaluate Print
Loop, REPL); this clutters up the problem with an irrelevant
detail. Console hacking is helpful, but it isn't literate and
it's barely programming.


**The Language Barrier**


In addition the tool barrier, we also have a language barrier.
When we're doing literate programming we're working in at least
three different languages concurrently. This makes our life
seem difficult.


-   **Literate Programming Markup**. This might be CWEB, pyWeb
    or any of a number of LP markup systems.

-   **Target Document Markup**. This might be LaTeX, RST,
    Markdown, DocBook XML or some other markup.

-   **Target Programming Languages**. For classic, Knuth-style
    projects, there's only a single language. However, for many
    projects this will not be a single language. For example, in
    a web environment, we'll have program source, SQL, HTML,
    CSS, and possibly other languages thrown in.


It's difficult to sort this out from an IDE's perspective. How
to handle syntax highlighting and code coloring? How to handle
code folding and indexing the document as presented?


The old-school techniques of decomposing a big document into
small sections still applies to literate programming. The
document sections do not in any way correspond with the final
program source, making the LP document tree far, far easier to
work with.


**The Mental Barrier**


The final barrier is entirely mental. This is really one of
experience and expectation.


It's hard -- really hard -- to step back from the code and ask
"What's this *mean*?" and "How would I explain it?"


Too often, we see a problem, we know the code, and we
understand the fix -- as code. This is a skill as well as a
habit we build up. It's not the best habit because the meaning
and explanatory power can be ignored or misplaced.


Stepping back from the code seems slow. "It's a one-line change
with a 10-paragraph explanation!" developers gripe. "I could
make the change now or spend hours explaining the change to
you. The value is in making the change and putting it into
production."


And that's potentially wrong.


Only a very small part of the a developer's value is the code
change itself. If code will be in production for decades (my
personal best is 17 years in production) then the 10-paragraph
explanation will -- over the life of the software -- be worth
it's weight in gold. A one line fix may actually be a
liability, not an asset.


**Solid Approach**


I think the approach has to be the following.


#.  Create a Spike Solution. Something that works, is
    incomplete, but shows the core approach, algorithms and data
    structures.

#.  Outline the next more complete solution using LP tools. The
    component structure, the logical model, the basics of the
    first sprint.

#.  Create a **publication pipeline** to process the LP source
    into document, code and tests, and run the test suite. A
    kind of the Continuous Integration daily build. This is
    easily a double-clickable script, or "tool" in an IDE.

#.  Fill in the code, the unit tests, and the necessary
    packaging and release stuff. Follow TDD practices, writing
    unit tests and code in that order. What's cool is being able
    to write about them side-by-side, even though the unit tests
    are kept separate from the deliverable code in the build
    area.

#.  Review the final document for it's explanatory power.


Consider a number of things we do in comments that are
better done outside the comments.


-  TODO lists. We often write special TODO comments. These
   can go in the proper Literate Programming text, not in
   the code.

-  Code samples. In JavaDocs, particularly, sample code
   isn't fun because of the volume of markup required. LP
   code samples are just more code; you can make them part
   of small "demo" or "test" structures that actually
   compile and are actually tested. Why not?


Consider a number of things we don't often do well.


-  Background on an algorithm or data structure.
   Footnotes, links, etc., are often slightly easier to
   write in word-processing markup than comments in the
   code.

-  Performance information on the choice of a data
   structure. Merely claiming that a HashMap is faster
   isn't quite as compelling as running timeit and
   including the results.

-  Binding unit tests and code side-by-side. Current
   practice keeps the unit tests well separated from
   code. (Django framework models are a pleasant
   exception.) What could be nicer than a method followed
   by unit tests that show hot it works? You may write
   the tests first, but the code-first explanation is
   sometimes nicer than the test-first development.

           
I think that LP isn't all that hard, but we have three
barriers to overcome. We don't have exceptional tools.
We have a complex welter of languages. And we have bad
habits to break and transform into new habits.


**Some Links**


http://www-cs-faculty.stanford.edu/~uno/programs.html


http://tex.loria.fr/english/litte.html


http://lambda-the-ultimate.org/node/3663


http://c2.com/cgi/wiki?LiterateProgramming


http://vasc.ri.cmu.edu/old_help/Programming/Literate/literate.html


http://www.desy.de/user/projects/LitProg.html


http://infohost.nmt.edu/~shipman/soft/litprog/


http://www.vivtek.com/litprog.html


http://www.literateprogramming.com/ - Good stuff, but not
a real wiki or forum site.


http://www.squidoo.com/literateprogramming


**Some Tools**


http://en.literateprograms.org/LiteratePrograms:Welcome


http://nuweb.sourceforge.net/


http://pylit.berlios.de/literate-programming.html


http://webpages.charter.net/edreamleo/design.html


http://pywebtool.sourceforge.net/



-----

Nice simple blog layout. I will click through on y...
-----------------------------------------------------

Maintenance Man<noreply@blogger.com>

2010-03-29 18:12:17.998000-04:00

Nice simple blog layout. I will click through on your AdSense.


You might want to have a look at the LEO programme...
-----------------------------------------------------

Michael<noreply@blogger.com>

2010-03-29 18:10:26.404000-04:00

You might want to have a look at the LEO programmer's editor
http://webpages.charter.net/edreamleo/front.html which is written in
Python and supports literate programming. It can be used to import
existing code in order to either document it, or to continue development
in a literate manner. The author has also written a bit about how he
uses LEO features in a very practical exposition of literate
programming.


Nice outline of a LP lifecycle. I'll try to us...
-----------------------------------------------------

Ryan<noreply@blogger.com>

2010-04-12 18:43:40.819000-04:00

Nice outline of a LP lifecycle. I'll try to use that on my next LP
project (a procedurally generated text adventure).
I was personally planning on using Sphinx with it's ability to include
external \*.py files.

The \*.py files and \*.rst files would have cross references that could
be moved between with a vim macro (that's the hope, at least).
I guess the approach I'm trying to take is a bit closer to Elucidative
Programming
[http://www.cs.aau.dk/~normark/elucidative-programming/index.html]
rather than pure Literate Programming.


Very detailed and serious article, I'm absolut...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2013-02-14 11:22:38.368000-05:00

Very detailed and serious article, I'm absolutely agree with author with
his thesises (please, exuse my English). Itried different tools (PyWeb
too), wrote 3, and now I'm developing NanoLP tool, for me it's syntax
and approach is the best (no language barrier, supports many formats
(Asciidoc, reStructuredText, TeX, HTML, XML and other) includes
OpenOffice/LibreOffice, so it can be use in WYSIWYG manner,

collaborative usage - with LP libraries support, publishing on Web), and
as main for me - very light syntax, so LP program is very readable, no
weird syntax as it's usual for CWEB or other tools. It's project page
is: http://code.google.com/p/nano-lp/ (me is author).

What LP missed? We can compare LP tools with the best but opposite tool

-   Doxygen. Doxygen is good due to its 'smart'

-   Doxygen creates structured, classified "guide" of input sources, something like "map"
    for navigation of code. So, LP can not help us to navigate (like in IDE,
    or Source Navigator) in code, it looks like 2 different dimensions of
    one, the same cube :) And attempts to summarize both in one text will be
    terrible (for user).





