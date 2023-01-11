Parallelism, Concurrency and Pipelines (Updated)
================================================

:date: 2007-10-29 19:45
:tags: architecture,design,data structure,algorithm
:slug: 2007_10_29-parallelism_concurrency_and_pipelines_updated
:category: Architecture & Design
:status: published







A taxonomy of pipeline alternatives is a big, hairy deal, involving lots of alternatives.  While your basic API methods are relatively few in number, each language and platform introduces new options.  Without some focus, it's challenging to produce a big, fluffy description of all potential alternatives.



However, the interesting thing is the value of pipelining in the first place.  Often, folks get confused and start insisting on multiple threads, more memory or some other non-solution.



Worse, I sometimes hear confusion about how pipelining even helps.  I've had too many questions about how to avoid bottlenecks in a pipeline, as if having a single slow step negates the value of the concurrent processing.



The point here is that we can achieve concurrency fairly simply.  It doesn't have to involve complex API's.  We can use a domain specific language (e.g. a shell) or we can use XML Pipeline Language (XPL).



Oracle Pipelining
-----------------



Oracle, for example, has -- for a while now -- offered a pipelining feature so that parts of a program don't have to wait for the entire query to finish before processing rows from the query.  These pipeline functions yield objects that are -- in effect -- table rows one at a time.



The big benefit is that we won't wait for the entire cursor to fetch all the rows.  Instead, we can apply a function to each row and yield that row to the calling application program.



This is, effectively, what the Python ``yield``  construct does.



We can do this without suffering through the complexities of Oracle or PL/SQL.  I want to emphasize the suffering and complexities here.  First, there isn't a lot of inherent parallelism in PL/SQL; this mechanism gives us a tiny bit of parallelism between parts of our application and the rows being built in the database.  Parallelism among non-database operations isn't possible.



Shell Pipelining
----------------



Every POSIX-compliant operating system (that is to say, everything but Windows and IBM's Z/OS) has trivial access to a standardized set of API's for creating pleasant pipelines.  Best, of course, is that all of the variants on the Shell do this for us.



The shell offers a wonderfully sophisticated math-like language of operators for connecting processes (and files) into tidy process composition expressions.  



There are several math-like operators:



-   ``;`` (also written as newline, ``\n``)

-   ``&``

-   ``|``

-   ``&&``

-   ``||``



Along with ()'s for grouping.  However, this isn't often-enough seen as the tidy little language that it really is.



Process Composition
--------------------



The operators have to be thought of as "composition", as in "process X is composed of process Y and Z".



Each operator defines a radically different kind of composition.



The most commonly used operator is newline or ;.  This operator effectively creates a new process composed of two processes executed sequentially.



The shell may optimize this by simply executing processes sequentially.  However, when we introduce ()'s, we force the shell to actually create this new process in the form of a subshell.



The | operator creates a new process composed of two processes which execute concurrently, and have stdout of one process connected to stdin of the subsequent process.  This is fairly easy to understand, but is often treated as an "advanced" topic in books on Linux or the shell.  I'm not sure why this is treated as advanced, since it's so simple and so effective for improving performance of complex processes.



A Confusing Special Case
-------------------------



The ``&`` operator, because it can be used in a special unary context, seems to create the most confusion.  For some reason, a construct like ``Y & Z`` isn't seen as two concurrent processes, but as Y running in some obscure nohup-like mode, and Z is part of ordinary sequential composition.



A unary ``&`` operator (at the end of a single line) is the most common use for ``&``, but it has to be seen as a special case.  When we do something like ``python idle.py &`` it isn't an example of process composition in an obvious way.



The binary ``&`` operator (between programs) is fairly rare.  Why run two programs concurrently when there's no obvious connection?  In many data warehouse contexts, we have a number of preconditions for a given load.  So we may have something like ``(A & B & C); D``.  In this case, we have three preconditions which all must finish before D can start.



Conditional Composition
-----------------------



The ``&&`` and ``||`` operators for composition are elegant ways to specify a kind of composition which is dependent on a condition.  In the ``&&`` case, the left-hand process must finish normally.  In the || case, the left-hand process must not finish normally.



This conditional composition was borrowed by perl, and used wisely, it can make a program somewhat easier to read.



Alternate Notations
-------------------



It turns out that the XML folks have concocted several alternate notation for this, including Apache `Jelly <http://commons.apache.org/jelly/>`_  and `XPL <http://www.w3.org/Submission/xpl/>`_ .  XPL doesn't seem to have a lot of implementations floating around.  `Orbeon <http://www.orbeon.com/>`_  seems to be it; however, the Wikipedia page lists some other implementations including Oracle and `smallx <https://smallx.dev.java.net/>`_ .



XPL adds a lot of detail (and a lot of syntax.)  In this case, I'm not sure the extra syntax provides any extra value.  The shell's syntax, which could be called a domain-specific language (DSL) solves the problem nicely.  



The `Lure of XML <{filename}/blog/2006/12/2006_12_23-xml_one_ring_to_rule_them_all.rst>`_  is strong.  The shell's language seems easy to parse and unambiguous.  Why add syntax?  How much less ambiguous can we make it?



[Incidentally, XPL is a heavily overloaded name.  See http://wiki.xplproject.org.uk/index.php/XPL_News, http://www.cs.toronto.edu/XPL/  and http://csdl2.computer.org/persagen/DLAbsToc.jsp?resourcePath=/dl/proceedings/&toc=comp/proceedings/icis/2007/2841/00/2841toc.xml&DOI=10.1109/ICIS.2007.197  for other meanings.]



Using Concurrency
-----------------



It can be challenging to reduce a big, complex algorithm down into smaller, pipelined steps.  However, doing this has a number of advantages, even if a pipelined shell script is never used.



First, breaking a big algorithm down into small algorithms is always helpful.



Additionally, the data structures which are passed from step to step can be done as in-memory structures or they can be explicitly written to a pipeline.



In Java, we have a Pipe class that we can use to pass serialized objects among Java threads or processes.   And we can use commodity shell constructs to compose fast, parallel processing applications rather than Java or Oracle constructs.



Since we have such a rich set of shell script operators for concurrency, we don't really need to deeply understand a lot of Java or Oracle to make this work.  We can decompose our algorithm, and use a few key serialized objects to move data among parallel processes.



If we have an XPL implementation, we could use that instead of the shell.  The point is to leverage concurrent processing in a portable, flexible way.  We can avoid the details of API calls (and PL/SQL) while improving throughput in an application.





