SQL Can Be Slow -- Why Do People Doubt This?
============================================

:date: 2010-09-30 13:03
:tags: data warehouse,#python,SQL
:slug: 2010_09_30-sql_can_be_slow_why_do_people_doubt_this
:category: Technologies
:status: published

Here's a typical problem that results from "SQL Hegemony" -- all data
must be in a database, and all access must be via SQL. This can also be
called the "SQL Fetish" school of programming.

**War Story**. On a Data Warehousing project, we had to load and
process the organizational hierarchy. SQL doesn't do hierarchies well
because they can (and should) involve an join of indefinite depth.
One of the DBA's wanted to use a "pure SQL" traversal of the
hierarchy.

My opinion was that it was a waste of code. We were writing Java
programs. We could -- trivially -- fetch the entire tree into Java
objects and work with the hierarchy as a hierarchy.

The DBA finally "won" because of the SQL Hegemony argument -- all
access must be in SQL, right? I say "won" because we eventually had
to throw all the SQL away and use flat files. A "pure SQL" data
warehouse is generally unacceptably slow for loading. Data mart
subsets can be done in pure SQL, but loads can't.

**Recent Events**. "a table called [LOTSADATA] and it has 14.7
million rows. One of the columns in [LOTSADATA] table is BRAND" for
which they need to do a select distinct. "The disadvantage of [SELECT
DISTINCT] is that the Oracle database engine will do a sort which is
an insanely expensive operation.

    Question: Are there alternative approaches to obtaining the unique
    brands in a table?"

Response 1. **Duh**. Of course there are alternatives. What are you,
stupid? You have programming languages. Use them.

Response 2. **You're kidding, right**? Why ask me? Why not just run
it? How hard can it be to benchmark this? What are you, stupid?
Seriously.

Response 3. **Oh**. SQL Hegemony. Folks are actually *arguing* about
the cost of a query and -- it appears -- no one can actually write
the eight lines of code required to demonstrate that SELECT ALL is
faster than SELECT DISTINCT.

[Sorry for calling you stupid. You're paralyzed by fear, not
stupidity. What if SQL isn't the perfect end-all, do-all language? If
SQL isn't perfect for all data processing, what other lies have we
been living? Is this the end of organized data processing? The
collapse of western civilization?

Indeed, I'm repeatedly shocked that the question even comes up. And
I'm more shocked that the "appeal to authority" argument has to be
used. It's trivial to measure. It appears that it's easier to ask me
than to gather data.]

**Edit**. SQL Hegemony? Yes. Rather than run a demonstration program,
written in Java or C# or Python, they argued about the SQL. Doing
this with minimalist SQL didn't seem to make anyone's radar. Why not?
SQL Hegemony. Rather than consider real alternatives, everyone was
reduced to looking for sneaky SQL tricks.

**Benchmarking**. Here is what I did. It's 5 lines of code for each
case. [How hard can this be? Apparently, SQL hegemony makes it
*impossible* for some organizations to do even this.]

::

    def select_distinct():
        q1= db.cursor()
        q1.execute( "SELECT DISTINCT BRAND FROM LOTSADATA" )
        print q1.fetchall()
        q1.close()

    def select_all():
        q2= db.cursor()
        q2.execute( "SELECT ALL BRAND FROM LOTSADATA" )
        print set( q2.fetchall() )
        q2.close()

**Notes**.

-   I only simulated 100,000 rows. [I don't have the patience to wait
    for 15 million rows to be created, loaded and queried.]

-   The table only had four columns.

-   I used SQLite3 -- which is mostly in-memory -- and runs much, much
    faster than Oracle.

-   The select all is not a specious result based on cache being
    filled; the results are repeatable in any ordering of the queries.

**Results**.

select_distinct 0.417096

select_all 0.162827

For this data, the SQL SELECT DISTINCT took almost 3x as long as
the SELECT ALL. It's just that simple.

Want more speed? Use array fetch features to get more rows in bigger
buffers.

**Consequences**.

This is not rocket science. **SQL can be Slow**. Don't Argue:
Benchmark. Your Mileage May Vary.

SQL databases do locking, transaction management, backup and recovery
and a **bunch** of things well. SQL databases are helpful and
necessary. However, SQL isn't always fast.

**SQL means Slow Query Language**. You've been told.



-----

SQL can handle hierarchies just fine, we have been...
-----------------------------------------------------

dwelden<noreply@blogger.com>

2010-09-30 12:27:01.964000-04:00

SQL can handle hierarchies just fine, we have been doing it for years.
See http://en.wikipedia.org/wiki/Nested_set_model or
http://kamfonas.com/wordpress/wp-content/uploads/2007/08/recursive-hierarchies-no-columns.htm.
I use a slight modification of the Kamfonas approach which also includes
the parent member in the row. This makes certain queries a little
simpler, and simpler is faster.


if program needs SELECT DISTINCT that badly, why d...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-09-30 21:41:20.754000-04:00

if program needs SELECT DISTINCT that badly, why don't you keep a table
with such results and select from it?
``select * from distinct_brands;`` -- will do the trick
+ update, that table from time to time when new data arrives.


Don&#39;t Blame SQL and relational databases that ...
-----------------------------------------------------

Dragan Sahpaski<noreply@blogger.com>

2010-10-01 08:51:10.908000-04:00

Don't Blame SQL and relational databases that your company staff are not
creative. Also SQL is a language. You probably wanted to say that
relational databases can be slow. Not SQL. SQL can also be implemented
in a non-relational database environment.


Ok, but say you want to only display the top 100 r...
-----------------------------------------------------

Matthys Meintjes<noreply@blogger.com>

2010-10-01 02:08:54.589000-04:00

Ok, but say you want to only display the top 100 results to the user -
do you still pull all 14.7 million before doing the paging, or do you do
the paging on the server (which forces you to do the DISTINCT on the
server as well)?

That's the problem with doing programming side manipulation on sets -
its usually too expensive retrieving all data before doing the
filtering.


rottweiler — you should read even rants with more ...
-----------------------------------------------------

Brandon Rhodes<noreply@blogger.com>

2010-10-01 00:04:41.288000-04:00

rottweiler — you should read even rants with more attentiveness. Yes,
'SELECT ALL' and 'SELECT DISTINCT' are “both SQL,” as you claim. But the
point is not whether one solution uses SQL and the other not —
obviously, every approach towards selecting the brands will have to
involve SQL because the data is stored in a table! The point is that the
'SELECT DISTINCT' solution is \*only\* SQL, whereas the alternative
approach combines a SQL statement that does not actually answer the
question (“What is the list of distinct brands?”) with post-processing
that reduces the data to a meaningful answer. That is the point: not
that both solutions involve SQL; but that one of them involves \*only\*
SQL, and that in some enterprises that is considered a necessary
attribute of \*any\* solution.


Your post is a rant.

So the choice is between &#3...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2010-09-30 11:29:04.923000-04:00

Your post is a rant.
So the choice is between 'SELECT ALL' and 'SELECT DISTINCT'. How is one
an example of "SQL Hegemony" and the other isn't? They're both SQL.
And your supposedly revolutionary timing code doesn't prove anything ...
they don't do the same thing. Doing less is faster than doing more, big
surprise.


Matt said ... want to only display the top 100 res...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-02 08:50:19.420000-04:00

Matt said ... want to only display the top 100 results ...
That is a different question than "provide a DISTINCT list of ALL the
values".

For a discussion of the "Top N query" problem, refer to
Processing Rows in Batches
http://www.drdobbs.com/184406071
Full disclosure: The above is a Dr. Dobb's article that Steve and I
co-authored.


Please note that the blog states &quot;One of the ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-01 19:44:38.101000-04:00

Please note that the blog states "One of the columns in [LOTSADATA]
table is BRAND for which they need to do a select distinct". In other
words the goal is to produce a list of distinct brands.

Ideally you would never be in this silly situation and would keep the
number of distinct brands somewhere else as one of the commenters
stated.

I think what is missing from the blog is the Python code that processes
the "select all" output through a Python "sets" to product the distinct
brands.
http://docs.python.org/tutorial/datastructures.html


For doing hierarchies in sql, some good references...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-10-01 19:34:32.593000-04:00

For doing hierarchies in sql, some good references are
1) Article: Trees in SQL by Joe Celko
http://intelligent-enterprise.informationweek.com/001020/celko.jhtml;jsessionid=X4HTCAP5KAJGPQE1GHRSKHWATMY32JVN
2) Book: Joe Celko's Trees and Hierarchies in SQL for Smarties
3) Some vendors like Oracle, have special knobs for hierarchical queries
CONNECT BY, LEVEL, PRIOR CONNECT_BY_ROOT
http://download.oracle.com/docs/cd/B19306_01/server.102/b14200/pseudocolumns001.htm#i1009313
http://download.oracle.com/docs/cd/B19306_01/server.102/b14200/operators004.htm#i1036358
http://download.oracle.com/docs/cd/B19306_01/server.102/b14200/queries003.htm#i2053935
4) Flatten the hierarchy using Kimball's bridge table concept


As per Dragan Sahpaski&#39;s post said, this isn&#...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-10-03 22:46:38.567000-04:00

As per Dragan Sahpaski's post said, this isn't a feature of SQL it is
one or more of; the database, the database configuration, etc.
The "select all" piped into a sort is really VERY inefficient, I can't
(and I won't) comment on the Oracle database you have but with a
database that has some good out of box defaults the database engine
should be a lot faster at sorting than the client. I tried out the idea
using Vectorwise and the dbt3 database and doing the sort is much
quicker in the database, I've in-lined the results below but the summary
is DBMS sort 0.164s versus 3.426s no sort and pulling the data back to
the client (and not applying a sort). This uses a table with ~6million
rows where 200K of the "distinct" column are unique. I should make clear
that this table is NOT indexed :-)

Doing the sort client side doesn't make any sense for this example if
you have a decent DBMS that has been configured correctly.
Someone already posted about trees in relational table approaches. If
you truly have a lot of data you can't store this in memory so you need
another approach (that may or may not be a relational DBMS).
Chris

Full disclosure: I work for Ingres so I'm likely to have some bias :-)

::

    [ivw@ingres_vw ~]$ cat /tmp/t.sh
    #!/bin/sh
    # Ingres Vectorwise dbt3 demo database
    sql dbt3 </tmp/1.txt </tmp/2.txt <<EOF
    select all l_partkey from lineitem\\p\\g
    EOF
    [ivw@ingres_vw ~]$ sh /tmp/t.sh
    INGRES TERMINAL MONITOR Copyright 2009 Ingres Corporation
    Ingres VectorWise Linux Version VW 1.0.0 (a64.lnx/114)NPTL login
    Sun Oct 3 19:21:34 2010
    continue
    \* /\* SQL Startup File \*/
    help lineitem
    Executing . . .
    Name: lineitem
    Owner: ivw
    Created: 17-aug-2010 10:54:23
    Type: user table
    Version: II10.0
    Column Information:
    Key
    Column Name Type Length Nulls Defaults Seq
    l_orderkey integer 4 no no
    l_partkey integer 4 no no
    l_suppkey integer 4 no no
    l_linenumber integer 4 no no
    l_quantity float 4 no no
    l_extendedprice float 4 no no
    l_discount float 4 no no
    l_tax float 4 no no
    l_returnflag char 1 no no
    l_linestatus char 1 no no
    l_shipdate ansidate no no
    l_commitdate ansidate no no
    l_receiptdate ansidate no no
    l_shipinstruct char 25 no no
    l_shipmode char 10 no no
    l_comment varchar 44 no no
    continue
    \* select count(*) from lineitem
    Executing . . .
    +----------------------+
    \|col1 \|
    +----------------------+
    \| 6001215\|
    +----------------------+
    (1 row)
    continue
    \*
    Ingres VectorWise Version VW 1.0.0 (a64.lnx/114)NPTL logout
    Sun Oct 3 19:21:34 2010
    distinct returns 200000 rows
    real 0m0.164s
    user 0m0.104s
    sys 0m0.008s
    real 0m3.426s
    user 0m3.152s
    sys 0m0.262s


As per Dragan Sahpaski&#39;s post said, this isn&#...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-10-03 22:45:36.723000-04:00

As per Dragan Sahpaski's post said, this isn't a feature of SQL it is
one or more of; the database, the database configuration, etc.
The "select all" piped into a sort is really VERY inefficient, I can't
(and I won't) comment on the Oracle database you have but with a
database that has some good out of box defaults the database engine
should be a lot faster at sorting than the client. I tried out the idea
using Vectorwise and the dbt3 database and doing the sort is much
quicker in the database, I've in-lined the results below but the summary
is DBMS sort 0.164s versus 3.426s no sort and pulling the data back to
the client (and not applying a sort). This uses a table with ~6million
rows where 200K of the "distinct" column are unique. I should make clear
that this table is NOT indexed :-)

Doing the sort client side doesn't make any sense for this example if
you have a decent DBMS that has been configured correctly.

Someone already posted about trees in relational table approaches. If
you truly have a lot of data you can't store this in memory so you need
another approach (that may or may not be a relational DBMS).
Chris

Full disclosure: I work for Ingres so I'm likely to have some bias :-)

::
    [ivw@ingres_vw ~]$ cat /tmp/t.sh
    #!/bin/sh
    # Ingres Vectorwise dbt3 demo database
    sql dbt3 </tmp/1.txt </tmp/2.txt <<EOF
    select all l_partkey from lineitem\\p\\g
    EOF
    [ivw@ingres_vw ~]$ sh /tmp/t.sh
    INGRES TERMINAL MONITOR Copyright 2009 Ingres Corporation
    Ingres VectorWise Linux Version VW 1.0.0 (a64.lnx/114)NPTL login
    Sun Oct 3 19:21:34 2010
    continue
    \* /\* SQL Startup File \*/
    help lineitem
    Executing . . .
    Name: lineitem
    Owner: ivw
    Created: 17-aug-2010 10:54:23
    Type: user table
    Version: II10.0
    Column Information:
    Key
    Column Name Type Length Nulls Defaults Seq
    l_orderkey integer 4 no no
    l_partkey integer 4 no no
    l_suppkey integer 4 no no
    l_linenumber integer 4 no no
    l_quantity float 4 no no
    l_extendedprice float 4 no no
    l_discount float 4 no no
    l_tax float 4 no no
    l_returnflag char 1 no no
    l_linestatus char 1 no no
    l_shipdate ansidate no no
    l_commitdate ansidate no no
    l_receiptdate ansidate no no
    l_shipinstruct char 25 no no
    l_shipmode char 10 no no
    l_comment varchar 44 no no
    continue
    \* select count(*) from lineitem
    Executing . . .
    +----------------------+
    \|col1 \|
    +----------------------+
    \| 6001215\|
    +----------------------+
    (1 row)
    continue
    \*
    Ingres VectorWise Version VW 1.0.0 (a64.lnx/114)NPTL logout
    Sun Oct 3 19:21:34 2010
    distinct returns 200000 rows
    real 0m0.164s
    user 0m0.104s
    sys 0m0.008s
    real 0m3.426s
    user 0m3.152s
    sys 0m0.262s





