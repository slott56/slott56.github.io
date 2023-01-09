Tools Aren't the Answer
=======================

:date: 2006-08-04 10:47
:tags: management
:slug: 2006_08_04-tools_arent_the_answer
:category: Management
:status: published





See `/dev/null <http://jroller.com/page/cpurdy>`_ 's post "`And the Braindead Award goes to... <http://jroller.com/page/cpurdy?entry=and_the_braindead_award_goes>`_ " for an
interesting tale of things that turn up in spite of 100% test
coverage.



Here's the
recap:

1.  They have 100% test coverage.

#.  Yet, they uncovered an error in an abstract superclass. 



How is this possible?  How
was it possible to turn up an untested method in spite of 100% test
coverage?



There's a technicality in
Java that makes some things hard to test.  In this case, a method
(isEmpty()) was
overridden in each subclass.  You can't really test abstract superclasses very
well, you can only test concrete subclasses.  The superclass method was never
used by any concrete subclass, and was never
tested.



So, was the 100% coverage claim
correct?  Here's one comment: "Clearly you did NOT have 100% test coverage,
otherwise that error would have been caught." 




However, I disagree.  I think they
**did**  test
every API that was implemented.   



That
one overridden API could only be tested by creating a concrete subclass with the
purpose of testing superclass methods.   This subclass would be a contrived
beast this isn't deliverable, and only exists because someone concocted it to
exercise the superclass methods. 




Someone would have to understand the
design well enough to build the necessary
**Proxy** 
classes.  This sounds suspiciously complex for any test coverage tool to tangle
with.



**How would they know?** 



How would they know that a
method was always overridden?  What test coverage tool does that analysis? 
Indeed, who knew that analysis even needed to be done in the first
place?



"I believe that we (as an
industry) can get to Zero Defect Software, but do we actually have the tools to
get there today?"  is Purdy's rhetorical
question.



I think the tools can
*never* 
exist to provide the kind of 100% coverage he's looking for.  Why not?  Why
can't we build a perfect unit test tool that absolutely proves our software
works?



The root problem is that we
can't create an automated proof our software works.  By prove, I mean absolute,
iron-bound, 100% proof of correctness.  Why not?  We can't create an automated
proof of loop termination.  



Assume
that HP/Mercury wrote a utility called
"terminates()"
which returned
True if a given
function would terminate.  Assume I wrote a function,
whistle() which
plays a MIDI file using samples of tea-kettle whistles.  Then I wrote this unit
test:

::

    def test_whistler():
        while terminates( test_whistler ):
            whistle( "stars_and_stripes.mid" )



What does
this do?  If the
terminates()
function thinks that
test_whistler()
will terminate, it has to loop forever.  
Contradiction.
Therefore, this
terminates()
function can't exist.



**If they can't know, what can they do?** 



Since
absolute proof can't exist, what can we do?  It has to involve much more than
tools.  It's about people, process, tools, funding and
organization.



People have to care about
perfect software.  People need the skills and education in what's possible and
how they contribute to it.  A ruthless eye for quality is essential. 
Additionally, the empowerment to make change to meet quality objectives is also
a necessary component.



Process is the
most important part.  Tools can't do everything.  Therefore, manual inspections,
walkthroughs and reviews are as important as anything else.  Properly scheduled
reviews are critical; if you are forced to wait a week, you make assumptions and
move on.  It's critical to get feedback early and often, or an assumption
solidifies into design, accretes features and eventually fossilizes into
coprolite.



Funding and Organization
must assure that "shipping something which works", and "passed all the tests",
and "deadlines matter most" are foreign concepts.  Funding should never trump
defect removal by reducing staff, tools or schedule.  The organization,
similarly, should never play the "too busy doing other things" trump
card.



Tools are least important.  Good
tools help, but it's the people and the processes that make a
difference.



**What they did right.** 



Purdy found the defect. 
Therefore, a process worked.  It's hard to say which process, but something
worked.



Purdy says "... we carefully
designed, implemented, tested (100% API coverage!), reviewed, and it still
slipped through" which isn't quite correct.  It didn't slip through.  An
additional review caught it, or we wouldn't have the benefit of the posting and
the lessons learned.



That additional --
possibly informal -- review caught the error.  I guess this means that the
additional review process is important, and should be added to their current
practices.



I say that what they're
doing worked, and they should do more of it.










