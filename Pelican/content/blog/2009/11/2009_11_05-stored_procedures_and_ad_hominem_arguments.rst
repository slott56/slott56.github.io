Stored Procedures and Ad Hominem Arguments
==========================================

:date: 2009-11-05 21:07
:tags: stored procedures,architecture,design,triggers
:slug: 2009_11_05-stored_procedures_and_ad_hominem_arguments
:category: Technologies
:status: published

The question of "Stored Procedures and Triggers" comes up fairly
frequently.

Over the years (since the 90's, when stored procedures were
introduced to Oracle) I've learned precisely how awful a mistake this
technology is.

I've seen numerous problems that have stored procedures as their root
cause. I'll identify just a few. These are not "biases" or
"opinions". These are experience.

#.  The "DBA as Bottleneck" problem. In short, the DBA's take projects
    hostage while the development team waits for stored procedures to
    be written, corrected, performance tuned or maintained.

#.  The "Data Cartel" problem. The DBA's own parts of the business
    process. They refuse (or complicate) changes to fundamental
    business rules for obscure database reasons.

#.  The "Unmaintainability" problem. The stored procedures (and
    triggers) have reached a level of confusion and complexity that
    means that it's easier to drop the application and install a new
    one.

#.  The "Doesn't Break the License" problem. For some reason, the
    interpreted and source-code nature of stored procedures makes them
    the first candidate for customization of purchased applications.
    Worse, the feeling is that doing so doesn't (or won't) impair the
    support agreements.

When I bring these up, I wind up subject to weird *ad hominem*
attacks.

I've been told (more than once) that I'm not being "balanced" and
that stored procedures have "There are pros and cons on both sides".
This is bunk. I have plenty of facts. Stored procedures create a
mess. I've never seen any good come from stored procedures.

I don't use GOTO's haphazardly. I don't write procedural spaghetti
code. No one says that I should be more "balanced."

I don't create random database structures with 1NF, 2NF and 3NF
violations in random places. No one says I should be more "balanced".

Indeed, asking me to examine my bias is an ad hominem argument. My
fact-based experience with stored procedures is entirely negative.

But when it comes to stored procedures, there's a level of
defensiveness that defies my understanding. I assume Oracle, IBM and
Microsoft are paying kickbacks to DBA's to support stored procedures
and PL/SQL over the more sensible alternatives.



-----

There are times when SP have their place (procedur...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-11-06 11:30:03.472000-05:00

There are times when SP have their place (procedures processing lots of
data, procedures pulling together several queries/updates into one DB
call, rather than several network round-trips and also for use in
securing certain permissions, etc., to only within specific
function/procedures).

However... if your procedures are getting written by DBAs, and not
developers (who know PL/SQL (or whatever language) you have a bit
problem... you wouldn't allow Websphere administrator to insist on
writing all Java code, for example!

As for customers edition stored procedures - yes, this is a nightmare -
however, Oracle (and possibly other RDBMS providers) have mechanisms for
encrypting code, mitigating against this problem.


These are pretty arbitrary objections.  You could ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-11-05 15:11:07.666000-05:00

These are pretty arbitrary objections. You could apply complaints #s 1-3
to virtually any group within a software development organization -
Business Analysts, for example, or QA testers. It sounds to me like
you've just had bad experiences with "database people" and decided to
hold a grudge.

There are perfectly legitimate reasons to create stored procedures -
restricting permissions and attack surface, for example, or enhancing
performance by caching query plans for queries with complex logic. That
doesn't justify jamming everything into a proc, but as with everything
else in software development, stored procs are a tool, and can be used
and abused like any other tool. How much do you like those sysadmins who
write everything in completely unreadable Perl scripts? Or the BAs who
code all the business logic in convoluted VBA before handing it over to
a "real" coder to re-write?

I would recommend examining your biases, and giving the DBAs a break,
because if you came to me with that attitude, you're damn right I would
hold up your project while I tune your stored procs, because now I have
serious doubts about your ability to use them effectively.


If you don&#39;t allow the possibility that those ...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-11-04 13:23:43.718000-05:00

If you don't allow the possibility that those who disagree with you
could be anything but crazy or corrupt, then it seems optimistic to
expect respectful debate from them.

In environments where the database will be accessed and changed by
ad-hoc programs and by many different applications, there are good
reasons to keep logic bound unavoidably to the data instead of trying to
duplicate it separately in every potential channel of access. In this
case, it's important that there not be a sharp and hostile separation
between DBAs and developers. If you've never worked in situations like
that, though - if your data is always the tail and the application is
the dog, instead of the other way around, or if you've never had good
cooperation between DBAs and development - then yes, I suppose you've
never been in a situation where stored procedures could have helped.
Or maybe I'm crazy and corrupt, too.

It would help a lot if approaches like PL/Python were available outside
postgresql (or if more workplaces used postgresql). Wanting to use
stored procedures shouldn't restrict a person to using a single rather
aged and limited language, but in most databases, it does.


There are 2 reasons for stored procedures:

1. Men...
-----------------------------------------------------

nnis<noreply@blogger.com>

2009-11-04 15:21:25.810000-05:00

There are 2 reasons for stored procedures:

1. Mentioned by Catherine: You have multiple applications written in
different languages/platforms and no shared libraries between those
accessing the same data and you want to make sure that some validation
always takes place. To avoid duplication of code you write it in a
stored procedure. This is to make sure there is 1 source for the rules,
otherwise you might end up with various apps doing different things.

2. The stored procedure is doing massive data moves. For example you
move a million records form table A to B and it can't be expressed in
one SQL statement. By doing it in a stored procedure you can use
variables etc, but avoid all that data going out of the database
application over the wire to your application server into your
application and back.

Otherwise you are right: Avoid stored procedures as much as possible.
The people that know the application better are the developers, there is
more of them than DBAs, they know their programming language better than
whatever language the DB provides, they have better IDEs and debugging
tools. Programming in stored procedures and having to depend on the
usually fewer expert DBAs slows everybody down. Also if you ever decide
to switch database engines for your application you will have to rewrite
all your stored procedures. It is better to try to decouple your
application from your particular Database implementation.


If you work in an area where items #1 and #2 are r...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2009-11-05 10:04:32.095000-05:00

If you work in an area where items #1 and #2 are real, then you have a
"management" and "staffing" problem, not a "stored procedure" problem.
(This is especially true if your developers aren't the ones writing the
stored procedures.)


I agree with the article. 

I've also come to ...
-----------------------------------------------------

Christopher<noreply@blogger.com>

2009-11-04 14:20:22.719000-05:00

I agree with the article.

I've also come to this realization that stored procedures break the
programmer's ability to "fully grasp" the program. This also means that
unless the programmer using his language also knows the SP language,
then you now automatically involve two programmers, and neither can
"hold the program in their head". So then you end up having to write
down a lot of documentation (business rules, etc) that too can be
misleading, and requires an analyst and lots of writing, and meetings,
and now instead of one guy being able to crank out something good and
fast you end up with a team creating something bad and slow.

Why bad? Because no matter how well people think they can write down
what's in their brain, putting things down on paper or even
communicating verbally creates friction that does not exist if one
person is able to just think about the whole problem.

@catherine: even PL/python is a subset of the real python languange, and
does not have the full expressiveness of python + standard library +
third party tools and frameworks.

The other thing is that people think they need to protect the data from
the programmer, that they need an abstraction layer. I say: get better
programmers.


Don't know why someone would argue with you, c...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-11-04 22:13:37.041000-05:00

Don't know why someone would argue with you, clearly you are speaking
from personal experiences. They are what they are.

Triggers can definitely get out of hand and are, imho, the most single
most abused "feature" of any database. What seems like a god-send
rapidly deteriorates into a tangled mess of "magic bullets". If you see
a lot of triggers being used that should throw up some serious red
flags.


sigh...developers sure love to hate on the DBAs.
------------------------------------------------

SDC<noreply@blogger.com>

2009-11-04 21:06:24.283000-05:00

sigh...developers sure love to hate on the DBAs.


Stored procedures may just be another facet of ven...
-----------------------------------------------------

Anonymous<noreply@blogger.com>

2009-11-05 04:38:44.880000-05:00

Stored procedures may just be another facet of vendor lock-in. Using one
type binds you forever.


@ Ira: I too have had bad experience with "d...
-----------------------------------------------------

Christopher<noreply@blogger.com>

2009-11-06 05:41:59.595000-05:00

@ Ira:
I too have had bad experience with "dba" people then. It seems to be the
norm, too.
So while in theory stored procedures are a great too, in practice they
turn things into a complete mess. That's what he's saying.
Also, and he approaches this obliquely, he states that insisting on
stored procedures implies mistrust of the programmer's skills. That
can't be good for morale, and demoralized programmers hardly produce
good stuff.


My biggest problem with sps is that the become bla...
-----------------------------------------------------

flukus<noreply@blogger.com>

2009-11-05 05:19:15.873000-05:00

My biggest problem with sps is that the become black holes that all
business logic fall into.

Something might start out as a simple stored procedure but sooner or
later complex business logic starts creeping in. Then if more than one
app requires the same proc critical mass is achieved.

Sql is great at expressing set based logic but it sucks at expressing
business rules.

And don't get me started on all those code generators that write stored
procs "because their faster". Then end up creating the most horifically
slow code.imaginable.





