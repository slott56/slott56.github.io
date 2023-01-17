SQL Hegemony -- a sad state of affairs
======================================

:date: 2015-12-29 08:00
:tags: #python,performance,SQL,scalability
:slug: 2015_12_29-sql_hegemony_a_sad_state_of_affairs
:category: Technologies
:status: published


It appears that there are people who don't recognize SQL as a
tradeoff.

Here's a complex two-part question that can only come from folks who
firmly believe in the magic of SQL.

The sentence that got my attention was "Python has basically made SQL
obsolete as a language for data structure manipulation". My question
would be about scaling.  If [*we? you?*] have 30 million rows in a
table, would Python still be better than straight up SQL? The other
question would be about the amount of time to come up to speed. It
just seems easier to learn SQL than Python.


Also, in working with legacy DBA's who are starting to learn
Cassandra, I see similar magical thinking. Somehow, Oracle's behavior
can become a baseline in some people's minds. When Cassandra's column
database shows different behavior, there are DBA's who are
surprisingly quick to portray Cassandra as "wrong" or "confusing."
Worse, they'll waste a lot of time insisting that Cassandra is
misusing the term "key" because Cassandra's idempotency policy means
multiple INSERTS with the same primary key are handled differently
from Oracle. Labeling Cassandra as "wrong" is a similar problem to the
question.

Let's unpack the "SQL is better" question and see why this seems so
sad.

I'm not going to address the quote ("Python has basically made SQL
obsolete...") since that wasn't part of the question. That's just
background. And everyone seems to agree on this. The question appears
to be related to clinging to SQL in spite of Python's advantages.

But first, I have to note that the question violates some pretty
serious rules of engagement.

The Rules for Questions
-----------------------


Asking hand-waving hypotheticals is generally a pretty bad practice.
Sometimes, I'm completely intolerant, and refuse to engage. In this
case, I felt compelled to respond, in spite if the vacuousity of the
question.


First, of course, "better" is undefined in the question. That
essentially ends any conversation.

Second, there's no code. It's very hard to discuss anything without
code. All the hand-waving is essentially meaningless because when
code finally does show up, it will fit into some edge or corner not
properly covered by hand-waving.

Third, there's no possibility of code. There's nothing resembling a
tangible use case or scenario that can be turned into code for
comparison purposes.

Also,  the question seems to be creating a false dichotomy between
SQL and Python. This is a more subtle issue, and we'll look at this,
too.

Python Better Than SQL
----------------------


We can assign a number of potential meanings to "better". Some other
phrases -- "30 million rows in a table" and "about scaling" -- could
be dismissed as mere noise. Perhaps they're hints.

Let's assume it's about size of storage. Can Python deal with 30
million rows of data? Since we don't know the row size, there is no
actual answer. Without transactions or activities of some kind, we're
similarly bereft of the kinds of details that lead to a sensible
answer.

Let's say we're limited to 32Gb of memory. If the row size is up to
1Kb, we can fit all of the data in memory. We're pretty much done with
size and speed.  Python wins for the canonical CRUD operations.

Python wins because any code we write will be completely customized
for the data we're given. We're freed from generalized SQL type
conversion complexity, ODBC driver folderol, storage management
overheads, SQL language parsing work. Just the data manipulation. No
lock escalation or read consistency consideration. Done.

But wait. Not so fast, what about loading 32Gb into memory?

What about it? The problem is so delightfully vague that we have no
clue what "loading" might mean. Oracle takes a while to mount a
database and do other startup things. Python can open a file and slurp
in the data pretty quickly. If you want to amortize the loading time,
you can have smarter loader that brings in data incrementally.

::

    def load(data, key_col):
       with data.open() as source:
           rdr = csv.reader(source)
           table = { row[key_col]: row for row in rdr }
       return table

    def CRUD(table, key_col, update_col):
       row = tuple(random_text() for i in range(10))

       # INSERT INTO table(col,col,...) VALUES(val,val,...)
       table[row[key_col]]= row

       # SELECT * FROM TABLE WHERE key_col = value
       found = table[row[key_col]]
       #print( found )

       # UPDATE TABLE SET update_col = "value" WHERE key_col = value
       table[row[key_col]][update_col] = "special text"

       # DELETE FROM TABLE WHERE key_col = value
       del table[row[key_col]]

       # Is it gone?
       assert row[key_col] not in table




Rather than go for 30 million rows on this little laptop (with only
8Gb RAM), we'll load 30,000 rows each of which is about 150
characters. Small. The point, however, is this:

::

    load 0.133, CRUD 0.176

We can load 30,000 rows of data in 133 ms.  We can do 1,000 sets of
CRUD operations in 176 ms. The load time scales with total number of
bytes, row size × number of rows. The CRUD operation time will barely
move no matter how many rows or how big the rows are.

The problem with this kind of benchmark is that it plays to SQL's
strengths. It makes SQL look like the benchmark. We're forced to show
how some non-SQL language can also do what SQL does. And that's silly.

What About Bigger?
------------------


Let's pretend the number was supposed to be 30 billion rows of data.
Something that clearly can't fit into memory. Wait. Traditional SQL
databases struggle with this, too. Let's press on. 30 billion rows of
data. Each row is at least 1K in size. 3Tb of storage. Can Python do
this?

Recall that the question gives us no help in reasoning about "better".

What's the representation? 3Tb has got to be a implemented as
collection of smaller files. All of the files must have a common
format. Let's posit CSV. We don't really want all of this storage on a
single server. We want to farm this out to several hosts. And we
probably want to layer in some redundancy in case one of those hosts
fails.

Okay. It might not be obvious, but we're describing the HDFS from
Hadoop. We could -- without too much trouble -- implement an HDFS
surrogate that has very limited functionality in Python. We can use
SFTP to smear two copies of each file among a fixed-size farm of
servers. Very hard-wired, unlike Hadoop.

Then the reading part of our imagined app will scroll through the
collection of CSV-formatted files on each processor. We'd have to
implement a Hadoop map-reduce in Python. Again. Not very difficult if
we eliminate some features and stick to a very basic version
map-reduce. We can coordinate the reductions by implementing a simple
REST-based master-reducer that accepts the reductions from the other
processors and does the final reduce.

Now we have a lot of Python language overheads. Have we failed at
"better" because we polluted the solution with a fake Hadoop?

No.

The SQL folks had to install, configure, and manage a SQL database
that handled 3Tb of storage. The Python folks installed Python.
Installed their fake Hadoop. Then they used a few clever abstractions
to write delightfully simple map and reduce functions. Python still
handles the extremely large amount of data faster than SQL. Also, it
does this without some RDBMS features.

Which leads us to the second part of the question. Expressivity.

Easier to Learn
---------------


From the Question: "It just seems easier to learn SQL than Python".

This is pretty much meaningless noise. Less meaningful than the rest
of the question. Having taught both, I'm confident in saying that SQL
can be pretty confusing.

But.

More importantly.

There's no rational basis for comparison.

SQL DML is a very tiny language with only a few concepts. It's not a
Turing-complete programming language.

What's important is this:

We have to embed SQL in another language.
-----------------------------------------

You can't actually DO anything in SQL by itself. You need another
language.

In the old days, we actually wrote SQL in the middle of some other
programming language source. A pre-processor replaced SQL with the
other language's code. Now we use ODBC/JDBC or other drivers to
execute SQL from within another language. The embedding isn't quite so
literal as it once was. But it's still embedding.

The SQL vs. Programming Language is not an "either-or" situation. We
never have a stark choice between SQL or "some other language." We
always have to learn "some other language." Always.

That "other language" might be PL/SQL or TSQL or whatever scripting
tool of choice comes bundled with the database. It isn't SQL, it's
another Turing-complete language that shares SQL syntax.

Since "some other language" is **required**, the real question is "is
there value in **also** learning SQL?" Or -- most importantly --
"What's the value in spreading the knowledge representation around
among multiple languages?"

In some contexts, SQL can act as a *lingua franca*, allowing a kind of
uniform access to data irrespective of the application programming
language.

In most contexts, however, the SQL -- in isolation -- is incomplete.
There is application processing that has semantic significance. The
"do everything in stored procedures" crowd spend too much time in
raging denial that application logic is still used to wrap their
stored procedures.  No matter how enthusiastic one embraces stored
procedures, application code still exists, and still implements
semantically significant operations.

SQL is merely a short-hand notation for *potentially* complex
algorithms. It's an optimization. SQL elects for universality via
abstraction. It can't cover efficiency or scalability. We have to bind
in a representation and access algorithm to compare SQL performance
with another language's performance. Or scalability.

By itself, SQL is useless. So there's a false dichotomy implied by the
question.

The Head-To-Head Problem
------------------------


Above, I provided code that demonstrates SQL CRUD operations in
Python. This is, of course, silly. It presumes that SQL is the
benchmark standard which Python must meet.

What if we lift up Python as the benchmark that SQL has to meet?

Ooops.

We can trivially write things in Python which cannot be expressed in
SQL at all.  E.g., Compute the 1000th Fibonacci Number. For fun, go to
https://projecteuler.net/archives and pick any problem and try to
solve it in SQL. Try to even frame the problem in a way that the
solution can be expressed in SQL. SQL has profound limitations.

Okay. That's sort of like cheating.

Let's not raise the bar quite so high, then. Here's today's problem.

I got a spreadsheet with 100's of rows of student evaluations. It may
have come from Survey Monkey. Or not. It doesn't matter.

Most of the columns are some kind of Agree-Disagree scale. Other
columns are comments or usernames, or stuff in an open-ended domain.

Note that I don't know which columns. And I don't care. And I don't
need to care.

Here's how we tackle this in Python. It **can** be done in SQL. That's
the point. It's not impossible. It's just kind of complex. Especially
because the data loading either requires converting the data to a
sequence of INSERT statements or we have to use a "loader" which lives
outside the SQL language.

::

    from collections import Counter
    def summarize(data):
       with data.open() as source:
           rdr = csv.DictReader(source)
           summaries = {name: Counter() for name in rdr.fieldnames}
           for row in rdr:
               for key, value in row.items():
                   summaries[key][value] += 1
       for key in sorted(summaries):
           summary= summaries[key]
           if len(summary) == 5:
               print(key, summary)
           else:
               print(key, "More than 5 values")


This is the kind of thing that people do in Python that demonstrates
the limitations of SQL.  We've summarized all columns doing a
count/group-by in one pass through the data. We've build Counter
objects for each column name in the file. Each Counter object will
collect a complete histogram for a given column. We'll do all of the
columns at once.

This is scalable to millions or billions of rows and runs delightfully
quickly. Doing something similar with SELECT COUNT(*) FROM TABLE GROUP
BY SOMETHING is remarkably slow.  Databases are forced to do a lot of
on-disk sorting and temporary file creation. The Python Counter lives
in memory and works at in-memory speeds. Even for millions of rows of
data.

Summary
-------


Please define "better". Be explicit on what your goals are: speed,
ACID, reliability, whatever.

Please provide code. Or provide use cases that map directly to code.

Please stop clinging to SQL. Be realistic.

Please consider the basics: Does it capture knowledge effectively? Is
it expressive?

Please don't create dichotomies where none exist.





