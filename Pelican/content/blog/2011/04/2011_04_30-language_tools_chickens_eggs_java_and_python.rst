Language, Tools, Chickens, Eggs, Java and Python
================================================

:date: 2011-04-30 08:00
:tags: Programming Languages,ide,tools
:slug: 2011_04_30-language_tools_chickens_eggs_java_and_python
:category: Technologies
:status: published

Too much of programming is intimately tied up with the tools to support
the development of the software.

Example 1. I was told -- with absolute and fierce conviction -- that
VB may suck as a language, but Visual Studio more than makes up for
the obvious problems. For some people, **Tools Trump Language**.
Sadly, I've also had customers with ancient code they could no longer
compile or maintain because the tools were out of support.

On Stack Overflow, you can read questions like this: "`What IDE to
use for
Python? <http://stackoverflow.com/questions/81584/what-ide-to-use-for-python>`__".
In spite of this question's immense popularity, it gets re-asked all
the time. Search for "Python IDE" to see endless duplicates. One of
the most common duplicate forms of this question asks (or demands)
code completion. As if there are folks who cannot write code without
code completion.

**Chickens and Eggs**

The issue with sophisticated IDE's (like Eclipse, NetBeans, and even
Komodo) is that you have to learn the tools before learning the
language. Until you know something about the language, the tools, of
course, are useless. Worse, Eclipse is for "enterprise" applications
and is so fat with bells (and whistles) that it's hard to determine
what to use and what it means.

So the tool is a prerequisite for the language. But the language is a
prerequisite for the tool.

How to cut the Gordian Knot?

**First Principles**

Irrespective of the "Visual Studio makes VB not suck" crowd, language
comes first -- and last -- and fills all the spaces in between.

Language is everything. Software is merely encoded knowledge. The
language of that encoding is how we determine meaning; how we argue
about correctness, adaptability, maintainability and security. Tools
don't endure -- they come and go -- but the language remains.

The only thing more important than the language is the data itself.
But that's another rant.

Proof, of course, is available everyone except in VB circles. For
non-proprietary languages (Java, Python, etc., etc.) there are a
large number of competing tools. One language many tools. Take the
hint. Language is important.

Yes, some tools are so flexible, they cover several languages. But
there's no universal tool any more than there's a universal language.
And the bias is clearly very, very many tools for a given language
and only a few languages for a given tool.

**How To Start**

Language comes first.

For Python, that's easy. Run Python, type code at the >>> prompt, and
you're learning. Python comes with IDLE which is a minimalist IDE. It
will get anyone started. Later, they can try other IDE's.

For Java, however, that's not that easy. It isn't however, impossible
to get started. It's just challenging.

Option 1 -- Bare Knuckles. It's possible to edit text and run the
javac compiler to learn a great deal of Java without an IDE. It's not
a bad idea. It will get complex to manage projects with more than a
few files.

Eventually that's what `Ant <http://ant.apache.org/>`__,
`Maven <http://maven.apache.org/>`__ and
`SCons <http://www.scons.org/>`__ are for. But that's not a good
place to start. Again, the tools don't make sense until you start
writing things big enough that the tools actually help.

Option 2 -- Succession of IDE's. It's probably best to start with a
very simple IDE for Java. Something like `Komodo
Edit <http://www.activestate.com/komodo-edit>`__,
`TextMate <http://macromates.com/>`__ or
`BBEdit <http://www.barebones.com/products/bbedit/index.html>`__.
There are a lot of choices, but the idea is to find something little
more than a text editor with a few tools. I've used these and like
their relative simplicity.

The `JavaWIDE <http://www.javawide.org/index.php/Main_Page>`__
toolset might be helpful. I haven't used it, but some folks suggest
that it simplifies the language learning. Later a "regular" desktop
IDE can be used.

Later, one can move to `NetBeans <http://netbeans.org/>`__ or
`Eclipse <http://www.eclipse.org/>`__.

**Classrooms and Autodidacts**

In the classroom, it's easy to demonstrate NetBeans and answer
questions.

For auto-didacts, however, choosing the wrong tool leads to endless
confusion. The chicken and egg issue isn't clarified by wasting time
trying to install and use a tool that's too sophisticated for a n00b.

N00b autodidacts really need to start with a simple text-editor. They
need to use \`javac\` to compile and \`java\` to run the resulting
class. For the first week or two, this will do. Once past the
fundamentals, however, IDE selection can start to make sense. A
BBEdit/TextMate/Komodo thing should be next. This is good for --
perhaps a year or more. Then, when doing "real" programming, a
heavier-weight tool makes sense.





