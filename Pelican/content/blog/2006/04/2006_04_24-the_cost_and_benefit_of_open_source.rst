The Cost (and Benefit) of Open Source
=====================================

:date: 2006-04-24 23:59
:tags: management
:slug: 2006_04_24-the_cost_and_benefit_of_open_source
:category: Management
:status: published





I've had this conversation more than
once.



Me: "We can download something
like `POI <http://jakarta.apache.org/poi/>`_  to read the Excel™ files.  Or I can
spend months writing something."



Them: 
"We have a policy against open source
software."



Me:  "Do you use `Apache <http://www.apache.org/>`_ ?"



Them:
"That's different."



Me:  "How so?  Be
specific in enumerating every difference between open-source Apache and
open-source POI."



Them:  "Fine, but
what about..."



1.  Bugs? 




Me: "Your software is a paragon of
virtue?"



2.  Viruses and Malware?



Me: "The other 1,000 users
will have found it and fixed it."



3.  Support?



Me: "You have their source. 
You have my source.  I'm leaving, eventually, you
know."



4.  Licensing?



Me:  "`Here <http://www.apache.org/licenses/LICENSE-2.0>`_ ."



**Varieties of Discomfort** .  This conversation is really
about discomfort with software where the focus is squarely on maintenance,
adaptation, integration and support.  The bottom line on discomfort is this:
"Who do you sue when something goes wrong?" 




Everyone denies that "who do we sue?"
is the bottom line.  But when you provide the license agreement to the CIO and
they provide it to the lawyers, the lawyer only looks at a few clauses related
to liability.  Everything else is -- well -- technical and not the lawyer's
problem.  Once it bounces back to the CIO, it can become a hand-wringing
exercise.



Previously, I mentioned
<{filename}/blog/2006/04/2006_04_22-the_role_of_open_source_in_the_enterprise_it_investment_strategy.rst> the "I don't see the value in converting"
conversation.  This misses the point of open source software entirely, reducing
it to a strange either-or proposition.  This tend to derail the conversation,
leaving the discomfort factor front and center, and ignoring the real issue of
cost and benefit.



This plays out into
the question "Is it really about replacement or is it about where new
development will be done?" http://www.haloscan.com/comments/slott/E20060422103757/#89360.  This question is still way off target,
since it provides a
*strategy* 
for conversion.  While a strategic direction (replace vs. evolve) might be a
nice thing to have, you can't establish a direction until after you address the
underlying discomfort issue.  Clearly, I can't say this enough times: it isn't
about
*converting* 
to open source.  That implies were converting
*from* 
something, and reduces the conversation to strange either-or
situations.



**Buy vs. Build** .  Tony notes http://www.haloscan.com/comments/slott/E20060422103757/#89484 that the real point is the minute
incremental cost in deploying open source software.  The incremental cost of
another *license to use*  is zero.  Support costs do rise with
number of desktops served.  Indeed, the costs of open source are often
comparable to proprietary software, but they're in-house costs.  The point is
that we can move beyond the tangential conversations about your level of
discomfort by focusing on two things:
**cost**  and
**benefit** .



A
focus on cost and benefit (and the tiny incremental cost of increasing your
usage) leads to the following:  **What's the best approach to acquiring the needed software?**   We used to call this question the
"Buy vs. Build" decision.  However, it's expanded into the following bewildering
spectrum of choices:

-   **Buy and Customize.** Possibly the least effective solution: begin
    with a standardized commercial product, then customize it so that it cannot be
    supported, maintained or enhanced.  

-   **Buy** .  Possibly the lowest risk solution: 
    purchase something standardized from a commercial vendor.

-   **Build** .  In this case, we want something
    totally unique, and hope we have the technical chops.  Emphasis on the
    *hope* ;
    not all organizations are structured to do development well.  Indeed, some IT
    organizations seemed to be intentionally structured to do development
    poorly.

-   **Build by someone else** .  The strange world of "we want the
    software, but not the collateral learnings that come from building the
    software."  Possibly even the worse situation of "we feel the process is more
    important than most of the products." ../C1076854706/E20060325113712.html

-   **Download** .  Possibly the most effective
    solution: download it.  Want to customize it?  While still a bad idea, it's more
    possible here than with something you
    purchased.



**Readiness Test** .  I think there are two elements of
readiness to implement open source
solutions.



1.  Desperation.



2.  Focus.



If you are
**desperate** 
to have your problem solved, you don't quibble about who you will sue.  When
I've had the frustrating tangential conversations focusing on discomfort, part
of the reason is that the customer isn't truly desperate to
*solve* 
a business problem.  Instead, they're busy implementing large and complex
application software, usually by building it from scratch.  They're proud of
their software development capabilities, and bypassing programmers by
downloading ready-to-hand solutions isn't what they want to
do.



If you are
**focused** 
on solving a problem, you can rationally evaluate the fit between a software
solution and the problem.  If you are doing something else, you have a million
other considerations that spin the conversation away from
*problem* -*and* -*solution* 
toward strategy, tactics, operational considerations, who do we sue, and other
tangents.



**Ramp Up** .  With all "new" directions, introducing a
new set of tools must be done incrementally.  It must be focused on solving a
problem where the customer is desperate.  Adding POI, for example, solved an
immediate problem.  We had to talk it to death, but the policy against open
source wasn't exactly as broad and silly as the customer initially described. 
Or, it wasn't inflexible in the face of a solution and a level of
desperation.



You'll always have a "one
true language" conversation `After PERL what? <{filename}/blog/2006/01/2006_01_27-after_perl_what_revised.rst>`_, but people will eagerly add Python to the
mix when there isn't a viable alternative.  Here's an
example:

1.  We need batch extractions to produce files for
    a variety of purposes.  We have a batch-job production control system with which
    it must interface.  Many kinds of tools can run in this environment, but GUI
    tools aren't a good choice.

#.  We need garden-variety CSV and Tab files, and
    SQL*Plus doesn't do this without a lot of pain.

#.  We need flexibility, but we don't want to
    spend $10K for an elaborate ETL or EAI application.  It's just CSV
    extracts.



A small technology stack
helps speed adoption.  Python 2.4 http://www.python.org/ and cx_Oracle http://www.python.org/pypi/cx_Oracle/4.1.2 allows them to write 10-line extraction
programs that run from the command-line in AIX or Windows, can be scheduled by
their tools, and can be modified without the egregious overhead of a Java
application.  



One tipping point was
the addition of the CSV library module in Python 2.3.  I've written CSV parsers,
and the regular expressions required to handle quote balancing are opaque.  In
the Python 2.3+ world, we can write a tidy chunk of code that expresses the
*Database to CSV™*  implementation with almost no
non-problem technology overheads.

[An example of a non-problem technology
overhead is the Java technique of locating a JDBC driver before opening a
connection.  Yes it's short, but it's also confusingly opaque when we only have
one vendor for our production
databases.]



**No Pain No Gain** .  The cost and benefit of Open Source is
only apparent if you have a specific problem to solve.  The derailing tangent
conversations about "converting" and the "value proposition" seem to happen when
discomfort with the approach is larger than the discomfort of the problem
itself.  If the problem isn't causing enough pain, then we are free to quibble
over solution strategies.



Consequently,
my real question is more fundamental.  It's not "why adopt open source?" nor is
it "how do we adopt open source?"  My question is "Are we ready to
**support** 
open source when (a) it solves our customer's problems and (b) they're ready to
adopt?"

















