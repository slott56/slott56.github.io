Essay 15 - Errors and Exceptions
================================

:date: 2005-09-19 18:00
:tags: architecture,software design
:slug: 2005_09_19-essay_15_errors_and_exceptions
:category: Architecture & Design
:status: published





When we embed explicit constraint checking into a
design, they can occur in any of the available tiers: persistence (database),
access, model, control or view.  Some of these options are easier to consider
than others.  The view tier, for instance, merely has responsibility for
presentation and should be able to cope with any data provided.  The other
tiers, however, do require some tradeoff
analysis.



The database tier is
appealing, but problems here can escalate because database triggers and checks
interact in subtle ways, and cascading trigger operations can consume precious
shared resources on a centralized database
server.



The access tier is appealing,
but often it is simply JDBC or CORBA connectivity.  Enhancing this with
application-specific constraints seems to be like cluttering the view tier with
application-specific features.  This may be appropriate, but may also limit
reuse as well distribute rules into unexpected
locations.



Remaining are the model and
control tiers.  Some contraints are essential, structural features of the model.
Many however, are a matter of enforcing a range of values that involves subtle,
mutable or weakly defined business semantics.  In this case, the control tier is
ideal, since these are part of the actor's interaction, not part of the essence
of the data model.



Having allocated
most constraints to control-related packages, we note that constraints reveal
two kinds of problems: design problems and operational problems. We also note
that software lives on a development phase of its life and a deployment phase. 
This gives us the following four places where constraint violations can be
discovered.



**Design Problem found in a Design Phase** .  Excellent.  Just
what we hoped for.  Thrown exceptions are very nice here: the application
crashes with a traceback dump that can be used for diagnosis.  The tools for
locating design problems are highly specialized.  Constraints in the code that
locate design problems at design time are nice to have; they are like JUnit test
cases.  Note that these are not part of the problem or the solution, they are
part of the software development process, and should stay there. It's on the
same order of utility as a debugger - fine for programmers, but not fine for end
users.



**Design Problem found in a Deployment Phase** .  The root cause is a
failure in the software development process.  The question is how to detect
these.  My preference is to avoid masking them with "clean", "user-invisible"
error handling.  The application is badly broken if it has design flaws. 
Silently ignoring these problems is bad.  Crashing outright, in some contexts is
bad, too.  There's a fine line here.  My preference is to crash, but application
errors logs with full tracebacks that help diagnosis are good when they are read
and acted upon by
developers.



**Operational Problems found in a Design Phase** .  Hmmm. 
While some would say this is just good design -- "idiot-proofing the software"
-- I disagree.  If operational problems are discovered during testing, it means
the requirements may have been wrong in the first place.  Note that we are not
talking about mechanisms to prevent fraud and abuse, those are ordinary
requirements.  We are talking about users trying to put textual notes in an
amount field, or creating domain-specific nulls.  

Example of a domain-specific null is
creating a goofy-looking default date (e.g., 10/29/1892) because the date is
mandatory but not actually available.  Using a goofy-looking amount (e.g.,
-9999.99) for the amount because it is mandatory in the software, but not in the
business process.



**Operational Problems found in a Deployment Phase** .  There
are two cases here.

1.  **Operational Problems** . Bad operation means that the actor
    was mistaken in their understanding of how to create business value: wrong goal,
    wrong software to meet that goal, etc. Constraints may help discover this.
    Typically a few key constraints will find this situation very early in the
    user's experience.  These are clearly part of the control layer, and meaningful
    diagnostic messages are important to alerting the actor that their actions are
    inappropriate for this piece of the system, but may be more appropriate with a
    different piece of the system.

#.  **Software Problems** .  Other than bad design, bad software
    usually means the business context has changed, and the software has not. This
    is ordinary evolution, and overly constrained software is an impediment, not a
    solution.  Again, a few key constraints to locate the situation and support
    diagnosis is the most important step.  The user's response, however, is
    different, because they are now asking the system to behave differently instead
    of using the system differently.



Note
that constraints lead to (1) development, (2) maintainence cost and (3)
adaptation cost.  Too many constraints, and inappropriately located constraints
will make adaptation costly, with the consequence of making business evolution
slow and complex.



When a constraint is
added to an application, there are two design considerations for the situation
we are trying to prevent.

-   If we omit the constraint, what breaks?
    The Law? Industry practices? The company structure? The line of business? An
    operational process?

-   If we omit the constraint, what is the
    nature of the breakage? OS crash? Application crash? Missing or damaged data
    with legal or financial consequences? Inconvenience?
    Confusion?



In short, is there a
reasonable return on the investment?













