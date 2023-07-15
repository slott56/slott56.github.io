Stating the Problem
===================

:date: 2006-01-20 12:01
:tags: architecture,software design,complexity,requirements
:slug: 2006_01_20-stating_the_problem
:category: Architecture & Design
:status: published





RL's blog http://rlucente.bloki.com/blog is
full of scrambling attempts at stating a problem.  While, in principle, stating
a problem is a trivial exercise (someone can't do something), RL has managed to
make it wonderfully complex.  The root cause of the complexity could be a
fundamental unwillingness to state the problem without including technology
hints like "database" or "hierarchy" or "project management" or "change
control".



**Context** 



When
the portal goes live, 10,000 people will want
accounts.



**Problem** 



The
help desk can't handle 10,000 account activation
requests.



The problem here will never
change.  My favorite technology may not solve this problem.  In spite of the
problem not being nuanced enough to justify a month of programming, that is the
problem.  It is only that, and it won't
change.



My advice?  Look at the people
you are supposed to be helping.  What can't they do?  In an hour of observing,
you should be able to figure out what they can't do and what is blocking them. 
The point of software is to remove constraints on their work-space so that they
can do more with
less.



**Forces** 



On
the one hand, we could hire a suitably-sized help desk staff for the week or so
that the desk will be flooded with account open requests.  10,000 requests
spread over 40 hours will be 250/hour, 4 each minute.  The calls aren't trivial,
we need to establish identity of the users, each call will take 5 minutes or
more.  You'd need a staff of 20+ to handle the flood; they'd only work for that
week.  



The portal toolset has a
self-registration portlet, but it has no validation, we'll need to add
functionality to establish identity.  Most of the 10,000 users are listed on an
employee file, where we have enough personally identifiable information to
establish identity.  Few of the 10,000 users have existing application or
network access accounts that can be used as part of single-sign-on
solution.



Some of the potential users
are at remote locations and remote security teams will have to establish
identity for them.  There's a workflow for requests involving the help desk,
remote security, and the help desk.



We
can't email people their passwords.  Direct mail, while possible, is also
expensive.  Further, direct mail is relatively removed from the high-tech image
of the portal.  This is marketing, and a high-tech portal needs a high-tech
registration process so that people can fully embrace this as central to their
work-life.



Some remote sites have LDAP
servers that we can interrogate to establish identity.  Some, however, do not,
and will require a more manual
process.



**Conclusion** 



All
of the various forces and nuances of the problem don't change the fundamental
problem.  There's something people can't do.  They can't establish identify and
create accounts for 10,000 users in the space of a week.  All of the other
forces that shape the solution don't change the
problem.



Now, folding in my technology
choices (J2EE, JDBC, Struts/JSF, etc.) doesn't change the
problem.



Adding features (logging the
interactions with the help desk, integrating with other LDAP servers,
bulk-loading people with existing accounts) doesn't change the
problem.



It's a hard discipline to
simply state what people can't do, and stick to it in spite of all the appealing
technologies and features.










