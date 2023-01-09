Regular Expression "Hell"
=========================

:date: 2015-05-26 08:00
:tags: regular expressions
:slug: 2015_05_26-regular_expression_hell
:category: Technologies
:status: published


Actual quote:

    "they spend a lot of time maintaining regular
    expressions. So, what are the alternatives to regular expression
    hell?"

Regular Expression Hell? It's a thing?

I have several thoughts:

#.  Do you have metrics to support "a lot"?  I doubt it. It's very
    difficult to tease RE maintenance away from code maintenance. Unless
    you have RE specialists. Maybe there's an RE organization that
    parallels the DBA org. DBA's write SQL. RE specialists write RE's. If
    that was true, I could see that you would have metrics, and could
    justify "a lot." Otherwise, I suspect this is hyperbole. There's
    frustration, true.

#.  REs are essential to programming.  It's hard to express how
    fundamental they are. I would suggest that programmers who have
    serious trouble with RE's have serious trouble with other aspects of
    the craft, and might need remedial training in RE's (and other
    things.) There's no shame in getting some training. There are a lot
    of books that can help. Claiming that there's no time for training
    (or no budget) is what created RE Hell to begin with. It's a trivial
    problem to solve. You can spend 16 hours fumbling around, or stop
    fumbling, spend 16 hours learning, and then press forward with a new
    skill. The choice is yours.

#.  REs are simply a variant on conventional set theory. They're not hard
    at all. Set theory is essential to programming, so are RE's. It's as
    fundamental as boolean algebra. It's as fundamental as getting a loop
    to terminate properly. It's as fundamental as copy-and-paste from the
    terminal window.

#.  REs are universal because they solve a number of problems better than
    any other technology. Emphasis on better than ANY alternative. RE's
    are baked into the syntax of languages like awk and perl. They're
    universal because no one has ever built a sensible alternative. If
    you want to see even more baked-in regular expression goodness, learn
    `SNOBOL4 <http://www.snobol4.org/>`__.


REs are essential. Failure to master REs suggests failure to learn the
fundamentals.

RE Hell is like Boolean Algebra Hell. It's like Set Theory Hell. It's
like Math Library Hell. It's like Uninitialized Variables Hell. These
are things you create through a kind of intentional ignorance.

I'm sorry to sound harsh. But I'm unsympathetic.
The initial regex in question?

::

    r"[\( \
    \$ \
    \/ \|]"

This
indicates a certain lack of familiarity with the basics. It looks
like it started as ``r"\(|\$|/"`` and someone put in spaces (perhaps
they intended to use the verbose option when compiling it) and/or
wrapped the whole in ``[]``\ 's. After trying the ``[]``\ 's, it appeared to work
and they called it done.
The email asked (sort of trivially) if it was true that the last pipe
was extraneous. Um. Yes. But.

**Follow-up**

The hard parts are (1) trying to figure out what the question really
is. Why did they remove just the last pipe character? What were they
trying to do? What's the goal? Then (2) trying to figure out how much
tutorial background is required to successfully answer whatever
question is really being asked. A response of ``r"[\(\$/]"`` seems like
it might not actually be **helpful**. Acting a magic oracle that
emits mysterious answers would only perpetuate the reigning state of
confusion.

The follow-up requests for clarification resulted in (1) an
exhaustive list of every book that seems to mention regex, (2) a user
story that was far higher level than the context of regex questions.
It's difficult to help when there's no focus. Every Book. Generalized
"matching" of "data."

The Python connection? Can't completely parse that out, either, It
appears that this is part of an ETL pipeline. I can't be sure because
the initial user story made so little sense.

Attempts to discuss the supplied user story about "matching" and
"data" -- predictably -- lead nowhere. It was stopped at "Some of the
problems ... aren’t just typos and misspellings." Wait. What? What
are they then? If they're not misspellings, what are they? Fraud?
Hacking attempts? Denial of Service attacks by tying up time in some
matching algorithm?

It's a misspelling. It can't be anything else. Ending the
conversation by claiming otherwise is a strange and self-defeating
approach to redesigning the software.

**More Follow-up**

At this point, we seem to be narrowing the domain of discussion to

    "As time goes on, we have accumulated a lot of the 'standard
    mistakes'. The question that need help w/ [*sic*] is how to manage
    all the code for these 'common mistakes'?"

This question was provided
in lieu of an actual user story. Lack of a story might mean that
we're not interested in actually solving the data matching problem.
Instead we're narrowly focused on sprinkling Faerie Dust all over the
regexes to make them behave better.

They don't want an *alternative* to regexes because the problems
"aren't just typos and misspellings." They want the regex without the
regex hell.





