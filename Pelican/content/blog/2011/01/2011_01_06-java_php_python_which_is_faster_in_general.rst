Java PHP Python -- Which is "Faster In General"?
================================================

:date: 2011-01-06 08:00
:tags: PHP,#python,java,numerosity
:slug: 2011_01_06-java_php_python_which_is_faster_in_general
:category: Technologies
:status: published

Sigh. What a difficult question. There are numerous incarnations on
StackOverflow. All nearly unanswerable. The worst part is questions
where they add the "in general" qualifier. Which is "faster in general"
is essentially impossible to answer. And yet, the question persists.

There are three rules for figuring out which is faster.

And there are three significant problems that make these rules
inescapable.

**Rule One. Languages don't have speeds. Implementations have speeds.**

Info on
`benchmarking <http://en.wikipedia.org/wiki/Benchmark_(computing)>`__.
The idea of a benchmark is to have a single, standard suite of
source code, which can be used to compare compilers, run-time
libraries or hardware.

Having a standard suite of source is essential because it provides
a basis for comparison. A single benchmark source is the fixed
reference. We don't compare the top of the Empire State Building
with the top of the Stratosphere in Las Vegas without specifying
whether we care about height above the ground or height above sea
level. There has to be some fixed point of comparison, some common
attribute, or the measurements devolve into mere numerosity.

Once we have a basis for comparison (one single body of source
code), the other attributes are degrees of freedom; the
measurements we make will include the other attributes. This will
allow a rational statement of what the experimental results where.
We can then compare these various free attributes against each
other. For details look at something like the `Java Micro
Benchmark <http://www.cs.cmu.edu/~jch/java/microbench.html>`__.

**Rule Two. Statistics Aren't a Panacea.**

The reason there's no "in general" comparison among languages is
because there are too many degrees of freedom to make any kind of
rational comparison. We can make irrational comparisons, but
that's the trap of numerosity -- throwing numbers around. 1250 vs.
1149, 1300 vs. 3177. What do they mean? Height above ground?
Height above sea level? What's being measured?

There's a huge problem with claiming that statistics will yield an
answer to which language implementation is faster "in general". We
need some population that we can sample and measure. **Problem
1**: What the population are we measuring? It can't be "programs":
we can't compare grep against Apache httpd. Those two programs
have almost no common features.

What makes the population of programs difficult to define is the
language differences. If we're trying to compare PHP, Python and
Java, we need to find a program which somehow -- magically -- is
common across all three languages.

**The Basis For Comparison**

Finding common programs degenerates into **Problem 2**: what
programs could be comparable? For example, we have the Tomcat
application, written in Java. We wouldn't want to write Tomcat in
Python (since Tomcat is a Java Servlet container). We could
probably write something Tomcat-like in PHP, but why try? So we
can't just grab programs randomly.

At this point, we devolve to subjectivity. We need to find some
kind of problem domain in which these languages overlap. This gets
icky. Clearly, big servers aren't a good problem domain. Almost as
clearly, command-line applications aren't the best idea. PHP does
run from the command-line, but it's always contrived-looking
because it doesn't exploit PHP's strengths. So we wind up looking
at web applications because that's where PHP excels.

Web applications? Subjective? Correct. PHP is a language plus a
web application framework bundled together. Java and Python -- by
themselves -- are just languages and require a framework. Which
Java (and Python) framework is *identical* to PHP's framework?
Spring, Struts, Django, Pylons? None of these reflects a code base
that's even remotely similar. Maybe Java JSP is similar enough to
PHP. For Python there are several implementations. Sigh.

**Crappy Program Problem**

We can't easily compare programs because we're really comparing
implementations of an algorithm. This leads to **Problem 3**: we
picked a poor algorithm or did a lousy job of implementing it in
the target language.

In order to be "comparable", we don't want to exploit
highly-optimized or unique features of a language. So we tried to
be generic. This is fraught with risks.

For example, Java and PHP don't have list comprehensions. Do we
forbid them from our Python behchmark? In Python, everything is a
reference, values cannot be copied. If we pick an algorithm
implementation which depends on copying objects, Java may appear
to excel. If we pick an algorithm implementation which depends on
sharing references, Python may appear to excel.

Somehow we have to get past language differences and programmer
mistakes. What to do?

**Synthetic Benchmarks**

Since we can't easily find comparable programs -- as whole
programs -- we're left with the need to create some kind of
benchmark based on language primitives. Statements or expressions
or something. We can try to follow the
`Whetstone <http://en.wikipedia.org/wiki/Whetstone_(benchmark)>`__/`Dhrystone <http://en.wikipedia.org/wiki/Dhrystone>`__
approach of analyzing a bunch of programs to find the primitive
constructs and their relative frequency.

Here's the plan. We'll take 100 PHP programs, 100 Java programs
and 100 Python programs and analyze them to find the relative
frequency of different kinds of statements. What then?

The goal is to create one source that reflects the statements
actually used in the 300 programs we analyzed. In three different
languages. Hmmm... Okay. We'll need to create a magical mapping
among the statement constructs in the three languages. Well,
that's hard. The languages aren't terribly comparable. A Python
expression using a List Comprehension is the same thing a
multi-statement Java loop. Rats.

The languages aren't very comparable at the statement level at
all. And if we force them to be comparable, we're not comparing
real programs, but an artificial mapping.

**Virtual Machine Benchmarks**

Since we can't compare the languages at the program level or the
statement level, what's left? Clearly, the underlying interpreter
is what we care about.

We're really comparing the Java Virtual Machine, the PHP
interpreter and the Python interpreter. That's what we really care
about.

And life is simple because we can compare Java, The `Project Zero
PHP Interpreter <https://www.projectzero.org/php/>`__ based on the
JVM and `Jython <http://www.jython.org/>`__. We can look at
"compiled" PHP, Java Class Files and Python .PYC files to find the
VM primitives used by each language and then -- what? Compare the
run-time of the various VM primitives? No, that's silly, since the
run-times are all JVM run-times.

**What We're Left With**

The very best we can can do is to compare the statistical
distribution of the VM instructions created by Java, PHP or Jython
compilers. We could note that maybe PHP or Python uses too many
"slow" VM instructions, where Java used more "fast" VM
instructions. That would be an "in general" comparison. Right?

See? You can `measure anything <http://www.howtomeasureanything.com/>`__.

In this case, the compiler itself is a degree of freedom. Sadly,
we're not comparing languages "in general". We're comparing the
bytecodes created by various compilers. We're actually comparing
compilers and compiler optimizations of the bytecode. Sigh.

That's not what we were hoping for. We were hoping for some kind
of "in general" comparison of the language, not the JVM compiler.

Java has pretty sophisticated optimization. Python, however,
eschews optimization. PHP has it's own weird issues. See this
paper from Rob Nicholson from the CodeZero project on how to
`implement PHP in the JVM <http://wiki.jvmlangsummit.com/pdf/24_Nicholson_p8.pdf>`__.
PHP doesn't fit the JVM as well as Python does. So there's a weird
bias.

**Rule Three. Benchmarking Is Hard.**

There is no "in general" comparison of programming languages. All
that we can do is benchmark something specific.

It works like this.

#.  Stop quibbling about language performance "in general".

#.  Find something specific and concrete we plan to implement.

#.  Actually write the performance-critical piece in Java, PHP,
    Python, Ruby, whatever. Yes. Build it several times. Really. We
    don't want to use "language-independent" or "common" features.
    We want to optimize ruthlessly -- use the language the way it
    was meant to be used. -- use the various unique-to-the language
    features correctly and completely.

#.  Actually run the performance-critical piece to get actual
    timings.

#.  Since run-time libraries and hardware are degrees of freedom,
    we have to use multiple run-time libraries, multiple compiler
    optimization settings and multiple hardware configurations to
    make a proper decision on which language to use for our
    specific problem.

Now we know something about our specific problem domain and the
available languages. That's the best we can do.

We can only compare a specific problem, with a specific algorithm.
That's the basis for all benchmark comparisons. Since each
implementation was well-done and properly optimized, the degree of
freedom is the language -- and the run-time implementation of that
language -- and the selected OS and hardware.



-----

Nice post, thanks for sharing.
------------------------------

MyOpenDraft<noreply@blogger.com>

2011-01-08 07:30:01.084000-05:00

Nice post, thanks for sharing.


Again, nice post, thanks.

But there is more to la...
-----------------------------------------------------

Paddy3118<noreply@blogger.com>

2011-01-11 16:24:07.364000-05:00

Again, nice post, thanks.
But there is more to language comparison than benchmarking/speed. See
http://rosettacode.org for an alternate approach.


I hope that PHP was very advanced compared to JAVA...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2011-10-13 07:03:08.721000-04:00

I hope that PHP was very advanced compared to JAVA as it has many
benefits compared to JAVA programming.U have shared many good points.
Thank you !
`web design company <http://www.web-designs-company.com>`__


I think you missed the point, although the points ...
-----------------------------------------------------

DarKMaTTeR<noreply@blogger.com>

2012-03-27 15:22:51.770000-04:00

I think you missed the point, although the points you made are valid.
I doubt the question "which is faster", even with "in general" included,
ever meant "how fast would the world be, if it was implemented in X". I
found the example about writing Tomcat in PHP embarassing, actually.
What people mean is "If I were to code a webpage of unspecified nature
and cared about speed, how much would the language matter"


Hi,

Recently I came across some great articles on...
-----------------------------------------------------

Innofied<noreply@blogger.com>

2013-04-16 06:51:03.954000-04:00

Hi,
Recently I came across some great articles on your site.
The other day, I was discussing
(This post) with
my colleagues and they suggested I submit an article of my own. Your
site is just perfect for what I have written!

Would it be ok to submit the article? It is free of charge, of course!
Let me know what you think

Contact me at anelieivanova@gmail.com

Regards

Anele Ivanova





