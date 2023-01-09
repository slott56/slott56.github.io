PL/SQL vs. Java - Additional Information
========================================

:date: 2007-03-23 15:21
:tags: architecture,design,data structure,algorithm
:slug: 2007_03_23-plsql_vs_java_additional_information
:category: Architecture & Design
:status: published





**Physical Tuning.** 



"...databases can be tuned
by creating appropriate indexes, removing others, modifying the physical
database schema to suit the most common types of queries, etc. So it isn't clear
whether the PL/SQL figure could be better if the database was optimised by a
good DBA."



While a good point, it
doesn't apply.  In order to compare Java and PL/SQL, I had to use the same
database for both implementations.  It was the same Oracle 10 XE
instance.



The physical design question
is really about comparing two data models, not about comparing two languages for
processing a single, common data model.  Yes, a change to the index might make
both the PL/SQL and the Java run even faster.  However, any performance
improvement would apply across the board to Java as well as
PL/SQL.



**DB Interaction.** 



"...it was typically
faster to do as much processing as possible in the database, rather than outside
of the database. This is particularly true where the external code has to make
many queries to the database in the course of doing a particular piece of work.
Replacing those with a single call to the database ... was a big performance
gain."



Again, a really good point, but
one that doesn't completely apply.



The
core issue of PL/SQL vs. Java doesn't matter.  PL/SQL, while resident in the
RDBMS server, isn't really part of the database.  PL/SQL makes SQL requests just
like Java (via JDBC) is making SQL requests.  Both the PL/SQL and the Java use
nearly the same SQL SELECT statements.  They can't be identical because SELECT
is part of the PL/SQL language, but a simple String object to
Java.



In both Java and PL/SQL, we're
doing as much in the DB as possible -- executing a SELECT which does simple
matching and executing a SELECT which does "near-miss" matching.  The PL/SQL
version is slower because the non-DB work done in the PL/SQL program is slower
than Java.  Further, the PL/SQL run-time environment is tightly constrained to
be part and parcel of the RDBMS, limiting memory and
throughput.



**The Bigger Picture.** 



From a slightly broader
point of view, people regularly claim that calling a PL/SQL procedure does "more
work in the database."  In this case, we have designed a moderately complex
procedure, which has to exist -- as a procedure -- somewhere.  We can't rewrite
our process to embed the logic in a SELECT statement.  We can't do more work in
the database; the procedure is either PL/SQL making SQL requests or Java making
SQL requests.



What happens all too
often is people take something this is already a first-class feature of SQL, and
write their own procedure to implement it.  For example, people will write
algorithms to do joins as nested lookups, or unions as a series of queries, or
group-by's in their own programs because they didn't understand SQL, or thought
they could write something faster.  In these cases, writing proper SQL, and
providing a sound RDBMS physical structure, is probably going to be fastest.




Any speedup from doing more work in
SQL and less work in the "application" applies to a Java application as well as
a PL/SQL application.  The point is to make better use of the SQL query and DML
features, and the physical structures in the
RDBMS.



In my example, the processing
can't easily be reduced to simple SQL.  It involves decision-making that is hard
to code as a simple WHERE-clause.  Therefore, we have two places to put the
processing: PL/SQL (slow) or Java (fast). 




**Aside.** 



The
SQL-For-Smarties crowd will note that multi-part matching is -- technically -- a
kind of union.  We could try to implement this processing as a union of exact
matches with near-miss-but-not-exact matches.  This can get very hairy, and it
becomes hard to maintain because we have to do a lot of predicate calculus to
work out the effect of implicitly procedural business
rules.



**Code Sample.** 



Here's the PL/SQL package I
used.

..  code:

::

    create or replace package body "MATCHSQL" is
    procedure MAIN
    as
       invno NUMBER;
       temp NUMBER;
       CURSOR invoice_qry( mandate DATE, mantotal NUMBER, manshiptocust NUMBER ) IS
           SELECT invno FROM INVOICE
           WHERE INVOICE.invtotal = mantotal
           AND   INVOICE.invdate = mandate
           AND   NVL(INVOICE.shiptocust,-1) = NVL(manshiptocust,-1);
       CURSOR invoice2_qry( mandate DATE, mantotal NUMBER, manshiptocust NUMBER ) IS
          SELECT invno FROM INVOICE
          WHERE INVOICE.invtotal BETWEEN mantotal-10 AND mantotal+10
          AND   INVOICE.invdate BETWEEN mandate-10 AND mandate+10
          AND   NVL(INVOICE.shiptocust,-1) = NVL(manshiptocust,-1);
       manCount NUMBER := 0;
       match NUMBER := 0;
       nearMatch NUMBER := 0;
       nonMatch NUMBER := 0;
       dupMatch NUMBER := 0;
    begin
     DBMS_OUTPUT.PUT_LINE( 'Pure SQL' );
     -- Iterate through all Manifests
     FOR man IN (SELECT manno, mantotal, mandate, shiptocust FROM MANIFEST)
     LOOP
        manCount := manCount + 1;
        -- Lookup matching Invoice
        OPEN invoice_qry( man.mandate, man.mantotal, man.shiptocust );
        FETCH invoice_qry INTO invno;
        IF invoice_qry%FOUND THEN -- Exact Match?
          FETCH invoice_qry INTO temp;
          IF invoice_qry%FOUND THEN -- Duplicate?
              dupMatch := dupMatch + 1; -- Duplicate
          ELSE
              match:= match + 1; -- Exact Match
          END IF;
        ELSE
          -- No Exact Match, try a fall-back near match
          OPEN invoice2_qry(man.mandate, man.mantotal, man.shiptocust);
          FETCH invoice2_qry INTO invno;
          IF invoice2_qry%FOUND THEN -- near match?
              FETCH invoice2_qry INTO temp;
              IF invoice2_qry%FOUND THEN -- duplicate?
                dupMatch := dupMatch + 1;
              ELSE
                nearMatch := nearMatch + 1;
              END IF;
          ELSE
             nonMatch := nonMatch + 1; -- No Match
          END IF;
          CLOSE invoice2_qry;
        END IF;
        CLOSE invoice_qry;
     END LOOP;
     -- Final Report
     DBMS_OUTPUT.PUT_LINE( 'Count ' || manCount );
     DBMS_OUTPUT.PUT_LINE( '  Match ' || match );
     DBMS_OUTPUT.PUT_LINE( '  Non-Match ' || nonMatch );
     DBMS_OUTPUT.PUT_LINE( '  Near Match ' || nearMatch );
     DBMS_OUTPUT.PUT_LINE( '  Duplicate ' || dupMatch );
    end MAIN;
    
    end MATCHSQL;





**The Real Speedup.** 



In addition to Java being
faster than PL/SQL, an additional speedup comes from making fewer DB requests in
the first place.  That's why I included the Pure SQL, One Dictionary and Two
Dictionary results.  Eliminating SQL entirely (and using Java HashMap) cuts the
time down to 0.4 of the Pure SQL performance. 




Here's my golden
rule:



**The Fastest RDBMS Operation is The One You Don't Do.** 



If it can be done outside the
database, it will be faster than if it is done in the database.  Clearly,
there's a fuzzy border between a sensible performance improvement and
reinventing your own RDBMS in your own application
program.



When it involves concurrent
transactions, your program's private cache of data is
**A Bad Thing** ™.  However, any data which is
static can -- and should -- be cached if you need to get maximum processing
speed.  Static, of course, is relative.  Some batch jobs run during windows in
which the database isn't "transactional", or during which the transaction load
is light or doesn't adversely impact the correctness of results that come from
cache. 



if. for example, a batch job
runs after midnight on yesterday's transactions, then an in-memory cache of
transaction data isn't invalidated by processing of today's transactions.   In
"`Processing Rows in Batches <http://ddj.com/dept/architect/184406071>`_ ", for example, one of
the factors left out of the article was the confusion over what rows were
actually part of a batch.  The original code did lots of thrashing around to try
and capture every transaction.  Why not just wait until the next batch
scheduling interval?  Or, why have batches in the first place?  Why not process
rows as they
arrive?



**Conclusion.** 



DB physical tuning helps both Java
and PL/SQL.  Since Java is already faster than PL/SQL, physical design is still
important and still helps.



Doing more
work in SQL's DML helps both Java and PL/SQL, also.  Knowing SQL, and making use
of the DML features is still important and still
helps.



PL/SQL is slow, and I find it
painful to manage, since it is relatively inflexible.  I don't have classpath,
working directories, environment variables, command-line parameters in my PL/SQL
environment.  I do have a kind of symbolic link as my only control mechanism for
introducing flexibility.



Since PL/SQL
is slower and less flexible than Java, I'm forced to to conclude that PL/SQL
isn't an effective way to implement anything. 








