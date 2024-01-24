The Twenty-Minute Solution
==========================

:date: 2006-04-05 15:49
:tags: web,cms
:slug: 2006_04_05-the_twenty_minute_solution
:category: Technologies
:status: published





First, let me get this off my chest: Django
http://www.djangoproject.com/ rules.  There are a number of reasons, but
they aren't the point of this
posting.



When someone creates a
twenty-minute application, they walk a fine line.  The minimalist approach to
software development can be viewed from two opposing points of
view.

1.  Small is **good** because there aren't many use cases, and over-engineering each use case doesn't
    add enough value.   Build something cheap using the defaults and built-ins. 
    Value comes from using it as soon as possible.

#.  Small is **bad** because there isn't enough control to prevent the users from abusing the
    application.  You must tightly constrain their use so it conforms to
    expectations irrespective of what they might do wrong.  Value comes from control
    over the users.



Clearly, there's a
middle ground that balances cheap development with enough control to assure
compliance with the quality objectives.



Battleground
------------



This conflict is played out daily, and is often surfaced when we try to implement
something "big" like a data warehouse.  The daily cheap vs. control conflict is
a kind of political and philosophical battleground, where strange positions
arise.



IT people, as a class, seem to crave control.
"We can't give the user's ad-hoc access to the data," I was told.



"Why not?" I asked.  "It's their data."



"You don't know our users," they said.
The implication was that their users were particularly malicious and
couldn't be trusted.



"Do they extract data and put it into spreadsheets?" I asked.



This lead to a firestorm of complaining.  Of course they put stuff in spreadsheets.
Of course, they massaged it.  It just proves that they can't be trusted with something simple,
flexible and open.



Or does it prove that?
----------------------



My position was that
users work around an application because the app imposes
*too much*  control.  In the effort to implement
"controls", we often go way too far into creating "idiot-proof" transactions
based on specifications written by
idiots.



Generally, it is simple
ignorance of special cases or planned strategic changes.  With a gap in the
detailed knowledge of what is really done on a daily basis, the business analyst
writes a detailed workflow.  Users (or user management) with similar gaps work
to "tighten" the workflow to control things, eliminating any possibility of
non-compliant behavior.  



Then, when the special cases are finally located (or the planned change occurs), the
software has imposed too many of the wrong kinds of controls.  It requires
rework or replacement.



Why is control bad?
-------------------



Control, *per se* , isn't bad.  What's bad is inflexible,
unrealistic control.  In many cases, it is merely an illusion of control, since
we can download to a spreadsheet and work around the controls anyway. 




What's more valuable than control is
transparency.  We really need to know the who-what-when-where-how-why of each
business event.  The bulk of application software **should**
be nothing more than structuring the details for easy analysis. 




Generally, the complex piece is the *what*
part of the problem.  When we're implementing a small application to prevent the
help desk from being flooded <{filename}/blog/2006/01/2006_01_20-stating_the_problem.rst> with activation requests, we have to avoid
the urge to build bewilderingly complex workflows and data structures.  The
context of the work is an activation request -- it has a few relevant attributes
-- the real *what* of the work is a review, an approve, a deny, a question, an answer, that kind of
thing.



Both things (the activation
request and the various activities that lead to approval or denial) can be made
simple.  Once stripped down to the bare data elements, the 20-minute design
discipline can be applied to build the smallest application that
captures the **Information**, the **Decision** and the **Action**.




What if I need control?
-----------------------



If you really need control, you have to reward the behavior you want to see.  A generous software
development budget doesn't give you any useful level of control if you don't
have the rewards in place.



The saddest thing is a reward system (either formal or cultural) that reinforces behavior
that is obviously not compliant with the design of the software. 




I hear this kind of thing: "Those
labor records can't be reconciled correctly, so we do that manually in a spreadsheet."



This means that the people are rewarded for "reconciling" those labor records in a way that the
application software doesn't support.  Why are they rewarded for this?  Why
doesn't the software do this correctly?  As you dig into this, the executives
claim it isn't happening, or shouldn't be happening.  The people doing it,
however, are really doing the work every week.  In the middle, some manager is
rewarding the work; or the executive isn't aware of the value produced by the
organization.



Software won't help solve
the problem.  The process of business analysis, however, will at least identify
the problem and start a useful discussion.  This can lead to beneficial business
changes, or a simplification in the software so it will support the necessary
flexibility.



I'm advocating removing
control and removing features to improve flexibility.  This is hard to do, but
really serves the users in the best possible way.  I applaud looking for the 20
minute solution.









