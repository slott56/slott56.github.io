End User Programming -- Solution or Nuisance?
#############################################

:date: 2010-08-09 08:00
:tags: complexity,software process improvement,#python
:slug: 2010_08_09-end_user_programming_solution_or_nuisance
:category: Technologies
:status: published

The question of "customization" and "extension" is a common one. For
example, "non-technical users to be able to extend with simple scripts".

Read this question on Stack Overflow: "`Programming / scripting
language aimed at non-technical
people <http://stackoverflow.com/questions/3410958/programming-scripting-language-aimed-at-non-technical-people>`__".

This is -- at best -- little more than an attractive nuisance. At
worst, of course, it turns into a maintenance nightmare and the
reason for killing the project. Let's look at the ways this can end
badly.

1.  Your "end users" can't or don't customize it with small scripts.
    Bottom line: you wrote a scripting interface which only you can use.
    Not all bad, but hardly worth the effort. Here's `one
    version <http://www.robelle.com/smugbook/laws.html>`__ of rule: "Make
    it possible for programmers to write in English and you will find
    that programmers cannot write in English."

2.  Your "end users" turn into the worst kind of hackers and break
    things left, right and center. Bottom line: you spend more time
    debugging the messes created by scripting.

3.  The real world use cases turn out to be more complex than you
    bargained for. You spend endless time extending and modifying the
    scripting support to try and balance limited power (to prevent
    problems) against enough sophistication (to handle unforeseen use
    cases.)

"Well," you argue, "those are extreme cases. There has to be a middle
road where the user's behave properly." No, not really. This middle
road doesn't exist. Why? Programming is hard. A phrase like "simple
scripts" is contradictory.

War Story I -- The SAS Hacks
----------------------------

At one organization, the accountants had created a monster. Their
chart of accounts in the General Ledger (GL) was not consistent
across all of the organizations. Consequently, financial analysis
programs required careful rearrangement of certain ledger totals to
make them reflect the business reality, not the legacy GL mistakes.

So they wrote some "simple" business rules in SAS do GL extracts. The
extracts which were processed by these rules were useful for
financial reporting because the legacy GL work-arounds were properly
allocated.

Our job was to write a proper financial reporting tool that correctly
extracted and reported on ledger data. It was going to be a proper
data warehouse. The facts were amounts, the various dimensions were
time, account, organization, bank product line, etc.

However, because of the SAS hacks, we could not get a single straight
answer to any question. Everything had to be explained by a "here's
some code" answer. Their business rules numbered over 9,000
individual simple statements.

Question: How is 9,000 of anything "simple"? Answer: it isn't. The
volume makes it complex.

Further -- of course -- the business rules were actually more complex
than claimed. The superficial claim was that the rules implemented
line-of-business (separate from organization) rules. Some statistics
showed that the rules likely contained two independent dimensions of
each amount.

The "simple" rules were used to create huge complexity. It's human
nature. The world is complex; we want to write software which
reflects the world as we encounter it.

War Story II -- The MS Access Hack
----------------------------------

At another organization, we had helped the end users buy really nice
reporting tools from
`Cognos <http://www-01.ibm.com/software/data/cognos/>`__ (before they
became part of IBM) and `Business
Objects <http://www.sap.com/solutions/sapbusinessobjects/index.epx>`__
(before they became part of SAP). The tools were -- at the time --
the state of the art in flexible end-user reporting. Cool
drag-and-drop interfaces, flexible scripting add-on capabilities.
Really sweet.

Did the users actually use this power?

No.

They wrote dumb, large, detail-oriented reports. They extracted the
bulk data into MS-Access Databases. Then they hacked around in
MS-Access to produce the reports they wanted.

Why? (1) They understood Access; learning to use Cognos or BO tools
wasn't going to happen. (2) They wanted real power; the limited
scripting capabilities weren't solving their problems.

The reason we became involved was because their Chief Access Hack
(CAH™) got another job and no one could figure out how the Access
stuff worked.

After two weeks of reverse engineering, I found a bunch of business
rules that should have been in the data warehouse. We had a nice
meeting with their executive; we wanted to talk about the CAH and
what they were going to do to prevent this kind of MS-Access
nightmare in the future.

The executive reminded us that business rules are subtle and complex.
Data warehouse software development is slow and clumsy. The users
will always be several steps ahead of the warehouse processing. The
MS-Access hacking is how they coped with the limitations of the
warehouse.

Bottom Lines
------------

Software is complex. We can't create a language suitable for
"non-technical users". Either the language is too technical for our
users -- and it isn't used -- or the users become technical and
demand more features.

People learn. They're only non-technical users on day 1. If they
start using the scripting language, they immediately start on the
path to become technical users.

The real world is complex. There are no "simple scripts" except in a
few textbook cases. When we first set out to build our simple
scripting environment, we start with a few sensible use cases. Then
unforeseen use cases crop up and we either tell people they can't use
our system [*Really, would you turn them down?*] or we have to add
complexity.

Architectural Implications
--------------------------

Because of this complexity issue, avoid some urges to refactor. Not
all refactoring is good refactoring. There is `A Limit to
Reuse <{filename}/blog/2010/05/2010_05_10-a_limit_to_reuse.rst>`__.
Specifically, any attempt to create plug-in scripting into a larger
application rapidly becomes hard to manage. It's better to provide
necessary libraries to build applications around a script than to
plug a script into a standardized application.



-----

To follow the train of thought related to &quot;A ...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-08-15 06:34:18.463000-04:00

To follow the train of thought related to "A Limit to Reuse", check out
"Code Reuse - A Myth ? by Danny Kalev"


There is a third way. At one client, the &quot;pow...
-----------------------------------------------------

Robert Lucente<noreply@blogger.com>

2010-08-09 20:22:17.007000-04:00

There is a third way. At one client, the "power users" did their thing
until the report became "stable". "Stable" was a negotiated definition
on a per report basis between the "power user" and management. Once it
was agreed that the report was "stable", it coded up into the formal
infrastructure. Yes, there were still politics. The "power user" did not
want to give up his baby. Management had to say, go have "another baby".


I am the marketing guy. I agree you're wasting...
-----------------------------------------------------

Unknown<noreply@blogger.com>

2010-08-12 02:23:47.637000-04:00

I am the marketing guy. I agree you're wasting time writing for us end
users. I liken your creative skills to that of an interpreter for a
diplomat. You translate the creative intent of others. Obviously you
couldn't translate for 2 people speaking at the same time. Obviously the
diplomat has no business asking you to teach him the language you've
mastered, as you are busy translating. Which of the diplomat wish to
learn a few light phrases to keep the conversation going shouldn't you
be the able to supply them? Of course problems will occur if you attempt
to teach him how to conduct his efforts, or become overly concerned with
the truth or accuracy of what he says.


I worked to program an online survey system that s...
-----------------------------------------------------

Christian<noreply@blogger.com>

2010-08-18 11:05:51.971000-04:00

I worked to program an online survey system that supports "interludes"
of (type-checked, limited) Python code that can be run between pages
during the survey interview process. The questionnaires are scripted in
a custom language that generates a web-version of the questionnaire so
the users are already programming to an extent. The Python interludes
give them some extra power and creative ability though and have allowed
them to do some things that the questionnaire scripting language doesn't
yet support in a first class way (or may never support, for one-off type
things).


The non-technical should maybe be allowed simple b...
-----------------------------------------------------

Paddy3118<noreply@blogger.com>

2010-08-19 12:55:30.031000-04:00

The non-technical should maybe be allowed simple binary flag
manipulation. Anything beyond that: loops, conditionals, subroutines,
... requires some technical ability.
Maybe a changes to a well commented .ini file is all that could be asked
of the non-technical user.
- Paddy.





