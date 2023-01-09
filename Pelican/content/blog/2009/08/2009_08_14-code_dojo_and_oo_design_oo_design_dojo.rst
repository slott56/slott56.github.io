Code Dojo and OO Design -- OO Design Dojo
=========================================

:date: 2009-08-14 14:58
:tags: code-kata,OO design
:slug: 2009_08_14-code_dojo_and_oo_design_oo_design_dojo
:category: Technologies
:status: published

Code Dojo, to an extent, includes a fair amount of OO Design.

I've been pondering ways to help folks who clearly have no design
skills at all. I've read their code. It's appalling.

Toward that end, I looked at some of the Code Kata links: the
`CodeKata <http://codekata.pragprog.com/>`__ page, Mark Needham's
blog posting on
`code-kata <http://www.markhneedham.com/blog/tag/code-kata/>`__,
Rizky Farhan's `Collection of Software
Projects <http://frizky.wikidot.com/projects:code-kata>`__,
jp.hamilton's `Code Kata
Resources <http://www.jphamilton.net/post/Coding-Dojo-and-Code-Kata-Resources.aspx>`__.

They asked for code samples to act as best practices. I suggested
to our sales folks that code samples and simple code "best
practices" were completely inadequate. They need serious remedial
skill-building in programming.

What started to percolate was organizing a periodic "code dojo"
meeting to help them build skills without the onerous "teaching"
(or worse, "lecturing") mode. Teaching OO design to working
programmers is generally hard. Many programmers seem to have a
starting point that isn't based on the requirements or any kind of
rational design. It appears that many programmers start with a
pretty random boilerplate program.

**Teaching Java to COBOL Programmers**

I remember struggling with COBOL programmers. Back in '02 (before
Code Dojo existed), I had no real way to educate folks except a
lot of one-on-one conversations. I tried to schedule code
walkthroughs, but the project manager didn't like the idea, and
cancelled them.

I was allowed a quick overview of J2EE concepts and how the web
side of our application was going to be assembled, but that was
it.

Even covering basic J2EE servlet concepts become a FAIL because
the legacy web framework was a JSP hack-around. It didn't work
well, couldn't easily be explained (or used). But it was
entrenched, and therefore, had priority in everyone's mind.

No matter how many times I tried to review basic OO concepts, and
some design approaches, there were problems.

Everyone wanted to start from "the top", with a "main program"
that "simply read and wrote files." COBOL concepts. Java File I/O
has a subtle complexity with lots of nested constructors. No one
likes to see that as a beginner. Also, file parsing is -- in
reality -- fairly hard, but COBOL provides a handy optimization
via a fixed format record layout and lots of implicit conversions.

We're writing servlets that query a database. There was no mapping
to the COBOL concepts everyone wanted to start with. A few
lectures and presentations aren't helpful. Had I but known about
Code Dojo, I would have suggested that. It might have worked.

**The "Getting Started" Problem**

Some Stack Overflow questions on design are really questions about
"getting started". These cause me to wonder how to help people who
are sure they know the language and syntax, but can't seem to get
started writing anything useful "from scratch" (or *de novo*.)

I've heard from people have have UML class diagrams and still
claim they don't know what to do next. They can't -- for some
reason -- get started.

I think this is related. They have a limited, fixed set of
programming templates. Learning a new language does not fit their
limited set of templates. Perhaps Code Dojo could help these folks
gain a new set of templates.



-----

Thanks for the code-kata links
------------------------------

Montecristo<noreply@blogger.com>

2009-12-15 03:51:15.528000-05:00

Thanks for the code-kata links





