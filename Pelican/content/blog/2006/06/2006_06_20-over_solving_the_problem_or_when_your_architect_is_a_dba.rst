Over-Solving the Problem or When your architect is a DBA...
===========================================================

:date: 2006-06-20 20:22
:tags: architecture,software design,complexity
:slug: 2006_06_20-over_solving_the_problem_or_when_your_architect_is_a_dba
:category: Architecture & Design
:status: published





R. Lucente shared an email with me that included
`Cary Millsap's <http://www.hotsos.com>`_   Volume Theorem.




*Theorem*:

    **No human wants to see more than 10 rows. Ever.**



Which caused me to wonder why
anyone would ever use an RDBMS as a slow, complex, high-overhead message queue. 
I've seen it done several times, and in all cases, it was considered A Bad Thing
after it had been in production for a while.  Either it was slow or it was
inflexible.



Why do we end up with this situation?



I had a DBA tell me that the
user registration application shouldn't directly update the LDAP server. 
Instead, the users should be placed in the database, where Oracle's DIPTEST
process would take the changes out of the database and apply them to the LDAP
directory.  He was adamant about it: the RDBMS was the sacred truth and
bypassing the RDBMS put the application in a state of
sin.



It turns out that there are some
things DIPTEST can't do.  The database-centric philosophy did us more harm than
good.



The RDBMS-as-Reliable-Message-Queue design pattern
---------------------------------------------------



We use the RDBMS as a
message queue for the same reason we use it as a front-end to the LDAP server. 
The RDBMS is the biggest, most expensive, most visible and most central
persistence mechanism we see.  We can't or don't see the file system, because
it's free with our OS; we take it for granted. 




So what features do we get from the RDBMS As Message Queue?



1.  **Reliability**.
    The RDBMS has logs and rollback space and carefully designed algorithms to
    assure that dirty cache storage is written to disk quickly.   Why not just write
    a file or two to different devices?  Isn't that multiple-device write what's
    going on under the hood in the RDBMS?



2.  **Scalability**.
    Multiple writers or multiple readers can share the RDBMS.  Multiple writers is
    easily handled by multiples files in a directory.  Multiple readers is easily
    handled by isolating the state information that describes "next transaction"
    from the multiple processes which execute individual
    transactions.



3.  **Recoverability**.
    When the transaction is finished, we can update the record in the RDBMS to show
    that it's complete.  Why?  To promote a reliable restart in the event of a
    crash; that way we won't reprocess queued transactions.  Why not write a second
    file of completed transaction id's?  At startup, read and locate transactions
    that are in the queue but not in the completed transaction file.  It can't take
    more than a second or so to write an updated, unprocessed transaction queue, and
    then be up and processing
    again.


Why did the RDBMS win out over simple files?
---------------------------------------------



My current
theory is that architecture depends on the project manager.  It's all about the
manager's level of comprehension of the technology choices, their level of trust
in their information sources and their involvement in the project.   It has
little to do with applying technology to solve a problem -- unless the PM
actually makes an effort to (1) be involved, (2) comprehend the alternatives, and (3) have a
trusted source of technology directions.



I've been undermined by all three.



No involvement means that the
client DBA's opinion carries more weight than mine.  Until things don't work,
and then the DBA can easily recast their insistence as a suggestion or a
preference.



No comprehension means that
the project sticks to what the project manager actually knows.  If the PM's
technical expertise includes RDBMS, then everything has to include a database. 
If the PM doesn't understand star-schema design, then the warehouse will not be
a usable warehouse -- it will be highly normalized and look like an OLTP
application database.



No trusted
sources mean that decisions get made, revoked, and then reinstated.  This isn't
about learning something and making a change based on new information. 
(Politicians call learning and changing "flip-flopping" and make it sound bad;
it's just learning.)  I'm talking about the extreme case of making the decision
to do X, backing down on that decision because X really is a bad idea, then
reinstating the decision to do X because the alternative isn't trusted
enough.



Don't Over Solve
----------------



Millsap's point is really
important.  It's about the people -- the actors, the use cases, the information,
decisions and actions.  If we are solving their problem, then we can make
rational technology choices.   The RDBMS-As-Message-Queue is grotesque overhead
for a tiny problem of reliable application integration.  TIBCO would have been
cheaper.  A file or two would have been
simpler.



But how do we know in advance
which is better: RDBMS-As-Message-Queue or File-As-Message-Queue?  The decision
is easy to make.
It depends on answering the following question: **are we are over-solving the problem?**



We're over-solving the
problem when the RDBMS-As-Message-Queue has added features like locking,
rollbacks, schema management, and -- worst of all -- ad-hoc query capability. 
We don't need these features, so why are they here?  We only need a couple of
files.  So, just build readers and writers for a couple of files and be
done.








