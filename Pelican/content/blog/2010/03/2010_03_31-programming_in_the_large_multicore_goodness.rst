Programming in the Large -- Multicore Goodness
==============================================

:date: 2010-03-31 08:00
:tags: performance,Programming Languages,architecture
:slug: 2010_03_31-programming_in_the_large_multicore_goodness
:category: Technologies
:status: published

The lowly shell (bash, zsh, csh, the whole bunch) is usually a
dreadful programming environment. Perfectly awful. With some care,
you can easily architect applications so that you don't really need
the shell for very much.

However, there is a precious nugget of goodness within the shell's
programming language. The Linux shell's have a cool Programming in
the Large (PITL) language. This combines executable programs using a
number of operators. These operators are an excellent set of design
patterns that can help us create complex multi-processing pipelines.

The best part about the shell's PITL language is that a simple shell
pipeline will use every core in our processor, maximizing throughput
and minimizing the amount of programming we have to do.

**PITL Objects**

This PITL language has a simple set of operators. If your programs
are well-behaved, the language is, in a formal mathematical sense,
closed. You can apply PITL operators to combinations of programs to
get new composite programs.

To be well-behaved a program must read from standard in and write to
standard out. The inputs and outputs must be in some regular syntax.
Regular, here, means parseable by regular expressions or regular
grammars.

As a special case, we need to create a special program that can read
from someplace other than standard in, but write it's content to
standard out. A program like cat.

Note that any map-reduce step will be well-behaved. To seed the
map-reduce pipeline we use cat as the "head-0f-the-pipeline".

**PITL Operators**

We'll look at the composition operators using three short-hand
commands: p1, p2 and p3. Each of these is "well-behaved": they read
from stdin and write to stdout.

Typically, running a program from the shell involves a much longer
and more involved command-line, but we'll use these three aliases to
strip away the details and look at the design patterns. You can
imagine them as being p1.py or even python p1.py.

**Sequence,** ``;``. A sequence of steps is shown in the shell on
multiple lines, or with the ; operator. In effect a sequence declares
a program as the precondition for the following program. We can
summarize this as "p1 ; p2".

**Parallel,** ``&``. A parallel operation is shown by using the &
operator. The two programs are declared as independent operations. We
can summarize this as "p1 & p2". As an extension to this, a trailing
"&" allows the programs to run in parallel with the shell itself;
this gives you a next prompt right away.

This allows the OS to schedule your two processes on two or more
cores. However, there's no real relationship between the processes.

**Pipeline,** ``|``. A pipeline operation is shown using the \|
operator. We can summarize this as "p1 \| p2". In addition to the
logical connection of one program's input being the other program's
output, both programs can run in parallel, also.

This allows the OS to schedule your two processes on two or more
cores. Indeed, the more stages in the pipeline, the more cores you'll
need to do the processing. Best, of course, the I/O is through a
shared buffer and doesn't involve any physical transfer of bytes
among the processes.

This is a very powerful way to use multiple cores with minimal
programming.

If one part of a pipeline is a sort, however, the parallel processing
is limited. The sort must read all input before providing any output.
A process like "p1 \| sort \| p3" is effectively serial: "p1 > temp1;
sort temp1 >temp2; p3 temp2".

**Grouping**. Programs are grouped by ``()``'s of various kinds (``{}``
and \``). Also the conditional and repetitive statements
effectively group series of programs. We use syntax like ``"``( p1 & p2 ); p3`` to show the situation where p1 and p2 must both complete
before p3 can begin processing.

**Using All the Cores**

Most importantly, something like "( p1 ; p2 ) \| p3" directs the
output of two programs into a third for further processing. And
the two program sequence runs concurrently with that third
program. This will use at least two cores.

What we'd also like is "( p1 & p2 ) \| p3", but this doesn't work
as well as we might hope. The output from p1 and p2 are not a
stream of atomic writes carefully interleaved. They are non-atomic
buffer copies that are impossible to disentangle. Sadly, this
can't easily be implemented.

**Other Features**

The shell offers a few other composition operations, but as we start
using these, we find that the shell isn't a very effective
programming environment. While the shell pipeline notation is
outstandingly cool, other parts of the notation are weak.

**Conditional**. The ``if``, ``case`` and ``select`` shell statements define
conditional processing and groupings for programs. Trying to evaluate
expressions is where this gets dicey and needlessly complex.

**Repetitive**. The ``for``, ``while`` and ``until`` shell statements define
repetitive processing for a program. Again, expression evaluation is
crummy. The for statement is usable without needless complication.

Four of these PITL operators (sequence, parallel, pipeline, grouping)
give us a hint as to how we can proceed to design large-scale
applications that will use every core we own.

**Implementation Hints**

You can -- trivially -- use all your cores simply by using the shell
appropriately. Use the shell's pipeline features **and nothing
else**, and you'll use every core you own.

For everything outside the pipelining features, use Python or
something more civilized.

And, you have a nice hybrid solution:
`iterpipes <http://pypi.python.org/pypi/iterpipes>`__. You can
construct pleasant, simple, "use-all-the-cores" pipelines directly in
Python.



-----


Check out

Computer Scientists Created the Paralle...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-04-02 08:16:50.053000-04:00

Check out
Computer Scientists Created the Parallel Programming Crisis
http://rebelscience.blogspot.com/2010/02/computer-scientists-created-parallel.html
... problem with the Turing Computing Model: timing is not an inherent
part of the model ...


One thing that helps me run my everyday tasks in p...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-03-31 17:22:11.781000-04:00

One thing that helps me run my everyday tasks in parallel using N cores
is the xargs -P N command. Diomidis Spinellis wrote an indroductionary
blog post on this subject `Parallelizing Jobs with
xargs <http://www.spinellis.gr/blog/20090304/>`__ a while ago. xargs -P
does a better job in balancing the workload than a pipeline composition
(|). It would be nice to mention xargs -P in your series of posts on
multicore programming.

Sometimes parallel mapping of a list of data units is not trivial due to
the complex nature of the list itself. For example, in GNU make a list
of jobs is computed lazily in the runtime. That is why it has a
special-purpose -j option for running a list of jobs in parallel.


For a Windows perspective on this issue, refer to ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-07-04 11:30:11.837000-04:00

For a Windows perspective on this issue, refer to "Windows Parallelism,
Fast File Searching, and Speculative Processing" By Johnson M. Hart
url:
http://www.informit.com/articles/article.aspx?p=1606242&ns=18872&WT.mc_id=2010-07-04_NL_InformITContent





