PL/SQL vs. Java - Which is REALLY faster?
=========================================

:date: 2007-03-23 00:12
:tags: architecture,design,data structure,algorithm
:slug: 2007_03_23-plsql_vs_java_which_is_really_faster
:category: Architecture & Design
:status: published





While the question of speed came up recently, it
ties in to a long-standing position of mine.  I ran some realistic benchmarks,
and I'm much happier with my architecture
now.



**Background.** 



Years
ago, at a Siebel conference, I heard a heretical comment.  Specifically, they
use the RDBMS as simple, flat storage: tables and indexes, nothing more.  I was
shocked and dismayed that they had just knocked the idea of stored procedures
and triggers right on its ear.



About
the same time, we had reached our limit in coping with an application that was
in "trigger hell" -- it had so many triggers firing for so many reasons, we
couldn't work with it.  Further, it had stored procedures in the RDBMS, plus is
had blocks of Tcl code in the database.  Too much architecture, without really
clear allocation of responsibility.  Application developers and maintainers
didn't really get intent behind the various features, and it was slowly spinning
out of control.



Since then, my position
has been that nothing -- nothing -- goes in the RDBMS but data.  All processing
(by all, I mean "all", as in "all") belongs in proper programming language class
definitions which are part of a proper application software architecture that is
outside the RDBMS.  I have lots of arguments with people who want to blur the
line between "data" and "processing" by claiming that some processing is so
intimately tied to the data that it can legitimately be encoded in the RDBMS as
part of the persistent storage.  The argument is silly.  Data is persistent and
processing isn't -- they are fundamentally different. 




**Recent Questions.** 



One recent question was
nearly incomprehensible, and appeared to be an attempt to sort out a jumble of
C++ and PL/SQL.  



As a side, note, the
literal question was "What is the fastest way for C++ code to get data from
Oracle ? By fastest I mean w/ the least software overhead."  I have no idea what
this means.  Fastest means fastest, except to this questioner, where it means
least "overhead", whatever "overhead" might be defined as.  In addition to
proposing that faster means "faster", I proposed several definitions for
"overhead" but haven't heard back.



The
other recent question was part of proposing some work to implement some really
complex business rules.  The initial request was to build them in PL/SQL. 
Complex rules don't often work out well in PL/SQL, since the language is fairly
thin on sophisticated data structures.  Yes, the most recent versions have some
kind of collections and some notion of objects, but it isn't a first-class part
of the language the way it is in Java.  It's seems to be a creepy-looking
add-on.  



**Performance Comparison.** 



The comparison in
"`Java vs.
PL/SQL: Where Do I Put the SQL? <http://www.dbazine.com/oracle/or-articles/moore2>`_ " uses a very limited set of processing
steps.  It uses some simplistic queries that don't reflect real-world problems. 




To be specific, real-world queries are
rarely simple "SELECT COUNT(*)" queries.  They fall into a number of
categories.

1.  Simple COUNT(*) queries, with few or no bind
    variables.  These are a rarity in real-world applications, and aren't a good
    choice for a benchmark.

#.  Big queries, based on complex table
    definitions in the FROM clause, but few or no bind variables.  These are
    commonly part of rather complex data warehouse query processing, and don't often
    have complex selection criteria.  

#.  Closely-related families of queries with
    multiple WHERE-clause alternatives.  These are dismayingly common because the
    data model hasn't kept up with actual use cases.  We have to use complex
    conditions to work around some limitations of the
    data.



These third class of queries are
the interesting ones.  These are the queries where you have to use CASE, DECODE
and NVL constructs.  These are the kinds of queries where you have a number of
variants, and you have to resort to "Cursor Variables" in
PL/SQL.



These, generally, are also
queries for which SQL is not completely appropriate.   If you have a problem
that sits squarely in SQL's sweet-spot, PL/SQL is a likely best-choice for
processing.



**Sample Problem.** 



Let's look at a sample
problem that portrays a more realistic problem.  Let's look at a common kind of
"near-miss" matching.  This happens when comparing work hours with work
requests, invoices with purchase orders, shipping manifests with advanced
shipping notices, manufacturing orders with shipments, etc.  In many cases,
these involve multi-way matches as we compare our vendors, our internal
processes, our logistics and our sales.  In extreme cases where we are the
vendor managing inventory at our customer's location, this can involve matching
customer logistics and sales records with our
records.



Typically, we have business
rules that match two documents based on a series of rules.  The first kinds of
rules look for exact matches, the subsequent business rules relax the criteria
in various ways to find a "near miss"
match.



There are a number of relaxation
approaches that are common:

-   Replacing an equality test (on numbers or
    dates) with a BETWEEN clause

-   Testing for equality of a nullable field
    (using IFNULL or NVL functions, or CASE expressions)

-   Testing for similarity of strings with a
    LIKE clause

-   Replacing an equality test with an EXISTS
    clause



Notably absent is the IN clause,
which isn't often "relaxed" into a less strict comparison.  When IN conditions
are changed it usually means adding additional values to the IN list, which is
essentially the same test.



We'll use
the first two kinds of comparison relaxations on numeric and date fields.  We
can create two hypothetical matching rules:

1.  Exact match on three fields.  This will be a
    query of the form WHERE num=? AND date=? AND NVL(optional,-1) = ?

#.  Range match on two of the three fields and
    exact match on the third.  This will be a query of the form WHERE (num BETWEEN ?
    AND ?) AND (date BETWEEN ? AND ?) AND (NVL(optional,-1) =
    ?)



We'll wind up with two
closely-related queries.  The matching algorithm will attempts the exact match
query first, then the near-miss query
second.



**Procedural Optimization.** 



This problem is
amenable to a non-database optimization.  This is a common optimization, and
I've talked about it at PyCon and seen some folks following up with similar
implementations.



Here's the secret: a
HashMap (a Python dictionary, indexed by tuples) is blazingly fast, far faster
than any RDBMS can ever be.  Other than customer data for utilities or banks,
you can almost always fit all the data in memory.  10,000 Java or Python objects
is not too much to fit into memory on modern
processors.



The common optimization is
to load one of the two document collections into a HashMap, keyed by the "exact
match" criteria.  Then, you can query the other document collection, do a nearly
instantaneous lookup in the HashMap.  if you don't find what you're looking for,
then you can fall back to the "relaxed" SQL query. 




This gives you a number of
implementation alternatives:

-   Pure SQL.  There really are two queries:
    the exact lookup query, and the relaxed ("near miss") query.

-   One Dictionary.  In this case, you load a
    dictionary (or HashMap) with one document collection, and do the exact lookup in
    the HashMap.  The near-miss query is still used for the special
    cases.

-   More Dictionaries.  In some cases, you
    can partition the document collection into a number of "closely-related"
    buckets.  You can use a fast Hash to locate a bucket which contains a number of
    candidate documents.  You can iterate through the collection of candidates
    looking for the best near-miss
    match.



**Sample Code.** 



The sample code is here to
show the algorithms -- in general.  The specific PL/SQL code and Java code
mirror this Python reference information
precisely.



Here's the basic, Pure SQL
algorithm, in Python.  I'm using Python and SQLAlchemy to simplify the
presentation.  PL/SQL and Java are god-awful wordy and long for precisely the
same piece of code.



..  code:

::

    def pureSQL():
        """Pure SQL matching."""
        # Get a working session
        session = create_session(bind_to=engine)
        invoice_qry= session.query(Invoice)
        manifest_qry= session.query(Manifest)
    
        # Match invoices
        count= 0
        match= 0
        nearMatch= 0
        multiMatch= 0
        nonMatch= 0
        for man in manifest_qry.select():
            invoices= invoice_qry.select_by(
                invtotal=man.mantotal, invdate=man.mandate,
                shiptocust=man.shiptocust )
            if len(invoices) == 1:
                match += 1
            elif len(invoices) > 1:
                multiMatch += 1 #multiple candidates!            
            else:
                totW= 10
                dateW= datetime.timedelta(10)
                candidates= invoice_qry.select( and_(
                    invoice_tbl.c.shiptocust==man.shiptocust,
                    invoice_tbl.c.invtotal.between(man.mantotal-totW,man.mantotal+totW),
                    invoice_tbl.c.invdate.between(man.mandate-dateW,man.mandate+dateW) ) )
                if len(candidates) == 1:
                    nearMatch += 1
                elif len(candidates) == 0:
                    nonMatch += 1 # non-match
                else:
                    multiMatch += 1 #multiple candidates!
            count += 1
        print "Manifests", count
        print "  matches", match
        print "  near matches", nearMatch
        print "  multiple near matches", multiMatch
        print "  non-matches", nonMatch





Here's the One Dictionary algorithm,
in Python.  The only change is on lines 25 and 26.

..  code:

::

    def oneDict():
        """Use a single dictionary for complete matches."""
        # Get a working session
        session = create_session(bind_to=engine)
        invoice_qry= session.query(Invoice)
        manifest_qry= session.query(Manifest)
    
        # Load the high-speed lookup dictionary
        invDict= {}
        for inv in invoice_qry.select():
            key= ( inv.invtotal, inv.invdate, inv.shiptocust )
            invDict[key]= inv
        print "Invoices", len(invDict)
        totW= 10
        dateW= datetime.timedelta(10)
    
        # Match invoices
        count= 0
        match= 0
        nearMatch= 0
        multiMatch= 0
        nonMatch= 0
        for man in manifest_qry.select():
            invkey= ( man.mantotal, man.mandate, man.shiptocust )
            if invDict.has_key( invkey ):
                match += 1
            else:
                candidates= invoice_qry.select( and_(
                    invoice_tbl.c.shiptocust==man.shiptocust,
                    invoice_tbl.c.invtotal.between(man.mantotal-totW,man.mantotal+totW),
                    invoice_tbl.c.invdate.between(man.mandate-dateW,man.mandate+dateW) ) )
                if len(candidates) == 1:
                    nearMatch += 1
                elif len(candidates) == 0:
                    nonMatch += 1 # non-match
                else:
                    multiMatch += 1 #multiple candidates!
            count += 1
        print "Manifests", count
        print "  matches", match
        print "  near matches", nearMatch
        print "  multiple near matches", multiMatch
        print "  non-matches", nonMatch





**Comparison Results.** 



Here's the important part.
I ran the Python, PL/SQL and Java versions on my Dell Laptop using Oracle 10 XE.
Since it's Oracle, the results are widely applicable.  (I often do this kind of
thing in SQLite, which leads to some disputes.)  Also, since it's all on a
single single-core box, it's the worst case.  A more complex architecture will
perform better.



I built about 4000
random invoices and 4000 random manifests that need to be matched.  About 2000
matched exactly, the remaining 2000 had about 1000 near-miss matches and about
1000 non-matches.  The numbers aren't exact because I use random number
generators and there are 81 documents which were supposed to be near misses, but
happened to be exact matches.  When you miss by zero, it looks like a
hit.



..  csv-table::

    "PL/SQL","Java"
    "24 sec.","7.7 sec."







Java is much faster than
PL/SQL.



How is this
possible?



Easy.  Java isn't competing
for scarce resources.  Java runs outside the RDBMS, where it has unlimited
processor resources.  PL/SQL, on the other hand, is just one of the things that
the RDBMS is doing.  Further, Java has JIT translation to hardware-speed
processing, something PL/SQL lacks.  Finally, Java has a slick optimizer
available to further reduce
overheads.



**Further Performance Improvement.** 



As if Java isn't fast
enough, we can squeeze a lot more performance out of this process by reducing
the SQL operations.  As mentioned above, we can replace some of the SQL with a
HashMap.  This has the following effects.



..  csv-table::

    "Algorithm","Java","Python"
    "Pure SQL","7.8 sec.","31 sec."
    "One Dictionary","3.5 sec.","12.5 sec."
    "Two Dictionaries"," ","9.7 sec."

    






Yes, Python plus SQLAlchemy is slow. 
That's not the point.



Eliminating the
exact-match SQL, cuts the run time to 0.4 of the pure SQL run time.  Replacing
all of the matching SQL reduces the run time to 0.3 of the original.  This
reflects a tradeoff between a more complex setup (which takes some of the
run-time) vs. a faster match algorithm. 




We'd predict a final run time of 2.4
seconds in Java.  However, I got bored of coding this in Java, since it's rather
tedious.



**Conclusion.** 



You
want things to run faster?  An order of magnitude faster?

1.  Replace PL/SQL with Java.

#.  Replace SQL lookups with in-memory HashMap
    lookups.



With some hard work, you can
change 24 seconds of processing to 2.4 seconds of processing.






















