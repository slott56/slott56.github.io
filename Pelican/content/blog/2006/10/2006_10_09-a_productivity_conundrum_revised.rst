A Productivity Conundrum (Revised)
==================================

:date: 2006-10-09 10:24
:tags: books,building skills,#python
:slug: 2006_10_09-a_productivity_conundrum_revised
:category: Books
:status: published





In one case, the prospect had 7 interlocked
databases, and wanted to do a technology upgrade.  In other cases, the numbers
was larger (up to 30, I think) but the problem was the same. 




Essentially they said "It's taking us
forever to rework this design.  What should we do that will get the job done
quickly?"



I thought I had a good
answer, but no one liked it.  So, I guess I'm barking up the wrong tree.  Or,
possibly, I'm not reinforcing their idea with an incremental improvement.  It
may be possible that what I'm suggesting is too foreign to make sense to
them.



The first key point is that they
grew the tangle of databases organically.  Each situation is a series of
short-sighted decisions that didn't reach a tipping point until it was a massive
problem.



**Failure of Foresight.** 



How did they get so far afoul of a
good, simple, usable database architecture?  This is the important question, and
I think, holds the key to understanding a lot of the cost and complexity that
seems to be associated with IT.  However, I just can't understand how anyone can
fail to foresee the consequences of a decision that creates complexity.




Somehow managers were able to convince
themselves that adding the seventh database was simpler than reworking the six
existing, complex, hard-to-manage databases.  Clearly, the short-term expedient
("just add more junk") trumped the desire to control cost and
complexity.



Working backwards to root
causes, this decision was made the same way each time it came up.  Every
opportunity to simplify was replaced with an increase in
complexity.



**What Changed?** 



Why do they now ask for help in
simplifying?  it's hard to say and I'm reluctant to ask.  Generally, I get hints
like "it finally got too complex" or "it finally won't scale" or "someone left"
or "someone new came on board."  But I think these aren't the whole story, I
think they're excuses; or perhaps
apologies.



They ask for help because
re-engineering all those short-term-expedient decisions is really hard to do. 
Faced with large and complex data structures, you don't really know where to
begin.  Everyone dives into their area of expertise and wants to rework a small
piece of the problem into something more useful and functional.  No one ever
seems to agree, since each person has a different area of
expertise.



My suggestions are pretty
consistent:  "Pick a high-value business process and rework just that."  It will
ripple through the database, but it won't touch everything that's
wrong.



I discourage looking at the
problem too broadly.  If you try to encompass everything in general, you often
wind up doing nothing in particular.  Infinitely broad is the same as infinitely
shallow.



More pragmatically, my second
key point is that they recognize the futility of redesigning the world in a
single pass.  While they know it can't be done, they still hold out hope that I
can help them do it.



Interestingly, I
get complaints when I talk about the incremental approach.  "If we do things in
pieces, we end up with more of the same."  I can only
agree.



**Recognizing Short-Term Thinking.** 



It seems like people are
looking for a way to manage complexity.  The first technique -- re-engineer the
world -- doesn't work.  They want me to sprinkle Faerie Dust™ on their
approach.  I can't see how to do everything any quicker than they are already
doing.  While I -- personally -- can design pretty quickly, it doesn't do an
organization any good, because an organization works at the median speed,
leaving slower people confused and faster people
frustrated.



When I suggest they tackle
complexity incrementally, they can only complain about one of two things.  The
first is an indictment of incremental thinking and the second is an indictment
of "extra" work.  



Incremental thinking
seems to get conflated with short-term thinking, and both are treated with
contempt.  Short-term thinking created the mess.  Incremental thinking cannot --
in any obvious way -- improve on the
situation.



Any effort to manage a huge
effort appears like "extra" work.  We all know that when we are up to our ass in
alligators, we can't waste time draining the
swamp.



This brings us to the third key
point:  viewed from a distance, these are both the responses of people crippled
by short-term thinking.  An incremental approach is an opportunity for
short-term decisions to ruin the design.  Extra work is a short-term cost that
we can't afford.  Therefore, I think the first issue is to recognize the
difference between short-term thinking and incremental
thinking.



**My Burden.** 



It looks like I have two
burdens.  First, to find a tidy metaphor for incremental thinking; a metaphor
that clears up the difference between short-term decisions and long-term,
incremental decisions.  Second, to find a way to query prospects on wether
they're still making short-term decisions, or ready to make incremental
decisions.



Clearly, what they were
doing wasn't working.  Somehow, I need to disturb their thinking so they stop
doing the same thing.  Disturbing their thinking amounts to saying that what
they've been doing hasn't been working.  I've got to pose the question in  way
that makes them say that their current approach can't work.  However, we have to
move beyond the trivial "not working" into the more substantive, "what
constitutes 'working' for you?"



I
suspect that asking them to define qualities or parameters of a better approach
might change the simple refusals into more useful, ongoing conversations.  We're
trying to stop organic growth, we're trying to manage complexity and we're
trying to grow long-term value in stages.  However, not everyone is ready to
give up on things that didn't work.  I think my obligation is to get them ready
to give up on the old ways before offering them something new.




**Addendum.** 



No
sooner do I post this than I see a related note in a post in `Agile
Testing <http://agiletesting.blogspot.com/>`_ , "`The 90-9-1 rule and building an open source
community <http://agiletesting.blogspot.com/2006/10/90-9-1-rule-and-building-open-source.html>`_  ".  This note had a helpful-looking book title:

`Fearless Change: Patterns for Introducing New Ideas <http://www.amazon.com/Fearless-Change-Patterns-Introducing-Ideas/dp/0201741571>`_ .  I found this to be a helpful
coincidence.  Clearly, I need help introducing change.





