Java vs. PL/SQL
===============

:date: 2009-07-24 06:10
:tags: PL/SQL,performance,java
:slug: 2009_07_24-java_vs_plsql
:category: Technologies
:status: published

Quite a while ago, I compared `Java and
PL/SQL <http://homepage.mac.com/s_lott/iblog/architecture/C465799452/E20070527090758/index.html>`__
to gauge their relative performance.

Recently (okay, back in mid-June) I got this request.

  One thing I would like to compare is Java vs PL/SQL using native
  compilation (search Oracle for NCOMP). Would you be willing to
  repeat
  your benchmark tests using NCOMP? NCOMP is pretty straightforward
  to
  set up, I think it is even easier in 11g, if you are using that.

  Also, when you test Java vs. PL/SQL, are you using Java stored
  procedures in Oracle, or are you using an external VM and
  connecting
  to Oracle? (One annoying limitation to Java Stored Procedures is
  the
  lack of threading ability, among a few other things).

Native Compilation will not make PL/SQL magically faster than Java.
The very best it can do is make PL/SQL as fast as Java. The clunky,
inelegance of PL/SQL isn't fixed by NCOMP, either.

My test was PL/SQL stored procedures in Oracle. These were compared
against Java programs in a separate JVM. I didn't use Java stored
procedures because the client didn't ask for this.

The client had legacy C code they wanted reverse engineered and
reimplemented. PL/SQL was unsuitable for this task for a number of
reasons.

#.  PL/SQL is slower than C or Java. Speed mattered.

#.  PL/SQL is a clunky and inelegant language. Worse than C and far
    worse than Java. The application would have grown to gargantuan
    proportions.

#.  The legacy C code was full of constructs that would have to be
    rethought from their very essence to recast them in PL/SQL. Java,
    for the most part, is a better fit with legacy C. The
    reverse-engineering was -- relatively -- easy in moving from C to
    Java.

There were some additional, minor considerations.

#.  There is some unit testing capability in PL/SQL
    (`UTPLSQL <http://utplsql.oracledeveloper.nl/>`__), but it's not
    as feature-rich as JUnit. Unit testing was essential for proving
    that the legacy features were ported correctly.

#.  PL/SQL is hard to develop. A nice IDE (like NetBeans or Eclipse)
    makes it very easy to write Java. The customer was using Toad and
    wasn't planning to introduce the kind of IDE required to build
    large, complex applications.

In short, the simple speed test -- PL/SQL vs. Java -- was
sufficient to show that PL/SQL is simply too slow for
compute-intensive speed-critical applications.


