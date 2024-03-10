Rewrites are NOT hazardous
===================================================

:date: 2024-02-06 08:01
:tags: test-driven reverse engineering,refactoring,legacy-code,estimating
:slug: 2024-02-06-rewrites_are_not_hazardous
:category: Management
:status: published

First, read this: `Hazards And Safeguards for Software Rewrites <https://www.industriallogic.com/blog/rewrites-hazardous/>`_.
This is an infuriating article. The first part is nonsense. I wonder if it's intended to be read ironically?
Maybe it's a list of bad ideas?
Skip straight to the **Safeguards for Rewrites** section. It's really good.

Also, this `Characterization Testing in Nuclear Power and Software <https://www.industriallogic.com/blog/characterization-testing-in-nuclear-power-and-software/>`_.
This is really good. I used to call it "Test-Driven Reverse Engineering." It's how you manage a rewrite.
Can endorse as a risk mitigation strategy for everyone who has legacy code.

BLUF
----

Rewrites are not hazardous. Ignore the "hazards" part of the article.
This part is infuriatingly full of talking points that make precious little sense.

It's **managing** the rewrite that can become hazardous when managers utterly fail to acknowledge the accrued costs and risks of legacy software.

Ignore the first part of the article. Skip to the **Safeguards for Rewrites** section.

Hazards? Really?
------------------

The article leads with four issues.
It's not clear if this is intended as a list of bad arguments against a rewrite or simply ironically wrong statements.

It says "Here are typical issues you’ll encounter:" as if these are real hazards.
I think these are nonsense things commonly stated as arguments to avoid or prevent a rewrite.
I think -- maybe -- these are issues people raise to avoid talking rationally about a rewrite.

This is what's infuriating about the article. The second half is really good. The first half is hard to interpret.

My working concept is the first half is "farcical hazard statements" not real hazards.

If I read these are specious, bad rationale for **Business as Usual** and **Keep The Lights On**, then,
it makes a little sense.
I've added refutations here, because the original article doesn't directly refute them, it just states them as if they're real hazards.

-   "100% feature matching is difficult." It's actually quite easy. Read the companion piece. Skip to the **Safegaurds** section.
    It's also undesirable. As noted later in the article, this should never have been a goal.

-   "You risk building the new system as poorly as the old system." This is only true if you have the same inept management and insane budgeting as the original.
    You'd also need to have the same language, frameworks, and lack of knowledge.

    Let me emphasize this last point: **lack of knowledge.**  The team writing the legacy code was feeling their way along in the
    dark. That's emphatically no longer true. The legacy system lights the path.

-   "It’s easy to underestimate the effort." This is always true. It's particularly true when management ignores
    the dollars poured into maintenance and support. More than once, I've been told that some 10-year-old spaghetti-bowl
    of legacy code was written by 4 people in 13 weeks. Somehow, the ensuing 10 years vanished.

-   "Tension may build between the rewrite team and the support team."
    I don't see much refutation, perhaps another article?
    I've encountered this, and seen people resign rather than be involved in replacing code they've spent their entire career maintaining.

Let's go on. There's more to the hazards section.

More Hazards
-----------------

Again, the following hazards are mostly bunk. Let's assume they're actually bad arguments against a rewrite.
The article doesn't refute these in detail, instead it skips on to the **Safeguards for Rewrites** section.
I feel the need to refute them in detail.

-   "If you miss an oft–used feature, you’ll injure your users." Right. And? What if the legacy software lacks features?
    The decision to invest in risky, buggy legacy code vs. a rewrite is nothing more than accepting high levels of risk.

-   "Ensuring you have duplicated all the features..." was never a goal.  Some legacy features are trash.
    One of the reasons for a rewrite is to purge obsolete junk code.

-   "No matter how difficult refactoring may appear, rewriting will be worse." False. They're the same thing.
    A rewrite **is** refactoring. It's refactoring with fewer constraints. It's still bound by the lessons learned
    creating the original software.  Remember. The **knowledge** gained means a rewrite has a solid footing for designing software.

-   "I’ve seen over and over again, ..., developers copying and pasting code from the existing system..."
    That's some poor management. What was the incentive that made this appealing to the developers?
    Later, talking about a C++ to Java conversion, the author suggests the "code complete" was somehow a goal.
    If so, that's bad management.

    Also. Most rewrites are not between two languages as similar as C++ and Java.
    Rewriting COBOL to Python can't invoplve copy-and-paste.

-   "It is safest to estimate that the rewrite will take similar effort as the original."
    This doesn't make too much sense.
    First, the original cost is both some original project **plus** years and years of maintenance.
    Further, the original project often had quite a bit of preliminary analytical work to refine the scope to something
    that could be budgeted. This labor is almost **never** accounted for.
    The time users spent helping to understand user stories? Was that part of the development budget also?
    The rewrite will be less than the total of development + maintenance.

-   "Any time saved during development will likely be lost to making sure the new system is feature complete."
    This doesn't make any sense at all. Development is development. It's all development until things are feature complete.
    There's no "time saved" if it's not feature complete.

-   "The usual strategy is a big bang replacement..." Okay. So that's a bad idea.
    The **Safeguards for Rewrites** clearly serves to refute this.

This "Hazards" section is infuriating because the tone is opaque.

Let's assume these are all bad arguments against a rewrite.
Let's call them "Farcical Non-Hazards" or "Things commonly cited as hazards" or something that clarifies
the tone.

The next section is a **much** more useful.

Safeguards for Rewrites
-----------------------

Instrumentation and collect usage statistics.

A CI/CD pipeline to allow incremental delivery.

Incremental conversion working down from the highest priority until the users stop demanding legacy features.

This is good stuff.

Summary
-------

Two of the three points in the summary are excellent.

The first bugs me.

"A complete rewrite of an existing application or system should be your last choice" is hardly worth repeating.
It's a simple cost-risk decision, and it's **always** on the table.

With extremely rich open-source ecosystems around languages like Python, the cost to rewrite
can be surprisingly low.

A super-fancy "analytical app" in an old Visual Basic program may have been reduced to a tidy
Java Spring Boot application that did some flexible analytical computations.
This may reduce, yet again, to an extract and a Jupyter Notebook handed over to skilled users.
The volume of code went from thousands of lines of VB to hundreds of lines of Java to a data dictionary
and a training class.

